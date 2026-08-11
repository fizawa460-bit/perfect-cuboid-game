# Stage14-Work-bmX25 — projected primitive Gaussian norm-form incidence and dual H gate

## Status

`COMPLETE_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_COMMON_LANGUAGE_WITH_SEPARATE_H_CONTRACTS`

Consumes merged-only Stage14 sources on latest main:

- merged `Stage14-Work-blX24`,
- merged `Stage14-4ea`,
- merged s-batch through `Stage14-s7-71`,
- merged t-batch through `Stage14-t108`,
- the immutable `Stage14-tH28` target frozen by t108.

Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

This Work run is triggered early by two material receiver changes: s7-71 exposes a theorem-ready primitive Gaussian root-density problem and t108 exposes a theorem-ready projected primitive norm-form support problem.

```text
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
```

## 1. Global s-route theorem-ready selector

Merged 4ea and s7-68 reduce the global arithmetic survivor to

```text
mu_G = mu_can * mu_recip,
```

where `mu_can` is canonical balanced integer/Gaussian allocation density on the polynomial primitive-slope background and `mu_recip` is the reciprocal conditional density.

Merged s7-69 removes the first reciprocal equation as a reconstructed identity. Merged s7-70/71 reduce the remaining reciprocal selector to the existence, for one charged-once `B^o(1)` candidate triple, of

```text
C0 | X0^2+Y0^2,
gcd(X0,Y0)=1,
gcd(C0,X0Y0)=1,
```

with the actual canonical-allocation correlation and all physical masks retained.

For every positive candidate this divisibility is exactly equivalent to the existence of a positive integer quotient `m` such that

```text
X0^2+Y0^2 = C0*m.
```

Thus the s-route theorem gate is the projection to the canonical primitive-slope background of a primitive Gaussian norm-factor incidence.

```text
S_ROUTE_ROOT_DIVISIBILITY_LIFTS_TO_NORM_FACTOR_EQUATION=true
S_ROUTE_PROJECTED_PRIMITIVE_NORM_FORM_INCIDENCE=true
S_ROUTE_FIXED_POWER_ROOT_DENSITY_SAVING_PROVED=false
```

This lift is an exact re-expression only. It does not create a new modulus or a new saving, and the quotient `m` may not be charged as an independent support length without a separate theorem.

## 2. Fixed-U t-route theorem-ready support

Merged t108 proves that the fixed-U positive principal obstruction is the projection to `Q` of primitive norm-form witnesses

```text
Q = ell*(u^2+v^2),
gcd(u,v)=1,
ell=LPF(Q),
v_ell(Q)=1,
all odd p|Q => p==1 mod 4,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
```

with all frozen physical linear/congruence/orientation masks retained.

```text
T_ROUTE_PROJECTED_PRIMITIVE_NORM_FORM_INCIDENCE=true
T_ROUTE_ARBITRARY_Q_WEIGHT_RECEIVER_ELIMINATED=true
T_ROUTE_PROJECTED_NORM_FORM_SUPPORT_SAVING_PROVED=false
```

The immutable audit target is `stages/stage14/14-t108/th28-target.md`.

## 3. X25 common structural language

Both live theorem gates are now projections of a primitive sum-of-two-squares incidence with physical masks:

```text
GLOBAL/s:
  X0^2+Y0^2 = C0*m
  -> project to canonical-allocation-bearing primitive slope omega

FIXED-U/t:
  u^2+v^2 = Q/ell
  -> project to canonical-LPF scalar Q
```

The common abstract object is therefore

```text
ProjectedPrimitiveGaussianNormFormPhysicalIncidence.
```

In both routes:

1. the primitive norm variables are coprime;
2. Gaussian split/root data are already physical data and cannot be recharged;
3. finite representation/candidate multiplicities are `B^o(1)` and cannot be recharged;
4. the saving question is a support/density question after projection, not an inner finite-fiber density question;
5. a theorem must retain the actual physical masks and quantifier order.

Hence

```text
COMMON_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_LANGUAGE_PROVED=true
COMMON_PROJECTED_SUPPORT_NOT_INNER_FIBER_PRINCIPLE_PROVED=true
COMMON_GAUSSIAN_SPLITTING_RECHARGE_FORBIDDEN=true
COMMON_FINITE_FIBER_RECHARGE_FORBIDDEN=true
```

## 4. Why the arithmetic adapter is still not proved

The two projected incidences are not the same arithmetic family.

The s-route has:

```text
outer variable: canonical primitive slope / allocation state omega,
modulus: C0 correlated with the same allocation witness,
quotient: m=(X0^2+Y0^2)/C0,
selector: existence of one charged-once opposite-reciprocal candidate.
```

The t-route has:

```text
outer variable: canonical-LPF scalar Q,
distinguished factor: ell=LPF(Q),
norm value: Q/ell=u^2+v^2,
selector: existence of one primitive Gaussian representation satisfying fixed-U physical masks.
```

