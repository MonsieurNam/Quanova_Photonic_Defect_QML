<!-- ppt-master-schema: design-spec/v1 -->
# Quandela Photonic Defect QML Interview Case Study - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | Quandela Photonic Defect QML Interview Case Study |
| Canvas Format | PPT 16:9 (1280 × 720) |
| Page Count | 10 |
| Primary Language | en-US |
| Target Audience | Quandela technical interview panel evaluating application choice, photonic-platform fit, execution discipline, and scientific judgment. |
| Communication Intent | Answer which application to choose, why it is promising for Quandela, and how to test feasibility within 2–3 months, using the completed pilot as de-risking evidence. |
| Desired Audience Outcome | The panel can see a concrete application choice, understand the platform rationale and 12-week workplan, and judge the proposal against explicit continue/stop criteria. |
| Core Message / Ask / Action | Choose few-label industrial defect inspection with a fixed photonic reservoir; the pilot demonstrates simulation-pipeline feasibility and useful signal while hardware remains untested, so continue only through a falsifiable multi-fold, noise-aware, simulator-to-hardware plan. |
| Delivery Context | Primarily a presenter-led 12–15 minute technical interview talk; secondarily a concise reader-led review copy for follow-up. |
| Artifact Afterlife | Technical handoff and audit trail linking claims to the repository, measured results, and next-stage protocol. |
| Reading Mode | balanced |
| Content Strategy | Answer-first: application choice → industrial and platform rationale → falsifiable 12-week approach → measured pilot evidence → conditional recommendation. Preserve all claims, caveats, and provenance. |
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
| Accent body | #9B2D17 | Small decision text on paper, beige, or salmon fields |
| Secondary accent body | #1B5756 | Small validation text on paper, beige, or salmon fields |
| Body text | #222222 | Body copy, labels, notes, and source lines |

Use the darker accent-body colors for text at 20 px or smaller on light fields. Keep the brighter accent colors for rules, filled decision blocks, and large display type.

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
| Card title | 28 |
| Compact display | 26 |
| Annotation | 18 |
| Micro annotation / source | 15 |

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
| learning_curve.png | 1904 × 1024 | 1.86 | Show all families across the three label budgets | Result chart | Dominant full-width evidence field with conclusion callout beside the plot | no-crop | user | Existing | `results/figures/learning_curve.png`; directly label Q1, B1, and B4; place remaining controls in a lower-right legend | none | local |
| compression_performance.png | 1904 × 1024 | 1.86 | Isolate the penalty from PCA-5 compression and the remaining feature-map gap | Result chart | Large plot paired with a narrow interpretation column | no-crop | user | Existing | `results/figures/compression_performance.png`; use a lower-left legend with full model names | none | local |
| finite_shot_sensitivity.png | 1684 × 980 | 1.72 | Show finite-shot sensitivity and non-monotonic performance | Result chart | Plot on the left with acceptance/failure callouts on the right | no-crop | user | Existing | `results/figures/finite_shot_sensitivity.png`; preserve error bars and shot labels | none | local |

## IX. Content Outline

### Part 1: Choice, rationale, and platform fit

#### Slide 01 - I would investigate few-label industrial defect inspection with a photonic reservoir

- **Audience move**: From an open application prompt → receiving the application choice and thesis immediately.
- **Layout**: Answer-first cover with the application statement, three rationale cards, and the measured Q1 result as a secondary proof point.
- **Title**: I would investigate few-label industrial defect inspection with a photonic reservoir
- **Core message**: The application addresses costly labels, fits a small fixed photonic feature map, and can be tested rigorously in 12 weeks.
- **Content**: “Real industrial need: scarce expert labels.” “Photonic fit: interference as a fixed nonlinear map.” “12-week test: public data, matched controls, simulator-to-hardware path.” Secondary evidence: “Completed pilot: Q1 0.8708 macro-F1 at 48 labels/class.”
- **Visualization**: Three compact rationale cards feeding a restrained pilot-evidence band.

#### Slide 02 - Why this is a good 12-week feasibility study

- **Audience move**: From hearing the choice → understanding the operational need and why the question is measurable.
- **Layout**: Six NEU-CLS samples across the top; three criteria below: real need, tractable benchmark, leakage-safe evidence.
- **Title**: Why this is a good 12-week feasibility study
- **Core message**: Industrial label scarcity is concrete, the public benchmark is measurable, and duplicate-safe evaluation limits false wins.
- **Content**: “1,800 audited images · six balanced defect classes.” “Expert labels are expensive; the target is useful accuracy from 12 / 24 / 48 labels per class.” “One exact duplicate pair is held in one group; fold 0 has 60 test images per class.” Conclusion: “Real need · accessible data · quantitative decision.”
- **Images**: Use all six neu_cls sample images in class order, fully visible.
- **Visualization**: Sample strip plus three evidence cards.

