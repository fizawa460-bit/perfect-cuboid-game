# Stage32 retrospective re-anchor — 32-19 / 32-20 / 32-21

This file is the authoritative Stage32 generation map after the long post-32-18 production sequence.

The re-anchor is retrospective only: it changes names and navigation, not any previously accepted exact result, audit verdict, artifact hash, UNKNOWN semantics, theorem credit, receiver credit, or perfect-cuboid firewall.

## Boundary

`32-18` remains the audited B16-era line. The clean generation boundary is after PR #1451 promoted the audited B16 stack. Post-B16 residual-feasibility, pairing-prefix production, and the long PR #1462 history are grouped below instead of being retroactively split into dozens of lettered historical leaves.

## 32-19 — brute-force scaling limit / hard-tail generation

Status: `CLOSED_RETROSPECTIVE`

Scope: post-B16 residual feasibility through the resumable Gen38 hard-tail and residual-volume diagnostics.

Accepted interpretation:

- bounded production did make exact progress, but the surviving strata became giant individual exact strata;
- Gen38 ended with 52 continuations from 73 inputs, and all 52 diagnostic survivors remained at the same `e`;
- FULL178 contains 64,111 coarse `e` strata;
- the exact finite raw remaining-node upper bound is `4555530975806418`;
- the local-linear estimate is `2877801026017990` remaining nodes, about `11241411` 256M-equivalent chunks or `661260` idealized 17-runner waves;
- therefore simply escalating 64M/128M/256M ceilings is no longer the primary strategy. Blind 512M/1B escalation is explicitly dominated.

This closes the operational question “can we finish by continuing to hit the same enumeration harder?” It does not revoke Gen33–Gen38 evidence.

## 32-20 — symbolic prefix compression / exact random access

Status: `CLOSED_CHECKPOINTED`

Goal: replace terminal-by-terminal materialization of the current 11-pairing prefix family.

Accepted checkpoint:

- exact symbolic terminal count: `688101306360803751427719294`;
- exact random-access unrank and inverse rank;
- small-family full-set bijection checked;
- large `e=663,729` roundtrips checked;
- the Gen38 52-unit frontier is retained as historical telemetry but superseded as the enumeration mechanism.

Result: `PASS_PREFIX_DFS_REPARAMETERIZED_TO_EXACT_INDEXED_TERMINAL_FAMILY`.

This is a representation theorem for the locked prefix family only. It is not numerical Picard row completion.

## 32-21 — numerical Picard leaf compression on the exact prefix representation

Status: `IN_PROGRESS`

The job now is to push actual numerical Picard information into the compressed representation and reduce the huge family without materializing it.

The Reynolds fixed rank-2 exact integer-QP check alone prunes `0 / 679337` continuous-KKT survivors, so information discarded by the fixed projection has to be restored or bounded.

### 32-21aa — anti-fixed coset penalty representation

Status: `CLOSED_CHECKPOINTED`

Exact checkpoint:

- exact Reynolds projection classes: `16384`;
- exact safe class penalty `lambda(r) <= -q^2` obtained from retained-coordinate fractional residues and exact slice-kernel dual norms;
- positive penalty classes: `16383`;
- zero penalty classes: `1`;
- distinct penalty values: `23`;
- minimum positive penalty: `1/572`;
- maximum coordinate-Cauchy penalty: `5/39`;
- exact CI run `33307921980`, artifact `9731071290`;
- canonical certificate SHA256 `f5e6e363fa2c8f2258e340054948319aae2ad805bd2ca5412f8e3a76231e0238`;
- canonical penalty-stream SHA256 `8bd09aa4a7e942b7bb772815a05475d04604985556325203dec0851437c0c76e`.

No 59-dimensional closest-vector search and no terminal-family materialization were used. This closes the finite anti-fixed penalty representation only; numerical row completion and all higher credit remain closed.

### 32-21ab — exact quotient class map

Status: `IN_PROGRESS`

Goal: derive an exact map from the rank-2 projected Smith affine coordinates to the `16384` Reynolds projection classes so the 32-21aa penalty can be attached to every projected candidate without terminal materialization.

Exit criterion: a deterministic exact class map with proof/check of compatibility with the fixed-image basis, Smith affine parameterization, and the 32-21aa canonical projection-residue convention.

### 32-21ac — cheap exact pruning predicate

Status: `PLANNED_IN_CURRENT_WORK_PACKAGE`

Goal: combine the exact projected self-intersection slack with the mapped 32-21aa anti-fixed penalty into a cheap, exact, safe pruning predicate.

Exit criterion: an evaluator whose negative decision rigorously prunes an original integral Picard slice, with deterministic tests/certificate and no 27-digit terminal-family materialization.

### Meaningful audit boundary: after 32-21ac

`32-21aa`, `32-21ab`, and `32-21ac` are one tightly coupled mathematical package:

1. represent the information lost by Reynolds averaging;
2. attach that finite state to the rank-2 projected coordinates;
3. turn the attached state into an actually usable exact pruning predicate.

Therefore the current PR #1465 is the container for `32-21aa -> 32-21ab -> 32-21ac`. Do **not** stop merely because one small leaf closes. Continue within the same PR while the next step is a tightly coupled adapter needed to make the package usable.

After 32-21ac reaches its exact exit criterion, stop and run a fresh boundary audit. Merge #1465 only after that audit passes. The audit should check the complete aa->ab->ac semantic chain, exactness, hashes/tests, UNKNOWN semantics, heavy-run safety, and all research-credit firewalls.

### 32-21ad — FULL178 compressed numerical census

Status: `BLOCKED_ON_AA_AC_BOUNDARY_AUDIT`

This is the next major phase: apply the audited compressed evaluator to the FULL178 population. It is a natural new PR / execution boundary because it changes from building the exact evaluator to using it at full population scale and may require a separately authorized production run.

Release condition: `32-21aa-ac boundary audit PASS`.

## PR / MAIN batch discipline from this boundary

PR #1462 is the historical exception and is merged.

From 32-21 onward, **leaf boundaries are reasoning/checkpoint boundaries, not automatic PR or audit boundaries**.

Default MAIN behavior:

- advance through consecutive tightly coupled leaves in the same PR until a meaningful boundary is reached;
- keep leaf labels small enough that exact failures and dependencies remain diagnosable;
- do not manufacture a PR merely because a lettered leaf completed;
- record intermediate exact checkpoints inside the current PR/controller/state;
- run a fresh audit at meaningful boundaries, especially before full-population production, heavy arming, downstream/claim promotion, or a materially different mathematical strategy;
- after an audit PASS, merge/checkpoint the package and start the next coherent package in a new PR;
- a material blocker or strategy change may force an earlier audit/split;
- controller/docs-only edits never authorize heavy compute;
- heavy work still requires a fresh run-key synchronization and repository-wide Actions policy compliance.

Current working package:

`PR #1465: 32-21aa CLOSED_CHECKPOINTED -> 32-21ab IN_PROGRESS -> 32-21ac PLANNED -> BOUNDARY AUDIT -> merge -> 32-21ad next PR`
