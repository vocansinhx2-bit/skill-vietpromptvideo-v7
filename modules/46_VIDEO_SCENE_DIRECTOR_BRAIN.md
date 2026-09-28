# 46 — VIDEO SCENE DIRECTOR BRAIN

> Bộ não điều phối cho `BUILD_VIDEO_PROMPT`. Nhận một ý tưởng cảnh bất kỳ (1 câu hoặc 1 đoạn) → quyết định setup video trước khi viết chữ nào của prompt. Chạy SAU module 01 (intent) và TRƯỚC module 11 (Video IR). Kết quả của bộ não là input cho IR, không phải prompt cuối.
> Target reader của module này: `HUMAN_DESIGNER` / skill. Không đưa tên module, archetype ID hay lý do vào prompt video (module 32).

## 46.1 Nguyên tắc
1. Setup trước, chữ sau. Thiết kế sai không cứu bằng prose (SKILL §15).
2. Mỗi segment timeline = 1 thay đổi chính + 1 end state nhìn thấy được.
3. Một segment chỉ có 1 motion owner: camera HOẶC chủ thể là chuyển động chính.
4. Năng lực model chỉ lấy từ `model_profiles/`. Không chắc → chọn đường bảo thủ.
5. Thiếu dữ liệu → điền mặc định + ghi giả định cho người dùng, không chặn luồng. Mặc định: bối cảnh Mỹ, Seedance 2.5, 9:16 nếu short-form, 720p, audio bật.
6. Cảnh vượt budget → `SIMPLIFY → SPLIT → REDESIGN → ĐỔI REFERENCE → ĐỔI SHOT → WORDING`.

## 46.2 Pipeline suy luận (tuần tự)
| Bước | Việc | Output |
|---|---|---|
| V1 | Scene DNA | 12 trường (46.3) |
| V2 | Archetype | 1 archetype chính + tối đa 2 phụ (46.4) |
| V3 | Runtime plan | tổng thời lượng, số clip, độ dài mỗi clip (46.5) |
| V4 | Input mode | T2V / first-frame / first+last / reference / edit / extend (46.6) |
| V5 | Reference map | mỗi asset 1 vai hẹp + negative transfer (module 17/18) |
| V6 | Timeline | segment liên tục, không chồng, mỗi segment có "Ends with" (46.7) |
| V7 | Camera + performance | 1 camera intention/segment, cảm xúc ngoại hoá thành hành vi |
| V8 | Dialogue + audio | ai nói, lúc nào, ai ngậm miệng; track audio tách (46.8) |
| V9 | Risk + guard | top 3 lỗi dự đoán + câu chặn cụ thể |
| V10 | Compile | Video IR → prompt theo profile (module 40) |

## 46.3 V1 — Scene DNA (12 trường)
`who` (nhân vật/động vật/vật thể chính, số lượng) · `where` (địa điểm + bố cục không gian) · `when` (giờ, thời tiết, mùa) · `core_action` (1 động từ chính) · `secondary_actions` · `emotion_arc` (đầu → cuối) · `initial_state` · `end_state` · `dialogue` (có/không, bao nhiêu câu, ngôn ngữ) · `audio_intent` (ambience/SFX/nhạc/không nhạc) · `duration_target` · `delivery` (nền tảng, aspect).
Trường P0 bắt buộc có giá trị hoặc giả định: `who`, `where`, `core_action`, `end_state`, `duration_target`. Thiếu mà không ghi giả định = `SCENE_DNA_INCOMPLETE`.

## 46.4 V2 — Archetype library
Mỗi archetype: cách chia segment · mode khuyên dùng · rủi ro chính · câu chặn.

