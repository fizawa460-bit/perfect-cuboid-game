# Stage14-s6-10 — active-direction obstruction and s6 method closure

## Purpose

Merged Stage14-s6-09 closed the fixed-direction analytic problem.  For a fixed primitive partner face `F2`, the transferred physical partners `F3` lie in one fixed squareclass of the merged t36 quartic, hence there are only `B^o(1)` of them in the polynomial-height window.

Merged Stage14-4bm independently localizes the remaining main-track family to

```text
X2 > B^(20/21),
X2_cross < B^(4/21),
q_ij >> B^(4/21)
```

for at least one good half-angle gcd cell, together with the normalized same-kernel condition from merged s6-08.  The cross-prime branch is already bounded by `B^(61/63+o(1))`.

The remaining question is therefore no longer how many physical partners occur in one direction.  It is how many primitive directions admit even one admissible partner.

This stage audits whether the direct post-local small-point architecture developed in s6 still contains an unused fixed-power mechanism for that active-direction count.  The answer is negative: the available fiber, gcd-cell, squareclass, and local-solubility information is compatible with a large matching of active directions and therefore cannot itself force power sparsity of the direction set.

The stage closes the s6 method at this boundary.  A further improvement requires a qualitatively new family-level theorem about the distribution of the first nonboundary bounded-height point across the moving direction family.

No external theorem is introduced here.

---

## 1. Merged inputs

We use only merged results.

### 1.1 s6-09 fixed-direction theorem

For a fixed primitive `F2` with half-angle parameters `0<a<b`, the transferred physical `F3` slope `x=c/d` satisfies

```text
F_ab(c,d) = -Delta0,
Delta0=square>0,
```

where

```text
F_ab(p,q)
=(b^2*p^2-a^2*q^2)(b^2*q^2-a^2*p^2).
```

Merged t36 therefore gives

```text
# {physical transferred F3 for fixed F2} <= B^o(1).
```

If `A_phys(B)` is the number of active primitive partner directions and `E_phys(B)` the ordered physical-edge count, then

```text
A_phys(B) <= E_phys(B) <= A_phys(B)*B^o(1).
```

Hence they have the same power exponent.

### 1.2 4bm residual localization

Merged 4bm gives

```text
X2<=B^(20/21)               -> B^(20/21+o(1)),
X2_cross>=B^(4/21)          -> B^(61/63+o(1)).
```

The unresolved family has

```text
X2>B^(20/21),
X2_cross<B^(4/21),
q_ij >> B^(4/21)
```

for one good gcd cell and satisfies the normalized s6-08 squareclass/kernel condition.

Call the set of active `F2` directions in this residual family `A_res(B)`.

Then the current physical count has the exact exponent ledger

```text
E_phys(B)
<< B^(20/21+o(1))
 + B^(61/63+o(1))
 + A_res(B)*B^o(1).                      (10.1)
```

---

## 2. The target curve is globally soluble for every direction

For a fixed direction `0<a<b`, define

```text
C^-_{a,b}: y^2 = -f_ab(x),

f_ab(x)
=(b^2*x^2-a^2)(b^2-a^2*x^2).
```

There is a universal rational point

```text
x=0,
y=ab,
```

because

```text
-f_ab(0)=a^2*b^2.
```

Thus every direction curve `C^-_{a,b}` is already rationally soluble.

The physical transferred partners are not detected by mere solubility.  They correspond to additional nonboundary rational points with positive primitive slope `x=c/d`, the Stage14 height restrictions, and the reconstructed physical cutoff.

Consequently the following cannot by themselves reduce the active-direction count:

- local solubility of `C^-_{a,b}`;
- global solubility of `C^-_{a,b}`;
- existence of one rational point on `C^-_{a,b}`;
- Selmer support whose only role is to certify solubility.

The active-direction problem is a **first nonboundary bounded-height point** problem, not a solubility problem.

