# BAD — VIDEO PROMPT (OVERPACKED ACTION CLIP) — DO NOT COPY
> Tầng Design. Minh họa lỗi quá tải và mất hướng.

## Prompt lỗi
```text
10 seconds. A cop chases a thief through a crowded market, across rooftops, into a subway, they fight on the train, the thief jumps out, the cop follows on a motorcycle, explosion behind them, the camera spins 360 degrees around both of them, then they shake hands and become friends, with lots of people watching and cheering.
```

## Mã lỗi
| Mã | Chỗ lỗi |
|---|---|
| CLIP_OVERPACKED | 4 địa điểm trong 10s |
| SEGMENT_OVERLOADED | hơn 8 hành động không phân giây |
| orientation_unlocked / screen_geography_flip | không khóa ai chạy trái→phải; xoay 360° phá trục |
| hand_ownership_missing | cảnh đánh nhau không nói tay nào làm gì |
| COVERAGE_MONOTONY | không có kế hoạch cỡ cảnh |
| PAYOFF_UNPLANTED | "become friends" không có cài cắm |
| crowd không khóa số người | "lots of people" dễ sinh người biến dạng |

## Sửa theo thứ tự
SPLIT thành Sequence Plan (module 51): 4 clip, mỗi clip một địa điểm → khóa hướng đuổi (cả hai chạy trái→phải của khung) và handoff hướng ở mỗi điểm nối → mỗi clip ≤3 hành động có `Ends with:` → bỏ xoay 360° → đẩy "thành bạn" sang clip cuối và cài lý do ở clip 1 → khóa đám đông thành "a few distant bystanders, out of focus".
