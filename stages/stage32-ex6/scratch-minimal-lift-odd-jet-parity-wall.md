# Stage32EX6 — minimal-lift odd-jet parity and globalization wall

Status: `SCRATCH_EXACT_BOUNDED_ODD_JET_PARITY_WALL_NO_ENDPOINT_CREDIT`.

This is the ninth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6.

Retained inputs:

- resolved A1 node chart `x=p^2`, `y=pq`, `z=q^2`, with blowup coordinate `u=y/x` and relation `z=x*u^2`;
- an FSM-minimal branch has `(A,B)=(1,1)`, exceptional multiplicity one, nonzero landing coordinate `lambda`, and is transverse to the exceptional curve;
- AR gives at least 186 such minimal branches at O266;
- the normalized Beauville double cover is ramified at each O266 node branch;
- each such branch has four lifts on the unramified degree-four product-cover component over the Beauville lift.

The previous scratch leaf identified `lambda` with the first-jet differential ratio at a minimal lift. The bounded question here is whether the next jet is also forced strongly enough to create a global counting obstruction.

## Exact local parity adapter

Work on the resolved x-chart. Because a minimal strict-transform branch is transverse to the exceptional divisor, choose the downstairs branch parameter so that

`x=t`.

Its exceptional coordinate is an arbitrary holomorphic unit-valued germ

`u(t)=lambda + mu_1*t + mu_2*t^2 + ...`,

with `lambda != 0`.

The surface equations give

`y=x*u(t)`

and

`z=x*u(t)^2`.

At O266 the Beauville double cover is ramified at this branch, so write

`t=s^2`.

Using the source-locked X(8)->X(4) cusp-square coordinates

`x=p^2`, `z=q^2`,

and choosing the compatible local square root, one obtains

`p=s`

up to a nonzero constant unit and

`q = +/- p*u(p^2)`.

Therefore

`q(p) = +/- (lambda*p + mu_1*p^3 + mu_2*p^5 + ...)`.

Hence the lift relation is odd in the X(8) cusp parameter:

- every even Taylor coefficient vanishes;
- in particular `q''(0)=0` in the normalized cusp coordinates;
- the first coefficient after the slope `lambda` is the cubic coefficient `mu_1`.

This is stronger than the previous first-jet statement but still purely local.

## Freedom begins at cubic order

The A1/FSM local model does not constrain `mu_1`.

Indeed any germ

`u(t)=lambda + mu*t + O(t^2)`

with `lambda != 0` produces a valid resolved minimal branch germ, and upstairs

`q(p)=+/- (lambda*p + mu*p^3 + O(p^5))`.

Thus the node geometry forces parity but does not fix the cubic jet. In particular there is no local finite list of second/third-jet values supplied by the retained model.

## Population upstairs

AR gives at least 186 FSM-minimal node branches downstairs. Each has four product-cover lifts over the Beauville ramified point. Therefore at least

`4*186 = 744`

minimal lift points satisfy the odd-jet relation above.

At each such point the two projection differentials are nonzero; this is not common ramification. The new local condition is the vanishing of the normalized quadratic coefficient of the graph relation, not a zero or pole of either projection differential.

## Why 744 odd-jet points are not yet a global divisor contradiction

A second derivative of a map between curves is not intrinsically a tensor under arbitrary coordinate changes. The statement `q''(0)=0` is meaningful in the source-locked modular cusp coordinates, whose square relation produces the parity, but one cannot count these 744 local vanishings as zeros of a global section without an exact globalization adapter.

Such an adapter would need, for example,

- a source-locked projective or affine connection on the X(8) cusp-coordinate system;
- an explicit algebraic 2-jet bundle section whose local expression is the normalized quadratic coefficient;
- a modular differential operator with a proved transformation law and computable divisor class;
- or an explicit fixed-V6 member equation whose second-jet coefficient is a global meromorphic function/section.

No such global jet/connection object is present in the retained EX6 source locks inspected so far, and bounded searches for higher-jet / jet-separation / landing terms did not surface one. This search miss is not a repository-wide absence claim.

The existing differential-ratio line bundle of degree 192 does not repair this gap: its divisor records first-derivative zeros and poles, while the quadratic graph coefficient is a different, coordinate-dependent jet datum. The 744 minimal lifts remain regular nonzero evaluation points for the first-derivative ratio.

## Consequence

The higher-jet route is narrowed rather than closed:

- local minimal-lift parity is exact;
- the quadratic term vanishes at every minimal lift;
- at least 744 product-cover lift points satisfy that local parity;
- cubic freedom remains branch-by-branch;
- no global 2-jet divisor class or degree bound has been source-locked;
- therefore no counting contradiction follows yet.

A useful continuation must globalize this parity into a bounded-degree modular jet section or constrain the cubic coefficient/member equation.

## Decision

Canonical scratch decisions:

- `MINIMAL_LIFT_X8_GRAPH_IS_ODD_IN_CUSP_PARAMETER = true`;
- `MINIMAL_LIFT_QUADRATIC_COEFFICIENT_VANISHES = true`;
- `MINIMAL_LIFT_FIRST_FREE_HIGHER_COEFFICIENT = CUBIC`;
- `MINIMAL_LIFT_CUBIC_COEFFICIENT_LOCALLY_FREE = true`;
- `ODD_JET_MINIMAL_LIFT_COUNT_UPSTAIRS >= 744`;
- `GLOBAL_SECOND_JET_SECTION_SOURCE_LOCKED = false`;
- `ODD_JET_COUNTING_CONTRADICTION = false`;
- `MEMBER_LEVEL_CUBIC_OR_GLOBAL_JET_COUPLING = UNTESTED`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- Local cusp-coordinate parity is not promoted to a coordinate-free global inflection theorem.
- `744` is not compared against an invented global second-jet divisor degree.
- Cubic freedom is a local feasibility statement, not a global realization theorem.
- No ambient/deck symmetry is promoted to a member-stabilizing symmetry.
- No RH, delta, conductor, cusp-grid, Picard, Abel, Jacobian, first-jet, or deck-translate total is double-charged as a new eta/rho cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
