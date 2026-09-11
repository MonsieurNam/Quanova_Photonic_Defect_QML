# Lựa chọn ứng dụng photonic QML cho case study Quanova

## 1. Khuyến nghị

**Chọn phân loại lỗi bề mặt thép với ít dữ liệu có nhãn, sử dụng một photonic quantum reservoir làm bộ biến đổi đặc trưng sau encoder thị giác cố định.** Tên trình bày đề xuất:

> **Low-label steel surface defect classification with photonic quantum reservoir features.**

Đây là lựa chọn tốt nhất xét đồng thời nền tảng hiện tại của Nguyễn Ngô Nhật Nam, thời gian chuẩn bị phỏng vấn, khả năng thực hiện nghiên cứu trong 8–12 tuần và mức độ phù hợp với công cụ Quandela. Khuyến nghị này là đánh giá chiến lược, không phải dự báo xác suất trúng tuyển hoặc dự báo quantum sẽ thắng classical.

Ứng dụng cụ thể là hỗ trợ kỹ sư chất lượng phân loại các ảnh vùng lỗi đã được chụp/cắt sẵn khi chỉ có ít ví dụ được chuyên gia gán nhãn. Phạm vi đầu tiên là phân loại loại lỗi đã biết. Phát hiện vùng lỗi trong toàn bộ ảnh, phát hiện lỗi chưa từng thấy và vận hành dây chuyền thời gian thực là những bài toán khác.

**Thứ tự lựa chọn:** (1) steel defect classification; (2) WiFi CSI activity recognition; (3) experimental band-gap regression; (4) XRD phase classification; (5) quantum simulation vật liệu. Nếu công ty xác nhận có dự án vật liệu cụ thể, dữ liệu và người hỗ trợ chuyên môn, thứ tự 1 và 3 có thể đảo. Email hiện tại không đặt điều kiện đó.

Mức chắc chắn của lựa chọn: **trung bình–khá**. Chứng cứ về nền tảng và sự phù hợp kỹ năng tương đối rõ; ưu tiên nội bộ công ty, khả năng truy cập QPU, chất lượng đặc trưng trên dataset và lợi ích thực nghiệm của mô hình vẫn chưa được xác nhận. Báo cáo này không chứa kết quả benchmark mới.

## 2. Đề bài thực sự yêu cầu gì?

Email yêu cầu khoảng 10 slide, chọn một ứng dụng triển vọng cho nền tảng Quandela và giải thích cách khảo sát tính khả thi trong 2–3 tháng. Production readiness không phải mục tiêu bắt buộc. Khoảng thời gian chuẩn bị slide và khoảng thời gian thực hiện dự án là hai mốc riêng biệt; buổi phỏng vấn dự kiến ngày 15/09/2026, 15:30 GMT+7.[^1]

Từ yêu cầu này, cách đọc hợp lý là hội đồng muốn đánh giá khả năng xác định vấn đề, lựa chọn phương pháp phù hợp thiết bị, quản lý phạm vi, thiết kế phép so sánh và rút ra quyết định từ kết quả. Đây là suy luận từ đề bài, không phải rubric chính thức của công ty.

Nội dung meeting củng cố cách hiểu đó. Khoảng 17:06, người phỏng vấn giải thích quantum nên nằm trong một phần của hybrid pipeline. Khoảng 27:02–27:24, anh nhắc QML và simulation cho vật liệu; đến 32:23, anh nói hướng nghiên cứu không nhất thiết phải là QML, miễn triển khai được trên hệ thống. Transcript có lỗi nhận dạng nên không nên biến một đoạn nhắc vật liệu thành yêu cầu bắt buộc.[^2]

Một case mạnh cần trả lời được năm câu:

1. Vấn đề của ai, và cải thiện nào có giá trị?
2. Vì sao ứng viên này có thể triển khai và đánh giá nó?
3. Phần quantum làm gì, và có đường chạy thực tế trên Quandela không?
4. Phép thử nào phân biệt lợi ích quantum với hiệu quả của preprocessing hoặc classical encoder?
5. Sau 8–12 tuần, bằng chứng nào đủ để tiếp tục, dừng hoặc đổi cách tiếp cận?

“New application” nên được trình bày là một đề xuất mở rộng có mục đích cho nền tảng. Không mặc nhiên đồng nghĩa với “đầu tiên trên thế giới”. Những gì đã xuất hiện trong nghiên cứu trước phải được thừa nhận, và tính mới đối với danh mục nội bộ Quandela vẫn cần xác nhận.

## 3. Nền tảng hiện tại và khoảng kiến thức cần bù

CV cho thấy kinh nghiệm trực tiếp về few-shot VLM adaptation, low-rank updates, mô hình gọn, đánh giá nhiều seed, robustness, dữ liệu WiFi/LiDAR và profiling hệ thống. SingLoRA-CLIP và OrthoAdapt là hai bằng chứng gần nhất với một nghiên cứu kiểm tra bộ biến đổi đặc trưng nhỏ dưới giới hạn dữ liệu và tài nguyên. Kinh nghiệm WiFi hiện có là pose estimation; nó hỗ trợ HAR nhưng không đồng nghĩa đã có sẵn pipeline activity recognition.[^3]

| Năng lực | Cách dùng trong đề tài được chọn | Điều không nên suy diễn |
|---|---|---|
| Few-shot learning, CLIP adaptation | Đóng băng encoder, đo learning curve theo ngân sách nhãn | Quantum reservoir tương đương LoRA |
| So sánh tham số và ablation | So readout ngang chiều, kiểm soát encoder, tách hiệu ứng compression | Ít tham số hơn tự động rẻ hơn trên QPU |
| Robustness và domain shift | Kiểm tra ảnh bị nhiễu; hiểu giới hạn ngoại suy sang nhà máy khác | Synthetic corruption chứng minh cross-factory generalization |
| PyTorch và scientific computing | Xây pipeline classical–quantum–classical và lưu thí nghiệm | PyTorch autograd đồng nghĩa QPU có gradient trực tiếp |
| Hardware-aware profiling | Đo sampling, hiệu suất lấy mẫu hợp lệ, thời gian remote và xử lý đầu cuối | Mô hình gọn trên GPU bảo đảm inference nhanh trên QPU |

