# 42 — RUNTIME FAILURE ROUTER
Classify before editing: INPUT_TEXT_RISK, INPUT_ASSET_RISK, OUTPUT_RISK, EXAMPLE_ANCHORING, CREATOR_LEAKAGE, IDENTITY_DRIFT, REFERENCE_LEAKAGE, STATE_RESET, SPATIAL_FLIP, CAMERA_FAILURE, MOTION_FAILURE, SPEAKER_SWAP, LIPSYNC_FAILURE, AUDIO_FAILURE, COMPLEXITY_OVERLOAD, MODEL_CAPABILITY_LIMIT.
Repair order: source/evidence -> design/IR -> reference/state/shot -> runtime compile -> wording.

## 42.1 Quy trình chẩn đoán
1. Xem video từng frame ở đoạn lỗi. Ghi timestamp bắt đầu lỗi.
2. Xác định lỗi xảy ra toàn clip hay cục bộ (1–3s). Lỗi cục bộ → ưu tiên edit vùng/đoạn hoặc cắt bỏ, không tạo lại cả clip.
3. Tra bảng 42.2 → lấy mã lỗi + nguyên nhân gốc.
4. Sửa theo thứ tự repair order. Chỉ đổi MỘT biến mỗi lần tạo lại; giữ seed nếu provider hỗ trợ.
5. Lỗi lặp 2 lần sau khi sửa câu chữ → không sửa câu chữ nữa; chuyển sang đổi reference, chia shot hoặc giảm độ phức tạp (luật NO PROMPT-FIX TRAP).
6. Lỗi lọt qua lần tạo trước không chứng minh prompt sai; tạo lại 1 lần với cùng prompt + seed khác trước khi sửa, nếu chi phí cho phép.

