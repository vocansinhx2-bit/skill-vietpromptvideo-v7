# 01 — INTENT, SCOPE & AUDIENCE ROUTER
Extract: requested artifact, target reader/model, modality, duration/aspect if supplied, references, hard constraints, success evidence, output language.
Classify intent and `TARGET_READER` separately.
Ask only when different answers materially change architecture; infer safe defaults otherwise.
Never assume a Master Prompt is a human-facing report.
