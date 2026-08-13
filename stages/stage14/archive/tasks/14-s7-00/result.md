# Stage14-s7-00 — family first-nonboundary-point architecture

## Purpose

Merged Stage14-s6-10 closes the direct post-local small-point method at the active-direction barrier.  The remaining problem is no longer to count points inside one fixed direction fiber.  It is to count how many primitive partner directions possess even one **nonboundary bounded-height rational point** satisfying the exact physical reconstruction.

Merged Stage14-4bn sharpens the same object: physical ordered edges with `d<=B` are in bijection with B-admissible positive cross-square pairs `(F2,F3)`, with exact reconstructed cutoff

```text
gcd(H,X2)*H3 <= B.
```

For a fixed primitive partner direction `F2`, merged t36 / s6-09 gives only `B^o(1)` admissible partners.  Therefore the physical edge count and the active-direction count have the same power exponent.

Stage14-s7 begins a qualitatively new route.  It does **not** reopen fixed-fiber square sieves, local 2-descent, or raw gcd-cell density.  Instead it organizes the moving direction curves themselves as a one-parameter genus-one / elliptic family and asks a prior structural question:

> after the universal boundary point and all generic torsion/sections are removed, is physical activation an exceptional specialization event, or does the family already carry a generic nonboundary section?

That generic-section audit is mandatory.  A rank-jump or first-small-point density theorem is meaningful only after the generic Mordell-Weil group of the exact base-changed family is known.

No generic Mordell-Weil rank is asserted in this stage.

---

## 1. Frozen merged input

### 1.1 s6 closure

Merged s6-10 gives

```text
S6_METHOD_CLOSED=true,
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42.
```

It also isolates the residual active-direction count `A_res(B)` through

```text
E_phys(B)
 << B^(20/21+o(1))
  + B^(61/63+o(1))
  + A_res(B)*B^o(1).                     (7.00.1)
```

The first two terms are already controlled sectors.  The third is the only unresolved s-side term.

### 1.2 exact physical-pair converse

Merged 4bn proves

```text
physical ordered edge d<=B
<->
B-admissible positive cross-square pair (F2,F3).
```

Thus the active-direction receiver is not an arbitrary global-solubility majorant.  It is an exact physical counting object.

### 1.3 fixed-fiber theorem

For fixed primitive `F2`, merged t36/s6-09 gives

```text
# {admissible physical F3 attached to F2} <= B^o(1).
```

Hence if `A_phys(B)` is the number of active primitive `F2` directions,

```text
A_phys(B) <= E_phys(B) <= A_phys(B)*B^o(1).   (7.00.2)
```

Any future power saving must therefore reduce the number of **active base directions**, not merely the point multiplicity in one fiber.

---

## 2. Exact direction curve

Let the primitive partner face `F2` have half-angle coordinates

```text
0<a<b,
gcd(a,b)=1,
```

with the finite two-adic type `kappa in {1,2}` absorbed as usual:

```text
H2-S2 = kappa*a^2,
H2+S2 = kappa*b^2,
X2     = kappa*a*b.
```

Merged s6-09 identifies the transferred partner slope `x=c/d` with the quartic

```text
F_ab(c,d)
 = (b^2*c^2-a^2*d^2)
   (b^2*d^2-a^2*c^2)
 = - square.
```

After division by `d^4`, define

```text
f_ab(x)
 = (b^2*x^2-a^2)
   (b^2-a^2*x^2).
```

The moving direction curve is

```text
C^-_{a,b}: y^2 = -f_ab(x).               (7.00.3)
```

It has the universal rational boundary point

```text
(x,y)=(0,ab).
```

That point exists for every direction and is not a physical positive partner.  Thus rational solubility of (7.00.3) is automatic and cannot be used as an activation sieve.

---

## 3. Remove the irrelevant scale: Jacobi normalization

Put

```text
r = a/b,
u = (b/a)*x,
v = y/(a*b).
```

