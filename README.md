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
- The measured Vietnamese report, interview Q&A, English slide deck, PDF, and speaker notes are complete.
- The ten-slide interview story now answers the application choice, why it fits Quandela, and how a
  gated twelve-week study would reach a go-or-stop decision; the completed pilot is supporting evidence.

## Interview deliverables

- [Editable PowerPoint deck](deliverables/Quanova_Photonic_QML_Interview_Case_Study_20260911.pptx)
- [Presentation PDF](deliverables/Quanova_Photonic_QML_Interview_Case_Study_20260911.pdf)
- [Vietnamese pilot report](reports/pilot_report_vi.md)
- [Vietnamese interview Q&A](reports/interview_qa_vi.md)
- [12-minute delivery runbook](reports/interview_12min_runbook_vi.md)
- [Technical interview drill](reports/technical_interview_drill_vi.md)
- [Proposed 12-week decision protocol](docs/proposed_12_week_protocol.md)
- [English speaker notes](presentation/quanova_interview_case_study_ppt169_20260911/notes/total.md)

The deck contains ten native DrawingML slides with embedded speaker notes. It distinguishes the
completed simulator pilot from the proposed remote-QPU gate and preregisters two continuation paths:
accuracy parity with PCA-5 RBF-SVM across at least four of five folds, or twofold label efficiency
under explicit shot and acceptance constraints. It preserves the measured result without claiming
practical or quantum advantage. Its final package postflight passed, and all slides were rendered
through Microsoft PowerPoint for visual inspection.

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