### VA01 — Hội thoại 2–3 người
- Chia: 1 câu thoại / 1 người nói / segment 5–8s. Master → OTS A → OTS B nếu cần cắt; one-take thì camera khoá, người nói luân phiên.
- Mode: reference (1 ảnh sạch 1 người / nhân vật) hoặc first-frame master.
- Rủi ro: nói nhầm người, miệng nhép cả hai, đổi chỗ ngồi, đổi trang phục.
- Chặn: "Only [A] speaks in this segment; [B] keeps mouth closed and listens." Screen geography cố định: A frame-left, B frame-right trong toàn cảnh.

### VA02 — Hành động / đánh nhau / thể thao / nhảy
- Chia: mỗi segment 1 pha tiếp xúc (chuẩn bị → tiếp xúc → hệ quả → phục hồi). Giới hạn 2–3 pha lớn / 10s.
- Mode: reference (identity) + video ref cho vũ đạo/camera nếu có.
- Rủi ro: tay chân thừa, nhân đôi người, tiếp xúc giả, slow-motion tự phát.
- Chặn: viết nguyên nhân trước phản ứng; "no duplicated limbs, no extra fighters, real-time speed, no slow motion". Ưu tiên chuyển động chậm, liên tục; năng lượng dồn vào camera/cắt.

### VA03 — Xe cộ / rượt đuổi / trong xe đang chạy
- Chia: tách ngoại cảnh (xe chạy) và nội cảnh (trong cabin). Nội cảnh: camera gắn cố định trong xe, cảnh ngoài cửa trôi đều 1 hướng.
- Rủi ro: xe đổi màu/mẫu, cảnh ngoài chạy ngược, người lái đổi bên.
- Chặn: khai báo tay lái (Mỹ = ghế lái bên trái), hướng di chuyển frame-left→frame-right giữ suốt; "same car model and color throughout".

### VA04 — Đám đông / nhiều nhân vật
- Chia: 1–3 nhân vật chính rõ nét, đám đông là nền mềm. Không giao hành động riêng cho người nền.
- Rủi ro: nhân vật chính hoà vào đám đông, clone mặt.
- Chặn: nhân vật chính có màu/trang phục phân biệt + vị trí khung cố định; "background crowd stays soft-focus and does not interact with [A]".

### VA05 — Vật lý / VFX: lửa, nước, khói, nổ, mưa, tuyết, vỡ
- Chia: nguồn → lan → điểm dừng. Mỗi segment 1 hiện tượng chính.
- Rủi ro: chất lỏng chảy ngược, lửa lan vô lý, mảnh vỡ tự biến mất.
- Chặn: mô tả nơi chuyển động KẾT THÚC ("pools on the floor and stops"); lửa/khói có hướng gió cố định. Cảnh nguy hiểm thật (cháy nhà có người) → module 30 compliance: không mô tả thương tích.

### VA06 — Biến đổi / timelapse / before-after
- Chia: camera khoá tuyệt đối; mỗi segment 1 stage với 1 progress marker không hồi quy.
- Mode: first+last (START/END từ skill ảnh) hoặc chain nhiều clip.
- Rủi ro: camera trôi, tiến độ lùi, vật tạm (công cụ) còn sót ở END.
- Chặn: "locked-off camera, identical framing"; mỗi segment "Ends with: [stage state]".

### VA07 — Reveal
- Chia: chi tiết bí ẩn → chuyển động hé lộ → toàn cảnh. Reveal ở ~60–75% thời lượng, không ở frame cuối.
- Chặn: "the camera does not reveal [X] until [trigger]".

### VA08 — Nhảy thời gian / lão hoá
- Chia: mỗi mốc tuổi 1 clip riêng + 1 reference riêng; không lão hoá liên tục trong 1 segment dài trừ khi là hiệu ứng chủ đích.
- Rủi ro: đổi danh tính thay vì đổi tuổi.
- Chặn: giữ neo danh tính (cấu trúc mặt, màu mắt, vết sẹo) + liệt kê chính xác cái gì thay đổi (tóc, da, dáng).

