# Stage23 self-contained closeout bundle

BUNDLE_ID=STAGE23-SELF-CONTAINED-CLOSEOUT-20260815
STATUS=AUDITED_PASS_CLOSED_PENDING_MERGE
STAGE=Stage23
TRANSITION=Stage17 -> Stage19

## Population contract

Let `N1(B)` count primitive canonical cuboids `0<a<b<c`, `gcd(a,b,c)=1`, with integral space diagonal

`d=R=sqrt(a^2+b^2+c^2)<=B`

and exactly one integral face diagonal. Let `N2(B)` count the same primitive/canonical/cutoff population with exactly two integral face diagonals.

The two strata are disjoint. Therefore `N2/N1` is a matched adjacent-stratum population-size ratio, not a literal survival probability of a fixed object.

## Frozen source and target facts

The audited Stage17 source law is

`N1(B) ~ kappa/(24*pi) * B(log B)^3`, with `kappa>0`.

The strongest audited Stage19 target theorem is only

`N2(B) <<_epsilon B^(1/2+epsilon)`.

Hence

`N2(B)/N1(B) <<_epsilon B^(-1/2+epsilon)/(log B)^3 -> 0`.

Thus the Stage17 -> Stage19 transition is rigorously zero-density.

No matching Stage19 asymptotic or lower power law is known. The current certified lower statement is only

`N2(B)>=3495` for `B>=500000000`,

from the exact census at `B=500000000` plus monotonicity.

## Source-host causal synthesis

A Stage17 object already carries a Pythagorean face and an integral space diagonal. After orienting the integral face as

`x^2+y^2=p^2`,

space integrality is already encoded by

`p^2+z^2=d^2`.

To enter Stage19, the object must add one of the cross-leg Pythagorean relations

`x^2+z^2=q^2`

or

`y^2+z^2=q^2`.

The frozen Stage13/Stage17 pair-overlap theorem gives total pair-overlap mass

`P(B)=o(B(log B)^3)`

inside this already-space-integral host. Every Stage19 exactly-two object lies in one of these pair-overlap loci, so

`N2(B)<=P(B)=o(B(log B)^3)`.

Together with the Stage17 asymptotic, this gives a direct qualitative causal proof of

`N2(B)/N1(B)->0`

without charging the space condition twice.

The sharper `B^(1/2+epsilon)` Stage19 upper bound is compatible with this explanation but is inherited from the deeper Stage19 target theorem. Stage23 does not identify the intrinsic mechanism producing the half-power exponent.

## Important contrast with Stage22

Stage22's dominant source-side cause was a complementary edge free at polynomial order that becomes coupled by a second face condition. That explanation does not transfer literally here. In Stage17 the complementary edge already participates in the Pythagorean space-extension equation `p^2+z^2=d^2`. Stage23 therefore starts from an already-coupled Pythagorean chain and imposes one additional cross-leg compatibility.

```text
STAGE22_FREE_EDGE_CAUSE_TRANSFERS_LITERALLY=false
SPACE_CONDITION_ALREADY_PAID_IN_SOURCE=true
SECOND_FACE_CROSS_LEG_COMPATIBILITY_IS_NEW=true
```

## Aggressive lower-bound search boundary

Stage23 did not stop after proving zero density. It attacked the target lower side using source-family slicing, a consecutive-parameter degeneration, Kummer/Jacobi moving-family analysis, four fresh Stage19 surgeon candidates, and eight source-level revalidations of older Stage14/15 routes.

Two rigorous global family exclusions emerged:

1. the selected AR-039 consecutive slice is empty for all integer parameters because its square-value right side is always `2 mod 8`;
2. the canonical Stage15-2 linear-size ambient exactly-two family cannot lift to Stage19 because its space norm is always `2 mod 16`.

These exclusions are family-specific. They do not prove Stage19 finiteness or nonexistence.

## Lower-bound and exponent frontier

```text
CERTIFIED_CONSTANT_LOWER_FLOOR=N2(B)>=3495_FOR_B>=500000000
TARGET_UNBOUNDEDNESS_PROVED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
HALF_POWER_OPTIMALITY_CLAIMED=false
```

Mere finite growth in the census is not promoted to an asymptotic. Mere infinitude of a hypothetical parameter sequence would also not imply a power lower bound without a quantitative density statement.

## Reuse firewalls

- Keep the literal Stage17/19 primitive canonical population and common cutoff `R=d<=B`.
- Do not interpret `N2/N1` as a subset-survival probability.
- Do not re-charge integral space diagonal as a new Stage23 thinning condition.
- Do not transfer Stage22's free-edge explanation literally.
- Do not promote the half-power target upper bound to an optimal exponent.
- Do not infer Stage19 unboundedness from the finite exact census.
- Do not infer global nonexistence from the mod-8 or mod-16 family obstructions.

## Scope

Stage23 proves a zero-density adjacent-stratum transition under an already-integral space diagonal and records a causal source-host explanation at qualitative scale. It does not prove existence or nonexistence of a perfect cuboid.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_DECISION=YES
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
ARSENAL_PROMOTION_REQUIRED=true
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
```