No merged theorem identifies `C0` with `ell`, `m` with a canonical LPF quotient, the global canonical-allocation measure with the fixed-U `Q` measure, or the two physical mask families.

Therefore

```text
COMMON_ARITHMETIC_NORM_FORM_ADAPTER_PROVED=false
GLOBAL_FIXED_U_BACKGROUND_MEASURES_IDENTIFIED=false
GLOBAL_FIXED_U_PROJECTION_VARIABLES_IDENTIFIED=false
SAVING_CROSS_PROMOTABLE=false
COMMON_ADAPTER_PROVED=false
```

The common language is suitable for sharing theorem-family reconnaissance, but not for sharing theorem conclusions.

## 5. H decisions

### Mainline

Merged 4ea still requires one further internal substitution before opening a mainline-specific theorem audit.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

### s route

Merged s7-71 explicitly exhausts the elementary reductions and freezes a theorem-ready external target.

```text
S_ROUTE_H_NEEDED=true
S_ROUTE_H_REQUEST=Stage14-sH71
S_ROUTE_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
S_ROUTE_H_BLOCKING=true
```

The requested audit must either prove a uniform fixed `delta>0` density deficit for the correlated root incidence with all physical masks retained, or give a rigorous no-go/full-exponent mechanism.

### fixed-U t route

Merged t108 explicitly freezes `Stage14-tH28`.

```text
FIXED_U_H_NEEDED=true
TH28_NEEDED=true
T_ROUTE_H_REQUEST=CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion
T_ROUTE_H_TARGET=stages/stage14/14-t108/th28-target.md
T_ROUTE_H_BLOCKING=true
```

The sH71 and tH28 audits must remain separate because their outer measures, distinguished factors, projection variables, and physical masks differ.

```text
COMMON_H_THEOREM_FAMILY_RADAR_CAN_BE_SHARED=true
COMMON_H_AUDIT_MERGE_ALLOWED=false
```

## 6. Current receivers

Global/main+s arithmetic receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
PrimitiveCoprimeBinaryForms
CanonicalBalancedIntegerGaussianAllocationDensity
x
ConditionalPrimitiveGaussianRootDensity.
```

Fixed-U receiver:

```text
SharedUCanonicalLPFProjectedPrimitiveNormFormPhysicalSupport.
```

Common formal receiver:

```text
ProjectedPrimitiveGaussianNormFormPhysicalIncidence
with route-specific outer support and masks.
```

## 7. Charged-once prohibitions

The following are localization/reparametrization only and may not be multiplied as additional savings:

```text
heavy mover-prime/root freezing,
primitive-direction localization,
Gaussian split/root orientation,
finite candidate/representation multiplicity,
first reciprocal reconstructed identity,
inner fixed-Q Gaussian fiber density,
prime-energy / collision-energy localization.
```

```text
NORM_FORM_LIFT_QUOTIENT_RECHARGE_ALLOWED=false
GAUSSIAN_ROOT_LINE_RECHARGE_ALLOWED=false
FINITE_REPRESENTATION_FIBER_RECHARGE_ALLOWED=false
```

## 8. Next integrated target

The next integrated comparison should occur after the independent theorem audits return, together with the next mainline substitution boundary.

```text
NEXT_INTEGRATED_TARGET=ProjectedPrimitiveNormFormPhysicalIncidenceTheoremIntersectionOrNoGo
NEXT_REVISIT_CONDITION=merged_4eb_and_sH71_and_tH28_or_material_early_trigger
```

A material early trigger includes:

- either H audit certifies a positive fixed-power saving;
- either H audit proves a sharp no-go/full-exponent countermechanism;
- mainline 4eb exposes an arithmetic predicate identical to one H target;
- an explicit adapter identifies the global root-density incidence with the canonical-LPF projected norm-form support.

## Frozen boundary

```text
STAGE14_WORK_BMX25=COMPLETE_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_COMMON_LANGUAGE_WITH_SEPARATE_H_CONTRACTS
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_ROOT_DIVISIBILITY_LIFTS_TO_NORM_FACTOR_EQUATION=true
S_ROUTE_PROJECTED_PRIMITIVE_NORM_FORM_INCIDENCE=true
T_ROUTE_PROJECTED_PRIMITIVE_NORM_FORM_INCIDENCE=true
COMMON_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_LANGUAGE_PROVED=true
COMMON_PROJECTED_SUPPORT_NOT_INNER_FIBER_PRINCIPLE_PROVED=true
COMMON_ARITHMETIC_NORM_FORM_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=true
S_ROUTE_H_REQUEST=Stage14-sH71
FIXED_U_H_NEEDED=true
TH28_NEEDED=true
COMMON_H_THEOREM_FAMILY_RADAR_CAN_BE_SHARED=true
COMMON_H_AUDIT_MERGE_ALLOWED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_INTEGRATED_TARGET=ProjectedPrimitiveNormFormPhysicalIncidenceTheoremIntersectionOrNoGo
NEXT_REVISIT_CONDITION=merged_4eb_and_sH71_and_tH28_or_material_early_trigger
```
