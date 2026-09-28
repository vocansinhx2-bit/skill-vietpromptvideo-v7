# CHANGELOG
## 7.4.0
- Thêm module 54 VFX_EFFECT_PERSISTENCE_ENGINE: nguyên nhân hiệu ứng biến mất khi camera rời vùng chạm, Effect Contract (source, attachment, look, motion behavior, light interaction, body/object interaction, lifecycle FORM → TRAVEL → CONTACT → SUSTAIN → DISSIPATE, residue, endpoint, camera rule), ba lớp neo (hiệu ứng + ánh sáng hắt + residue), effect ledger theo segment, luật camera khi hiệu ứng active, hiệu ứng trong hoạt hình, nối clip có effect handoff, âm theo pha, ngân sách và cách sửa, mã lỗi hiệu ứng.
- Module 42: thêm lỗi 39–43 (EFFECT_PERSISTENCE_LOSS, EFFECT_DETACHED, EFFECT_STATIC_OVERLAY, EFFECT_NO_ENDPOINT, EFFECT_BODY_CORRUPTION).
- Module 15, 27, 23, 52, 53: tham chiếu chéo sang 54 (vòng đời hiệu ứng, trường EFFECT_STATE trong ledger, camera khi hiệu ứng active, mã lỗi hiệu ứng trong hành động và hoạt hình, hiệu ứng trong style lock).
- SKILL.md: bảng nạp module thêm dòng hiệu ứng; bước A3 gọi 54; Definition of Done thêm điều kiện hiệu ứng.
- Example (EVIDENCE_ONLY): `good_video_prompt_vfx_persistent_effect.md`.
- Tests: thêm bộ case hiệu ứng; `runtime_failure_benchmark` thêm case hiệu ứng.
- Đóng gói: gộp 12 file benchmark trong `tests/` thành `tests/BENCHMARK_SUITE.md` (mỗi benchmark cũ là một mục `## [tên_file]`), giữ riêng `tests/master_prompt_purity_benchmark.md` cho validate; gói còn dưới 100 file.
- Manifest: `vfx_gates`.

## 7.3.0
- Thêm module 52 ACTION_CHOREOGRAPHY_ENGINE: đơn vị đòn anticipation → action → contact → reaction → recovery, initiator/responder, ngân sách exchange theo thời lượng, trục và hướng màn hình, hai trường phái quay (WIDE_LONG_TAKE / TIGHT_KINETIC), một đường camera, trọng lượng và bằng chứng lực, rượt đuổi/stunt, chia pha hành động thành nhiều clip, ngôn ngữ dàn dựng không bạo lực đồ họa, mã lỗi hành động.
- Thêm module 53 ANIMATION_STYLE_ENGINE: 7 họ phong cách có medium line, 12 nguyên lý hoạt hình dịch thành câu prompt, style lock + danh sách loại trừ, rostrum grammar cho 2D, sakuga grammar (on twos/ones, smear, impact frame, speed lines, held frame), ánh sáng vẽ, âm cách điệu, chống style drift, không dùng tên studio/franchise, mã lỗi hoạt hình.
- Module 50: G02 Action viết lại theo 52; thêm G13 Animation; bảng tra nhanh thêm dòng Animation.
- Module 42: thêm lỗi 34–38 (ACTION_NO_CONTACT, FIGHTER_MERGE, EXCHANGE_OVERLOAD, PHOTOREAL_DRIFT, BOILING_LINES).
- SKILL.md: bảng nạp module thêm hành động/hoạt hình; bước A3 gọi 52/53; Definition of Done thêm điều kiện hành động và hoạt hình.
- Examples (EVIDENCE_ONLY): cảnh đánh live-action, cảnh anime action.
- Tests: `action_choreography_benchmark.md`, `animation_style_benchmark.md`.
- Manifest: `action_gates`, `animation_gates`.

