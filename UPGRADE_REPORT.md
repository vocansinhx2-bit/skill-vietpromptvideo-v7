# V7.3 -> V7.4 UPGRADE REPORT

## Root problem fixed
V7.3 dàn dựng được đòn đánh nhưng hiệu ứng (chưởng, năng lượng, lửa, điện) chỉ được viết như một sự kiện. Khi camera rời vùng chạm rồi quay lại, model vẽ lại vùng đó từ prompt và hiệu ứng biến mất hoặc đổi dạng.

## New / upgraded layers
- 54_VFX_EFFECT_PERSISTENCE_ENGINE.
- 42 thêm lỗi 39–43; 15, 27, 23, 52, 53 tham chiếu chéo sang 54.
- Benchmark mới: vfx_effect_persistence_benchmark; runtime_failure_benchmark thêm case hiệu ứng.
- Mọi benchmark (trừ master_prompt_purity_benchmark) gộp vào `tests/BENCHMARK_SUITE.md`; tên benchmark cũ tra theo mục `## [tên]`.

## Non-regression
Giữ nguyên Two-World, Example Quarantine, Audience Firewall, Master Prompt Hard Gates và toàn bộ gate của 7.1–7.3.

---

# V7.1 -> V7.2 UPGRADE REPORT

## Root problem fixed
V7.1 chặn được lỗi kỹ thuật nhưng chưa có tầng craft để video "hay": không có hook, đường cong cảm xúc, ngôn ngữ ống kính theo cảm xúc, playbook thể loại, hay kế hoạch phim nhiều clip. Frontmatter thiếu `description` nên AI khó tự kích hoạt skill; chưa có bảng nạp module và giá trị mặc định.

## New / upgraded layers
- 49_CINEMATIC_CRAFT_ENGINE, 50_GENRE_PLAYBOOKS, 51_SEQUENCE_FILM_PLANNER.
- 20 và 12 viết lại; 38 thêm nhóm điểm thẩm mỹ.
- SKILL.md: `description`, `name` bỏ hậu tố -v6, 4.1 Module Loading Map, 4.2 Defaults & When To Ask, bước A3/A4, mode PLAN_SEQUENCE_FILM.
- Template Craft Plan + sequence_plan_template; examples video tốt/xấu; benchmark craft + sequence.

## Non-regression
Giữ nguyên Two-World, Example Quarantine, Audience Firewall, Master Prompt Hard Gates và các video gate của 7.1.

---

# V7.2 -> V7.3 UPGRADE REPORT

## Root problem fixed
V7.2 có craft chung nhưng hành động chỉ ở mức playbook 10 dòng và chưa có kiến thức hoạt hình: pha đánh dễ ra đòn không chạm, hai người nhập nhau, camera chồng chuyển động; video hoạt hình dễ trôi về ảnh thật hoặc mặt 3D chung chung.

## New / upgraded layers
- 52_ACTION_CHOREOGRAPHY_ENGINE, 53_ANIMATION_STYLE_ENGINE.
- G02 viết lại, G13 mới; 42 thêm lỗi 34–38.
- Benchmark mới: action_choreography_benchmark, animation_style_benchmark.

## Non-regression
Giữ nguyên Two-World, Example Quarantine, Audience Firewall, Master Prompt Hard Gates và toàn bộ gate của 7.1/7.2.

---

# V7.0 -> V7.1 UPGRADE REPORT

## Root problem fixed
V7.0 gọi được tên lỗi runtime (spatial flip, identity drift, tay thừa, đạo cụ teleport) nhưng chưa có luật chặn cụ thể và chưa có đường sửa khi video đã lỗi.

## New / upgraded layers
- 22 orientation ledger + luật xoay người + mirror handling.
- 42 bảng triệu chứng → nguyên nhân → sửa, một biến mỗi lần regenerate.
- 48 BODY_HANDS_GROUP_INTEGRITY.
- 14, 17, 18, 19, 27 mở rộng thành luật thực thi.
- Benchmark mới: spatial_orientation_benchmark; runtime_failure_benchmark mở rộng.

---

# V6 -> V7 UPGRADE REPORT

## Root problem fixed
V6 có kiến trúc purity tốt nhưng thiếu "não đạo diễn" để biến một ý tưởng cảnh quay bất kỳ thành setup video, và các module camera/performance/dialogue/audio/transition/lighting chỉ có 2-4 dòng. Profile Seedance 2.5 chưa có thông số thật.

## New / upgraded layers
- 46_VIDEO_SCENE_DIRECTOR_BRAIN: Scene DNA, archetype VA01-VA20, cây quyết định input mode, luật timeline, Video Setup Plan, mã lỗi.
- 47_IMAGE_SKILL_BRIDGE: dùng chung shot ID / entity ID / keyframe role với skill ảnh.
- Profile Seedance 2.5 + 2.0 có thông số API và mức tin cậy.
- Module 13, 15, 16, 21, 23, 24, 25, 26, 28, 29 được viết lại thành bảng luật vận hành.
- Template video_setup_plan + video prompt template theo khối Seedance 2.5.
- Benchmark mới cho Seedance 2.5 và bộ não video.

## Non-regression
Giữ nguyên toàn bộ luật V6: Two-World, Example Quarantine, Audience Firewall, Master Prompt Hard Gates.

---

# V5 -> V6 UPGRADE REPORT

## Root problem fixed
V5 có output compiler tốt cho video nhưng đường build Master System chưa tạo compile boundary đủ mạnh giữa tài liệu thiết kế và executable Master Prompt. V6 biến boundary này thành kiến trúc bắt buộc.

## New control layers
- Audience Router
- Evidence/Runtime Classifier
- Example Distillation Engine
- Anti-Anchoring Generalization
- MASTER_PROMPT_IR
- Audience Firewall
- Creator Commentary Stripper
- Example Contamination Detector
- Runtime Instruction Compiler
- Master Prompt Purity Linter
- Purity-aware 100-point Evaluator
- Dedicated contamination/regression benchmarks

## Behavior change
Old risk:
`examples + research + failure notes -> authoring -> Master Prompt with explanatory residue`

V6:
`evidence -> quarantine -> distill -> IR -> runtime compile boundary -> purity gates -> executable Master Prompt`

## Non-regression
Video state, reference authority, timeline, spatial ledger, camera, performance, audio, continuity, compliance, compression and model-profile routing remain first-class modules.
