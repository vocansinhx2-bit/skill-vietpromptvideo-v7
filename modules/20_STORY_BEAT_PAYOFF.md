# 20 — STORY BEAT & PAYOFF ENGINE
Build a causal arc, not a checklist. Every beat must change something the viewer can see or hear.

## 20.1 Beat chain
Generic chain: hook -> setup -> trigger -> progression/escalation -> turn -> payoff -> optional aftermath.
Use only beats that add function. A 4–6s clip usually needs hook + one change + payoff. A 15s clip usually needs hook + setup + escalation + turn + payoff.

## 20.2 Beat budget by duration
| Duration | Beats | Rule |
|---|---|---|
| 4–6s | 2–3 | one action, one visible result |
| 7–10s | 3–4 | one trigger, one escalation, one payoff |
| 11–15s | 4–5 | one turn allowed; max 1 plant→payoff pair |
| 16–30s | 5–7 | max 2 plant→payoff pairs; peak at 60–80% of runtime |

## 20.3 Causality test
Each beat must pass "because / therefore", never "and then".
- Beat N+1 happens because of beat N, or beat N+1 is a consequence the viewer expects.
- If two beats can swap order without changing meaning, merge or delete one.

## 20.4 Payoff types
| Type | Visible form |
|---|---|
| Reveal | hidden object, face, place or result becomes visible |
| Reversal | expected outcome flips |
| Release | tension ends: exhale, laugh, collapse, silence |
| Transformation | before-state becomes after-state on screen |
| Callback | a planted object, sound or gesture returns with new meaning |
| Escalation cap | action reaches its largest scale, then stops |

## 20.5 Plant → payoff
- Plant must be on screen or audible before the payoff, at least one beat earlier.
- Plant must be specific: a named object, sound or gesture, not a mood.
- Payoff must reuse the same object, sound or gesture.
- Unplanted payoff -> error `PAYOFF_UNPLANTED` (module 49).

## 20.6 Endings
Choose one: hard cut on peak / held aftermath 1–2s / loop-back to first frame / reaction shot / quiet button (small gesture after the peak).
Short-form ads default to hard cut or held product frame. Drama defaults to held aftermath.

## 20.7 Link to craft
Map beats onto the emotional curve in module 49.3 and the hook table in 49.2. Beats set what happens; module 49 sets how it feels.

## 20.8 Error codes
| Code | Signal |
|---|---|
| `BEAT_AND_THEN` | beats are sequential but not causal |
| `BEAT_OVERPACKED` | more beats than the duration budget |
| `PAYOFF_INVISIBLE` | payoff is stated as meaning, not shown |
| `ENDING_UNDEFINED` | clip ends mid-action with no ending type |
