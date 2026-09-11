# 1_I would investigate few-label industrial defect inspection with a photonic reservoir

I would investigate few-label industrial defect inspection using a fixed photonic reservoir. I chose it because expert defect labels are costly, photonic interference provides a compact nonlinear feature map, and the idea can be evaluated rigorously within twelve weeks using public data, matched classical controls, and a staged path from simulation to hardware. I have already completed a de-risking pilot: Q1 reached a macro-F1 of 0.8708 at forty-eight labels per class. That result shows useful signal, but it does not yet show a practical or quantum advantage.

---

# 2_Why this is a good 12-week feasibility study

The application begins with a real operational constraint: industrial inspection images can be plentiful, while reliable defect labels require scarce expert time. That makes performance at twelve, twenty-four, and forty-eight labels per class a meaningful and measurable target. NEU-CLS provides 1,800 audited images across six balanced surface-defect classes, so the first feasibility study can run without waiting for proprietary data collection. The evaluation also has a clear failure mode. One exact duplicate pair, Pa_101 and Pa_105, stays in the same group, and the pilot test fold holds sixty images per class with no sample or duplicate-group overlap. This gives the project three properties I want in a short research assignment: a real need, accessible evidence, and a quantitative decision metric.

---

# 3_A small photonic reservoir fits Quandela’s path to hardware

The architecture is deliberately hybrid and small. A frozen OpenCLIP encoder produces image embeddings; PCA is fitted on training data only and reduces each embedding to five values scaled into the phase range from minus pi to pi. Those phases enter a fixed six-mode, two-photon circuit, and postselection converts twenty-one possible outcomes into fifteen conditional probabilities for a linear readout. The trainable part remains classical, so the experiment isolates the contribution of the photonic map without requiring a costly variational loop. Perceval provides the Quandela simulation layer, and its probabilities agree with an independent MerLin implementation to machine precision. That simulator check is complete. A remote QPU subset is the proposed final validation gate and has not yet been executed, so the current evidence must not be described as a hardware result.

---

# 4_The feasibility question is deliberately falsifiable

The feasibility question is narrower than asking whether quantum machine learning is generally better. At the same five-dimensional compressed input and fifteen-dimensional output, can Q1 beat a matched random Fourier feature map and close the gap to stronger nonlinear controls such as ELM and RBF-SVM? Alternatively, can it demonstrate an accuracy, sampling, or resource trade-off with practical value? The benchmark uses paired label budgets of twelve, twenty-four, and forty-eight examples per class, three nested subset seeds, and the same locked outer test fold. Seven model families separate the effects of full embeddings, PCA compression, nonlinear mapping, and output dimension. Hyperparameters are selected using validation macro-F1 only, while map seeds are averaged rather than selected. The continue gate is evidence against strong controls across outer folds or a useful resource trade-off. If Q1 only beats RFF, the stop conclusion is feasibility without utility.

---

# 5_A 12-week plan moves from simulation to a decision

The twelve-week plan removes uncertainty in stages and delays scarce hardware time until the earlier gates pass. Weeks one and two freeze the data audit, leakage-safe splits, metrics, classical baselines, and stopping criteria. Weeks three and four implement the Perceval circuit and require agreement with an independent simulator before benchmarking. Weeks five and six run the paired model matrix across five outer folds to test whether the ranking generalizes beyond the pilot. Weeks seven and eight introduce finite-shot sampling, photon loss, phase drift, distinguishability, detector effects, and noise-aware training where appropriate. Weeks nine and ten run a frozen remote subset with raw counts and calibration metadata, but only if the simulation and noise gates remain credible. Weeks eleven and twelve replicate on a harder dataset, document resource accounting, and issue a go-or-stop decision memo.

---

# 6_The pilot shows useful signal—not competitive advantage

The completed pilot provides early evidence rather than the final answer. Q1 macro-F1 rises from 0.7812 at twelve labels per class to 0.7886 at twenty-four and 0.8708 at forty-eight. The upward trend means the photonic feature map contains useful class information. However, the full CLIP linear baseline starts at 0.9242 and reaches 0.9852 at the largest budget. Each point is the mean across three subset seeds, with sample-standard-deviation error bars, but all points reuse one outer test fold. The disciplined interpretation is therefore that Q1 learns useful structure on this pilot, while the current configuration does not justify replacing the full embedding or claiming competitive advantage.

---

# 7_Compression—not photonics alone—explains the shortfall

The diagnostic result changes what the next experiment should test. Moving from the full embedding to PCA-five costs the linear baseline 0.1018, 0.0993, and 0.0713 macro-F1 across the three budgets, so important information is lost before the nonlinear map is evaluated. Within the compressed comparison, Q1 beats matched RFF by 0.3133, 0.2238, and 0.2307. It still trails ELM by between roughly 0.02 and 0.04, and trails PCA-five RBF by about 0.05 to 0.06 at every budget. The surviving claim is specific: the photonic map is better than one weak matched random map, but not the stronger nonlinear controls. The next study must therefore vary representation size and circuit design separately rather than attributing the entire gap to photonics.

---

# 8_Finite-shot sampling is stable; accuracy does not recover

The finite-shot test asks whether sampled output probabilities behave stably enough to support a later hardware comparison. Mean macro-F1 is 0.7662 with five hundred launched shots, 0.7739 with two thousand, and 0.7725 with eight thousand, based on fifteen evaluations at each level. Acceptance remains close to 0.754, and none of the forty-five evaluations suffers a zero-acceptance failure. Increasing shots does not produce a monotonic accuracy recovery, so shot count alone does not close the model gap. This experiment tests sampling and postselection around an ideal-trained readout. It does not yet include photon loss, phase drift, partial distinguishability, detector noise, or noise-aware training, which are explicit tasks in the proposed twelve-week plan.

---

# 9_Technically feasible; practical utility remains open

The current evidence supports a calibrated three-level verdict. Technical feasibility is proven: the pipeline executes, simulator semantics agree independently, and the artifacts are reproducible. Application signal is partially answered: Q1 improves with labels, the paired one-fold ranking is known, and finite-shot sampling is stable in the tested range. Practical utility remains unanswered because we do not yet have five-fold generalization, realistic photonic noise, or remote hardware execution. Runtime does not block that work. On the measured local CPU run, OpenCLIP extraction took 96.57 seconds and the first benchmark after embeddings took about 59.9 seconds. The real bottleneck is scientific validity under more folds, harder data, realistic noise, and calibrated hardware—not local computation time.

---

# 10_Recommendation: continue only through a decision-changing test

My application choice is few-label industrial defect inspection with a fixed photonic reservoir. I chose it because label scarcity is real, the compact phase-encoded feature map fits Quandela’s simulator-to-hardware workflow, and the evidence can be produced within twelve weeks. The completed pilot says the idea is technically feasible and scientifically interesting, but it has not demonstrated practical advantage. I would continue only through the predefined next gates: Q1 must close the ELM or RBF gap across outer folds, or demonstrate a resource trade-off that matters in practice. If it continues to beat only RFF while the strong controls remain better, I would report feasibility without utility and stop. The repository linked here contains the protocol, implementation, results, and presentation artifacts needed to reproduce that decision.
