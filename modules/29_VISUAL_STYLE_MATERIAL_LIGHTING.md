# 29 — VISUAL STYLE, MATERIAL & LIGHTING
Express style through observable material, surface, lighting, color, capture and environment cues.
Avoid adjective clouds.
Separate style invariants from content variables so a series can vary without losing visual DNA.

## 29.1 Đoạn ánh sáng riêng
Mỗi prompt có một đoạn ánh sáng riêng gồm: hướng sáng + chất sáng (cứng/mềm) + độ tương phản + nguồn sáng thực.
Đoạn này ảnh hưởng chất lượng hình nhiều hơn các tag như cinematic, 8K.

## 29.2 Màu ba lớp
- Base tone: màu nền diện rộng.
- Secondary tone: màu gắn với chủ thể.
- Accent: 1–2 điểm nhấn nhỏ.

## 29.3 Vật liệu và chất lỏng
- Mô tả bề mặt nhìn thấy: brushed steel with fine scratches, wet asphalt reflecting neon.
- Chất lỏng ghi điểm kết thúc chuyển động: the stream lands on the butter, divides around it, pools on the plate and does not flow uphill.
- Vải/tóc: ghi hướng gió hoặc lực tác động.

## 29.4 Khóa phong cách cho series
Tách `STYLE_INVARIANTS` (ống kính, bảng màu, chất sáng, grain) khỏi `CONTENT_VARIABLES` (địa điểm, hành động). Chỉ lặp khối invariant nguyên văn giữa các clip.
