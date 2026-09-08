# Stage32EX6 — X(8) first-order Jacobian common-factor blindness wall

Status: `SCRATCH_EXACT_BOUNDED_FIRST_ORDER_JACOBIAN_CLASS_WALL_NO_ENDPOINT_CREDIT`.

This is the fourth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6. Let `D` be the exact `q'=4` normalized product-cover component. The retained product-cover source lock gives

- `g(D)=533`;
- `g(X(8))=5`;
- `pi105 : D -> X(8)` of degree `105`;
- `pi81 : D -> X(8)` of degree `81`;
- exact ramification degrees `deg R105=224`, `deg R81=416`.

The previous scratch diagnostics established that O266 node lifts carry no common criticality, all simultaneous criticality is nonnode, and

`c_common = deg(gcd(R105,R81))/8 <= 28`.

The bounded question here is whether first-order `X(8)` Jacobian/divisor-class data can itself expose or bound that common ramification divisor.

## Differential line bundles

For a finite morphism `pi : D -> X(8)` between smooth curves, the differential is a section

`d pi in H^0(D, K_D tensor pi^* K_X(8)^(-1))`,

whose zero divisor is exactly the ramification divisor.

Define

`L105 = K_D tensor pi105^* K_X(8)^(-1)`,

`L81  = K_D tensor pi81^*  K_X(8)^(-1)`.

Then

`div(d pi105)=R105`,

`div(d pi81)=R81`.

The retained genera and degrees give

`deg L105 = (2*533-2) - 105*(2*5-2) = 1064-840 = 224`,

`deg L81  = 1064 - 81*8 = 416`,

recovering the exact Riemann--Hurwitz totals.

## The common factor cancels from the first-order ratio

Let

`G := gcd(R105,R81)`

coefficientwise, and write

`R105 = G + A`,

`R81  = G + B`,

where `A` and `B` have disjoint support coefficientwise.

Although the two differentials are sections of different line bundles, their quotient is a meromorphic section of

`M := L81 tensor L105^(-1)`.

The canonical factors cancel, so

`M = pi105^* K_X(8) tensor pi81^* K_X(8)^(-1)`.

Its degree is

`deg M = 105*8 - 81*8 = 192`.

The divisor of the meromorphic ratio is

`div((d pi81)/(d pi105))`
`= R81-R105`
`= (G+B)-(G+A)`
`= B-A`.

Thus the simultaneous/common ramification divisor `G` cancels identically.

Numerically,

`deg(R81-R105)=416-224=192=deg M`,

so the first-order divisor-class relation contains exactly the already-known ramification-degree difference and no common-overlap information.

## Rank-two Jacobian viewpoint

Equivalently, the ordered differential

`dh=(d pi105,d pi81)`

is a section of the rank-two vector bundle

`L105 direct-sum L81`

on the smooth curve `D`.

Its zero scheme is precisely the simultaneous critical locus. On a one-dimensional base, however, there is no top-Chern degree formula forcing the zero length of a section of a rank-two bundle. The two component degrees determine `deg R105` and `deg R81`, but they do not determine `deg gcd(R105,R81)`.

This is the bundle-theoretic reason that a generic first-order Jacobian computation cannot manufacture a positive common-overlap lower bound from bidegrees, genera, or Riemann--Hurwitz totals alone.

## What an actual subresultant/Jacobian improvement would require

A stronger member-level coupling is still logically possible, but it must use data beyond the two differential divisor classes. Examples include

- an explicit defining equation for the fixed-V6 image in `X(8) x X(8)`;
- a source-locked Jacobian/Fitting ideal for that member;
- an explicit function-field relation whose subresultants constrain simultaneous derivative vanishing;
- a modular-symmetry identity forcing a prescribed divisor for the ratio section beyond its degree/class;
- or a higher-jet/landing theorem restricting the common factor `G`.

The bounded repository searches performed for `Jacobian`, `Jacobian ideal`, `subresultant`, `resultant`, `pair-map`, and `V6 theta equation X8` did not surface such a retained member-level asset. The retained pair-map/Rosati source lock supplies exact bidegrees, birationality, deck intersections, and Rosati arithmetic, but not an explicit fixed-V6 pair-image equation or a Jacobian/subresultant identity. This search miss is not a repository-wide nonexistence claim.

## Consequence for EX6

The first-order `X(8)` Jacobian/divisor-class route is therefore exact but common-factor blind:

- `deg R105=224` and `deg R81=416` remain exact;
- `R81-R105` has class/degree `192`;
- the common divisor `G=gcd(R105,R81)` cancels from that relation;
- no new lower or upper bound on `c_common` follows;
- the previous `c_common<=28` remains the best current overlap cap;
- no independent bound on `eta` or `rho` follows.

This does **not** exhaust an explicit member-level subresultant/Jacobian route. It excludes only the generic first-order divisor-class version of that idea.

## Decision

Canonical scratch decisions:

- `X8_DIFFERENTIAL_LINE_BUNDLE_DEG_105 = 224`;
- `X8_DIFFERENTIAL_LINE_BUNDLE_DEG_81 = 416`;
- `X8_DIFFERENTIAL_RATIO_LINE_BUNDLE_DEGREE = 192`;
- `X8_DIFFERENTIAL_RATIO_DIVISOR = R81_MINUS_R105`;
- `COMMON_RAMIFICATION_CANCELS_FROM_FIRST_ORDER_RATIO = true`;
- `GENERIC_FIRST_ORDER_JACOBIAN_FORCES_COMMON_OVERLAP = false`;
- `EXPLICIT_MEMBER_LEVEL_JACOBIAN_OR_SUBRESULTANT_ASSET = NOT_RETAINED_BY_BOUNDED_SEARCH`;
- `EXPLICIT_MEMBER_LEVEL_JACOBIAN_OR_SUBRESULTANT_ROUTE = UNTESTED`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- No repository-wide absence of an explicit Jacobian/subresultant theorem is claimed.
- The line-bundle calculation does not identify scalar discriminants with normalization ramification.
- The common divisor cancellation does not imply `G=0`; it means the first-order ratio is blind to `G`.
- No total RH, delta, conductor, cusp-grid, or tangent datum is recharged as an `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
