# Stage32EX5 retired command/startup surface — 2026-09-14

This directory preserves Stage32EX5 command/startup prose and coordination snapshots removed from the live stage root during startup-surface collapse.

Historical/reference only. Ordinary `stage32ex5-mainbatch` and current `stage32ex5-audit` must not treat these files as live authority.

Live ordinary mainbatch startup authority is:

1. repository `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. current `stages/stage32/MAIN-STATE.json`;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. `stages/stage32-ex5/MAIN-STATE.json`;
6. only `current_leaf_working_set` from that state.

Current audit behavior is governed by repository `AGENTS.md` hostile-audit triggers/policy, `stages/stage32/COMMANDS.md`, and the exact current `stages/stage32-ex5/MAIN-STATE.json` boundary. The archived `AUDIT-CONTRACT.md` is the old Cycle1 route-decision/bounded-exhaustion contract and is not current BC2 audit authority.

Retired files:
- `README.md`
- `MAIN-START-HERE.md`
- `MAINBATCH-OPERATIONS.md`
- `CROSS-LANE-STATE.json`
- `CURRENT-ROADMAP.md`
- `CURRENT-AUDIT-CONTRACT.md`
- `AUDIT-CONTRACT.md` (Cycle1 audit contract)

They were removed from the stage root because their responsibilities overlapped and they represented different EX5 generations. Git history remains exact provenance for the original paths.

No mathematical authority, audit credit, Stage32 MAIN credit, runkey authorization, or merge authorization is changed by this organizational move.