Trong meeting, Nam tự mô tả quantum mới ở mức tự học khoảng một đến hai tuần, chủ yếu lý thuyết. Không có bằng chứng đã có nền tảng sâu về Hamiltonian vật liệu, DFT, crystal chemistry hoặc hiệu chuẩn thí nghiệm quang học.[^2] Chọn bài toán ML quen thuộc giúp dành thời gian học đúng phần mới: Fock state, optical mode, giao thoa nhiều photon, phase encoding, phép đo và hạn chế lấy mẫu.

## 4. Những bằng chứng quan trọng nhất

### 4.1. Quandela có đường triển khai phù hợp người làm ML

MerLin được thiết kế cho nghiên cứu photonic/hybrid QML với PyTorch và scikit-learn, coi benchmarking và reproducibility là trọng tâm. Paper công bố một tập các nghiên cứu được tái hiện có thể mở rộng. Điều này tạo cơ sở cho đề xuất nghiên cứu có baseline và ablation rõ ràng.[^4]

### 4.2. Materials QML có tiền lệ thật nhưng chưa quyết định đề tài tốt nhất cho ứng viên

PolyT kết hợp encoder cổ điển và quantum classifier trên Ascella để phân loại tính ổn định nhiệt polymer. Quandela báo cáo khoảng 84–85% accuracy, kết quả cạnh tranh với MPNN và thử nghiệm trên hardware. Đây là báo cáo của chính đơn vị tham gia dự án, hỗ trợ tính khả thi của workflow; không chứng minh mọi bài toán vật liệu sẽ có quantum advantage hoặc xác nhận dataset sẵn cho ứng viên.[^5]

### 4.3. Photonic reservoir có bằng chứng hardware, và có baseline cổ điển rất cạnh tranh

Rambach và cộng sự nghiên cứu QORC với Fock-state photons, phase encoding và readout cổ điển; có thực nghiệm 3 photon/12 mode trên Ascella. Bản v2 ngày 11/08/2026 bổ sung so sánh đáng chú ý: ở cấu hình MNIST 3 photon/20 mode, QORC đạt 96.5% và Random Fourier Features đạt 96.7%; ở 5 photon/24 mode, cả hai đạt 97.5%. Kết quả giảm số mẫu nổi bật của bài chủ yếu được đặt cạnh multinomial logistic regression. Vì vậy, không được diễn giải thành lợi thế 20 lần so với mọi mô hình cổ điển.[^6]

Hệ quả cho thiết kế nghiên cứu: phải đưa Random Fourier Features (RFF) và mô hình kernel mạnh vào baseline; lợi ích so với một linear head đơn giản chưa đủ kết luận phần quantum đáng đầu tư.

### 4.4. Quantum kernel cho vật liệu cũng cần đọc quá abstract

Nghiên cứu XRD của Adams và cộng sự dùng dữ liệu Fe–Ga–Pd, với 20 mẫu được chọn từ tập 237 vị trí, chạy kernel trên IonQ Aria 25 qubit. Trong thí nghiệm nhãn vật lý, quantum vượt RBF ở một số mức dữ liệu nhưng cosine kernel đạt kết quả tốt nhất. Các kernel cổ điển sử dụng hyperparameter cố định; dữ liệu engineered-label là một phép thử khác. Đây là tiền lệ thú vị, nhưng không phải bằng chứng quantum thắng baseline mạnh trên mọi task vật liệu, và kiến trúc IonQ không thể được coi là cấu hình Quandela sẵn chạy.[^16]

### 4.5. Có giới hạn software cần phản ánh ngay trong kế hoạch

Tài liệu MerLin 0.4 cho biết `MerlinProcessor` chưa truyền gradient qua remote execution. Huấn luyện end-to-end trong simulator và inference trên QPU là hai việc khác nhau.[^8] Workflow reservoir cố định thuận lợi vì đặc trưng có thể được tính và cache, còn readout học ở máy cổ điển.[^7]

Với phần hardware, ưu tiên phase encoding và đầu ra từ counts/probabilities. Raw amplitudes không phải dữ liệu có thể đọc trực tiếp từ QPU. Lựa chọn trạng thái, phép đo và postselection phải khớp khả năng detector của backend thực tế.[^9]

Một benchmark rộng của Bowles, Ahmed và Schuld cho thấy các mô hình cổ điển phổ thông thường thắng các quantum classifier trong những bài toán nhỏ họ thử. Kết quả này không phủ nhận mọi tiềm năng QML; nó cho thấy chất lượng thiết kế thí nghiệm có thể quan trọng hơn một tuyên bố advantage hấp dẫn.[^12]

## 5. So sánh các hướng

Các đánh giá trong bảng là phán đoán định tính cho case này, không phải điểm đo thực nghiệm hoặc xác suất thành công.

| Hướng | Phù hợp kiến thức Nam | Đường tới photonic QPU | Khối lượng học domain | Điểm thuyết phục | Rủi ro chính | Vị trí |
|---|---|---|---|---|---|---|
| Few-label steel defect classification | Rất cao | Rõ: encoder + fixed reservoir | Thấp–vừa | Nối nghiên cứu hiện có với ứng dụng công nghiệp cụ thể | Baseline vision có thể quá mạnh; benchmark nhỏ | Khuyến nghị chính |
| WiFi CSI activity recognition | Cao | Khả thi sau xử lý và nén tín hiệu | Vừa | Có kinh nghiệm cảm biến, câu chuyện khác biệt | Split theo người/phòng, domain shift, temporal representation | Dự phòng số 1 |
| Experimental band-gap regression | Vừa | Khả thi với descriptor và readout regression | Vừa–cao | Liên hệ materials discovery rõ | Composition thiếu thông tin cấu trúc; baseline tabular mạnh | Đổi sang nếu công ty ưu tiên vật liệu |
| XRD phase classification | Vừa | Cần thiết kế lại circuit và encoding | Cao | Nối signal processing với materials characterization | Domain interpretation, quá ít mẫu độc lập | Đề xuất tiếp nối với mentor |
| Polymer thermal stability giống PolyT | Vừa | Có tiền lệ | Vừa–cao | Sát use case Quandela | Dễ thành tái hiện dự án cũ; dữ liệu chưa rõ | Không ưu tiên |
| VQE/Fermi–Hubbard hoặc materials simulation | Thấp | Phụ thuộc task và tài nguyên | Rất cao | Gần bài toán quantum tự nhiên | Học đồng thời quantum algorithm và materials physics | Không chọn làm case chính |

