# Stage14-4eh — polynomial-core saturation to exponent-zero centered root discrepancy

## Status

`COMPLETE_POLYNOMIAL_COMMON_CORE_SATURATION_TO_CENTERED_ROOT_DISCREPANCY_RECEIVER`

Consumes batch-local `Stage14-4eg`, merged `Stage14-sH71`, and merged `Stage14-4ef`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering polynomial-core block

Fix a common-core dyadic block

```text
C0=B^(kappa+o(1)),
kappa>=epsilon>0.
```

Stage14-4eg gives the exact candidate-incidence decomposition

```text
R_root=rho(C0)+Delta_root,
rho(C0)=B^(-kappa+o(1)).
```

Let `Omega_can,kappa` denote the canonical-allocation-bearing slope background contributing to this block and let `I_kappa` be its charged-once reciprocal candidate incidence. Because each slope has only `B^o(1)` candidates,

```text
|I_kappa| = |Omega_can,kappa| B^o(1)
```

whenever the block is nonempty at exponent scale.

## 2. Principal mass is strictly power-small

The principal contribution satisfies

```text
sum_{z in I_kappa} rho(C0(z))
 <= |I_kappa| B^(-epsilon+o(1)).
```

Therefore any subsequence whose reciprocal root acceptance remains exponent-zero on this block must satisfy

```text
sum_{z in I_kappa} Delta_root(z)
 = |I_kappa| B^(-o(1))
```

with positive sign after restricting to a further exponent-zero subblock if necessary.

Equivalently the canonical-allocation-conditioned candidate family has an exponent-zero excess over the unit-ratio principal root-line density.

```text
POLYNOMIAL_CORE_PRINCIPAL_ROOT_MASS_POWER_SAVED=true
POLYNOMIAL_CORE_SATURATION_FORCES_POSITIVE_CENTERED_EXCESS=true
CENTERED_ROOT_DISCREPANCY_EXPONENT_ZERO_ON_SATURATING_BLOCK=true
```

No pseudorandomness or independence assumption is used: this is forced by the exact 4eg decomposition and positivity of accepted mass.

## 3. Freeze harmless labels

The following labels remain only `B^o(1)`:

```text
common-core dyadic exponent cell,
root/unit convention,
endpoint/2-primary decoration,
atomic chart,
finite reciprocal candidate index.
```

Hence on a saturating polynomial-core sequence one complete label package can be frozen without fixed-power loss. The modulus value `C0` itself is **not** frozen: it still ranges through a polynomial dyadic interval.

```text
ONE_POLYNOMIAL_CORE_LABEL_PACKAGE_CAN_BE_FROZEN=true
EXACT_C0_VALUE_REMAINS_POLYNOMIAL=true
```

## 4. New live reciprocal receiver

The opaque reciprocal density has now contracted to the signed quantity

```text
D_kappa
 := sum_{z in I_kappa}
      [1_{C0(z)|X0(z)^2+Y0(z)^2} - rho(C0(z))].
```

A square-root-saturating polynomial-core branch requires

```text
D_kappa = |I_kappa| B^(-o(1)).
```

Thus the live problem is no longer raw root-line occupancy but **large positive centered discrepancy against a candidate-correlated polynomial common-core modulus**.

Receiver:

```text
PolynomialCommonCoreCanonicalAllocationCenteredGaussianRootLineDiscrepancy.
```

```text
RECIPROCAL_POLYNOMIAL_CORE_RECEIVER_IS_CENTERED_DISCREPANCY=true
CENTERED_DISCREPANCY_FIXED_POWER_BOUND_PROVED=false
```

## Boundary

```text
STAGE14_4EH=COMPLETE_POLYNOMIAL_COMMON_CORE_SATURATION_TO_CENTERED_ROOT_DISCREPANCY_RECEIVER
POLYNOMIAL_CORE_PRINCIPAL_ROOT_MASS_POWER_SAVED=true
POLYNOMIAL_CORE_SATURATION_FORCES_POSITIVE_CENTERED_EXCESS=true
CENTERED_ROOT_DISCREPANCY_EXPONENT_ZERO_ON_SATURATING_BLOCK=true
EXACT_C0_VALUE_REMAINS_POLYNOMIAL=true
RECIPROCAL_POLYNOMIAL_CORE_RECEIVER_IS_CENTERED_DISCREPANCY=true
CENTERED_DISCREPANCY_FIXED_POWER_BOUND_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ei
```
