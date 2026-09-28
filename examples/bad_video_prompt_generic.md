# BAD — VIDEO PROMPT (GENERIC ADJECTIVE BLOAT) — DO NOT COPY
> Tầng Design. Minh họa lỗi, không dùng làm khuôn.

## Prompt lỗi
```text
An epic, stunning, emotional cinematic masterpiece in 8k. A sad old woman feels very emotional as she remembers her past and finally finds peace. Beautiful lighting, amazing atmosphere, dramatic camera movements, slow motion, the camera flies around her, emotional music swells, she cries and smiles and reads a letter and looks outside and stands up and walks to the door.
```

## Mã lỗi
| Mã | Chỗ lỗi |
|---|---|
| GENERIC_ADJECTIVE_BLOAT | "epic, stunning, masterpiece, 8k, beautiful, amazing" không điều khiển được gì |
| HOOK_WEAK | không có frame đầu kể tình huống |
| FLAT_CURVE / PEAK_MISPLACED | không có thời điểm đỉnh, mọi việc dồn một câu |
| SEGMENT_OVERLOADED | 6 hành động, không phân đoạn thời gian |
| EMOTION_STYLE_MISMATCH | "camera flies around" phá cảm xúc lặng |
| orientation_unlocked | không nói hướng thân, hướng nhìn |
| identity_lock_missing | không khóa trang phục/khuôn mặt |
| SOUND_FLAT | chỉ "emotional music swells" |
| Tên cảm xúc trừu tượng | "feels emotional", "remembers her past", "finds peace" không quan sát được |

## Sửa theo thứ tự
SIMPLIFY (còn 3 hành động) → SPLIT theo giây → chuyển cảm xúc thành ống kính/ánh sáng/âm → khóa hướng + danh tính → xóa tính từ khen. Kết quả: xem `good_video_prompt_drama.md`.
