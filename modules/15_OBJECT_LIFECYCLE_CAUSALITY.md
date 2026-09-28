# 15 — OBJECT LIFECYCLE & CAUSALITY
Track object provenance, possession, location, transformation and disposal.
No teleporting props, duplicate held objects, unexplained reconstruction or state reset.
For important transformations require before -> contact/action -> visible change -> after.

## 15.1 Sổ vật thể
Mỗi vật quan trọng có: tên, số lượng, người/vị trí giữ ở đầu clip, thay đổi trong clip, người/vị trí giữ ở cuối clip.
Vật chỉ có một: ghi `there is exactly one [object] throughout`.

## 15.2 Ràng buộc chống lỗi hay gặp
- no duplicated [object], no object teleportation
- no identity change, clothing change, color change, duplication
- no floating objects, no duplicated limbs
Chỉ thêm ràng buộc cho vật thật sự có rủi ro; không dán danh sách chung vào mọi prompt.

## 15.3 Hiệu ứng là thực thể
Chưởng, lửa, điện, khói, băng, hào quang được ghi vào sổ như vật thể: nguồn, nơi bám, pha vòng đời, endpoint, residue. Chi tiết ở module 54.

## 15.4 Khi lỗi xảy ra
Viết lại trạng thái vật lý tại chỗ hành động hỏng bắt đầu và trạng thái nó phải kết thúc. Mỗi lần sinh lại chỉ đổi một điều.
