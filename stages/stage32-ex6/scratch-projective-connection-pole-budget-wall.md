# Stage32EX6 — projective-connection pole budget and uniform jet-strength wall

Status: `SCRATCH_EXACT_BOUNDED_PROJECTIVE_POLE_BUDGET_WALL_NO_ENDPOINT_CREDIT`.

This is the twelfth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6. Let `N` be its normalization and `D` the exact `q'=4` normalized product-cover component.

Retained inputs:

- `g(D)=533`;
- factor projections `D -> X(8)` have degrees `105` and `81`;
- at O266 all `266` node contacts have exceptional multiplicity one;
- at least `186` node branches are FSM-minimal, hence at least `744` minimal lifts on `D`;
- for the normalization factor maps, post1648AR gives at O266
  `52=q81_node+eta81+rho81` and
  `28=q105_node+eta105+rho105`;
- the total boundary intersections with the six multiplicity-two special boundary elliptics are
  `q81=110` and `q105=182`;
- away from O-contacts, a normalization point has eight lifts to `D`;
- the two factor-cusp boundary families meet only at the box-node geometry.

The previous scratch leaves introduced the intrinsic difference `Theta` of the two pulled-back uniformizing projective connections and showed that at a minimal lift

`q(p)=eps*(lambda*p+mu1*p^3+mu2*p^5+...)`

and

`Theta(P_min)=8*(mu1/lambda)*(dp)^2`.

The question here is the actual compactified pole budget of `Theta`, and therefore the real zero-capacity threshold for any future high-jet vanishing theorem.

## Standard local pullback formula

For a projective connection with local coefficient `P(w)`, its pullback through `w=f(t)` has coefficient

`P(f(t))*(f'(t))^2 + S(f,t)`,

where `S` is the Schwarzian derivative.

At an `X(8)` cusp use the compactifying coordinate `w`, with uniformizing coordinate proportional to `log w`. Therefore the uniformizing projective connection is

`P_cusp(w)=S(log w,w)=1/(2*w^2)`.

If `w=t^e*unit(t)`, then by the Schwarzian chain rule the pulled-back cusp projective connection has principal part

`1/(2*t^2)+O(1/t)`.

The coefficient of the double pole is independent of the local degree `e`.

At an interior target point, choose a local projective coordinate. If the map has local degree `e`, then

`S(t^e,t)=(1-e^2)/(2*t^2)`

up to lower pole order from analytic units. Thus an interior ramification point creates at most a double pole.

## All O266 node lifts are regular for Theta

At O266, `min(A,B)=1` and retained parity gives `A+B` even, hence both `A,B` are odd.

At a Beauville/product-cover node lift choose local source parameter `s` so the quotient involution is `s -> -s`. The retained node inertia acts `(p,q)->(-p,-q)`. Therefore the two cusp functions have the equivariant forms

`p=s^A*U(s^2)`,
`q=s^B*V(s^2)`,

with nonzero even units `U,V`.

Consequently

`S(log p,s)=1/(2*s^2)+holomorphic_even`,
`S(log q,s)=1/(2*s^2)+holomorphic_even`.

The universal double poles cancel and there is no simple pole because the unit corrections are even. Hence

`Theta` is regular at every O266 node lift.

There are four product-cover points above each of the 266 node branches, so this regularity holds at all

`4*266 = 1064`

node lifts, not only the at least 744 FSM-minimal lifts.

## Exact smooth-boundary support counts

For one factor direction post1648AR defines

`q_smooth=q-q_node`,
`s=q_smooth-eta`.

At O266 `t=0`.

For degree 81:

`q81=110`,
`52=q81_node+eta81+rho81`,

so

`s81=110-q81_node-eta81=58+rho81`.

For degree 105:

`q105=182`,
`28=q105_node+eta105+rho105`,

so

`s105=182-q105_node-eta105=154+rho105`.

Thus the two factor directions have exactly

`s81+s105 = 212+rho81+rho105`

smooth-boundary normalization points.

The first-factor and second-factor boundary families meet only at node geometry. Therefore these smooth-boundary supports are disjoint between the two directions. Each such normalization point has eight lifts to `D`, giving exactly

`8*(212+rho81+rho105)`

product-cover points where exactly one projection lands at an X(8) cusp.

## Each one-cusp smooth point is an unavoidable double pole

At such a point one projection is a cusp map. Its pulled-back projective connection has double-pole coefficient `1/2`.

The other projection lands in the interior. If its local degree is `e>=1`, its pulled-back projective connection has double-pole coefficient `(1-e^2)/2` (zero when unramified).

Therefore their difference has double-pole coefficient, up to sign,

`e^2/2`,

which is never zero.

Hence every one-cusp smooth-boundary lift is an exact pole of order two of `Theta`.

Write

`Rrho := rho81+rho105`.

The exact smooth-boundary pole contribution is therefore

`P_smooth = 2*8*(212+Rrho)`
`         = 3392+16*Rrho`.