Then direct substitution gives the exact normalized family

```text
boxed:
v^2 = (1-u^2)(1-r^4*u^2).                (7.00.4)
```

Thus the isomorphism class depends only on the rational direction ratio `r=a/b`, and specifically through the fourth-power parameter

```text
lambda = r^4.
```

The universal boundary point becomes

```text
(u,v)=(0,1).                               (7.00.5)
```

The four branch points are

```text
u = +/-1,
nu = +/-r^(-2),                            (7.00.6)
```

and are rational over `Q(r)`.  They form the obvious boundary / two-torsion locus after an origin is chosen.

The crucial warning is that the parameter is not a generic independent `lambda`; Stage14 lies on the fourth-power base change

```text
lambda=r^4.
```

A generic Mordell-Weil computation on the unpulled-back Legendre/Jacobi family is therefore insufficient.  New sections may appear after this base change.

```text
DIRECTION_FAMILY_JACOBI_NORMALIZATION_EXACT=true
JACOBI_PARAMETER_IS_FOURTH_POWER_BASE_CHANGE=true.
```

---

## 4. Exact Legendre-type degree-two quotient

From (7.00.4) put

```text
U=u^2,
V=u*v.
```

Then

```text
boxed:
V^2 = U(1-U)(1-r^4*U).                    (7.00.7)
```

Call this elliptic curve over `Q(r)`

```text
L_r: V^2=U(1-U)(1-r^4 U).
```

The map

```text
C^-_r -> L_r,
(u,v)  -> (u^2,u*v)
```

is generically degree two.  It is **not** declared birational.

The physical lift retains extra information:

- `U` must be a rational square `u^2`;
- the point must lift to the chosen Jacobi sheet;
- branch/boundary points are excluded;
- the primitive partner `F3` conditions are retained;
- the exact reconstructed cutoff from 4bn is retained.

Therefore a theorem about rational points on `L_r` alone is only a majorant until the square-`U` lift and physical cutoff are put back.

```text
LEGENDRE_TYPE_DEGREE_TWO_QUOTIENT_EXACT=true
LEGENDRE_MODEL=V^2=U(1-U)(1-r^4*U)
PHYSICAL_POINT_REQUIRES_SQUARE_U_LIFT=true.
```

---

## 5. Base-height scale and exact exponent translation

From

```text
H2 = kappa*(a^2+b^2)/2,
```

the natural direction height is

```text
T=max(a,b) asymp sqrt(H2).
```

On the physical range `H2<=B`,

```text
T <= C*sqrt(B),
B asymp T^2                                  (7.00.8)
```

on dyadic boxes.

The ambient primitive direction count is therefore of order `T^2`, matching the order-`B` ambient Pythagorean-face count.

The current whole-family exponent translates as

```text
B^(41/42) = T^(41/21).                      (7.00.9)
```

The merged 4bm cross-sector ceiling translates as

```text
B^(61/63) = T^(122/63).                     (7.00.10)
```

Hence the first useful active-direction improvement needs only

```text
41/21 - 122/63 = 1/63                       (7.00.11)
```

of saving on the `T` scale.

The square-root target is

```text
B^(1/2)=T,                                  (7.00.12)
```

so reaching it from the current `T^(41/21)` bound requires

```text
41/21 - 1 = 20/21                           (7.00.13)
```

of additional base-scale saving.

This distinction is important:

- `1/63` on `T` scale is enough to reach the next already-proved ceiling `61/63`;
- `20/21` on `T` scale is required to reach the full square-root upper-bound scale.

---

## 6. The first mandatory gate: generic sections

The universal anchor proves every fiber is globally soluble.  Therefore the first structural question is the generic Mordell-Weil group after choosing a rational origin on the Jacobi/Legendre family.

Stage14-s7 must determine over `Q(r)`:

