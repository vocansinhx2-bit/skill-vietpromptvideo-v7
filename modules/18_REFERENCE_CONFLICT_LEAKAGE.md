# 18 — REFERENCE CONFLICT & LEAKAGE
Check identity/style/geometry/state conflicts between references and prompt.
Separate spatial/previs authority from texture/style authority.
Prevent final-state references from leaking into early-state frames unless intended.

## 18.1 Kiểm tra xung đột
| Xung đột | Dấu hiệu | Xử lý |
|---|---|---|
| Reference ↔ reference | 2 ảnh cùng nhân vật khác góc/ánh sáng/tuổi | Giữ ảnh rõ nhất làm canonical; ảnh còn lại chỉ phụ trách góc/chi tiết |
| Reference ↔ prompt | prompt tả tóc đỏ, ảnh tóc đen | Sửa prompt theo ảnh, hoặc tuyên bố rõ thay đổi nào là có chủ đích |
| Style ↔ identity | ảnh style khác chất liệu với ảnh nhân vật | Style ref chỉ phụ trách màu/grain: "@ImageN sets color grade only" |
| Motion ↔ identity | diễn viên trong video chuyển động ghi đè nhân vật | "do not copy the actor, clothes or environment from @VideoN" |
| Final state ↔ early state | ảnh trạng thái cuối xuất hiện từ đầu | Chỉ dùng ảnh cuối làm LAST_FRAME; không đưa vào reference mode chung |
| First/last ↔ reference mode | trộn 2 chế độ | Chọn 1 chế độ (module 46.6) |

## 18.2 Rủi ro rò rỉ thường gặp
- Phông nền/ánh sáng trong ảnh nhân vật lan sang cảnh.
- Tư thế trong ảnh nhân vật bị giữ cứng, nhân vật không chuyển động.
- Hướng nhìn trong ảnh reference ghi đè hướng yêu cầu → khai báo hướng trong prompt (module 22).
- Ảnh bị lật gương → phụ kiện/tóc đổi bên.
- Nhãn chữ trên ảnh reference xuất hiện trong video → không gắn chữ lên ảnh.
- Hai nhân vật trong một ảnh → trộn mặt.

## 18.3 Hàng rào chặn
- Mỗi reference có danh sách NOT_AUTHORITATIVE_FOR ghi thành câu "Do not copy…".
- Trạng thái cần đổi so với ảnh → viết trong STARTING STATE: "Unlike @Image1, [A] now wears…".
- Hướng/tư thế khác ảnh → "[A] faces [direction], not the pose in @Image1."

## 18.4 Lỗi
REFERENCE_LEAKAGE, IDENTITY_BLEND, MIRROR_FLIP, REFERENCE_VS_LASTFRAME_CONFLICT → module 42.2.
