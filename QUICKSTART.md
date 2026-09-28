# QUICKSTART — V7

## Khi nhận ý tưởng cảnh quay để làm video
1. Đọc `SKILL.md`, route `BUILD_VIDEO_PROMPT`.
2. Chạy `modules/46_VIDEO_SCENE_DIRECTOR_BRAIN.md`: điền Scene DNA, chọn archetype, chọn input mode.
3. Nếu có output từ skill ảnh: map qua `modules/47_IMAGE_SKILL_BRIDGE.md`.
3b. Điền Craft Plan bằng `modules/49_CINEMATIC_CRAFT_ENGINE.md` + một playbook trong `modules/50_GENRE_PLAYBOOKS.md`.
3c. Nếu ý tưởng >30s hoặc nhiều cảnh: lập Sequence Plan (`modules/51_SEQUENCE_FILM_PLANNER.md`) trước, rồi làm từng clip.
4. Xuất Video Setup Plan (`templates/video_setup_plan_template.md`) khi user cần biết cách chuẩn bị asset.
5. Đọc `16_MODEL_PROFILE_ROUTER` → `model_profiles/seedance_2_5.md` (hoặc 2.0).
6. Compile prompt theo `templates/video_generation_prompt_template.md`.
7. Kiểm tra: ≤2000 ký tự, timeline liên tục, mỗi reference một vai, một người nói mỗi shot.

## Khi build Master Prompt mới
1. Đọc `SKILL.md`.
2. Xác định `TARGET_READER=RUNTIME_AI`.
3. Quarantine examples/research/failure history.
4. Distill examples bằng module 03-04.
5. Build `MASTER_PROMPT_IR`.
6. Compile qua module 32-35.
7. Chạy purity linter 36-39.
8. Xuất **MASTER PROMPT** trước; design notes chỉ khi user yêu cầu.

## Khi audit Master Prompt cũ
Tìm 4 nhóm lỗi trước:
- creator commentary;
- training-example contamination;
- provenance/history leakage;
- non-operational documentation bloat.
Sau đó mới audit state/reference/camera/model fit.

## Heuristic local check
`python tools/purity_lint.py your_master_prompt.md`
`python tools/validate_package.py`
Đây chỉ là preflight; semantic purity vẫn phải qua module 37 + benchmark tests.
