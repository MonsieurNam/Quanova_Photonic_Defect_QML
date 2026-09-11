<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: en-US
- audience: Quanova technical interview panel evaluating machine-learning rigor, quantum–photonic relevance, and experimental judgment
- objective: Explain the completed pilot and its limits so the panel can assess the contribution and judge whether the focused next-stage experiment is worthwhile.
- core_message: The fixed photonic reservoir is executable and reproducible, but Q1 currently loses to strong baselines; continue only through a targeted falsifiable plan.
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: briefing, pyramid
- mode_behavior: Use briefing to present complete scannable experimental facts and pyramid assertion titles to state the judgment each evidence page supports; move from hypothesis and controls through observations to a conditional decision.

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
- paired-differences: images/paired_quantum_differences.png | source=user | pattern=Full-width evidence panel crossing a neutral zero reference | crop=no-crop
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
