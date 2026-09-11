<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: en-US
- audience: Quandela technical interview panel evaluating application choice, photonic-platform fit, execution discipline, and scientific judgment
- objective: Answer which application to choose, why it fits Quandela, and how to test feasibility within 2–3 months, using the completed pilot as de-risking evidence.
- core_message: Choose few-label industrial defect inspection with a fixed photonic reservoir; the pilot proves technical feasibility and useful signal but not practical advantage, so continue only through a falsifiable multi-fold, noise-aware, simulator-to-hardware plan.
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: briefing, pyramid
- mode_behavior: Use briefing to answer choice, rationale, platform fit, and 12-week approach before showing pilot evidence; use pyramid assertion titles to move from evidence to a conditional decision.

## visual_style
- visual_style: swiss-minimal

## colors
- background: #FBF7EE
- secondary_bg: #EFE6D5
- primary: #1C2D38
- accent: #D84924
- secondary_accent: #2D7A78
- body_text: #222222

## typography
- font_family: Arial, Helvetica, sans-serif
- title_family: Georgia, Times New Roman, serif
- body_family: Arial, Helvetica, sans-serif
- data_family: Consolas, Courier New, monospace
- body: 23
- title: 40
- subtitle: 32
- card_title: 28
- compact_display: 26
- annotation: 18

## icons
- library: tabler-filled
- inventory: tabler-filled/photo, tabler-filled/flask-2, tabler-filled/chart-dots-3, tabler-filled/shield-check, tabler-filled/bulb, simple-icons/github

## images
- neu-crazing: images/neu_cls_crazing.png | source=user | pattern=Equal-height six-sample strip with label below | crop=no-crop
- neu-inclusion: images/neu_cls_inclusion.png | source=user | pattern=Equal-height six-sample strip with label below | crop=no-crop
- neu-patches: images/neu_cls_patches.png | source=user | pattern=Equal-height six-sample strip with label below | crop=no-crop
- neu-pitted: images/neu_cls_pitted_surface.png | source=user | pattern=Equal-height six-sample strip with label below | crop=no-crop
- neu-rolled-scale: images/neu_cls_rolled_in_scale.png | source=user | pattern=Equal-height six-sample strip with label below | crop=no-crop
- neu-scratches: images/neu_cls_scratches.png | source=user | pattern=Equal-height six-sample strip with label below | crop=no-crop
- learning-curve: images/learning_curve.png | source=user | pattern=Dominant full-width evidence field with conclusion callout beside the plot | crop=no-crop
- compression-performance: images/compression_performance.png | source=user | pattern=Large plot paired with a narrow interpretation column | crop=no-crop
- shot-sensitivity: images/finite_shot_sensitivity.png | source=user | pattern=Plot on the left with acceptance/failure callouts on the right | crop=no-crop
- runtime-breakdown: images/runtime_breakdown.png | source=user | pattern=Compact plot nested inside a broader limitations-and-readiness page | crop=no-crop

## page_rhythm
- P01: anchor
- P02: dense
- P03: anchor
- P04: dense
- P05: dense
- P06: dense
- P07: anchor
- P08: dense
- P09: dense
- P10: breathing

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
