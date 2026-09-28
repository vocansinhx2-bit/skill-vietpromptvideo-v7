# 22 — SPATIAL LEDGER & SCREEN GEOGRAPHY
Track stable landmarks, subject sides, entry/exit direction, prop positions and camera relation.
For multi-character scenes protect screen direction and interaction ownership.
Do not repair spatial contradictions with vague cinematic language.

## 22.1 Orientation Ledger (bắt buộc khi có nhân vật)
Mỗi entity, mỗi segment/shot có một dòng:

| Field | Giá trị | Ví trí trong prompt |
|---|---|---|
| FRAME_SIDE | frame-left / center / frame-right, foreground / background | STARTING STATE |
| BODY_FACING | toward camera / three-quarter left / three-quarter right / profile left / profile right / back to camera | STARTING STATE + mỗi segment có thay đổi |
| HEAD_FACING | cùng bộ giá trị BODY_FACING; chỉ ghi khi khác thân | cùng dòng |
| EYELINE_TARGET | entity / object / off-screen point có hướng (off-screen left) / lens | mỗi segment |
| MOTION_VECTOR | frame-left→frame-right, toward camera, away from camera, static | mỗi segment có di chuyển |
| HANDEDNESS | tay thuận + tay đang cầm vật gì | khi có đạo cụ |
| ASYMMETRIC_MARKS | phụ kiện/vết/đường rẽ tóc nằm bên trái hay phải CƠ THỂ nhân vật | CHARACTER LOCK |

Quy ước bắt buộc:
- Hướng màn hình dùng `frame-left / frame-right` (theo người xem).
- Bên cơ thể dùng `her left hand / his right shoulder` (theo nhân vật). Không trộn hai hệ trong cùng một câu.
- Hướng quay mặt dùng thế giới hoặc khung hình: `facing frame-right, toward the window`. Không viết `facing left` trơn.

## 22.2 Luật xoay người và đổi hướng
- Nhân vật giữ nguyên BODY_FACING cho tới khi có câu hành động xoay riêng.
- Xoay là một hành động có thời lượng: nêu chiều xoay, góc, tốc độ và hướng kết thúc.
  `She turns slowly over her right shoulder, about 90 degrees, until she faces the camera.`
- Không xoay >90° trong một segment nếu reference không có góc nghiêng/lưng; nếu cần 180°, chia 2 bước hoặc bổ sung reference side/back view (module 19).
- Sau khi quay lưng hoặc bị che khuất: nhắc lại CHARACTER LOCK và hướng mặt mới ngay câu đầu segment kế.
- Chuyển động không được có "đảo chiều ngầm": nếu hành động xong sớm, model hay phát ngược để lấp thời gian. Nối 2–3 hành động cùng chiều cho đủ segment hoặc ghi hướng kết thúc rồi `holds still`.

## 22.3 Eyeline và nhìn nhau
- Hai người đối thoại: A frame-left facing frame-right, B frame-right facing frame-left. Lặp lại câu này ở mọi segment cận (MCU/CU), không chỉ ở wide.
- Shot ngược (reverse) giữ eyeline: A nhìn ra frame-right, B nhìn ra frame-left, cả khi người kia ngoài khung.
- Nhìn vật: ghi rõ vật và vị trí (`looks down at the phone in her right hand`), không viết `looks at it`.
- Nhìn camera chỉ khi có chủ đích (vlog, talking head): `looks directly into the lens`. Mặc định: `does not look at the camera`.

## 22.4 Lật gương (mirror flip)
Nguyên nhân: ảnh selfie bị lật, pose trung tính khiến model tự diễn giải, reference nhiều góc lệch nhau, framing đối xứng.
Chặn:
- Kiểm reference trước khi upload: chữ trên áo/biển có đọc xuôi không, đường rẽ tóc và phụ kiện đúng bên. Ảnh selfie lật lại trước khi dùng.
- Ghi dấu hiệu bất đối xứng vào CHARACTER LOCK: `scar above her left eyebrow, watch on her right wrist, hair parted on her left`.
- Thêm câu khóa: `No mirrored features. Keep the watch on her right wrist throughout.`
- Chữ trong cảnh (biển hiệu, logo): `All text reads left to right, not mirrored.`
- First/last frame: kiểm hai ảnh cùng hướng; nếu last frame lật, model sẽ xoay/biến hình nhân vật giữa clip.

## 22.5 Layout không gian (khi có cửa, hành lang, đồ vật chắn)
Viết một khối SPATIAL LAYOUT ngắn trước TIMELINE:
- Vị trí camera và hướng nhìn: `The camera is inside the kitchen, facing the closed back door.`
- Vật cản giữa người và camera: `The counter sits between her and the camera.`
- Đường đi: `She walks around the counter from frame-left to frame-right; she never passes through it.`
- Cửa/lối đi là vật bắt buộc: `The doorway stays open and visible on frame-right throughout.`

## 22.6 Đa shot và nhiều clip
- Hướng di chuyển thế giới giữ nguyên qua cut: nhân vật rời khung ở frame-right thì vào shot sau từ frame-left.
- Clip nối tiếp: câu đầu nhắc hướng lại dù đã có last frame: `She is on frame-left, facing frame-right, mid-stride.`
- Tốc độ đi/xe giữ bằng số tuyệt đối, lặp nguyên văn trong từng prompt: `walks at a steady slow pace, about 4 km/h`. Không viết `same speed as Shot 2`.
- Camera ở cùng phía trục trong cả scene (module 23.4).

## 22.7 Runtime phrases (English, chèn trực tiếp)
- `[A] stays on frame-left and [B] stays on frame-right for the entire clip.`
- `[A] faces frame-right toward [B]; [B] faces frame-left toward [A].`
- `She keeps facing the window until 6 seconds, then turns toward the camera.`
- `He never turns his back to the camera.`
- `No mirrored features, no side swap.`

## 22.8 Failure codes
- `ORIENTATION_UNDECLARED`: nhân vật không có BODY_FACING ở STARTING STATE.
- `SIDE_SYSTEM_MIXED`: trộn frame-left và "her left" trong một câu.
- `UNSCHEDULED_TURN`: hướng mặt đổi giữa segment mà không có hành động xoay.
- `EYELINE_BREAK`: reverse shot có eyeline trùng hướng.
- `MIRROR_RISK`: reference chưa kiểm lật hoặc CHARACTER LOCK không có dấu bất đối xứng.
- `LAYOUT_MISSING`: cảnh có cửa/vật cản/đường đi mà không có SPATIAL LAYOUT.
