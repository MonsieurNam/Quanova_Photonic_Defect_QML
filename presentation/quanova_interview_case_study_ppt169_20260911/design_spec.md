<!-- ppt-master-schema: design-spec/v1 -->
# Quanova Photonic Defect QML Interview Case Study - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | Quanova Photonic Defect QML Interview Case Study |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 10 |
| Primary Language | en-US |
| Target Audience | Quanova technical interview panel familiar with machine learning and evaluating experimental judgment, quantum–photonic relevance, and engineering rigor. |
| Communication Intent | Explain the proposed hybrid photonic machine-learning pipeline, report the completed pilot honestly, and gain agreement on a focused next-stage feasibility plan. |
| Desired Audience Outcome | The panel can assess the candidate's contribution, understand what the evidence supports, and judge whether the proposed next experiment is technically worthwhile. |
| Core Message / Ask / Action | A fixed photonic reservoir is executable and reproducible, but the current Q1 system loses to strong classical baselines; further work should proceed only through a targeted, falsifiable improvement plan. |
| Delivery Context | Primarily a presenter-led 12–15 minute technical interview talk; secondarily a concise reader-led review copy for follow-up. |
| Artifact Afterlife | Technical handoff and audit trail linking claims to the repository, measured results, and next-stage protocol. |
| Reading Mode | balanced |
| Content Strategy | Balanced: reorganize and distill the source into a decision-oriented experimental audit while preserving all claims, figures, caveats, and provenance. |
| Design Style | Swiss-minimal geometry with a warm lab-notebook palette; custom briefing/pyramid mode that makes every experimental fact scannable and every evidence page conclude with a judgment. |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy |
| Custom Animations | disabled — final Stage-2 proactive policy |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-09-11 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64 px horizontal; 48 px vertical safe area |
| Content Area | x=64–1216, y=48–672 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: briefing, pyramid
- **Mode Behavior**: Use briefing for complete and scannable experimental facts, while pyramid assertion titles identify the judgment each evidence page supports. Organize the deck as hypothesis, controls, observations, interpretation, and decision, with speaker notes carrying nuance and caveats.
- **Visual style**: swiss-minimal
- **Theme**: A clean research notebook translated through strict Swiss grid discipline: warm paper fields, dark ink, exact rules, one oxide-red decision signal, and one muted-teal validation signal.
- **Tone**: Candid, analytical, rigorous, and calm; negative results are treated as useful engineering evidence.

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FBF7EE | Main warm paper field |
| Secondary background | #EFE6D5 | Evidence strips, quiet comparison zones, and chart mats |
| Primary | #1C2D38 | Titles, structural rules, and principal geometry |
| Accent | #D84924 | Decision points, shortfalls, and falsification gates |
| Secondary accent | #2D7A78 | Validation checks, confirmed facts, and viable paths |
| Body text | #222222 | Body copy, labels, notes, and source lines |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | Editorial serif, assertive and compact | Georgia | — | Times New Roman, serif |
| Body | Neutral scientific sans | Arial | — | Helvetica, sans-serif |
| Data | Tabular technical annotation | Consolas | — | Courier New, monospace |