#### Slide 03 - A small photonic reservoir fits Quandela’s simulator-to-hardware path

- **Audience move**: From application rationale → understanding what runs on the photonic platform and why the architecture is near-term.
- **Layout**: Left-to-right hybrid pipeline with a simulator-to-hardware lane below it.
- **Title**: A small photonic reservoir fits Quandela’s simulator-to-hardware path
- **Core message**: A frozen encoder and compact phase-encoded circuit isolate the photonic feature map and permit staged validation from Perceval to remote hardware.
- **Content**: Frozen OpenCLIP → train-only PCA-5 → phases [−π, π] → six modes / two photons → 15 conditional probabilities → linear readout. “Perceval: Quandela simulation layer, completed.” “MerLin second-implementation cross-check: completed.” “Remote QPU subset: proposed, not yet executed.” Preserve exact numerical verification errors and state that the MerLin check is a separate code path, not external replication.
- **Mathematical content**: U(x)=U D(x) U; phi_Q(x)=Normalize({P(n|x)}).
- **Visualization**: Main pipeline plus three-stage validation rail: Perceval → second implementation → remote QPU.

#### Slide 04 - The feasibility question is deliberately falsifiable

- **Audience move**: From understanding the architecture → seeing exactly what would count as evidence for or against utility.
- **Layout**: Central question, equal-width schematic baseline rows, compact protocol ledger, and two quantitative pass gates plus one stop gate.
- **Title**: The feasibility question is deliberately falsifiable
- **Core message**: At the same PCA-5 input, Q1’s 15-D photonic features must approach PCA-5 RBF-SVM or establish a pre-specified label-efficiency advantage under a bounded shot budget.
- **Content**: Label budgets 12 / 24 / 48; subset seeds 11 / 22 / 33; B1–B6 and Q1; validation-only selection; map seeds averaged, never picked; one test evaluation per selected fitted pipeline. Repeated evaluations share one outer test fold. Define B4 explicitly as PCA-5 RBF-SVM. Pass A: at 48 labels per class, Q1 is within 0.02 macro-F1 of B4 on at least 4/5 outer folds. Pass B: Q1 at 24 labels/class is within 0.02 of B4 at 48 labels/class on at least 4/5 folds, with no more than 2,000 launched shots per image and acceptance rate at least 0.70. Stop if neither criterion holds or Q1 loses to both RFF-15 and ELM-15 on at least 4/5 folds. Define RFF, ELM, and RBF-SVM at first appearance.
- **Visualization**: Question → matched controls → locked test → two decision gates.

#### Slide 05 - The 12-week project starts after the completed pilot

- **Audience move**: From seeing completed pilot evidence → understanding that the proposed project clock begins with the unanswered feasibility work.
- **Layout**: A completed pre-study ribbon above a six-stage proposed timeline, with a deliverable and exit criterion under every stage.
- **Title**: The 12-week project starts after the completed pilot
- **Core message**: The dataset audit, frozen protocol, simulator verification, and fold-0 result are already complete; the twelve weeks are reserved for decision-changing evidence.
- **Content**: Pre-study completed: dataset audit, frozen protocol, simulator verification, fold-0 result. Proposed project: weeks 1–2 five-fold replication; 3–4 PCA/circuit/measurement ablations; 5–6 realistic photonic noise; 7–8 select and freeze the hardware candidate; 9–10 remote QPU subset with raw counts/calibration; 11–12 harder-data or independent replication plus decision memo.
- **Visualization**: Completed-pilot ribbon separated from six proposed milestones; hardware work remains explicitly conditional.

### Part 2: Pilot evidence and diagnosis

#### Slide 06 - The pilot proves useful signal, not competitive advantage

- **Audience move**: From the proposed plan → seeing that an initial de-risking pilot has already been executed.
- **Layout**: learning_curve.png dominates the page with a narrow conclusion column.
- **Title**: The pilot proves useful signal, not competitive advantage
- **Core message**: Q1 improves from 0.7812 to 0.8708 as labels increase, but full CLIP reaches 0.9852.
- **Content**: Q1 0.7812 → 0.7886 → 0.8708; B1 0.9242 → 0.9638 → 0.9852. Means ± sample SD across three subset seeds on one outer fold.
- **Images**: learning_curve.png, fully visible and uncropped.
- **Visualization**: learning-curve=yes as a pre-rendered evidence image; Native-ready: learning-curve=no.

