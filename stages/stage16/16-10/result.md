# Stage16-10 — one-face population contract

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Purpose

Open Stage16 under the Stage16-28 roadmap and freeze the physical population before any new finite census, asymptotic comparison, or theorem transfer is attempted.

Stage16 studies primitive canonical cuboids with **exactly one** integral face diagonal and does **not** require the space diagonal to be integral.

## Physical population

For positive integer edges, use the unique canonical representative

\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]

Define

\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}.
\]

The common cutoff is

\[
R(a,b,c)\le B.
\]

For the three face predicates

\[
F_{ab}: a^2+b^2\text{ is a square},\quad
F_{ac}: a^2+c^2\text{ is a square},\quad
F_{bc}: b^2+c^2\text{ is a square},
\]

Stage16 requires exactly

\[
1_{F_{ab}}+1_{F_{ac}}+1_{F_{bc}}=1.
\]

Thus exactly-two and three-face Euler cuboids are excluded from the Stage16 population rather than being counted with multiplicity.

No condition is imposed on whether `R` is integral.

## Count notation

Let

\[
\mathcal B_1(B)=\{(a,b,c): 0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly one face predicate holds}\},
\]

and

\[
M_1(B)=\#\mathcal B_1(B).
\]

This is the ambient exactly-one population for Stage16. It is intentionally distinct from historical exactly-one populations that additionally imposed an integral space diagonal.

## Common-cutoff adapter for Stage17 / Stage21

If a Stage16 object also has an integral space diagonal `d`, then by definition

\[
d^2=a^2+b^2+c^2=R^2,
\]

and positivity gives `d=R`. Hence on the integral-space-diagonal subpopulation

\[
R\le B\iff d\le B.
\]

This exact identity is the intended comparison adapter for Stage16 -> Stage17 and later Stage21. It avoids dividing counts taken under incompatible height conventions.

## Reuse / provenance

- `AR-001` is reused directly for primitive/canonical deduplication and exact separation of one/two/three-face populations.
- `AR-002` is retained as the standard exact Euclid certificate for whichever single face is integral; it does not by itself count the Stage16 population.
- `AR-039` is **not charged at Stage16-10**. It is recorded only as a future Stage16-50 candidate because its integral-space-diagonal exactly-one family lies inside the broader Stage16 population after the common-cutoff adapter is checked. No Stage16 lower bound is claimed here.

## Evidence and dependency ledger

```text
EVIDENCE_LEVEL=PROVED
DEPENDS_ON=docs/stage16-28-population-roadmap.md,docs/stage16-28-execution-controller-template.md,arsenal:AR-001,arsenal:AR-002
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
```

`EVIDENCE_LEVEL=PROVED` here applies only to the exact normalization and `R=d` adapter just stated. Stage16-10 makes no asymptotic count, ratio, upper bound, lower bound, or causal claim.

## Checkpoint decision

`Stage16-10` is submitted, not self-audited. The main lane stops before `Stage16-20` because a finite-data baseline generated before the population/cutoff contract is independently audited could bake a convention error into all later counts.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=10
CHECKPOINTS_ATTEMPTED=10
CHECKPOINTS_SUBMITTED=10
NEW_CLAIMS=exact Stage16 ambient exactly-one population definition and exact R=d cutoff adapter on the integral-space-diagonal subpopulation
REUSED_WEAPONS=AR-001,AR-002
CODEX_REQUIRED=false
CODEX_REASON=No bounded implementation or repository-heavy task is required for the population-contract checkpoint.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
```
