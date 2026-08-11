# Stage14-4fd — surviving heavy ray requires polynomial radial occupancy at its exact mass exponent

## Status

`COMPLETE_HEAVY_RAY_MASS_TO_RADIAL_OCCUPANCY_SUPPORT_REDUCTION`

Consumes Stage14-4fb/4fc, merged Stage14-4eq, and merged Stage14-s7-77.

Fix a surviving heavy primitive ray at exact `C` with

```text
M_C=B^(mu+o(1)),
0<mu<=rho(phi):=1/4-phi<=1/24.
```

Merged s7-77 gives

```text
m_max(C)=M_C B^(-o(1)).
```

Choose a maximizing primitive ray `r_*`. After the charged-once data of merged 4fa are frozen, let

```text
H_*(C,r_*)
 := {exact admissible radial scales h producing a physical incidence on r_*}.
```

Merged 4eq gives `B^o(1)` physical reverse multiplicity per exact `h`. Therefore

```text
m_C(r_*) <= |H_*(C,r_*)| B^o(1).
```

Since `m_C(r_*)=M_C B^(-o(1))`, necessarily

```text
boxed:
|H_*(C,r_*)| >= B^(mu-o(1)).
```

Stage14-4fa simultaneously gives

```text
|H_*(C,r_*)| <= B^(rho(phi)+o(1)).
```

Thus a surviving heavy branch is no longer an arbitrary mass-capacity gap. It requires a genuinely polynomial set of exact radial square scales, with support exponent at least the exact-`C` mass exponent and at most `rho(phi)`:

```text
B^(mu-o(1))
 <= |H_*|
 <= B^(1/4-phi+o(1)).
```

For every fixed `epsilon>0`, the region `mu>=rho(phi)+epsilon` is already transferred to the genuine-mover branch by 4fc. The residual heavy branch has the exact receiver

```text
FixedPrimitiveRayFixedAgreementPairPolynomialRadialOccupancy
WithMassExponentMuAtMostOneQuarterMinusPhi.
```

This is a material receiver change: the unknown object is now the physical density/structure of a polynomial radial support, not the atomic weight or agreement-pair multiplicity.

No new external H is opened because the radial predicate still has an immediate internal arithmetic opening through the exact square-value identity of merged 4ex.

```text
SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))
SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_UPPER_BOUND=B^(1/4-phi+o(1))
SURVIVING_HEAVY_RAY_MU_RANGE=0<mu<=1/4-phi
HEAVY_RAY_ATOMIC_CAPACITY_GAP_SUPERSEDED=true
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairPolynomialRadialOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAIN_ROUTE_H_NEEDED=false
NEXT=Stage14-4fe
```
