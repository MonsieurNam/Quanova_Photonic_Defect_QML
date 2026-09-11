from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from quanova_qml.analysis.summarize import summarize_runs
from quanova_qml.config import load_config
from quanova_qml.data.audit import audit_dataset
from quanova_qml.data.splits import create_splits
from quanova_qml.features.clip import extract_clip_embeddings
from quanova_qml.runner import count_work, run_benchmark, run_shots
from quanova_qml.timing import time_quantum_map
from quanova_qml.verify import verify_project

ROOT = Path(__file__).resolve().parents[2]


def _cfg(path: str):
    return load_config(ROOT / path if not Path(path).is_absolute() else path)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="quanova-qml")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ["audit", "embed", "smoke", "run", "summarize", "verify"]:
        command = sub.add_parser(name)
        default_config = "configs/base.yaml"
        if name == "smoke":
            default_config = "configs/smoke.yaml"
        elif name == "run":
            default_config = "configs/pilot.yaml"
        command.add_argument("--config", default=default_config)
        if name in {"smoke", "run"}:
            command.add_argument("--dry-run", action="store_true")
            command.add_argument("--resume", action="store_true")
    sub.add_parser("shots").add_argument("--config", default="configs/shots.yaml")
    args = parser.parse_args(argv)
    cfg = _cfg(getattr(args, "config", "configs/base.yaml"))
    os.environ.setdefault("TORCH_HOME", str(ROOT / "cache" / "torch"))
    os.environ.setdefault("HF_HOME", str(ROOT / "cache" / "huggingface"))
    os.environ.setdefault("TMPDIR", str(ROOT / "cache" / "tmp"))

    if args.command == "audit":
        summary = audit_dataset(
            ROOT / cfg["project"]["raw_dir"],
            ROOT / cfg["project"]["manifest"],
            cfg["data"]["duplicate_hamming_threshold"],
        )
        split_summary = create_splits(
            ROOT / cfg["project"]["manifest"],
            ROOT / cfg["project"]["splits_dir"],
            cfg["data"]["budgets"],
            cfg["data"]["subset_seeds"],
            cfg["data"]["outer_folds"],
            cfg["data"]["outer_seed"],
        )
        summary["splits"] = split_summary
    elif args.command == "embed":
        summary = extract_clip_embeddings(
            ROOT / cfg["project"]["manifest"],
            ROOT / cfg["project"]["embeddings"],
            cfg["encoder"]["model"],
            cfg["encoder"]["checkpoint"],
            cfg["encoder"]["batch_size"],
        )
    elif args.command in {"smoke", "run"}:
        if args.dry_run:
            summary = count_work(cfg)
        elif args.command == "smoke":
            summary = {
                "verification": verify_project(ROOT),
                "timing_gate": time_quantum_map(cfg, ROOT),
            }
        else:
            summary = run_benchmark(cfg, ROOT, resume=args.resume)
    elif args.command == "shots":
        summary = run_shots(cfg, ROOT, resume=True)
    elif args.command == "summarize":
        summary = summarize_runs(ROOT)
    elif args.command == "verify":
        summary = verify_project(ROOT)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
