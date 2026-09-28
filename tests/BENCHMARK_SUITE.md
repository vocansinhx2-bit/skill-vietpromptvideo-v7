# BENCHMARK SUITE (gộp)
Mỗi mục dưới đây là một bộ benchmark trước đây nằm ở file riêng; tên file gốc ghi ở tiêu đề mục. `master_prompt_purity_benchmark.md` vẫn là file riêng.

## [action_choreography_benchmark]
## ACTION CHOREOGRAPHY BENCHMARK (module 52 + G02 + 22 + 48)
Mỗi case: đưa ý tưởng hành động thô, kiểm tra Exchange Plan và prompt cuối.

| ID | Input | PASS khi |
|---|---|---|
| A01 | "Hai người đánh nhau cực chất, epic" | Loại tính từ; lập bảng exchange có initiator/responder, khoảng cách, đường đi, điểm chạm, phản ứng |
| A02 | Pha đánh 10 đòn trong 8s | EXCHANGE_OVERLOAD; cắt theo ngân sách 52.3 hoặc tách clip |
| A03 | Một chọi nhiều | CROWD_SIMULTANEOUS được chặn; đối thủ vào làn lần lượt |
| A04 | Prompt có zoom + whip pan + orbit + shake | CAMERA_STACK; giữ một đường camera |
| A05 | Hai fighter không khóa phía khung | AXIS_BREAK / FIGHTER_MERGE; khóa frame side + màu trang phục mỗi người |
| A06 | Segment kết thúc giữa cú đá, clip sau nối tiếp | NO_RECOVERY_STATE; `Ends with:` có khoảng cách + tư thế ổn định |
| A07 | Slow motion ở 3 đoạn | SLOWMO_OVERUSE; một đoạn có mốc giây |
| A08 | Brief có máu, thương tích | GRAPHIC_RISK; ngôn ngữ dàn dựng, cắt sang hậu quả, câu compliance trong constraints |
| A09 | Rượt đuổi xe qua 3 địa điểm trong 10s | Tách clip theo địa điểm (51); hướng di chuyển giữ nguyên qua điểm nối |
| A10 | Đấu kiếm | Tối đa 3 exchange đo đếm; vũ khí cứng, không biến dạng; tia lửa chỉ ở lần chạm cuối |
| A11 | Đòn trượt không khí trong video đã tạo | Debug 42 mã 34 ACTION_NO_CONTACT; chỉ đổi một biến |
| A12 | Pha đánh 45s | PLAN_SEQUENCE_FILM; chia theo exchange, nối bằng last frame, hero exchange có ngân sách thử riêng |

Gates: Exchange Plan xuất trước prompt; không còn mã lỗi 52.13; prompt ≤2000 ký tự; purity lint PASS.

## [animation_style_benchmark]
## ANIMATION STYLE BENCHMARK (module 53 + G13 + 29 + 18)
Mỗi case: đưa brief hoạt hình thô, kiểm tra Style Plan và prompt cuối.

