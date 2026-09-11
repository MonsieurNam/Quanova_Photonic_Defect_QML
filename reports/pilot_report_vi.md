# Báo cáo pilot: photonic reservoir cho phân loại lỗi bề mặt thép ít nhãn

**Ngày chạy:** 11/09/2026
**Dataset:** NEU-CLS
**Phạm vi bằng chứng:** ideal simulation trên outer fold 0; finite-shot là sampled simulation; chưa có kết quả hardware/QPU.

## 1. Kết luận dành cho quyết định

Pilot đã hoàn thành toàn bộ R1, R2 và R3 theo protocol khóa trước khi xem test. Kết quả chính là
**không có bằng chứng để tuyên bố photonic feature map tốt hơn các baseline mạnh**. Q1 tốt hơn RFF-15
ở cả ba ngân sách, nhưng kém ELM-15 và RBF-SVM trên cùng PCA-5; baseline thực dụng nhất, full CLIP
embedding + logistic regression (B1), tốt hơn Q1 rất rõ.

Ở 24 nhãn/lớp (16 train + 8 validation), macro-F1 trung bình của Q1 là **0,7886**, so với **0,8318**
của ELM-15, **0,8444** của PCA-5 + RBF-SVM và **0,9638** của B1. Chênh lệch ghép cặp Q1–ELM là
**−0,0432**, Q1–RBF là **−0,0558**, còn Q1–RFF là **+0,2238**. Kết luận kỹ thuật là photonic map
này hoạt động như một nonlinear representation có ích hơn RFF cấu hình đã khóa, nhưng chưa biện minh
được cho chi phí quantum khi ELM/RBF và đặc biệt full embedding mạnh hơn.

Finite-shot inference không gây failure ở 500, 2.000 hoặc 8.000 launched shots, với acceptance xấp xỉ
0,754. Macro-F1 sampled nằm trong 0,766–0,774 và không tăng đơn điệu theo shot budget trong 45 lần
đánh giá. Đây là độ nhạy sampling trên ideal-trained readout, chưa phải noise-aware training.

**Quyết định đề xuất:** dùng kết quả này để trình bày năng lực thiết kế benchmark và khả năng rút ra
kết luận âm có ích. Chỉ mở rộng R4 năm folds nếu mục tiêu là xác nhận độ ổn định khoa học. Không ưu
tiên QPU quota lớn cho cấu hình hiện tại; trước QPU nên kiểm tra thêm circuit/measurement ablation đã
định trước và một use case khó hơn nơi B1 chưa gần trần.

## 2. Dữ liệu và kiểm tra leakage

Archive chính thức được tải từ Google Drive ID `1NGlXT9sIaQpyxUoT6MLKm1Pr6x8oxOvc`.

| Hạng mục | Kết quả |
|---|---:|
| Ảnh tổng / hợp lệ | 1.800 / 1.800 |
| Số lớp | 6 |
| Ảnh mỗi lớp | 300 |
| Ảnh quarantine | 0 |
| Exact duplicate groups | 1 |
| Near/exact groups tổng | 1.799 |
| Duplicate khác nhãn | 0 |
| Cặp exact duplicate | `Pa_101.bmp`, `Pa_105.bmp` |

Cặp exact duplicate cùng nhãn được giữ chung một group. `StratifiedGroupKFold`, seed 42, tạo năm
outer folds. Fold 0 có đúng 60 test images/lớp. Ở budget 24, mỗi lớp có 16 train, 8 validation và 60
test. Kiểm tra theo `sample_id` và `duplicate_group` đều không thấy giao nhau giữa ba luồng.

Nguồn số: [`dataset_audit.csv`](../results/tables/dataset_audit.csv), manifest và split hashes trong
`data/manifests/` và `data/splits/`.

## 3. Pipeline và tính đúng của circuit

Ảnh được đưa qua OpenCLIP `ViT-B-32`, checkpoint `openai`, đóng băng và L2-normalize. Checkpoint lấy
từ URL công bố của OpenAI, SHA-256
`40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af`. Trích xuất 1.800 embedding
trên CPU mất **96,57 giây**. PCA-5 và scaler chỉ fit trên training subset.

Q1 dùng sáu modes, hai photons, input occupation `[1,0,1,0,0,0]`, năm phase features và mode 5 làm
reference. Với mỗi map seed, cùng Haar-random `U` nằm hai phía: `U → D(x) → U`. Simulator tính đủ 21
Fock outcomes; 15 collision-free probabilities được chuẩn hóa theo acceptance để tạo feature vector,
và acceptance được lưu riêng.

