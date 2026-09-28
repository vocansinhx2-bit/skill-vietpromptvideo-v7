# MODEL PROFILE — SEEDANCE 2.0

> Design-time profile. Research date: 2026-09. Confidence tags as in `seedance_2_5.md`.

## 1. Hard specs

| Field | Value | Confidence |
|---|---|---|
| Model ids | `doubao-seedance-2-0-260128`, `-fast-260128`, `-mini-260615` | reported |
| Duration | 4–15 s (default 5; `-1` = auto) | verified |
| Resolution | 480p / 720p / 1080p — 1080p standard only; fast & mini cap at 720p (1080p → 400) | verified |
| Aspect | `16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptive` | verified |
| Output | mp4 only (H.264) | verified |
| References | 9 images + 3 videos + 3 audio (videos ≤ 15 s total, audio ≤ 15 s total); audio needs an image or video alongside | verified |
| Modes | first-frame / first+last / multimodal reference — mutually exclusive | verified |
| Edit / extend task types | not available (2.5 only) | verified |

## 2. Compiler behavior
- Strict second-level timestamps are unstable on 2.0 — use `Shot 1 / Shot 2 / Shot 3` phases and let the model pace; timestamps only as soft guidance.
- Few meaningful temporal phases; concise sequence grammar.
- Explicit image/video/audio reference roles (`@Image1`… by upload order).
- Protect identity, scene geometry, prop identity and causal action.
- Avoid simultaneous camera + action + dialogue overload.
- Do not port 2.5 micro-timestamp/30-reference habits onto 2.0.

Recommended order: reference map -> invariants -> opening state -> sequence (Shot N) -> camera -> audio -> continuity/final state.

## 3. When to prefer 2.0 over 2.5
- Need 1080p and the 2.5 provider only offers 720p.
- Short clip (≤ 15 s) with ≤ 9 image refs where 2.5 cost/latency is not justified.

Sources: https://docs.apiyi.com/en/api-capabilities/seedance2/overview · https://suno.bi/en/blog/seedance-2-5-prompt-guide · https://www.atlabs.ai/blog/seedance-2-prompts-guide
