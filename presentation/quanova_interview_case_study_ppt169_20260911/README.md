# quanova_interview_case_study

- Canvas format: ppt169
- Created: 20260911

## Directories

- `svg_output/`: raw SVG output
- `svg_final/`: self-contained SVG visual preview; may be inserted manually as an SVG image, but PowerPoint Convert to Shape is unsupported
- `images/`: runtime image pool; converter assets keep their original short filenames when possible
- `icons/`: project icon set — selected library icons copied in (via icon_sync.py) plus any custom icons you add; embedded from here at export
- `notes/`: speaker notes
- `templates/`: project templates
- `live_preview/`: browser preview runtime files and history (lock.json, server.log, edits.jsonl, annotations.jsonl)
- `sources/`: source materials and normalized markdown
- `analysis/`: machine-extracted intermediate analysis (PPTX intake, image_analysis.csv) — the pipeline's canonical must-read source/asset facts
- `validation/`: cold workflow audit log, SVG quality reports, and PPTX postflight audit reports
- `exports/`: final native DrawingML pptx deliverables only (timestamped); `_native_charts_tables.pptx` name with `--native-charts-and-tables`, `_narrated.pptx` name when narration audio is embedded
- `backup/<timestamp>/`: svg_output/ archive (always written in default-flow mode; safe to delete old timestamps)

## Published artifacts

- `../../deliverables/Quanova_Photonic_QML_Interview_Case_Study_20260911.pptx`
- `../../deliverables/Quanova_Photonic_QML_Interview_Case_Study_20260911.pdf`
- `notes/total.md`: complete English speaker notes, split one-to-one into `P01.md` through `P10.md`
- `../../reports/interview_10min_runbook_vi.md`: rehearsal timing, transitions, and cut rules
- `../../reports/quandela_panel_simulation_vi.md`: three-role technical panel simulation and scoring rubric
- `../../reports/technical_interview_drill_vi.md`: concise technical Q&A practice set
- `../../docs/proposed_12_week_protocol.md`: prospective quantitative pass/stop rules

The final SVG quality gate reported zero blocking findings. The native PPTX package passed
postflight with ten slides and ten note pages. Every slide was rendered at 1920×1080 through
Microsoft PowerPoint and inspected. The final narrative separates the completed pilot from the
proposed twelve-week project, identifies MerLin as a second implementation path, and states that
each selected pipeline receives one test evaluation. Slide 4 defines numerical accuracy and
label-efficiency gates; the cover carries the presenter, target role, and interview date; small
accent text uses darker projector-safe red and teal variants.
