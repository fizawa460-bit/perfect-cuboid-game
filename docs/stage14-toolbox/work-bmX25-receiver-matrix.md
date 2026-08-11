# Stage14-Work-bmX25 receiver / H-gate matrix

| Route | Current polynomial object | Primitive norm-form form | Projection / density variable | External gate | Cross-promotion |
|---|---|---|---|---|---|
| main/global | canonical allocation density × reciprocal conditional density on primitive slopes | reciprocal branch lifts to `X0^2+Y0^2=C0*m` | canonical-allocation-bearing primitive slope `omega` | mainline H not yet opened | forbidden |
| s | conditional primitive Gaussian root density | `X0^2+Y0^2=C0*m`, `gcd(X0,Y0)=1` | density inside canonical allocation background | `Stage14-sH71` | forbidden |
| fixed-U t | canonical-LPF projected primitive norm-form physical support | `Q=ell*(u^2+v^2)`, `gcd(u,v)=1` | outer canonical-LPF scalar `Q` support | `Stage14-tH28` | forbidden |

## Common structural result

Both theorem-ready route gates belong to the formal class

```text
ProjectedPrimitiveGaussianNormFormPhysicalIncidence.
```

The common facts are:

```text
COMMON_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_LANGUAGE_PROVED=true
COMMON_PROJECTED_SUPPORT_NOT_INNER_FIBER_PRINCIPLE_PROVED=true
COMMON_GAUSSIAN_SPLITTING_RECHARGE_FORBIDDEN=true
COMMON_FINITE_FIBER_RECHARGE_FORBIDDEN=true
```

## Non-identifications

The common formal class is not an arithmetic adapter.

```text
s outer background = canonical primitive slope / allocation family
s distinguished divisor = C0
s quotient = m
s projection = omega

t outer background = canonical-LPF Q family
t distinguished factor = ell=LPF(Q)
t norm value = Q/ell
t projection = Q
```

No merged theorem identifies these data or their physical measures.

```text
COMMON_ARITHMETIC_NORM_FORM_ADAPTER_PROVED=false
GLOBAL_FIXED_U_BACKGROUND_MEASURES_IDENTIFIED=false
GLOBAL_FIXED_U_PROJECTION_VARIABLES_IDENTIFIED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## H decisions

```text
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=true
S_ROUTE_H_REQUEST=Stage14-sH71
S_ROUTE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_H_BLOCKING=true
FIXED_U_H_NEEDED=true
TH28_NEEDED=true
T_ROUTE_H_REQUEST=CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion
T_ROUTE_H_TARGET=stages/stage14/14-t108/th28-target.md
T_ROUTE_H_BLOCKING=true
COMMON_H_THEOREM_FAMILY_RADAR_CAN_BE_SHARED=true
COMMON_H_AUDIT_MERGE_ALLOWED=false
```

The two audits may survey overlapping theorem families (Gaussian/Kloosterman dispersion, large sieve for roots of `-1`, norm-form sieve, bilinear congruence incidence), but applicability must be proved separately against each immutable route contract.

## Charged-once warning

The norm-factor lift

```text
C0 | X0^2+Y0^2
<=>
exists integer m>0: X0^2+Y0^2=C0*m
```

is a re-expression. The quotient `m` is not a new independently chargeable support length. Likewise Gaussian root orientation and finite representation fibers have already been charged.

## Current exponent

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

Next integrated target:

```text
ProjectedPrimitiveNormFormPhysicalIncidenceTheoremIntersectionOrNoGo
```

Normal revisit:

```text
merged 4eb + merged sH71 + merged tH28
```

or an earlier material theorem/adapter trigger.
