# Stage32EX6 scratch — Beauville branch pullback Pluecker saturation wall

Status: `SCRATCH_EXACT_BOUNDED_BEAUVILLE_BRANCH_PULLBACK_PLUCKER_SATURATION_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, or create Stage32 MAIN / hostile-audit credit.

## Input from the preceding square-root leaf

On the hypothetical O266 genus-one normalization `N`, the Beauville branch half-line-bundle is

`A = 3H_N - sum_{j=1}^6 L_j`,

with

`deg A = 133`, `2A = D_O`, `deg D_O=266`.

Let

`pi:Y->N`

be the connected Beauville double cover.  Then

`g(Y)=134`,

and because `K_N` is trivial,

`K_Y = pi^* A`.

The complete linear series `|A|` on the genus-one curve has

`h0(N,A)=133`,

so its pullback gives a linear subsystem

`V := pi^* H0(N,A) subset H0(Y,K_Y)`

of projective dimension `r=132` and degree `d_Y=deg(pi^*A)=266`.

Thus `V` is a `g^132_266` on the genus-134 curve `Y`.

## Branch-point vanishing sequence

At a branch point `Q in Y` above `P in N`, choose local parameters with

`t=s^2`.

If the vanishing sequence of the complete `|A|` at `P` is

`a_0<...<a_132`,

then the pullback subsystem has vanishing sequence

`2a_0 < ... < 2a_132`

at `Q`.

Let

`w_A(P)=sum_i(a_i-i)`

be the ramification weight of `|A|` at `P`.  The ramification weight of the pullback subsystem at the branch point is therefore

`w_V(Q) = sum_i(2a_i-i)`
`       = 2*w_A(P) + sum_{i=0}^{132} i`
`       = 2*w_A(P) + 8778`.

So every O266 branch point carries the universal baseline weight

`8778`.

## Exact Pluecker total

For a `g^r_d` on a genus `g` curve, the Pluecker ramification degree is

`(r+1)*(d+r*(g-1))`.

Here

- `r=132`;
- `d=266`;
- `g=134`.

Hence

`W_V = 133*(266+132*133)`
`    = 2,370,326`.

The branch baseline contributes

`266*8778 = 2,334,948`.

On the genus-one base, the complete `g^132_133=|A|` has total ramification weight

`W_A = 133*133 = 17,689`.

Pullback contributes exactly twice the base ramification weight in addition to the branch baseline, because an unbranched base point has two lifts with the same weight and a branch point contributes `2*w_A(P)` in the displayed branch formula.

Therefore

`266*8778 + 2*17689`
`= 2,334,948 + 35,378`
`= 2,370,326`
`= W_V`.

The branch baseline plus the pulled-back base inflection divisor **exactly saturates the entire Pluecker ramification budget** of the `g^132_266`.

## Consequence

There is no hidden positive Pluecker surplus available from the invariant canonical subsystem `pi^*H0(A)`.

In particular one may not argue that the 266 branch points already consume “too much” Weierstrass/ramification weight.  Their large even-order contribution is exactly the functorial ramification expected from pulling a complete degree-133 series through a branched double cover.

Any future Weierstrass/Wronskian closure must therefore use genuinely additional structure, for example

- a distinguished **pencil** inside `H0(N,A)` whose Wronskian is constrained by the V6/rank3 geometry;
- the extra anti-invariant canonical section in `H0(Y,K_Y)` rather than only the invariant pullback subsystem;
- an independent restriction forcing abnormal base inflection weight at the O266 branch points;
- or a Wronski-map/image condition on the specific branch divisor `D_O`.

The complete pullback-subseries Pluecker formula itself is an exact equivalence, not an exclusion.

## Decision

- `BEAUVILLE_INVARIANT_CANONICAL_SUBSYSTEM = g132_266`;
- `BRANCH_POINT_PULLBACK_WEIGHT_BASELINE = 8778`;
- `BASE_COMPLETE_A_SERIES_TOTAL_WEIGHT = 17689`;
- `PULLBACK_SUBSERIES_TOTAL_PLUCKER_WEIGHT = 2370326`;
- `BRANCH_BASELINE_PLUS_TWICE_BASE_WEIGHT = 2370326`;
- `PLUCKER_BUDGET_EXACTLY_SATURATED = true`;
- `INVARIANT_CANONICAL_SUBSERIES_WEIERSTRASS_ROUTE_EXCLUDES_O266 = false`;
- `DISTINGUISHED_DEGREE133_PENCIL_WRONSKIAN = UNTESTED`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No distinguished pencil in `|A|` is constructed.
- The pullback subsystem is not confused with the full canonical series of `Y`.
- Pluecker saturation is a structural identity, not evidence that the hypothetical carrier exists.
- No Stage32 MAIN, hostile-audit, merge, endpoint, lower-O, or Perfect Cuboid credit follows.
