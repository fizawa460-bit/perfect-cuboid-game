# Stage28-60 — mechanism comparison ledger

Stage28 compares two different completions of the same two-face arithmetic environment. Checkpoint40/50 now allow a sharp separation between features that cannot explain a relative exponent and features where a genuine differential remains.

## Common structure — not a differential explanation

The Stage19 space completion and Stage20 third-face completion have, on the audited common toric base,

```text
COMMON_BASE=Y=Bl_4(P1xP1)
COVER_DEGREE=2 for both
TOTAL_BRANCH_CLASS=-2K_Y for both
CANONICAL_COVER_TYPE=K3 for both
LOCAL_SIEVE_DIMENSION=2 for both
HUANG_THIN_COVER_RANGE=eta<1/46 for both
FIRST_ORDER_LOCAL_SIEVE_DIMENSION_DIFFERENCE=0
RELATIVE_LOCAL_POLYNOMIAL_DRIFT=0
RELATIVE_LOCAL_FIRST_ORDER_LOG_DRIFT=0
```

The normalized good-prime local quotient has only a finite positive Euler-product bias after the quadratic-character factor is removed. Therefore none of the known first-order local laws supplies a relative power of `B` or a relative power of `log B`.

Likewise, the common degree-two/K3/`-2K_Y` data and the matched Huang exponent range cannot be subtracted or cancelled to produce a global ratio theorem.

## Genuine structural differences

Checkpoint40-r2 proves

```text
SPACE_BRANCH_PROFILE=4 x genus-0 components
THIRD_FACE_BRANCH_PROFILE=2 x genus-1 components
SAME_QUADRATIC_EXTENSION_OVER_FIXED_BASE=false
BASE_AUTOMORPHISM_IDENTIFICATION=false
```

Thus the two completions are not the same quadratic cover in disguise. This branch-profile / squareclass difference is currently the first certified geometric place where the two marginal problems genuinely diverge.

However checkpoint50-r2 also proves that the four rational geometric space-branch components do not meet the positive physical real torus, so branch rationality itself is not a Stage19 physical lower family.

No theorem currently converts the branch-profile difference into a relative physical-height rational-lift count.

## Different proof strengths are not yet causal laws

The strongest current whole-family source upper is

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

while the target upper remains

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta},\quad \eta<1/46.
\]

This is a difference in certified theorem strength, not proof that the space condition is intrinsically more restrictive than the third-face condition.

The best known constructive floors are also different:

```text
N2 known family exponent=1/4
M3 known family exponent=1/3 with explicit positive liminf coefficient
```

but construction efficiency is a family-level statement and cannot be promoted to a whole-population ordering.

## Current causal boundary

The known local, generic-cover, and construction ledgers do not resolve the direct condition-cost ratio. The surviving relative mechanism is

```text
OPEN_GATE_60=DistinctBranchProfilePhysicalHeightMarginalComparison
COMMON_HOST=two-face toric physical environment under R<=B
REQUIRED_OUTPUT=direct comparison of N2 and M3 marginals, or a theorem assigning a relative power/log-power to the branch-profile difference
ENDPOINT_COUNT_FORBIDDEN=true
```

A valid future theorem may be a branch-sensitive rational-lift comparison, a same-measure dispersion/energy theorem, or a moving-height theorem. It must compare marginals directly and must not consume the perfect-cuboid joint endpoint count.