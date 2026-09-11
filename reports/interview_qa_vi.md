# Luyện Q&A cho phỏng vấn Quandela

## Câu hỏi đề bài

> Assume you are working as part of our research team and are assigned to investigate a promising new application for Quandela’s photonic quantum computing platform. You have only 2–3 months to explore and demonstrate the feasibility of the idea. Which application would you choose, and why? Describe also how you would approach the project.

## Phiên bản 30 giây

I would investigate few-label industrial defect inspection using a fixed photonic reservoir. It addresses a real constraint—expert defect labels are expensive—while a small phase-encoded circuit gives Quandela a credible near-term role as a nonlinear feature map. The idea is testable within twelve weeks using public data, strong matched baselines, Perceval, finite-shot and noise studies, and a conditional hardware subset. My pilot shows technical feasibility and useful signal, but no practical advantage yet, so I would continue only if the next study closes the ELM or RBF gap or demonstrates a useful resource trade-off.

## Phiên bản 90 giây

I would investigate few-label industrial visual defect classification using a fixed photonic quantum reservoir. A frozen vision encoder would extract image embeddings, training-only PCA would reduce them to a small number of phase variables, and a six-mode, two-photon circuit would transform those values into conditional photon-count probabilities. A lightweight classical classifier would use those probabilities.

I chose this application because industrial inspection has a genuine label-scarcity problem, the compact feature-map architecture fits near-term photonic hardware better than a large end-to-end variational model, and the feasibility question can be measured within two to three months. I would compare the photonic map with full-embedding classifiers, PCA controls, RFF, ELM, and RBF-SVM under the same splits and output dimension.

The first weeks would freeze the protocol and verify the Perceval implementation. I would then run paired multi-fold benchmarks, finite-shot and realistic-noise studies, followed by a small remote-hardware subset only if the earlier gates pass. Success means closing the ELM or RBF gap across outer folds or demonstrating a useful resource trade-off.

I have already completed a de-risking pilot. Q1 reached 0.8708 macro-F1 and clearly beat matched RFF, but it remained below ELM, RBF-SVM, and the full CLIP representation. Therefore, the current conclusion is technical feasibility without demonstrated application utility.

## Phiên bản khoảng 3 phút

I would choose few-label industrial visual defect classification and investigate a fixed photonic reservoir as the nonlinear feature map. The business motivation is straightforward: factories can collect many images, but reliable defect labels require domain experts, particularly for rare failure modes. That makes sample efficiency at twelve, twenty-four, or forty-eight labels per class a meaningful target rather than an artificial benchmark.

The system would remain hybrid. I would use a frozen OpenCLIP encoder for visual semantics, fit PCA and scaling only on the training data, encode the reduced values as optical phases, and send them through a small six-mode, two-photon circuit. The circuit is fixed; only the input phases change. Fifteen postselected photon-count probabilities then feed a classical linear classifier. This is appropriate for Quandela because Perceval supports the simulator stage, the circuit is compact enough for finite-shot and noise studies, and the same frozen specification can later be submitted to a remote photonic processor. It avoids claiming that a large trainable quantum neural network is ready for production.

I would define feasibility before running the experiment. At the same compressed input and fifteen-dimensional output, Q1 should beat matched random Fourier features and meaningfully close the gap to stronger nonlinear controls such as ELM and RBF-SVM. Alternatively, it should demonstrate a useful resource trade-off in accuracy, shots, latency, or hardware cost. If it only beats RFF while the stronger controls stay better, the project stops with a feasibility-only conclusion.

Weeks one and two would freeze the data audit, group-safe splits, metrics, baseline grids, and stop rule. Weeks three and four would implement the circuit in Perceval and require numerical agreement with an independent implementation. Weeks five and six would run a paired five-fold benchmark across label budgets and random seeds. Weeks seven and eight would add finite-shot sampling, photon loss, phase drift, distinguishability, detector effects, and noise-aware training where justified. Weeks nine and ten would use a remote hardware subset with raw counts and calibration metadata, but only if the previous gates pass. The final two weeks would replicate on a harder dataset, account for resources, and deliver a go-or-stop recommendation.

