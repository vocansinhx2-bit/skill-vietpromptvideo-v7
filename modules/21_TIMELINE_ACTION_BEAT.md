# 21 — TIMELINE & ACTION-BEAT COMPILER
Use temporal blocks only when they improve control.
Each block should contain a small coherent action set and inherit prior end state.
Avoid dense second-by-second choreography unless the model/task genuinely benefits.

## 21.1 Khi nào dùng timestamp
| Model | Cú pháp ưu tiên | Ghi chú |
|---|---|---|
| Seedance 2.5 | `0-5 seconds:` / `(0:00–0:05)` | Timestamp phản hồi tốt; dùng cho MV, sync-cut, cảnh nhiều hành động |
| Seedance 2.0 | `Shot 1 / Shot 2 / Shot 3` | Timestamp chính xác không ổn định; để model tự nhịp |
| Model chưa rõ | Pha tuần tự không có số giây | Compile bảo thủ |

Clip ≤ 6s có một hành động: không cần timestamp.

## 21.2 Luật block
- Block liên tục, không chồng lấn, tổng = duration.
- Timestamp là ngân sách thời gian cho sự kiện, không phải điểm cắt frame-level.
- Mỗi block: một thay đổi chính + dòng `Ends with:` ghi vị trí người, ai giữ vật gì, trạng thái khung hình.
- Block sau bắt đầu từ trạng thái `Ends with:` của block trước.
- Block quá ít việc → model tự bịa thêm (lặp, chờ, slow motion). Block quá nhiều việc → model bỏ qua giữa hoặc vội tới kết.
- Không mô tả cùng một hành động hai lần ở hai block.

## 21.3 Mật độ khuyến nghị
| Độ dài block | Nội dung hợp lý |
|---|---|
| 2–4s | 1 hành động ngắn hoặc 1 câu thoại ngắn |
| 5–8s | 1 hành động chính + 1 phản ứng, hoặc 1 câu thoại + micro-action |
| 8–12s | 1 chuỗi hành động có 2–3 tiếp xúc vật lý |
| >12s | Tách block |

Clip 30s mặc định 3–5 block.

## 21.4 Nhân quả trong block
Viết theo thứ tự: tiếp xúc → chuyển động kết quả → âm thanh → phản ứng.
Không viết phản ứng trước nguyên nhân.