## 7.2.0
- Cấu hình Claude Skills: frontmatter có `description` (khi nào kích hoạt), `name` bỏ hậu tố "-v6"; thêm §4.1 Module Loading Map theo task và thể loại, §4.2 bảng mặc định và quy tắc khi nào hỏi user.
- Thêm module 49 CINEMATIC_CRAFT_ENGINE: 8 loại hook, đường cong cảm xúc, plant → payoff, bảng cảm xúc → ống kính/bố cục/ánh sáng/màu/nhịp/âm, khóa ống kính, chống vẻ "nhựa", Craft Plan, mã lỗi craft.
- Thêm module 50 GENRE_PLAYBOOKS: 12 playbook thể loại (cấu trúc, độ dài shot, ống kính, camera, ánh sáng, âm, diễn xuất, signature, pitfalls).
- Thêm module 51 SEQUENCE_FILM_PLANNER: cấp bậc film → segment, coverage, thứ tự generate, continuity bible, kiểu nối, nhịp toàn phim, nối với skill ảnh.
- Mode mới `PLAN_SEQUENCE_FILM`; pipeline thêm bước A3 (craft) và A4 (sequence).
- Viết lại module 20 (story beat & payoff) và 12 (đa dạng nội dung/series); module 38 thêm nhóm điểm thẩm mỹ, giữ hard gate.
- Template: thêm mục Craft Plan vào `video_setup_plan_template.md`; thêm `sequence_plan_template.md`.
- Examples (Design, EVIDENCE_ONLY): 2 prompt video tốt, 2 prompt video xấu.
- Tests: `cinematic_craft_benchmark.md`, `sequence_planner_benchmark.md`.
- Manifest: `craft_modules`, `craft_gates`, `sequence_gates`.

## 7.1.0
- Module 22 viết lại: orientation ledger cho từng nhân vật/segment (vị trí khung, hướng thân, hướng mặt, eyeline, hướng di chuyển), luật xoay người là hành động riêng, xử lý reference lật gương, spatial layout block, handoff hướng khi nối clip.
- Module 42 thành bảng lỗi Seedance: triệu chứng → nguyên nhân gốc → thứ tự sửa → biến duy nhất cần đổi khi regenerate.
- Module 27 bổ sung: state ledger, đạo cụ theo chủ sở hữu, chống reset/teleport, handoff giữa clip.
- Module 17, 18, 19 bổ sung: character lock, vai trò hẹp cho từng reference, reference pack đồng nhất, chống leakage phông nền/trang phục, canonical reset khi extend.
- Module 14 bổ sung ngưỡng độ phức tạp theo thời lượng.
- Thêm module 48 BODY_HANDS_GROUP_INTEGRITY: tay thừa, đạo cụ nhân đôi, nhóm người, đi bộ, thao tác vật có nhân quả.
- Mở rộng `tests/runtime_failure_benchmark.md`; thêm `tests/spatial_orientation_benchmark.md`.

## 7.0.0
- Profile Seedance 2.5 viết lại đầy đủ: giới hạn thời lượng/reference/độ phân giải/aspect ratio, 3 input mode loại trừ nhau, omni_reference_task_type (auto/edit/extend), cú pháp @Image/@Video/@Audio, bracket audio, lip-sync, nối clip bằng last frame, bảng mức tin cậy.
- Profile Seedance 2.0 cập nhật giới hạn và khác biệt so với 2.5.
- Thêm module 46 VIDEO_SCENE_DIRECTOR_BRAIN: Scene DNA 12 trường, 20 archetype cảnh, cây quyết định input mode, luật timeline, Video Setup Plan, mã lỗi riêng.
- Thêm module 47 IMAGE_SKILL_BRIDGE: dùng chung shot ID / entity ID với skill ảnh, map keyframe_role sang input mode video.
- Bổ sung nội dung thực thi cho module 13, 15, 16, 21, 23, 24, 25, 26, 28, 29 (feasibility, lifecycle/causality, router, timeline, camera, performance, dialogue/lip-sync, audio, transition/extend, lighting/material).
- Thêm template `video_setup_plan_template.md`; nâng `video_generation_prompt_template.md` theo block Seedance 2.5.
- Mở rộng `tests/seedance_2_5_benchmark.md`; thêm `tests/video_scene_director_brain_benchmark.md`.
- Giữ nguyên toàn bộ luật V6: Design/Runtime split, Example Quarantine, Audience Firewall, hard gates.

## 6.0.0
- Tách Design World và Runtime World.
- Thêm Example Quarantine Law và distillation pipeline.
- Thêm Audience Firewall, provenance stripping, anti-anchoring.
- Thêm MASTER_PROMPT_IR.
- Thêm runtime purity compiler/linter và contamination gates.
- Đổi Master System output policy: runtime artifact first, design report optional.
- Nâng evaluator và regression suite.
- Giữ và nâng các luật state/reference/camera/audio của V5.