| ID | Input | PASS khi |
|---|---|---|
| N01 | "Làm kiểu anime" không thêm gì | Chọn một họ phong cách; medium line + style lock bằng tham số; danh sách loại trừ |
| N02 | Brief ghi tên studio / franchise | STUDIO_NAME_RISK; thay bằng kỹ thuật + thời kỳ + palette |
| N03 | Prompt 2D có "85mm, bokeh, shallow depth of field" | LENS_GRAMMAR_IN_2D; đổi sang rostrum grammar |
| N04 | Người thật trong bối cảnh hoạt hình, không khai báo ý đồ | STYLE_MIX; một họ phong cách |
| N05 | Cảnh anime đánh nhau nhanh | Tốc độ vào smear / speed lines / nền cuộn; impact frame; held frame; thông số bóng lặp trong segment nhanh; bật 52 |
| N06 | Clip hoạt hình trôi về bán ảnh thật (debug) | 42 mã 37 PHOTOREAL_DRIFT; medium line đầu prompt + loại trừ |
| N07 | Chuyển động trôi, thiếu lực | FLOATY_MOTION; on twos, anticipation, held frames |
| N08 | Hai nhân vật đổi màu áo cho nhau | PALETTE_SWAP; khóa màu chính/phụ/nhấn từng nhân vật |
| N09 | 3D stylized feature | Được dùng ngôn ngữ ống kính; squash & stretch vừa phải; loại trừ da ảnh thật |
| N10 | Stop-motion clay | Nhịp hơi giật on twos, chất liệu tay nặn, không motion blur mượt |
| N11 | Series 4 clip hoạt hình | Medium line + palette lặp nguyên văn; layout cuối clip trước = layout đầu clip sau (51) |
| N12 | Ảnh reference nhân vật có ngón tay bị cắt, tay chồng nhau | Yêu cầu ảnh sạch một tư thế trước khi animate (53.10) |

Gates: Style Plan xuất trước prompt; không còn mã lỗi 53.12; prompt ≤2000 ký tự; purity lint PASS.

## [cinematic_craft_benchmark]
## CINEMATIC CRAFT BENCHMARK (module 49 + 50 + 20)
Mỗi case: đưa ý tưởng thô, kiểm tra Craft Plan và prompt cuối.

| ID | Input | PASS khi |
|---|---|---|
| C01 | Ý tưởng 1 câu, không nêu thể loại | Chọn đúng một playbook; Craft Plan đủ 10 trường, trường đoán được ghi "giả định" |
| C02 | Quảng cáo 15s | Hook ở 0–2s, frame đầu kể được vấn đề; cài → trả là bằng chứng quan sát được |
| C03 | Cảnh buồn lặng | Ống kính dài/tĩnh, nhịp chậm, khoảng lặng trước đỉnh; không có camera xoay nhanh (EMOTION_STYLE_MISMATCH) |
| C04 | Brief đầy "epic, stunning, 8k, masterpiece" | GENERIC_ADJECTIVE_BLOAT; xóa hết, thay bằng ống kính/ánh sáng/chất liệu cụ thể |
| C05 | Cảnh 10s có 3 segment cùng độ dài, cùng cỡ cảnh | UNIFORM_RHYTHM hoặc COVERAGE_MONOTONY; đổi cỡ cảnh hoặc độ dài |
| C06 | Payoff xuất hiện mà không có vật/hành động cài trước | PAYOFF_UNPLANTED; thêm plant ở segment đầu |
| C07 | Đỉnh cảm xúc ở giây 1 của clip 10s | PEAK_MISPLACED; dời đỉnh về 60–80% |
| C08 | Cảnh hành động | Playbook G02; bật 48 + 22; mỗi segment khóa hướng di chuyển; tối đa một đoạn slow motion |
| C09 | Horror | Âm ngoài khung hoặc khoảng lặng làm hook; ánh sáng một nguồn; không lộ hết mối đe dọa trước đỉnh |
| C10 | Thể loại lai (comedy + action) | Một playbook chính + tối đa một thủ pháp mượn; không trộn quy tắc mâu thuẫn |
| C11 | Prompt chỉ có "sad music" | SOUND_FLAT; có ambience + SFX gắn thời điểm + quyết định nhạc rõ |
| C12 | Craft Plan tốt nhưng prompt chứa "she feels hopeful" | Tên cảm xúc trừu tượng bị thay bằng biểu hiện quan sát được |

Gates: Craft Plan xuất trước prompt; không còn mã lỗi 49.13; prompt ≤2000 ký tự; purity lint PASS; evaluator (38) phần craft ≥20/25.

## [example_contamination_benchmark]
## EXAMPLE CONTAMINATION BENCHMARK
Given memorable examples with distinctive subjects, objects, colors, numbers and outcomes:
- identify which details are invariants vs evidence;
- compile mechanism without hidden template copying;
- verify unseen variation remains possible;
- fail if the artifact turns examples into a default list/menu without explicit user request.

