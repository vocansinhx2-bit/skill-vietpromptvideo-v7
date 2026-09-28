# 49 — CINEMATIC CRAFT ENGINE

> Lớp "làm cho hay". Module 46 quyết định setup kỹ thuật; module này quyết định cảm xúc, nhịp, hook, bố cục, ống kính, âm thanh kể chuyện. Chạy sau 46 bước V2 (archetype) và trước V6 (timeline). Output là **Craft Plan** (design-time), sau đó được compile thành câu lệnh quan sát được trong prompt.
> Target reader: `HUMAN_DESIGNER` / skill. Không đưa tên module, mã lỗi, điểm số vào prompt video.

## 49.1 Luật nền
1. Mỗi clip có **một câu cảm xúc chủ đạo** (controlling emotion) và **một khoảnh khắc chữ ký** (signature moment) mà người xem sẽ nhớ.
2. Cảm xúc chỉ tồn tại khi nhìn/nghe thấy được: chuyển tính từ thành ống kính, bố cục, ánh sáng, nhịp, hành vi, âm thanh.
3. Cụ thể thắng hoa mỹ: một chi tiết đúng lúc (giây, vị trí khung, lực) mạnh hơn năm tính từ.
4. Một luật hình ở đầu prompt (FORMAT/style), một luật âm ở cuối (AUDIO), ở giữa là các segment.
5. Craft không được phá luật an toàn của 22/27/42/48. Nếu một lựa chọn craft làm tăng rủi ro lỗi (orbit nhanh, 5 người, lửa lớn) → giữ cảm xúc, đổi phương tiện.

## 49.2 Hook (0–3 giây đầu)
Chọn đúng **một** loại hook trước khi viết:
| Hook | Cơ chế | Cách dựng trong prompt |
|---|---|---|
| Problem | Thấy ngay điều sai | Frame đầu đã chứa sự cố đang xảy ra |
| Promise | Thấy ngay kết quả mong muốn | Mở bằng trạng thái đẹp nhất, rồi lùi về quá trình |
| Contrast | Trước/sau, lớn/nhỏ, im/ồn | Hai trạng thái đối lập trong 2 giây đầu |
| Curiosity | Câu hỏi chưa trả lời | Che một phần, âm thanh ngoài khung, vật lạ |
| Reveal | Lộ dần chủ thể | Ánh sáng quét, lấy nét chuyển, vật cản rời khỏi khung |
| Motion surprise | Chuyển động bất ngờ phá tĩnh | Khung tĩnh 1 giây rồi một chuyển động dứt khoát |
| In medias res | Vào giữa hành động | Segment 1 bắt đầu khi hành động đã chạy |
| Sound hook | Âm thanh kéo tai trước | Âm thanh lạ/đột ngột trước khi thấy nguồn |

Luật hook:
- Frame đầu tiên một mình phải kể được chủ thể + tình huống (nền tảng hiển thị frame đầu trước khi chạy).
- Chuyển động hoặc thay đổi đầu tiên bắt đầu trong 0.5–1 giây với nội dung short-form. Phim chậm (drama, noir) được giữ tĩnh, nhưng khi đó phải có một yếu tố sống (nước chảy, khói, âm thanh) để khung không chết.
- Không mở bằng establishing shot trống cho nội dung mạng xã hội, trừ khi chính không gian là hook.
- Không nhồi chữ vào hook; caption thêm ở hậu kỳ.

## 49.3 Đường cong cảm xúc
Gán cường độ 1–5 cho từng segment trong Craft Plan.
| Hình dạng | Dùng cho |
|---|---|
| Rise (1→5) | hành động, quảng cáo, reveal |
| Fall (5→1) | hậu quả, buồn, kết thúc có dư âm |
| Rise–fall (2→5→2) | drama, câu chuyện ngắn có payoff |
| Fall–rise (4→1→5) | hài (setup–lệch–punchline), cứu vãn |
| Flat–spike (2→2→5) | kinh dị jump, twist, hài deadpan |

Luật:
- Hai segment liền nhau không cùng cường độ, trừ khi cố ý "hold" và ghi rõ lý do trong plan.
- Đỉnh đặt ở khoảng 60–80% thời lượng. Không đặt đỉnh ở giây 0 hay giây cuối (trùng luật 46.7).
- 10–15% cuối là aftermath / hold / button: để phản ứng hoặc hình ảnh đọng lại.

## 49.4 Setup → Payoff
- Mỗi payoff có một plant nhìn/nghe thấy được ở segment trước đó, cách ít nhất một segment.
- Plant phải tự nhiên trong khung (vật trên bàn, âm thanh nền, cử chỉ lặp), không được nhấn bằng camera zoom thẳng vào, trừ khi thể loại cho phép (hài, bí ẩn).
- Payoff phải xảy ra trên màn hình và có end state rõ; không để "ngụ ý".
- Một clip ngắn (≤15s) tối đa một cặp plant–payoff. Clip 30s tối đa hai.