I have already run an initial one-fold pilot to reduce uncertainty. Q1 improves from 0.7812 to 0.8708 macro-F1 as labels increase, so the map contains useful information. It beats matched RFF by about 0.22 to 0.31, but it remains below ELM and PCA-five RBF, while full CLIP plus a linear model reaches 0.9852. The analysis also shows that PCA-five removes substantial information before the circuit runs. Finite-shot inference is stable between five hundred and eight thousand shots, with acceptance near 0.754, but more shots do not restore accuracy.

My current recommendation is therefore to continue only through a falsifiable next experiment. The idea is technically feasible and scientifically informative, but it has not demonstrated practical or quantum advantage. That distinction is the main decision I would bring back to the research team.

## Phản biện: Tại sao cần photonics khi full CLIP đã tốt hơn?

Không cần photonics để tối đa hóa accuracy trong pilot hiện tại. Full CLIP là upper operational baseline và đang thắng rõ. Vai trò của circuit là kiểm tra xem một biểu diễn quang tử nhỏ có thể giữ được accuracy hữu ích hoặc tạo resource trade-off hay không. Nếu không có trade-off như số chiều, năng lượng, latency hoặc khả năng triển khai phần cứng, lựa chọn kỹ thuật đúng là giữ baseline cổ điển.

## Phản biện: Negative result còn được gọi là promising application không?

“Promising” mô tả lý do đáng để kiểm tra, không bảo đảm kết quả phải dương. Bài toán có nhu cầu thật, kiến trúc phù hợp với photonic feature mapping và có tiêu chí đo trong 12 tuần. Pilot đã giảm rủi ro bằng cách chỉ ra phần nào hoạt động và bottleneck nằm ở đâu. Kết quả âm trở thành giá trị nếu nó giúp đội nghiên cứu dừng sớm hoặc thiết kế thí nghiệm tiếp theo tốt hơn.

## Phản biện: Đây có phải quantum advantage không?

Không. Một claim quantum advantage cần thắng các baseline cổ điển mạnh dưới resource accounting công bằng, trên nhiều outer fold, với noise và phần cứng thực. Pilot chỉ cho thấy Q1 vượt RFF trong một thiết kế cụ thể; ELM, RBF-SVM và full CLIP vẫn tốt hơn.

## Phản biện: Vì sao pilot chỉ có một outer fold?

Một outer fold phù hợp với vai trò de-risking ban đầu: xác minh pipeline, protocol, simulator, runtime và hướng của hiệu năng trước khi tiêu tốn ngân sách cho ma trận năm fold. Nó không đủ cho kết luận khái quát. Vì vậy năm outer fold là deliverable bắt buộc ở tuần năm và sáu của dự án chính.

## Phản biện: Khi nào mới nên dùng hardware?

Chỉ sau khi circuit, shot definition, calibration fields, preprocessing và evaluation set đã được đóng băng; simulator đã được kiểm tra độc lập; benchmark nhiều fold còn đủ triển vọng; và realistic-noise study không cho thấy collapse. Hardware run phải lưu raw counts, calibration metadata, queue/runtime information và mọi failure, thay vì chỉ lưu metric cuối.

## Phản biện: Quantum đóng góp ở đâu?

Quantum circuit chỉ thay lớp feature map. Năm thành phần PCA điều khiển pha, hai photon truyền qua U D(x) U, và mười lăm xác suất collision-free đi vào linear readout. Các baseline B1–B6 tách ảnh hưởng của embedding, compression, nonlinearity và output dimension để tránh gán mọi cải thiện cho circuit.

## Câu kết nên dùng

The pilot answers feasibility, not advantage. It shows that the photonic reservoir is executable, reproducible, and capable of learning useful structure. The next twelve weeks are justified only if they can produce evidence that changes the application decision.
