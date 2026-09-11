# Stage32 command-surface audit — 2026-09-11

Scope: ordinary Stage32 operator commands and startup/routing documents on `main`. This is an operational audit; it does not alter mathematical credit.

## Findings

1. **MAIN command spelling drift.** `MAIN-START-HERE.md` used both `Stage32-main-batch` and `stage32main batch`, while ordinary user operation uses `stage32mainbatch`.
2. **MAIN role ambiguity.** Existing text correctly prevented duplicate vertical attacks but could be read as making MAIN coordination-only. Historical operation and user intent require MAIN to keep doing mathematics when the current route is MAIN-owned, cross-lane, or unowned.
3. **178 startup routing drift.** `32-01-178/MISSION.json` remained ACTIVE but its integration surface and startup snapshot referenced PR #1753 / older N240-N280-era conditions. Stage32 MAIN has since advanced through audited N355 with N356 retained `AUDIT_REQUIRED`. The old mission snapshot is valid history but unsafe as current routing authority.
4. **EX5 post-merge drift.** `README.md`, `MAIN-START-HERE.md`, `MAINBATCH-OPERATIONS.md`, `CURRENT-ROADMAP.md`, `CURRENT-AUDIT-CONTRACT.md`, `MAIN-STATE.json`, and `verify_main_state.py` still encoded PR #1765 as an active merge-first checkpoint even though #1765 is merged at `98c5710dad4ca9a006e93b273ecf5259733e03aa`.
5. **Historical parallel lanes remain discoverable.** 178 `a..f` and EX5 `a..h` branches/history remain useful evidence but are not ordinary active dispatch surfaces. Without a canonical registry they are easy to mistake for live commands.

## Repair

- Added `stages/stage32/COMMANDS.md` as the canonical human-facing command registry.
- Canonicalized Stage32 MAIN to `stage32mainbatch`.
- Preserved MAIN as **controller + researcher**, with direct mathematics allowed for explicit MAIN-owned, cross-lane, or unowned work.
- Made 178 startup synchronize against current Stage32 `MAIN-STATE.json` before using its local mission DAG; Generation-1 lanes remain historical inputs only.
- Marked the old 178 startup snapshot as historical/non-routing while preserving its evidence.
- Advanced EX5 ordinary startup from the merged #1765 merge-first state to a post-merge BC2-25-preflight-ready state; no new mathematical credit is granted.
- Made `stage32ex5-audit` fail conceptually closed until a new exact retained checkpoint exists.
- Added `stages/stage32/verify_command_surface.py` and updated `stages/stage32-ex5/verify_main_state.py` to guard the repaired command surface and post-merge EX5 state.

## Canonical ordinary commands after repair

- `stage32mainbatch`
- `stage32audit`
- `stage32-01-178-mainbatch`
- `stage32-01-178-audit`
- `stage32ex5-mainbatch`
- `stage32ex5-audit`

No `-a/-b/...` child command is ordinary-active.

## Research / coordination decision

Do **not** split Stage32 MAIN into separate generic `coordinator` and `researcher` commands. That would add another ownership boundary and increase handoff/state drift. Instead:

- MAIN coordinates and researches when the obligation is MAIN-owned/cross-lane/unowned;
- 178 owns sustained FULL178 census research;
- EX5 owns sustained Picard64/node-support producer research;
- MAIN integrates specialist results and may take over only through explicit current routing.

This keeps one controller without turning it into a passive dispatcher.
