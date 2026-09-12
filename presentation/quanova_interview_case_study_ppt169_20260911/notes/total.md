# 1_I would investigate few-label industrial defect inspection with a photonic reservoir


# 1_I would investigate few-label industrial defect inspection with a photonic reservoir

Good afternoon. I am Nguyen Ngo Nhat Nam, and I would investigate few-label industrial defect inspection using a fixed photonic reservoir. I chose it for three reasons: expert defect labels are costly, photonic interference offers a compact nonlinear feature map, and the idea can be evaluated rigorously within twelve weeks using public data, matched controls, and a staged path from simulation to hardware. I have already completed a de-risking pilot. Q1 reached 0.8708 macro-F1 at forty-eight labels per class. That is useful signal, but it is not evidence of practical or quantum advantage.

---

# 2_Why this is a good 12-week feasibility study

The operational constraint is label scarcity. Inspection images may be plentiful, but reliable defect labels consume expert time. Performance at twelve, twenty-four, and forty-eight labels per class is therefore a meaningful target. NEU-CLS gives 1,800 audited images across six balanced steel-surface defect classes, so the study can start without waiting for proprietary data. The evaluation also has a clear failure mode: the exact duplicate pair Pa_101 and Pa_105 remains in one group, and the pilot test fold contains sixty images per class with no sample or duplicate-group overlap. This gives a real need, accessible evidence, and a quantitative decision.

---

# 3_A small photonic reservoir fits Quandela’s path to hardware

The architecture is deliberately hybrid and small. A frozen OpenCLIP encoder produces an image embedding. Principal component analysis is fitted on training data only and reduces it to five values scaled from minus pi to pi. Those phases enter a fixed six-mode, two-photon circuit. Postselection turns twenty-one possible outcomes into fifteen conditional probabilities for a linear readout. Only the readout is trained, which isolates the feature map and avoids a costly variational loop. Perceval is the primary simulation layer. A second implementation in MerLin reproduces the probabilities to machine precision. That is a separate code path inside the same ecosystem, not external replication. Both checks are complete. Remote QPU execution remains a proposed final gate, subject to access.

---

# 4_The feasibility question is deliberately falsifiable

The question is specific: from the same PCA-five input, can Q1’s fifteen-dimensional photonic features beat matched fifteen-dimensional controls and approach PCA-five RBF-SVM? RFF means random Fourier features; ELM means extreme learning machine; and RBF-SVM means radial-basis-function support vector machine. The protocol uses nested label budgets, validation-only selection, averaged map seeds, and one test evaluation per selected fitted pipeline. I would preregister two pass routes. Accuracy passes if Q1 is within 0.02 macro-F1 of PCA-five RBF-SVM on at least four of five outer folds. Resource value passes if Q1 with twenty-four labels per class reaches the forty-eight-label RBF-SVM within 0.02 on at least four folds, using at most two thousand launched shots per image and an acceptance rate of at least 0.70. If neither route passes, or Q1 fails both matched controls on at least four folds, I stop.

---

# 5_The 12-week project starts after the completed pilot

The pilot is pre-study evidence; it does not consume the twelve-week project. The dataset audit, frozen protocol, simulator checks, finite-shot test, and fold-zero result are complete. Weeks one and two replicate all five outer folds. Weeks three and four ablate PCA dimension, circuit design, and measurement choices. Weeks five and six add loss, phase drift, partial distinguishability, detector effects, and noise-aware training. Weeks seven and eight select and freeze one hardware candidate, including preprocessing, shot definition, and calibration fields. Weeks nine and ten run a remote QPU subset only if the earlier gates pass. Weeks eleven and twelve use harder data or an independent evaluation, account for resources, and produce a go-or-stop memo.

---

# 6_The pilot shows useful signal—not competitive advantage

Here is the primary pilot evidence. Q1 rises from 0.7812 at twelve labels per class to 0.7886 at twenty-four and 0.8708 at forty-eight. The upward trend shows that the photonic features contain class information. The full OpenCLIP linear baseline, however, starts at 0.9242 and reaches 0.9852. Each point averages three subset seeds, with sample-standard-deviation error bars, but all points reuse one outer test fold. The correct conclusion is that Q1 learns useful structure on this pilot while the current configuration does not justify replacing the full embedding or claiming an advantage.

---

# 7_Compression—not photonics alone—explains the shortfall

The diagnosis changes the next experiment. Compressing the full embedding to five principal components costs the linear baseline about 0.07 to 0.10 macro-F1, so information is lost before the nonlinear map is tested. Within the compressed comparison, Q1 beats the locked RFF-fifteen comparator by about 0.22 to 0.31. It still trails ELM by roughly 0.02 to 0.04 and PCA-five RBF-SVM by about 0.05 to 0.06. The surviving claim is narrow: this photonic map is better than one matched random-feature control, but not the stronger nonlinear controls. I would therefore vary representation size and circuit design separately.

---

# 8_Finite-shot sampling is stable; accuracy does not recover

The finite-shot test asks whether sampled probabilities are stable enough for a later hardware comparison. Macro-F1 is 0.7662 at five hundred launched shots, 0.7739 at two thousand, and 0.7725 at eight thousand. Each shot level contains fifteen evaluations: three map seeds times five sampling seeds. Across all three levels, that is forty-five evaluations on the same outer test fold. Acceptance stays near 0.754, with no zero-acceptance failure. More shots do not recover accuracy monotonically, so shot count alone does not close the gap. This tests sampling around an ideal-trained readout; loss, drift, distinguishability, detectors, and noise-aware training remain future work.

---

# 9_Technically feasible; practical utility remains open

The evidence supports a three-level verdict. Technical feasibility is proven: the pipeline executes, two implementations agree, and the artifacts are reproducible. Application signal is partly answered: Q1 improves with labels, the paired one-fold ranking is known, and finite-shot sampling is stable in the tested range. Practical utility remains open because five-fold generalization, realistic noise, and remote hardware are unfinished. Local runtime is not the constraint: cached OpenCLIP extraction took 96.57 seconds, and the pilot model grid took about 59.9 seconds on CPU. The bottleneck is scientific validity under more folds, stronger controls, realistic noise, and calibrated hardware.

---

# 10_Recommendation: continue only through a decision-changing test

My recommendation is to continue this application only through a decision-changing test. The case is worth testing because label scarcity is real, the compact circuit fits Quandela’s simulator-to-hardware path, and the pilot proves that the workflow can be executed. It has not yet demonstrated practical advantage. I would continue only if the preregistered accuracy-parity or label-efficiency gate passes. If Q1 still beats only RFF while ELM and RBF-SVM remain stronger, I would report technical feasibility without utility and stop. The repository link contains the protocol, implementation, results, and presentation artifacts needed to audit that decision. Thank you.
