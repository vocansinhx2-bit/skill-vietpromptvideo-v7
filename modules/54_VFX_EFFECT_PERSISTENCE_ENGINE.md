# 54 — VFX & EFFECT PERSISTENCE ENGINE
Giữ hiệu ứng (chưởng, năng lượng, lửa, điện, phép, khói, băng, hào quang, khiên) gắn đúng vào nhân vật hoặc vật, và còn tồn tại qua camera move, cắt cảnh, che khuất và nối clip.
Chạy ở bước A3 khi cảnh có hiệu ứng tương tác với nhân vật hoặc vật. Bật kèm 15 (lifecycle), 27 (state ledger), 23 (camera), 48 (vùng tiếp xúc cơ thể); thêm 52 khi có đánh nhau, 53 khi là hoạt hình.

## 54.1 Vì sao hiệu ứng biến mất
- Model không có bộ nhớ cho vùng đã rời khung: vùng đó khi quay lại được vẽ lại từ prompt và frame hiện tại.
- Hiệu ứng là ánh sáng, hạt, khói, không có khối rắn → bị xếp là chi tiết phụ và mất trước đạo cụ.
- Prompt viết hiệu ứng như sự kiện ("fires a blast that hits her") thay vì trạng thái có thời lượng.
- Camera rời vùng chạm đúng lúc hiệu ứng đang hoạt động (orbit, whip pan, quay qua lại).
- Không có endpoint → model tự quyết định hiệu ứng tan lúc nào.
- Segment nhanh không nhắc lại thông số hiệu ứng → hiệu ứng mờ dần hoặc đổi dạng.

## 54.2 Effect Contract (bắt buộc cho mỗi hiệu ứng chính)
| Trường | Nội dung |
|---|---|
| effect_id | FX1, FX2 |
| type | energy blast / aura / fire / electric arc / smoke / water / ice / particles / portal / shield |
| source | bộ phận cơ thể hoặc vật phát ra, ghi trái/phải (right palm, sword edge) |
| attachment | nơi chạm và cách bám (hits left shoulder → wraps upper left arm) |
| look | màu lõi + màu viền + hình dạng + độ dày + độ sáng |
| motion_behavior | đổi hình mỗi frame, nhịp đập, xoắn, chảy theo trọng lực/gió |
| light_interaction | màu hắt lên mặt, áo, nền; hướng hắt |
| body_object_interaction | đẩy lùi, áo bay, cháy xém, đóng băng, ướt, nứt sàn |
| lifecycle | FORM → TRAVEL → CONTACT → SUSTAIN → DISSIPATE, mỗi pha có mốc giây |
| residue | dấu vết sau khi tan: vết cháy, khói mảnh, tia lửa lẻ, sương băng, ánh sáng mờ dần |
| endpoint | settle / fade / evaporate / freeze / collapse / glow out / leave residue |
| camera_rule | camera được làm gì khi hiệu ứng active (54.6) |

## 54.3 Luật nền
- Một hiệu ứng chính mỗi clip; tối đa một hiệu ứng phụ nhỏ (bụi, tia lửa lẻ).
- Hiệu ứng luôn có nguồn neo vào một bộ phận cơ thể hoặc vật cụ thể.
- Hiệu ứng là trạng thái có thời lượng: ghi "persistent effect" và khoảng giây active.
- Mỗi hiệu ứng có endpoint; hiệu ứng vĩnh viễn không có hậu quả dễ biến thành lớp phủ nhiễu.
- Hiệu ứng bao quanh nhân vật, không xuyên qua mặt hoặc tay; danh tính giữ ổn định dưới hiệu ứng.
- Hiệu ứng tuân theo trọng lực, gió, va chạm, phản chiếu và che khuất.
- Viết hành vi của hạt, ánh sáng, khói, biến dạng; cấm nhãn rỗng "epic VFX", "magical effect", "cinematic effect".

## 54.4 Ba lớp neo
Hiệu ứng sống sót khi rời khung nhờ ba lớp, xếp từ yếu đến bền:
1. **Neo hiệu ứng**: bản thân hiệu ứng (coils, flames, aura).
2. **Neo ánh sáng**: màu hiệu ứng hắt lên da, áo, môi trường; còn thấy được khi hiệu ứng bị che một phần.
3. **Neo vật chất (residue)**: thay đổi trên nhân vật hoặc vật: tay áo cháy xém, tóc dựng, sương băng, vết nứt sàn. Đây là trạng thái vật thể (module 27) nên model giữ tốt nhất.

Mỗi segment sau CONTACT ghi đủ ba lớp trong `Ends with:`.

## 54.5 Effect ledger theo segment (mở rộng 27)
| Segment | FX | Pha | Bám ở | Look | Light spill | Residue | Trong khung? |
|---|---|---|---|---|---|---|---|

- Segment nào hiệu ứng còn active thì cột "Trong khung?" là `yes`, hoặc `occluded t1–t2 + reappears unchanged`.
- Hiệu ứng rời khung khi còn active mà không có lý do → `EFFECT_PERSISTENCE_LOSS` ở tầng thiết kế, sửa trước khi viết prompt.

## 54.6 Camera khi hiệu ứng active (mở rộng 23, 52)
- Trong khoảng CONTACT → SUSTAIN: camera locked, hoặc một chuyển động chậm giữ vùng chạm trong khung (slow push-in, slow lateral track cùng phía trục).
- Cấm orbit, whip pan, pan rời vùng chạm hoặc quay đi quay lại khi hiệu ứng active.
- Cần thấy phản ứng của người khác → dùng cut, không dùng pan. Shot sau mở bằng câu nhắc trạng thái: "The blue coils are still wrapped around her left arm."
- Quay lại vùng chạm → mở segment bằng full effect state (look + attachment + light + residue); không viết "back to her".
- Hiệu ứng cần tan khi camera rời → cho tan trong khung trước, hoặc để residue làm bằng chứng.

