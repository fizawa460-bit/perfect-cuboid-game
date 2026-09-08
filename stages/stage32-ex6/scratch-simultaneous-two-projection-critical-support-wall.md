# Stage32EX6 — simultaneous two-projection critical-support diagnostic

Status: `SCRATCH_EXACT_BOUNDED_STRUCTURAL_RELATION_NO_ENDPOINT_CREDIT`.

This is an isolated micro-diagnostic from PR #1715 head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Work under the same conditional O=266 population as the retained EX6 product-cover leaves: a hypothetical integral irreducible geometric-genus-one V6 carrier, its normalization `N`, the connected Beauville pullback `Y`, and the exact `q'=4` normalized product-cover component `D`.

The two nonconstant modular projections are

`pi105 : D -> X(8)`, degree `105`,

`pi81 : D -> X(8)`, degree `81`.

The retained product-cover Riemann--Hurwitz totals are

`deg R105 = 224`, `deg R81 = 416`.

The retained nonnode split is

`deg R105_nonnode = 8*(eta105+rho105)`,

`deg R81_nonnode = 8*(eta81+rho81)`.

The purpose of this diagnostic is only to determine what an actual *simultaneous* critical point of the two projections means geometrically.

## Local product-map criterion

Let

`h=(pi105,pi81): D -> X(8) x X(8)`.

At a smooth point `P in D`, choose a local parameter `t` on `D` and local parameters `u,v` at the two target points. Write the two local degrees as `e105,e81`. Then

`ord_P(R105)=e105-1`,

`ord_P(R81)=e81-1`.

The tangent map of `h` is the ordered pair of the two factor differentials. Hence

`dh_P=0  <=>  d pi105(P)=0 and d pi81(P)=0`

and therefore

`P in supp(R105) intersect supp(R81)  <=>  h is non-immersive at P`.

Equivalently, simultaneous projection-critical support is not free support data: it is exactly the non-immersive locus of the product map.

This is the curve-to-product form of the standard unramified/differential criterion. For source reference, see the Stacks Project, Tag `02H9` (`Omega_{X/S}=0` criterion) together with Tag `0AB1` for normalization being an isomorphism over a normal locus.

Because `D` is the normalization of an irreducible pullback component in the smooth product, if the image curve is smooth at `h(P)`, the normalization is locally an isomorphism there. Thus a simultaneous critical point must land on a singular image point and, more precisely, on a non-immersive normalization branch. Ordinary immersed branches of a nodal image do not create simultaneous criticality.

## O266 node lifts contribute no simultaneous critical support

At an O266 node contact, the retained AN/AR adapter gives local projection degrees `A,B` on each lift to `D`, with

`min(A,B)=m=1`.

Therefore at least one of the two local projection degrees is exactly one. Its ramification order is zero. Hence for every point of `D` lying above an O266 node contact,

`min(ord R105, ord R81)=0`.

So

`O266_NODE_COMMON_CRITICAL_SUPPORT = EMPTY`.

All simultaneous critical support of the two X(8) projections, if any, is forced into the retained nonnode locus.

## Exact common-ramification divisor bound

Define the coefficientwise common ramification divisor

`R_common := gcd(R105,R81)`.

The node calculation above gives

`R_common = gcd(R105_nonnode,R81_nonnode)`.

Away from the O-contacts, `D -> N` is unramified of degree eight, so a common critical branch downstairs has eight lifts with the same two local ramification orders. Consequently `deg R_common` is a multiple of eight. Writing

`c_common := deg(R_common)/8`,

one has the exact tautological bound

`c_common <= min(eta105+rho105, eta81+rho81)`.

At O266 the retained slack identities give

`eta105+rho105 = 28-q105_node <= 28`,

`eta81+rho81 = 52-q81_node <= 52`.

Hence

`c_common <= 28`,

or upstairs

`deg R_common <= 224`.

This is a support localization and overlap cap only. It is not an independent upper bound on either `eta_i` or `rho_i`; it follows from the already-retained factorwise ramification budgets.

## Why this does not close O266

The new structural information is:

1. node lifts cannot carry simultaneous criticality at O266;
2. any simultaneous criticality is a nonnode non-immersive/singular-image phenomenon of the pair map;
3. the common ramification overlap is at most 28 downstairs units.

But the currently source-locked data do not force a positive minimum amount of common overlap, do not forbid non-immersive nonnode branches, and do not provide a member-level discriminant/jet equation that caps `eta` or `rho` from this localization.

Therefore the simultaneous-support route is not empty, but this first structural adapter alone is nonexcluding. A useful continuation needs one further independent statement, for example:

- immersion of the product map on the relevant nonnode population;
- a bound on non-immersive branches from the actual fixed-V6 image singularities;
- a critical-value/discriminant relation coupling the two projections;
- or a landing/jet theorem forcing enough overlap to contradict `c_common<=28`.

## Scratch decisions

- `SIMULTANEOUS_TWO_PROJECTION_CRITICAL_SUPPORT = NONIMMERSIVE_PRODUCT_MAP_LOCUS`;
- `O266_NODE_COMMON_CRITICAL_SUPPORT = EMPTY`;
- `SIMULTANEOUS_COMMON_RAMIFICATION_DOWNSTAIRS <= 28`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- No claim is made that the product image is smooth or immersed away from the node lifts.
- No ordinary singular-image delta budget is converted into a ramification cap without a source-locked local adapter.
- No critical-value relation is invented.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf is non-authoritative until a later retained consolidation and hostile-audit workflow.