Smoke verification cho thấy tổng probability bằng 1 trong sai số floating point, conditional 15-vector
tổng bằng 1, acceptance thuộc [0,1], và thay input làm đổi distribution. Sai số tối đa giữa simulator
nội bộ và Perceval 1.2.4 là **4,16×10⁻¹⁷**; sai số với MerLin 0.4.1 cũng ở mức machine precision.
Cache round-trip, resume và train-only preprocessing đều có tests.

## 4. Protocol đánh giá

R1 dùng fold 0, subset seeds 11/22/33 và ba tổng ngân sách 12/24/48 nhãn trên mỗi lớp. B1–B4 có một
test evaluation cho mỗi subset; B5/B6/Q1 giữ cả ba map seeds 101/202/303, không chọn seed và không
ensemble. Hyperparameter được chọn bằng validation macro-F1; với family ngẫu nhiên, dùng trung bình
trên cả ba map seeds. Model đã fit trên train được giữ nguyên, không refit train+validation.

Runner ghi nhận đúng **1.404 candidate fits và 117 test evaluations** cho R1. R2 thêm 24 fits/2
evaluations trên train/validation rộng hơn của fold 0. R3 dùng ba quantum seeds × ba launched-shot
budgets × năm sampling seeds = 45 evaluations, không train lại. Các seed/subset dùng cùng outer test
fold nên là repeated paired evaluations, không phải 117 dataset độc lập.

Timing gate chỉ dùng 64 input thuộc train/validation: 0,0508 giây, tương đương 0,000794 giây/input.
Forecast phần sinh quantum features của R1 là 0,0094 giờ, thấp hơn ngưỡng sáu giờ, nên đã chạy R1 đầy
đủ thay vì fallback `pilot_min`.

## 5. Kết quả R1

Macro-F1 là mean ± sample standard deviation trên ba subset seeds. Với family ngẫu nhiên, ba map
seeds được lấy trung bình bên trong mỗi subset trước khi tính mean/std; cách này tránh coi map seed là
dataset độc lập.

| Family | 12 labels/lớp | 24 labels/lớp | 48 labels/lớp |
|---|---:|---:|---:|
| B1 — full CLIP + LR | **0,9242 ± 0,0373** | **0,9638 ± 0,0323** | **0,9852 ± 0,0064** |
| B2 — full CLIP + RBF | 0,8976 ± 0,0207 | 0,9316 ± 0,0181 | 0,9504 ± 0,0177 |
| B3 — PCA-5 + LR | 0,8224 ± 0,0084 | 0,8646 ± 0,0307 | 0,9138 ± 0,0294 |
| B4 — PCA-5 + RBF | 0,8319 ± 0,0075 | 0,8444 ± 0,0231 | 0,9242 ± 0,0137 |
| B5 — PCA-5 + RFF-15 + LR | 0,4679 ± 0,0295 | 0,5648 ± 0,0493 | 0,6401 ± 0,0142 |
| B6 — PCA-5 + ELM-15 + LR | 0,7978 ± 0,0113 | 0,8318 ± 0,0112 | 0,8923 ± 0,0027 |
| Q1 — PCA-5 + photonic-15 + LR | 0,7812 ± 0,0185 | 0,7886 ± 0,0197 | 0,8708 ± 0,0281 |

Full embeddings giữ nhiều tín hiệu quan trọng: B1–B3 chênh 0,1018/0,0993/0,0713 tại ba ngân sách;
B2–B4 chênh 0,0657/0,0872/0,0263. Bottleneck PCA-5 là một phần lớn của khoảng cách Q1 với B1.

| Paired difference | 12 | 24 | 48 |
|---|---:|---:|---:|
| Q1 − RFF-15 | +0,3133 | +0,2238 | +0,2307 |
| Q1 − ELM-15 | −0,0166 | −0,0432 | −0,0215 |
| Q1 − PCA-5 RBF | −0,0507 | −0,0558 | −0,0534 |

Q1 có acceptance trung bình 0,7344/0,7428/0,7423 theo ba ngân sách. Kết quả chi tiết theo mọi
subset/map seed nằm trong [`main_results_raw_evaluations.csv`](../results/tables/main_results_raw_evaluations.csv)
và [`paired_differences.csv`](../results/tables/paired_differences.csv).

## 6. R2 và R3

