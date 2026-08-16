# Stage23 arsenal promotion — one-face-space to two-face-space transition

PROMOTION_ID=AR-STAGE23-TRANSITION-N1-N2
WEAPON_ID=S23-W01
STATUS=AUDITED_PASS_CLOSED_WITH_STAGE25_SUPERSESSION
SOURCE_STAGE=Stage23
SOURCE_CHECKPOINT=70

## Purpose

Reusable interface for the transition from primitive canonical exactly-one-face cuboids with integral space diagonal to the matching exactly-two-face stratum under the same physical cutoff.

## Input contract

```text
POPULATION_SOURCE=primitive canonical exactly-one integral face + integral space diagonal
POPULATION_TARGET=primitive canonical exactly-two integral faces + integral space diagonal
CANONICAL=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
CUTOFF=R=d<=B
RATIO_SEMANTICS=matched adjacent-stratum population-size ratio
LITERAL_SUBSET_TRANSITION=false
SPACE_DIAGONAL_ALREADY_PRESENT_IN_SOURCE=true
```

## Output theorem

With

`N1(B) ~ kappa/(24*pi) * B(log B)^3`, `kappa>0`,

and

`N2(B) <<_epsilon B^(1/2+epsilon)`,

one has

`N2(B)/N1(B) <<_epsilon B^(-1/2+epsilon)/(log B)^3 -> 0`.

The transition is therefore zero-density.

A second same-host proof is available at qualitative scale: every Stage19 target lies in a second-face pair-overlap locus inside the already-space-integral Stage17 Pythagorean-chain host, and the frozen overlap theorem gives

`N2(B)<=P(B)=o(B(log B)^3)`.

This directly yields `N2(B)=o(N1(B))` without double-charging space integrality.

## Causal reuse note

Stage17 already satisfies

`x^2+y^2=p^2`,
`p^2+z^2=d^2`.

Stage19 adds one cross-leg face condition

`x^2+z^2=q^2` or `y^2+z^2=q^2`.

Thus the reusable causal description is:

```text
already-space-integral Pythagorean chain
  -> add second cross-leg Pythagorean compatibility
  -> pair-overlap is zero-density in the Stage17 host
```

Do not reuse Stage22's free-complementary-edge mechanism literally here.

## Reusable family-obstruction pattern

Stage23 also promotes a family-specific warning useful in future lower-bound searches. The canonical Stage15-2 explicit linear ambient exactly-two family has

`R^2=17(p^4+q^4)`

for odd `p,q`, hence `R^2=2 mod 16`. Therefore it has zero integral-space lifts. An ambient lower family may be quantitatively large and still be annihilated completely by the space-integrality condition.

This is a route filter, not a global Stage19 nonexistence theorem.

## Reuse conditions

Use the transition theorem directly only when population, canonicalization, primitivity, cutoff, multiplicity and space-diagonal requirements match exactly. Preserve the distinction between the qualitative Stage17-host overlap explanation and the stronger inherited Stage19 half-power upper bound.

## Nonclaims

```text
TARGET_UNBOUNDEDNESS_PROVED=true
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=true
CURRENT_GLOBAL_LOWER=N2(B)>>B^(1/4)
CURRENT_DIRECTIONAL_LOWER=N2,j(B)>>_j B^(1/4) for j=a,b,c
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
HALF_POWER_OPTIMALITY_CLAIMED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

Historically, the exact census `N2(500000000)=3495` gave only a constant floor
by monotonicity. It remains finite evidence, but the current unboundedness and
positive-power statements now come from the audited S25-W01 construction, not
from that census.

```text
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_DECISION=YES
ARSENAL_PROMOTION_MATERIALIZED=true
REUSE_CLASS=DIRECT_REUSE_ON_EXACT_STAGE23_CONTRACT
NEW_STANDALONE_ANALYTIC_THEOREM_PROMOTED=false
```

## Stage25 exact-mask upgrade

```text
WEAPON_ID=S23-W02
TYPE=EXACT_MASK_FORMULA
STATUS=ACTIVE
```

The audited Stage25 reentry truth table adds the reusable identities

\[
N_{2,a}=A_{ab,ac}-A_3,\quad
N_{2,b}=A_{ab,bc}-A_3,\quad
N_{2,c}=A_{ac,bc}-A_3.
\]

Hence every pairwise directional contrast cancels the common `A3`
contamination exactly. This is an algebraic mask adapter; it does not assume
that perfect cuboids exist or do not exist.