1. the exact Jacobian / Weierstrass model of `C^-_r`;
2. the singular fibers and discriminant after the fourth-power base change;
3. the complete generic torsion subgroup;
4. the generic Mordell-Weil rank;
5. every generic rational section of polynomial height;
6. which generic sections correspond only to boundary/degenerate points;
7. whether any generic nonboundary section can satisfy the physical square-`U` lift and reconstructed cutoff on a Zariski-open set of directions.

Until these are known, it is invalid to call the active set a rank-jump set.

```text
GENERIC_MORDELL_WEIL_GROUP_AUDITED=false
GENERIC_NONBOUNDARY_SECTIONS_CLASSIFIED=false
S7_GENERIC_SECTION_AUDIT_IS_MANDATORY=true.
```

---

## 7. The two branches after the generic-section audit

### Case G0 — no generic physical nonboundary section

Suppose the generic section group, after removing torsion/boundary sections, contributes no physical nonboundary point.

Then an active direction must be an exceptional specialization carrying an additional rational point of the required small height.  The correct target becomes a **small specialization-rank-jump / first-small-point** set:

```text
R_small(T)
 = #{primitive a,b with max(a,b)<=T:
     C^-_{a/b} has a nonboundary physical point
     in the Stage14 height/cutoff window}.
```

The first quantitative goal is

```text
R_small(T) << T^(41/21-delta_T+epsilon),
delta_T>0.                                  (7.00.14)
```

Any `delta_T>0` is a new whole-family improvement beyond s6.  `delta_T>=1/63` reaches the current `61/63` cross-sector ceiling.

### Case G+ — generic nonboundary sections exist

If a generic nonboundary section exists, one must not immediately conclude that most directions are physically active.

Each generic section must be classified against:

- the Jacobi square-`U` lift;
- positivity and primitive partner conditions;
- branch/boundary exclusions;
- reconstructed first face;
- exact cutoff `gcd(H,X2)*H3<=B`;
- the physical point-height window.

If every generic section fails one of those conditions generically, the residual activation problem may still reduce to Case G0 after removing the generic sections.

If at least one generic section is physically admissible on a Zariski-open set with the required height scale, then active-direction power sparsity is false for structural reasons and the Stage14 counting model must pivot rather than trying to prove a nonexistent sparsity theorem.

---

## 8. Route comparison for s7

### Route A — generic Mordell-Weil / section classification first

Status: **selected mandatory first step**.

Reason: it decides whether the desired active-direction sparsity theorem is even structurally possible.

```text
S7_PRIMARY_GATE=GENERIC_MORDELL_WEIL_AND_SECTION_CLASSIFICATION.
```

### Route B — plain positive-rank density

Status: **not primary**.

Even in Case G0, positive rank alone does not imply a physical point below `B`.  The s3/s6 height gate remains real.

The useful event is

```text
extra specialization point
+ nonboundary physical lift
+ bounded height / exact cutoff,
```

not rank positivity by itself.

```text
PLAIN_POSITIVE_RANK_DENSITY_PRIMARY=false.
```

### Route C — average Selmer/global solubility

Status: **not primary**.

Every direction already has the universal rational anchor.  Solubility statistics do not detect the second nonboundary point.

```text
PLAIN_GLOBAL_SOLUBILITY_PRIMARY=false.
```

### Route D — continue fixed-fiber squareclass energy

Status: **closed upstream**.

Merged t36/s6-09 is already at the `B^o(1)` multiplicity floor.  Further fixed-fiber improvement cannot reduce the active vertex exponent.

```text
FIXED_FIBER_RECOUNT_PRIMARY=false.
```

### Route E — determinant / rational-point counting on the total surface

Status: **reserved after generic-section removal**.

Once all generic sections and accumulating boundary curves are classified, the two-dimensional total space may be attacked by determinant/height methods on the residual open subset.  Applying such a theorem before removing generic sections risks counting an accumulating section as though it were exceptional.

