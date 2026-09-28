# 28 — TRANSITION & ONE-TAKE PLANNER
Choose cut, hidden cut, continuous move or one-take based on feasibility, not prestige.
One-take is a constraint with spatial and action costs; do not force it when cuts improve reliability.

## 28.1 Chọn kiểu chuyển
| Kiểu | Dùng khi | Rủi ro |
|---|---|---|
| Hard cut | Đổi địa điểm, đổi thời gian, thoại shot/reverse | Lệch identity nếu thiếu reference |
| Match cut | Hình dạng/hành động nối hai cảnh | Chỉ đổi một biến giữa hai shot |
| Hidden cut (che khuất) | One-take giả qua cột, cửa, người đi ngang | Nhân đôi chủ thể hai bên vật che |
| Continuous move | Theo chủ thể qua không gian | Trôi hình học, bịa phòng mới |
| Chain clip | Vượt giới hạn độ dài một clip | Lệch màu/aspect giữa clip |

## 28.2 Che khuất
Ghi thời gian bị che và cái phải giữ khi xuất hiện lại: both the woman and the suitcase are fully hidden for just under two seconds; the same woman emerges on the opposite side with the same face, hair and coat. Không để chủ thể xuất hiện hai bên vật che cùng lúc.

## 28.3 Nối clip (extend / chain)
- Lấy frame cuối của clip trước làm first frame của clip sau (hoặc bật `return_last_frame`).
- Prompt: `Use @Image1 as the exact first frame and continue forward from that moment.`
- Cấm lặp lại hành động đã xảy ra trước frame đó.
- Giữ cùng model, aspect, style và ánh sáng suốt chuỗi.
