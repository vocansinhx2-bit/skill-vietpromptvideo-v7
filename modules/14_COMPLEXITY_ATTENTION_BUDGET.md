# 14 — COMPLEXITY & ATTENTION BUDGET
Budget independent subjects, props, state changes, camera changes, simultaneous actions, dialogue turns, audio events and reference responsibilities.
High control density reduces reliability.
Protect hero action, identity, causal transitions and payoff before decorative detail.

## 14.1 Ngưỡng đề xuất cho mỗi shot / segment
Các con số là ngưỡng thiết kế an toàn, không phải giới hạn cứng của model.
| Hạng mục | An toàn | Rủi ro | Vượt → |
|---|---|---|---|
| Nhân vật có hành động | 1–2 | 3 | ≥4: nhóm thành đám đông nền, không giao hành động riêng |
| Nhân vật dùng tay | 1–2 | — | ≥3: chia shot (module 48) |
| Đạo cụ được thao tác | 1 | 2 | ≥3: chia shot |
| Thay đổi trạng thái vật | 1 | 2 | chia segment |
| Chuyển động camera chính | 1 | 2 tuần tự | 2 đồng thời: bỏ một |
| Người nói | 1 | — | ≥2: chia shot |
| Sự kiện SFX nổi bật | 1–3 | 4–5 | giảm |
| Hành động chính mỗi segment 8–10s | 1–2 | 3 | chia segment |

## 14.2 Ngân sách cả clip
- Clip ≤10s: 1 hành động chính + 1 phản ứng.
- Clip 10–20s: 2–3 beat.
- Clip 20–30s: 3–4 beat; mỗi beat có end state.
- Chuyển cảnh/cut trong clip: ≤3 shot mỗi 15s.
- Khóa identity cho ≤5 thuộc tính mạnh mỗi nhân vật; dồn chi tiết phụ vào reference.

## 14.3 Thứ tự cắt khi quá ngân sách
1. Bỏ chi tiết trang trí (hạt bụi, vật nền, chuyển động phụ).
2. Bỏ camera move trang trí.
3. Giảm số nhân vật có hành động.
4. Chia segment/shot.
5. Chỉ sau cùng mới rút gọn hero action.

## 14.4 Tính điểm nhanh
Đếm: nhân vật có hành động + đạo cụ thao tác + thay đổi trạng thái + chuyển động camera + người nói.
Tổng ≤4 mỗi segment: PASS. 5–6: WARN, xem lại. ≥7: FAIL → COMPLEXITY_OVERLOAD, chia segment.
