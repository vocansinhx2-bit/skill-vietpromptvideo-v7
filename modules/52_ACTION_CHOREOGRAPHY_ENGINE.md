# 52 — ACTION CHOREOGRAPHY ENGINE
Biến một ý tưởng hành động (đánh nhau, rượt đuổi, đấu kiếm, stunt) thành chuỗi trao đổi đòn mà model video đọc và dựng được: ai ra đòn, từ khoảng cách nào, theo hướng nào, chạm vào đâu, phản ứng ra sao, kết thúc ở tư thế nào.
Chạy sau module 49 khi playbook là G02 hoặc cảnh có va chạm thân thể. Luôn bật kèm 22 (trục, hướng), 48 (tay, nhóm người), 27 (state ledger).

## 52.1 Luật nền
- Pha hành động là chuỗi EXCHANGE, không phải danh sách tính từ. "Fast, epic combat" không định nghĩa được khoảng cách, hướng, camera hay kết quả → cấm.
- Mỗi exchange có đúng một INITIATOR và một RESPONDER. Đổi vai phải là một beat riêng (counter).
- Neo cố định trước, sự kiện sau: danh tính + trang phục + vị trí trên khung + địa điểm được viết trước mọi hành động.
- Mỗi segment kết thúc ở một tư thế ổn định kế thừa được (`Ends with:` có khoảng cách + vị trí trên khung + tư thế).

## 52.2 Đơn vị đòn (move unit)
`ANTICIPATION -> ACTION -> CONTACT -> REACTION -> RECOVERY`

| Trường | Bắt buộc ghi | Câu mẫu dạng tham số |
|---|---|---|
| start_distance | khoảng cách bằng mét hoặc "arm's length" | "four meters apart" |
| path | bộ phận ra đòn + hướng | "right jab toward the left shoulder" |
| defense | cách đỡ/né đọc được | "outside slip", "forearm block", "back step" |
| contact_point | vùng chạm hoặc bị đỡ | "blocked on the forearm" |
| reaction_evidence | bằng chứng lực quan sát được | "hood snaps back", "rear foot slides", "puddle splashes" |
| recovery | tư thế sau đòn | "both reset one step apart, guards up" |

Thiếu `contact_point` hoặc `reaction_evidence` → đòn "đánh vào không khí" (ACTION_NO_CONTACT).

## 52.3 Ngân sách exchange theo thời lượng
| Thời lượng clip | Số exchange tối đa | Cấu trúc |
|---|---|---|
| 4–6s | 1 | vào thế → 1 exchange → tư thế ổn định |
| 8–10s | 2 | establish 0–2s → exchange → counter → settle |
| 12–15s | 2 + resolution | 0–3 establish (danh tính, khoảng cách, lối thoát, hướng màn hình) / 3–7 exchange 1 / 7–11 counter đổi thế chủ động / 11–15 tách ra, camera dừng, giữ tư thế cuối |
| 20–30s | 2 cụm nối nhau | cụm 1 → reset beat (tách, thở, đổi vị trí) → cụm 2 → resolution |
| Đấu vũ khí dài (kiếm, gậy) | 3 exchange đo được / clip | cao–đỡ / thấp–lùi / khóa vũ khí |

Nhiều hơn ngân sách → tách clip (52.10), không nén thêm vào prompt.

## 52.4 Blocking, trục và hướng màn hình
- Khóa trục 180°: fighter A luôn một bên khung, fighter B bên kia; ghi vào orientation ledger (22) cho từng segment.
- Nếu hai người đổi bên (vòng qua nhau) → đó là một beat riêng có mốc giây; sau đó ghi lại bên mới và giữ nguyên đến hết clip ("preserve screen direction after any crossing").
- Nhận dạng bằng trang phục tương phản màu (một ấm, một lạnh) và nhắc lại anchor trang phục ở segment có tiếp xúc gần.
- Một đấu nhiều: serialize — chỉ một đối thủ ở làn trung tâm tại một thời điểm; đối thủ thứ hai chỉ tiến vào sau khi người thứ nhất rời làn. Người còn lại đứng xa, không có hành động riêng.
- Tiếp xúc đồng thời nhiều điểm (vật lộn, ôm khóa) → giữ shot rộng, ngắn, tăng khoảng tách trước và sau.

## 52.5 Hai trường phái quay
| Trường phái | Đặc điểm | Ống kính | Dùng khi |
|---|---|---|---|
| WIDE_LONG_TAKE | toàn thân, thấy chân và khoảng cách, ít cắt, đòn đọc rõ | 24–35mm | mặc định cho model video: dễ đọc, ít lỗi nhân vật nhập nhau |
| TIGHT_CUT | cận tay/mặt, cắt ngay lúc chạm, năng lượng từ dựng | 35–50mm + insert | chỉ khi chia thành nhiều clip ngắn nối nhau; không nhồi nhiều cut vào một clip |

Mặc định cho Seedance: mở wide để lập khoảng cách/chân/chướng ngại → một close-up cho một đòn hoặc một phản ứng quan trọng → trở lại khung đọc được.

## 52.6 Camera
- Một đường camera chủ đạo mỗi clip. Cấm chồng zoom + whip pan + orbit + drone dive + shake.
- Chọn theo hướng hành động: lateral track (di chuyển ngang), orbit chậm và giới hạn (đấu tay đôi tại chỗ), backward track (một bên tiến công liên tục).
- Camera ở cùng một phía trục trong suốt clip.
- Rung máy chỉ là phản ứng một nhịp tại một cú chạm, không kéo dài.
- Khi thử lần đầu: dựng choreography trên static wide; chỉ thêm tracking chậm khi đòn đã đọc được.