## 49.5 Bảng cảm xúc → ngôn ngữ điện ảnh
| Cảm xúc | Cỡ cảnh | Ống kính / DOF | Camera | Bố cục | Ánh sáng | Màu | Nhịp | Âm thanh |
|---|---|---|---|---|---|---|---|---|
| Căng thẳng / sợ | CU chặt, hoặc wide có khoảng trống lớn | 24–35mm gần mặt; DOF nông ở CU | locked hoặc push rất chậm | chủ thể lệch mép, khoảng tối lớn phía sau | low-key, nguồn đơn cứng, bóng dày | lạnh, bão hoà thấp | hold dài rồi cắt gắt | ambience thưa, khoảng lặng trước biến cố |
| Cô đơn | wide / extreme wide | 24–35mm, deep focus | static | chủ thể nhỏ, nhiều negative space | mềm, phẳng | lạnh hoặc nhạt | chậm | một âm nền đơn, xa |
| Thân mật / lãng mạn | MCU, two-shot gần | 85mm, DOF nông, bokeh | locked hoặc drift nhẹ | hai người chia khung, gần | mềm, ấm, backlight viền | ấm, da đẹp | chậm, hold | gần micro, hơi thở, ít nhạc |
| Vui / hài | medium, wide đủ thấy cơ thể | 28–35mm | static (hài cần khung ổn định) | đối xứng, gọn | sáng đều, key cao | tươi, bão hoà vừa | setup đều → pause → punchline | pause im 0.5–1s trước punchline |
| Hùng tráng / kinh ngạc | extreme wide + low angle | 18–24mm | crane/rise hoặc push chậm, liên tục | chủ thể nhỏ trước khối lớn, leading lines | ánh sáng tự nhiên mạnh, rim | tương phản ấm–lạnh | chậm, dài | nhạc nền lớn dần, âm trầm |
| Quyền lực / áp đảo | medium low angle | 35–50mm | locked hoặc push chậm | chủ thể trung tâm, headroom thấp | key cứng từ trên/cạnh | tối, một màu nhấn | chậm, chắc | ít âm, trầm |
| Yếu đuối | high angle, CU | 50–85mm | locked | chủ thể thấp trong khung | mềm, từ trên | nhạt | chậm | im, hơi thở |
| Gấp gáp / hành động | medium + insert ngắn | 24–35mm | track song song, handheld có kiểm soát | hướng chuyển động có khoảng trống phía trước | cứng, có tương phản | tương phản cao | cắt nhanh, có 1 nhịp dừng | SFX sắc, nhạc nhịp nhanh |
| Bí ẩn | CU chi tiết, silhouette | 50–100mm | push rất chậm, rack focus | che một phần, frame-in-frame | low-key, nguồn thực trong khung | lạnh + một màu nhấn | chậm | âm ngoài khung |
| Hoài niệm | medium | 50mm, DOF vừa | drift chậm | ấm, nhiều lớp tiền cảnh | nắng thấp, halation | ấm, phai | chậm | âm nền mềm, nhạc mộc |
| Bình yên | wide/medium | 35–50mm | static hoặc drift rất nhẹ | cân bằng, đường ngang ổn định | mềm tự nhiên | pastel/tự nhiên | chậm | ambience thiên nhiên |
| Bất ngờ / reveal | từ CU ra wide hoặc ngược lại | đổi cỡ cảnh gắt | hard cut hoặc pull-out 1 lần | lộ thông tin ở vùng đã để trống | đổi độ sáng tại reveal | màu nhấn xuất hiện lúc reveal | im → bùng | cắt âm 0.5s trước reveal |

Mỗi segment chọn một hàng chính. Không trộn hai cảm xúc đối lập trong một segment.

## 49.6 Lens lock
Ghi tiêu cự hoặc mô tả tương đương cho từng segment, không viết "cinematic lens" chung chung.
- 16–24mm: không gian rộng, méo khi gần, cảm giác lớn/ngột.
- 28–35mm: tự nhiên, kể chuyện, đi theo người.
- 50mm: trung tính, gần mắt người.
- 85mm: chân dung, nén hậu cảnh, tách chủ thể.
- 100mm macro: chi tiết sản phẩm, vật liệu.
- 135mm+: nén mạnh, quan sát từ xa, cảm giác bị theo dõi.
DOF: `deep focus` cho không gian và hài; `shallow depth of field` cho cảm xúc và sản phẩm. Khi đổi tiêu cự trong một clip, mỗi đổi = một hard cut.

