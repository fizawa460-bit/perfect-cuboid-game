# Stage14-t99 — pigeonhole the influential physical boundary class

## Status

`COMPLETE_BOUNDARY_CLASS_PIGEONHOLE_LOCALIZATION`

Stage14-t99 consumes merged t98 and the completed frozen tH26 snapshot without reopening H.

Merged t96 gives, on every square-root-saturating exponent-zero intermediate occupancy packet, an influential generic split-prime orientation bit `p` with

```text
Inf_p(f) >= B^(-o(1)).
```

Merged t98 decomposes the corresponding explicit physical symmetric difference into `B^o(1)` elementary boundary events of three classes:

1. `SIGN`: explicit linear sign/order half-space XORs;
2. `DIV`: four-cell divisor-membership XORs modulo divisors of the fixed direction support `A0*B0`;
3. `PROJ`: endpoint projective residue XORs modulo `d=B^o(1)`.

If the union of `J=B^o(1)` elementary events has average at least `B^(-o(1))`, then by the union bound and pigeonhole at least one elementary event has average

```text
>= B^(-o(1))/J = B^(-o(1)).
```

Hence every saturating sequence has a subsequence localized to one explicit elementary boundary of one of the three classes. No cancellation between boundary classes is needed for this reduction.

This is a localization theorem only. A sign/order half-space boundary can have positive density; a divisor boundary can involve a large fixed divisor; and an endpoint projective residue boundary need not by itself be sparse. Therefore no fixed-power saving follows yet.

The receiver is now theorem-specific enough for a new immutable H audit: audit the three single-boundary classes separately and determine whether any standard lattice/equidistribution/character theorem gives a uniform fixed-power deficit under the full physical masks. The target is frozen in `stages/stage14/14-t99/th27-target.md`.

```text
STAGE14_T99=COMPLETE_BOUNDARY_CLASS_PIGEONHOLE_LOCALIZATION
T98_BOUNDARY_DECOMPOSITION_RETAINED=true
INFLUENTIAL_GENERIC_BIT_RETAINED=true
BOUNDARY_EVENT_COUNT=Bo1
SINGLE_ELEMENTARY_BOUNDARY_PIGEONHOLE_PROVED=true
SATURATION_LOCALIZES_TO_ONE_BOUNDARY_CLASS=true
SIGN_BOUNDARY_BRANCH_RETAINED=true
FIXED_DIVISOR_BOUNDARY_BRANCH_RETAINED=true
ENDPOINT_PROJECTIVE_BOUNDARY_BRANCH_RETAINED=true
FIXED_POWER_BOUNDARY_SPARSITY_PROVED=false
TH26_COMPLETE_CONSUMED=true
TH27_NEEDED=true
TH27_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH27=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFSingleGenericPrimeSingleElementaryBoundaryClassEnergy
NEXT=Stage14-t100
```
