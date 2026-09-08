# Stage32EX6 — full order-8 descent of the projective-connection budget to genus one

Status: `SCRATCH_EXACT_BOUNDED_FULL_H_GENUS1_PROJECTIVE_DESCENT_NO_ENDPOINT_CREDIT`.

This is the fifteenth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266`, with normalization `N`, and the exact `q'=4` normalized product-cover component `D` used throughout EX6.

Retained Stage32 inputs source-lock:

- `P=X(8) x X(8)` maps to the box variety by a diagonal order-eight quotient group `H ~= (Z/2)^3`;
- its free subgroup `V4 ~= (Z/2)^2` gives the Beauville quotient `P->X`;
- the residual quotient `X->B` has degree two and is ramified along the resolved exceptional divisor;
- exact V6 factor degrees force `q'=4`, hence `deg(D->N)=2q'=8`;
- at O266 every one of the 266 exceptional contacts has multiplicity one and is odd;
- `D->N` has four points above each O266 node branch, each with local ramification index two;
- away from O-contacts, `D->N` is unramified.

Previous scratch inputs establish the intrinsic meromorphic quadratic differential

`Theta = pi81^*P_X8 - pi105^*P_X8`

on `D`, its invariance under the free V4 subgroup, exact double poles at one-cusp smooth lifts, and regularity at all O266 node lifts.

The question here is whether `Theta` descends through the full order-eight action to a meromorphic quadratic differential on the genus-one normalization `N`, and what branch-level divisor budget results.

## Full connected order-eight pullback

The retained product quotient has generic Galois group `H` of order eight. The chosen normalized component `D` has generic degree eight over `N`.

Therefore the connected component already has full generic degree `|H|`; equivalently it is the full connected normalized pullback of the order-eight quotient along the hypothetical carrier. The diagonal modular action of `H` stabilizes `D`, and the quotient is `N`.

This statement is only about the same conditional hypothetical carrier. It does not assert existence of such a carrier.

## H-invariance of Theta and meromorphic descent

Every element of `H` acts diagonally by modular automorphisms on the two `X(8)` factors. The uniformizing projective connection on `X(8)` is preserved by those modular automorphisms. Hence for every `h in H`,

`h^*Theta = Theta`.

At the function-field level, an H-invariant rational quadratic differential on the smooth curve `D` descends uniquely to a meromorphic quadratic differential `barTheta` on the quotient normalization `N` such that

`Theta = f^*barTheta`,

where `f:D->N`.

For quadratic differentials the divisor relation is

`div(Theta) = f^*div(barTheta) + 2 R_f`,

with `R_f` the ramification divisor of `f`.

At O266 there are four ramification points of index two above each of the 266 node branches, so

`deg R_f = 4*266 = 1064`.

This exactly matches Riemann--Hurwitz:

`2g(D)-2 = 1064`

for `g(D)=533` and `g(N)=1`.

## Node descent: regular upstairs becomes at most simple pole downstairs

Near an O266 node lift use a source parameter `s` with residual inertia `s->-s` and downstairs parameter `t=s^2`.

Write locally

`Theta = theta(s) (ds)^2`.

H-invariance under the node stabilizer makes `theta(s)` even. If `ord_s Theta=m>=0`, then from `dt=2s ds`,

`ord_t barTheta = (m-2)/2`.

Hence an upstairs-regular node lift (`m>=0`) yields downstairs order at least `-1`: every O266 node point is at worst a simple pole of `barTheta`.

In particular the 266 node branches contribute at most

`266`

to the pole degree of `barTheta`.

## Smooth-boundary poles descend exactly

Previous scratch plus retained AR gives the exact smooth-boundary normalization-point counts

- `s81 = 58+rho81`;
- `s105 = 154+rho105`.

The two factor boundary families are disjoint away from node geometry, so there are exactly

`212 + Rrho`,

where `Rrho=rho81+rho105`, one-cusp smooth points on `N`.

The cover `D->N` is unramified there, and the eight lifts each carry an exact double pole of `Theta`. Therefore `barTheta` itself has an exact double pole at every such normalization point.

Thus the exact smooth-boundary pole contribution downstairs is

`P_smooth(barTheta) = 2*(212+Rrho) = 424+2Rrho`.

## Off-special pole allowance downstairs

Away from the six special fibres, retained post1715 gives ramification degree `rho81` and `rho105` for the two normalization factor maps. The union of those off-special ramification supports therefore has at most `Rrho` points.

