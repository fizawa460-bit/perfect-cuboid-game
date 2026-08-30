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

Current exact obstruction: the Reynolds fixed rank-2 projection is cheap, but its exact integer-QP check prunes `0 / 679337` continuous-KKT survivors. Information discarded by the fixed projection must therefore be restored or bounded.

### 32-21aa — anti-fixed coset penalty representation

Status: `IN_PROGRESS`

Goal: obtain an exact finite-state representation of the anti-fixed lift / coset penalty, or an equivalent exact condition using the information lost by Reynolds averaging.

Exit criterion: an exact representation with a proof/check that it is safe for the numerical leaf and does not rely on enumerating the 27-digit terminal family.

Planned nearby leaves, subject to evidence:

- `32-21ab` — exact quotient class map;
- `32-21ac` — cheap exact lower bound / pruning predicate;
- `32-21ad` — FULL178 compressed numerical census once the evaluator is certified.

If 32-21aa reveals a materially different blocker, open a new leaf instead of stretching `aa`.

## PR discipline from this boundary

PR #1462 is a historical exception. It remains the container for the retrospective consolidation and current checkpoint until explicitly closed/merged by the user.

After #1462:

- normally one clear hypothesis + implementation + proof/check per leaf;
- normally one leaf per PR;
- two or three tightly coupled leaves may share one PR when separating them would create artificial boundaries;
- completed machinery is checkpointed rather than carried through many unrelated generations;
- a materially different strategy gets a new leaf label;
- controller/docs-only edits never authorize heavy compute;
- heavy work still requires a fresh run-key synchronization and repository-wide Actions policy compliance.

Current pointer:

`32-19 CLOSED_RETROSPECTIVE -> 32-20 CLOSED_CHECKPOINTED -> 32-21aa IN_PROGRESS`
