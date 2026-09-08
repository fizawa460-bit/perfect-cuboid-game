# Stage32EX6 — simultaneous critical support versus intrinsic delta budget

Status: `SCRATCH_EXACT_BOUNDED_DOMINATED_DELTA_WALL_NO_ENDPOINT_CREDIT`.

This is the second isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6. Let `N` be its normalization and let `D` be the exact `q'=4` normalized product-cover component with projections of degrees `105` and `81` to `X(8)`.

The preceding scratch diagnostic established that simultaneous critical support of the two projections is exactly the non-immersive locus of the product map and that O266 node lifts contribute no simultaneous critical support. It also defined

`c_common = deg(gcd(R105,R81))/8`

and obtained the existing factor-budget cap

`c_common <= 28`.

The bounded question here is whether the fixed-V6 singularity/normalization defect supplies a stronger cap or forces positive common overlap.

## Opposite smooth-boundary excess supports are disjoint

The retained modular-factor source note identifies the 12 Satake-boundary elliptics as six first-factor and six second-factor cusp families. Near a box node the two boundary axes have strict transforms `L_p` and `L_q` separated by the exceptional curve `E`, with

`div(x)=2L_p+E`,

`div(z)=2L_q+E`.

Thus a normalization point away from the box nodes cannot be simultaneously a smooth-boundary point for both factor directions. Consequently the two smooth-special excess species have disjoint support:

`supp(eta105) intersect supp(eta81) = empty`.

Therefore any nonnode simultaneous critical point must be of one of the support types

- `eta105` with `rho81`,
- `rho105` with `eta81`,
- `rho105` with `rho81`.

There is no `eta105`--`eta81` common-support species.

This is a genuine support refinement, but by itself it gives no numerical improvement over `c_common<=28`, because the `rho` species have no member-level support cap in the retained data.

## Intrinsic delta budget

The retained intermediate-quotient/conductor source note records that the strict-transform V6 curve on the resolved box surface has arithmetic genus `473` and normalization genus `1`. Hence its intrinsic normalization defect is exactly

`delta_intrinsic = 472`.

Away from the O-contact node locus, the product-cover construction is unramified. At a nonnode simultaneous critical branch, choose local product coordinates so that the normalized branch has local coordinate orders `a,b >= 2`. Its common ramification coefficient is

`min(a-1,b-1)`.

The branch multiplicity is `m=min(a,b)`, and the standard plane-branch multiplicity bound gives

`delta_branch >= m(m-1)/2 >= m-1 = min(a-1,b-1)`.

Summing over nonnode simultaneous-critical branches therefore gives the bounded implication

`c_common <= delta_nonnode <= 472`.

This is strictly weaker than the already-retained product-factor cap

`c_common <= 28`.

So the fixed intrinsic delta budget does not sharpen the simultaneous-support bound.

## Delta does not force positive common overlap

The same intrinsic defect also cannot be reversed into a positive lower bound for `c_common`. Normalization defect may be carried by immersed multi-branch singularities, for example ordinary transverse node contributions, where each normalization branch is immersive and therefore neither branch is simultaneously critical for the two product coordinates.

Accordingly, the scalar condition `delta_intrinsic=472` is compatible with `c_common=0` at the level of singularity type bookkeeping. This is only a nonexclusion statement: it does not construct a global V6 carrier or a global curve with a prescribed 472-node realization.

## Decision

Canonical scratch decisions:

- `ETA105_ETA81_COMMON_SUPPORT = EMPTY`;
- `COMMON_CRITICAL_SUPPORT_TYPES = ETA105_RHO81_OR_RHO105_ETA81_OR_RHO105_RHO81`;
- `INTRINSIC_DELTA_COMMON_RAMIFICATION_CAP = 472`;
- `INTRINSIC_DELTA_CAP_DOMINATED_BY_EXISTING_28 = true`;
- `INTRINSIC_DELTA_FORCES_POSITIVE_COMMON_OVERLAP = false`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Consequence for route selection

The simultaneous-support route has now produced two exact structural refinements but no closing inequality:

1. O266 node common critical support is empty and all common criticality is nonnode;
2. opposite-factor smooth-special excess supports are disjoint;
3. the available intrinsic delta budget only gives `c_common<=472`, dominated by `c_common<=28`, and does not force any positive common overlap.

A useful next re-entry must therefore contain genuinely new member-level information: a critical-value/discriminant relation, an immersion theorem on the nonnode population, a quantitative restriction on the `rho` supports, or a landing/jet condition that forces overlap. Replaying genus defect or conductor totals alone is not independent.

## Firewalls

- No global V6 carrier is constructed.
- No claim is made that 472 ordinary nodes are globally realizable in the V6 class; they only show why total delta does not logically force non-immersive branches.
- The plane-branch delta inequality is used only for the one-way upper bound on common ramification.
- No quotient/conductor total is recharged as an eta/rho cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.