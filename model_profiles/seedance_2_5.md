# MODEL PROFILE — SEEDANCE 2.5 (ByteDance Seed)

> Design-time profile. Numbers below control compile decisions; do not paste them into the video prompt.
> Confidence: `verified` = API schema / provider docs; `reported` = consistent secondary guides; `conflict` = sources disagree, use the safe value.
> Research date: 2026-09. Released 2026-07-31; public API via providers from ~2026-08-07. Re-check provider schema before locking a job.

## 1. Hard specs

| Field | Value | Confidence |
|---|---|---|
| Model id (Volcengine/BytePlus) | `doubao-seedance-2-5-260628` | reported |
| Duration | 4–30 s, whole seconds; `-1` / auto = model chooses | verified |
| Resolution | 480p, 720p (default). 1080p only on some providers (H.265). No 4K | conflict → default 720p |
| FPS | 24 fixed | verified |
| Aspect ratio | `16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptive` (default adaptive) | verified |
| Aspect in frame/edit/extend modes | forced `adaptive` (follows first-frame image / source video); concrete ratio → `InvalidParameter` | verified |
| Output | mp4 (default), mov (H.264 yuv444p + PCM) | verified |
| Audio | `generate_audio` default true; native lip-synced dialogue from quoted lines | verified |
| Prompt length | provider cap exists (Cloudflare: 2000 chars). Official samples are long; fit the provider cap | conflict → compile ≤ provider cap |
| `camera_fixed`, `frames` | not supported (Seedance 1.x params) — write camera lock in prose | verified |
| `seed` | supported | verified |
| `return_last_frame` | supported — use for chaining | reported |

## 2. Reference limits (multimodal reference mode)

| Asset | Max | Extra rule | Confidence |
|---|---|---|---|
| Images | 30 (each ≤ 4K) | recommended 1–8 subjects; more assets = lower stability | verified / reported |
| Videos | 10 | each 1.8–30.2 s; total ≤ ~30 s | verified |
| Audio | 10 | each 1.8–30.2 s; total ≤ ~30 s; audio may be the only reference | verified |
| Total files | 50 | some front-ends expose only a subset (9 img + 3 vid) | verified |

## 3. Input modes — mutually exclusive

| Mode | Inputs | Use when |
|---|---|---|
| `T2V` | prompt only | no locked look; exploration |
| `I2V_FIRST` | 1 image = exact first frame | shot must open on an approved keyframe |
| `I2V_FIRST_LAST` | first + last image (last requires first) | end state must be exact; aspect follows first image |
| `R2V_MULTIMODAL` | up to 30 img / 10 vid / 10 audio as references | identity/product/location/camera/motion/voice from assets |
| `EDIT` | source video + prompt (`omni_reference_task_type=edit`) | add/remove/replace inside an existing clip; duration ≈ source (±0.3 s), ratio kept |
| `EXTEND` | source video + prompt (`task_type=extend`) | continue a clip forward |

Never mix frame mode with reference mode in one call. If identity refs AND an exact first frame are both needed: bake identity into the keyframe first (image skill), then run `I2V_FIRST`.

## 4. Compiler behavior (2.5-specific)
- Second-level timestamps are responsive: use `0-4s:` blocks for multi-beat shots, music sync, 15–30 s one-takes. Blocks are continuous, non-overlapping, pacing budgets — not frame-exact cuts.
- Each block has one main change and a visible end state that the next block inherits.
- Empty or thin blocks make the model invent, stall, repeat or slow-mo. Too many events make it skip the middle or rush the ending.
- Every reference gets one narrow role + what NOT to take from it. Mapping lives in the prompt text, never burned into the image.
- Image refs carry look (identity, product, location); video refs carry motion/camera/timing; audio refs carry voice/music/rhythm. Do not give two assets the same job.
- When a video ref is precise enough, say "follow the camera motion of @Video1" and do not re-describe it.
- One dedicated lighting paragraph (direction + hard/soft + contrast + color base/secondary/accent) — biggest quality lever.
- Favor slow, continuous, decomposed motion; high-burst action (sprint, big jump, tumble) is the top collapse point — give energy to camera/edit instead, or split.
- Dialogue: one speaker per shot, quoted line with timestamp, speaker named, listener mouth closed.
- WHITE_MODEL / CLAY_PREVIS / grid storyboard refs = spatial/blocking authority, not style authority.

## 5. Recommended prompt order
`REFERENCE ROLES -> ONE-SENTENCE SUMMARY -> STARTING STATE -> TIMELINE (timestamped beats) -> CAMERA -> LIGHTING -> AUDIO/DIALOGUE -> CONTINUITY/HOLD-THROUGH -> ENDING STATE -> CONSTRAINTS`

Full rules: `modules/47_SEEDANCE_25_PROMPT_COMPILER.md`. Template: `templates/seedance_2_5_prompt_template.md`.

## 6. Sources (design-time only)
- Cloudflare AI docs — Seedance 2.5 schema: https://developers.cloudflare.com/ai/models/bytedance/seedance-2.5/
- APIYI — Seedance 2.0 / 2.5 overview: https://docs.apiyi.com/en/api-capabilities/seedance2/overview
- fal — Seedance 2.5 prompting guide: https://fal.ai/learn/devs/seedance-2-5-prompting-guide
- dev.to — Seedance 2.5 official manual (English): https://dev.to/super_lewis/the-seedance-25-prompting-guide-in-english-4hen
- SunoMV — Seedance 2.5 prompt guide: https://suno.bi/en/blog/seedance-2-5-prompt-guide
- Seedance.tv — lip sync issues: https://www.seedance.tv/blog/seedance-2-5-lip-sync-issues
- ImagineToVideo — release + live API notes: https://imaginetovideo.com/blog/seedance-2-5-official-release-and-integration-plan
