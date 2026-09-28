# 27 — STATE HANDSHAKE & CONTINUITY
Every important beat exports an END_STATE consumed by the next beat.
Track entity state, object state, possession, environment, damage/build progress and spatial location.
Reset only after explicit cut/time/location/state change.

## 27.1 Continuity ledger (mỗi segment một dòng)
| Trường | Nội dung |
|---|---|
| ENTITY_STATE | tư thế, vị trí (module 22), biểu cảm, trạng thái cơ thể (ướt, bẩn, thở dốc) |
| WARDROBE | trang phục + phụ kiện + trạng thái (xắn tay, cởi khuy, dính nước) |
| POSSESSION | ai cầm vật gì, tay nào, cầm thế nào |
| OBJECT_STATE | mở/đóng, đầy/vơi, lành/vỡ, bật/tắt, vị trí |
| ENVIRONMENT | thời tiết, ánh sáng, khói, nước đọng, cửa mở/đóng |
| PROGRESS | tiến độ việc đang làm (đã rót nửa ly, đã xây 3 tầng) |
| EFFECT_STATE | hiệu ứng đang active: pha, bám ở đâu, look, light spill, residue (module 54.5) |

## 27.2 Luật handshake
- END_STATE của segment N = STARTING STATE của segment N+1, viết lại bằng đúng từ ngữ, không đổi từ đồng nghĩa.
- Thay đổi trạng thái chỉ xảy ra khi có hành động nhìn thấy gây ra nó (module 15).
- Trạng thái đã đổi phải được nhắc lại bằng cụm "the same [X], now [state]" để model không tạo vật mới.
- Trạng thái không đổi nhưng dễ trôi (vật đã vỡ, áo đã ướt) → nhắc lại trong CONTINUITY mỗi segment.

## 27.3 Possession ledger
- Vật đổi tay phải có hành động trao: ai đưa, tay nào nhận, ở đâu trong khung.
- Mỗi tay tối đa 1 vật chính; vật thứ hai → đặt xuống trước (ghi rõ đặt ở đâu).
- Vật được đặt xuống giữ nguyên vị trí cho đến khi có người chạm lại.
- Vật rời khung hình rồi quay lại → giữ nguyên hình dạng, màu, trạng thái.

## 27.4 Nối clip (extend / last frame)
- Mở prompt clip sau bằng state handoff: vị trí + hướng + tư thế + vật đang cầm + trạng thái môi trường.
- "Preserve the exact face, hair, body proportions, outfit and props from the preceding clip."
- Sau 2–3 lần extend liên tiếp: đưa lại reference nhân vật sạch để reset identity.
- Không dùng frame cuối có motion blur hoặc bị che khuất làm first frame; chọn frame rõ nét gần cuối.

## 27.5 Câu khóa tiếng Anh
- "The glass stays on the table where she set it down."
- "He keeps the phone in his right hand throughout."
- "The window remains open; rain continues at the same intensity."
- "Her sleeves stay rolled to the elbow."
- "The same blue coils are still wrapped around her left arm, slowly fading."

## 27.6 Lỗi
- STATE_RESET, PROP_TELEPORT, POSSESSION_SWAP, WARDROBE_DRIFT → sửa theo bảng 42.2.
- Hiệu ứng mất sau camera move hoặc nối clip → EFFECT_PERSISTENCE_LOSS / EFFECT_CHAIN_BREAK, sửa theo module 54.
