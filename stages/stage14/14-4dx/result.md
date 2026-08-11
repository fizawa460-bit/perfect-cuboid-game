# Stage14-4dx — fixed-prime/fixed-root primitive divisor-pair physical-mask transport

## Status

`COMPLETE_PROJECTIVE_SLOPE_MASK_TRANSPORT_NO_FIXED_POWER_DEFICIT`

Consumes merged `Stage14-4dw`, merged `Stage14-s7-63`, merged `Stage14-Work-bjX22`, merged `Stage14-t103`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering receiver

Merged Work-bjX22 localizes any square-root-saturating range-stable arithmetic survivor to

```text
ell_* = B^o(1) fixed,
epsilon_* in {+1,-1} fixed,
r < s,
gcd_odd(r,s)=1,
r == epsilon_* i_* s (mod ell_*),
```

with

```text
x=(r^2+s^2)/(2 ell_*),
y=rs,
```

and `B^(1/2-o(1))` distinct primitive directions `(r:s)` carrying the transported physical masks.

The collision-energy description is already discharged as localization and is not an independent source of saving.

## 2. Projective slope / scale coordinates

Put

```text
t = r/s in (0,1),
q = s.
```

Then

```text
r=tq,
y=rs=t q^2,
x=(r^2+s^2)/(2 ell_*)
  = q^2(1+t^2)/(2 ell_*).
```

Therefore the projective ratio is exactly

```text
x/y = (t+t^(-1))/(2 ell_*).
```

Also, with the complementary-square variables

```text
D=(r+s)/2,
A=(s-r)/2,
```

one has

```text
A/D=(1-t)/(1+t),
D/A=(1+t)/(1-t).
```

Hence every retained condition that depends only on the normalized complementary-square geometry, norm ratios, or angular/interior position transports to a one-variable condition in the projective slope `t`.

```text
PROJECTIVE_SLOPE_COORDINATE_DEFINED=true
NORM_RATIO_MASKS_TRANSPORT_TO_SLOPE=true
COMPLEMENTARY_ANGLE_MASKS_TRANSPORT_TO_SLOPE=true
```

## 3. What the fixed Gaussian root condition becomes

The frozen root orientation is

```text
r == epsilon_* i_* s (mod ell_*),
```

with `i_*^2 == -1 (mod ell_*)`.

Because `gcd(s,ell_*)=1` on the generic primitive branch, this is the fixed projective residue condition

```text
t == epsilon_* i_* (mod ell_*),
```

interpreted in primitive integer representatives `(r,s)` rather than as a real congruence for `t`.

This is one fixed residue line modulo the already frozen subpolynomial prime `ell_*`. Its cost is at most subpolynomial on the Stage14 exponent scale and is already part of the Gaussian mover localization.

```text
FIXED_ROOT_PROJECTIVE_RESIDUE_LINE_PROVED=true
FIXED_ROOT_CONGRUENCE_NEW_FIXED_POWER_SAVING=false
FIXED_ROOT_CONGRUENCE_DOUBLE_CHARGE_ALLOWED=false
```

## 4. Primitive and scale decorations

The primitive condition is

```text
gcd(r,s)=1
```

up to the already frozen 2-primary / endpoint bookkeeping. It removes imprimitive scale copies but does not force the projective image to have sub-square-root cardinality: merged Work-bjX22 already proves that a saturating survivor contains `B^(1/2-o(1))` distinct primitive directions.

The scale variable `q` is then restricted by the original dyadic/range bounds after substituting

```text
x=q^2(1+t^2)/(2 ell_*),
y=tq^2.
```

For fixed `t` inside an interior cell these are ordinary multiplicative intervals in `q`; no merged theorem shows that their allowed length has a fixed-power deficit uniformly in the surviving slope family.

```text
PRIMITIVITY_ALREADY_CHARGED_BY_DIRECTION_REDUCTION=true
SCALE_WINDOW_FIXED_POWER_DEFICIT_PROVED=false
```

