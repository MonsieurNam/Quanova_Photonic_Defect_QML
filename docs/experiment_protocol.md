# Frozen experiment protocol

Protocol freeze date: 2026-09-11. Changes made after test inspection must be logged as exploratory.

## Data

NEU-CLS is audited for unreadable files, SHA-256 exact duplicates, perceptual-hash near duplicates,
and conflicting labels. Conflicting groups are quarantined without relabeling. A duplicate group
may occur in only one of train, validation, and test. Five shuffled stratified group folds use seed
42; fold 0 is the pilot. Label budgets per class are 8/4, 16/8, and 32/16 train/validation, with
subset seeds 11, 22, and 33. Budgets are nested within fixed train and validation streams.

The frozen encoder may be evaluated and cached for all images. PCA and every scaler fit only the
training subset. The unused outer-training pool is not used as unlabeled data.

## Feature pipeline

The encoder is OpenCLIP `ViT-B-32`, checkpoint `openai`, with L2-normalized image embeddings. Full
models use a train-fitted standard scaler. Compressed models use train-fitted PCA-5 and a train-fitted
min-max scaler to [-pi, pi]. No CLIP fine-tuning, LoRA, or skip concatenation is used.

Q1 has six modes, two photons, input occupation `[1,0,1,0,0,0]`, encoded modes 0–4, and reference
mode 5. For each map seed, one Haar-random U is used on both sides of phase encoding: `U D(x) U`.
All 21 two-photon Fock probabilities are calculated. The 15 collision-free probabilities are divided
by their acceptance probability to form the feature vector; acceptance is retained separately.
Map seeds are 101, 202, and 303.

## Models and selection

B1/B3 use 12 locked C values. B2/B4 use four C values by three RBF scales. B5/B6/Q1 use four C
values by three feature-map scales. Candidate selection maximizes validation macro-F1. For a random
map family, its candidate score is the mean across all three map seeds; a seed is never selected and
the seeds are not ensembled. Ties prefer lower C, then locked order. The train-fitted selected model
is evaluated without refitting on train plus validation.

One pilot cell therefore has 156 candidate fits and 13 test evaluations. R1 has nine cells: 1,404
fits and 117 evaluations. R4 has 7,020 fits and 585 evaluations including R1. These repeated test
evaluations share outer test data and are not independent experiments.

## Runtime gate and shots

The quantum map is timed on 64 train/validation inputs before viewing test results. A forecast over
six hours switches execution to fold 0, subset seed 11, budget 24, all seven families: 156 fits and
13 evaluations.

Finite-shot R3 uses the ideal-selected Q1 readout at fold 0, seed 11, budget 24. Launched-shot budgets
are 500, 2,000, and 8,000, with five sampling seeds for each quantum map seed (45 evaluations).
Sampling starts from all 21 outcomes and then postselects. Accepted/rejected counts are retained.
Zero accepted outcomes produce an explicit abstention and remain in metrics.
