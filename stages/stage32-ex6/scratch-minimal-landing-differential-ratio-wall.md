# Stage32EX6 — minimal landing / differential-ratio adapter and interpolation wall

Status: `SCRATCH_EXACT_BOUNDED_LANDING_DIFFERENTIAL_RATIO_WALL_NO_ENDPOINT_CREDIT`.

This is the seventh isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6. Let `N` be its normalization and `D` the exact `q'=4` normalized product-cover component.

Retained inputs:

- AN local node model `x=p^2`, `y=pq`, `z=q^2`, `xz=y^2`;
- for an FSM-minimal branch `(A,B)=(1,1)`, the strict-transform germ may be written
  `gamma_lambda(t)=(x,y,z)=(t,lambda*t,lambda^2*t)` with `lambda != 0`;
- AR proves at least `186` such FSM-minimal node branches at O266;
- each minimal branch has zero ramification in both factor directions and a nonzero finite exceptional landing ratio `lambda`;
- the normalized product-cover has four points over the Beauville lift of each O266 node branch;
- the two X(8) projections on `D` have exact ramification divisors `R105,R81` and differential-ratio line bundle
  `M = pi105^*K_X(8) tensor pi81^*K_X(8)^(-1)` of degree `192`.

The bounded question is whether the many minimal landing parameters can be converted into a degree-192 interpolation contradiction.

## Exact local landing-to-differential adapter

On the minimal downstairs germ

`x=t`, `z=lambda^2*t`,

so

`dz/dx = lambda^2`.

At an O266 node the Beauville double cover is ramified. Write a local parameter `s` upstairs with

`t=s^2`.

The source-locked X(8)->X(4) cusp coordinates satisfy

`x=p^2`, `z=q^2`.

After choosing the compatible local cusp uniformizers at a lift, one may write

`p = u_p*s + O(s^2)`,
`q = u_q*lambda*s + O(s^2)`,

with nonzero local units `u_p,u_q` determined by the chosen lift/trivializations. Therefore

`(dq/dp)(0) = (u_q/u_p)*lambda`.

In the normalized source chart where the standard cusp uniformizers are chosen with equal leading-unit normalization, this is

`dq/dp = +/- lambda`,

and invariantly

`(dq/dp)^2 = lambda^2 = dz/dx`

up to the fixed nonzero unit coming from the target-coordinate trivializations.

Thus the exceptional landing parameter is genuinely the local value, modulo the finite deck/trivialization unit, of the ratio of the two X(8) projection differentials.

## At least 744 regular evaluation points upstairs

AR gives at least `186` minimal branches on `N`.

Each O266 branch has one Beauville ramified point and four points above it on the unramified degree-four map `D->Y`. Hence the minimal population gives at least

`4*186 = 744`

points on `D` at which both X(8) projection local degrees are exactly one.

Therefore at all these points

- `d pi105 != 0`;
- `d pi81 != 0`;
- the meromorphic ratio section
  `r := (d pi81)/(d pi105)`
  is finite and nonzero;
- its local value records the corresponding exceptional landing parameter `lambda` up to the fixed deck/trivialization unit.

This is an exact landing-to-first-jet adapter.

## Why `744 > 192` is not an interpolation contradiction

The ratio `r` is a meromorphic section of the nontrivial line bundle `M` of degree `192`. Its divisor is

`div(r)=R81-R105`.

The number `192` controls the divisor class/zero-minus-pole degree. It does **not** bound the number of points where a meromorphic section takes an ordinary finite nonzero value.

All 744 minimal-lift points are precisely of this latter type: they are neither zeros nor poles of `r`.

Moreover the values are not externally prescribed. AN explicitly leaves the nonzero landing coordinate `lambda` free branch-by-branch; several branches over the same node may be assigned pairwise distinct nonzero `lambda` values. AR also records only the residual involution `lambda -> -lambda`, not a finite allowed landing set or a source-locked algebraic equation for the actual values.

Consequently the existence of at least 744 regular evaluation points supplies no degree contradiction with `deg M=192`.

## What a genuine higher-jet continuation would need

The new adapter is useful because it identifies the precise missing structure. A closing landing/jet theorem would need at least one independent statement such as:

1. a source-locked finite or low-degree algebraic constraint on the allowed `lambda` values at each node;
2. a global comparison section/trivialization converting the local landing ratios into zeros of a fixed meromorphic function of bounded degree;
3. a second- or higher-jet identity forcing repeated landing values to produce zeros/poles or branch collisions;
4. a modular/deck symmetry theorem coupling landing values across different node exceptional curves;
5. a member-level tangent-separation theorem forcing collisions among the at least 186 minimal strict-transform branches.

Without one of these, the first-jet landing values are free regular evaluations rather than divisor conditions.

## Decision

Canonical scratch decisions:

- `MINIMAL_LANDING_EQUALS_LOCAL_DIFFERENTIAL_RATIO_UP_TO_DECK_UNIT = true`;
- `MINIMAL_BRANCH_COUNT_DOWNSTAIRS >= 186`;
- `MINIMAL_LIFT_REGULAR_EVALUATION_COUNT_UPSTAIRS >= 744`;
- `MINIMAL_LIFTS_ARE_ZEROS_OR_POLES_OF_RATIO = false`;
- `DEGREE_192_BOUNDS_NUMBER_OF_REGULAR_NONZERO_EVALUATIONS = false`;
- `LANDING_VALUES_EXTERNALLY_PRESCRIBED = false`;
- `FIRST_JET_LANDING_COUNT_CONTRADICTION = false`;
- `HIGHER_JET_OR_CROSS_NODE_LANDING_COUPLING = UNTESTED`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- The local differential-ratio statement uses the retained FSM node chart and the source-locked X(8)->X(4) square cusp relation only.
- `744>192` is explicitly not promoted to a contradiction.
- Freedom of `lambda` is a local feasibility statement, not a global realization theorem.
- No finite landing set, cross-node identification, global trivialization, or higher-jet relation is invented.
- No total RH, delta, conductor, cusp-grid, Picard, Abel, or previous Jacobian datum is double-charged as a new `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