## 49.7 Bố cục
Viết bố cục thành vị trí quan sát được:
- Thirds: `subject on the left third, looking into the open right side of frame`.
- Negative space: `the figure occupies the lower fifth of frame, empty sky above`.
- Leading lines: `the road lines lead from the bottom corners to the figure`.
- Frame-in-frame: `seen through the doorway, the door frame borders both sides`.
- Tiền cảnh: `out-of-focus foreground leaves at frame edge`.
- Đối xứng: `perfectly centered, symmetrical corridor`.
Luật: luôn chừa khoảng trống phía trước hướng nhìn và hướng di chuyển (lead room), trừ khi cố ý gây ngột.

## 49.8 Nhịp & dựng trong clip
- Không chia segment đều nhau máy móc; nhịp đến từ tương phản dài–ngắn.
- Cắt trên hành động (cut on action) khi đổi shot giữa chuyển động; viết `hard cut` rõ ràng.
- Giữ (hold) sau đỉnh cảm xúc ít nhất 1–2 giây.
- Độ dài shot trung bình theo thể loại xem module 50.
- Một clip có tối đa một đoạn slow motion và phải ghi rõ khoảng giây; mặc định `real-time speed, no slow motion`.

## 49.9 Âm thanh kể chuyện
- Khoảng lặng: cắt ambience 0.5–1s trước reveal / punchline / jump.
- Pre-lap: âm thanh của shot sau bắt đầu cuối shot trước để nối cảm xúc.
- Motif: một âm lặp 2 lần có nghĩa (plant–payoff bằng âm).
- Âm ngoài khung: nghe trước khi thấy, tạo tò mò.
- Phối cảnh âm: gần mic cho thân mật, xa và vang cho cô đơn.
- Chữ ký âm: mỗi clip một âm đặc trưng, đặt đúng giây.
Mọi âm vẫn theo cú pháp module 26.

## 49.10 Kết cấu hình ảnh, chống "nhựa"
- Thêm dấu vết quang học có kiểm soát: `fine 35mm film grain`, `soft halation on highlights`, `slight lens breathing`.
- Ánh sáng có nguồn thật trong không gian (motivated light), không "dramatic lighting" chung chung.
- Chi tiết bề mặt: bụi, vân gỗ, vết nước, nếp vải.
- Bỏ các từ rỗng: `8k`, `masterpiece`, `ultra-detailed`, `hyperrealistic`, `epic`, `stunning`, `cinematic` đứng một mình.

## 49.11 Specificity law
- Sự kiện quan trọng đặt theo giây (độ mịn 0.5s).
- Một cơ chế vật lý / hiệu ứng được mô tả một lần và lặp y hệt ở mọi segment, không biến tấu.
- Một logic nguồn sáng giữ suốt clip.
- Diễn xuất nhỏ và muộn nửa nhịp tạo cảm giác thật hơn phản ứng to và tức thì.

## 49.12 Craft Plan (thêm vào Video Setup Plan)
| Trường | Nội dung |
|---|---|
| controlling_emotion | 1 cảm xúc |
| hook_type | 1 loại ở 49.2 + mô tả frame đầu |
| curve | hình dạng + cường độ từng segment |
| plant → payoff | cặp, segment đặt |
| signature_moment | 1 khoảnh khắc + giây |
| lens_per_segment | tiêu cự / DOF |
| composition_per_segment | vị trí chủ thể, khoảng trống |
| color_script | nền / phụ / nhấn (module 29) |
| sound_design | khoảng lặng, motif, chữ ký âm |
| ending_type | button / hold / loop / cliffhanger |

## 49.13 Craft failure codes
| Code | Ý nghĩa | Sửa |
|---|---|---|
| `HOOK_WEAK` | 2 giây đầu không có thay đổi hoặc frame đầu không kể tình huống | chọn lại hook 49.2 |
| `FLAT_CURVE` | mọi segment cùng cường độ | gán lại curve 49.3 |
| `PEAK_MISPLACED` | đỉnh ở đầu hoặc sát cuối | dời đỉnh về 60–80% |
| `PAYOFF_UNPLANTED` | payoff không có plant | thêm plant ở segment trước |
| `EMOTION_STYLE_MISMATCH` | ống kính/ánh sáng/nhịp ngược cảm xúc | tra bảng 49.5 |
| `GENERIC_ADJECTIVE_BLOAT` | tính từ rỗng thay cho chỉ dẫn | thay bằng lens/bố cục/nguồn sáng |
| `UNIFORM_RHYTHM` | segment đều nhau, không tương phản nhịp | đổi độ dài, thêm hold |
| `NO_SIGNATURE_MOMENT` | không có khoảnh khắc đáng nhớ | chọn 1 chi tiết + giây |
| `SOUND_FLAT` | âm thanh chỉ là nền, không kể chuyện | thêm khoảng lặng / motif / chữ ký âm |
