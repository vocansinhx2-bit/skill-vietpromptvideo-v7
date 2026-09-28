# 53 — ANIMATION STYLE ENGINE
Dựng video hoạt hình ở mức chuyên nghiệp: chọn đúng họ phong cách, khóa style bằng tham số, dịch nguyên lý hoạt hình thành câu model làm theo được, và chặn style trôi về ảnh thật.
Chạy sau module 49 khi playbook là G13 hoặc brief có chữ hoạt hình / anime / cartoon / 3D stylized / claymation / stop-motion. Bật kèm 29 (style, palette) và 18 (reference khác style).

## 53.1 Luật nền
- Model mặc định về ảnh thật khi không có chỉ dẫn style → câu đầu tiên của prompt là MEDIUM LINE nêu kỹ thuật hoạt hình.
- Lặp nguyên văn medium line + một cụm palette cố định trong mọi clip của cùng dự án.
- Một họ phong cách mỗi clip. Không trộn từ vựng 2D vẽ tay với từ vựng 3D render; trộn → kết quả rơi về bán ảnh thật.
- Không trộn nhân vật ảnh thật với bối cảnh hoạt hình (hoặc ngược lại) trừ khi user khai báo đó là ý đồ.
- Mô tả style bằng kỹ thuật + thời kỳ + bảng màu + chất liệu, không bằng tên studio, franchise hay đạo diễn (rủi ro kiểm duyệt và bản quyền). Viết "anime" chung chung không kèm tham số → model trả về khuôn mặt trung bình, nên luôn nêu trường phái bằng tham số.

## 53.2 Họ phong cách
| Họ | Medium line (câu mở) | Camera grammar | Ánh sáng | Nhịp chuyển động | Loại trừ bắt buộc |
|---|---|---|---|---|---|
| `3D_STYLIZED_FEATURE` | "stylized 3D animated feature look, soft subsurface skin, exaggerated appealing proportions" | được dùng ngôn ngữ ống kính (mm, dolly, depth of field) | global illumination mềm, rim light màu | mượt, squash & stretch vừa phải | photoreal skin pores, uncanny realistic faces |
| `2D_CEL_ANIME` | "hand-drawn 2D cel animation, crisp cel-shaded characters over a painted background" | rostrum: pan qua nền vẽ, parallax lớp, push-in trên held frame | vẽ: bóng cel 2 tông, rim là mảng rõ | on twos, bùng on ones cho khoảnh khắc chính, held frames | lens blur, depth of field, bokeh, handheld, 3D CG face |
| `2D_CLASSIC_HAND_DRAWN` | "traditional hand-drawn 2D animation, fluid ink lines, painted watercolor backgrounds" | rostrum, multiplane | mềm, bóng ít | full animation mượt, arcs rõ | 3D shading, photoreal texture |
| `PAINTERLY_STORYBOOK` | "illustrated storybook animation, watercolor and gouache texture, visible paper grain" | pan/tilt chậm qua tranh | ánh sáng vẽ, bloom nhẹ | chậm, ít chuyển động | sharp CG edges, photoreal lighting |
| `STOP_MOTION_CLAY` | "stop-motion clay animation, handmade puppets, visible fingerprints in the clay, miniature set" | ống kính macro, bàn quay nhỏ | ánh sáng studio thu nhỏ, bóng cứng | hơi giật, xúc giác (on twos) | smooth motion blur, CG sheen |
| `LOW_POLY_TOON_3D` | "low-poly 3D toon render, flat-shaded facets, bold outline" | camera 3D đơn giản | phẳng, bóng cứng | snappy | photoreal, painterly texture |
| `MOTION_GRAPHICS_FLAT` | "flat vector motion graphics, clean geometric shapes, limited palette" | 2D phẳng, không chiều sâu | không bóng hoặc bóng phẳng | ease in/out rõ | gradients photoreal, textured noise |