## 52.7 Trọng lượng, vật lý, slow motion
- Mỗi đòn có trọng lượng: chuyển trọng tâm trước khi ra đòn, giật lùi khi trúng, mất thăng bằng rồi lấy lại. Cấm nhảy lơ lửng kiểu dây treo trừ khi thể loại là fantasy/wuxia và đã khai báo.
- Bằng chứng lực đến từ môi trường và trang phục: vải giật, chân trượt, nước bắn, bụi bay, vật rung.
- Slow motion: tối đa một đoạn mỗi clip, ghi khoảng giây rõ ("8.5–9.5s only: half-speed"). Phần còn lại ghi "real-time speed".
- Âm thanh khớp từng hành động: giày, vải, hơi thở, một tiếng va chạm chính; một khoảng lặng ngắn trước đòn quyết định.

## 52.8 Stakes, môi trường, trạng thái
- Stakes tăng qua từng exchange: khoảng cách hẹp dần, không gian bị dồn, đòn nặng dần.
- Tối đa một vật trong bối cảnh được dùng mỗi clip (cửa, ghế, lan can, xe), ghi rõ trạng thái trước/sau (15).
- State ledger (27): mệt, bẩn, rách, ướt tích lũy qua clip và mang sang clip sau; không reset.

## 52.9 Rượt đuổi, xe, stunt
- Rượt đuổi: khóa hướng di chuyển trên màn hình cho cả hai bên (cùng hướng), khoảng cách giữa người đuổi và người chạy thay đổi quan sát được ở mỗi segment, tối đa một chướng ngại mỗi segment.
- Xe: một chiếc chính trong khung; tốc độ thể hiện bằng motion blur nền, bụi, tiếng động cơ; va chạm lớn → anticipation + aftermath thay vì khoảnh khắc va (13).
- Stunt nhảy/rơi: ghi điểm cất, quỹ đạo, điểm tiếp đất, tư thế sau tiếp đất.

## 52.10 Chia pha hành động thành nhiều clip
- Pha dài hơn ngân sách 52.3 → chia clip theo exchange; mỗi clip kết thúc ở trạng thái kế thừa được, clip sau mở bằng last frame clip trước (28).
- Cắt giữa chuyển động khi nối để giấu điểm nối; ghi hướng mỗi động tác ở cả hai phía điểm nối.
- Exchange quyết định (hero) là clip riêng có ngân sách thử 3–5 lần (51).
- Khi một clip hỏng: viết lại transition hỏng, không viết lại cả prompt.
- Đòn có chưởng / năng lượng / phép: điền Effect Contract (54.2); trong khoảng hiệu ứng active camera theo 54.6, `Ends with:` ghi đủ ba lớp neo (54.4).

## 52.11 Compliance
- Dùng ngôn ngữ dàn dựng không bạo lực đồ họa: "non-graphic staged choreography", "no blood, no injury, no gore".
- Vũ khí: "keep both blades rigid and unchanged", tia lửa chỉ ở điểm chạm cuối.
- Không dùng tên nhân vật/thương hiệu có bản quyền; mô tả trang phục bằng đặc điểm.
- Brief có bạo lực thực tế nặng → đưa về dàn dựng thể thao/võ thuật hoặc cắt sang hậu quả (30).

## 52.12 Khối prompt hành động
```text
[FORMAT — ratio, duration, resolution, speed rule]
[FIGHTER ANCHORS — identity, wardrobe color, frame side for each]
[LOCATION + START DISTANCE — surfaces and obstacles that affect movement]
[TIMED EXCHANGES — per segment: initiator, path, defense, contact, reaction, Ends with]
[ONE CAMERA PATH — lens + move, same side of the axis]
[LIGHTING]
[SOUND — synced to each action, one main impact]
[CONSTRAINTS — staged non-graphic, headcount, frame sides, wardrobe, hands, no extra cuts]
```

## 52.13 Mã lỗi hành động
| Mã | Dấu hiệu | Sửa |
|---|---|---|
| `ACTION_NO_CONTACT` | đòn không có điểm chạm/phản ứng | thêm start distance, path, contact point, reaction evidence |
| `FIGHTER_MERGE` | hai người nhập nhau, đổi mặt/trang phục | tăng khoảng tách, nhắc lại anchor trang phục, giảm tiếp xúc đồng thời, một reference mỗi danh tính |
| `EXCHANGE_OVERLOAD` | vượt ngân sách 52.3 | tách clip theo exchange |
| `CAMERA_STACK` | nhiều hơn một đường camera chủ đạo | giữ một đường, bỏ phần còn lại |
| `AXIS_BREAK` | fighter đổi bên không có beat vượt trục | khóa frame side, thêm beat crossing có mốc giây |
| `WEIGHTLESS_MOTION` | đòn lơ lửng, không trọng lượng | thêm chuyển trọng tâm, giật lùi, bằng chứng môi trường |
| `NO_RECOVERY_STATE` | segment kết thúc giữa đòn, clip sau reset | thêm tư thế ổn định + khoảng cách ở `Ends with:` |
| `CROWD_SIMULTANEOUS` | nhiều đối thủ tấn công cùng lúc | serialize theo làn |
| `SLOWMO_OVERUSE` | slow motion nhiều đoạn hoặc không ghi giây | một đoạn, ghi khoảng giây |
| `GRAPHIC_RISK` | máu, thương tích, từ ngữ bạo lực thực | ngôn ngữ dàn dựng, cắt sang hậu quả |
| `EFFECT_PERSISTENCE_LOSS` | chưởng/năng lượng bám người mất sau camera move | module 54: effect ledger + camera lock + restate |