## 42.2 Bảng lỗi Seedance — triệu chứng → nguyên nhân → sửa
| # | Mã | Triệu chứng | Nguyên nhân gốc | Sửa (theo thứ tự) |
|---|---|---|---|---|
| 1 | SPATIAL_FLIP | Nhân vật đổi bên trái/phải sau cut hoặc giữa clip | Không khóa screen position; câu tả tư thế trung tính để model tự diễn giải | Khóa ở mọi beat: "[A] stays frame-left facing right" (module 22); thêm "No mirrored framing" |
| 2 | FACING_ERROR | Nhân vật quay lưng/nhìn sai hướng, đi lùi | Không ghi hướng thân + hướng mặt; ảnh reference có tư thế khác | Ghi body facing + head facing + eyeline từng segment (22.2); đổi first frame đúng hướng |
| 3 | MIRROR_FLIP | Tay thuận, nốt ruồi, phụ kiện, vạch ngôi tóc đổi bên | Framing đối xứng mơ hồ; ảnh reference đã bị lật | Ghi rõ bên của đặc điểm bất đối xứng: "scar on her left cheek, left-handed"; kiểm tra ảnh reference chưa lật (22.5) |
| 4 | UNMOTIVATED_TURN | Nhân vật tự xoay người không lý do | Hướng không khóa; timeline thưa → model tự thêm chuyển động | Viết xoay người thành hành động riêng có trigger; nếu không xoay: "keeps facing [X] throughout" |
| 5 | IDENTITY_DRIFT | Mặt/tuổi/tỷ lệ đổi dần, nhất là ở close-up | Reference mâu thuẫn góc/ánh sáng; thiếu ảnh mặt trung tính; extend nhiều lần | Bộ reference đồng nhất (module 19); lặp character lock nguyên văn; reset bằng reference sạch sau 2–3 lần extend |
| 6 | IDENTITY_BLEND | Hai nhân vật trộn mặt thành một | Dùng ảnh chụp chung; mô tả hai người quá giống | Mỗi nhân vật 1 ảnh riêng; làm khác biệt rõ trang phục/tóc; tên vai cố định |
| 7 | WARDROBE_DRIFT | Quần áo đổi sau cut, phụ kiện biến mất | Mô tả trang phục mơ hồ; phụ kiện nhỏ không được khóa | Ghi trang phục cụ thể (màu + chất + chi tiết); "keeps the [accessory] throughout"; ảnh close-up phụ kiện |
| 8 | REFERENCE_LEAKAGE | Model copy phông nền/ánh sáng/quần áo từ ảnh nhân vật | Reference không giới hạn thẩm quyền | Câu phủ định: "Do not copy the background, lighting or outfit from @ImageN" (module 18) |
| 9 | DUPLICATE_SUBJECT | Nhân vật/vật bị nhân đôi giữa clip | Mô tả cùng chủ thể 2 lần bằng cụm khác nhau; nhiều reference cùng entity không gán vai | Một handle duy nhất cho mỗi entity; "Only one [X] exists in the scene"; ghi headcount (module 48) |
| 10 | EXTRA_LIMB | Tay thứ 3, tay không chủ trong cảnh đông người | Model tính lại quyền sở hữu tay mỗi cut | "There are only two hands in frame, both belonging to [A]"; giới hạn hành động tay ≤2 nhân vật/shot (module 48) |
| 11 | PROP_TELEPORT | Đạo cụ đổi tay, đổi vị trí, tự xuất hiện | Không có possession ledger; đạo cụ không có điểm vào | Ghi ai cầm, tay nào, ở đâu mỗi segment (module 27); vật mới phải có điểm vào khung hình |
| 12 | LINKED_OBJECT_DRIFT | Vật bên cạnh chuyển động theo vật chính | Model hiểu các vật gần nhau là dính liền | "The [B] stays in place throughout; only the [A] moves" |
| 13 | MIMED_ACTION | Tay làm động tác nhưng vật không đổi (xé, rót, bấm) | Chỉ có động từ, thiếu cơ chế | Chuỗi 5 phần: cấu trúc ban đầu → điểm tựa → hướng lực → phản hồi vật liệu → trạng thái cuối (module 15) |
| 14 | TRUNCATED_ACTION | Hết clip khi hành động chưa xong | Thời gian dồn vào giai đoạn tiếp cận | Ghi trạng thái hoàn thành + giữ 0.3–0.5s: "the lid seats flush and stays there"; giảm hành động trước đó |
| 15 | ACTION_REVERSAL | Hành động xong sớm rồi tua ngược; camera trượt về | Timeline thừa thời gian, model lấp bằng đảo ngược | Nối 2–3 hành động cùng chiều cho đủ thời lượng; ghi điểm dừng camera; chuyến đi-về → tách 2 shot |
| 16 | SEGMENT_INVENTION | Model tự thêm người/vật/sự kiện không yêu cầu | Segment quá thưa | Mỗi segment có hành động + end state; thêm micro-action (module 24); rút ngắn duration |
| 17 | STATE_RESET | Vật đã vỡ/ướt/mở lại lành/khô/đóng | End state không được truyền sang beat sau | Beat sau mở đầu bằng trạng thái đã đổi: "the same cup, now cracked" (module 27) |
| 18 | OCCLUSION_SWAP | Người/vật đi sau vật che rồi ra khác đi | Không khai báo bất biến khi che khuất | Ghi thời gian bị che + "reappears unchanged: same [lock]" (module 15, 21) |
| 19 | WALK_GLITCH | Trượt chân, cùng chân 2 lần, lướt, đi xuyên vật | Chuyển động chu kỳ khó; không ghi vật lý bước | "heel lands first, strict left-right alternation, one foot always on the ground"; ghi đường đi quanh vật cản |
| 20 | SPEAKER_SWAP | Người không nói lại mấp máy môi | Không ghi trạng thái miệng người nghe | "Only [A] speaks; [B] lips at rest, jaw closed, eyes on [A]" (module 25) |
| 21 | FILLER_BABBLE | Thoại ngắn bị kèm âm lầm bầm hoặc lặp lại | Khoảng thời gian dài hơn câu thoại | Câu 5–8s khớp độ dài segment; lấp khoảng trống bằng SFX/hành động; "says the line once and nothing else" |
| 22 | LIPSYNC_FAILURE | Môi lệch tiếng | Nhiều người nói/1 shot; góc nghiêng; camera động | MCU chính diện, camera khóa, 1 người/1 câu/1 shot; số viết thành chữ (module 25) |
| 23 | AUDIO_FAILURE | Nhạc đè thoại, SFX sai thời điểm, tiếng lạ | Không phân kênh; không có nguyên nhân hình ảnh | Dấu ngoặc Music ( ) / SFX < > / Dialogue { }; mỗi SFX gắn một sự kiện nhìn thấy (module 26) |
| 24 | CAMERA_OVERLOAD | Hình rung, khó đọc, camera bay lung tung | Chồng nhiều chuyển động cùng lúc | Một chuyển động chính/shot; tuần tự: "rises 0–3s, holds, then pushes in 4–8s" (module 23) |
| 25 | AXIS_BREAK | Cut qua trục làm đảo hướng | Góc máy shot sau đặt ngược phía | Khai báo phía camera bằng mốc thế giới; shot trung gian nếu cần vượt trục |
| 26 | SPACE_GEOMETRY | Cửa/hành lang sai hướng, xuyên đồ đạc | Không có spatial layout | Khối layout: vị trí camera, hướng nhìn, vật giữa camera và nhân vật, đường đi (module 22) |
| 27 | CLIP_REPLAY | Clip nối lặp lại đoạn cũ | Prompt extend tả lại hành động đã xảy ra | "Use @Image1 as the exact first frame and continue forward. Do not replay…" (module 28) |
| 28 | CHOPPY_CHAIN | Chuỗi clip giật, reset tư thế/nhịp | Mỗi clip tự đoán lại tư thế | Nối frame cuối → frame đầu, cắt giữa chuyển động; ghi hướng mỗi động tác; cấm slow motion nếu không muốn |
| 29 | STYLE_DRIFT | Ảnh thật dần thành hoạt hình/đổi màu | Style mơ hồ; reference khác style | Một câu style cố định lặp nguyên văn; reference cùng style; khóa palette 3 lớp (module 29) |
| 30 | LIGHT_JUMP | Hướng sáng/nhiệt màu nhảy giữa shot | Không có đoạn ánh sáng riêng | Đoạn ánh sáng cố định: nguồn + hướng + chất + nhiệt màu, lặp mỗi shot |
| 31 | FRAME_STUTTER | Hình giật, frame lặp, fps thực thấp | Hành động dày trong clip dài | Giảm mật độ hành động; ghi "real-time speed, smooth continuous motion"; cắt bỏ đoạn lỗi ở hậu kỳ |
| 32 | TEXT_GARBLE | Chữ/logo trên vật bị méo | Model yếu render chữ chuyển động | Tránh chữ trong khung; chữ quan trọng → chèn hậu kỳ; nếu cần, chữ ngắn, to, đứng yên |
| 33 | INPUT_REJECTED | Lỗi tham số / bị kiểm duyệt | Sai ratio (edit/extend cần adaptive), file vượt giới hạn, từ nhạy cảm | Kiểm tra profile model; đổi từ nhạy cảm sang trung tính (module 30); không gửi lại y nguyên |
| 34 | ACTION_NO_CONTACT | Đòn đánh xuyên người hoặc trượt không khí, không ai phản ứng | Không có khoảng cách, đường đi, điểm chạm | Ghi start distance + path + contact point + reaction evidence cho từng đòn (module 52.2) |
| 35 | FIGHTER_MERGE | Hai người đánh nhau nhập làm một, đổi mặt/áo | Tiếp xúc đồng thời quá lâu, anchor trang phục yếu | Tăng khoảng tách, nhắc lại màu áo + frame side, một reference mỗi danh tính, beat đó rộng và ngắn hơn |
| 36 | EXCHANGE_OVERLOAD | Pha đánh rối, động tác mất, tư thế reset | Số exchange vượt ngân sách thời lượng | Cắt theo ngân sách 52.3, tách clip theo exchange, nối bằng last frame |
| 37 | PHOTOREAL_DRIFT | Clip hoạt hình dần thành bán ảnh thật / mặt 3D chung chung | Thiếu medium line, trộn từ vựng 2D/3D, lens grammar trong 2D | Medium line ở câu đầu, lặp thông số bóng trong segment nhanh, thêm danh sách loại trừ (module 53.4) |
| 38 | BOILING_LINES | Viền nhấp nháy, mặt biến dạng trong hoạt hình | Hành động + camera quá dày | Một hành động chính + một chuyển động phụ + camera đơn giản; tốc độ đưa vào speed lines / nền cuộn |
| 39 | EFFECT_PERSISTENCE_LOSS | Chưởng/lửa/điện đang bám nhân vật biến mất sau khi camera quay đi rồi quay lại, sau cut hoặc bị che | Hiệu ứng viết như sự kiện, không có thời lượng; camera rời vùng chạm khi hiệu ứng active; không nhắc lại trạng thái | Effect Contract + effect ledger + ba lớp neo (hiệu ứng, ánh sáng, residue) + camera lock trong SUSTAIN + cut kèm restate (module 54.4–54.6) |
| 40 | EFFECT_DETACHED | Hiệu ứng trôi khỏi nguồn hoặc nhảy sang nhân vật khác | Nguồn không neo vào bộ phận cơ thể cụ thể | Ghi source + attachment trái/phải, "stays attached to", "never jumps to another character" (54.2, 54.7) |
| 41 | EFFECT_STATIC_OVERLAY | Glow đứng yên như dán lên hình, không hắt sáng | Thiếu motion behavior và light spill; thêm hiệu ứng lớn bằng edit/V2V | "changes shape every frame", light spill lên mặt/áo; tạo lại từ đầu thay vì edit (54.7, 54.9) |
| 42 | EFFECT_NO_ENDPOINT | Hiệu ứng lơ lửng mãi hoặc tắt đột ngột | Không có lifecycle và endpoint | Lifecycle FORM→DISSIPATE có mốc giây + endpoint + residue (54.2) |
| 43 | EFFECT_BODY_CORRUPTION | Tay/mặt méo, chi nhân đôi nơi năng lượng chạm | Hiệu ứng xuyên qua cơ thể, vùng chạm quá lớn | "around, not through", thu nhỏ vùng chạm, neo tay theo module 48; tách hiệu ứng phụ (54.3) |

## 42.3 Cách sửa cục bộ (Seedance 2.5)
- Lỗi trong 1 đoạn ngắn → edit mode: "Edit [t1]–[t2] seconds only. Preserve motion, background, camera, lighting and audio." Chỉ dùng add/remove/replace.
- Lỗi chi tiết nhỏ (khuyên tai, vết bẩn) → edit vùng hoặc sửa hậu kỳ.
- Đoạn còn dùng được trong clip hỏng → cắt giữ làm insert/cutaway.
- Lỗi hệ thống (toàn clip) → sửa thiết kế rồi tạo lại.

## 42.4 Output chẩn đoán
```
FAILURE: <mã>  at <t1–t2>s  scope: LOCAL | CLIP | SERIES
ROOT CAUSE: <1 câu>
FIX LEVEL: DESIGN | REFERENCE | SHOT | COMPILE | WORDING | POST
CHANGE ONE VARIABLE: <biến đổi duy nhất>
PATCHED PROMPT LINES: <chỉ các dòng đổi>
```