## 53.3 Mười hai nguyên lý → câu prompt
| Nguyên lý | Câu model làm theo được |
|---|---|
| Squash & stretch | "her body squashes on landing and stretches on the jump" |
| Anticipation | "she crouches and pulls her arm back before the throw" |
| Staging | "one character in a clear silhouette against a simple background" |
| Straight ahead / pose to pose | "snappy key poses with quick transitions" hoặc "continuous fluid flowing motion" |
| Follow-through & overlapping | "hair, scarf and coat tails keep settling after her body stops" |
| Slow in / slow out | "the motion eases in and eases out" |
| Arcs | "the arm swings along a smooth arc" |
| Secondary action | "while she talks, her fingers tap the table" (một hành động phụ, vùng nhỏ) |
| Timing | "animated on twos", "a burst on ones for the key move", "a held frame on her expression" |
| Exaggeration | "eyes widen to twice their size for one beat, then return" |
| Solid drawing | "consistent volume and proportions from every angle" |
| Appeal | "rounded friendly shapes, large readable eyes" |

Chỉ đưa vào prompt 2–4 nguyên lý phục vụ trực tiếp beat của clip; không liệt kê cả 12.

## 53.4 Style lock block (bắt buộc với anime / 2D)
1. Tham số style: độ dày và màu nét ("thin colored contour lines"), số bậc bóng ("two-step cel shading with a translucent mid-shadow"), lớp highlight ở mắt và tóc, độ phản xạ riêng cho vải/da/kim loại/kính.
2. Danh sách loại trừ: các style lân cận không được xuất hiện ("photoreal, semi-photoreal, smooth plastic 3D CG, generic 3D face, thick black outlines, flat single-layer shadow, muddy colors"). Thiếu danh sách → anime rơi về khuôn mặt 3D chung chung.
3. Khóa nhân vật & palette: mỗi nhân vật có màu chính / màu phụ / màu nhấn / motif chất liệu; cấm trao đổi màu giữa các nhân vật.
4. Sân khấu: nền tối hơn nhân vật một bậc; màu đặc trưng của nhân vật làm màu key light và màu bóng của chính họ.
5. Camera và hành động (53.5–53.6).
6. Hiệu ứng (nếu có): màu lõi/viền của từng hiệu ứng, "hand-drawn effects animation with hard graphic shapes", nhịp on twos, impact frame ở CONTACT (54.8).

## 53.5 Camera trong hoạt hình
- 2D: camera là rostrum trên tranh. Dùng "pan across the painted background", "foreground layer slides faster than the distant background" (parallax), "slow push-in on a held face", "vertical tilt down the painted tower". Cấm lens, mm, bokeh, depth of field, handheld, dolly, lens breathing.
- 3D stylized và stop-motion: được dùng ngôn ngữ ống kính như live-action (49.6), giữ chuyển động camera chậm.
- Một chuyển động camera có động cơ mỗi shot.

## 53.6 Hành động kiểu anime (sakuga grammar)
- Nhịp nỗ lực xen kẽ: "a burst of fluid full animation as she turns, then a held frame on her expression".
- "animated on twos" là nhịp nền; "on ones" chỉ cho khoảnh khắc trình diễn.
- Va chạm: "a single high-contrast impact frame on the hit".
- Tốc độ: "speed lines streak the background during the dash", "her arm smears across the swing", nền cuộn thay vì camera lao.
- Follow-through: tóc, vải, dây túi tiếp tục lắng sau khi thân dừng.
- Nhắc lại thông số bóng trong segment tốc độ cao, nếu không bóng cel thoái hóa thành ánh sáng thật.
- Mặt chảy trong cảnh nhanh → đẩy tốc độ vào speed lines, smear, nền cuộn; cắt sang held impact frame; giữ mặt ở held frame.
- Choreography vẫn theo module 52 (initiator, contact, reaction, frame side) — chỉ đổi ngữ pháp hình ảnh.

## 53.7 Ánh sáng và màu (ánh sáng được vẽ)
- 2D: "hard two-tone cel shadow", "rim light drawn as a clean shape along the jaw", "specular drawn as a white wedge in the eye".
- Nêu palette và bề mặt hoàn thiện: "limited warm palette, paper texture", "flat color with painted light bloom", "1990s hand-painted TV-anime look with light film grain".
- 3D stylized: key/fill/rim theo module 29, màu bão hòa hơn live-action một bậc.