```text
UNIVERSAL_BOUNDARY_RATIONAL_ANCHOR=true
DIRECTION_CURVE_GLOBAL_SOLUBILITY_AUTOMATIC=true
GLOBAL_SOLUBILITY_FILTER_CAN_SAVE_ACTIVE_DIRECTIONS=false.
```

---

## 3. Fixed-fiber multiplicity is already at its power-scale floor

Write

```text
R(F2;B)
=# {admissible physical partners F3 attached to F2}.
```

Merged s6-09 gives

```text
R(F2;B)<=B^o(1).
```

For active directions `R(F2;B)>=1`.  Therefore

```text
E_phys(B)=sum_F2 R(F2;B)
```

and

```text
A_phys(B)
<=E_phys(B)
<=A_phys(B)B^o(1).
```

No stronger estimate of the form

```text
R(F2;B)<=B^{-delta}
```

is meaningful on an active integral count, because `R>=1` there.

Hence any method whose only new output is a stronger upper bound on `R(F2;B)` cannot improve the power exponent once `B^o(1)` has been reached.

```text
FIXED_FIBER_MULTIPLICITY_AT_POWER_SCALE_FLOOR=true.
```

---

## 4. Why collision energy cannot force active-direction sparsity

The t36/s6-09 collision-energy mechanism proves that repeated points in one direction are rare.  It does not prove that many direction fibers are empty.

Abstractly, consider a bipartite graph with `N` left vertices and `N` right vertices forming a perfect matching.  Then

```text
maximum degree = 1,
collision energy = N,
number of active left vertices = N,
number of edges = N.
```

Thus even the strongest possible bounded-degree statement is compatible with every direction being active.

The s6 residual graph may of course have additional arithmetic structure, but that structure must be used **across directions**.  Fixed-fiber Cauchy, squareclass energy, or point multiplicity alone cannot supply the missing exponent.

```text
SUBPOLYNOMIAL_DEGREE_IMPLIES_ACTIVE_VERTEX_SAVING=false
FIXED_FIBER_COLLISION_ENERGY_IMPLIES_ACTIVE_VERTEX_SAVING=false.
```

---

## 5. Why the large good gcd cell is not a direction-only rarity condition

In the unresolved 4bm branch, one actual physical edge has a good cell

```text
q_ij >> B^(4/21).
```

Each cell is a gcd between one half-angle coordinate of `F2` and one half-angle coordinate of its actual partner `F3`.

Therefore `q_ij` is **edge data**, not an invariant attached to `F2` alone.

Projecting away the partner `F3` leaves only the weak statement that one half-angle coordinate of `F2` possesses a divisor of size at least `B^(4/21)`.  That statement is not rare: a large half-angle coordinate itself is such a divisor.

The useful information is that the same divisor occurs in the corresponding coordinate of an actual target-class partner.  Recovering a saving from that fact requires an average theorem coupling many different `F2` directions and their admissible partners.  It cannot be obtained by recharging the gcd divisor inside one already-controlled fiber.

Merged s6-08 additionally proves that the good gcd-cell product is an automatic square factor of the raw cross-square detector, so the same divisor cannot be charged again as an independent square-sieve modulus.

```text
LARGE_GOOD_CELL_IS_EDGE_RELATIVE=true
LARGE_GOOD_CELL_DIRECTION_ONLY_PROJECTION_POWER_SPARSE=false
RAW_GCD_CELL_SAVING_RECHARGE_ALLOWED=false.
```

---

## 6. Residual active-direction ledger

Equation (10.1) isolates the remaining quantitative receiver.

Any theorem

```text
A_res(B) << B^(41/42-delta+epsilon),
delta>0,
```

would give the first whole-family post-local improvement, until another sector becomes dominant.

The first existing ceiling is the merged 4bm cross branch

```text
B^(61/63+o(1)).
```

Since

```text
41/42 - 61/63 = 1/126,
```

an active-direction saving of at least `1/126` would lower the whole-family exponent to the cross-branch ceiling `61/63`.