### VA09 — Sản phẩm hero / packshot
- Mode: reference ảnh sản phẩm (chỉ lấy thiết kế) — "Do not copy the studio background".
- Rủi ro: logo/nhãn biến dạng, nhân đôi sản phẩm.
- Chặn: "exactly one [product] throughout; label text stays unchanged and readable"; camera chậm, ánh sáng có đoạn riêng.

### VA10 — POV / handheld / selfie / vlog
- Chia: 1 người nói vào camera, handheld nhẹ; không first+last (handheld tự do mâu thuẫn end frame cố định).
- Chặn: "handheld selfie framing at arm's length, subtle natural shake, no cuts".

### VA11 — Close-up cảm xúc
- Chia: 1 thay đổi cảm xúc / segment, ngoại hoá thành cơ thể (vai, tay, ánh mắt, hơi thở).
- Chặn: cấm tính từ cảm xúc trần; viết hành vi.

### VA12 — Establishing / drone / toàn cảnh
- Chia: 1 chuyển động camera duy nhất (push/orbit/rise), chủ thể tĩnh hoặc chuyển động nhỏ.

### VA13 — Chuyển cảnh / match cut / seamless transition
- Seedance 2.5 hỗ trợ transition liền mạch; khai báo hình dạng/vị trí khớp giữa 2 cảnh và thời điểm chuyển.
- Chặn: chỉ 1 biến đổi mạnh qua cut.

### VA14 — Montage
- Chia: "Shot 1 / Shot 2 / ..." mỗi shot 2–4s, 1 hình ảnh 1 hành động; nhạc làm trục nhịp.

### VA15 — Tay thao tác chính xác (nấu ăn, nhạc cụ, gõ phím, lắp ráp)
- Rủi ro: ngón thừa, vật đổi tay.
- Chặn: close-up ổn định; "[object] stays in the right hand"; thao tác chậm, ít bước.

### VA16 — Động vật
- Chặn: 1 con vật chính, giống/màu/dấu hiệu nhận dạng cố định; hành vi tự nhiên của loài, không nhân hoá trừ khi phong cách hoạt hình.

### VA17 — Đêm / ít sáng / mưa / gương / kính
- Chặn: đoạn ánh sáng riêng (nguồn, hướng, nhiệt màu); phản chiếu trong gương phải khớp người thật; mưa có hướng cố định.

### VA18 — Chữ / màn hình / UI trong khung
- Chặn: chữ ngắn, đặt trong ngoặc 【 】 nếu là phụ đề; màn hình điện thoại thì nội dung tối giản; thêm "No subtitles" nếu không muốn chữ tự sinh.

### VA19 — Sinh vật / phép thuật / fantasy
- Chặn: reference cho sinh vật; hiệu ứng phép có nguồn, màu và điểm dừng; quy luật thế giới khai báo 1 lần trong closing constraints.

### VA20 — Không khớp archetype
- Phân rã theo động từ: liệt kê mọi động từ → gom thành segment 1 động từ chính → áp luật chung. Không bỏ qua; ghi `ARCHETYPE_UNROUTED` nếu chưa phân rã.

## 46.5 V3 — Runtime plan
- Seedance 2.5: 1 clip 4–30s. Chia segment 5–10s; dưới ~4s mỗi segment dễ bị vội, trên ~10s dễ sinh "chờ/lặp/slow-motion".
- Công thức: `so_segment ≈ ceil(duration / 8)`; mỗi segment phải có đủ hành động cho độ dài của nó.
- Khi tổng > 30s hoặc cần nhiều địa điểm/ngày khác nhau → nhiều clip, nối bằng last frame (`return_last_frame`) hoặc extend.
- Seedance 2.0: tối đa 15s, dùng `Shot N`, không ép timestamp chính xác.
- Thoại có lip-sync: mỗi câu 5–8s, 1 người nói/segment; cảnh thoại dài → tách clip.

