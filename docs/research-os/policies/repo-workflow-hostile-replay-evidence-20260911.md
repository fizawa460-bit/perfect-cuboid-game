# Repository workflow hostile-replay evidence — 2026-09-11

Purpose: freeze exact-head sibling replay evidence for PR #1769 after hostile re-audit found that the previous PR prose incorrectly reported zero total runs on #1765 and #1766.

Lifecycle interpretation follows `pr-workflow-trigger-lifecycle.md`: only automatic execution by workflows classified `MANUAL` or `RETIRED` is prohibited. Current `ACTIVE_AUTO` workflows, including cross-Stage current-frontier and repository safety/authority workflows, may fire on long-lived sibling PRs when their trigger/path conditions match. Therefore replay evidence reports both total runs and historical/manual fan-out.

## #1753 Stage32 MAIN

Exact cleanup head: `d80cc9fb2bede1cf7efdeef30f33c61552368335`

Total PR-triggered runs: 4.

- `34538392833` — Stage32 MAIN startup authority — success
- `34538392846` — Stage32 claim frontier integrity — failure
- `34538392803` — Stage32 stale-run sweeper — success
- `34538392812` — [Stage32][32-01-178][N356] optimistic exceptional transport cap — success

`MANUAL` / `RETIRED` automatic runs: 0.
Historical fan-out: 0.

## #1752 Stage36 MAIN

Exact cleanup head: `ca3646e5a7073b6a750a5a5470392672f189c6fc`

Total PR-triggered runs: 1.

- `34537913427` — Stage36 authority audit — failure

`MANUAL` / `RETIRED` automatic runs: 0.
Historical fan-out: 0.

## #1765 Stage32EX5

Exact cleanup head: `cc549b247c1229668604a36f2e4a61966a4cf265`

Total PR-triggered runs: 6.

- `34538687116` — Stage32 stale-run sweeper — success
- `34538686920` — Stage32 MAIN startup authority — success
- `34538687005` — Stage32EX5 BC2-24 explicit fibre-degree partition — success
- `34538686941` — Stage32EX5 main integrity — failure
- `34538687083` — Stage32 claim frontier integrity — failure
- `34538686993` — [Stage32][32-01-178][N356] optimistic exceptional transport cap — failure

`MANUAL` / `RETIRED` automatic runs: 0.
Historical fan-out: 0.

BC2-24 remains independently protected by its heavy-run authorization gate; workflow trigger eligibility is not compute authorization.

## #1766 Stage35EX

Exact cleanup head: `abe842fdfb300cebaf993d4e62233da74a130902`

Total PR-triggered runs: 8.

- `34538754264` — Stage32 MAIN startup authority — failure
- `34538754506` — Stage35-EX Goal4CF selected discriminant height — success
- `34538754171` — Stage36 authority audit — failure
- `34538754199` — Stage32 claim frontier integrity — failure
- `34538754471` — Stage32 stale-run sweeper — success
- `34538754289` — Stage32EX5 main integrity — failure
- `34538754207` — Stage35 and Stage35-EX aggregate audit — failure
- `34538754343` — [Stage32][32-01-178][N356] optimistic exceptional transport cap — failure

`MANUAL` / `RETIRED` automatic runs: 0.
Historical fan-out: 0.

## Result

The earlier zero-total-run claims for #1765 and #1766 were incorrect and are superseded by this evidence. The repository-wide lifecycle migration result remains: the audited sibling heads show zero automatic runs from `MANUAL` or `RETIRED` workflow classes. Cross-Stage `ACTIVE_AUTO` execution is intentional under the current policy and is not counted as historical fan-out.

Workflow job success/failure is an authority/execution result separate from this lifecycle classification. This evidence grants no mathematical credit and no merge authorization.
