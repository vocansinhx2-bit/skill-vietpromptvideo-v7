# Prompt Architect V7

V7 giữ nguyên compiler hai tầng của V6 (**Design-Time Evidence** và **Runtime Artifact**) và thêm một "bộ não đạo diễn" cho video: nhận một ý tưởng cảnh quay bất kỳ, tự quyết định cách setup (input mode, reference, timeline, thoại, audio) trước khi viết prompt Seedance 2.5.

## Điểm mới trong V7
- Profile Seedance 2.5 đầy đủ, có mức tin cậy cho từng thông số (xem `model_profiles/seedance_2_5.md`).
- Module 46 Video Scene Director Brain: Scene DNA, 20 archetype cảnh, cây quyết định input mode, Video Setup Plan.
- Module 47 Image Skill Bridge: nối với skill ảnh `ai-video-reference-image-os` qua shot ID / entity ID chung.
- Các module camera, performance, dialogue/lip-sync, audio, transition, lighting, lifecycle được viết lại thành luật thực thi.
- Template Video Setup Plan + benchmark cho bộ não video.

## Điểm mới trong V7.1 — chặn lỗi runtime
- Module 22 orientation ledger: vị trí khung, hướng thân, hướng mặt, eyeline, hướng di chuyển cho từng nhân vật × từng segment; luật xoay người, reference lật gương, handoff hướng khi nối clip.
- Module 42 bảng lỗi Seedance: triệu chứng → nguyên nhân gốc → thứ tự sửa → biến duy nhất cần đổi.
- Module 48 Body/Hands/Group Integrity: tay thừa, đạo cụ nhân đôi, nhóm người, đi bộ, thao tác vật có nhân quả.
- Module 14, 17, 18, 19, 27 bổ sung ngưỡng độ phức tạp, character lock, chống leakage reference, state ledger.

## Điểm mới trong V7.2 — video hay hơn + cấu hình skill
- Module 49 Cinematic Craft Engine: 8 loại hook 2 giây đầu, đường cong cảm xúc, cài cắm → trả, bảng cảm xúc → ống kính/bố cục/ánh sáng/màu/nhịp/âm, chống vẻ "nhựa", Craft Plan.
- Module 50 Genre Playbooks: 12 thể loại (drama, action, horror, comedy, quảng cáo, UGC, romance, epic, noir, tài liệu, MV, explainer).
- Module 51 Sequence / Film Planner: phim nhiều clip, coverage, thứ tự generate, continuity bible, kiểu nối.
- Module 20 và 12 viết lại; evaluator 38 có nhóm điểm thẩm mỹ, vẫn giữ hard gate.
- SKILL.md có `description` chuẩn Claude Skills, bảng nạp module theo task/thể loại, bảng mặc định và luật khi nào hỏi user; thêm mode `PLAN_SEQUENCE_FILM`.
- Template Craft Plan + Sequence Plan; 4 prompt mẫu tốt/xấu (Design only); benchmark craft và sequence.

## Điểm mới trong V7.3 — hành động và hoạt hình
- Module 52 Action Choreography: pha đánh/rượt đuổi thành chuỗi exchange có khoảng cách, đường đi, điểm chạm, phản ứng, tư thế kết thúc; ngân sách exchange theo thời lượng; một đường camera; chia nhiều clip.
- Module 53 Animation Style: 7 họ phong cách, 12 nguyên lý hoạt hình thành câu prompt, style lock + loại trừ, grammar riêng cho 2D/anime, chống trôi về ảnh thật.
- Playbook G13 Animation, G02 Action viết lại; bảng lỗi 42 thêm 5 lỗi hành động/hoạt hình.

## Điểm mới trong V7.4 — hiệu ứng bám nhân vật không mất
- Module 54 VFX & Effect Persistence: Effect Contract (nguồn, bám ở đâu, look, lifecycle có mốc giây, endpoint, residue), effect ledger theo segment, ba lớp neo (hiệu ứng + ánh sáng hắt + residue), luật camera khi hiệu ứng active, nối clip giữ hiệu ứng, hiệu ứng trong hoạt hình.
- Bảng lỗi 42 thêm 5 lỗi hiệu ứng (39–43); module 15/23/27/52/53 có tham chiếu chéo sang 54.

## Giữ từ V6
- Audience Firewall, Example Quarantine + Distillation, Master Prompt IR.
- Creator Commentary Stripper, Example Contamination Detector, Runtime Instruction Compiler.
- Purity Linter + hard gates, Evaluator 100 V2, regression benchmarks.

## Cách dùng
Đọc `SKILL.md`. Skill tự route theo task. Với video: ý tưởng cảnh → module 46 lập Video Setup Plan → compile prompt theo profile model. Với Master Prompt: artifact cuối mặc định là bản executable sạch; báo cáo thiết kế chỉ xuất khi được yêu cầu.
