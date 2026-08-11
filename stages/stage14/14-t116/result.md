# Stage14-t116 — exceptional-support / generic-orientation split of the physical cofactor core

## Status

`COMPLETE_EXCEPTIONAL_SUPPORT_AND_GENERIC_ORIENTATION_CORE_SPLIT`

Consumes Stage14-t115 on the same batch branch together with merged `Stage14-t91`.

Fix one norm fiber

```text
n=N(gamma)
```

from t115.  Merged t91 defines the packet exceptional support

```text
E_U=rad_odd(2*k0*d*kappa*R*S*A0*B0)
```

and factors

```text
n=n_E*n_G,
n_E=gcd(n,E_U^infinity),
n_G=n/n_E.
```

Up to the finite unit/two-primary convention, primitive Gaussian representations of `n_G` are exactly the Boolean split-prime orientation cube

```text
epsilon in {0,1}^{omega_odd(n_G)}.
```

All exceptional orientation/unit labels above `n_E` form a set

```text
E(n),
|E(n)|=B^o(1).
```

Merged t91 also proves two facts needed here:

1. the primitive-cover mask is automatic after parameterizing by the primitive orientation cube;
2. every genuinely nontrivial **local** interaction of a cofactor prime with fixed packet data is supported on the exceptional support `E_U`.

Accordingly, after enlarging the exceptional label to include the finite unit/two-primary data, the exact ell-independent core can be written

```text
C_U(n;e,epsilon)
 = L_U(n;e) * S_U(n;e,epsilon),
```

where

```text
L_U(n;e) in {0,1}
```

contains all frozen exceptional/local tag, four-cell, denominator and analogous packet interactions, while

```text
S_U(n;e,epsilon) in {0,1}
```

is the remaining global Boolean physical predicate on the generic orientation cube.  In the merged t91 language this global remainder includes reconstructed sign/positivity/canonical-orientation effects and any residual cross-prime condition not localized on `E_U`.

No multiplicativity or bounded Fourier degree of `S_U` is asserted.

Define

```text
w_G(n)=omega_odd(n_G),

sigma_U(n;e)
 := 2^(-w_G(n))
    sum_{epsilon in {0,1}^{w_G(n)}} S_U(n;e,epsilon).
```

After absorbing all O(1) unit labels into `E(n)`, the norm-fiber density from t115 has the exact finite-mixture form

```text
rho_core(n)
 = [sum_{e in E(n)} L_U(n;e) sigma_U(n;e)] / |E(n)|
```

when all exceptional labels have the same generic cube cardinality; equivalently, with the harmless exact O(1) label multiplicities retained, it is the corresponding multiplicity-weighted average.  In either form the exceptional label family has only `B^o(1)` complexity.

Crucially, `|E(n)|=B^o(1)` does **not** make the exceptional-local support analytically irrelevant.  The local predicate may kill every exceptional label for a polynomial family of scalar norms.  What is discharged is only the false idea that the number of exceptional labels itself supplies an independent fixed-power factor.

Thus the Branch-A receiver from t114 splits internally into two possible mechanisms:

```text
ExceptionalLocalAdmissibleNormSupportDeficit
```

or, on locally admissible norms,

```text
GenericSplitPrimeOrientationPhysicalAcceptanceDensityDeficit.
```

```text
PRIMITIVE_MASK_AUTOMATIC_ON_ORIENTATION_CUBE=true
EXCEPTIONAL_GENERIC_ORIENTATION_SPLIT_EXACT=true
EXCEPTIONAL_LABEL_COMPLEXITY=Bo1
LOCAL_FIXED_PACKET_INTERACTIONS_CONFINED_TO_EXCEPTIONAL_SUPPORT=true
GENERIC_ORIENTATION_GLOBAL_BOOLEAN_REMAINS=true
EXCEPTIONAL_LABEL_COUNT_FIXED_POWER_RECHARGE_FORBIDDEN=true
EXCEPTIONAL_LOCAL_NORM_SUPPORT_MAY_STILL_BE_POWER_THIN=true
GENERIC_ORIENTATION_ACCEPTANCE_MAY_STILL_BE_POWER_THIN=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUExceptionalLocalAdmissibleNormSupportOrGenericOrientationPhysicalDensity
NEXT_INTERNAL_TARGET=GenericOrientationPrincipalCenteredAndCoreSavingTrichotomy
NEXT=Stage14-t117
```