**Vì sao steel defect đứng trên WiFi?** Cả hai đều phù hợp hồ sơ. Tuy nhiên, ảnh vùng lỗi có pipeline và nhãn đơn giản hơn chuỗi CSI, và không cần hứa tốc độ phản ứng của hệ thống chăm sóc người cao tuổi. Có thể tập trung phần lớn thời gian vào thiết kế phép thử photonic QML. WiFi vẫn rất đáng chọn nếu có sẵn dataset đã làm sạch, subject/session identifiers và baseline hoạt động tốt.

CSI-Bench cho thấy hướng WiFi có dữ liệu nghiên cứu quy mô lớn, nhiều môi trường và task, nhưng đồng thời làm rõ khó khăn generalization ngoài điều kiện kiểm soát.[^17] LiteHAR đã dùng convolution kernels ngẫu nhiên cố định với ridge classifier; do đó “ít tham số và không cần train feature extractor” cũng đã có giải pháp cổ điển nhẹ để so sánh.[^18] Việc học HAR từ CSI không đương nhiên tương thích vật lý hơn với photonics chỉ vì cả hai liên quan sóng.

**Vì sao band gap không đứng đầu?** Đây là một task tốt và dễ lấy dữ liệu công khai. `matbench_expt_gap` có 4,604 mẫu, dự đoán từ composition; `matbench_steels` chỉ có 312 mẫu. Các task có cấu trúc tinh thể và nhãn DFT là những task khác, không được hoán đổi khi so điểm.[^14] Đối với Nam, lợi thế CV/few-shot trực tiếp mạnh hơn kiến thức vật liệu hiện có. Hơn nữa, dự đoán band gap từ composition không tương đương khám phá một semiconductor hữu dụng: vẫn cần xét cấu trúc, điều kiện đo và nhiều tính chất ứng dụng khác.

Nếu buộc chọn vật liệu theo nghĩa dự đoán tính chất, ưu tiên **experimental band-gap regression**, dùng Matbench và baseline composition descriptor, giữ fold chính thức để dễ đối chiếu.[^15] Steel yield strength có tập quá nhỏ để làm lựa chọn đầu tiên khi mục tiêu là một kết luận ổn định trong phỏng vấn. XRD có câu chuyện vật lý hay hơn nhưng cần mentor kiểm tra preprocessing, nhãn pha và các bất biến hợp lý.

**Vì sao không chọn quantum simulation?** Một toy VQE vẫn có thể làm trong vài tuần, nhưng rất khó nối từ toy result đến ứng dụng vật liệu mới có giá trị. Nghiên cứu Fermi–Hubbard quy mô hữu ích mà Quandela giới thiệu là ước lượng tài nguyên cho hệ fault-tolerant tương lai, không phải cấu hình QPU cloud hiện tại.[^19] Với hồ sơ hiện nay, đây là chi phí học cao mà chưa giúp chứng minh ưu thế của ứng viên.

## 6. Định nghĩa đề tài được chọn

**Bối cảnh sử dụng:** kỹ sư chất lượng cần phân loại các vùng lỗi đã xác định trên bề mặt thép. Khi có một đợt dữ liệu ít nhãn, một mô hình có thể học từ ít ví dụ hơn sẽ giảm công gán nhãn và hỗ trợ phân tích lỗi. Đây là giả thuyết giá trị sử dụng cần kiểm chứng với đối tác; chưa có số liệu khách hàng hoặc ROI để khẳng định mức tiết kiệm.

**Câu hỏi nghiên cứu chính:**

> Can a fixed photonic feature map improve steel defect classification under a limited label budget, compared with strong classical feature maps using the same frozen visual encoder, and can the resulting pipeline be validated on Quandela hardware?

**Dataset chính:** NEU-CLS, gồm 1,800 ảnh grayscale 200×200, sáu loại lỗi, mỗi loại 300 ảnh. Dùng bản classification; không nhầm với NEU-DET có bounding boxes. Tập này chứa các lớp lỗi; nó không tự cung cấp bài toán normal-versus-defective đầy đủ.[^10]

**Vai trò của novelty:** QML cho manufacturing defects đã được nghiên cứu bằng QSVM và quantum annealing.[^11] Đề tài đề xuất không tuyên bố phát minh lĩnh vực đó. Đóng góp khảo sát là thử photonic reservoir sau encoder thị giác cố định trong điều kiện ít nhãn, với kiểm soát classical feature maps và kiểm chứng phần cứng. Chưa đủ căn cứ để khẳng định đây là ứng dụng chưa từng có trong nội bộ Quandela.

**Giới hạn domain:** kiểm tra lỗi bề mặt thuộc materials inspection/manufacturing quality. Nó không phải polymer chemistry, dự đoán tính chất khối hoặc quantum simulation vật liệu. Cách liên hệ này nên được nói đúng ngay trong slide.

Không chọn MVTec AD làm dataset chính cho một supervised six-class classifier. Protocol gốc của MVTec dành ảnh bình thường cho training và ảnh có anomaly cho testing; lấy nhãn lỗi từ test để train sẽ đổi bài toán và làm phép so với literature không còn hợp lệ.[^13] MVTec chỉ phù hợp nếu mở một nghiên cứu anomaly detection riêng sau này.

## 7. Phương pháp và thiết kế thí nghiệm

### 7.1. Kiến trúc tối thiểu

```text
Ảnh vùng lỗi
  → encoder thị giác pretrained, đóng băng
  → PCA và scaling chỉ fit trên training subset
  → phase encoding trong photonic circuit cố định
  → tần suất các sự kiện photon được chấp nhận
  → chuẩn hóa đặc trưng bằng thống kê training
  → linear classifier sáu lớp ở máy cổ điển
```

