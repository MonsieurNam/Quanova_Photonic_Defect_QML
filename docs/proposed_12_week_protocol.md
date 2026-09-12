# Proposed 12-week decision protocol

This document defines the prospective decision rule discussed in the interview deck. It is separate from the completed fold-0 pilot protocol in `experiment_protocol.md`.

## Primary comparison

- Input for matched comparison: train-fitted PCA-5 representation.
- Candidate: Q1 fixed photonic feature map with 15 output probabilities and a classical linear readout.
- Matched controls: Random Fourier Features with 15 outputs (RFF-15) and Extreme Learning Machine features with 15 outputs (ELM-15).
- Strong compressed reference: PCA-5 radial-basis-function support vector machine (RBF-SVM).
- Primary metric: macro-F1 on five duplicate-safe outer folds.
- Model selection: validation data only. Each selected fitted pipeline receives one test evaluation on its fold.

## Pre-specified pass routes

**Pass A — accuracy parity**

Q1 reaches within 0.02 macro-F1 of PCA-5 RBF-SVM on at least four of five outer folds at the same label budget.

**Pass B — practical resource value through label efficiency**

Q1 trained with 24 labels per class reaches within 0.02 macro-F1 of PCA-5 RBF-SVM trained with 48 labels per class on at least four of five outer folds, while using:

- no more than 2,000 launched shots per image; and
- a postselection acceptance rate of at least 0.70.

This defines “resource value” as a twofold reduction in labelled examples under explicit photonic sampling constraints. QPU calls, end-to-end latency, and memory remain reported secondary resource measures; they are not allowed to substitute for a failed primary pass rule.

## Stop rule

Stop the application track if neither pass route holds. Also stop if Q1 fails to outperform both matched 15-D controls on at least four of five outer folds. Report such an outcome as technical feasibility without demonstrated practical utility.

## Sequence

1. Weeks 1–2: five-fold replication.
2. Weeks 3–4: PCA, circuit, and measurement ablations.
3. Weeks 5–6: realistic photonic noise and noise-aware training.
4. Weeks 7–8: select and freeze one hardware candidate.
5. Weeks 9–10: remote QPU subset, conditional on prior gates and access.
6. Weeks 11–12: harder-data or independent evaluation, resource accounting, and decision memo.

Thresholds are prospective project criteria, not claims supported by the completed pilot.
