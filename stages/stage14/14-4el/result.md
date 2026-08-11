# Stage14-4el — diagonal/proportional removal in the concentrated projective-collision branch

## Status

`COMPLETE_CONCENTRATED_PROJECTIVE_COLLISION_DIAGONAL_PROPORTIONAL_REMOVAL`

Consumes merged `Stage14-4ek`, merged `Stage14-4ef`, merged `Stage14-Work-bnX26`, and latest main `c6c4136d21bc75bd14a92156d774c680feaa63bb`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed exact-modulus energy

On the concentrated branch freeze one exact polynomial common-core modulus `C` with only `B^o(1)` loss. Use the merged 4ek notation

```text
M_C = sum_z w(z),
E_C = (1/phi(C)) sum_{chi!=1}|A_C(chi)|^2,
```

where the charged-once physical candidate weights satisfy

```text
0 <= w(z) <= B^o(1).
```

Merged 4ek gives exactly

```text
E_C
 = sum_{z1,z2} w(z1)w(z2)
     1_{C | X1*Y2-X2*Y1}
   - M_C^2/phi(C).
```

On an exponent-zero centered-discrepancy subfamily,

```text
|D_C| = M_C B^(-o(1)),
|D_C|^2 <= B^o(1) E_C,
```

so

```text
E_C >= M_C^2 B^(-o(1)).
```

Because a concentrated exact modulus carries polynomial physical mass on a square-root-saturating sequence,

```text
M_C = B^(mu+o(1))
```

for some fixed `mu>0` after a further exponent cell is frozen. A `B^o(1)`-mass exact modulus cannot by itself carry the polynomial branch mass.

```text
CONCENTRATED_SATURATING_EXACT_MODULUS_HAS_POLYNOMIAL_CANDIDATE_MASS=true
```

## 2. Diagonal mass is too small

The literal diagonal contribution is

```text
Diag_C = sum_z w(z)^2 <= B^o(1) M_C.
```

Hence

```text
Diag_C = o_power(M_C^2)
```

on every polynomial-mass concentrated cell.

```text
DIAGONAL_COLLISION_MASS_AT_MOST_M_C_BO1=true
DIAGONAL_COLLISIONS_CANNOT_SUPPORT_EXPONENT_ZERO_ENERGY=true
```

## 3. Exact rational proportional pairs are also finite-fiber

All live primitive reciprocal vectors satisfy

```text
gcd(X0,Y0)=1
```

and the sign/unit convention is already frozen. If

```text
X1*Y2-X2*Y1 = 0,
```

then the two primitive vectors are the same canonical projective vector. The reverse reciprocal / allocation decorations above one fixed primitive vector have only `B^o(1)` charged-once multiplicity by the merged finite-fiber reductions.

Therefore the complete rationally proportional pair mass is bounded by

```text
Prop_C <= B^o(1) M_C.
```

and likewise cannot support `E_C >= M_C^2 B^(-o(1))`.

```text
RATIONAL_PROPORTIONAL_COLLISION_FIBER=Bo1
PROPORTIONAL_COLLISIONS_CANNOT_SUPPORT_EXPONENT_ZERO_ENERGY=true
```

## 4. Genuine off-diagonal collision forced

Remove the diagonal and exact-proportional pairs. A saturating concentrated modulus must retain exponent-zero pair mass on

```text
C | Delta,
Delta := X1*Y2-X2*Y1 != 0.
```

Thus the concentrated polynomial-core obstruction contracts to genuine nonzero determinant collisions.

```text
CONCENTRATED_SATURATION_FORCES_GENUINE_OFF_DIAGONAL_PROJECTIVE_COLLISIONS=true
NONZERO_DETERMINANT_COLLISION_MASS_EXPONENT_ZERO=true
FRESH_DETERMINANT_SAVING_PROVED=false
```

This is a contraction only; `C` is still the same root modulus and cannot be recharged as an independent spacing modulus.

## Boundary

```text
STAGE14_4EL=COMPLETE_CONCENTRATED_PROJECTIVE_COLLISION_DIAGONAL_PROPORTIONAL_REMOVAL
DIAGONAL_COLLISIONS_CANNOT_SUPPORT_EXPONENT_ZERO_ENERGY=true
PROPORTIONAL_COLLISIONS_CANNOT_SUPPORT_EXPONENT_ZERO_ENERGY=true
CONCENTRATED_SATURATION_FORCES_GENUINE_OFF_DIAGONAL_PROJECTIVE_COLLISIONS=true
NONZERO_DETERMINANT_COLLISION_MASS_EXPONENT_ZERO=true
FRESH_DETERMINANT_SAVING_PROVED=false
NEW_RECIPROCAL_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4em
```