Khởi đầu bằng image encoder CLIP ViT-B/32 cố định để nối với kinh nghiệm hiện có; không cần text branch hoặc prompt engineering trong PoC chính. Ghi rõ checkpoint và nguồn pretraining. Grayscale được đưa qua preprocessing chuẩn của encoder một cách nhất quán; không crop ngẫu nhiên ở evaluation. Đây là lựa chọn triển khai đề xuất, chưa phải kết quả đã xác nhận trên NEU.

Dùng cấu hình pilot **6 mode, 2 photon, 5 đặc trưng pha**, với một mode tham chiếu. Cấu hình mở rộng định trước là **12 mode, 3 photon, 11 đặc trưng pha**, chỉ khảo sát sau khi pilot và kiểm tra khả năng backend ổn định. MerLin reservoir có quy ước số mode tối thiểu bằng số đặc trưng mã hóa cộng một; cấu hình phải được khai báo và kiểm tra cụ thể.[^7]

Circuit có thứ tự `fixed interferometer → data phase shifts → fixed interferometer → measurement`. Lớp trộn trước phase encoding rất quan trọng: đặt phase shifts lên một Fock input cố định rồi chỉ trộn về sau có thể chỉ tạo global phase không mang tín hiệu phân loại. Cần kiểm tra bằng cách thay input và xác nhận phân phối đầu ra thay đổi.

Với postselection giữ đúng số click, tối đa một photon/mode, số đặc trưng là tổ hợp số mode chọn số photon: 15 ở cấu hình 6/2 và 220 ở cấu hình 12/3. Đây là số outcome được sử dụng, không phải số qubit. Raw counts, số mẫu bị loại và xác suất acceptance phải được lưu; chuẩn hóa trên sự kiện hợp lệ không được che chi phí mất photon.

Không đặt kỳ vọng chỉ năm hoặc mười một thành phần PCA luôn đủ. Compression là giả thuyết cần thử. Giữ các baseline trên embedding đầy đủ để biết quantum pipeline có mất tín hiệu quan trọng trước khi vào circuit hay không.

### 7.2. Baseline trả lời những câu hỏi khác nhau

| So sánh | Cấu hình | Mục đích |
|---|---|---|
| Baseline toàn ứng dụng | Embedding đầy đủ + linear classifier; embedding đầy đủ + RBF-SVM | So với cách làm cổ điển thực dụng, không ép baseline chịu bottleneck của QPU |
| Chi phí compression | Cùng PCA input + linear classifier/RBF-SVM | Đo mất mát do nén trước circuit |
| Kiểm soát feature expansion | Cùng PCA input + RFF + linear classifier | Kiểm tra quantum có hơn nonlinear map cổ điển với cùng chiều đầu ra |
| Kiểm soát reservoir | Cùng PCA input + fixed random MLP/ELM + linear classifier | So với feature map cố định có cơ chế huấn luyện tương tự |
| Quantum chính | Cùng PCA input + photonic reservoir + linear classifier | Đo đóng góp của photonic features |
| Quantum resource ablation | Distinguishable-photon simulation với cùng circuit và phép đo | Tìm xem nhiều-photon interference có đóng góp hữu ích không |

Readout trên 15 feature và sáu lớp có 96 tham số gồm bias; trên 220 feature có 1,326 tham số. Đối chứng RFF cùng chiều có cùng số tham số readout. Đây là phép đếm toán học, không phải bằng chứng ngang chi phí: phải báo cáo cả encoder, PCA, fixed map, số feature, sampling và thời gian.

Cùng ngân sách tuning và cùng training/validation/test cho các nhánh. RBF-SVM không nên bị loại chỉ vì không thể so tham số một-một với mạng. So ngân sách dữ liệu và khả năng dự đoán trước, rồi trình bày chi phí phù hợp từng họ mô hình.

Ban đầu `concatenate=False` để dễ đo đóng góp reservoir. Nếu khảo sát nối embedding gốc với reservoir ở giai đoạn sau, nhánh classical cũng phải được nối embedding với RFF tương ứng. Không cho quantum thêm thông tin hoặc thêm feature mà baseline không có đối chứng.

### 7.3. Protocol ít nhãn và tránh leakage

Chia năm outer folds stratified sau khi kiểm tra ảnh trùng/gần trùng. Mỗi fold có khoảng 60 ảnh mỗi lớp làm test; training pool còn lại không được tự động dùng hết. Nếu tìm thấy ảnh liên quan cùng mẫu hoặc metadata theo lô, split theo nhóm trước; khi đó số ảnh mỗi fold có thể thay đổi.

Đề xuất ba ngân sách **tổng nhãn mỗi lớp**: 12, 24 và 48, tương ứng train/validation là 8/4, 16/8 và 32/16. Như vậy không gọi một thí nghiệm là “16-shot tổng cộng” nếu đã dùng thêm tám nhãn validation. Các ảnh còn lại trong pool không tham gia fitting PCA hay huấn luyện trong protocol chính.

Lặp ba lần chọn subset và ba reservoir seeds định trước. Bắt đầu thí nghiệm nhỏ ở một fold để kiểm tra runtime, sau đó mới chạy protocol khóa. Encoder pretrained cố định dùng chung mọi nhánh. PCA, scaling, lựa chọn hyperparameter và các statistics khác chỉ học từ dữ liệu cho phép trong fold; tuyệt đối không fit PCA trên cả dataset vì không cần nhãn.

Metric chính: macro-F1; thêm balanced accuracy và per-class recall. Báo cáo learning curve theo tổng nhãn, không chỉ một điểm tốt nhất. Giữ một baseline dùng nhiều nhãn hơn làm tham chiếu; chỉ nói “cần ít nhãn hơn” khi hai đường cong cho phép so tại cùng chất lượng và có độ bất định kèm theo.

Kết quả phải ghép cặp theo fold/subset. Không coi hàng trăm seed là hàng trăm dataset độc lập. Có thể báo cáo fold-level differences, phân tán và khoảng bất định với resampling nêu rõ giả định; mọi kết luận vẫn chỉ được xác nhận trên benchmark này. Chênh lệch nhỏ hơn biến thiên split/seed là kết quả chưa phân biệt được, không phải thắng.

### 7.4. Hai loại robustness riêng biệt

**Ảnh đầu vào:** dùng một tập corruption định trước gồm brightness/contrast, blur nhẹ và noise, trên những ảnh test đã giữ riêng. Giữ cùng transform cho mọi mô hình. Đây là sensitivity test; không gọi nó là chứng minh hoạt động trên một nhà máy mới.

