# Stage14-4dw — fixed-prime primitive divisor-pair mass reduction

## Status

`COMPLETE_FIXED_PRIME_STATE_TO_PRIMITIVE_DIVISOR_PAIR_MASS_REDUCTION`

Consumes merged `Stage14-4dv`, merged `Stage14-s7-62`, merged `Stage14-Work-biX21`, merged `Stage14-t102`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering fixed-prime receiver

Merged `4dv` removes the tautological pair-collision energy and leaves, on a square-root-saturating range-stable arithmetic subfamily, one fixed Gaussian mover prime

```text
ell_*=B^o(1)
```

carrying `B^(1/2-o(1))` weighted state mass. On the plus branch the local arithmetic graph is

```text
r s = y,
r^2+s^2 = 2 ell_* x,
```

with all balanced/range/chart/primitive/reciprocal-completion masks retained.

## 2. The cofactor state is reconstructed from one divisor pair

For fixed `ell_*`, the equations give exactly

```text
y = r s,
x = (r^2+s^2)/(2 ell_*).
```

Thus `(x,y)` is not an additional free arithmetic coordinate once `(r,s)` is fixed. The map

```text
(r,s) -> (x,y)
```

has `O(1)` ambiguity after the charged-once ordering/sign convention (`r<s`, positive branch) and the already retained endpoint convention.

Therefore the heavy fixed-prime state mass may be counted directly on the divisor-pair variables.

```text
FIXED_ELL_PLUS_STATE_RECONSTRUCTED_FROM_DIVISOR_PAIR=true
FIXED_ELL_STATE_TO_DIVISOR_PAIR_FIBER=O1
STATE_MASS_AND_DIVISOR_PAIR_MASS_EQUIVALENT_UP_TO=Bo1
```

## 3. Primitive content of the pair

Write

```text
r=D-A,
s=D+A.
```

Then

```text
gcd(r,s) | 2 gcd(D,A).
```

On the retained primitive interior packet, all fixed common content is already separated into the existing primitive/gcd cells. Hence after absorbing the allowed 2-primary and frozen gcd decoration, the live odd parts of `r,s` are coprime up to `B^o(1)` bookkeeping.

This is not a new saving; it only gives the correct primitive divisor-pair receiver.

```text
ODD_DIVISOR_PAIR_COPRIME_AFTER_FROZEN_GCD_DECORATION=true
PRIMITIVE_GCD_DECORATION_NEW_FIXED_POWER_SAVING=false
```

## 4. Fixed Gaussian root congruence

Because

```text
r^2+s^2 = 2 ell_* x
```

and the live mover prime is coprime to the frozen pair outside the already-separated exceptional support, reduction modulo `ell_*` gives

```text
r^2 + s^2 == 0 (mod ell_*).
```

For `s` invertible modulo `ell_*`, this is

```text
(r s^{-1})^2 == -1 (mod ell_*).
```

Since `ell_*` is Gaussian split, there are exactly two root orientations

```text
r == + i_* s (mod ell_*),
r == - i_* s (mod ell_*),
```

with `i_*^2 == -1 (mod ell_*)`.

Thus the fixed-prime plus graph is a primitive divisor-pair family in one of two fixed Gaussian root residue classes.

```text
FIXED_ELL_GAUSSIAN_ROOT_CONGRUENCE_EXPLICIT=true
FIXED_ELL_ROOT_ORIENTATION_COUNT=2
```

## 5. Why this still gives no fixed-power saving

Merged `s7-62` / `Work-biX21` give

```text
ell_*=B^o(1).
```

Therefore imposing one residue class modulo `ell_*` costs at most a subpolynomial factor. It does not create a modulus of size `B^delta`, and the Gaussian split/root condition is the same local arithmetic already used to identify the mover prime.

Hence neither the fixed-prime divisibility nor the two root classes may be charged as a fresh fixed-power loss.

```text
FIXED_ELL_ROOT_CONGRUENCE_FIXED_POWER_SAVING=false
FIXED_ELL_GAUSSIAN_CONDITION_DOUBLE_CHARGE_ALLOWED=false
```

## 6. Minus branch

The minus-state divisor graph from merged `s7-62` is

```text
ell_*^2 a^2 + b^2 = 2x,
a b = y
```

or its swapped form. Once `(a,b)` and `ell_*` are fixed, `(x,y)` is again reconstructed with `O(1)` ambiguity. Thus the minus branch has the same structural conclusion: fixed-prime state mass is equivalent to mass on a primitive low-degree divisor-pair graph, not to a higher-dimensional state family.

```text
FIXED_ELL_MINUS_STATE_RECONSTRUCTED_FROM_DIVISOR_PAIR=true
FIXED_ELL_MINUS_GRAPH_DEGREE_AT_MOST=2
```

## 7. New minimal receiver

The range-stable arithmetic obstruction contracts to

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimePrimitiveDivisorPairPhysicalMaskMass.
```

For the plus branch, equivalently estimate the weighted mass of primitive pairs `(r,s)` satisfying

```text
r<s,
gcd_odd(r,s)=1,
r == +/- i_* s (mod ell_*),
x=(r^2+s^2)/(2ell_*),
y=rs,
```

with every original balanced/range/chart/orientation/reciprocal physical mask transported through this reconstruction.

The unresolved issue is now not local congruence sparsity. It is whether the transported physical masks force a genuinely thin subset of this two-variable primitive divisor-pair family.

## 8. H decision

No new H is opened. The next internal task should transport the remaining physical masks explicitly into `(r,s)` (or ratio/scale coordinates) and test whether they reduce to intervals/sectors plus one nontrivial arithmetic condition. External theorem matching is premature until that mask geometry is explicit.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DW=COMPLETE_FIXED_PRIME_STATE_TO_PRIMITIVE_DIVISOR_PAIR_MASS_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FIXED_ELL_PLUS_STATE_RECONSTRUCTED_FROM_DIVISOR_PAIR=true
FIXED_ELL_STATE_TO_DIVISOR_PAIR_FIBER=O1
ODD_DIVISOR_PAIR_COPRIME_AFTER_FROZEN_GCD_DECORATION=true
FIXED_ELL_GAUSSIAN_ROOT_CONGRUENCE_EXPLICIT=true
FIXED_ELL_ROOT_ORIENTATION_COUNT=2
FIXED_ELL_ROOT_CONGRUENCE_FIXED_POWER_SAVING=false
FIXED_ELL_GAUSSIAN_CONDITION_DOUBLE_CHARGE_ALLOWED=false
FIXED_ELL_MINUS_STATE_RECONSTRUCTED_FROM_DIVISOR_PAIR=true
SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_PRIMITIVE_DIVISOR_PAIR_PHYSICAL_MASK_MASS=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimePrimitiveDivisorPairPhysicalMaskMass
```

Next: `Stage14-4dx`.