## 54.7 Câu prompt (English)
- "The [color] [effect] is a persistent effect, not a flash; it stays attached to [body part] from [t1]s to [t2]s."
- "The [effect] changes shape every frame, crackling and flickering, never a static glow or a painted-on overlay."
- "[Color] light from the [effect] spills onto her face and jacket."
- "The [effect] wraps around her arm, not through it; her hand and face stay unchanged."
- "Camera stays on the contact area while the effect is active."
- "After [t2]s the [effect] fades out, leaving [residue]."
- "Ends with: [effect] still on [body part], [residue], [light spill]."
- Constraints: "no static glow, no painted-on overlay, no floating or duplicated limbs where the energy touches the body; the effect never jumps to another character."

## 54.8 Hoạt hình và anime (mở rộng 53)
- Đưa hiệu ứng vào style lock: màu lõi/viền, "hand-drawn effects animation with hard graphic shapes", "animated on twos", impact frame ở CONTACT.
- 2D: hiệu ứng là mảng màu cứng có viền, không dùng glow photoreal. 3D stylized: glow + hạt mềm.
- Lặp thông số hiệu ứng trong segment nhanh giống như thông số bóng.
- Mỗi nhân vật một màu hiệu ứng riêng; cấm đổi màu hiệu ứng giữa các nhân vật.

## 54.9 Nối clip
- Frame cuối clip trước (làm @Image1 first frame) phải thấy rõ hiệu ứng hoặc residue; không chọn frame bị chớp trắng che hết.
- Prompt clip sau mở bằng effect handoff: "Continue from @Image1: the same blue coils still wrap her left arm, fading; her sleeve is scorched."
- Có ảnh hiệu ứng mẫu từ skill ảnh → @ImageN vai "effect appearance only"; không lấy nhân vật hay nền từ ảnh đó (18).
- Hiệu ứng phức tạp tạo từ đầu bằng prompt đủ Effect Contract; edit / video-to-video chỉ dùng để vá 1–3s, vì thêm hiệu ứng lớn bằng edit thường ra glow tĩnh dán lên.

## 54.10 Âm thanh
- Âm theo pha: <charge hum> ở FORM, <whoosh> ở TRAVEL, <impact> ở CONTACT, <steady crackle> suốt SUSTAIN, nhỏ dần ở DISSIPATE.
- Âm SUSTAIN liên tục và có mốc giây, không tắt trước khi hiệu ứng tan.

## 54.11 Ngân sách và sửa
- Shot hiệu ứng khó: dự trù khoảng 3 lần tạo cho một shot dùng được; giữ đoạn tốt nhất, ghép ở hậu kỳ.
- Mất hiệu ứng trong 1–3s → edit mode: "Edit [t1]–[t2] seconds only. Add back the blue coils wrapped around her left arm, matching the earlier look. Preserve motion, camera, lighting and audio."
- Mất cả đoạn sau camera move → sửa thiết kế, một biến mỗi lần: khóa camera, hoặc đổi pan thành cut + restate.
- Hiệu ứng quá tải → giảm diện tích/cường độ, để residue kể phần còn lại.

## 54.12 Khối prompt hiệu ứng
```text
[EFFECT LINE — type, source, color core/edge, persistent, active t1–t2]
[TIMELINE — FORM / TRAVEL / CONTACT / SUSTAIN / DISSIPATE, each "Ends with:" effect + light + residue]
[CAMERA — locked or one slow move on the contact area while active]
[LIGHT — effect light spill on subject and surroundings]
[AUDIO — sound per phase, continuous sustain sound]
[CONSTRAINTS — attached to source, never jumps, around not through, no static overlay, endpoint + residue]
```

## 54.13 Mã lỗi hiệu ứng
| Mã | Dấu hiệu | Sửa |
|---|---|---|
| `EFFECT_PERSISTENCE_LOSS` | hiệu ứng biến mất sau camera move, cut hoặc che khuất khi còn active | effect ledger + ba lớp neo + camera lock + restate sau cut |
| `EFFECT_DETACHED` | hiệu ứng trôi khỏi nguồn hoặc nhảy sang người khác | neo bộ phận cơ thể + "stays attached to" + "never jumps" |
| `EFFECT_STATIC_OVERLAY` | glow đứng yên như dán lên hình | "changes shape every frame" + light spill; tạo từ đầu thay vì edit |
| `EFFECT_NO_ENDPOINT` | hiệu ứng lơ lửng mãi hoặc tắt đột ngột | lifecycle có mốc giây + endpoint + residue |
| `EFFECT_STACK` | nhiều hiệu ứng chính chồng nhau | một hiệu ứng chính mỗi clip |
| `EFFECT_BODY_CORRUPTION` | tay/mặt méo, chi nhân đôi nơi năng lượng chạm | "around, not through", thu nhỏ vùng chạm, module 48 |
| `EFFECT_STYLE_DRIFT` | hiệu ứng anime thành glow thật hoặc ngược lại | đưa hiệu ứng vào style lock (53) |
| `EFFECT_CHAIN_BREAK` | mất hiệu ứng giữa hai clip nối | last frame có hiệu ứng/residue + effect handoff |
| `EFFECT_LABEL_ONLY` | chỉ ghi "epic VFX", "magic" | điền Effect Contract 54.2 |
