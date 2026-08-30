# Stage32 retrospective re-anchor — 32-19 / 32-20 / 32-21

This file is the authoritative Stage32 generation map after the long post-32-18 production sequence.

The re-anchor changes navigation, not historical exact evidence, audit verdicts, hashes, UNKNOWN semantics, theorem/receiver credit, or perfect-cuboid firewalls.

## 32-19 — brute-force scaling limit / hard-tail generation

Status: `CLOSED_RETROSPECTIVE`

The post-B16 resumable production reached giant individual exact strata. Gen38 retained 52 continuations from 73 inputs, while the exact finite raw remaining-node upper bound is `4555530975806418`. Blind 512M/1B escalation is therefore dominated as the primary strategy. Historical Gen33–Gen38 evidence remains valid.

## 32-20 — symbolic prefix compression / exact random access

Status: `CLOSED_CHECKPOINTED`

Result: `PASS_PREFIX_DFS_REPARAMETERIZED_TO_EXACT_INDEXED_TERMINAL_FAMILY`.

Exact symbolic terminal count: `688101306360803751427719294`, with exact random-access unrank and inverse rank. The Gen38 52-unit frontier remains historical telemetry but is superseded as the enumeration mechanism. This is not numerical Picard row completion.

## 32-21 — numerical Picard leaf compression

Status: `IN_PROGRESS_AT_AUDITED_BOUNDARY`

The fixed Reynolds rank-2 integer-QP alone pruned `0 / 679337` continuous-KKT survivors. The coherent aa->ab->ac package restores a finite exact piece of the information discarded by Reynolds averaging and turns it into a usable safe pruning predicate.

### 32-21aa — anti-fixed coset penalty representation

Status: `CLOSED_AUDITED_AS_PART_OF_AA_AC_PACKAGE`

Exact checkpoint:

- Reynolds projection classes: `16384`;
- `lambda(r) <= -q^2` from exact retained-coordinate fractional residues and exact slice-kernel dual norms;
- positive classes `16383`, zero class `1`;
- minimum positive penalty `1/572`;
- certificate SHA256 `f5e6e363fa2c8f2258e340054948319aae2ad805bd2ca5412f8e3a76231e0238`.

### 32-21ab — exact quotient class map

Status: `CLOSED_AUDITED`

Result: `PASS_STAGE32_21AB_EXACT_QUOTIENT_CLASS_MAP`.

For exact fixed-image basis `B`, projected Smith-right transform `T`, and Smith affine state `y=(y0,y1,y2,u,v)`, the canonical Reynolds projection residue is

`r=(B*T*y) mod 64`.

Exact package CI proves the Smith-coordinate image is exactly the same `16384` classes as 32-21aa. The free `(u,v)` directions generate a subgroup of order `128`, hence exactly `128` quotient cosets.

Certificate SHA256: `07bf0aff16a344ad68fe7179ff797057fca562fd6bafbdaf418155ba0995c8b4`.

### 32-21ac — cheap exact anti-fixed coset pruning predicate

Status: `CLOSED_AUDITED`

Result: `PASS_STAGE32_21AC_CHEAP_EXACT_ANTIFIXED_COSET_BOUND`.

For the exact free-subgroup coset `C` occupied by one projected slice, define

`lambda_C=min_{r in C} lambda(r)`.

Then every integral lift satisfies `x^2 <= p^2-lambda_C`. The existing exact rank-2 concave integer-QP is reused against the raised threshold `lower+lambda_C`, scaled to exact integers.

Exact package CI:

- free subgroup order `128`;
- quotient cosets `128`;
- positive minimum-penalty cosets `127`;
- zero minimum-penalty cosets `1`;
- minimum positive coset bound `1/572`;
- certificate SHA256 `2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e`.

### aa->ab->ac meaningful boundary audit

Status: `PASS`

Verdict: `PASS_STAGE32_21AA_AC_FRESH_BOUNDARY_AUDIT`.

Fresh audit run `33309333080`, job `99251414877`, artifact `9731500315` independently rebuilt `B*T mod 64`, the 16384-element image, the 128-element free subgroup, all 128 cosets, all 16384 penalties, and all coset minima. Canonical audit SHA256:

`5dfd1087d7d1c20baa3475e05e1768edbb9e8f063b20d01ca467a6725b657f1e`.

The 81-case synthetic Smith panel had old-rank2-false -> new-true count `0` and old-true -> new-false count `1`. That one strengthened panel prune is regression evidence only, not FULL178 numerical credit.

The initial audit attempt failed only because the audit harness omitted the `quad` import; it received no PASS or mathematical credit. The repaired fresh audit above is the authoritative audit.

## 32-21ad — FULL178 compressed numerical census

Status: `BLOCKED_PENDING_PR1465_MERGE`

This is the next major execution phase: apply the audited aa->ab->ac evaluator to the FULL178 population. It is deliberately separated from evaluator construction/audit.

Release requires:

1. #1465 merged into the authoritative base;
2. reread of current controller/main after merge;
3. execution/storage/concurrency preflight if the census design is materially heavy;
4. fresh run-key authorization if a heavy production workflow is used.

The aa->ab->ac audit does not arm 32-21ad.

## PR / MAIN batch discipline

Leaf labels are small reasoning/checkpoint units, not automatic PR or audit boundaries.

Default MAIN behavior:

- continue through tightly coupled leaves in one PR until a usable mathematical interface or other meaningful boundary is reached;
- checkpoint intermediate exact leaves so failures remain diagnosable;
- audit at meaningful boundaries, especially before full-population production, heavy arming, downstream/claim promotion, or a materially different strategy;
- after an audit PASS, checkpoint/merge the coherent package before entering the next major phase;
- controller/docs edits never authorize heavy compute;
- UNKNOWN remains distinct from UNSAT;
- all theorem / receiver / route / perfect-cuboid firewalls remain explicit.

Current pointer:

`32-19 CLOSED_RETROSPECTIVE -> 32-20 CLOSED_CHECKPOINTED -> 32-21aa CLOSED_AUDITED -> 32-21ab CLOSED_AUDITED -> 32-21ac CLOSED_AUDITED -> PR #1465 CHECKPOINT_MERGE_READY -> 32-21ad BLOCKED_PENDING_MERGE`
