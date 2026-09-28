# MIGRATION V6 -> V7

## Không phá vỡ
- Mọi luật, hard gate, module 01-45 và schema của V6 giữ nguyên tên và vai trò.
- `validate_package.py` và `purity_lint.py` không đổi.

## Thay đổi đóng gói (7.4)
- 12 file benchmark trong `tests/` gộp thành `tests/BENCHMARK_SUITE.md`, mỗi file cũ là một mục `## [tên_file_cũ]`. Nội dung giữ nguyên.
- `tests/master_prompt_purity_benchmark.md` giữ riêng (validate cần file này).
- Tên file benchmark nhắc ở các mục bên dưới giờ là tên mục trong `BENCHMARK_SUITE.md`.
- Thêm `modules/54_VFX_EFFECT_PERSISTENCE_ENGINE.md` — bật khi có hiệu ứng bám nhân vật/vật.

## Thêm mới
- `modules/46_VIDEO_SCENE_DIRECTOR_BRAIN.md` — chạy trước compile khi task là video từ ý tưởng cảnh.
- `modules/47_IMAGE_SKILL_BRIDGE.md` — dùng khi đầu vào đến từ skill ảnh.
- `templates/video_setup_plan_template.md`.
- `tests/video_scene_director_brain_benchmark.md`.
- `modules/48_BODY_HANDS_GROUP_INTEGRITY.md` — tay/chân/nhóm người, chống tay thừa, đạo cụ nhân đôi, nhân vật nhập nhau.
- `tests/spatial_orientation_benchmark.md`.

## Thay đổi (7.2)
- `name` trong SKILL.md và manifest đổi thành `prompt-architect-video-generation-compiler` (bỏ `-v6`). Nếu nơi khác gọi skill bằng tên cũ, cập nhật lại.
- Thêm `description` vào frontmatter.
- Thêm module 49, 50, 51; `templates/sequence_plan_template.md`; `tests/cinematic_craft_benchmark.md`, `tests/sequence_planner_benchmark.md`; 4 file `examples/*video_prompt*`.
- Module 12, 20, 38 viết lại; `templates/video_setup_plan_template.md` thêm Craft Plan.

## Thêm mới (7.3)
- `modules/52_ACTION_CHOREOGRAPHY_ENGINE.md` — bật khi có va chạm thân thể, đánh nhau, rượt đuổi, stunt.
- `modules/53_ANIMATION_STYLE_ENGINE.md` — bật khi brief là hoạt hình / anime / cartoon / 3D stylized / stop-motion.
- `tests/action_choreography_benchmark.md`, `tests/animation_style_benchmark.md`.
- Module 50 có G13; module 42 có lỗi 34–38.

## Thay đổi nội dung (7.1)
- Module 22 viết lại thành Orientation Ledger (frame side, body facing, head facing, eyeline, travel direction), luật xoay người, lật gương, hướng vào/ra khung khi nối clip.
- Module 42 thành bảng triệu chứng → nguyên nhân → cách sửa → một biến cần đổi.
- Module 14, 17, 18, 19, 27 mở rộng thành luật thực thi có ngưỡng.
- `tests/runtime_failure_benchmark.md` mở rộng theo bảng lỗi mới.

## Thay đổi nội dung
- `model_profiles/seedance_2_5.md`, `seedance_2_0.md` viết lại theo tài liệu API.
- Module 13, 15, 16, 21, 23, 24, 25, 26, 28, 29 mở rộng từ vài dòng thành luật thực thi.
- `templates/video_generation_prompt_template.md` theo block FORMAT / REFERENCE ROLES / STARTING STATE / TIMELINE / CAMERA / CONTINUITY / AUDIO / ENDING STATE / CONSTRAINTS.

## Cần kiểm tra lại khi nhà cung cấp cập nhật
- Độ phân giải tối đa (480p/720p chính thức; 1080p chỉ ở một số provider).
- Giới hạn reference và ký tự prompt theo từng provider.
