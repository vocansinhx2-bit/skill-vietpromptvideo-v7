# 16 — MODEL PROFILE ROUTER
Select model-specific behavior from `model_profiles/`.
Do not impose Seedance 2.5 timestamp/reference micro-control onto 2.0 by default.
If target model unknown, compile conservatively and avoid unsupported specificity claims.

## 16.1 Bảng route
| User nói | Profile |
|---|---|
| Seedance 2.5, SD 2.5, doubao-seedance-2-5 | `model_profiles/seedance_2_5.md` |
| Seedance 2.0 / 2.0 Fast / 2.0 Mini | `model_profiles/seedance_2_0.md` |
| "Seedance" không ghi phiên bản | Seedance 2.5, ghi giả định |
| Model khác / chưa rõ | Compile bảo thủ: pha tuần tự, không timestamp chính xác, không giả định last frame |

## 16.2 Kiểm tra trước khi compile
- Duration, resolution, aspect nằm trong giới hạn profile.
- Số reference nằm trong giới hạn profile.
- Không trộn first/last frame với reference mode trên model cấm trộn.
- Tham số sinh (resolution, duration, ratio, seed) đặt ở API/UI, không viết vào prompt.
- Thông số nhà cung cấp có thể khác nhau; khi user dùng nền tảng cụ thể, ưu tiên giới hạn của nền tảng đó.
