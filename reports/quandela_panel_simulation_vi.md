# Mô phỏng hội đồng Quandela

## Thành phần hội đồng giả lập

1. **Photonic hardware scientist** — kiểm tra tính đúng đắn vật lý, postselection, noise và QPU path.
2. **Quantum ML researcher** — kiểm tra baseline, leakage, statistics, falsifiability và claims.
3. **R&D lead** — kiểm tra lựa chọn application, khả năng thực thi 12 tuần và quyết định go/stop.

## Luật buổi mock 25 phút

- Trình bày deck trong 10 phút, không dừng để giải thích ngoài slide.
- Hội đồng hỏi 10 câu trong 12 phút. Mỗi câu trả lời tối đa 45 giây; câu follow-up tối đa 25 giây.
- Ba phút cuối dùng để chấm. Không sửa câu trả lời trong lúc chấm.
- Mỗi câu được 0–2 điểm: đúng kỹ thuật, trực tiếp, có ranh giới bằng chứng. Tổng tối đa 20.

## Vòng hỏi chính

### Hardware scientist

1. **“Why should a six-mode, two-photon simulation tell us anything about hardware feasibility?”**
   - Câu trả lời đạt: cấu hình nhỏ và hardware-aware giúp chuẩn bị payload; chỉ simulation feasibility được chứng minh; loss, sources, detectors, calibration và access vẫn chưa kiểm thử.
2. **“Your acceptance rate is about 0.754 in ideal sampling. What happens under loss?”**
   - Câu trả lời đạt: chưa biết từ pilot; acceptance và effective shots phải được đo lại dưới noise; Pass B yêu cầu acceptance ≥0.70 và tối đa 2.000 launched shots/image.
3. **“What exactly would you freeze before submitting to the QPU?”**
   - Câu trả lời đạt: circuit, input state, PCA/scaler, phase mapping, measurement/postselection, selected readout, subset, shot definition, raw-count schema và calibration metadata.

### Quantum ML researcher

4. **“Why is Pass A evaluated only at 48 labels per class?”**
   - Câu trả lời đạt: đây là budget có tín hiệu Q1 mạnh nhất và là endpoint thực dụng của pilot; quyết định được preregister trước five-fold run; toàn bộ budgets vẫn được báo cáo như secondary evidence.
5. **“Why is a 0.02 margin scientifically defensible?”**
   - Câu trả lời đạt: practical-equivalence margin prospective, nhỏ hơn rõ rệt gap pilot 0.05–0.06; khóa trước outer-fold evaluation; báo sensitivity analysis quanh margin.
6. **“You ran 117 pilot test evaluations. Why is this not severe test leakage?”**
   - Câu trả lời đạt: selection dùng validation only, mỗi fitted pipeline test một lần; nhưng nhiều pipelines cùng nhìn một fold tạo multiplicity và không thay thế independent folds, nên claim hiện tại chỉ descriptive.
7. **“Why compare with RFF-15 and ELM-15?”**
   - Câu trả lời đạt: cùng PCA-5 input và 15-D output để kiểm soát feature dimension; RBF-SVM là nonlinear reference mạnh không bị ép 15-D output.

### R&D lead

8. **“What result would make you cancel the project before requesting QPU time?”**
   - Câu trả lời đạt: neither pass holds, hoặc Q1 loses to both RFF-15 and ELM-15 on ≥4/5 folds; noise collapse cũng chặn QPU gate.
9. **“What does Quandela gain if the result is negative?”**
   - Câu trả lời đạt: benchmark reproducible, giới hạn của compression/map, resource accounting và một hardware-ready protocol; tránh tốn QPU time vào candidate không qua simulation gates.
10. **“Why are you the right person to execute this?”**
    - Câu trả lời đạt: năng lực chính là experimental ML, leakage-safe evaluation, reproducibility, sensor/image data và resource-aware deployment; phối hợp với photonics experts cho constraints thiết bị, không nhận quá kinh nghiệm hardware.

## Follow-up gây áp lực

- “Is MerLin really independent?” — “It is an independent code path, not an independent organization or external replication.”
- “So you have demonstrated hardware feasibility?” — “No. I have demonstrated simulation-pipeline feasibility; hardware remains untested.”
- “Why not simply use full OpenCLIP?” — “For this benchmark today, I would. The research question is whether a compact photonic map offers label or resource value under constraints; the pilot has not shown that yet.”
- “What if Q1 passes accuracy but requires unacceptable QPU latency?” — “Then the practical decision can still be stop; Pass A is scientific parity, while deployment requires separate latency and QPU-call accounting.”

## Rubric

| Điểm | Đánh giá |
| ---: | --- |
| 17–20 | Sẵn sàng: chính xác, ngắn, không overclaim |
| 13–16 | Tốt: còn 1–2 câu dài hoặc thiếu một qualifier |
| 9–12 | Rủi ro: nhầm simulation với hardware hoặc rule thiếu nhất quán |
| 0–8 | Cần luyện lại: trả lời chung chung, không dùng evidence/gate |

Ba lỗi trừ thẳng 2 điểm mỗi lần: gọi MerLin là external validation; nói hardware feasibility đã proven; biến 117 evaluations thành 117 independent tests.
