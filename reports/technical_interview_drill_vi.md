# Luyện phỏng vấn kỹ thuật — photonic QML case study

Mỗi câu trả lời ngắn dưới đây nên nói trong 25–45 giây. Phần “đào sâu” là ý để dùng khi hội đồng hỏi tiếp.

## 1. Why this application?

**Answer:** “Few-label defect inspection has a concrete operational constraint: expert labels are expensive. It also gives a measurable 12-week study because the dataset, label budgets, controls, and failure criteria can all be fixed in advance.”

**Đào sâu:** Đây là application-fit claim, không phải quantum-advantage claim. NEU-CLS chỉ là benchmark khởi đầu; harder-data replication nằm cuối dự án.

## 2. Why use a frozen OpenCLIP encoder?

**Answer:** “Freezing the encoder isolates the feature-map question and keeps the label-limited comparison tractable. It also lets every model family reuse exactly the same image representation.”

**Đào sâu:** Fine-tuning encoder là một research axis khác và có thể che lấp tác động của photonic map.

## 3. Why PCA-5?

**Answer:** “Five inputs fit a small phase-encoded circuit and make simulation cheap enough for controlled comparisons. The pilot shows that this compression is aggressive, so PCA dimension becomes an explicit ablation rather than a fixed assumption in the proposed project.”

## 4. Why six modes and two photons?

**Answer:** “It is a deliberately small configuration with a compact output space and a plausible simulator-to-hardware path. With two photons in six modes there are twenty-one Fock outcomes, and the unbunched postselected space provides fifteen features.”

**Đào sâu:** Không nói cấu hình này tối ưu; đây là candidate đã de-risk, sẽ so với architecture alternatives.

## 5. What is trained?

**Answer:** “The photonic circuit is fixed in the pilot. Only the classical linear readout is fitted. This isolates whether the fixed photonic transformation creates useful features and avoids the cost and instability of a variational loop.”

## 6. What exactly did MerLin verify?

**Answer:** “MerLin reproduced the ideal output probabilities through a second implementation path to machine precision. It checks code-path consistency, not external replication, experimental validation, or organizational independence.”

## 7. Why is the experiment leakage-safe?

**Answer:** “PCA and every fitted transform use training data only. Hyperparameters use validation macro-F1 only. The exact duplicate pair stays in one group, and test samples never participate in selection.”

## 8. Did you evaluate the test set once?

**Answer:** “Once per selected fitted pipeline. The pilot contains multiple pipelines across families, budgets, subsets, and map seeds, so it has multiple test evaluations. They share one outer fold and must not be interpreted as independent generalization folds.”

## 9. Why macro-F1?

**Answer:** “Macro-F1 gives each defect class equal weight and exposes uneven class performance. The dataset is balanced, but macro-F1 remains a better guard against a model improving by favoring easier classes.”

## 10. What is the strongest pilot result?

**Answer:** “Q1 reaches 0.8708 macro-F1 at forty-eight labels per class and consistently beats the locked RFF-15 comparator. That establishes useful signal, not competitive advantage.”

## 11. What is the most damaging result?

**Answer:** “Q1 remains about 0.05 to 0.06 below PCA-5 RBF-SVM and below ELM at every label budget. The full OpenCLIP linear baseline is stronger still.”

## 12. Why not claim quantum advantage?

**Answer:** “There is no basis for that claim. Strong classical controls win, the pilot uses ideal simulation and one outer fold, and no QPU run has been completed. The present claim is technical feasibility with an application signal.”

## 13. What is the falsifiable success criterion?

**Answer:** “Accuracy passes if Q1 is within 0.02 macro-F1 of PCA-5 RBF-SVM on at least four of five folds. Resource value passes if Q1 at twenty-four labels per class reaches the forty-eight-label RBF-SVM within 0.02 on at least four folds, with no more than two thousand shots per image and acceptance of at least 0.70.”

## 14. Why choose 0.02?

**Answer:** “It is a prospective practical-equivalence margin: small enough to rule out the pilot’s current 0.05 gap, but large enough to avoid treating negligible score noise as a meaningful difference. I would freeze it before the five-fold run and report sensitivity to nearby margins.”

## 15. What does resource value mean?

**Answer:** “The primary resource claim is label efficiency: matching a forty-eight-label classical reference with twenty-four labels for Q1. The claim is valid only under the pre-specified shot and acceptance constraints. I would also report QPU calls, latency, and memory as secondary accounting.”

## 16. Why does more sampling not improve macro-F1?

**Answer:** “Sampling noise is not the dominant limitation in this range. The readout was trained on ideal probabilities, and the representation and feature map already impose a larger error. More shots reduce estimation noise but cannot restore information lost by PCA or fix a weaker decision geometry.”

## 17. What noise must be added before hardware?

**Answer:** “Photon loss, phase drift, partial distinguishability, source impurity, detector behavior, and postselection effects. I would use measured or documented hardware parameters where available and compare ideal-trained with noise-aware readouts.”

## 18. What would you send to the QPU?

**Answer:** “One frozen circuit configuration, fixed preprocessing, a predeclared subset, shot count, raw-count schema, and calibration metadata. Hardware is a validation gate after simulation and noise tests, not another tuning loop.”

## 19. What if hardware access is unavailable?

**Answer:** “I would complete the five-fold and noise-aware evidence, freeze a hardware-ready payload, and report the QPU result as access-dependent. I would not replace the missing hardware evidence with a stronger claim.”

## 20. Why is the repository named Quanova?

**Answer:** “Quanova is the internal project and repository slug created for the case-study application. The technical platform references in the deck are Quandela, Perceval, and MerLin. I keep the repository URL stable for reproducibility.”

## 21. What would make you stop early?

**Answer:** “I stop if neither pre-specified pass route holds, or if Q1 fails both matched 15-dimensional controls on at least four folds. I would publish the negative result as feasibility without utility rather than moving to hardware by default.”

## 22. What is your contribution as an AI researcher?

**Answer:** “My contribution is disciplined experimental design: leakage-safe splits, matched controls, reproducible pipelines, resource accounting, and clear decision rules. I would work with photonics specialists on device constraints while owning the ML evaluation and evidence chain.”

## Tự chấm sau mỗi vòng

- Có trả lời trực tiếp trong câu đầu không?
- Có phân biệt pilot đã hoàn thành và dự án đề xuất không?
- Có nói đúng “one test evaluation per selected pipeline” không?
- Có tránh dùng “independent validation” cho MerLin không?
- Có nêu một con số hoặc một tiêu chí khi câu hỏi yêu cầu định lượng không?
- Có dừng sau 45 giây, thay vì tự mở thêm một bài giảng không?