At any such interior point the projective-connection difference has pole order at most two. Hence the additional off-special pole contribution of `barTheta` is at most

`2Rrho`.

Combining node, smooth-special and off-special species gives

`424+2Rrho <= deg Pole(barTheta) <= 690+4Rrho`.

Since the O266 slack gives

`0<=Rrho<=80`,

the uniform bound is

`deg Pole(barTheta) <= 1010`.

The lower bound already forces `barTheta !=0`.

## Genus-one zero capacity

Because `g(N)=1`, `deg K_N^2=0`. Therefore for nonzero meromorphic `barTheta`,

`deg Zero(barTheta) = deg Pole(barTheta)`.

Consequently

`deg Zero(barTheta) <= 690+4Rrho <=1010`.

This is the genus-one quotient form of the previous upstairs `8080` capacity. It is not an independent stronger inequality; the ramification correction accounts exactly for the difference.

## General r-flat branch capacity

At an FSM-minimal node branch, suppose the first `r` higher odd coefficients vanish on its product-cover lifts:

`mu1=...=mur=0`.

Previous local jet analysis gives upstairs

`ord_s Theta >= 2r`.

The ramified quotient formula then gives downstairs

`ord_t barTheta >= r-1`.

Such an r-flat branch is therefore a zero of `barTheta` of order at least `r-1`, and in particular it is not one of the possible node simple poles.

Let `B_r` be the number of r-flat FSM-minimal downstairs branches. Starting from the uniform node pole allowance 266, every r-flat branch removes one possible simple-pole unit. Hence

`deg Pole(barTheta) <= 690+4Rrho-B_r`.

Since the same branches force at least `(r-1)B_r` zeros and `deg Zero=deg Pole`, one gets

`(r-1)B_r <= 690+4Rrho-B_r`,

therefore the exact branch-capacity formula

`B_r <= floor((690+4Rrho)/r)`.

This directly reproduces the previous V4-orbit thresholds:

- `r=4`: all 186 minimal branches would contradict only for `Rrho<=13`;
- `r=5`: all 186 would contradict only for `Rrho<=59`;
- `r=6`: uniformly
  `B_6 <= floor(1010/6)=168`,
  so at least `186-168=18` minimal branches are not projectively six-flat.

Thus the full H/genus-one descent is an exact conceptual compression, not a new numerical endpoint closure beyond the V4-orbit result.

## Decision

Canonical scratch decisions:

- `D_TO_N_FULL_GENERIC_DEGREE8_CONNECTED_PULLBACK = true`;
- `THETA_FULL_H_INVARIANT = true`;
- `THETA_DESCENDS_TO_MEROMORPHIC_QUADRATIC_DIFFERENTIAL_ON_N = true`;
- `D_TO_N_RAMIFICATION_DEGREE = 1064`;
- `DOWNSTAIRS_NODE_POLE_ORDER_MAX = 1`;
- `DOWNSTAIRS_NODE_POLE_DEGREE_MAX = 266`;
- `DOWNSTAIRS_SMOOTH_BOUNDARY_POLE_DEGREE_EXACT = 424+2*Rrho`;
- `DOWNSTAIRS_OFFSPECIAL_POLE_DEGREE_MAX = 2*Rrho`;
- `BART_HETA_POLE_DEGREE_UPPER = 690+4*Rrho`;
- `BART_HETA_ZERO_DEGREE_UPPER = 690+4*Rrho`;
- `BART_HETA_ZERO_DEGREE_UNIFORM_UPPER = 1010`;
- `R_FLAT_MINIMAL_BRANCH_CAP = floor((690+4*Rrho)/r)`;
- `SIX_FLAT_MINIMAL_BRANCH_UNIFORM_MAX = 168`;
- `PROJECTIVELY_NON_6_FLAT_MINIMAL_BRANCHES_UNIFORM_MIN = 18`;
- `GENUS1_DESCENT_STRICTLY_IMPROVES_V4_ORBIT_NUMERICS = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- The full-H action and quotient are used only for the same conditional full-degree connected pullback.
- `barTheta` is meromorphic; regularity upstairs at a ramification point does not imply regularity downstairs. Node simple poles are explicitly included.
- The genus-one bound is not double-counted as independent from the upstairs/V4 divisor budget; it is the quotient reformulation of the same geometry.
- No coefficient-flatness theorem is proved.
- No endpoint exclusion, lower-O descent, Stage32 MAIN credit, hostile-audit credit, merge, or Perfect Cuboid claim follows.