## [runtime_failure_benchmark]
## RUNTIME FAILURE BENCHMARK
Failures: example anchoring, creator leakage, reference leakage, state reset, spatial flip, prop teleport, duplicate hands/props, speaker swap, camera conflict, complexity overload, capability mismatch.
Correct response must classify root layer before editing wording.

### Debug cases (module 42 + 22 + 27 + 48)
| # | Triệu chứng user báo | Phải route về | Sửa đúng thứ tự |
|---|---|---|---|
| 1 | Nhân vật quay lưng/đổi hướng mặt giữa clip | SPATIAL_FLIP / ORIENTATION_DRIFT | orientation ledger → xoay người thành hành động riêng → wording |
| 2 | Hai người đổi chỗ trái/phải sau cut | SPATIAL_FLIP | screen geography lock lặp lại ở mọi segment |
| 3 | Nhân vật bị lật gương, phụ kiện đổi bên | MIRROR_FLIP | kiểm tra reference bị flip → khóa bên phụ kiện |
| 4 | Người thứ ba nói thay | SPEAKER_SWAP | speaker + mouth-at-rest cho người nghe |
| 5 | Câu thoại ngắn bị chèn lời lẩm bẩm | FILLER_BABBLE | lấp đầy cửa sổ thoại hoặc cắt segment |
| 6 | Hành động xong sớm rồi tua ngược | ACTION_REVERSAL_FILL | nối 2–3 hành động cùng hướng hoặc rút duration |
| 7 | Tay thừa trong cảnh nhóm/cận tay | ORPHAN_LIMB | đếm tay + chủ sở hữu + hướng vào khung |
| 8 | Tay làm động tác nhưng vật không đổi | MIMED_MANIPULATION | chuỗi nhân quả 5 phần |
| 9 | Vật bên cạnh bay theo vật chính | PHYSICS_ANCHOR_LEAK | khai báo vật đứng yên |
| 10 | Mặt trôi dần sau nhiều lần extend | IDENTITY_DRIFT | canonical reset bằng reference sạch |
| 11 | Model copy phông nền từ ảnh reference nhân vật | REFERENCE_LEAKAGE | câu "Do not copy" + tách reference |
| 12 | Clip nối tiếp phát lại đoạn cũ | STATE_RESET | last frame làm first frame + "Do not replay" |
| 13 | Chưởng đang bám người mất khi camera quay đi rồi quay lại | EFFECT_PERSISTENCE_LOSS | effect ledger → camera lock trong SUSTAIN hoặc cut + restate → ba lớp neo trong `Ends with:` (module 54) |
| 14 | Luồng điện nhảy sang nhân vật khác | EFFECT_DETACHED | neo source + attachment trái/phải → "never jumps to another character" |
| 15 | Hiệu ứng như glow dán lên, không hắt sáng | EFFECT_STATIC_OVERLAY | tạo lại từ đầu với motion behavior + light spill, không thêm bằng edit |

Gates:
- Không case nào được sửa bằng cách chỉ viết prompt dài hơn.
- Mỗi lần regenerate chỉ đổi 1 biến.
- Prompt sửa xong qua purity lint PASS.

## [seedance_2_0_benchmark]
## SEEDANCE 2.0 BENCHMARK
Verify concise phases, low timestamp granularity, explicit reference roles, identity/state continuity and no camera/action/dialogue overload.

## [seedance_2_5_benchmark]
## SEEDANCE 2.5 BENCHMARK
Verify useful timestamp blocks, state inheritance, reference authority, screen geography, micro-actions, separate audio track and controlled event density.

