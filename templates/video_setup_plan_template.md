# VIDEO SETUP PLAN — TEMPLATE (module 46 + 49 + 50)

> Phần 1–7 là design-time (cho người dùng đọc, tiếng Việt). Chỉ phần 8 là prompt runtime gửi cho model video (English) và phải qua purity gate.

## 1. Scene DNA
| Trường | Giá trị | Giả định? |
|---|---|---|
| who | | |
| where | | |
| when | | |
| core_action | | |
| secondary_actions | | |
| emotion_arc | | |
| initial_state | | |
| end_state | | |
| dialogue | | |
| audio_intent | | |
| duration_target | | |
| delivery (platform / aspect) | | |

## 2. Archetype & thể loại
Archetype chính: `VA__` · Phụ: `VA__` · Thể loại (module 50): `G__` · Lý do (1 dòng):

## 3. Craft Plan (module 49)
| Trường | Giá trị |
|---|---|
| controlling_emotion | |
| hook_type (0–2s) | |
| first_frame_story (frame đầu kể được gì) | |
| curve (Rise / Fall / Rise–fall / Fall–rise / Flat–spike) | |
| peak_at (giây, 60–80%) | |
| plant → payoff | |
| signature_moment | |
| lens_per_segment | |
| composition_per_segment | |
| color_script | |
| sound_design (lặng / pre-lap / motif / off-screen) | |
| ending_type | |

## 4. Setup kỹ thuật
```
MODEL: Seedance 2.5 | 2.0
MODE: text-to-video | first-frame | first+last | reference | edit | extend
DURATION: __s   RESOLUTION: 480p | 720p | 1080p (nếu nhà cung cấp hỗ trợ)
ASPECT: __ (adaptive nếu first/last/edit/extend)
AUDIO: on | off     CLIPS: __ (chain: có/không → nếu có dùng sequence_plan_template)
```

## 5. Reference map
| Tag | File | Chỉ lấy | Không lấy |
|---|---|---|---|
| @Image1 | | | |

## 6. Timeline
| Segment | Thời gian | Motion owner | Hành động | Camera / ống kính | Thoại / audio | Ends with |
|---|---|---|---|---|---|---|

## 7. Rủi ro & chặn
| Rủi ro | Câu chặn trong prompt |
|---|---|

## 8. Prompt (runtime, English)
```text
[VISUAL RULE — one line: look, lens family, grain/halation, light logic]
[REFERENCE ROLES]
[ONE-SENTENCE SUMMARY]
[STARTING STATE]
[TIMELINE — continuous, non-overlapping segments, each with "Ends with:"]
[LIGHTING — direction, quality, contrast, color layers]
[AUDIO — ambience, <sfx>, (music) or "No background music."]
[CLOSING CONSTRAINTS — what holds through the whole clip]
```
