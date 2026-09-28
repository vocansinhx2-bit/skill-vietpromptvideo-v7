# 48 — BODY, HANDS & GROUP INTEGRITY
Prevent duplicate subjects, extra limbs, orphan hands, merged bodies, headcount changes and broken locomotion.

## 48.1 Headcount lock
- Ghi số người chính xác và thứ tự trái→phải trong mọi shot có ≥2 người: "Exactly three people: [A] frame-left, [B] center, [C] frame-right."
- Nhắc lại headcount sau mỗi cut, sau che khuất, sau khi camera đổi góc.
- Đám đông nền: "background crowd stays out of focus and does not interact with [A]."
- Người vào/ra khung: ghi cạnh vào/ra và thời điểm; không ai tự xuất hiện hay biến mất.

## 48.2 Duplicate subject
- Mỗi entity một handle duy nhất, dùng nguyên văn suốt prompt; không đổi sang từ đồng nghĩa.
- Không tả cùng một người/vật hai lần ở hai chỗ bằng hai cách khác nhau.
- Entity có nhiều reference → gán vai rõ cho từng ảnh (module 17).
- Câu khóa: "Only one [A] exists in the scene." / "There is a single [prop]."
- Cảnh gương/phản chiếu: "The mirror shows only [A]'s reflection, matching her movement."

## 48.3 Hands
- Giới hạn hành động tay ≤2 nhân vật mỗi shot.
- Mỗi tay vào khung có chủ, bên (trái/phải), tay áo, điểm vào và điểm về.
- Close-up tay: "There are only two hands in frame, both belonging to [A]: left hand in the [sleeve] holds…, right hand…"
- Tay chạm vật: ghi điểm tiếp xúc và lực (module 15). Tay không cầm gì: ghi tư thế nghỉ.
- Tránh: đan tay phức tạp, nhiều ngón làm việc riêng, tay lướt nhanh qua nhau.

## 48.4 Contact và ôm, chen, đánh nhau
- Tiếp xúc giữa 2 người: ghi ai chạm ai, bằng tay nào, vào đâu; giữ 2 thân thể tách biệt: "their bodies stay distinct; no merging."
- Ôm/đỡ: chọn góc thấy rõ 2 đầu, 2 cặp vai.
- Chuỗi đánh nhau: mỗi động tác có vector ("lands facing the window"); tốc độ thực; cắt insert tay/chân để nối.

## 48.5 Locomotion
- Đi bộ: "heel lands first, strict left-right alternation, one foot always on the ground, no gliding."
- Chạy: "both feet leave the ground briefly each stride, arms swing opposite to legs."
- Đi đôi: "shoulder to shoulder, on one depth line, same pace."
- Cầu thang/cửa: ghi lối đi là vật bắt buộc; nhân vật không xuyên tường/đồ đạc.
- Tracking cùng bước đi qua nhiều shot: lặp nguyên văn tốc độ tuyệt đối ("the camera tracks alongside at a steady walking pace, 2 m away").

## 48.6 Anatomy khác
- Tư thế ngồi/nằm: ghi điểm tiếp xúc với ghế/sàn.
- Góc cực đoan (từ dưới lên, foreshortening) ở close-up tay/chân → rủi ro cao; đổi góc nếu không bắt buộc.
- Trẻ em/động vật nhiều chân: giữ hành động đơn giản, camera ổn định.

## 48.7 Mã lỗi
DUPLICATE_SUBJECT, EXTRA_LIMB, HEADCOUNT_CHANGE, BODY_MERGE, WALK_GLITCH → sửa theo module 42.2.
