# Runbook bài nói 12 phút

## Nhịp tổng thể

| Slide | Thời gian | Mốc kết thúc | Mục tiêu duy nhất |
| --- | ---: | ---: | --- |
| 1 | 0:55 | 0:55 | Nêu ứng dụng, lý do chọn và giới hạn của pilot |
| 2 | 0:55 | 1:50 | Chứng minh bài toán có nhu cầu thật và benchmark sạch |
| 3 | 1:15 | 3:05 | Giải thích phần nào chạy photonic và trạng thái xác minh |
| 4 | 1:30 | 4:35 | Đưa tiêu chí pass/fail định lượng |
| 5 | 1:15 | 5:50 | Tách pilot đã xong khỏi kế hoạch 12 tuần |
| 6 | 1:05 | 6:55 | Trình bày kết quả chính, không overclaim |
| 7 | 1:05 | 8:00 | Chẩn đoán PCA và các comparator |
| 8 | 0:55 | 8:55 | Chốt finite-shot và phần chưa kiểm thử |
| 9 | 0:55 | 9:50 | Nêu ranh giới bằng chứng và bottleneck thật |
| 10 | 1:05 | 10:55 | Đưa khuyến nghị có điều kiện |
| Dự phòng | 1:05 | 12:00 | Ngắt nhịp, đổi slide, câu hỏi chen ngang |

Speaker notes trong deck là bản script chính. Bản hiện tại khoảng 1.040 từ; với tốc độ kỹ thuật 95–105 từ/phút, cộng chuyển slide và các khoảng dừng có chủ ý, bài nói nằm trong khoảng 11:30–12:15.

## Câu chuyển slide nên học thuộc

1. **1 → 2:** “The choice matters only if the constraint is real and the test is measurable.”
2. **2 → 3:** “That defines the task; now I will show exactly where photonics enters.”
3. **3 → 4:** “A runnable circuit is only a starting point, so I need a rule that can reject it.”
4. **4 → 5:** “Those gates define the future project; the pilot itself is already complete.”
5. **5 → 6:** “Here is what that pilot actually found.”
6. **6 → 7:** “The headline gap is real, but the controlled comparison shows where it comes from.”
7. **7 → 8:** “Before proposing hardware, I also tested whether sampling is operationally stable.”
8. **8 → 9:** “Together, those results set a clear evidence boundary.”
9. **9 → 10:** “That boundary leads to a conditional recommendation.”

## Ba câu phải nói nguyên ý

- “A separate implementation path is not external replication.”
- “The current pilot uses one outer test fold; repeated evaluations do not create independent folds.”
- “The thresholds on slide four are prospective go/no-go criteria, not thresholds fitted after seeing the pilot.”

## Cắt nội dung khi bị chậm

- Nếu hết phút 5 mà chưa sang slide 5: bỏ đọc seed IDs trên slide 4; chỉ nói validation-only selection và hai pass gates.
- Nếu hết phút 8:30 mà chưa sang slide 8: trên slide 7 chỉ nêu hai con số tròn, PCA mất 0.07–0.10 và Q1 kém RBF-SVM khoảng 0.05.
- Nếu còn dưới 90 giây ở slide 9: nói một câu về ba tầng bằng chứng rồi chuyển ngay slide 10.
- Không cắt caveat “one outer fold”, qualifier MerLin, hoặc câu “no advantage yet”.

## Cách trình bày

- Dừng nửa giây sau kết quả `0.8708`, sau mỗi tiêu chí pass, và trước khuyến nghị cuối.
- Trên slide 4, chỉ tay theo thứ tự: question banner → Pass A → Pass B → Stop.
- Trên slide 6–8, nói kết luận trước, rồi mới đọc số hỗ trợ.
- Kết thúc bằng “Thank you” và im lặng; không tự thêm một đoạn tóm tắt thứ hai.
