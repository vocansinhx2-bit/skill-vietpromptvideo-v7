# 47 — IMAGE SKILL BRIDGE (skilltaoanh v5 → video prompt)

> Nhận đầu ra của skill ảnh `ai-video-reference-image-os` (Scene Setup Plan, shot list, asset dossier, keyframe) và chuyển thành input cho bộ não video (module 46). Không bắt buộc: skill video vẫn chạy độc lập khi không có đầu ra skill ảnh.

## 47.1 Mapping ID (giữ nguyên, không đổi tên)
| Skill ảnh | Skill video | Ghi chú |
|---|---|---|
| `SCxx_SHxx` | shot / clip ID | 1 shot ảnh = 1 clip hoặc 1 segment |
| `duration_s` | độ dài segment / clip | cộng dồn các shot cùng clip ≤ 30s (2.5) / ≤ 15s (2.0) |
| `keyframe_role` START | first frame | |
| `keyframe_role` END | last frame | chỉ khi mode FIRST+LAST |
| `keyframe_role` FIRST_LAST | first + last | |
| `keyframe_role` STANDALONE | first frame hoặc @Image1 | |
| Character Sheet (A-ID) | @Image vai "identity only" | 1 ảnh sạch / nhân vật |
| Location Bible | @Image vai "layout only" | |
| Prop Sheet | @Image vai "exact object design only" | |
| Style Bible | closing constraints (ánh sáng/màu) | không gửi làm reference style nếu đã có first frame |
| `motion_owner` | camera hoặc subject của segment | |
| `video_mode` (module 38 ảnh) | input mode (46.6) | kiểm lại theo profile Seedance |
| continuity ledger (trục, screen direction, ánh sáng) | invariants + screen geography | |

## 47.2 Luật chuyển
1. Không mô tả lại nội dung tĩnh đã có trong keyframe; prompt video mô tả chuyển động, trình tự, âm thanh và end state.
2. Aspect lấy từ keyframe. First/last Seedance 2.5 tự adaptive theo first frame.
3. Keyframe là sheet storyboard (nhiều panel) → không dùng trực tiếp làm first frame; dùng frame đã rebuild full-res. Nếu cố ý dùng grid storyboard của Seedance 2.5, khai báo rõ: grid chỉ là tham chiếu trình tự, không phải khung hình đầu.
4. Asset > 8 subject trong 1 clip → tách clip (độ ổn định giảm khi quá nhiều asset).
5. Chain clip: last frame clip N (lấy qua `return_last_frame`) = first frame clip N+1; prompt clip N+1 "continue forward from that moment, do not replay [hành động trước]".
6. Mã lỗi ảnh vẫn giữ nguyên tên khi báo cáo chéo (ví dụ `CHAIN_IDENTITY_BREAK`, `PEAK_ACTION_FREEZE_RISK`).

## 47.3 Đầu vào tối thiểu khi có skill ảnh
`shot_id, duration_s, keyframe files + role, asset list + vai, motion_owner, continuity ledger, delivery aspect`.
Thiếu trường nào → module 46 tự điền và ghi giả định.
