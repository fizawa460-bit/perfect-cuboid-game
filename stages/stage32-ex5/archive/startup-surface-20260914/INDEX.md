# Stage32EX5 retired startup surface — #1800 handoff / 2026-09-14

This directory preserves the exact Stage32EX5 startup/readme/roadmap/audit/coordination files removed from the live EX5 stage root during the #1800 integration cleanup.

Historical/reference only. Ordinary `stage32ex5-mainbatch` and `stage32ex5-audit` must not treat these archived files as live authority.

Live startup authority is:

1. repository `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. current `stages/stage32/MAIN-STATE.json`;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. EX5 entrypoint selected by `stages/stage32/proof/LANE-ADAPTERS.json`, which is `stages/stage32-ex5/MAIN-STATE.json`;
6. only the exact evidence selected by current routing/state.

The retained EX5 `MAIN-STATE.json` V5 bytes are intentionally not rewritten by this organizational handoff. Its old execution-path fields are merged-state provenance only; they do not override the live `LANE-ADAPTERS.json` startup entrypoint.

Retired from the live EX5 root:
- `README.md`
- `MAIN-START-HERE.md`
- `MAINBATCH-OPERATIONS.md`
- `CROSS-LANE-STATE.json`
- `CURRENT-ROADMAP.md`
- `CURRENT-AUDIT-CONTRACT.md`
- `AUDIT-CONTRACT.md` (Cycle1 source-locked audit contract)

Compatibility replay files:
- `verify_main_state_v5_pre_startup_collapse.py` is the exact pre-collapse V5 verifier. The live `verify_main_state.py` supplies the archived startup projection only transiently while replaying it.
- Cycle1 replay transiently restores archived `AUDIT-CONTRACT.md` for the unchanged source-locked Cycle1 verifier.
- Stage32 cross-lane replay transiently restores archived `CROSS-LANE-STATE.json` for the historical V23 verifier.
- The Stage32 command-surface guard transiently replays the exact pre-collapse command/startup contract, then restores the collapsed live surface.

No mathematical authority, pruning/receiver/theorem/effectivity/endpoint credit, EX5 retained result, Stage32 MAIN credit, runkey authorization, or merge authorization is changed by this move.
