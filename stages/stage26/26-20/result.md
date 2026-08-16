# Stage26-20 — matched finite third-face transition baseline

EVIDENCE_LEVEL=DERIVED_EXACT_FINITE
CHECKPOINT=20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage26-10_AUDITED_PASS_MERGED_PR1014
TRANSITION=Stage18->Stage20

## Purpose

Checkpoint20 does not estimate the true Euler-brick exponent. It freezes the exact finite comparison panel obtained by joining the already-audited Stage18 and Stage20 censuses on the same primitive/canonical Euclidean cutoff.

The source tables are

- `stages/stage18/18-20/counts.csv`, counting exactly-two objects `M2(B)`;
- `stages/stage20/20-20/counts.csv`, counting exactly-three Euler objects `M3(B)`.

Both use

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]

with no integral-space-diagonal requirement and one count per primitive canonical physical object.

```text
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
SPACE_DIAGONAL_REQUIRED=false
FINITE_JOIN_KEY=B
```

## Exact finite adapters

For each common cutoff define

\[
H_{\ge2}=M_2+M_3,\qquad P=M_2+3M_3,
\]

\[
r=\frac{M_3}{M_2},\qquad
\Phi=\frac{M_3}{M_2+M_3},\qquad
\Theta=\frac{3M_3}{M_2+3M_3}.
\]

The Stage26-10 bridge is rechecked row by row:

\[
\Theta=\frac{3\Phi}{1+2\Phi},\qquad
\Phi=\frac{\Theta}{3-2\Theta}.
\]

The frozen common panel is:

| B | M2 | M3 | H>=2 | P | Phi | Theta |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 16 | 0 | 16 | 16 | 0 | 0 |
| 100 | 56 | 0 | 56 | 56 | 0 | 0 |
| 200 | 172 | 0 | 172 | 172 | 0 | 0 |
| 400 | 494 | 1 | 495 | 497 | 1/495 | 3/497 |
| 800 | 1347 | 3 | 1350 | 1356 | 1/450 | 3/452 |
| 1200 | 2350 | 5 | 2355 | 2365 | 1/471 | 3/473 |
| 1600 | 3536 | 5 | 3541 | 3551 | 5/3541 | 15/3551 |
| 2000 | 4812 | 7 | 4819 | 4833 | 7/4819 | 7/1611 |

Canonical machine-readable rows are in `finite-panel.csv`.

## What the finite panel establishes

1. The object-host survival `Phi` and the raw-pair completion `Theta` are numerically distinct even at identical `B`; using one in place of the other is a multiplicity error.
2. The exact Stage26-10 bridge holds on every row, including the zero rows.
3. Once `M3>0`, `Theta/Phi=3/(1+2Phi)<3`, and the observed values are close to but strictly below `3`; this is algebra plus finite evaluation, not an asymptotic proof.
4. The common matched panel stops at `B=2000`. Larger known Stage20/Stage14-e Euler counts such as `M3(10000)=18`, `M3(50000)=42`, `M3(200000)=82`, `M3(1000000)=219` do **not** form a Stage26 transition ratio here because a matched Stage18 `M2` census at those cutoffs is not frozen in the repository interface.
5. The Stage14-num integral-space population is not substituted for `M2`; it remains a negative-control/regression oracle only.

## Frozen theorem backdrop, not inferred from the table

The audited asymptotic interfaces remain

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

and for every fixed `eta<1/46`,

\[
B^{1/6}\ll M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Together with the exact Stage26-10 adapter they imply the already-authorized completion corridor and `Phi,Theta -> 0`; none of those statements is proved from the eight finite rows.

## Numerical reuse protocol

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=Stage18-20_FROZEN_CENSUS,Stage20-20_FROZEN_CENSUS,NUM-R01,NUM-R03,NUM-R08
NUM_POPULATION_MATCH=ADAPTER_PROVED_FOR_STAGE18_STAGE20;NO_MATCH_FOR_STAGE14_NUM_SPACE_POPULATION
NUM_EVIDENCE_LEVEL=DERIVED_EXACT_FINITE
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_FOR_GLOBAL_PANEL;EXISTING_MATCHED_FROZEN_COUNTS_SUFFICE
```

## Firewalls

```text
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
TRUE_M3_EXPONENT_IDENTIFIED=false
SQUARE_ROOT_LAW_CLAIMED=false
MONOTONIC_COMPLETION_RATE_CLAIMED=false
INDEPENDENCE_PRODUCT_CLAIMED=false
INTEGRAL_SPACE_CENSUS_SUBSTITUTED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=30
NEXT_EXPECTED_COMMAND=Stage26-audit
```
