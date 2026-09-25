# Stage32 MAIN startup

This is the ordinary Stage32 startup contract.

## Read order

For `stage32mainbatch`, read only:

1. repository-root `AGENTS.md`;
2. this file;
3. `stages/stage32/CURRENT.json`;
4. `stages/stage32/LIVE-ROADMAP.md`;
5. the `LIVE.json` of the selected unit;
6. only the detailed state/evidence explicitly named by that live pointer and needed for the current leaf.

Do **not** ordinarily preload `MAIN-STATE.json`, full `ROADMAP.md`, claim registries, lane registries, cross-lane demands, historical controllers, audit receipts, parked lanes, or Research OS policies. They are verification/detail authority and are opened only when the selected work actually requires them.

## Dispatch

`CURRENT.json` owns the compact current routing projection.

- 32-01 is complete and retained.
- 32-02 is primary.
- 32-03 is parallel.
- 32-04 waits for both.
- 32-05 is external hostile audit.

Default to 32-02. Use 32-03 when 32-02 is blocked or resumable 32-03 work is the better immediate path.

EX5, MB, and MB-FIB are internal execution surfaces, not operator entrypoints. 178, CUT, and BRIDGE are parked/reopen-only.

## Authority

Compact live files are routing aids, not proof certificates. If a mathematical claim, credit transition, source identity, historical receipt, or audit boundary becomes load-bearing, open the exact detailed authority named by the live pointer.

Never promote bounded/sample/timeout evidence into theorem, effectivity, receiver, endpoint, closure, or Perfect-Cuboid credit without the required audited boundary.

## Stop

Stop on the smallest precise residual/tool/theorem wall, at the 32-04 synthesis boundary, or before 32-05 external audit.

Do not merge without explicit user authorization.
