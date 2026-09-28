# 26 — AUDIO TRACK PLANNER
Treat ambience, Foley, dialogue/voice and music as separate tracks.
Resolve conflicts and priority.
Do not add music by default when user wants ASMR/environmental realism.

## 26.1 Bốn track
| Track | Nội dung | Ký hiệu Seedance 2.5 |
|---|---|---|
| Ambience | room tone, mưa, gió, phố | liệt kê trong `Audio:` |
| Foley / SFX | tiếng bước, chạm, vỡ | `< >` |
| Dialogue / VO | lời nói | `{ }` |
| Music | nhạc nền | `( )` |
| Subtitle | chữ trên màn hình | `【 】` |

## 26.2 Ưu tiên khi xung đột
Dialogue > SFX gắn với hành động nhìn thấy > ambience > music.
Có thoại: tắt hoặc hạ nhạc; ghi `No background music; keep only dialogue, ambience and action effects.`
Mặc định thêm `No subtitles.` trừ khi user cần chữ.

## 26.3 Đồng bộ âm thanh với hình
- SFX gắn đúng thời điểm tiếp xúc trong block.
- Nhạc cần khớp beat → dùng timestamp (Seedance 2.5) và đặt cắt/hành động ở mốc beat.
- Audio reference dùng cho nhịp, giọng, bài nhạc; ghi rõ nó điều khiển gì.

## 26.4 Nối clip
Clip nối tiếp giữ cùng ambience và xu hướng âm lượng. Độ lớn đoạn extend có thể lệch nhẹ so với nguồn; xử lý ở hậu kỳ.