## Off-special pole allowance

Post1715 source-locks the upstairs off-special ramification degrees as

`8*rho81` and `8*rho105`.

The number of points in the union of these off-special ramification supports is at most

`8*Rrho`,

because every ramified point contributes at least one ramification unit. At an interior ramification point `Theta` has pole order at most two. Therefore any additional off-special pole degree is at most

`16*Rrho`.

There are no other pole species in this bounded model:

- node cusp lifts are regular by the parity cancellation above;
- smooth special-fibre lifts are exactly the one-cusp points already counted;
- interior unramified points are regular.

Thus the actual pole divisor satisfies

`3392+16*Rrho <= deg Pole(Theta) <= 3392+32*Rrho`.

The O266 slack identities give

`rho81<=52`, `rho105<=28`,

hence

`0<=Rrho<=80`

and uniformly

`deg Pole(Theta) <= 3392+32*80 = 5952`.

## Actual meromorphic zero-capacity bound

Since `g(D)=533`,

`deg K_D^2 = 4g(D)-4 = 2128`.

For a nonzero meromorphic quadratic differential,

`deg Zero(Theta)-deg Pole(Theta)=2128`.

Therefore

`deg Zero(Theta) <= 2128 + 3392 + 32*Rrho`
`               = 5520+32*Rrho`
`               <= 8080`.

This replaces the previous optimistic holomorphic benchmark `2128` by an actual endpoint-uniform meromorphic capacity bound.

The unavoidable smooth-boundary poles also give the lower zero-degree demand

`deg Zero(Theta) >= 5520+16*Rrho`,

but this lower bound is only diagnostic and is not an exclusion.

## Uniform high-jet strength threshold

At each FSM-minimal lift write

`q(p)=eps*(lambda*p + mu1*p^3 + mu2*p^5 + ... )`.

If the first `r` higher odd coefficients vanish,

`mu1=...=mur=0`,

then the first possible relative correction has order `p^(2r+2)`, and the projective-connection difference has

`ord_P(Theta)>=2r`.

There are at least `744` minimal lifts. Hence such a theorem at every minimal lift would force at least

`1488*r`

zeros counted with multiplicity.

Against the actual capacity bound:

- `r=4`: forced `5952`; sufficient only if `Rrho<=13`;
- `r=5`: forced `7440`; sufficient only if `Rrho<=59`;
- `r=6`: forced `8928`, and
  `8928>8080`,
  so it is uniformly sufficient over the full O266 slack range to force `Theta identically 0`.

Thus a future member-level jet theorem whose sole projective-connection consequence is weaker than six consecutive higher-odd coefficient vanishings at every one of the 744 guaranteed minimal lifts is not uniformly sufficient by this divisor route.

Even the six-jet threshold would only force `Theta identically 0`; a separate theorem is still required to show that equality of the two pulled-back projective connections is impossible for the fixed-V6 pair map.

## Decision

Canonical scratch decisions:

- `O266_NODE_LIFT_THETA_REGULAR_COUNT = 1064`;
- `SMOOTH_BOUNDARY_POINT_COUNT_81 = 58+rho81`;
- `SMOOTH_BOUNDARY_POINT_COUNT_105 = 154+rho105`;
- `ONE_CUSP_SMOOTH_LIFT_COUNT = 1696+8*(rho81+rho105)`;
- `ONE_CUSP_SMOOTH_LIFTS_ARE_EXACT_DOUBLE_POLES = true`;
- `THETA_POLE_DEGREE_LOWER = 3392+16*(rho81+rho105)`;
- `THETA_POLE_DEGREE_UPPER = 3392+32*(rho81+rho105)`;
- `RHO81_PLUS_RHO105_MAX = 80`;
- `THETA_POLE_DEGREE_UNIFORM_UPPER = 5952`;
- `THETA_ZERO_DEGREE_UNIFORM_UPPER_IF_NONZERO = 8080`;
- `FIVE_HIGHER_ODD_JET_VANISHINGS_UNIFORMLY_SUFFICIENT = false`;
- `SIX_HIGHER_ODD_JET_VANISHINGS_FORCE_THETA_IDENTICALLY_ZERO = true`;
- `THETA_IDENTICALLY_ZERO_IMPLIES_V6_IMPOSSIBLE = UNTESTED`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- The pole calculation is conditional on the same hypothetical O266 carrier and exact product-cover component used by retained EX6.
- `Theta identically 0` is not an endpoint contradiction without a separate global projective-correspondence theorem.
- No coefficient vanishing `mu1=...=mur=0` is actually proved here; those are threshold tests only.
- The off-special support upper bound uses only exact retained `8rho` ramification degree and does not assume simple ramification or independence.
- Pole cancellations can only lower the actual pole degree; the upper bound remains valid.
- No RH, delta, conductor, cusp-grid, Picard, Abel, deck symmetry, or previous jet datum is double-charged as an eta/rho cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