**QPU:** khảo sát finite sampling, photon loss, distinguishability và phase error ở các mức có căn cứ từ backend hoặc ghi rõ là synthetic stress test. Không sử dụng một noise setting làm đẹp kết quả rồi coi đó là đặc tính vật lý thực của máy.

Chỉ mở rộng sang miền ảnh khác sau khi có dataset độc lập, taxonomy nhãn phù hợp và đủ thời gian. NEU một mình không chứng minh generalization theo nhà máy, camera hoặc quy trình sản xuất.

### 7.5. Đường tới hardware và ngân sách

Reservoir cố định cho phép tính quantum features một lần cho mỗi input/circuit rồi cache, huấn luyện readout nhiều lần ở máy cổ điển. Cách này tránh vòng lặp optimizer gọi QPU ở mỗi batch. Khi đổi PCA, seed circuit hoặc noise setting, cache tương ứng không còn dùng lại được.

Quy trình đề xuất: ideal local simulation → finite-shot/noisy simulation → remote simulator → QPU subset cố định. Freeze preprocessing, circuit và readout trước hardware test. Nếu cần hiệu chỉnh readout bằng hardware, dùng một calibration subset tách biệt; không chỉnh bằng test labels. Quota và backend capability phải xác nhận ngay tuần đầu.

Phân biệt **accepted samples** với **raw shots/attempts**. Nếu cần S mẫu hợp lệ cho mỗi input và xác suất acceptance là a, số lần thử kỳ vọng xấp xỉ S/a. Ví dụ kế hoạch, không phải số đo: 360 input × 2,000 mẫu hợp lệ = 720,000 accepted samples; với a=0.1 sẽ cần khoảng 7.2 triệu raw attempts. Cloud batching, giới hạn job và overhead phải được tính thêm.

Sweep 500/2,000/8,000 accepted samples trên validation ở simulator để khảo sát tradeoff. Không mặc định các mức này đủ cho mọi phân phối. Hardware pilot bắt đầu bằng một subset nhỏ chọn trước, cân bằng theo lớp và không chọn theo mức dễ; mở rộng theo quota đo được. Dùng estimator của backend khi có, lưu acceptance thực tế và job metadata.[^8]

So QPU với finite-shot simulation bằng độ lệch phân phối, thay đổi prediction và metric kèm uncertainty. Một QPU subset nhỏ xác nhận đường thực thi và mức tương thích; không đủ để tuyên bố đã xác nhận accuracy toàn benchmark hoặc toàn ứng dụng. Không hứa realtime, speedup hay năng lượng thấp hơn nếu chưa đo end-to-end.

## 8. Kế hoạch 8–12 tuần và quyết định tiếp tục

| Thời gian | Công việc trọng tâm | Đầu ra và điểm quyết định |
|---|---|---|
| Tuần 1 | Tải và audit NEU-CLS; kiểm tra source/licence, duplicate; xác nhận backend và quota | Dataset manifest, mô tả phạm vi sử dụng, cấu hình simulator/QPU; có đường chạy tiny circuit |
| Tuần 2 | Encoder cố định, full-embedding baselines và kiểm tra compression | Baseline đáng tin; khóa split, nhãn, metrics và tuning budget trước quantum sweep |
| Tuần 3–4 | Reservoir pilot và đối chứng RFF/ELM; learning curve | Xác định tín hiệu lợi ích, underfitting hoặc bottleneck; dừng việc tăng quy mô nếu không có căn cứ |
| Tuần 5–6 | Chạy protocol nhiều fold/seed; finite-shot và noise; resource ablation | Báo cáo lợi ích, uncertainty, độ nhạy và chi phí; chọn một cấu hình để kiểm chứng hardware |
| Tuần 7–8 | Remote simulator và QPU pilot/subset theo quota | Pipeline thực thi, hồ sơ sampling, simulator–hardware comparison và go/no-go memo |
| Tuần 9–10 nếu có | Thêm lần kiểm chứng độc lập; mở rộng tập QPU nếu quota cho phép | Kiểm tra độ bền của kết luận, không chỉ thêm cấu hình để tìm điểm đẹp |
| Tuần 11–12 nếu có | Một ablation bổ sung hoặc dataset độc lập có nhãn phù hợp; đóng gói | Repo tái chạy được, limitations, báo cáo nghiên cứu và đề xuất giai đoạn tiếp theo |

**Thành công về feasibility:** có pipeline tái lập từ ảnh đến photonic features và output; chạy được trên backend mục tiêu nếu được cấp quyền; biết phạm vi tài nguyên, mức sai lệch hardware và kết quả so baseline. Nếu chỉ hoàn thành simulator, cần ghi rõ hardware feasibility chưa được xác nhận.

**Thành công về utility:** ở một vùng ngân sách dữ liệu được định trước, phương pháp có lợi ích so baseline cổ điển mạnh, hoặc đạt chất lượng tương đương với tradeoff tài nguyên có giá trị đã đo. Cạnh tranh với linear head yếu đơn lẻ không đủ.

Một ngưỡng nghiên cứu đề xuất để thảo luận với team là cải thiện khoảng **2 điểm phần trăm macro-F1** so baseline mạnh ở ít nhất hai mức nhãn, xu hướng cùng chiều ở đa số outer folds và khoảng bất định của chênh lệch hỗ trợ kết luận. Đây là **ngưỡng quyết định đề xuất**, không phải kết quả kỳ vọng, yêu cầu khách hàng hoặc chứng cứ rằng mức tăng đó sẽ xảy ra. Trước khi chạy, khóa ngưỡng phù hợp với variance pilot và chi phí thực tế; không đổi sau khi xem test.

**Điều kiện dừng hoặc giới hạn đầu tư:** RFF/RBF-SVM liên tục ngang hoặc hơn; quantum thắng chỉ khi bỏ baseline embedding đầy đủ; lợi ích biến mất khi đo bằng số shot khả thi; compression làm mất tín hiệu quá nhiều; hoặc chi phí lấy mẫu vượt quota. Kết quả âm vẫn tạo giá trị nếu chỉ ra được nguyên nhân và giúp tránh đầu tư tiếp vào một cấu hình không hiệu quả.