## 46.6 V4 — Cây quyết định input mode
```
Có ảnh first frame đã duyệt (skill ảnh)?
├─ Không → Có asset nhân vật/sản phẩm/địa điểm cần giữ?
│         ├─ Có → REFERENCE mode (@Image/@Video/@Audio, vai hẹp)
│         └─ Không → TEXT-TO-VIDEO
└─ Có → Shot cần end state chính xác (timelapse, đặt vật đúng chỗ, loop)?
          ├─ Có → FIRST+LAST (last cùng aspect; aspect tự adaptive)
          └─ Không → Cần giữ thêm nhân vật/sản phẩm bằng ảnh riêng?
                    ├─ Có → REFERENCE mode, dùng ảnh first frame làm @Image1
                    │       + "Use @Image1 as the exact first frame"
                    └─ Không → FIRST-FRAME
Có video nguồn cần sửa cục bộ → EDIT. Cần nối tiếp video → EXTEND.
```
Luật cứng: first/last-frame và reference mode loại trừ nhau trong cùng 1 request. Gửi cả hai = `REFERENCE_VS_LASTFRAME_CONFLICT`. Handheld tự do + first+last = `VIDEO_MODE_MISMATCH`.

## 46.7 V6 — Luật timeline
- Segment liên tục, không chồng, phủ đủ thời lượng.
- Timestamp là ngân sách nhịp, không phải điểm cắt frame.
- Mỗi segment: hành động + camera + (thoại) + (âm thanh) + `Ends with: [vị trí người, ai cầm gì, trạng thái khung]`.
- Segment sau kế thừa `Ends with` của segment trước.
- Không mô tả cùng một hành động hai lần.
- Không đặt đỉnh hành động ở giây 0 hoặc giây cuối.

## 46.8 V8 — Thoại & audio
- Thoại trong `{ }` hoặc ngoặc kép, kèm người nói, ngôn ngữ, thời điểm. "Her mouth moves only during her own lines."
- Ngôn ngữ mặc định cho bối cảnh Mỹ: "Dialogue language: American English."
- Số viết bằng chữ; một cảm xúc/tông mỗi câu.
- Audio tách: ambience, SFX `< >`, nhạc `( )`. Không muốn nhạc: "No background music." Không muốn chữ: "No subtitles."
- Shot có lip-sync: medium close-up, mặt chính diện, camera gần như khoá.

## 46.9 Output — Video Setup Plan
Dùng `templates/video_setup_plan_template.md`. Plan là design-time; chỉ phần "Prompt" cuối cùng là runtime và phải qua purity gate.

## 46.10 Failure codes (module 46)
| Code | Ý nghĩa |
|---|---|
| `SCENE_DNA_INCOMPLETE` | Trường P0 trống mà không ghi giả định |
| `ARCHETYPE_UNROUTED` | Không gán archetype và không phân rã theo động từ |
| `VIDEO_MODE_MISMATCH` | Input mode không hợp nhu cầu shot |
| `REFERENCE_VS_LASTFRAME_CONFLICT` | Gửi first/last-frame cùng reference mode |
| `SEGMENT_UNDERFILLED` | Segment dài nhưng quá ít hành động → chờ/lặp/slow-motion |
| `SEGMENT_OVERLOADED` | Segment có >1 thay đổi chính hoặc camera + chủ thể cùng chuyển động mạnh |
| `SPEAKER_AMBIGUITY` | Không rõ ai nói / ai ngậm miệng |
| `DUPLICATE_ACTION_DESCRIPTION` | Cùng hành động mô tả 2 lần → lặp trong video |

## 46.11 Checklist trước khi compile
- [ ] Scene DNA đủ P0 (hoặc giả định)
- [ ] Archetype + lý do một dòng
- [ ] Mode hợp lệ theo profile, không trộn first/last với reference
- [ ] Mỗi asset có 1 vai hẹp + negative transfer
- [ ] Segment liên tục, mỗi segment có Ends with
- [ ] Không segment nào quá tải hoặc thiếu hành động
- [ ] Thoại có người nói + thời điểm + người im lặng
- [ ] Top 3 rủi ro có câu chặn
