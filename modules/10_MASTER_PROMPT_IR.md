# 10 — MASTER PROMPT IR
Source of truth for reusable Master Systems.
Recommended fields: role, runtime_objective, target_reader, inputs, invariants, variables, decision_points, routing, workflow, state_model, references, content_mechanisms, diversity_dimensions, failure_prevention, precedence, output_contract, runtime_self_check, exclusions, fallbacks, extension_points.
Separate `design_evidence` from `runtime_ir`; design_evidence MUST NOT compile into runtime unless promoted intentionally.
Omit empty branches.
