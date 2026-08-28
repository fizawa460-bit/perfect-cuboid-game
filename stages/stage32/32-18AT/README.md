# Stage32-18AT — b16 heavy frontier tier-3 cost planner

18AS completed exact cost measurement for 502 of the 682 tier-1-heavy cut39 frontier states at a 32,768-node local probe budget. Exactly 180 frontier states remained capped. Combined with 18AR, 3,923 of the 4,103 frontier states now have exact lower-subtree costs.

18AT probes only those 180 unresolved frontier IDs with a 262,144-node local exact budget. It does not rerun the 3,923 resolved states and does not change the frozen p436/s5 x1024 ownership boundary. Frontier IDs remain an internal resumable queue, not a finer canonical partition.

Inputs are digest-locked compact artifacts from 18AR and 18AS plus the immutable exact Stage32 source artifact. The output records exact tier-3 costs for newly resolved states, retains any still-capped IDs as tier-4 monster candidates, and reports the next production/planner decision.

Operational preflight: one heavy runner only; compact input/output artifacts; no raw frontier dump is persisted beyond the small deterministic certifier output. The run therefore remains far below the Stage32 <=18 heavy-runner cap and does not depend on large spare Actions storage.

No b16 numerical wall credit, global aggregation credit, theorem credit, receiver credit, or perfect-cuboid claim is granted by this planner. Controller state is updated separately in the same PR/checkpoint and controller/docs edits do not arm this workflow.