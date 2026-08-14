# Stage23-60 — causal decomposition after old-branch revalidation

EVIDENCE_LEVEL=PROVED_CAUSAL_SYNTHESIS_PLUS_ATTACK_LEDGER
CHECKPOINT=60
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Revalidation gate consumed before synthesis

The checkpoint60 policy is satisfied by `stages/stage23/23-60/revalidation-ledger.md`. Eight high-value Stage14/15 branches were opened at their actual source artifacts and retested against the literal Stage23 target before this synthesis was written.

The strongest fresh revalidation is the global exclusion of the Stage15-2 explicit ambient exactly-two lower family. That family has

\[
R^2=17(p^4+q^4)
\]
for coprime odd `p,q`. Integral space diagonal would require `D^2=17(p^4+q^4)`, but the right side is `2 mod 16`, impossible for a square. Thus a linear-size ambient Stage18 family can be completely annihilated by the already-required Stage17/19 space condition.

No revalidated branch proves Stage19 unboundedness or a positive-power lower bound.

## 2. Frozen quantitative transition

Stage17 supplies

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad \kappa>0,
\]
while Stage19 supplies only

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]
Therefore checkpoint30 remains

\[
\boxed{
\frac{N_2(B)}{N_1(B)}
\ll_\varepsilon
\frac{B^{-1/2+\varepsilon}}{(\log B)^3}
\to0.
}
\]

The current certified lower floor is

\[
\boxed{N_2(B)\ge3495\qquad(B\ge500{,}000{,}000),}
\]
from the exact census at `500,000,000` plus monotonicity. No unboundedness follows.

## 3. Source architecture with space diagonal already paid

Choose the unique integral face of a Stage17 source object and write it as

\[
x^2+y^2=p^2.
\]
Because the space diagonal is already integral, the complementary edge `z` is not a free order-`B` edge. It already satisfies

\[
p^2+z^2=d^2,
\qquad d=R.
\]

Thus the Stage17 source architecture is an **already coupled two-level Pythagorean chain**

\[
(x,y)\to p,\qquad (p,z)\to d.
\]

This distinction is essential when comparing Stage23 with Stage22.

## 4. Exact new Stage23 condition: close the cross-leg Pythagorean compatibility

To enter the exactly-two target, one of the two remaining faces must become Pythagorean:

\[
\boxed{x^2+z^2=q^2}
\qquad\text{or}\qquad
\boxed{y^2+z^2=q^2}.
\]

Hence Stage23 does not impose the space equation again. It asks the pre-existing Stage17 chain to admit an additional cross-leg Pythagorean relation while preserving primitivity, canonicalization, the exactly-two mask and the same physical cutoff.

This is the clean Stage17-originating causal description of the transition.

```text
SOURCE_STRUCTURE=ONE_FACE_PLUS_INTEGRAL_SPACE_PYTHAGOREAN_CHAIN
NEW_STAGE23_RELATION=SECOND_FACE_CROSS_LEG_PYTHAGOREAN_COMPATIBILITY
SPACE_DIAGONAL_NEWLY_IMPOSED=false
```

## 5. Direct Stage17-host proof of qualitative zero density

Stage17's frozen Stage13 interface contains raw pair-overlap bounds

\[
A_{ab,ac},\ A_{ab,bc},\ A_{ac,bc},\ A_3
=o(B(\log B)^3)
\]
in the integral-space host. Put

\[
P(B)=A_{ab,ac}+A_{ab,bc}+A_{ac,bc}.
\]

Every Stage19 exactly-two object has two integral faces and an integral space diagonal, so it lies in at least one pair-overlap locus. Consequently

\[
0\le N_2(B)\le P(B)=o(B(\log B)^3).
\]

Since

\[
N_1(B)\sim cB(\log B)^3,
\qquad c>0,
\]
we obtain directly

\[
\boxed{N_2(B)/N_1(B)\to0.}
\]

This is a **source-host causal zero-density proof**: once space integrality has already been paid, the added second face forces the object from the dominant exactly-one stratum into a lower-order pair-overlap locus.

It does not recover the stronger half-power rate.

## 6. No double charge of the Stage19 squareclass mechanism

Stage19 gives an exact target-side representation of integral space diagonal through paired Gaussian norms:

\[
\operatorname{sf}(A)=\operatorname{sf}(B),
\]
and split-prime valuation parity explains zero density when going from Stage18 to Stage19.

For the Stage17-to-Stage19 transition, however, **space integrality is already part of every source object**. Therefore the paired-norm squareclass condition is useful as a coordinate description of the target but cannot be charged again as the new Stage23 thinning event.

