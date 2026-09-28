# GOOD — VIDEO PROMPT (2D CEL ANIME ACTION, 10s, text-to-video) — EVIDENCE_ONLY
> Tầng Design. Dùng để hiểu cơ chế, không copy chủ thể/bối cảnh/motif sang prompt khác (Example Quarantine Law).

## Craft + Style Plan (tóm tắt)
| Trường | Giá trị |
|---|---|
| playbook | G13, họ `2D_CEL_ANIME` |
| medium line | câu đầu prompt, lặp nguyên văn nếu nối clip |
| hook_type | Curiosity: held frame đôi mắt nheo lại dưới vành mũ |
| principles | anticipation (vặn người), smear (cú vung), impact frame, follow-through (tóc, áo) |
| timing | on twos, bùng on ones cho cú đánh, held frame sau va chạm |
| camera | rostrum: push-in trên held face, parallax nền khi bóng bay |
| exclusions | không lens/bokeh/depth of field; không mặt 3D CG, không bán ảnh thật |

## Prompt (runtime, English)
```text
Hand-drawn 2D cel animation, crisp cel-shaded characters over a painted watercolor background, thin colored contour lines, two-step cel shadow, limited warm palette, animated on twos.

A 12-year-old girl in an oversized red baseball cap and blue jersey stands at home plate on a dusty small-town sandlot at sunset, bat raised, facing frame-right toward the pitcher.

0–2s: Held frame, slow push-in on her eyes narrowing under the cap brim. Ends with: her grip tightening on the bat.
2–4s: She twists her hips back and lifts her front foot, pure anticipation, the bat drawn behind her shoulder. Ends with: her body coiled.
4–5s: Animated on ones. She swings; the bat smears into a curved arc. A single high-contrast black-and-white impact frame on contact.
5–8s: Back on twos. The ball streaks away with speed lines while the painted sky and the foreground fence slide past in parallax. Her cap flies off and her hair and jersey keep settling after she stops.
8–10s: Held frame on her grin, rim light drawn as a clean orange shape along her cheek. Ends with: she drops the bat and starts to run toward first base, exiting frame-right.

Light: drawn sunset light, hard two-tone cel shadow, pink-orange sky, background one step darker than the character.
Audio: crickets and distant wind, <whoosh on the smear>, <sharp crack on the impact frame>, room tone drops out on the final held frame, then (a short brass sting).
Constraints: one character only, same face, cap and jersey colors throughout. No lens blur, no bokeh, no depth of field, no handheld shake, no 3D CG face, no semi-photoreal rendering, no text or logos.
```

## Vì sao đạt (Design)
- Medium line đứng đầu, nên model không trượt về ảnh thật.
- Tốc độ đưa vào smear, speed lines, nền cuộn thay vì camera xoay, nên mặt không bị chảy.
- Có đủ anticipation → action → impact frame → follow-through → held frame.
- Dùng từ vựng rostrum, không có ống kính; có danh sách loại trừ; không ghi tên studio.
