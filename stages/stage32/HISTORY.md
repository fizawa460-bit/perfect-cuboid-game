# Stage32 history and reusable evidence index

Purpose: give MAIN a compact way to answer **what was already proved, what was superseded, and what can still be reused** without reconstructing Stage32 from old PRs, workflow logs, or the full controller history.

This file is an index, not an authority for live state. For the current machine state, use `stages/stage32/controller.json`.

## Generation map

| Unit | Role | Status | Reuse rule |
|---|---|---|---|
| 32-19 | brute-force scaling limit / hard-tail diagnosis | CLOSED_RETROSPECTIVE | Historical telemetry and scaling diagnosis remain valid; do not revive blind node-ceiling escalation as the default strategy. |
| 32-20 | symbolic prefix compression / exact indexed terminal family | CLOSED_CHECKPOINTED | Exact symbolic counts and rank/unrank interface remain reusable; the Gen38 52-unit frontier is historical, not the active enumeration mechanism. |
| 32-21 | numerical Picard / exact integer-fiber compression | ACTIVE | Reuse only audited/checkpointed interfaces listed below; preserve `UNKNOWN != UNSAT` and representative-sample firewalls. |

Authoritative generation map: `stages/stage32/ROADMAP-32-19-21-REANCHOR.md`.

## 32-19 — scaling-limit evidence

Reusable facts:

- Gen38: 73 inputs -> 52 continuations; hard tail remains substantial.
- Exact finite raw remaining-node upper bound: `4555530975806418`.
- Blind 512M/1B-style escalation was judged operationally dominated as the primary route.
- Historical Gen33-Gen38 evidence is not revoked; only its use as the active enumeration mechanism is superseded.

Primary history snapshot: `stages/stage32/controller-history-through-32-21ad.json`.

## 32-20 — symbolic replacement of brute-force enumeration

Reusable/current interface:

- `PASS_PREFIX_DFS_REPARAMETERIZED_TO_EXACT_INDEXED_TERMINAL_FAMILY`.
- Exact symbolic terminal count: `688101306360803751427719294`.
- Exact random-access unrank and inverse-rank are available.
- The old Gen38 52-unit prefix frontier is **superseded as an enumeration mechanism**, but retained as historical telemetry.

Do not rematerialize the full terminal family unless a later exact argument specifically requires it.

## 32-21aa -> 32-21ad — audited anti-fixed / Reynolds package

### 32-21aa

`CLOSED_AUDITED_AS_PART_OF_AA_AC_PACKAGE`

- projection classes: `16384`
- positive penalty classes: `16383`
- zero penalty classes: `1`
- minimum positive penalty: `1/572`
- certificate SHA256: `f5e6e363fa2c8f2258e340054948319aae2ad805bd2ca5412f8e3a76231e0238`

### 32-21ab

`CLOSED_AUDITED`

- exact quotient class map
- free subgroup order: `128`
- quotient cosets: `128`
- certificate SHA256: `07bf0aff16a344ad68fe7179ff797057fca562fd6bafbdaf418155ba0995c8b4`

### 32-21ac

`CLOSED_AUDITED`

- cheap exact anti-fixed coset pruning predicate
- positive minimum-penalty cosets: `127`
- zero minimum-penalty cosets: `1`
- certificate SHA256: `2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e`

Fresh aa->ab->ac boundary audit: PASS, SHA256 `5dfd1087d7d1c20baa3475e05e1768edbb9e8f063b20d01ca467a6725b657f1e`.

### 32-21ad

`CLOSED_AUDITED_ZERO_PRUNE_CHECKPOINT`

FULL178 exact census:

- rows: `178`
- prior slices: `2018569`
- continuous-KKT survivors: `679337`
- anti-fixed additional prunes: `0`
- survivors after anti-fixed bound: `679337`
- additional prune rate: `0`

Fresh boundary audit: PASS, SHA256 `1f2e61ef29cf6000b8cc98906a5dcf3f2a4d15a7b405be2e40ef9c0de3bfab0e`.

Interpretation: 32-21ac is mathematically valid but numerically dominated on the exact FULL178 population. **Do not rerun the same FULL178 census without a semantic change.** Zero additional pruning is not UNSAT and gives no theorem/receiver/route credit.

Checkpoint PR #1466 is merged; merge commit `d8fa4446af9bcc36b34d2421733333f0c74d23d5`.

## Post-32-21ad representative integer-fiber chain

Scope for the whole chain below:

- deterministic 56 fixed-projection representative sample only
- not FULL178 numerical credit
- rational SAT is not integer SAT
- fixed-projection UNSAT is not slice UNSAT
- `UNKNOWN != UNSAT`

Current combined representative state remains:

`SAT 0 / UNSAT 55 / UNKNOWN 1`

