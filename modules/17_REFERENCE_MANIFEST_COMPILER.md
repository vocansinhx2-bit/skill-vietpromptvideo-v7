# 17 — REFERENCE MANIFEST COMPILER
For every reference define ID, TYPE, ENTITY, AUTHORITATIVE_FOR, NOT_AUTHORITATIVE_FOR, ACTIVE_SCOPE, conflict priority and leakage risk.
Do not allow a reference image to become universal authority by accident.

## 17.1 Đánh số và cú pháp
- @Image1, @Image2… / @Video1… / @Audio1… theo đúng thứ tự upload; mỗi loại đánh số riêng.
- Không ghi tên file, asset ID hay URL trong prompt.
- Không đổi thứ tự upload sau khi đã viết prompt; đổi thứ tự → viết lại toàn bộ tham chiếu.

## 17.2 Một reference = một việc
| TYPE | AUTHORITATIVE_FOR | Câu mẫu |
|---|---|---|
| IDENTITY_FACE | khuôn mặt, tuổi, tóc | "@Image1 is the canonical face of [A]." |
| IDENTITY_BODY | tỷ lệ cơ thể, trang phục đầy đủ | "@Image2 defines [A]'s full-body proportions and outfit." |
| ANGLE_SHEET | mặt nghiêng/sau lưng | "@Image3 shows [A] from the side and back." |
| PROP | hình dạng, màu, chất liệu vật | "@Image4 defines the [prop]." |
| ENVIRONMENT | không gian, bố cục, ánh sáng | "@Image5 defines the location layout and lighting." |
| STYLE | màu, grain, chất hình | "@Image6 sets the color grade only." |
| FIRST_FRAME / LAST_FRAME | trạng thái đầu/cuối chính xác | chế độ first/last, không trộn với reference mode |
| MOTION | quỹ đạo chuyển động, nhịp | "@Video1 is a motion reference for the gait only." |
| CAMERA | chuyển động máy | "@Video2 provides the camera path only." |
| VOICE / MUSIC | giọng, nhạc | "@Audio1 is [A]'s voice." |

## 17.3 Câu phủ định bắt buộc
Mỗi reference kèm ít nhất một câu "Do not copy X from @ImageN" cho thuộc tính dễ rò:
- Ảnh nhân vật → không copy phông nền, ánh sáng, tư thế.
- Video chuyển động → không copy diễn viên, quần áo, môi trường.
- Ảnh style → không copy nhân vật, bố cục.

## 17.4 Ngân sách
- Seedance 2.5: khuyến nghị 1–8 ảnh chủ thể; tối đa 30 ảnh, 10 video, 10 audio, 50 file. Seedance 2.0: 9 ảnh, 3 video, 3 audio.
- Ưu tiên 3–5 reference đồng nhất hơn nhiều reference trùng vai.
- Mỗi nhân vật chính: 1 ảnh mặt trung tính + 1 ảnh toàn thân; thêm ảnh nghiêng/sau lưng nếu có xoay người hoặc camera orbit.

## 17.5 Output manifest
```
@Image1 | IDENTITY_FACE | A | face, age, hair | background, lighting, pose | all segments | leak: background
```
