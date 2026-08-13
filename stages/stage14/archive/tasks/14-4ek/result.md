# Stage14-4ek — character-energy expansion and concentrated/diffuse modulus dichotomy

## Status

`COMPLETE_CHARACTER_ENERGY_TO_PROJECTIVE_COLLISION_OR_DIFFUSE_NORM_DIVISOR_GRAPH_DICHOTOMY`

Consumes batch-local `Stage14-4ej`, `Stage14-4eh`, merged `Stage14-sH71`, and merged `Stage14-4ef`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Exact fixed-modulus character energy

For one exact polynomial common-core modulus `C`, write

```text
M_C := sum_{z:C0(z)=C} w(z),
A_C(chi) := sum_{z:C0(z)=C} w(z) chi(X0(z)) conjugate(chi(Y0(z))).
```

Define the nonprincipal character energy

```text
E_C := (1/phi(C)) sum_{chi != 1} |A_C(chi)|^2.
```

Because every live candidate has `gcd(C,X0Y0)=1`, multiplicative-character orthogonality gives exactly

```text
E_C
 = sum_{z1,z2:C0=C}
     w(z1)w(z2)
     1_{X1*Y2 == X2*Y1 (mod C)}
   - M_C^2/phi(C).
```

Equivalently the collision congruence is

```text
C | X1*Y2-X2*Y1.
```

Thus the second moment counts **projective ratio collisions modulo the same exact common-core modulus**, not a new independent Gaussian norm condition.

```text
FIXED_C_CHARACTER_ENERGY_PROJECTIVE_COLLISION_IDENTITY_EXACT=true
PROJECTIVE_COLLISION_CONGRUENCE=C_divides_X1Y2_minus_X2Y1
```

## 2. Large fixed-C discrepancy forces character energy, but not automatically saving

Let `D_C` be the centered root discrepancy contribution at modulus `C`. Stage14-4ej and Parseval give by Cauchy--Schwarz

```text
|D_C|^2 <= |I_C| * E_C,
```

where

```text
|I_C|=2^omega(C)=B^o(1).
```

Hence an exponent-zero fixed-C discrepancy forces exponent-zero character/projective-collision energy at the corresponding normalization.

```text
FIXED_C_LARGE_DISCREPANCY_FORCES_LARGE_PROJECTIVE_COLLISION_ENERGY=true
```

However `E_C` includes diagonal pairs, and the congruence uses the same `C` already present in the root selector. No determinant saving, off-diagonal saving, or second-modulus gain is claimed.

```text
PROJECTIVE_COLLISION_DIAGONAL_REMOVED=false
FRESH_DETERMINANT_SAVING_PROVED=false
SECOND_MODULUS_RECHARGE_ALLOWED=false
```

## 3. Exact-modulus concentration versus diffuse support

The polynomial dyadic block contains potentially polynomially many exact values of `C`. It is therefore illegal to freeze one exact modulus merely because the dyadic scale has been frozen.

There are two exponent-level possibilities for a square-root-saturating centered discrepancy sequence.

### Concentrated-modulus branch

A `B^o(1)`-sized collection of exact moduli carries exponent-zero discrepancy mass. Then one exact growing modulus sequence `C=C(B)` can be frozen with only `B^o(1)` loss, and Section 2 reduces the obstruction to its projective collision energy.

```text
CONCENTRATED_MODULUS_BRANCH_REDUCES_TO_PROJECTIVE_COLLISION_ENERGY=true
```

### Diffuse-modulus branch

No `B^o(1)` collection of exact moduli carries exponent-zero discrepancy mass. Then polynomially many correlated moduli are genuinely needed. A second moment at one fixed `C` cannot control the branch.

The live arithmetic graph remains the variable-modulus incidence

```text
C | X0^2+Y0^2,
C=B^(kappa+o(1)),
kappa>0,
```

with `C,(X0,Y0)` reconstructed from the same canonical allocation witness and with the principal density subtracted globally.

Call this receiver

```text
DiffusePolynomialCommonCoreCanonicalAllocationNormDivisorGraphDiscrepancy.
```

```text
DIFFUSE_MODULUS_BRANCH_REMAINS_VARIABLE_NORM_DIVISOR_GRAPH=true
```

This branch is precisely why a naive collision-energy argument is insufficient.

## 4. Updated polynomial-core receiver

The polynomial-core centered-discrepancy obstruction has now split into

```text
A. ConcentratedExactCommonCoreProjectiveCollisionEnergy
or
B. DiffusePolynomialCommonCoreCanonicalAllocationNormDivisorGraphDiscrepancy.
```

Neither branch has a certified fixed-power bound.

```text
POLYNOMIAL_CORE_DISCREPANCY_SPLIT_INTO_CONCENTRATED_OR_DIFFUSE_MODULUS=true
CONCENTRATED_BRANCH_FIXED_POWER_SAVING_PROVED=false
DIFFUSE_BRANCH_FIXED_POWER_SAVING_PROVED=false
```

Together with Stage14-4ei, the complete current arithmetic obstruction is therefore:

```text
LOW C0:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity;

POLYNOMIAL C0, concentrated exact moduli:
  ProjectiveCollisionEnergy;

POLYNOMIAL C0, diffuse exact moduli:
  CanonicalAllocationNormDivisorGraphDiscrepancy.
```

## 5. H decision and next

The allocation H target from 4ef remains open and unchanged. No new reciprocal H is opened at 4ek: the concentrated branch still needs a diagonal/off-diagonal audit, while the diffuse branch still needs an internal persistent-modulus/divisor-graph quantifier check before an immutable theorem contract is frozen.

```text
MAINLINE_ALLOCATION_H_NEEDED=true
MAINLINE_ALLOCATION_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity
NEW_RECIPROCAL_H_NEEDED=false
NEXT_H_NEEDED=false
```

Next internal stage:

```text
Stage14-4el
```

should separate diagonal/proportional projective collisions from genuine off-diagonal mover collisions and, in parallel, test whether the diffuse norm-divisor graph admits a persistent accepted ray/full-exponent mechanism.

## Boundary

```text
STAGE14_4EK=COMPLETE_CHARACTER_ENERGY_TO_PROJECTIVE_COLLISION_OR_DIFFUSE_NORM_DIVISOR_GRAPH_DICHOTOMY
FIXED_C_CHARACTER_ENERGY_PROJECTIVE_COLLISION_IDENTITY_EXACT=true
FIXED_C_LARGE_DISCREPANCY_FORCES_LARGE_PROJECTIVE_COLLISION_ENERGY=true
FRESH_DETERMINANT_SAVING_PROVED=false
POLYNOMIAL_CORE_DISCREPANCY_SPLIT_INTO_CONCENTRATED_OR_DIFFUSE_MODULUS=true
CONCENTRATED_MODULUS_BRANCH_REDUCES_TO_PROJECTIVE_COLLISION_ENERGY=true
DIFFUSE_MODULUS_BRANCH_REMAINS_VARIABLE_NORM_DIVISOR_GRAPH=true
CONCENTRATED_BRANCH_FIXED_POWER_SAVING_PROVED=false
DIFFUSE_BRANCH_FIXED_POWER_SAVING_PROVED=false
MAINLINE_ALLOCATION_H_NEEDED=true
NEW_RECIPROCAL_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4el
```
