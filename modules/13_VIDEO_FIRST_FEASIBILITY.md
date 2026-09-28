# 13 — VIDEO-FIRST FEASIBILITY
Validate whether requested action is visually observable, physically understandable and achievable within model/duration/reference limits.
Prefer fewer hero transformations with clear causal bridges over dense event lists.
If infeasible, redesign before wording.

## 13.1 Feasibility gates (run in order)
| Gate | Question | FAIL action |
|---|---|---|
| OBSERVABLE | Can every beat be seen or heard on screen, without inner thought or off-screen knowledge? | Rewrite as body detail, object change or sound |
| DURATION | Does the beat count fit the clip length (about one main beat per 8–10s on 2.5, one per 4–5s on 2.0)? | SPLIT into more clips |
| TRANSFORMATION | Are there at most 1–2 hero transformations per clip? | Keep the hero, move others to other clips |
| CAUSALITY | Does each change have a visible cause written before its effect? | Add the cause beat or drop the effect |
| REFERENCE | Do identities, props and places that must stay exact have a reference asset? | Add reference or relax the invariant |
| MODE | Does the input mode support the task (first+last, first-only, reference, edit, extend)? | Route through 46.6 decision tree |
| AUDIO | Is there at most one speaker per shot and one language per line? | Split shots or reassign lines |
| MOTION ENERGY | Is peak motion slow and continuous enough to render cleanly? | Reduce speed, add transition micro-actions, replace explosion with aftermath |

## 13.2 High-risk content (simplify before writing)
- Crowds with individual choreography: keep crowd as texture, give action to one foreground subject.
- Hands manipulating small objects: one grip, one motion, closed hand position at end.
- Text, logos, numbers on screen: avoid or supply as reference; state "No subtitles" when none are wanted.
- Fast fights, sports impacts, vehicle crashes: cut to anticipation plus aftermath, or split into slow sequential beats.
- Fluids, smoke, cloth, hair in wind: always state where the material ends up.
- Multi-character dialogue in one shot: split into one speaker per shot.
- Large scale changes (growth, transformation, morphing): one continuous change with named start and end states.

## 13.3 Output
Feasibility verdict: `FEASIBLE`, `FEASIBLE_AFTER_SPLIT`, `FEASIBLE_AFTER_REDESIGN`, `INFEASIBLE_NEEDS_USER_DECISION`, with the list of changes applied.
