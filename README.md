# Photonic quantum reservoir for few-label steel-defect classification

This repository is a reproducible case study for NEU-CLS: a frozen CLIP ViT-B/32 image encoder,
train-only PCA/scaling, matched classical feature maps, and a six-mode/two-photon photonic reservoir.
The pilot is designed to answer whether the 15-dimensional photonic representation is useful under
small label budgets. It is not designed to claim quantum advantage.

## Current status

- Protocol, model grid, run counts, provenance fields, and stop rule are locked.
- Dataset audit and split generation are implemented.
- CLIP extraction, seven model families, ideal simulation, finite-shot inference, resume, result
  aggregation, and Perceval cross-checking are implemented.
- R1, R2, and R3 are complete: 1,428 classifier fits and 164 test evaluations in total.
- The measured Vietnamese report is in `reports/pilot_report_vi.md`; slide production is tracked in
  `PLAN.md`.

## Reproduce

PowerShell, from this directory:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e '.[clip,photonic,dev]'
$env:TORCH_HOME = "$PWD\cache\torch"
$env:HF_HOME = "$PWD\cache\huggingface"
$env:TEMP = "$PWD\cache\tmp"
.\.venv\Scripts\quanova-qml.exe audit
.\.venv\Scripts\quanova-qml.exe embed
.\.venv\Scripts\quanova-qml.exe smoke --dry-run
.\.venv\Scripts\pytest.exe
.\.venv\Scripts\quanova-qml.exe run --config configs/pilot_min.yaml --dry-run
.\.venv\Scripts\quanova-qml.exe run --config configs/pilot_min.yaml --resume
.\.venv\Scripts\quanova-qml.exe shots
.\.venv\Scripts\quanova-qml.exe summarize
.\.venv\Scripts\quanova-qml.exe verify
```

The `pilot`, `full`, and `shots` profiles use the same runner. The Colab notebooks call this CLI;
they do not contain another implementation. Raw images, weights, caches, environments, runs, and
large exports are ignored by Git.

## Evidence boundaries

The same outer test fold is reused across subset and map seeds. Those evaluations are paired
repetitions, not independent datasets. Model selection uses validation macro-F1 only. Preprocessing
is never refit on validation or test data. Hardware results remain a future stage until access,
quota, and the frozen circuit are confirmed.