### Parameter gates
| ID | Case | PASS khi |
|---|---|---|
| S25-P01 | Brief 45s liên tục | Tách thành ≥2 clip 4–30s, nối bằng last frame; không xuất một prompt 45s |
| S25-P02 | First+last frame + ratio 16:9 | Router đổi ratio sang adaptive hoặc cảnh báo TaskTypeConstraint |
| S25-P03 | Edit video có sẵn | task_type=edit, ratio adaptive, duration -1, có @Video1, động từ add/remove/replace |
| S25-P04 | Extend clip | task_type=extend, động từ extend/continue, không mô tả lại hành động cũ |
| S25-P05 | 12 ảnh + 4 video + 2 audio | Kiểm tra giới hạn (≤30 ảnh, ≤10 video, ≤10 audio, ≤50 file, tổng video/audio ≤30.2s) |
| S25-P06 | Yêu cầu 4K | Báo không hỗ trợ; đề xuất 720p/1080p tùy nhà cung cấp |
| S25-P07 | Prompt > 2000 ký tự | Nén qua module 31 trước khi xuất |

### Prompt-writing gates
| ID | Case | PASS khi |
|---|---|---|
| S25-W01 | Timeline 0-3/2-6s chồng lấn | Linter báo lỗi; sửa thành liên tục, mỗi đoạn có "Ends with" |
| S25-W02 | Đoạn 10s chỉ có "she looks around" | SEGMENT_UNDERFILLED; thêm hành động có định lượng hoặc rút ngắn |
| S25-W03 | Hai người cùng nói trong một shot lip-sync | SPEAKER_AMBIGUITY; tách shot, ghi rõ ai ngậm miệng |
| S25-W04 | Thoại có số "3.5%" | Viết thành chữ; ghi ngôn ngữ cạnh câu thoại |
| S25-W05 | @Image1 vừa là nhân vật vừa là bối cảnh | Tách vai trò hẹp + "Do not copy ... from @Image1" |
| S25-W06 | Chất lỏng đổ không có điểm dừng | Bổ sung điểm kết thúc dòng chảy và trạng thái vật chứa |
| S25-W07 | Nhân vật ra khỏi khung rồi quay lại | Ghi thời gian bị che khuất + bất biến trang phục/đạo cụ |
| S25-W08 | Nối clip 2 phát lại hành động clip 1 | Có câu "continue forward... Do not replay" |
| S25-W09 | Audio có nhạc, SFX, thoại, phụ đề | Dùng đúng ( ) < > { } 【 】 |

Gates: runtime purity PASS; không có raw asset ID trong prompt; score ≥90.

## [sequence_planner_benchmark]
## SEQUENCE / FILM PLANNER BENCHMARK (module 51)
Mỗi case: đưa ý tưởng vượt một clip, kiểm tra Sequence Plan trước Video Setup Plan.

| ID | Input | PASS khi |
|---|---|---|
| S01 | Phim ngắn 60s, 1 nhân vật, 3 địa điểm | Route PLAN_SEQUENCE_FILM; mỗi clip ≤30s và một địa điểm; arc toàn phim có đỉnh ở 70–85% |
| S02 | Rượt đuổi 4 địa điểm trong 10s | CLIP_OVERPACKED; tách thành nhiều clip, khóa hướng đuổi và handoff ở từng điểm nối |
| S03 | Hai nhân vật xuyên suốt 5 clip | Continuity bible khóa khuôn mặt, trang phục, đạo cụ, ánh sáng; thiếu → BIBLE_MISSING |
| S04 | Có hero shot (khoảnh khắc chính) | Hero shot tách clip riêng, ngân sách 3–5 lần thử; generate sau clip thiết lập |
| S05 | 6 clip liền đều là medium shot tĩnh | COVERAGE_MONOTONY; đề xuất wide/close/insert xen kẽ |
| S06 | Điểm nối không nói kiểu nối | JOIN_UNPLANNED; mỗi điểm nối có kiểu (cut/match/extend/last-frame) và hướng nhân vật đầu clip sau |
| S07 | Nối clip bằng last frame | Last frame clip trước = first frame clip sau; ratio adaptive; không trộn reference mode |
| S08 | Shot list SCxx_SHxx từ skill ảnh | Giữ nguyên shot ID; map mỗi shot vào clip; bridge 47 chạy trước |
| S09 | Trailer 30s | Cấu trúc theo thời lượng (51.2); nhịp tăng dần; kết bằng title hold hoặc sting |
| S10 | Series 5 tập cùng format | Module 12: tách invariant và chiều biến thể; không lặp cùng hook/payoff giữa các tập |

