# Luyện Q&A cho phỏng vấn

## Vì sao chọn bài toán này?

NEU-CLS là bài toán thị giác công nghiệp nhỏ nhưng đủ sáu lớp để kiểm tra học ít nhãn. Encoder đóng
băng tận dụng kinh nghiệm computer vision hiện có, còn feature map photonic tạo một cầu nối cụ thể
sang công việc quantum optics mà không giả vờ rằng simulator đã là phần cứng.

## Quantum đóng góp ở đâu?

Quantum circuit chỉ thay lớp feature map: năm thành phần PCA điều khiển pha, hai photon truyền qua
`U D(x) U`, và 15 xác suất collision-free đi vào linear readout. B1–B6 tách ảnh hưởng của embedding,
compression, nonlinearity và số chiều.

## Nếu quantum không thắng?

Đó vẫn là kết quả hữu ích. Tôi sẽ phân tích chênh lệch ghép cặp, acceptance, finite-shot variance và
chi phí. Nếu RFF/RBF tốt hơn ổn định, quyết định kỹ thuật đúng là không dùng circuit này cho use case
hiện tại, hoặc thay đổi giả thuyết trong một protocol exploratory được ghi rõ.

## Đây có phải quantum advantage không?

Không. Pilot dùng một dataset nhỏ, một outer fold và ideal simulation. Một claim mạnh hơn cần nhiều
fold, matched compute/resource accounting, noise, statistical unit đúng và QPU verification.

## Cần tài nguyên gì trong 8–12 tuần?

GPU chủ yếu dùng để trích xuất encoder một lần; simulator/QPU cần đo riêng. QPU work chỉ bắt đầu sau
khi khóa circuit, xác nhận quota, shot definition, calibration metadata và cách thu kết quả thô.
