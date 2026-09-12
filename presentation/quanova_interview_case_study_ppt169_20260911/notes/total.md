# 1_I would investigate few-label industrial defect inspection with a photonic reservoir

Good afternoon. I am Nguyen Ngo Nhat Nam. I would investigate few-label industrial defect inspection with a fixed photonic reservoir. Expert labels are costly, interference offers a compact nonlinear map, and the question can be tested in twelve weeks with public data, matched controls, and a simulator-to-hardware path. My completed pilot reached 0.8708 macro-F1 at forty-eight labels per class. That demonstrates useful signal in simulation, not practical or quantum advantage. The choice matters only if the constraint is real and the test is measurable.

---

# 2_Why this is a good 12-week feasibility study

The operational constraint is label scarcity: inspection images may be plentiful, while reliable labels require expert time. NEU-CLS provides 1,800 audited images across six balanced defect classes, so the study can begin without proprietary collection. The exact duplicate pair Pa_101 and Pa_105 remains in one group, and the pilot test fold has sixty images per class with no overlap. The application therefore has a real need, accessible evidence, and a measurable failure condition. Now I will show where photonics enters.

---

# 3_A small photonic reservoir fits Quandela’s path to hardware

A frozen OpenCLIP encoder produces an embedding. Train-only principal component analysis reduces it to five phase values. A fixed six-mode, two-photon circuit maps them to fifteen postselected probabilities for a linear readout. Only the readout is trained, which isolates the feature map. Perceval is the primary simulation path; MerLin reproduces the ideal probabilities to machine precision through a separate code path, not external replication. Remote QPU execution remains untested and conditional on access and prior gates. A runnable simulation is only a starting point, so I need a rule that can reject it.

---

# 4_The feasibility question is deliberately falsifiable

From the same PCA-five input, can Q1 beat matched fifteen-dimensional controls and approach PCA-five RBF-SVM? RFF means random Fourier features; ELM means extreme learning machine. I preregister two pass routes. Pass A: at forty-eight labels per class, Q1 is within 0.02 macro-F1 of RBF-SVM on at least four of five folds. Pass B: Q1 at twenty-four labels reaches the forty-eight-label RBF-SVM within 0.02 on four folds, using at most two thousand shots per image and acceptance of at least 0.70. I stop if neither passes, or Q1 loses to both RFF-15 and ELM-15 on four folds. These gates define the proposed project; the pilot is already complete.

---

# 5_The 12-week project starts after the completed pilot

The pilot is pre-study evidence and does not consume the project clock. Weeks one and two replicate five outer folds. Weeks three and four ablate PCA, circuit, and measurement choices. Weeks five and six add realistic photonic noise. Weeks seven and eight freeze one hardware candidate and its resource definitions. Weeks nine and ten run a remote subset only if prior gates pass. Weeks eleven and twelve use harder data or independent replication and produce the decision memo. Here is what the pilot actually found.

---

# 6_The pilot shows useful signal—not competitive advantage

Q1 rises from 0.7812 to 0.7886 and then 0.8708 as the label budget grows. The full OpenCLIP linear baseline starts at 0.9242 and reaches 0.9852. Each point averages three subset seeds, but every point reuses one outer test fold. The correct conclusion is limited: Q1 contains useful class information in this simulation pilot, while the current map is not competitive with the full representation. The controlled comparison shows where that gap comes from.

---

# 7_Compression—not photonics alone—explains the shortfall

PCA-five costs the linear baseline about 0.07 to 0.10 macro-F1, so important information is lost before the nonlinear comparison. Within the compressed setting, Q1 beats the locked RFF-15 comparator by 0.22 to 0.31. It still trails ELM by about 0.02 to 0.04 and PCA-five RBF-SVM by about 0.05 to 0.06. I would therefore vary representation size and circuit design separately rather than attributing the whole gap to photonics. Before proposing hardware, I also tested whether sampling is stable.

---

# 8_Finite-shot sampling is stable; accuracy does not recover

Macro-F1 remains near 0.77 from five hundred to eight thousand launched shots. Each level contains three map seeds times five sampling seeds; all forty-five evaluations share one outer test fold. Acceptance stays near 0.754 with no zero-acceptance failures. More shots do not recover accuracy, so sampling noise is not the main limitation in this range. Photon loss, phase drift, distinguishability, detector effects, and noise-aware training remain untested. These results define the current evidence boundary.

---

# 9_Simulation feasibility demonstrated; hardware remains untested

The demonstrated result is simulation-pipeline feasibility: the code executes, two implementation paths agree, and the artifacts are reproducible. Application signal is only partly answered because the ranking comes from one outer fold. Hardware feasibility remains untested because realistic noise and remote execution are unfinished. Local computation is not the bottleneck: embedding extraction took 96.57 seconds and the pilot model grid about 59.9 seconds. The bottleneck is scientific validity across folds, noise, and calibrated hardware. That boundary leads to a conditional recommendation.

---

# 10_Recommendation: continue only through a decision-changing test

My recommendation is conditional. Few-label defect inspection fits a useful Quandela simulator-to-hardware study, and the pilot shows that the simulation workflow is executable. It has not demonstrated practical or hardware advantage. I continue only if Pass A at forty-eight labels or Pass B for twofold label efficiency holds. The shot and acceptance constraints belong only to Pass B. If neither passes, or Q1 loses to RFF-15 and ELM-15 on at least four folds, I report simulation feasibility without utility and stop before spending QPU time. Thank you.