Gates: Sequence Plan xuất trước; không còn mã lỗi 51.10; mỗi clip sau đó qua module 46 + 49 checklist; mỗi prompt ≤2000 ký tự và purity lint PASS.

## [spatial_orientation_benchmark]
## SPATIAL / ORIENTATION / BODY INTEGRITY BENCHMARK (module 22 + 27 + 48)

### Cases
1. Một nhân vật đi bộ từ trái sang phải, 3 shot liên tiếp → hướng di chuyển giữ nguyên, tốc độ camera tuyệt đối lặp lại giống nhau trong mọi prompt.
2. Nhân vật quay 180° để nhìn ra sau → xoay người là một hành động riêng có thời lượng; có reference mặt sau hoặc hạ yêu cầu.
3. Hai người đối thoại ngồi đối diện → A frame-left facing right, B frame-right facing left, lặp ở mọi segment; eyeline ghi rõ.
4. Nhân vật vào phòng qua cửa → spatial layout block: vị trí camera, vật cản, hướng đi quanh vật.
5. Ảnh reference nhân vật bị lật gương so với ảnh khác → phát hiện và chọn một bản chuẩn trước khi viết prompt.
6. Cận cảnh tay mở khóa → "only two hands in frame", tay nào từ đâu vào.
7. Nhóm 4 người đứng hàng → đếm người, thứ tự trái→phải, chỉ tối đa 2 người thao tác bằng tay.
8. Nhân vật bị che khuất 2s rồi xuất hiện lại → nhắc lại character lock ngay sau khi hết che.
9. Nối 3 clip bằng last frame → mỗi clip có orientation handoff (vị trí, hướng thân, hướng mặt).

Gates:
- Mỗi segment có đủ trường orientation cho từng nhân vật đang xuất hiện.
- Không có đổi hướng nào không được viết thành hành động.
- Không mâu thuẫn giữa screen geography và camera axis.
- Prompt cuối qua purity lint PASS.

## [v6_core_benchmark]
## V6 CORE BENCHMARK
Test sparse brief, example-heavy brief, contradictory references, creator notes mixed with requirements, series diversity, stateful video, 30s complexity overload, dialogue, one-take request, final-state reference leakage and model profile routing.
Gates: no unresolved critical contradiction; runtime purity PASS; score >=90.

## [vfx_effect_persistence_benchmark]
## VFX EFFECT PERSISTENCE BENCHMARK (module 54 + 15 + 27 + 23 + 48)
Mỗi case: đưa brief hoặc video lỗi, kiểm tra Effect Contract, effect ledger và prompt cuối.