#### Slide 07 - PCA-5 explains most of the gap; the map explains the rest

- **Audience move**: From observing the gap → diagnosing where it appears and which comparative claim survives.
- **Layout**: compression_performance.png on the left; paired difference callouts on the right.
- **Title**: PCA-5 explains most of the gap; the map explains the rest
- **Core message**: PCA-5 accounts for most of the deficit relative to full features; Q1 beats RFF but remains below ELM and PCA-5 RBF.
- **Content**: B1−B3 at 12 / 24 / 48 labels: +0.1018 / +0.0993 / +0.0713. Q1−RFF: +0.3133 / +0.2238 / +0.2307. Q1−ELM: −0.0166 / −0.0432 / −0.0215. Q1−PCA-5 RBF: −0.0507 / −0.0558 / −0.0534.
- **Images**: compression_performance.png, fully visible and uncropped.
- **Visualization**: compression-comparison=yes as a pre-rendered evidence image; Native-ready: compression-comparison=no.

#### Slide 08 - Finite-shot sampling is stable but does not rescue accuracy

- **Audience move**: From diagnosing representation loss → understanding the tested sampling behavior and untested physical effects.
- **Layout**: finite_shot_sensitivity.png left with direct series labels; three shot callouts and a tested/not-tested ledger right.
- **Title**: Finite-shot sampling is stable but does not rescue accuracy
- **Core message**: Performance stays near 0.77 from 500 to 8,000 launched shots, with stable acceptance and no zero-acceptance failure.
- **Content**: Q1 at 24 labels/class on outer fold 0. 500: 0.7662 ± 0.0322; 2,000: 0.7739 ± 0.0308; 8,000: 0.7725 ± 0.0363; acceptance ≈0.754; zero failures across 45 evaluations. The 45 evaluations are 3 map seeds × 5 sampling seeds × 3 shot levels on the same outer test fold. Not tested: loss, phase drift, distinguishability, detector noise, noise-aware training.
- **Images**: finite_shot_sensitivity.png, fully visible and uncropped.
- **Visualization**: shot-sensitivity=yes as a pre-rendered evidence image; Native-ready: shot-sensitivity=no.

### Part 3: Verdict and recommendation

#### Slide 09 - Simulation feasibility is demonstrated; hardware remains untested

- **Audience move**: From individual results → a calibrated feasibility verdict.
- **Layout**: Three evidence tiers across the page with two large runtime KPIs and the scientific-validity constraint below.
- **Title**: Simulation feasibility demonstrated; hardware remains untested
- **Core message**: The simulation pipeline and reproducible workflow are demonstrated; realistic noise and hardware feasibility remain unanswered.
- **Content**: Demonstrated: executable simulation pipeline, simulator consistency, reproducible artifacts. Partially answered: learning signal, paired one-fold comparison, finite-shot sampling. Unanswered: five-fold generalization, realistic photonic noise, remote hardware. Runtime: OpenCLIP 96.57 s; R1 after embeddings ≈59.9 s.
- **Visualization**: Three status tiers plus large measured-runtime KPI cards; no small runtime chart.

#### Slide 10 - Recommendation: continue only through a decision-changing test

- **Audience move**: From the feasibility verdict → receiving a direct recommendation to the research team.
- **Layout**: Three answer statements followed by one large conditional decision gate and the repository handoff.
- **Title**: Recommendation: continue only through a decision-changing test
- **Core message**: Choose the application for its real need and platform fit, but invest further only if stronger evidence can establish utility.
- **Content**: “Choice: few-label industrial defect inspection with a photonic reservoir.” “Why: real label scarcity, compact phase encoding, and a Quandela simulator-to-hardware path.” “Current verdict: feasible in simulation and scientifically interesting; hardware feasibility remains untested.” Continue only if the pre-specified accuracy-parity or label-efficiency gate passes; otherwise report simulation feasibility without utility and stop. Keep the existing repository URL.
- **Visualization**: Answer stack → continue/stop gate → repository handoff.
## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: Write complete English presenter notes for every slide. Lead with the page takeaway, explain the evidence in plain technical language, state caveats where they affect interpretation, expand acronyms on first use, and distinguish measured pilot results from proposed future work. Preserve all numbers and never imply QPU/hardware execution.
- **Total duration**: 10 minutes, including transitions and a short pause before the final recommendation
- **Notes style**: Conversational, technically precise, candid, and suitable for a technical interview panel
- **Presentation purpose**: Answer the Quandela application-choice prompt directly, explain platform fit and the 12-week approach, use the completed pilot as de-risking evidence, and recommend a conditional next step