Nếu baseline đã gần trần chất lượng ở ít nhãn, không cố thêm quantum để tạo lý do. Có thể hoàn thành một hardware feasibility benchmark nhỏ, ghi nhận không có utility case trên NEU và xin dữ liệu khó hơn từ nhu cầu thực tế. Không tự động quét nhiều dataset rồi chỉ công bố nơi quantum thắng.

## 9. Chuẩn bị đến buổi phỏng vấn

Mục tiêu vài ngày trước phỏng vấn là **lập luận chắc, sơ đồ đúng và kế hoạch có thể thực thi**. Không cần hoàn thành dự án 8–12 tuần. Đề xuất lịch kể từ thời điểm khảo sát 11/09/2026:

| Ngày | Việc ưu tiên | Sản phẩm tối thiểu |
|---|---|---|
| 12/09 | Đọc MerLin reservoir, remote execution và paper QORC v2; kiểm tra dữ liệu | Giải thích được pipeline, bằng chứng và giới hạn; chạy tiny local circuit nếu môi trường sẵn |
| 13/09 | Chuẩn bị baseline và một pilot nhỏ nếu kịp | Dataset/encoder/split rõ ràng; kết quả sơ bộ phải ghi đúng số mẫu và giới hạn |
| 14/09 | Viết khoảng 10 slide, luyện phản biện | Mỗi slide một thông điệp; nguồn ở slide liên quan; phân biệt planned với observed |
| 15/09 trước giờ họp | Chạy thử bài nói và Q&A | Có thể trình bày 12–15 phút rồi dành thời gian thảo luận; đây là thời lượng đề xuất, chưa được công ty xác nhận |

Nếu setup hoặc tải dữ liệu tốn nhiều thời gian, ưu tiên proposal và hiểu circuit thay vì chạy một benchmark vội thiếu đối chứng. Một smoke test ít mẫu có thể minh họa kỹ năng học nhanh; không dùng nó để tuyên bố hiệu quả khoa học.

Các kiến thức cần nắm trước buổi họp:

- Phân biệt photon, optical mode, qubit và Fock occupation; giải thích cấu hình 6 mode/2 photon bằng hình.
- Beam splitter, phase shifter và giao thoa; tại sao cần trộn trạng thái trước lớp phase encoding.
- Reservoir cố định và readout học ở classical computer; cache đặc trưng có lợi thế vận hành gì.
- Vì sao simulator có probability lý tưởng còn QPU phải ước lượng bằng counts.
- Tại sao photon loss, bunching/postselection, indistinguishability và finite shots ảnh hưởng giá thành cũng như prediction.
- Vì sao sampling khó về tính toán không tự suy ra classification tốt hơn hoặc toàn pipeline nhanh hơn.
- Phân biệt few-label budget, train labels, validation labels và pretraining data.
- Number factorization thuộc quantum algorithms; không dùng nó làm ví dụ về lợi ích QML cho image classification.

Tài liệu ôn trước đây về continuous-variable QML hữu ích để mở rộng kiến thức, nhưng case này nên bám **discrete-variable photonic circuit, single-photon/Fock inputs, interferometer và photon detection**. Không đưa displacement, squeezing hoặc homodyne thành phần bắt buộc của một workflow Quandela nếu chưa xác nhận backend hỗ trợ.

## 10. Mạch trình bày khoảng 10 slide

| Slide | Tiêu đề đề xuất | Nội dung phải làm rõ |
|---|---|---|
| 1 | Application choice | Chọn low-label steel defect classification; một câu research question; giới hạn 8–12 tuần |
| 2 | Industrial task and data | Người sử dụng, giá trị nhãn, NEU-CLS; sáu loại lỗi; không giả định có normal class |
| 3 | Why this application | So ngắn với WiFi và property prediction; liên hệ vài kỹ năng thực sự đã có |
| 4 | Evidence and open question | QORC có hardware precedent; RFF vẫn cạnh tranh; giả thuyết còn cần kiểm chứng |
| 5 | Hybrid architecture | Encoder cố định → nén → reservoir → counts → classifier; khoanh phần quantum |
| 6 | Photonic implementation | 6 mode/2 photon pilot; phase encoding, fixed mixing, valid counts; đường remote |
| 7 | Fair evaluation | Tổng nhãn, splits, baseline đầy đủ và baseline ngang chiều, macro-F1 |
| 8 | Hardware and resource validation | Finite shots, acceptance, noise, simulator/QPU subset; quota và tradeoff |
| 9 | 8–12 week execution | Milestones, gates, deliverables; phương án khi không có utility hoặc QPU bị chậm |
| 10 | Decision and expected contribution | Điều kiện tiếp tục; giá trị của kết quả dương/âm; đóng góp Nam có thể trực tiếp thực hiện |

Nguồn đặt ngay slide dùng claim. Không dùng một slide sources riêng làm mất một trong mười slide chính; có thể thêm bibliography và circuit details ở appendix nếu cần. Nếu có biểu đồ pilot, ghi rõ “preliminary”, số mẫu, split, số seed và phạm vi mô phỏng. Không vẽ đường quantum luôn thắng để minh họa một kỳ vọng rồi để người nghe tưởng là kết quả.

## 11. Câu trả lời mở đầu và phản biện

### Bản mở đầu tiếng Anh

> I would investigate low-label steel surface defect classification using a hybrid photonic quantum reservoir. The practical question is whether a fixed photonic feature map can help a small classifier learn from fewer labelled defect images. This connects directly to my experience with few-shot learning, compact models and controlled evaluation.
>
> I would use a frozen visual encoder, compress its features, and encode them into phase shifts in a small photonic circuit. Only the classical readout would be trained initially. In eight to twelve weeks, I would establish strong classical baselines, test data efficiency and sampling sensitivity in simulation, and validate a fixed configuration on Quandela hardware, subject to access.
>
> I would not assume quantum advantage. Random Fourier features and RBF-SVM are essential controls. The deliverable would be a reproducible feasibility study and a clear decision on whether the measured benefit justifies further development.

### Những câu hỏi có khả năng xuất hiện

