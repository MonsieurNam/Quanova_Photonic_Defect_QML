from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import imagehash
import pandas as pd
from PIL import Image
from tqdm import tqdm

from quanova_qml.utils import sha256_file, write_json

IMAGE_SUFFIXES = {".bmp", ".png", ".jpg", ".jpeg", ".tif", ".tiff"}


class UnionFind:
    def __init__(self, values: list[str]):
        self.parent = {v: v for v in values}

    def find(self, value: str) -> str:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: str, right: str) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[max(a, b)] = min(a, b)


def _label_for(path: Path, root: Path) -> str:
    if path.parent != root:
        return path.parent.name
    return path.stem.split("_")[0].split("-")[0]


def audit_dataset(raw_dir: Path, output_csv: Path, hamming_threshold: int = 4) -> dict:
    paths = sorted(p for p in raw_dir.rglob("*") if p.suffix.lower() in IMAGE_SUFFIXES)
    if not paths:
        raise FileNotFoundError(f"No images found under {raw_dir}")
    records: list[dict] = []
    for path in tqdm(paths, desc="Auditing images"):
        record = {
            "sample_id": path.relative_to(raw_dir).as_posix(),
            "path": str(path.resolve()),
            "label": _label_for(path, raw_dir),
            "sha256": "",
            "phash": "",
            "width": None,
            "height": None,
            "valid": False,
            "error": "",
        }
        try:
            record["sha256"] = sha256_file(path)
            with Image.open(path) as image:
                image.load()
                record["width"], record["height"] = image.size
                record["phash"] = str(imagehash.phash(image.convert("L")))
                record["valid"] = True
        # Every decoder/filesystem failure is data quality evidence and must stay in the manifest.
        except Exception as exc:  # noqa: BLE001
            record["error"] = f"{type(exc).__name__}: {exc}"
        records.append(record)

    valid_ids = [r["sample_id"] for r in records if r["valid"]]
    uf = UnionFind(valid_ids)
    exact: dict[str, list[str]] = defaultdict(list)
    hashes: list[tuple[str, imagehash.ImageHash]] = []
    for row in records:
        if row["valid"]:
            exact[row["sha256"]].append(row["sample_id"])
            hashes.append((row["sample_id"], imagehash.hex_to_hash(row["phash"])))
    for ids in exact.values():
        for other in ids[1:]:
            uf.union(ids[0], other)
    for idx, (left_id, left_hash) in enumerate(tqdm(hashes, desc="Near-duplicate scan")):
        for right_id, right_hash in hashes[idx + 1 :]:
            if left_hash - right_hash <= hamming_threshold:
                uf.union(left_id, right_id)

    group_labels: dict[str, set[str]] = defaultdict(set)
    for row in records:
        if row["valid"]:
            row["duplicate_group"] = uf.find(row["sample_id"])
            group_labels[row["duplicate_group"]].add(row["label"])
        else:
            row["duplicate_group"] = ""
    conflict_groups = {group for group, labels in group_labels.items() if len(labels) > 1}
    for row in records:
        row["quarantine"] = (not row["valid"]) or row["duplicate_group"] in conflict_groups

    frame = pd.DataFrame(records)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_csv, index=False)
    summary = {
        "raw_dir": str(raw_dir.resolve()),
        "images_total": len(frame),
        "valid": int(frame["valid"].sum()),
        "quarantined": int(frame["quarantine"].sum()),
        "class_counts": dict(Counter(frame.loc[~frame["quarantine"], "label"])),
        "exact_duplicate_groups": sum(len(v) > 1 for v in exact.values()),
        "near_or_exact_duplicate_groups": int(frame.loc[frame["valid"], "duplicate_group"].nunique()),
        "conflicting_duplicate_groups": len(conflict_groups),
        "hamming_threshold": hamming_threshold,
        "manifest_sha256": sha256_file(output_csv),
    }
    write_json(output_csv.with_suffix(".summary.json"), summary)
    return summary