```text
STAGE19_SQUARECLASS_TARGET_DESCRIPTION_REUSABLE=true
STAGE19_SPACE_SQUARECLASS_CHARGED_AS_NEW_STAGE23_COST=false
DOUBLE_CHARGE_CHECK=PASS
```

The new condition in Stage23 is the second-face compatibility inside that already space-integral host.

## 7. Comparison with Stage22: the free-edge mechanism does not transfer unchanged

Stage22 proved that without requiring an integral space diagonal,

\[
M_2(B)/M_1(B)\asymp (\log B)^4/B,
\]
with the polynomial loss localized to replacing the Stage16 order-`B` free complementary edge by a coupled second Pythagorean face.

Stage23 starts later in the condition lattice. Its complementary edge is already constrained by

\[
p^2+z^2=d^2.
\]

Therefore Stage22's phrase “remove the free complementary-edge degree of freedom” is **not** a valid literal causal explanation for Stage23. The Stage23 loss is instead caused by asking the already constrained `z` to participate simultaneously in a second face relation.

This establishes a structural interaction difference between the two arrows

```text
Stage16 -> Stage18
Stage17 -> Stage19
```
without claiming a probabilistic independence/correlation coefficient or a sharp Stage23 ratio order.

## 8. What checkpoint60 still cannot explain

The direct pair-overlap theorem explains qualitative zero density but supplies no effective rate. The inherited Stage14 theorem supplies

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]
but checkpoints40/50 and the eight-branch revalidation still do not identify which exact Stage17-host mechanism pays for that half-power ceiling.

The revalidation clarifies several non-solutions:

- the canonical Stage15 explicit linear ambient lower family is globally killed mod 16 after space integrality is imposed;
- Selmer/positive rank alone does not create integral physical survivors;
- generic Kummer packet geometry is subsumed by the sharper Q06/t64 moving-family boundary;
- the exact moving genus-one target receiver requires a new uniform height/count theorem;
- root-ratio, occupancy and character formulations require new whole-family distribution/cancellation input.

Thus

```text
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
TRUE_TARGET_EXPONENT_IDENTIFIED=false
TARGET_UNBOUNDEDNESS_PROVED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_FOUND=false
MATCHING_HALF_POWER_LOWER_BOUND_FOUND=false
```

## 9. Exactly-two mask boundary

The target is exactly two faces, not at least two. Checkpoint60 does not infer that the three-face exclusion is negligible relative to `N2(B)`, because no Stage19 asymptotic is known. The direct pair-overlap upper inclusion is safe regardless: every exactly-two target lies in a pair-overlap locus.

No third-face or perfect-cuboid nonexistence conclusion is made.

## 10. Causal verdict

The strongest certified Stage23 causal statement is:

```text
TRANSITION=Stage17_exactly_one_face_plus_space -> Stage19_exactly_two_faces_plus_space
SOURCE_STRUCTURE=PYTHAGOREAN_FACE_THEN_PYTHAGOREAN_SPACE_EXTENSION
NEW_CONSTRAINT=ADDITIONAL_CROSS_LEG_PYTHAGOREAN_FACE
SOURCE_HOST_PAIR_OVERLAP_LOWER_ORDER=true
SOURCE_HOST_ZERO_DENSITY_PROVED=true
STRONG_RATE_SOURCE=INHERITED_STAGE14_HALF_POWER_UPPER_BOUND
STRONG_RATE_CAUSALLY_DERIVED_HERE=false
SPACE_SQUARECLASS_DOUBLE_CHARGED=false
STAGE22_FREE_EDGE_CAUSE_TRANSFERS_LITERALLY=false
CURRENT_CERTIFIED_LOWER_FLOOR=N2(B)>=3495_FOR_B>=500000000
UNBOUNDEDNESS_PROVED=false
TRUE_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

The Stage23 transition is therefore qualitatively understood as **pair-overlap thinning inside an already space-integral Pythagorean chain**, while its sharp quantitative order remains open.

## 11. Exit

```text
OLD_DEAD_BRANCH_REVALIDATION_REQUIRED=true
SOURCE_LEVEL_BRANCHES_REVALIDATED=8
MIN_HIGH_VALUE_BRANCHES=8
REVALIDATION_GATE=PASS_MATERIALIZED
REVALIDATION_LEDGER=stages/stage23/23-60/revalidation-ledger.md
CAUSAL_DECOMPOSITION_MATERIALIZED=true
NEW_UPPER_BOUND_IMPROVEMENT=false
NEW_POSITIVE_POWER_LOWER_BOUND=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=70
MERGE_ALLOWED=false
CODEX_REQUIRED=false
NEXT_EXPECTED_COMMAND=Stage23-audit
```