- **Title stack**: Georgia, Times New Roman, serif
- **Body stack**: Arial, Helvetica, sans-serif
- **Data stack**: Consolas, Courier New, monospace
- **Data Role rationale**: Use only for compact codes, seed identifiers, runtimes, and numeric callouts where alignment improves comparison.

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 23 |
| Title | 40 |
| Subtitle | 32 |
| Annotation | 18 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: Assertion title first, then one dominant evidence carrier, then a compact implication or source line.
- **Composition tendency**: Use asymmetric Swiss divisions, one oversized numeral or evidence panel, sparse square-corner containers, and unboxed plots placed directly on the field.
- **Cross-page continuity**: A thin top rule and compact page index recur; oxide red marks evidence against the hypothesis, while teal marks validation or a viable next action. Plot pages share a stable title-and-evidence frame.
- **Spacing posture**: Variable by page rhythm—open on the cover and decision close, compact on method and limitations, and evidence-dense on benchmark pages without falling into repeated equal-card layouts.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-filled
- **Brand-logo library**: simple-icons

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-filled/photo | Dataset and visual-input cue |
| tabler-filled/flask-2 | Frozen experiment and ablation cue |
| tabler-filled/chart-dots-3 | Measured-result and comparison cue |
| tabler-filled/shield-check | Leakage control, reproducibility, and verification cue |
| tabler-filled/bulb | Hypothesis and next-experiment cue |
| simple-icons/github | Repository handoff link on the closing page |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| neu_cls_crazing.png | 200 × 200 | 1.00 | Orient the audience to the crazing class | Dataset sample | Equal-height six-sample strip with label below | no-crop | user | Existing | NEU-CLS `Cr_1.bmp`, converted losslessly to PNG | none | local |
| neu_cls_inclusion.png | 200 × 200 | 1.00 | Orient the audience to the inclusion class | Dataset sample | Equal-height six-sample strip with label below | no-crop | user | Existing | NEU-CLS `In_1.bmp`, converted losslessly to PNG | none | local |
| neu_cls_patches.png | 200 × 200 | 1.00 | Orient the audience to the patches class | Dataset sample | Equal-height six-sample strip with label below | no-crop | user | Existing | NEU-CLS `Pa_1.bmp`, converted losslessly to PNG | none | local |
| neu_cls_pitted_surface.png | 200 × 200 | 1.00 | Orient the audience to the pitted-surface class | Dataset sample | Equal-height six-sample strip with label below | no-crop | user | Existing | NEU-CLS `PS_1.bmp`, converted losslessly to PNG | none | local |
| neu_cls_rolled_in_scale.png | 200 × 200 | 1.00 | Orient the audience to the rolled-in-scale class | Dataset sample | Equal-height six-sample strip with label below | no-crop | user | Existing | NEU-CLS `RS_1.bmp`, converted losslessly to PNG | none | local |
| neu_cls_scratches.png | 200 × 200 | 1.00 | Orient the audience to the scratches class | Dataset sample | Equal-height six-sample strip with label below | no-crop | user | Existing | NEU-CLS `Sc_1.bmp`, converted losslessly to PNG | none | local |
| learning_curve.png | 1904 × 1024 | 1.86 | Show all families across the three label budgets | Result chart | Dominant full-width evidence field with conclusion callout beside the plot | no-crop | user | Existing | `results/figures/learning_curve.png`; preserve axes, legend, and uncertainty marks | none | local |
| compression_performance.png | 1904 × 1024 | 1.86 | Isolate the penalty from PCA-5 compression and the remaining feature-map gap | Result chart | Large plot paired with a narrow interpretation column | no-crop | user | Existing | `results/figures/compression_performance.png`; preserve all labels | none | local |
| paired_quantum_differences.png | 1906 × 1024 | 1.86 | Compare paired Q1 differences against RFF, ELM, and PCA-5 RBF | Result chart | Full-width evidence panel crossing a neutral zero reference | no-crop | user | Existing | `results/figures/paired_quantum_differences.png`; preserve zero line and labels | none | local |
| finite_shot_sensitivity.png | 1684 × 982 | 1.71 | Show finite-shot sensitivity and non-monotonic performance | Result chart | Plot on the left with acceptance/failure callouts on the right | no-crop | user | Existing | `results/figures/finite_shot_sensitivity.png`; preserve error bars and shot labels | none | local |
| runtime_breakdown.png | 1901 × 1024 | 1.86 | Ground the feasibility claim in measured CPU runtime | Result chart | Compact plot nested inside a broader limitations-and-readiness page | no-crop | user | Existing | `results/figures/runtime_breakdown.png`; local CPU profiling only | none | local |

## IX. Content Outline

### Part 1: Hypothesis and controls

#### Slide 01 - A reproducible photonic pilot delivers a useful negative result

