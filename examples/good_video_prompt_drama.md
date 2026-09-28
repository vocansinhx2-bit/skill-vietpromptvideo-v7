# GOOD — VIDEO PROMPT (DRAMA, 10s, text-to-video) — EVIDENCE_ONLY
> Tầng Design. Dùng để hiểu cơ chế, không copy chủ thể/bối cảnh/motif sang prompt khác (Example Quarantine Law).

## Craft Plan (tóm tắt)
| Trường | Giá trị |
|---|---|
| controlling_emotion | nỗi buồn kìm nén → chấp nhận |
| hook_type | Curiosity (vật lạ trong tay ở frame đầu) |
| curve | Fall–rise, đỉnh ở giây 7 |
| plant → payoff | lá thư chưa mở (0s) → mở ra, cười nhẹ (7s) |
| signature_moment | ngón tay dừng trên mép phong bì trước khi xé |
| lens | 35mm → 85mm → 50mm |
| sound | tiếng mưa trên kính, im lặng 0.5s trước khi xé, không nhạc |

## Prompt (runtime, English)
```text
A woman in her 60s sits alone at a kitchen table in a small Ohio farmhouse on a rainy afternoon, holding an unopened envelope in both hands.

Starting state: she faces camera-left toward the window, envelope resting on the table edge, a cold cup of coffee beside her right hand.

0–3s: Medium shot, 35mm, static camera. She turns the envelope over once with both thumbs and stops. Ends with: her eyes fixed on the handwriting.
3–7s: Slow push-in to a close-up, 85mm. Her right index finger rests on the flap edge for a moment, then tears it open in one steady pull. Ends with: the folded letter half out of the envelope.
7–10s: Static close-up, 50mm. She unfolds the letter, reads, and the corners of her mouth lift slightly while her eyes stay wet. Ends with: she lowers the letter to her lap and looks out the window.

Lighting: soft gray window light from camera-left, low contrast, warm tungsten fill from a lamp behind her, fine film grain, gentle halation on the window.
Audio: steady rain on glass, faint refrigerator hum, paper tearing <sfx>. One half-second of near silence right before the tear. No background music. No dialogue.
Constraints: one woman only, same face and gray cardigan throughout, she stays seated facing camera-left, real-time speed, no slow motion, no text on screen.
```

## Vì sao đạt (Design)
- Frame đầu một mình đã kể được tình huống (người + phong bì chưa mở).
- Mỗi segment một hành động quan sát được, có `Ends with:`.
- Cảm xúc chuyển thành ống kính/ánh sáng/âm, không viết "sad", "emotional", "cinematic masterpiece".
- Khóa hướng thân (camera-left), số người, trang phục, tốc độ.