**“Why not use a classical model?”** Classical là baseline mặc định và có thể là kết luận cuối. Thí nghiệm kiểm tra xem photonic map có tạo ra tradeoff hữu ích ở ít nhãn không. Nếu một classical map rẻ hơn đạt cùng chất lượng thì chưa có lý do ứng dụng để dùng quantum.

**“What exactly is quantum here?”** Chuẩn bị Fock input, tiến hóa qua interferometer phụ thuộc dữ liệu và sampling photon detection. Encoder, PCA và classifier vẫn chạy classical. Đặt trọng tâm vào phần có thể vẽ và giải thích; không nói toàn bộ network chạy trên QPU.

**“Where is the novelty?”** Đóng góp đề xuất là một đánh giá hướng ứng dụng và chuyển sang photonic hardware với điều kiện ít nhãn, fair controls và resource accounting. Quantum defect classification nói chung đã có nghiên cứu. Tính mới để publish cần khảo sát tiếp; case interview không cần hứa một thuật toán chưa từng tồn tại.

**“Is this materials science?”** Đây là materials inspection. Nếu ưu tiên của nhóm là materials property prediction hoặc simulation thì cần chọn một task tương ứng. Không dùng từ vật liệu để che sự khác nhau về mục tiêu khoa học.

**“Why not polymer classification or band gap?”** PolyT là nguồn tham khảo tốt, nhưng tái hiện cùng target sẽ cần chứng minh phần mở rộng và có dữ liệu. Band gap là phương án hợp lý khi có mentor/domain requirement; ở thời điểm này, defect images tận dụng kinh nghiệm trực tiếp hơn và giảm khối lượng phải học trong vài ngày chuẩn bị.

**“Why a frozen reservoir instead of a trainable QNN?”** Nó giảm số thành phần phải tối ưu và cho phép cache quantum features; cả circuit execution lẫn readout đều có đường triển khai rõ. Một shallow trainable quantum layer có thể là ablation về sau, huấn luyện trong simulator. Không gọi việc freeze reservoir là bảo đảm không có mọi vấn đề generalization hoặc noise.

**“Would photons give an advantage because the input is an image?”** Không. Đây là ảnh đã số hóa và đặc trưng cổ điển được mã hóa thành phase. Sự giống nhau về tên “optical” không chứng minh ưu thế tính toán hoặc hiệu quả dự đoán.

**“How do you isolate the quantum contribution?”** Giữ nguyên encoder và input compression; so RFF/ELM cùng chiều; so baseline embedding đầy đủ; dùng resource ablation trong simulator. Cải thiện sau một nonlinear map có thể đến từ feature expansion nói chung. Distinguishable-photon control cũng không thay thế toàn bộ baseline cổ điển mạnh.

**“Can this run in real time on a production line?”** Chưa có căn cứ. PoC hướng tới nghiên cứu và phân loại theo lô; phải đo cả sampling và remote overhead trước khi nói về realtime. Một deployment route về sau có thể là học offline, nhưng nếu dùng distillation sang classical student phải đánh giá nó như giai đoạn nghiên cứu riêng.

**“What if the quantum model loses?”** Xác định có mất tín hiệu ở compression, kém hơn classical feature map, overfit readout hay không chịu được finite shots. Nếu kiểm soát đều hợp lệ và không có lợi ích, khuyến nghị dừng đầu tư vào cấu hình đó. Một báo cáo âm tốt hữu ích hơn một thắng lợi do baseline yếu.

**“What if QPU access is delayed?”** Tiếp tục ideal/noisy simulation và remote simulator, giữ cấu hình hardware-compatible. Báo cáo phần nào đã xác nhận và phần hardware nào còn pending. Không đổi tên simulator result thành hardware demonstration.

**“How will this save money?”** Chưa có customer data để tính ROI. Thước đo gần nhất là số nhãn cần đạt một mức chất lượng, cùng chi phí QPU và compute. Muốn đổi sang tiền phải có thời gian gán nhãn thực tế, chi phí sai loại và sản lượng từ đối tác.

## 12. Các điều kiện có thể làm thay đổi lựa chọn

| Thông tin mới | Ảnh hưởng tới quyết định |
|---|---|
| Công ty có task vật liệu đang mở, dataset và mentor | Ưu tiên task thật đó; cân nhắc band gap hoặc target đã được đối tác xác định |
| Nam đã có HAR pipeline tái lập, metadata người/phòng và dataset quen thuộc | WiFi CSI có thể lên vị trí số 1; rủi ro preprocessing và protocol giảm đáng kể |
| Chỉ có simulator, chưa có quota QPU | Vẫn nghiên cứu được nhưng điều chỉnh deliverable hardware; không coi quyền truy cập là có sẵn |
| NEU baseline gần trần hoặc low-dimensional compression thất bại | Thu hẹp thành feasibility benchmark; cần nhu cầu/data mới trước khi tiếp tục tuyên bố utility |
| Hội đồng yêu cầu world-first application | Cần novelty search chuyên biệt; không khẳng định đề tài hiện tại thỏa điều kiện đó |

Khuyến nghị chung không dựa trên việc tên đề tài nghe gần “quantum” nhất. Nó ưu tiên một dự án mà ứng viên có thể lý giải từ dữ liệu, mô hình, phép đo đến quyết định nghiên cứu. Trọng tâm gây ấn tượng là năng lực chuyển bằng chứng thành một thí nghiệm kiểm chứng được.

## Nguồn và phạm vi kiểm chứng

Nguồn công khai được kiểm tra trong ngày 11/09/2026. Ưu tiên tài liệu chính thức, paper gốc và trang dataset của tác giả. Các proposal, thời gian, cấu hình circuit và ngưỡng quyết định trong báo cáo là thiết kế đề xuất, không phải kết quả đã chạy. Trang chính thức NEU dẫn tới archive `NEU-CLS.rar` trên Google Drive; chưa tải và audit archive trong lần khảo sát này. Chưa xác nhận quota/token, cấu hình QPU của công ty hoặc khả năng chạy package trên máy hiện tại.

[^1]: Quanova. Email “[Quanova] Case-study interview”, 11/09/2026. Nội dung do ứng viên cung cấp; nguồn riêng tư, không có URL công khai. Dùng để xác định đề bài, số slide và thời hạn.

