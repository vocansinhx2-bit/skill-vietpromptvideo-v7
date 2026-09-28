# 51 — SEQUENCE & FILM PLANNER

> Tầng trên module 46. Dùng khi đầu ra dài hơn một clip: phân cảnh nhiều shot, phim ngắn, quảng cáo nhiều cảnh, series. Module 46 lập kế hoạch cho **từng clip**; module này lập kế hoạch cho **cả phim** rồi giao từng clip xuống 46.
> Target reader: `HUMAN_DESIGNER` / skill. Sequence Plan là design-time; chỉ prompt của từng clip là runtime.

## 51.1 Cấp bậc
`FILM → ACT → SEQUENCE → SCENE → SHOT → CLIP (1 lần generate) → SEGMENT (timestamp trong clip)`
- Một clip có thể chứa nhiều shot (hard cut trong prompt) nếu cùng không gian, cùng nhân vật, cùng ánh sáng.
- Đổi địa điểm, đổi thời gian, đổi dàn nhân vật lớn → clip mới.

## 51.2 Cấu trúc theo độ dài
| Tổng thời lượng | Cấu trúc | Số shot gợi ý | Số clip |
|---|---|---|---|
| 15–30s | hook → phát triển → turn → payoff | 3–6 | 1–2 |
| 30–60s | hook → setup → leo thang → turn → payoff → button | 6–12 | 2–4 |
| 1–3 phút | 3 hồi thu nhỏ: hồi 1 (25%) setup + biến cố; hồi 2 (50%) leo thang + điểm giữa; hồi 3 (25%) đỉnh + kết | 12–40 | 4–12 |
| Series nhiều tập | mỗi tập một cấu trúc 15–60s + invariants chung (module 12) | theo tập | theo tập |

Cấu trúc nhanh theo mục đích:
- Quảng cáo / social: hook → vấn đề → biến đổi → kết quả → CTA.
- Du lịch / lifestyle / bất động sản: establishing → hành động → chi tiết → hero cuối.
- Hướng dẫn: trước → quá trình → sau.
- Truyện: nhân vật bước vào → phát hiện → phản ứng → giải quyết.

## 51.3 Coverage & đa dạng shot
- Mỗi scene cần tối thiểu: một shot thiết lập không gian, một shot hành động chính, một shot chi tiết hoặc phản ứng.
- Không để 3 shot liền nhau cùng cỡ cảnh hoặc cùng chuyển động camera.
- Cắt phản ứng (reaction) sau mỗi hành động có trọng lượng cảm xúc.
- Insert (tay, vật, chân) dùng để che nối và giảm rủi ro continuity.

## 51.4 Phân bổ thời lượng & ưu tiên generate
1. Xác định hero shot (signature moment của phim, 49.1) → cho nhiều thời gian và nhiều lần thử nhất.
2. Shot rủi ro cao (tay, nhóm người, đánh nhau, chất lỏng) → rút ngắn, tách riêng clip.
3. Establishing / insert → ngắn, có thể tái dùng.
4. Thứ tự generate: canonical reference (skill ảnh) → hero shot → các shot nối trực tiếp với hero → phần còn lại.
5. Ngân sách thử: hero 3–5 lần, shot thường 1–2 lần; mỗi lần thử đổi một biến (42).

## 51.5 Nối clip
| Kiểu nối | Khi nào | Cách làm |
|---|---|---|
| Frame chain | hành động liên tục qua 2 clip | last frame clip N = `@Image1` clip N+1, cắt giữa chuyển động (module 28) |
| Extend | kéo dài cùng một take | `omni_reference_task_type=extend`, handoff trạng thái (27) |
| Hard cut độc lập | đổi góc/cỡ cảnh trong cùng scene | cùng character lock + location lock + lighting lock |
| Motion match | đổi scene, giữ năng lượng | chuyển động cùng hướng, cùng tốc độ ở cuối clip trước và đầu clip sau |
| Shape / color match | chuyển cảnh nghệ thuật | hình/màu chủ đạo khớp ở frame cuối và frame đầu |
| Action match | cắt giữa một hành động | hành động bắt đầu ở clip trước, hoàn tất ở clip sau |
| Scale match | từ nhỏ ra lớn / ngược lại | cỡ vật tương tự ở điểm nối |
| Sound bridge | nối cảm xúc | âm clip sau pre-lap ở cuối clip trước (dựng ở hậu kỳ) |