But even that is still far above the square-root scale:

```text
61/63 - 1/2 = 59/126.
```

Likewise the small-partner-leg sector

```text
B^(20/21+o(1))
```

is itself above `B^(1/2+o(1))` by

```text
20/21 - 1/2 = 19/42.
```

Therefore a future square-root theorem would have to sharpen **all** remaining sectoral ceilings, not merely solve `A_res(B)`.

---

## 7. What s6 has actually completed

The s6 route began with the post-local question:

> among locally admissible cover states, how many contain a bounded-height global physical point?

It has now established the following chain.

1. exact primitive global witness equation and two-quadrics normal form;
2. physical compact torsion normalization;
3. exact second-face half-angle denominator and square-cancellation formulas;
4. third primitive Pythagorean face transfer;
5. dual half-angle gcd matrix and root-sign no-go;
6. extraction of the automatic gcd-square resonance;
7. normalized same-kernel collision;
8. exact identification with the merged t36 fixed-direction quartic;
9. `B^o(1)` physical partner multiplicity for each fixed direction;
10. reduction of the remaining power exponent to an active-direction sparsity problem.

Every attempted within-fiber source of a new fixed power has now either been proved and exhausted or shown to be algebraically resonant.

---

## 8. Method closure

The remaining theorem has the form

> count primitive moving directions `F2` for which there exists at least one nonboundary bounded-height rational point on `C^-_{a,b}` satisfying the exact physical reconstruction and large-good-cell residual conditions.

This is a family-level first-point distribution theorem.  It is not a further local sieve optimization, fixed-cover point count, fixed-direction squareclass energy estimate, or raw gcd incidence estimate.

Accordingly Stage14-s6 is closed at this boundary.

Reopening s6 is justified only if one of the established reductions is found incorrect.  A new family-average theorem for active directions belongs to a qualitatively new route.

The natural handoff is

```text
Stage14-s7-00
```

with the initial task:

```text
select a moving-direction first-nonboundary-point architecture
for the family C^-_{a,b}, retaining the exact physical cutoff
and the 4bm residual decomposition.
```

---

## Boundary

```text
STAGE14_S6_10=COMPLETE_ACTIVE_DIRECTION_OBSTRUCTION_AND_S6_METHOD_CLOSURE
MERGED_S6_09_FIXED_DIRECTION_FIBER_BOUND_IMPORTED=true
MERGED_4BM_RESIDUAL_LOCALIZATION_IMPORTED=true
UNIVERSAL_BOUNDARY_RATIONAL_ANCHOR=true
DIRECTION_CURVE_GLOBAL_SOLUBILITY_AUTOMATIC=true
GLOBAL_SOLUBILITY_FILTER_CAN_SAVE_ACTIVE_DIRECTIONS=false
FIXED_FIBER_MULTIPLICITY_AT_POWER_SCALE_FLOOR=true
SUBPOLYNOMIAL_DEGREE_IMPLIES_ACTIVE_VERTEX_SAVING=false
FIXED_FIBER_COLLISION_ENERGY_IMPLIES_ACTIVE_VERTEX_SAVING=false
LARGE_GOOD_CELL_IS_EDGE_RELATIVE=true
RAW_GCD_CELL_SAVING_RECHARGE_ALLOWED=false
RESIDUAL_ACTIVE_DIRECTION_RECEIVER_DEFINED=true
ACTIVE_DIRECTION_SAVING_TO_REACH_CROSS_CEILING=1/126
CROSS_SECTOR_CURRENT_EXPONENT=61/63
CROSS_SECTOR_GAP_TO_SQRT=59/126
SMALL_PARTNER_LEG_CURRENT_EXPONENT=20/21
SMALL_PARTNER_LEG_GAP_TO_SQRT=19/42
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
S6_METHOD_CLOSED=true
S6_SUBSTAGE_SPLIT_REQUIRED=false
NEXT=Stage14-s7-00
```