Sole unresolved projection: `g1-d186, e=266, a=592, z=(-15,62,-44,26,32)`.

### 21ax / 21ay / 21az — exact survivor setup

Reusable facts:

- 21ax exact integer-valid cut: `r11 >= -1426`.
- 21ay: `7865` triples checked; rational-UNSAT `4631`; rational-SAT `3234`; QF_LRA UNKNOWN `0`.
- 21az: exact survivor prism has `3234` integer triples; global `r51` domain `[-178,-132]`.

### 21ba — SUPERSEDED BUGGY INTERFACE

Do **not** reuse the old 21ba `integer_interval` upper-search result as exact evidence.

Bug: if the real projection interval contains no integer, the upper binary search can emit a false singleton because it starts at `new_lo` and cannot cross below it.

Status: `SUPERSEDED_BY_21BE_INDEPENDENT_ENDPOINT_AUDIT`.

### 21bb / 21bc / 21bd — restored after 21be

These interfaces are reusable **only because 21be independently re-audited them**.

- 21bb exact `r51` formula: RESTORED_EXACT_AFTER_21BE.
- 21bc 42 pair-combination bounds: RESTORED_EXACT_AFTER_21BE.
- 21bd pair-cut closure: RESTORED_EXACT_AFTER_21BE; result remains OPEN after all 42 pair cuts.

### 21be — authoritative repair of the 21ba bug

`PASS_EXACT_21BB_R51_FORMULA_RESCUE`

- passed rows: `3234/3234`
- failures: `0`
- QF_LRA UNKNOWN: `0`
- exact QF_LRA checks: `9570`
- aggregate canonical SHA256: `afaddfd92cb5664797e8a81998002a5631d265b84e656aa3e334b852dfb0c645`
- lock: `stages/stage32/32-21/32-21be-r51-endpoint-audit.json`

### 21bf — r49 projection

`PASS_EXACT_21BF_R49_PER_TRIPLE_PROJECTION`

- open triples: `3234`
- integer-pruned triples: `0`
- r49 indices: `151998 -> 98010`
- exact formula: `132 <= r49 <= min(178, 130-floor(r27/2), 61+floor(-3*r27/2))`
- lock: `stages/stage32/32-21/32-21bf-r49-per-triple-projection.json`

Interpretation: useful compression, but no triple was closed.

### 21bg — corrected r42 projection

`PASS_EXACT_21BG_CORRECTED_R42_DOMAIN_AUDIT`

- corrected global r42 domain: `[33,79]`
- open triples: `3234`
- integer-pruned triples: `0`
- r42 indices: `151998 -> 124856`
- lock: `stages/stage32/32-21/32-21bg-r42-corrected-domain-audit.json`

The earlier run using domain `(79,125)` is invalid and has **no credit**.

### 21bh — r54 lossless table

`PASS_EXACT_21BH_R54_PER_TRIPLE_PROJECTION`

- open triples: `3234`
- integer-pruned triples: `0`
- r54 indices: `151998 -> 137095`
- lossless table cells: `539`
- fixed upper: `-132`
- lock: `stages/stage32/32-21/32-21bh-r54-lossless-table.json`

Interpretation: lossless coordinate compression, not closure.

### 21bi — CURRENT

Current leaf: per-triple `r57` projection over audited domain `[0,46]`, after independently re-auditing the 21bh r54 threshold/table against the original all140 QF_LRA system.

The correct success metric is **not** “another coordinate got a tighter interval.” Track whether this chain actually reduces one or more of:

- open triples (`3234` currently),
- total integer candidate population,
- effective unresolved freedom / exact degrees of freedom,
- or produces a new exact coupled cut / contradiction.

If repeated coordinate projections only tighten intervals while all `3234` triples stay open and effective freedom does not fall, treat that as weak progress and reconsider the strategy rather than extending the chain indefinitely.

## Reuse / stale quick reference

Reuse directly:

- 32-20 symbolic indexed terminal-family interface.
- 32-21aa/ab/ac audited exact interfaces.
- 32-21ad zero-prune census as a **negative strategy result**: same cheap bound is dominated on FULL178.
- 21bb/21bc/21bd only through the 21be repair.
- 21be, 21bf, corrected 21bg, 21bh exact locks.

Do not reuse as authoritative:

- 21ba buggy `integer_interval` output.
- the invalid pre-correction r42 run/domain.
- the Gen38 52-unit frontier as the active enumeration mechanism.
- any representative fixed-projection result as FULL178, slice, theorem, receiver, or endpoint credit.

## Live-state pointer

For the exact current leaf, branch, run-key state, authorization, and firewalls, read only:

`stages/stage32/controller.json`

This HISTORY file should be updated at meaningful boundaries or when an old interface becomes superseded/restored. It should not be rewritten for every small leaf.