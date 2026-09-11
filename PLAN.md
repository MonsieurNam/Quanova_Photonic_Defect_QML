# Implementation checklist

## Interview package

- [x] Create isolated repository and preserve the original research review.
- [x] Lock protocol and predefined model grids.
- [x] Implement dataset audit, duplicate grouping, quarantine, and five outer folds.
- [x] Implement frozen CLIP cache and train-only preprocessing.
- [x] Implement B1–B6 and Q1 with validation-only selection.
- [x] Implement finite-shot postselection with explicit abstention.
- [x] Implement provenance, resume, predictions, metrics, and aggregation.
- [x] Download and audit NEU-CLS.
- [x] Extract CLIP embeddings and record exact package/checkpoint versions.
- [x] Pass smoke tests and Perceval/MerLin numerical comparisons.
- [x] Time 64 train/validation inputs and apply the six-hour stop rule before test access.
- [x] Run full R1 after the timing gate selected `pilot`.
- [x] Run R2 and R3.
- [x] Generate measured tables/figures and Vietnamese pilot report.
- [ ] Generate and visually inspect the English PPTX/PDF and speaker notes.

## Eight-to-twelve-week extension

- [ ] R4: five outer folds with the unchanged R1 matrix.
- [ ] R5: 12 modes, three photons, PCA-11, and matched classical controls.
- [ ] R6: distinguishability, phase error, and photon-loss ablations.
- [ ] R7: frozen remote/QPU verification after access and quota confirmation.
