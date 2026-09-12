# Runbook bài nói 10 phút

## Nhịp trình bày

| Slide | Thời gian | Mốc kết thúc | Việc phải hoàn thành |
| --- | ---: | ---: | --- |
| 1 | 0:45 | 0:45 | Nêu application, ba lý do chọn và giới hạn pilot |
| 2 | 0:45 | 1:30 | Chứng minh nhu cầu thật và benchmark sạch |
| 3 | 1:00 | 2:30 | Chỉ rõ phần photonic và trạng thái xác minh |
| 4 | 1:20 | 3:50 | Nêu Pass A, Pass B và stop rule |
| 5 | 1:00 | 4:50 | Tách pilot đã xong khỏi dự án 12 tuần |
| 6 | 0:55 | 5:45 | Trình bày kết quả chính, không overclaim |
| 7 | 0:55 | 6:40 | Chẩn đoán PCA và comparator mạnh |
| 8 | 0:45 | 7:25 | Chốt finite-shot và phần chưa kiểm thử |
| 9 | 0:50 | 8:15 | Đặt ranh giới simulation/hardware |
| 10 | 0:55 | 9:10 | Đưa khuyến nghị có điều kiện |
| Dự phòng | 0:50 | 10:00 | Chuyển slide, khoảng dừng, câu hỏi chen ngang |

Speaker notes khoảng 840 từ. Với tốc độ kỹ thuật 90–100 từ/phút và các khoảng dừng ngắn, bài nói nằm trong khoảng 9:15–10:00.

## Câu chuyển slide

1. **1 → 2:** “The choice matters only if the constraint is real and the test is measurable.”
2. **2 → 3:** “That defines the task; now I will show where photonics enters.”
3. **3 → 4:** “A runnable simulation is only a starting point, so I need a rule that can reject it.”
4. **4 → 5:** “Those gates define the proposed project; the pilot is already complete.”
5. **5 → 6:** “Here is what the pilot actually found.”
6. **6 → 7:** “The controlled comparison shows where the gap comes from.”
7. **7 → 8:** “Before proposing hardware, I tested whether sampling is stable.”
8. **8 → 9:** “These results define the current evidence boundary.”
9. **9 → 10:** “That boundary leads to a conditional recommendation.”

## Bốn câu không được làm mờ

- “MerLin is a separate code path, not external replication.”
- “Repeated test evaluations still share one outer fold.”
- “Pass A is evaluated at 48 labels per class.”
- “Simulation-pipeline feasibility is demonstrated; hardware feasibility remains untested.”

## Cắt khi bị chậm

- Sau phút 3 mà chưa tới slide 4: bỏ chi tiết công thức ở slide 3.
- Sau phút 5 mà chưa tới slide 6: không đọc seed IDs hoặc toàn bộ từng giai đoạn trên slide 5.
- Sau phút 7 mà chưa tới slide 8: ở slide 7 chỉ nói PCA mất 0,07–0,10 và Q1 kém RBF-SVM khoảng 0,05.
- Còn dưới 75 giây ở slide 9: nói đúng một câu về simulation/hardware rồi chuyển slide 10.
- Không cắt qualifier MerLin, “one outer fold”, hai pass gate, hoặc giới hạn hardware.

## Cách nói

- Trên slide 4, chỉ theo thứ tự Pass A → Pass B → Stop; nhấn rằng shots/acceptance chỉ thuộc Pass B.
- Trên slide 6–8, nói kết luận trước rồi mới dùng số để chứng minh.
- Dừng nửa giây trước câu “hardware remains untested” và trước khuyến nghị cuối.
- Kết thúc bằng “Thank you” rồi chờ câu hỏi.