- **Audience move**: From expecting a quantum-performance pitch → understanding that the case study demonstrates experimental judgment through a measured negative result.
- **Layout**: Anchor cover with a large `0.8708` Q1 macro-F1 facing `0.9852` for full CLIP + linear regression at 48 labels/class; the title occupies the opposite grid zone, with a small oxide-red delta marker and a restrained subtitle.
- **Title**: A reproducible photonic pilot delivers a useful negative result
- **Core message**: The fixed photonic reservoir runs correctly, yet the current application evidence does not support quantum advantage.
- **Content**: Subtitle: “Few-label steel defect classification · ideal photonic simulation · fold-0 pilot.” Supporting line: “Q1 beats locked RFF, but loses to ELM, RBF-SVM, and full embeddings.” Footer: “Quanova interview case study · 11 Sep 2026.”
- **Visualization**: Native numeric contrast: Q1 `0.8708` vs B1 `0.9852`; the 48-label/class cell is the binding cover hook.

#### Slide 02 - The benchmark starts with 1,800 audited images and a leakage barrier

- **Audience move**: From seeing an abstract QML task → seeing the concrete dataset, label scarcity, and duplicate-aware split discipline.
- **Layout**: Six NEU-CLS samples form a clean horizontal strip; below, one wide factual band holds dataset counts and one compact leakage-control diagram.
- **Title**: The benchmark starts with 1,800 audited images and a leakage barrier
- **Core message**: The comparison uses balanced data and group-safe splits, so duplicate leakage cannot create a false win.
- **Content**: “6 classes · 300 images/class · 1,800/1,800 valid · 0 quarantined.” “One exact duplicate pair: Pa_101 / Pa_105, same label, one group.” “Five StratifiedGroupKFold outer folds, seed 42; pilot uses fold 0 with 60 test images/class.” Source line: `results/tables/dataset_audit.csv`; `docs/experiment_protocol.md`.
- **Images**: Use all six `neu_cls_*.png` samples in class order: crazing, inclusion, patches, pitted surface, rolled-in scale, scratches. Keep every image fully visible.
- **Visualization**: Qualitative flow: image IDs + duplicate groups → stratified group split → disjoint train / validation / test.

#### Slide 03 - The circuit is fixed; only the phase encoding changes per image

- **Audience move**: From knowing the data controls → understanding exactly what is quantum-inspired, what is trained, and what is verified.
- **Layout**: One left-to-right pipeline is the page spine: frozen OpenCLIP → train-only scale/PCA-5 → five phases → `U D(x) U` six-mode, two-photon circuit → 15 postselected collision-free probabilities → linear readout. A compact verification seal sits under the circuit.
- **Title**: The circuit is fixed; only the phase encoding changes per image
- **Core message**: Q1 is a transparent fixed feature map whose probability semantics match two independent photonic libraries at machine precision.
- **Content**: “Input occupation [1,0,1,0,0,0] · encoded modes 0–4 · mode 5 reference · map seeds 101/202/303.” “21 two-photon Fock outcomes → 15 collision-free conditional features; acceptance retained separately.” “Max error vs Perceval 1.2.4: 4.16 × 10⁻¹⁷; vs MerLin 0.4.1: 8.33 × 10⁻¹⁷.” Source: `docs/experiment_protocol.md`; `results/summaries/verification.json`.
- **Mathematical content**: U(x)=U D(x) U,\quad \phi_Q(x)=\operatorname{Normalize}\left(\{P(\mathbf{n}\mid x)\}_{\mathbf{n}\in\mathcal{C}}\right)
- **Visualization**: Qualitative linked process with the same sample token traveling through each transformation; validation callout branches from the probability vector.

#### Slide 04 - The protocol makes overclaiming difficult

- **Audience move**: From understanding the map → trusting that the benchmark compares like with like and freezes model selection before test inspection.
- **Layout**: Dense but scannable audit page: a vertical protocol spine at left, a baseline family ladder in the center, and a large `1,404 fits / 117 evaluations` ledger at right.
- **Title**: The protocol makes overclaiming difficult
- **Core message**: Frozen budgets, paired subsets, train-only preprocessing, and strong baselines create a hard test for utility.
- **Content**: “Budgets per class: 12 / 24 / 48 total labels, split 8/4, 16/8, 32/16 train/validation.” “Subset seeds 11/22/33; map seeds 101/202/303 are averaged, never selected or ensembled.” Baselines: B1 full CLIP + LR; B2 full CLIP + RBF; B3 PCA-5 + LR; B4 PCA-5 + RBF; B5 RFF-15; B6 ELM-15; Q1 photonic-15. “Validation selects hyperparameters; selected train-fitted model is evaluated once without refit.” Source: `docs/experiment_protocol.md`.
- **Visualization**: Qualitative audit trail; nested budget tokens align across all seven families and terminate at a locked test gate.