R2 dùng phần train/validation rộng hơn của fold 0. B1 đạt **0,9972 macro-F1**, B2 đạt **0,9833**.
Đây là kiểm tra trần chất lượng trên cùng test fold, không phải so sánh cross-validation.

| Launched shots/ảnh | Macro-F1 mean ± std (15 evaluations) | Acceptance | Failure |
|---:|---:|---:|---:|
| 500 | 0,7662 ± 0,0322 | 0,7538 | 0 |
| 2.000 | 0,7739 ± 0,0308 | 0,7538 | 0 |
| 8.000 | 0,7725 ± 0,0363 | 0,7536 | 0 |

Shot budget là số lần launch trước postselection. Mỗi ảnh vẫn được giữ trong metric; nếu accepted
count bằng zero, runner gán `__ABSTAIN__`. Không có trường hợp đó trong R3. Việc 8.000 shots không hơn
rõ 2.000 cho thấy map-seed/subset uncertainty đang lớn hơn sai số sampling trong vùng này.

## 7. Chi phí đo được

Tổng các thời gian đã instrument cho R1, không gồm Python startup và I/O orchestration, khoảng 59,9
giây sau khi có embeddings. Q1 chiếm khoảng 26,0 giây candidate-fit/validation và 8,37 giây test
inference; B1 tương ứng 3,31 và 0,18 giây. Đây là profiling cùng CPU trong một pipeline, không phải
so CPU với GPU hoặc QPU. [`compute_cost.csv`](../results/tables/compute_cost.csv) chứa từng record.

## 8. Giới hạn và kế hoạch 8–12 tuần

- Chỉ một outer test fold được dùng; ba subset seeds không thay thế năm test folds độc lập.
- Grid khóa nhỏ và validation chỉ 4/8/16 ảnh/lớp, nên việc chọn hyperparameter có variance cao.
- NEU-CLS nhỏ, sạch và B1 gần trần; chưa đại diện ảnh nhà máy khác, defect detection hay anomaly mới.
- Ideal simulation không mô hình photon loss, distinguishability, phase drift, detector noise hoặc
  remote queue. R3 chỉ thêm multinomial sampling/postselection.
- Acceptance khoảng 0,74 nghĩa là cần launch nhiều hơn accepted events; chưa có chi phí QPU thật.
- Không có phép kiểm định hypothesis ở n=1 outer fold. Các mean/std hiện tại là mô tả, không phải
  confidence interval cho deployment population.

Nếu tiếp tục, tuần 1–2 giữ nguyên R4 năm folds và tái kiểm tra conclusion. Tuần 3–4 phân tích tại sao
PCA-5 mất tín hiệu và thử circuit ablations đã đăng ký trước. Tuần 5–6 thêm distinguishability, phase
error và loss; chỉ khóa một QPU candidate sau các bước này. Tuần 7–8 chạy remote simulator/QPU subset
nếu có quota, lưu raw counts/calibration và so distribution/prediction với finite-shot simulation.
Tuần 9–12 dành cho một dataset khó hơn hoặc independent replication, không quét nhiều dataset để
chỉ giữ nơi quantum thắng.

Điều kiện tiếp tục utility: Q1 phải thu hẹp hoặc đảo chiều chênh lệch với ELM/RBF trên đa số outer
folds, hoặc chứng minh một tradeoff tài nguyên có giá trị thực. Nếu chỉ thắng RFF yếu hơn trong khi
B1/ELM/RBF tiếp tục tốt hơn, kết luận nên là **hardware-feasibility study without an application
utility case for this circuit**.

## 9. Provenance

- NEU-CLS RAR SHA-256: `A85BCC6BFA1A40E76F28079E135694AAF5F6A4EE01203F7EAACFF0EBAFAA96F8`.
- Manifest SHA-256: `6D7D85A3D64D96F0A1B0B8C3A26204394BC5E7B054D4954198654FEF4A49B130`.
- CLIP checkpoint SHA-256: `40D365715913C9DA98579312B702A82C18BE219CC2A73407C4526F58EBA950AF`.
- Package/runtime versions được khóa trong `requirements/locked-cpu.txt`.
- Mỗi run có `config.json`, `metrics.json`, `predictions.csv`, candidate registry và serialized selected
  pipeline. Registry tổng nằm trong `runs/registry_*.csv`.
- Nguồn học thuật và tài liệu chính thức: [`research_review.md`](../docs/research_review.md).