```text
TOTAL_SPACE_DETERMINANT_RESERVED_AFTER_SECTION_AUDIT=true.
```

### Route F — moving canonical-prime Gaussian spin average from t37

Status: **secondary compatible weapon**.

Merged t37 proves fixed-canonical-prime power saving but leaves the moving-prime sum.  If later t stages prove a moving-prime bilinear/spin theorem, it may provide an independent cross-direction average usable inside s7.

It is not selected as the s7 first gate because it does not answer whether the direction family already carries generic physical sections.

```text
MOVING_CANONICAL_PRIME_SPIN_SECONDARY=true.
```

---

## 9. What Stage14-s7-01 must do

Stage14-s7-01 should be a **generic-fiber geometry audit**, not an exponent optimization stage.

Required outputs:

1. derive an explicit Weierstrass/Jacobian model over `Q(r)` for (7.00.4);
2. verify the exact relation to the Legendre-type quotient (7.00.7);
3. compute discriminant and `j`-invariant and list singular fibers, including `r=0, infinity` and roots of the discriminant;
4. determine whether the surface is rational, K3, or another elliptic-surface type after minimalization/base change;
5. determine generic torsion and generic Mordell-Weil rank using an exact method such as Shioda-Tate / explicit descent / independent specialization bounds;
6. enumerate generic sections and classify boundary versus nonboundary sections;
7. map every nonboundary generic section back through the square-`U` lift and test the physical open set/cutoff;
8. only then choose the s7-02 quantitative theorem.

No claimed rank value should be frozen until this audit is complete.

---

## 10. Boundary

```text
STAGE14_S7_00=COMPLETE_FAMILY_FIRST_NONBOUNDARY_POINT_ARCHITECTURE
S6_METHOD_ACCEPTED_AS_CLOSED=true
MERGED_4BN_PHYSICAL_PAIR_BIJECTION_IMPORTED=true
ACTIVE_DIRECTION_IS_EXACT_PHYSICAL_COUNTING_OBJECT=true
DIRECTION_FAMILY_JACOBI_NORMALIZATION_EXACT=true
JACOBI_PARAMETER_IS_FOURTH_POWER_BASE_CHANGE=true
UNIVERSAL_ANCHOR_NORMALIZES_TO=(0,1)
LEGENDRE_TYPE_DEGREE_TWO_QUOTIENT_EXACT=true
LEGENDRE_MODEL=V^2=U(1-U)(1-r^4*U)
PHYSICAL_POINT_REQUIRES_SQUARE_U_LIFT=true
BASE_HEIGHT_VARIABLE=T=max(a,b)
CURRENT_ACTIVE_DIRECTION_EXPONENT_T=41/21
CROSS_SECTOR_CEILING_EXPONENT_T=122/63
ACTIVE_DIRECTION_SAVING_TO_CROSS_CEILING_T=1/63
SQRT_TARGET_EXPONENT_T=1
ACTIVE_DIRECTION_SAVING_TO_SQRT_T=20/21
GENERIC_MORDELL_WEIL_GROUP_AUDITED=false
GENERIC_NONBOUNDARY_SECTIONS_CLASSIFIED=false
S7_GENERIC_SECTION_AUDIT_IS_MANDATORY=true
S7_PRIMARY_GATE=GENERIC_MORDELL_WEIL_AND_SECTION_CLASSIFICATION
PLAIN_POSITIVE_RANK_DENSITY_PRIMARY=false
PLAIN_GLOBAL_SOLUBILITY_PRIMARY=false
FIXED_FIBER_RECOUNT_PRIMARY=false
TOTAL_SPACE_DETERMINANT_RESERVED_AFTER_SECTION_AUDIT=true
MOVING_CANONICAL_PRIME_SPIN_SECONDARY=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
S7_METHOD_CLOSED=false
S7_PREEMPTIVE_SUBSTAGE_SPLIT=false
NEXT=Stage14-s7-01
```
