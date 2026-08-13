# Stage14-s7-73 — exact principal-density plus centered-discrepancy decomposition

## Status

`COMPLETE_CANONICAL_RECIPROCAL_ROOT_PRINCIPAL_PLUS_CENTERED_DISCREPANCY_DECOMPOSITION`

Consumes batch-local `Stage14-s7-72`, merged `Stage14-sH71`, and merged `Stage14-4ef`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Fixed scale/candidate packet

Freeze one `kappa` scale cell, one canonical allocation type, and one charged-once reciprocal candidate label. The live objects are

```text
omega in Omega_kappa,
(C0(omega),X0(omega),Y0(omega)),
C0=B^(kappa+o(1)),
```

with all original primitive, allocation, range, squarefree/coprime, smooth/rough, root-orientation and chart masks retained.

## 2. Centered root indicator

Let `U(C0)` be the primitive unit-pair residue space modulo `C0` compatible with the frozen local support. Let

```text
rho(C0)
 = |{(x,y) in U(C0): x == i_C y (mod C0)}| / |U(C0)|.
```

On squarefree split support,

```text
rho(C0)=C0^(-1+o(1)).
```

Define exactly

```text
Delta_C0(X,Y)
 := 1_{X == i_C Y (mod C0)} - rho(C0).
```

By construction,

```text
E_{(X,Y) in U(C0)} Delta_C0(X,Y)=0.
```

No assertion is made that the physical candidate sequence samples `U(C0)` uniformly.

```text
CENTERED_ROOT_INDICATOR_DEFINED=true
CENTERING_REFERENCE_MEASURE=primitive_unit_pairs_mod_C0
```

## 3. Exact count decomposition on the physical sequence

Let

```text
N_root(kappa)
 = sum_{omega in Omega_kappa} 1_root(omega).
```

Then identically

```text
N_root(kappa)
 = P_kappa + D_kappa,
```

where

```text
P_kappa
 := sum_{omega in Omega_kappa} rho(C0(omega)),

D_kappa
 := sum_{omega in Omega_kappa}
      Delta_{C0(omega)}(X0(omega),Y0(omega)).
```

This equality is taken before absolute values and does not require independence.

```text
PHYSICAL_ROOT_COUNT_PRINCIPAL_DISCREPANCY_IDENTITY_EXACT=true
INDEPENDENCE_ASSUMED=false
```

## 4. Principal contribution on polynomial C0 cells

For fixed `kappa>0`,

```text
rho(C0)=B^(-kappa+o(1))
```

uniformly inside the dyadic exponent cell. Therefore

```text
P_kappa
 <= |Omega_kappa| B^(-kappa+o(1)).
```

Thus the principal term itself has fixed-power deficit `kappa` relative to that cell.

This is now legal because the principal local density is merely being summed exactly; no equidistribution of the physical sequence is assumed.

```text
POLYNOMIAL_C0_PRINCIPAL_TERM_FIXED_POWER_SMALL=true
POLYNOMIAL_C0_PRINCIPAL_TERM_SAVING=kappa
```

## 5. Small C0 principal contribution

For `kappa=0`,

```text
P_0 <= |Omega_0| B^(-o(1)),
```

which gives no fixed-power deficit. Hence any saving on the small-common-core branch must come from a different physical factor, not from root principal density alone.

```text
SMALL_C0_PRINCIPAL_TERM_FIXED_POWER_SMALL=false
```

## 6. Centered discrepancy is the only reciprocal obstruction on polynomial cells

For every fixed `kappa>0`, if

```text
|D_kappa| <= |Omega_kappa| B^(-delta+o(1))
```

for some fixed `delta>0`, then

```text
N_root(kappa)
 <= |Omega_kappa| B^(-min(kappa,delta)+o(1)).
```

Thus after the exact decomposition the polynomial-common-core reciprocal problem is purely a centered discrepancy problem.

Merged sH71 says no audited theorem currently controls this correlated discrepancy with all masks retained.

```text
POLYNOMIAL_C0_RECIPROCAL_RECEIVER_IS_CENTERED_DISCREPANCY=true
CENTERED_DISCREPANCY_FIXED_POWER_BOUND_PROVED=false
```

## 7. No double charge

The factor `rho(C0)` is the principal mass of the same root-line condition whose centered part is `Delta`; they are not independent savings. Local Gaussian splitting and the frozen root orientation are already included in the reference space and cannot be charged again.

```text
PRINCIPAL_AND_CENTERED_ROOT_TERMS_DOUBLE_CHARGED=false
LOCAL_GAUSSIAN_SUPPORT_RECHARGE_ALLOWED=false
```

## H decision

No new H at s7-73. One more internal saturation decomposition is required to determine whether the small-`C0` and polynomial-`C0` branches are genuinely separate minimal receivers.

```text
S7_73_NEW_AUXILIARY_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
```

## Boundary

```text
STAGE14_S7_73=COMPLETE_CANONICAL_RECIPROCAL_ROOT_PRINCIPAL_PLUS_CENTERED_DISCREPANCY_DECOMPOSITION
CENTERED_ROOT_INDICATOR_DEFINED=true
PHYSICAL_ROOT_COUNT_PRINCIPAL_DISCREPANCY_IDENTITY_EXACT=true
POLYNOMIAL_C0_PRINCIPAL_TERM_FIXED_POWER_SMALL=true
SMALL_C0_PRINCIPAL_TERM_FIXED_POWER_SMALL=false
POLYNOMIAL_C0_RECIPROCAL_RECEIVER_IS_CENTERED_DISCREPANCY=true
CENTERED_DISCREPANCY_FIXED_POWER_BOUND_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_73_NEW_AUXILIARY_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
REMAINING_RECEIVER=SmallCommonCoreCanonicalAllocationSurvivorOrPolynomialCommonCoreCenteredRootDiscrepancy
NEXT=Stage14-s7-74
```