### Part 2: Observations and interpretation

#### Slide 05 - Q1 improves with labels, but the full embedding stays dominant

- **Audience move**: From trusting the protocol → seeing the primary outcome across all model families and label budgets.
- **Layout**: `learning_curve.png` dominates the page; a narrow conclusion column highlights the 48-label endpoint and the B1–Q1 gap.
- **Title**: Q1 improves with labels, but the full embedding stays dominant
- **Core message**: At 48 labels/class, Q1 reaches 0.8708 macro-F1 while B1 reaches 0.9852.
- **Content**: Pull figures: “Q1 0.7812 → 0.7886 → 0.8708.” “B1 0.9242 → 0.9638 → 0.9852.” Interpretation: “The photonic map learns useful structure, but not enough to justify discarding the full 512-D embedding.” Source: `results/tables/main_results.csv`; means ± sample SD across three subset seeds.
- **Images**: `learning_curve.png`, fully visible and uncropped.
- **Visualization**: `learning-curve=yes` as a pre-rendered evidence image; Native-ready: learning-curve=no.

#### Slide 06 - PCA-5 compression explains much of the distance to the best baseline

- **Audience move**: From seeing Q1 trail B1 → separating the loss caused by compression from the loss caused by the photonic map.
- **Layout**: `compression_performance.png` uses the left two-thirds; the right third decomposes B1→B3 and B2→B4 gaps, then positions Q1 against other PCA-5 models.
- **Title**: PCA-5 compression explains much of the distance to the best baseline
- **Core message**: The bottleneck removes important signal before any nonlinear map is applied.
- **Content**: “B1−B3: +0.1018 / +0.0993 / +0.0713 at 12 / 24 / 48 labels.” “B2−B4: +0.0657 / +0.0872 / +0.0263.” “At 24 labels/class: B3 0.8646, B4 0.8444, B6 0.8318, Q1 0.7886.” Source: `results/tables/compression.csv`; `results/tables/main_results.csv`.
- **Images**: `compression_performance.png`, fully visible and uncropped.
- **Visualization**: `compression-comparison=yes` as a pre-rendered evidence image; Native-ready: compression-comparison=no.

#### Slide 07 - The paired result is specific: Q1 beats RFF, not the strong nonlinear controls

- **Audience move**: From a broad leaderboard view → understanding exactly which quantum claim survives paired comparison.
- **Layout**: `paired_quantum_differences.png` spans the page under the title; the zero line is visually protected, with one teal annotation on positive RFF differences and oxide-red annotations on ELM/RBF shortfalls.
- **Title**: The paired result is specific: Q1 beats RFF, not the strong nonlinear controls
- **Core message**: Q1’s advantage is relative to the locked RFF-15 map; it remains below ELM-15 and PCA-5 RBF at every budget.
- **Content**: “Q1−RFF: +0.3133 / +0.2238 / +0.2307.” “Q1−ELM: −0.0166 / −0.0432 / −0.0215.” “Q1−PCA-5 RBF: −0.0507 / −0.0558 / −0.0534.” Source: `results/tables/paired_differences.csv`; subset-paired descriptive differences.
- **Images**: `paired_quantum_differences.png`, fully visible and uncropped.
- **Visualization**: `paired-differences=yes` as a pre-rendered evidence image; Native-ready: paired-differences=no.

#### Slide 08 - More launched shots do not resolve the model gap