## 5. Balanced/interior masks are slope windows, not thin arithmetic sets

On a fixed dyadic Stage14 cell, balanced and interior conditions compare positive quantities built from `x,y,D,A` up to fixed-power constants. After the formulas above, these become finitely many inequalities of the form

```text
F_j(t) in I_j
```

for explicit rational functions `F_j` and fixed cell intervals `I_j`, together with ordinary scale windows in `q`.

Thus on each monotonicity component the accepted slopes form an `O(1)` union of real intervals. Nothing in the merged sources proves that these intervals shrink to width `B^{-delta}`.

Consequently they are archimedean selector masks, not a fresh sparse congruence or a low-cardinality image theorem.

```text
BALANCED_INTERIOR_MASKS_ARE_O1_SLOPE_WINDOWS=true
SLOPE_WINDOW_WIDTH_FIXED_POWER_SMALL_PROVED=false
ARCHIMEDEAN_SLOPE_MASK_GIVES_NEW_POWER_SAVING=false
```

## 6. Remaining nontrivial transport

After freezing

```text
ell_*, epsilon_*,
primitive projective residue line,
```

and transporting norm/angle/balanced/interior constraints to slope/scale coordinates, the only potentially saving content is the **joint occupancy** of these masks with the remaining chart/orientation/reciprocal-completion acceptance inherited from the original physical packet.

These retained selectors are not proved to factor independently in `(t,q)`, and no merged theorem gives a uniform fixed-power density deficit for their intersection along the primitive residue-line family.

Thus the canonical arithmetic obstruction becomes

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimeFixedRootPrimitiveProjectiveSlopeScale
TransportedPhysicalMaskOccupancy.
```

Equivalently, one must bound the mass of primitive lattice directions on one fixed projective residue line modulo `ell_*` whose slope lies in the transported `O(1)` archimedean windows and whose scale passes all remaining physical completion masks.

```text
PHYSICAL_MASK_TRANSPORT_TO_SLOPE_SCALE_COMPLETED=true
ALL_TRANSPORTED_MASKS_INDEPENDENTLY_FACTOR_PROVED=false
TRANSPORTED_MASK_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false
SQRT_OBSTRUCTION_REDUCED_TO_PROJECTIVE_SLOPE_SCALE_MASK_OCCUPANCY=true
```

## 7. H decision

No new H is opened at 4dx. The receiver has only now become a fixed-prime, fixed-root, two-coordinate primitive lattice occupancy problem. Before external theorem matching, the next internal step should identify whether the remaining completion mask is predominantly a function of slope, predominantly a function of scale, or genuinely coupled.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DX=COMPLETE_PROJECTIVE_SLOPE_MASK_TRANSPORT_NO_FIXED_POWER_DEFICIT
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PROJECTIVE_SLOPE_COORDINATE_DEFINED=true
NORM_RATIO_MASKS_TRANSPORT_TO_SLOPE=true
COMPLEMENTARY_ANGLE_MASKS_TRANSPORT_TO_SLOPE=true
FIXED_ROOT_PROJECTIVE_RESIDUE_LINE_PROVED=true
FIXED_ROOT_CONGRUENCE_NEW_FIXED_POWER_SAVING=false
PRIMITIVITY_ALREADY_CHARGED_BY_DIRECTION_REDUCTION=true
BALANCED_INTERIOR_MASKS_ARE_O1_SLOPE_WINDOWS=true
SLOPE_WINDOW_WIDTH_FIXED_POWER_SMALL_PROVED=false
PHYSICAL_MASK_TRANSPORT_TO_SLOPE_SCALE_COMPLETED=true
ALL_TRANSPORTED_MASKS_INDEPENDENTLY_FACTOR_PROVED=false
TRANSPORTED_MASK_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false
SQRT_OBSTRUCTION_REDUCED_TO_PROJECTIVE_SLOPE_SCALE_MASK_OCCUPANCY=true
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4dy`.
