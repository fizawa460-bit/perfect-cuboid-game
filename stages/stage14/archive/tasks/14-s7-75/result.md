# Stage14-s7-75 — concentrated-modulus discrepancy forces off-diagonal projective collision energy

## Status

`COMPLETE_CONCENTRATED_MODULUS_DISCREPANCY_TO_OFFDIAGONAL_PROJECTIVE_COLLISION_ENERGY`

Consumes merged `Stage14-s7-74`, merged mainline `Stage14-4ej/4ek`, merged `Stage14-Work-bnX26`, and latest main at batch start `c6c4136d21bc75bd14a92156d774c680feaa63bb`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Imported exact character-energy identity

On the polynomial-`C0` branch, merged `4ej/4ek` gives for one exact modulus `C`

```text
M_C = total charged-once candidate mass,
A_C(chi)=sum_z w(z) chi(X0(z)) conjugate(chi(Y0(z))),
E_C=(1/phi(C)) sum_{chi!=1}|A_C(chi)|^2,
```

and exactly

```text
E_C
 = sum_{z1,z2:C0=C}
     w(z1)w(z2) 1_{C|X1Y2-X2Y1}
   - M_C^2/phi(C).
```

Also

```text
|D_C|^2 <= |I_C| E_C,
|I_C|=2^omega(C)=B^o(1).
```

All canonical allocation and physical masks remain inside `w`.

## 2. Unit-incidence normalization

The physical candidate multiplicity per primitive slope is `B^o(1)`. Expanding each bounded/subpolynomial charged weight into its underlying candidate incidences changes counts by only `B^o(1)`. Hence on the exponent ledger we may work with unit incidences.

Then the diagonal collision contribution is

```text
K_diag(C)=M_C
```

up to `B^o(1)` distortion in the original weighted model.

```text
UNIT_INCIDENCE_NORMALIZATION_COST=Bo1
DIAGONAL_PROJECTIVE_COLLISION_MASS=M_C_Bo1
```

This is a normalization, not a saving.

## 3. Concentrated discrepancy forces quadratic-scale energy

In the concentrated exact-modulus branch of merged `4ek`, a `B^o(1)` collection of exact polynomial moduli carries exponent-zero centered discrepancy mass. Freezing one such exact modulus with maximal contribution loses only `B^o(1)`. On that sequence,

```text
|D_C| = M_C B^(-o(1)),
M_C = B^(eta+o(1))
```

for some fixed `eta>0`; the second statement follows because the exact modulus carries polynomial-scale mass from a square-root-saturating polynomial background.

Cauchy--Schwarz therefore gives

```text
E_C >= |D_C|^2/|I_C|
    = M_C^2 B^(-o(1)).
```

But the diagonal mass is only

```text
M_C B^o(1)
 = M_C^2 B^(-eta+o(1)),
```

which is fixed-power smaller than the required energy.

Hence diagonal self-pairs cannot support concentrated polynomial-core saturation.

```text
CONCENTRATED_FIXED_C_DISCREPANCY_FORCES_QUADRATIC_CHARACTER_ENERGY=true
DIAGONAL_COLLISIONS_CANNOT_SUPPORT_CONCENTRATED_SATURATION=true
```

## 4. Genuine off-diagonal projective collision mass is mandatory

Let

```text
K_off(C)
 = sum_{z1!=z2:C0=C}
     1_{C|X1Y2-X2Y1}
```

in the unit-incidence model. Since

```text
E_C = K_diag(C)+K_off(C)-M_C^2/phi(C)
```

and `E_C=M_C^2 B^(-o(1))` while `K_diag(C)` is fixed-power smaller, necessarily

```text
K_off(C)=M_C^2 B^(-o(1)).
```

Thus every concentrated exact-modulus saturating sequence contains exponent-zero density of distinct candidate pairs colliding projectively modulo the same growing `C`.

```text
CONCENTRATED_SATURATION_FORCES_OFFDIAGONAL_PROJECTIVE_COLLISION_DENSITY_EXPONENT_ZERO=true
```

No determinant or spacing saving is claimed yet.

## 5. Receiver and next step

The small-`C0` allocation branch and the diffuse polynomial-modulus branch remain unchanged. Only the concentrated polynomial-modulus branch has been contracted from generic character energy to mandatory off-diagonal projective collision mass.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_75_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

The next internal step must split these off-diagonal collisions into exact proportional primitive rays and genuine nonzero determinant multiples of `C`.

## Boundary

```text
STAGE14_S7_75=COMPLETE_CONCENTRATED_MODULUS_DISCREPANCY_TO_OFFDIAGONAL_PROJECTIVE_COLLISION_ENERGY
MERGED_4EJ_4EK_CHARACTER_ENERGY_IMPORTED=true
UNIT_INCIDENCE_NORMALIZATION_COST=Bo1
CONCENTRATED_FIXED_C_DISCREPANCY_FORCES_QUADRATIC_CHARACTER_ENERGY=true
DIAGONAL_COLLISIONS_CANNOT_SUPPORT_CONCENTRATED_SATURATION=true
CONCENTRATED_SATURATION_FORCES_OFFDIAGONAL_PROJECTIVE_COLLISION_DENSITY_EXPONENT_ZERO=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_75_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-76
```
