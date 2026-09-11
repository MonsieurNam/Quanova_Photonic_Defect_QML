# 1_A reproducible photonic pilot delivers a useful negative result

This case study asks whether a small, transparent photonic feature map can add value in few-label steel defect classification. In one frozen outer-fold pilot measured on 11 September 2026, the photonic model reaches a macro-F1 of 0.8708 at forty-eight labels per class. The full CLIP embedding with a linear classifier reaches 0.9852 on the same test fold, leaving a gap of 0.1143. The photonic model does beat the locked random Fourier feature baseline, but it does not beat ELM, the RBF-SVM controls, or the full embedding. That result is useful because it identifies a concrete representation bottleneck and gives the next experiment a falsifiable decision gate.

---

# 2_The benchmark starts with 1,800 audited images

The benchmark contains 1,800 valid images, balanced across six surface-defect classes with three hundred images per class: crazing, inclusion, patches, pitted surface, rolled-in scale, and scratches. The audit quarantined no invalid files, but it found one exact duplicate pair, Pa_101 and Pa_105. Those two images share one duplicate group, so they can never cross the train, validation, and test boundary. Fold zero uses seed forty-two and holds out sixty images per class, with checks confirming there is no sample-ID or duplicate-group overlap. This group-safe split matters because even one duplicated image on both sides could make a small-data result look stronger than it is.

---

# 3_The circuit is fixed; only phase encoding changes

Every model starts from a frozen OpenCLIP ViT-B/32 embedding, which is L2-normalized. PCA is fitted on training data only, reduces the representation to five dimensions, and scales those values into the phase range from minus pi to pi. The ideal photonic map uses six modes and two photons: modes zero through four encode the input while mode five acts as a reference, with occupation one-zero-one-zero-zero-zero. A fixed Haar-random unitary appears on both sides of the diagonal phase encoding, and postselection converts twenty-one possible outputs into a fifteen-dimensional conditional probability feature vector for a linear readout. Map seeds 101, 202, and 303 are averaged rather than selected or ensembled. Independent checks against Perceval 1.2.4 and MerLin 0.4.1 agree to about four times ten to the minus seventeen and eight times ten to the minus seventeen maximum error, respectively, which supports the simulator semantics used here.

---

# 4_The protocol makes overclaiming difficult

The paired label budgets are twelve, twenty-four, and forty-eight examples per class, divided into eight plus four, sixteen plus eight, and thirty-two plus sixteen for training and validation. Subset seeds eleven, twenty-two, and thirty-three are nested and share the same outer test fold. Seven model families face the same test gate: linear and RBF classifiers on full CLIP, linear and RBF classifiers on PCA-five, random Fourier features with fifteen outputs, ELM with fifteen outputs, and the fifteen-output photonic model. The first-run ledger contains 1,404 candidate fits but only 117 test evaluations. Hyperparameters are selected using validation macro-F1, map seeds are averaged rather than picked, training and validation are not refit together, and each selected configuration receives one locked test evaluation. Because evaluations reuse one outer test set, the repeated cells improve descriptive stability but do not create independent estimates of population generalization.

---

# 5_Q1 improves with labels, but full embeddings dominate

The learning curves show that the photonic model learns useful structure as the label budget rises: mean macro-F1 moves from 0.7812 at twelve labels per class to 0.7886 at twenty-four and 0.8708 at forty-eight. The full CLIP linear model is already at 0.9242 at the smallest budget and reaches 0.9852 at the largest. At forty-eight labels, Q1 therefore trails B1 by 0.1143, even though its own gain with more labels is real. Each point is the mean across three subset seeds, and the uncertainty bars are sample standard deviations, so the chart should be read as a measured pattern on this outer fold. The evidence supports continued study of the learned photonic representation, but it gives no case for discarding the full embedding.

---

# 6_PCA-5 compression explains much of the gap

Compressing the CLIP embedding to five principal components causes a large performance penalty before any nonlinear map is applied. For the linear classifier, the full-minus-PCA gap is 0.1018, 0.0993, and 0.0713 at label budgets twelve, twenty-four, and forty-eight. For the RBF classifier, the corresponding gaps are 0.0657, 0.0872, and 0.0263. At twenty-four labels per class, PCA-five linear scores 0.8646, PCA-five RBF scores 0.8444, ELM scores 0.8318, and Q1 scores 0.7886. The key implication is that information is lost during compression, before the classical or photonic nonlinear feature map is evaluated. Any follow-up should therefore separate the effect of compression from the effect of the circuit.

---

# 7_Q1 beats RFF, not the strong nonlinear controls

Pairing results by subset makes the comparison direction clear. Against the fifteen-feature random Fourier map, Q1 gains 0.3133, 0.2238, and 0.2307 macro-F1 at twelve, twenty-four, and forty-eight labels per class. Against ELM, however, Q1 is lower by 0.0166, 0.0432, and 0.0215. Against PCA-five RBF, it is lower by 0.0507, 0.0558, and 0.0534. These are descriptive differences paired within the same subset and outer test fold, so they reveal a consistent ranking without supporting a broad significance claim. The result narrows the claim to a specific weak baseline: this photonic map is better than locked RFF, but it does not establish an advantage over the stronger nonlinear controls.

---

# 8_More launched shots do not resolve the model gap

Finite-shot inference was evaluated fifteen times at each of three shot counts. Mean macro-F1 is 0.7662 with five hundred launched shots, 0.7739 with two thousand, and 0.7725 with eight thousand; the sample standard deviations are about 0.0322, 0.0308, and 0.0363. Acceptance stays near 0.754 and there are no zero-acceptance failures across all forty-five evaluations. Increasing the number of launched shots therefore produces no meaningful recovery toward the ideal-model benchmark. This test uses a readout trained on ideal probabilities, rather than noise-aware training, so it isolates sampling sensitivity but does not represent a complete hardware-noise study.

---

# 9_Scientific validity, not runtime, is the bottleneck

On the measured local CPU run, OpenCLIP feature extraction takes 96.57 seconds and the first-run benchmark after embeddings takes about 59.9 seconds. Within that benchmark, Q1 candidate fitting and validation accounts for about twenty-six seconds, with roughly 8.37 seconds for its test inference, so the pilot is computationally manageable. The stronger limitation is the evidence ladder: simulator semantics are validated, repeated subset evaluations are complete, and one outer-fold generalization test exists, while realistic photonic noise and hardware execution remain untested. The result also depends on small validation cells, and the full CLIP linear baseline is already near ceiling. Runtime is therefore not the current decision constraint; external validity under more folds, harder data, noise, and hardware is.

---

# 10_Continue only if a falsifiable gate can change the decision

The next experiment is a twelve-week conditional program. Weeks one and two freeze an R4 protocol with five outer folds; weeks three and four preregister PCA and circuit ablations; weeks five and six add loss, phase drift, and detector effects; weeks seven and eight run a remote subset with raw counts and calibration; and weeks nine through twelve replicate on a harder dataset. The program continues only if Q1 closes the ELM or RBF gap across outer folds, or demonstrates a resource tradeoff with practical value. If Q1 continues to beat only RFF, the correct conclusion is feasibility without utility and the line should stop. The complete code, protocol, results, and interview materials are available in the linked GitHub repository for reproduction and review.