Luật: hướng màn hình ở điểm nối ghi theo module 22 (orientation handoff). Tốc độ camera giữa các shot khớp nhau phải ghi cùng một giá trị tuyệt đối y nguyên trong cả hai prompt; không tham chiếu "như shot trước".

## 51.6 Continuity bible (khoá toàn phim)
| Khoá | Nội dung | Lặp ở đâu |
|---|---|---|
| Character lock | 1 câu anchor/nhân vật + reference canonical (17–19) | mọi prompt có nhân vật đó, y nguyên từng chữ |
| Location lock | bố cục, mốc cố định, hướng trục camera (22) | mọi clip cùng địa điểm |
| Lighting lock | nguồn, hướng, giờ, nhiệt màu (29) | mọi clip cùng scene |
| Palette | nền / phụ / nhấn cho toàn phim, đổi có chủ đích theo hồi | FORMAT / LIGHTING |
| Lens set | 3–4 tiêu cự dùng cho cả phim | CAMERA |
| Audio bed | ambience chính mỗi địa điểm, motif âm | AUDIO |
| Prop ledger | đạo cụ, chủ sở hữu, trạng thái theo scene (27) | STARTING STATE / ENDING STATE |

## 51.7 Nhịp toàn phim
- Xen kẽ shot dài và shot ngắn; sau đoạn nhanh là một hold.
- Mỗi hồi có một đỉnh nhỏ; đỉnh lớn nhất ở 70–85% thời lượng phim.
- Bảng màu và ánh sáng có thể đổi theo hồi để kể chuyện, nhưng phải ghi trong bible.
- Đoạn cuối có button: một hình ảnh hoặc âm thanh gói lại ý chính.

## 51.8 Nối với skill ảnh
Khi có output từ skill ảnh (module 47): giữ shot ID `SCxx_SHxx`, map mỗi shot sang một clip hoặc một segment. Canonical character/location references từ skill ảnh là nguồn duy nhất cho character lock và location lock.

## 51.9 Sequence Plan (output)
Dùng `templates/sequence_plan_template.md`:
1. Logline + cảm xúc chủ đạo toàn phim + thể loại (50).
2. Cấu trúc hồi/sequence với thời lượng.
3. Continuity bible.
4. Bảng shot: ID · mục đích kể chuyện · cỡ cảnh/ống kính · hành động · camera · âm/thoại · nối với shot sau · clip số · mode · rủi ro.
5. Bảng clip: clip · shot chứa · duration · mode · reference theo thứ tự upload · thứ tự generate · số lần thử.
6. Ghi chú dựng: thứ tự, kiểu nối, caption/nhạc thêm ở hậu kỳ.
Sau đó mỗi clip đi qua 46 → 49 → compile riêng.

## 51.10 Failure codes
| Code | Ý nghĩa |
|---|---|
| `SEQUENCE_NO_ARC` | chuỗi clip không có turn/payoff, chỉ là các cảnh đẹp rời rạc |
| `COVERAGE_MONOTONY` | 3+ shot liền nhau cùng cỡ cảnh/chuyển động |
| `BIBLE_MISSING` | nhiều clip nhưng không có character/location/lighting lock |
| `JOIN_UNPLANNED` | điểm nối giữa clip không có kiểu nối và orientation handoff |
| `HERO_UNDERBUDGETED` | hero shot bị gộp chung clip rủi ro hoặc không có ngân sách thử |
| `CLIP_OVERPACKED` | một clip chứa nhiều địa điểm hoặc nhiều thay đổi dàn nhân vật |