## 53.8 Âm thanh cách điệu
- Whoosh trên smear, sting trên impact frame, room tone tắt trong held frame.
- Foley phóng đại vừa phải cho cartoon; anime giữ ambience rõ và nhạc mỏng.

## 53.9 Chống style drift và vỡ nhân vật
- Giới hạn mỗi clip: một hành động chính + một chuyển động phụ + một chuyển động camera đơn giản.
- Chuyển động phụ chỉ ở vùng nhỏ: đuôi tóc, tay áo, hơi nước, mưa, gấu vải.
- Tránh xoay nhanh, xoay toàn thân, đổi phối cảnh lớn, handheld mạnh — chúng tăng rủi ro vỡ thiết kế.
- Khi lỗi: giảm hành động hoặc chuyển động camera trước; không thêm danh sách phủ định dài.
- Cấm chữ, logo, UI, biển hiệu trong nền (nền hoạt hình dễ sinh chữ méo).
- Duyệt cả clip, không chỉ frame đầu: mắt đổi kích cỡ, cằm nhấp nháy, nét viền "sôi".

## 53.10 Reference cho hoạt hình
- Có artwork sẵn → image-to-video; ảnh nguồn neo frame đầu. Chỉ dùng artwork user có quyền sử dụng.
- Ảnh sạch: một tư thế đọc được, khoảng trống quanh bộ phận chuyển động; tránh ngón tay bị cắt, phụ kiện chồng nhau, chữ trong nền, nhiều nhân vật chồng tay chân.
- Câu preserve chỉ nêu anchor không được đổi: dáng mặt, màu mắt, độ dày viền, silhouette tóc, mảng trang phục, đạo cụ đặc trưng, palette.
- Nhiều nhân vật: character sheet riêng mỗi người, một reference mỗi danh tính (17).
- Reference ảnh thật cho nhân vật hoạt hình → chỉ lấy tư thế/bố cục, ghi rõ "not authoritative for rendering style" (18).

## 53.11 Nối clip hoạt hình
- Lưu mỗi shot: ảnh nguồn đã duyệt, frame cuối, prompt nguyên văn.
- Layout cuối của clip đã duyệt = layout mở của clip sau; giữ hướng màn hình và chuyển động đang mở.
- Lặp nguyên văn medium line, palette phrase, danh sách loại trừ trong mọi clip.

## 53.12 Mã lỗi hoạt hình
| Mã | Dấu hiệu | Sửa |
|---|---|---|
| `STYLE_UNNAMED` | prompt không có medium line → ra ảnh thật | thêm medium line ở câu đầu |
| `STYLE_MIX` | trộn 2D và 3D, hoặc người thật trong nền hoạt hình | một họ phong cách |
| `LENS_GRAMMAR_IN_2D` | mm/bokeh/depth of field trong prompt 2D | đổi sang rostrum grammar |
| `PHOTOREAL_DRIFT` | clip dần thành bán ảnh thật | lặp medium line + thông số bóng trong segment nhanh; thêm loại trừ |
| `BOILING_LINES` | viền nhấp nháy, mặt biến dạng | giảm hành động/camera; một hành động chính |
| `FLOATY_MOTION` | chuyển động trôi, thiếu lực | "on twos", held frames, smear, anticipation |
| `FACE_MELT_ACTION` | mặt chảy khi đánh/chạy | tốc độ vào speed lines/nền cuộn; held impact frame |
| `PALETTE_SWAP` | nhân vật đổi màu hoặc lấy màu của nhau | khóa màu chính/phụ/nhấn từng nhân vật |
| `STUDIO_NAME_RISK` | prompt ghi tên studio/franchise | thay bằng kỹ thuật + thời kỳ + palette |
| `EXCLUSION_LIST_MISSING` | anime/2D không có danh sách loại trừ | thêm 53.4 mục 2 |
| `EFFECT_STYLE_DRIFT` | hiệu ứng 2D thành glow ảnh thật | thêm 53.4 mục 6, module 54.8 |
