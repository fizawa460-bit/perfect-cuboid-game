# Stage32 scratch — Cecotti B.7/B.8 branch-marked J[2] to retained W

Status: scratch exact finite diagnostic only. No MAIN authority, claim-DAG, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Why this route

The previous order-8 reentry leaf reduced the absolute-marking problem to source-binding a named Bolza curve automorphism to a specific retained lattice element. A direct KKK homology-basis comparison is possible in principle, but it is stronger than needed for the mod-2 question.

For the absolute Q602 residue selector we only need the action on `J[2]`. Cecotti Appendix B already supplies, in one source, both:

- the retained principal G12 matrices `b3`, `b4` and the ordered abstract generators `S=b4`, `T=-b3` in (B.1)--(B.4);
- the same Bolza curve `y^2=x^5-x` and explicit curve automorphisms B.7 and B.8.

Therefore the six branch points can be used directly to build a branch-marked `J[2]` model, with no KKK integral-homology extraction in this leaf.

External source: Sergio Cecotti, *Symplectic Singularities, Color Confinement, and the Quantum Dirac Sheaf*, arXiv:2509.24605v1, Appendix B, equations (B.1)--(B.9).

The source does **not** explicitly state that the displayed B.7 and B.8 curve automorphisms are the particular retained generators `S` and `T`. That missing semantic binding remains the firewall.

## Exact branch actions

For `y^2=x^5-x`, the Weierstrass points are

`{0, infinity, 1, -1, i, -i}`.

B.7 has

`x -> -(x+i)/(1+i*x)`

and therefore

- `0 -> -i`, `infinity -> i`;
- `1 <-> -1`;
- `i -> infinity`, `-i -> 0`.

B.8 has

`x -> i*(x-1)/(x+1)`

and therefore

- `0 -> -i`, `infinity -> i`;
- `1 -> 0`, `-1 -> infinity`;
- `i -> -1`, `-i -> 1`.

On the retained pair partition

- `Z1={1,-1}`;
- `Z2={i,-i}`;
- `Z3={0,infinity}`;

this gives

- B.7: `Z1` fixed, `Z2 <-> Z3`;
- B.8: `Z1 -> Z3 -> Z2 -> Z1`.

This is exactly the same labelled permutation pattern as the retained mod-2 action

- `S=b4`: `L1` fixed, `L2 <-> L3`;
- `T=-b3`: `L1 -> L3 -> L2 -> L1`.

## Full J[2] intertwiner enumeration

Use the standard hyperelliptic description

`J[2] = {even subsets of the six Weierstrass points}/(subset ~ complement)`

with basis

`(delta_0inf, delta_1inf, delta_-1inf, delta_iinf)`.

The replay script enumerates all `4x4` matrices over `F2` and keeps exactly the invertible matrices `P` satisfying

`P*B7 = S*P`,

`P*B8 = T*P`.

There are exactly **2** such `GL4(F2)` intertwiners. Both send

- `Z1 -> L1`;
- `Z2 -> L2`;
- `Z3 -> L3`.

Because the enumeration is over all invertible intertwiners, any symplectic intertwiner is a subset of these two and has the same three pair-line images.

Thus, conditional on a source-bound ordered identification `B.7 <-> S`, `B.8 <-> T`, the absolute line is forced:

`delta_0inf = Z3 -> L3 -> residue 235`.

No residual `L1/L2/L3` ambiguity survives that ordered generator binding.

## Complex representation compatibility

On the holomorphic differential basis `(dx/y, x*dx/y)`, direct pullback gives an ordered B.7/B.8 representation that is simultaneously conjugate over `Q(i,sqrt(2))` to `(S,T^-1)`.

The inverse on `T` is the expected contravariance between pullback on differentials and the point/homology action. This is a nontrivial compatibility check, but it is **not** promoted to an integral symplectic marking.

## Remaining exact gap

The new minimal reentry datum is now only:

`SOURCE_BIND_THE_ORDERED_CURVE_AUTOMORPHISM_PAIR_B7_B8_TO_THE_RETAINED_PRINCIPAL_GENERATOR_PAIR_S_T_OR_SUPPLY_AN_EQUIVALENT_MARKED_JACOBIAN_ADAPTER`.

Until that datum is supplied, the conclusion `delta_0inf=L3`, hence residue `235`, remains conditional scratch mathematics only.

Replay:

`python3 stages/stage32/scratch/diagnose_stage32_b7_b8_j2_retained_w_intertwiner.py`