| ID | Input | PASS khi |
|---|---|---|
| X01 | "Nhân vật trúng chưởng, camera xoay quanh" | Phát hiện camera rời vùng chạm khi active; đổi orbit thành locked/slow push-in hoặc cut + restate (54.6) |
| X02 | Video lỗi: chưởng bám tay biến mất khi camera quay lại (debug) | 42 mã 39 EFFECT_PERSISTENCE_LOSS; effect ledger + ba lớp neo + camera lock; một biến mỗi lần |
| X03 | Brief chỉ ghi "epic magic VFX" | EFFECT_LABEL_ONLY; điền Effect Contract đủ source/attachment/look/lifecycle/endpoint |
| X04 | Năng lượng nhảy sang nhân vật khác | EFFECT_DETACHED; neo bộ phận cơ thể trái/phải + "never jumps to another character" |
| X05 | Glow đứng yên như dán | EFFECT_STATIC_OVERLAY; "changes shape every frame" + light spill; tạo lại từ đầu thay vì edit |
| X06 | Hiệu ứng tắt đột ngột giữa clip | EFFECT_NO_ENDPOINT; lifecycle có mốc giây + endpoint + residue |
| X07 | Lửa + điện + băng cùng lúc trong 8s | EFFECT_STACK; một hiệu ứng chính, tối đa một phụ nhỏ, tách clip |
| X08 | Tay méo, ngón nhân đôi nơi năng lượng chạm | EFFECT_BODY_CORRUPTION; "around, not through", thu nhỏ vùng chạm, bật 48 |
| X09 | Anime: chưởng thành glow ảnh thật | EFFECT_STYLE_DRIFT; đưa hiệu ứng vào style lock (53.4 mục 6), mảng màu cứng có viền |
| X10 | Hai clip nối, clip sau mất hiệu ứng | EFFECT_CHAIN_BREAK; last frame thấy hiệu ứng/residue + effect handoff "the same … still …" |
| X11 | Cần thấy phản ứng người thứ ba giữa SUSTAIN | Dùng cut, không pan; shot sau mở bằng câu nhắc trạng thái hiệu ứng |
| X12 | Hiệu ứng bị che khuất 1s | Ledger ghi `occluded t1–t2 + reappears unchanged`; prompt nhắc lại look + attachment khi lộ lại |
| X13 | Mất hiệu ứng 2s giữa clip đã gần đạt | Edit mode chỉ đoạn t1–t2, giữ motion/camera/lighting/audio (54.11) |

Gates: Effect Contract + effect ledger xuất trước prompt; mỗi `Ends with:` sau CONTACT có hiệu ứng + ánh sáng + residue; không còn mã lỗi 54.13; prompt ≤2000 ký tự; purity lint PASS.

## [video_scene_director_brain_benchmark]
## VIDEO SCENE DIRECTOR BRAIN BENCHMARK (module 46 + 47)
Mỗi case: đưa một ý tưởng cảnh quay thô, kiểm tra Video Setup Plan trước khi viết prompt.

| ID | Input | PASS khi |
|---|---|---|
| B01 | Ý tưởng 1 câu, không nói thời lượng/model | Scene DNA đủ 12 trường (hoặc đánh dấu giả định); chọn archetype; chọn input mode |
| B02 | Cảnh rượt đuổi nhiều địa điểm trong 10s | SEGMENT_OVERLOADED; đề xuất tách shot/clip |
| B03 | Có keyframe START và END từ skill ảnh | Chọn chế độ first+last; ratio adaptive; không trộn reference-to-video |
| B04 | Có ảnh nhân vật + ảnh last frame clip trước | REFERENCE_VS_LASTFRAME_CONFLICT được giải quyết: last frame = @Image1 first frame |
| B05 | Hai nhân vật đối thoại qua lại 20s | Lịch speaker, mỗi shot một người nói, câu 5–8s |
| B06 | Shot list SCxx_SHxx từ skill ảnh có PEAK_ACTION_FREEZE_RISK | Bridge chuyển keyframe thành trạng thái trước/sau, không dùng peak làm first frame |
| B07 | Dossier có CHAIN_IDENTITY_BREAK | Chặn tạo video; yêu cầu sửa reference ảnh trước |
| B08 | Cảnh chỉ có âm thanh tham chiếu (nhạc) | Cho phép audio-only reference trên 2.5; từ chối trên 2.0 |
| B09 | Brief mô tả cùng hành động ở hai chỗ | DUPLICATE_ACTION_DESCRIPTION; gộp lại |
| B10 | Ý tưởng không có thay đổi quan sát được | Feasibility (13) yêu cầu thiết kế lại trước khi viết |

Gates: plan xuất trước prompt; mọi mã lỗi 46.10 được xử lý; prompt cuối qua purity lint PASS.
