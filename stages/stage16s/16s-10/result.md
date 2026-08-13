# Stage16S-10 — space-diagonal baseline population contract

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Purpose

Open the auxiliary Stage16S lane defined by `docs/stage16-28-population-roadmap.md` and freeze the common physical population before any finite census, asymptotic law, or causal comparison is attempted.

Stage16S measures the cost of requiring an integral space diagonal **before** any integer-face condition is charged. It tracks two populations:

```text
SPACE_AT_LEAST = integer space diagonal, no face-diagonal restriction
SPACE_ONLY     = integer space diagonal and zero integer face diagonals
```

Stage16S is parallel to the numbered roadmap. It does not replace or block the current Stage17/18 lane.

## Common source population

For positive integer edges, use the canonical primitive representative

\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]

Define the geometric height

\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}
\]

and impose the common cutoff

\[
R(a,b,c)\le B.
\]

This is the same primitive/canonical `R<=B` source convention used by Stage16.

Let the face predicates be

\[
F_{ab}:a^2+b^2\text{ is a square},\quad
F_{ac}:a^2+c^2\text{ is a square},\quad
F_{bc}:b^2+c^2\text{ is a square}.
\]

## SPACE_AT_LEAST

Define

\[
\mathcal S_{\mathrm{all}}(B)=
\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ R\in\mathbb Z\}.
\]

Write

\[
N_S^{\mathrm{all}}(B)=\#\mathcal S_{\mathrm{all}}(B).
\]

No restriction is placed on the number of integral face diagonals in this population.

If `d` denotes the positive integral space diagonal, then

\[
d^2=a^2+b^2+c^2=R^2,
\]

so positivity gives

\[
d=R.
\]

Therefore on Stage16S objects

\[
d\le B\iff R\le B.
\]

No separate height adapter is needed.

## SPACE_ONLY

Define the zero-face subpopulation

\[
\mathcal S_0(B)=
\{(a,b,c)\in\mathcal S_{\mathrm{all}}(B):
1_{F_{ab}}+1_{F_{ac}}+1_{F_{bc}}=0\}.
\]

Write

\[
N_S^0(B)=\#\mathcal S_0(B).
\]

Thus `SPACE_ONLY` excludes every object with one, two, or three integral face diagonals. The exclusion is exact, not multiplicity-weighted.

## Exact comparison interfaces

Because Stage16 and Stage16S use the same primitive/canonical `R<=B` source convention, their ambient comparison needs no cutoff or symmetry adapter.

Under the frozen contracts,

\[
\text{Stage17 population}
=
\text{Stage16 population}\cap\mathcal S_{\mathrm{all}}(B).
\]

This is an exact set identity: Stage16 supplies the exactly-one-face condition and Stage16S supplies the integral-space-diagonal condition. No survival ratio or independence conclusion is inferred from the identity at checkpoint 10.

Likewise, `SPACE_ONLY` is disjoint from Stage16, Stage17, Stage18, Stage19, and Stage20 populations because all of those named populations require at least one integral face diagonal.

## Reuse / provenance

- Stage16-10 supplies the already-audited primitive/canonical `R<=B` source convention.
- `AR-001` supplies the reusable primitive/canonical physical convention and face-multiplicity separation.
- No Stage13, Stage14, Stage15, or Stage17 asymptotic theorem is imported at checkpoint 10.

## Evidence and dependency ledger

```text
EVIDENCE_LEVEL=PROVED
DEPENDS_ON=docs/stage16-28-population-roadmap.md,docs/stage16-28-execution-controller-template.md,stages/stage16/16-10/result.md,arsenal:AR-001
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
PARALLEL_LANE=YES
```

`EVIDENCE_LEVEL=PROVED` applies only to the exact definitions and set/cutoff identities above. Stage16S-10 makes no finite-count, asymptotic, density, upper-bound, lower-bound, or causal claim.

## Checkpoint decision

`Stage16S-10` is submitted, not self-audited. The main lane stops before `Stage16S-20` because checkpoint 20 would freeze the canonical finite census. The population/cutoff contract must receive a fresh Stage16S audit before any enumerator output becomes stage evidence.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=10
CHECKPOINTS_ATTEMPTED=10
CHECKPOINTS_SUBMITTED=10
NEW_CLAIMS=exact Stage16S SPACE_AT_LEAST and SPACE_ONLY population definitions; exact d=R cutoff identity; exact Stage17=Stage16 intersect SPACE_AT_LEAST set interface
REUSED_WEAPONS=Stage16-10,AR-001
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 10 is a compact population-contract freeze and requires no bounded implementation or repository-heavy task.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
```
