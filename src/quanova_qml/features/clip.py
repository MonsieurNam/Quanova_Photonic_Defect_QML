from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image

from quanova_qml.utils import sha256_file


def extract_clip_embeddings(
    manifest_csv: Path,
    output_npz: Path,
    model_name: str = "ViT-B-32",
    checkpoint: str = "openai",
    batch_size: int = 32,
    device: str | None = None,
) -> dict:
    import open_clip
    import torch
    from torch.utils.data import DataLoader, Dataset

    frame = pd.read_csv(manifest_csv)
    frame = frame.loc[(frame["valid"] == True) & (frame["quarantine"] == False)].copy()
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    local_checkpoint = output_npz.parent / "weights" / f"{model_name}.pt"
    resolved_checkpoint = str(local_checkpoint) if local_checkpoint.exists() else checkpoint
    model, _, preprocess = open_clip.create_model_and_transforms(
        model_name,
        pretrained=resolved_checkpoint,
        # The official OpenAI checkpoint is a TorchScript archive. Its SHA-256 is
        # recorded above, so legacy archive loading is deliberate and reproducible.
        weights_only=False,
    )
    model = model.eval().to(device)

    class Images(Dataset):
        def __len__(self) -> int:
            return len(frame)

        def __getitem__(self, index: int):
            with Image.open(frame.iloc[index]["path"]) as image:
                return preprocess(image.convert("RGB")), frame.iloc[index]["sample_id"]

    loader = DataLoader(Images(), batch_size=batch_size, shuffle=False, num_workers=0)
    vectors, ids = [], []
    start = time.perf_counter()
    with torch.inference_mode():
        for images, batch_ids in loader:
            encoded = model.encode_image(images.to(device))
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            vectors.append(encoded.cpu().numpy().astype(np.float32))
            ids.extend(batch_ids)
    output_npz.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "library": "open_clip",
        "model": model_name,
        "checkpoint_tag": checkpoint,
        "checkpoint_file": str(local_checkpoint.resolve()) if local_checkpoint.exists() else None,
        "checkpoint_sha256": sha256_file(local_checkpoint) if local_checkpoint.exists() else None,
        "device": device,
        "seconds": time.perf_counter() - start,
        "count": len(ids),
    }
    np.savez_compressed(
        output_npz,
        sample_ids=np.asarray(ids),
        embeddings=np.concatenate(vectors),
        metadata=np.asarray(json.dumps(metadata)),
    )
    return metadata


def load_embeddings(path: Path) -> tuple[dict[str, np.ndarray], dict]:
    archive = np.load(path, allow_pickle=False)
    metadata = json.loads(str(archive["metadata"]))
    return dict(zip(archive["sample_ids"].tolist(), archive["embeddings"])), metadata
