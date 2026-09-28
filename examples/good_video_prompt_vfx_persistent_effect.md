# GOOD — VIDEO PROMPT (LIVE-ACTION FANTASY, PERSISTENT EFFECT, 10s, text-to-video) — EVIDENCE_ONLY
> Tầng Design. Dùng để hiểu cơ chế, không copy chủ thể/bối cảnh/motif sang prompt khác (Example Quarantine Law).

## Effect Contract (tóm tắt)
| Trường | Giá trị |
|---|---|
| effect_id | FX1 |
| type | electric energy blast → coils |
| source | right palm của người tấn công |
| attachment | chạm vai trái → quấn cánh tay trái trên |
| look | lõi trắng xanh, viền cyan, sợi mảnh xoắn |
| lifecycle | FORM 0–2s, TRAVEL 2–3s, CONTACT 3–4s, SUSTAIN 4–8s, DISSIPATE 8–10s |
| residue | tay áo cháy xém, khói mảnh, tia lửa lẻ |
| endpoint | glow out + leave residue |
| camera_rule | locked wide đến 4s, slow push-in cùng phía trục 4–8s, không pan rời vùng chạm |

## Effect ledger
| Segment | Pha | Bám ở | Light spill | Residue | Trong khung? |
|---|---|---|---|---|---|
| 0–2s | FORM | right palm (A) | cyan trên mặt A | — | yes |
| 2–3s | TRAVEL | giữa hai người | cyan trên nền bê tông | — | yes |
| 3–4s | CONTACT | vai trái (B) | cyan trên mặt B | vết cháy vai | yes |
| 4–8s | SUSTAIN | cánh tay trái trên (B) | cyan trên mặt, áo B | tay áo xém, khói mảnh | yes |
| 8–10s | DISSIPATE | cánh tay trái (B), mờ dần | yếu dần | tay áo xém, tia lửa lẻ | yes |

## Prompt (runtime, English)
```text
Live-action fantasy, 16:9, 10s, real-time. An empty concrete parking garage in Chicago at night, cool sodium lights.

A man in a gray hoodie stands frame-left facing right. A woman in a black leather jacket stands frame-right facing left, 4 meters away.

The electric blast is a persistent effect, not a flash.
0–2s: Locked wide shot. White-blue sparks gather in his right palm. Ends with: a crackling ball in his right palm, cyan light on his face.
2–3s: He thrusts his palm forward; the blast travels straight across the gap. Ends with: the blast reaching her.
3–4s: The blast hits her left shoulder and wraps around her upper left arm as thin cyan coils. She staggers one step back. Ends with: cyan coils wrapped around her upper left arm, sleeve scorched at the shoulder.
4–8s: Slow push-in on her, staying on the same side. The cyan coils stay on her upper left arm the whole segment, changing shape every frame, crackling. Cyan light spills onto her face and jacket. She grips her left arm with her right hand. Ends with: coils still on her left arm, thin smoke from the sleeve.
8–10s: The coils flicker and glow out, leaving a scorched sleeve, thin smoke and a few stray sparks. Ends with: she lowers her right hand, breathing hard.

Audio: low charge hum, <whoosh> on travel, <sharp electric impact> at 3s, steady crackle from 4s to 8s fading out by 10s, garage echo.
Constraints: two people only, same faces and clothes throughout. The coils wrap around her arm, not through it; her hand and face stay unchanged. The effect never jumps to him. Camera never leaves the contact area while the effect is active. No static glow, no painted-on overlay, no duplicated limbs, no blood, no injury.
```

## Vì sao đạt (Design)
- Hiệu ứng được khai báo là trạng thái có khoảng giây, không phải sự kiện chớp nhoáng.
- Mỗi `Ends with:` sau CONTACT có đủ ba lớp neo: coils, ánh sáng cyan, residue.
- Camera chỉ push-in cùng phía trục, vùng chạm luôn trong khung khi hiệu ứng active.
- Có endpoint và residue nên model không tự tắt hiệu ứng giữa chừng.