- **Audience move**: From seeing an ideal-simulation shortfall → understanding that finite-shot sampling is stable here but does not create a performance rescue.
- **Layout**: `finite_shot_sensitivity.png` sits left; three aligned shot callouts sit right above an acceptance band and a “0 failures” validation mark.
- **Title**: More launched shots do not resolve the model gap
- **Core message**: Between 500 and 8,000 launched shots, performance stays near 0.77 and is not monotonic.
- **Content**: “500: 0.7662 ± 0.0322.” “2,000: 0.7739 ± 0.0308.” “8,000: 0.7725 ± 0.0363.” “Acceptance ≈ 0.754; 0 zero-acceptance failures across 45 evaluations.” Caveat: “Sampled inference uses the ideal-trained readout; this is not noise-aware training.” Source: `results/tables/finite_shot.csv`.
- **Images**: `finite_shot_sensitivity.png`, fully visible and uncropped.
- **Visualization**: `shot-sensitivity=yes` as a pre-rendered evidence image; Native-ready: shot-sensitivity=no.

### Part 3: Decision and next experiment

#### Slide 09 - The simulator is fast enough; scientific validity is the real bottleneck

- **Audience move**: From focusing on model scores → distinguishing computational feasibility from unresolved hardware and generalization risk.
- **Layout**: The page divides asymmetrically: `runtime_breakdown.png` and two measured runtime figures on the left; a descending uncertainty ladder on the right moves from validated simulator semantics to untested hardware effects.
- **Title**: The simulator is fast enough; scientific validity is the real bottleneck
- **Core message**: Runtime supports broader experiments, but one outer fold and ideal optics limit what the result can claim.
- **Content**: “OpenCLIP extraction: 96.57 s on CPU.” “Instrumented R1 after embeddings: ≈59.9 s; Q1 candidate fitting/validation ≈26.0 s; Q1 test inference 8.37 s.” Limits: one outer test fold; small validation cells; B1 near ceiling; no loss, distinguishability, phase drift, detector noise, or QPU queue; acceptance ≈0.74; no deployment-population confidence interval. Source: `results/tables/compute_cost.csv`; `reports/pilot_report_vi.md`.
- **Images**: `runtime_breakdown.png`, contained within its evidence region and fully visible.
- **Visualization**: `runtime-breakdown=yes` as a pre-rendered evidence image; Native-ready: runtime-breakdown=no. Qualitative uncertainty ladder: simulator correctness → repeated subsets → outer-fold generalization → realistic photonic noise → hardware execution.

#### Slide 10 - Continue only if a falsifiable gate can change the decision

- **Audience move**: From accepting the limitations → agreeing on a disciplined 8–12 week plan and a clear stop condition.
- **Layout**: Breathing close with a four-stage horizontal path and a large conditional gate at the end; the GitHub repository link sits as a compact handoff object, not a generic thank-you.
- **Title**: Continue only if a falsifiable gate can change the decision
- **Core message**: Scale the experiment only if Q1 closes the ELM/RBF gap across outer folds or demonstrates a valuable resource tradeoff.
- **Content**: “Weeks 1–2: run the frozen five-fold R4 protocol.” “Weeks 3–4: diagnose PCA-5 loss; preregister circuit/measurement ablations.” “Weeks 5–6: add distinguishability, phase error, loss, and detector effects.” “Weeks 7–8: remote simulator/QPU subset with raw counts and calibration.” “Weeks 9–12: harder dataset or independent replication.” Stop condition: “If Q1 only beats RFF while B1/ELM/RBF stay better, report hardware feasibility without an application utility case.” Handoff link: “Repository: https://github.com/MonsieurNam/Quanova_Photonic_Defect_QML”.
- **Visualization**: Qualitative staged path with an oxide-red decision gate and two terminal outcomes: “utility evidence” or “feasibility-only conclusion.”

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: Write complete English presenter notes for every slide. Lead with the page takeaway, explain the evidence in plain technical language, state caveats where they affect interpretation, expand acronyms on first use, and distinguish measured pilot results from proposed future work. Preserve all numbers and never imply QPU/hardware execution.
- **Total duration**: 12–15 minutes
- **Notes style**: Conversational, technically precise, candid, and suitable for a technical interview panel
- **Presentation purpose**: Explain the system, report and account for the completed pilot, demonstrate experimental judgment, and align on a conditional next-stage feasibility plan