[^2]: “Impromptu Google Meet Meeting – September 11”, transcript do ứng viên cung cấp, các đoạn 11:13–17:06, 27:02–27:24 và 32:23. Bản chép tự động có lỗi; dùng cho ngữ cảnh, không coi mọi câu là trích dẫn nguyên văn chính xác.

[^3]: Nguyễn Ngô Nhật Nam. CV Quanova hiện tại, `NguyenNgoNhatNam_CV_Quanova.tex`, và thông tin dự án đã được ứng viên cung cấp. Nguồn riêng tư; dùng cho đánh giá kinh nghiệm, không phải kiểm định độc lập toàn bộ thành tích.

[^4]: Notton, C., et al. [MerLin: A Discovery Engine for Photonic and Hybrid Quantum Machine Learning](https://arxiv.org/abs/2602.11092v2), 2026, v2 17/04/2026. Tác giả ghi nhận accepted tại IJCNN/WCCI 2026. Dùng cho mục tiêu reproducibility và hệ sinh thái ML.

[^5]: Quandela. [Predicting polymer behaviour with quantum machine learning: Lessons from the PolyT project](https://www.quandela.com/resources/blog/predicting-polymer-behaviour-quantum-machine-learning-polyt/), 02/07/2026. Báo cáo trực tiếp của đơn vị tham gia dự án; dùng cho tiền lệ materials QML, không suy thành lợi thế phổ quát.

[^6]: Rambach, M., et al. [Photonic Quantum-Accelerated Machine Learning](https://arxiv.org/html/2512.08318v2), arXiv, v2 11/08/2026, Table 1 và Sections II.5–II.6. Dùng cho hardware precedent và đối chứng RFF. Bản v2 có nội dung baseline khác bản v1; cần đọc đúng phiên bản.

[^7]: MerLin 0.4 documentation. [ReservoirClassifier](https://merlinquantum.ai/0.4/user_guide/models/reservoir_classifier.html). Dùng cho fixed feature map, quy ước input/modes, caching và classical readout. Ví dụ API có thể chứa tên argument cũ; khi triển khai đối chiếu release notes và package cài thực tế.

[^8]: MerLin 0.4 documentation. [MerlinProcessor User Guide](https://merlinquantum.ai/0.4/user_guide/remote_execution.html), đặc biệt Gradient Propagation và Estimating Required Shots. Dùng cho giới hạn remote gradients và kế hoạch thực thi. Không mặc định cam kết v0.5 đã có hiệu lực.

[^9]: MerLin 0.4 documentation. [Hardware-Aware QML Guidelines](https://merlinquantum.ai/0.4/user_guide/hardware_design_checklist.html). Dùng cho phase encoding, measured output và simulator-to-QPU workflow. Khả năng detector cuối cùng phải xác nhận theo backend cụ thể.

[^10]: Song, K., and Yan, Y., Northeastern University. [NEU surface defect database](https://faculty.neu.edu.cn/songkechen/zh_CN/zdylm/263270/list/index.htm), trang dataset chính thức; liên quan publication gốc 2013. Dùng cho 1,800 ảnh, sáu lớp, kích thước ảnh và phân biệt NEU-CLS/NEU-DET.

[^11]: Guijo, D., et al. [Quantum artificial vision for defect detection in manufacturing](https://arxiv.org/abs/2208.04988), arXiv, 2022; bản sửa 05/01/2024. Dùng để xác nhận prior art với gate-based QSVM/quantum annealing; không ngoại suy kết quả sang photonics.

[^12]: Bowles, J., Ahmed, S., and Schuld, M. [Better than classical? The subtle art of benchmarking quantum machine learning models](https://arxiv.org/abs/2403.07059), 2024. Dùng cho yêu cầu kiểm soát baseline và giới hạn diễn giải benchmark nhỏ.

[^13]: Bergmann, P., Fauser, M., Sattlegger, D., and Steger, C. [MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection](https://www.mvtec.com/fileadmin/Redaktion/mvtec.com/company/research/datasets/mvtec_ad.pdf), CVPR 2019. Dùng cho protocol normal training/anomalous testing; không phải MVTec AD 2.

[^14]: Matminer documentation. [Table of Datasets](https://hackingmaterials.lbl.gov/matminer/dataset_summary.html), mục `matbench_expt_gap`, `matbench_steels` và bảng tổng hợp. Dùng cho target, modality và số mẫu; không dùng phiên bản docs để khẳng định môi trường cài đặt đã sẵn.

[^15]: Dunn, A., Wang, Q., Ganose, A., Dopp, D., and Jain, A. [Benchmarking materials property prediction methods: the Matbench test set and Automatminer reference algorithm](https://www.nature.com/articles/s41524-020-00406-3), npj Computational Materials 6, 138, 2020. Dùng cho phương pháp benchmark và nguyên tắc so theo protocol phù hợp.

[^16]: Adams, F., Zhu, D., Steuerman, D. W., Kusne, A. G., and Takeuchi, I. [Quantum Kernel Machine Learning for Autonomous Materials Science](https://arxiv.org/html/2601.11775v1), arXiv, 16/01/2026, Sections II.1–II.3 và III.2. Dùng cho XRD/IonQ và giới hạn so sánh; chưa mặc định là paper đã phản biện.

[^17]: Zhu, G., et al. [CSI-Bench: A Large-Scale In-the-Wild Dataset for Multi-task WiFi Sensing](https://arxiv.org/abs/2505.21866), 2025; bản v2 ghi nhận accepted tại NeurIPS. Dùng cho dữ liệu nhiều môi trường và khó khăn generalization.

[^18]: Salehinejad, H., and Valaee, S. [LiteHAR: Lightweight Human Activity Recognition from WiFi Signals with Random Convolution Kernels](https://arxiv.org/abs/2201.09310), ICASSP 2022. Dùng cho baseline CSI dùng random kernels và ridge classifier.

[^19]: Quandela. [Spin-Optical Quantum Computing for Fermi–Hubbard Simulation](https://www.quandela.com/resources/blog/spin-optical-quantum-computing-fermi-hubbard-simulation/), 2026; thảo luận Bourdoncle et al., arXiv:2605.05315. Dùng để phân biệt resource estimation fault-tolerant với PoC trên QPU hiện có.
