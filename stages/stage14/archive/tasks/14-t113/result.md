# Stage14-t113 — equidistribution no-go and principal-scale depletion criterion

## Status

`COMPLETE_EQUIDISTRIBUTION_SAVING_NOGO_AND_PRINCIPAL_SCALE_DEPLETION_CRITERION`

Consumes Stage14-t112 on the same batch branch together with merged tH26/tH28 negative theorem boundaries.

For a charged-once cofactor block `Omega`, t112 gives exactly

```text
T_Omega=M_Omega+D_Omega,
T_Omega>=0,
M_Omega>=0,
```

where `M_Omega` is the uniform-projective-class principal mass and `D_Omega` is the physical cofactor-selected centered class discrepancy.

The sign needed for a saving is now explicit.  A standard equidistribution statement of the shape

```text
|Delta_gamma(c)| <= epsilon_B A_gamma,
epsilon_B=o(1),
```

uniformly on the live cofactor background would imply

```text
|D_Omega| <= epsilon_B M_Omega
```

and hence

```text
T_Omega=(1+o(1))M_Omega.
```

Because the projective principal factor is only `1/|G|=B^(-o(1))`, such ordinary equidistribution cannot by itself produce a fixed-power deficit.  It preserves the exponent of the principal mass.

Conversely, if for some fixed `delta>0`

```text
T_Omega <= B^(-delta) M_Omega
```

with `M_Omega>0`, then the exact identity forces

```text
D_Omega
 <= -(1-B^(-delta)) M_Omega.
```

Thus a fixed-power improvement coming from the selected projective class requires **principal-scale negative discrepancy**: the physically selected classes must be systematically depleted relative to their uniform class share.  Small centered discrepancy is not the desired mechanism.

This distinction is important for theorem routing.  Merged tH26 audits Hecke/BV/BDH/large-sieve style equidistribution and already certifies that those tools do not handle the full frozen coefficient system.  Even if a stronger version supplied small discrepancy here, it would only show `T_Omega~M_Omega`, not a new `B^-delta` upper bound unless the principal physical cofactor mass `M_Omega` was already power-small.

Therefore the two logically distinct fixed-U saving mechanisms are now

```text
(A) principal physical cofactor mass M_Omega is fixed-power sparse;
(B) selected projective classes have negative discrepancy comparable to M_Omega.
```

No third saving is available from standalone class density or ordinary class equidistribution.

```text
ORDINARY_PROJECTIVE_EQUIDISTRIBUTION_FIXED_POWER_SOURCE=false
SMALL_CENTERED_DISCREPANCY_PRESERVES_PRINCIPAL_EXPONENT=true
PROJECTIVE_SAVING_REQUIRES_PRINCIPAL_SCALE_NEGATIVE_DISCREPANCY=true
STANDALONE_CLASS_DENSITY_RECHARGE_FORBIDDEN=true
TH26_EQUIDISTRIBUTION_BOUNDARY_CONSUMED=true
TH28_PROJECTED_SUPPORT_BOUNDARY_CONSUMED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUPrimitiveCofactorPrincipalMassOrSelectedClassPrincipalScaleDepletion
NEXT=Stage14-t114
```
