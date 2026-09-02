# Stage32 post-1484 O=210 q'=4 six-cusp Hurwitz reduction

Scope: fixed recovered V6 class `g1-d186` only. This note consumes the hostile-audited post-#1484 boundary canonical `791870c37681702392e1e59d224f494ed791709d467efa68a20cf49bff4ab420`. It does not reopen O=188 and does not claim O=210 exclusion.

## Retained inputs

The audited boundary fixes `q'=4`, modular factor degrees `(105,81)`, source projection ramification `(0,192)`, descended ramification `(0,48)`, and the unique zero-defect exceptional-contact histogram `210 x m1 + 28 x m2`.

Reuse only the formal part of the audited q'=4 V4 descent authority `post1473-o188-q4-genus2-descent-source-note.md` (blob `ac85353c...`): the V4 torsor square is Cartesian, finite degree is preserved under the etale base change `X(8)->C0`, and ramification degree divides by four. Do not reuse its superseded O=188 numerical values `93/93` or ramification `2/2`.

The retained V4 quotient certificate fixes

- `C0=X(8)/(Gamma'[4]/Gamma[8])`, genus 2;
- `X(8)->C0` finite etale of degree 4;
- `C0->X(4)` of degree 2;
- `X(4)` genus 0;
- the six quotient cusps are exactly the six branch/Weierstrass points of `C0->X(4)`.

Hence at O=210 the descended curve `Y` has `g(Y)=1+210/2=106` and carries simultaneous maps

`f_z:Y->C0`, degree 105, ramification 0,

`f_w:Y->C0`, degree 81, ramification 48.

The first map is therefore etale. The old odd-etale self-correspondence obstruction cannot be reused here: its commensurator proof required both projections to be etale, whereas `f_w` has ramification 48.

## Double-base-change local lemma

For the first factor, use the same normalized Beauville/base-change local model already source-locked by the cusp adapter. Let a point of `N` above one of the six branch values of `C0->X(4)` have local degree `e` for `N->X(4)`. Locally the normalized fiber product is the normalization of

`t^e=s^2`.

Write `g=gcd(e,2)`. The normalization has `g` local branches, and on each branch the map to the `s`-line has ramification index `e/g`. Therefore the normalized base-changed map is unramified exactly for `e=1` or `e=2`. Away from the six branch values, the degree-two base change is etale, so any ramification of `N->X(4)` would survive in `Y->C0`.

Since `f_z` is etale, the degree-105 map `N->X(4)=P1` is therefore branched only over the six modular cusp values, and every ramification point is simple (`e=2`). Riemann--Hurwitz for genus-one `N` gives total ramification

`R = 2*105 = 210`.

Thus its six branch permutations are involutions in `S_105`, with a total of exactly 210 transpositions and 210 fixed points. For each cusp `j`, write the cycle type as

`2^{r_j} 1^{s_j}`, with `2 r_j + s_j = 105`.

The six permutations must generate a transitive action and have product identity.

## Exact V6 decomposition of the 210 transpositions

For the six first-factor boundary labels, the audited resolved-fiber certificate has

`C.L = (26,31,26,25,40,34)` for labels `(34,35,38,39,42,43)`.

Their sum is 182. Because the first normalized base change is etale, every strict-boundary contribution to the degree-105 cusp fiber must be a simple `e=2` point on `N`; higher local degree would ramify `Y->C0`. These strict-boundary intersections therefore account for 182 of the 210 transpositions.

The O=210 zero-defect histogram supplies exactly 28 exceptional `m=2` contacts. For the first projection, zero ramification forces local `A_1=2`, so each is one additional simple `e=2` point. Hence

`182 + 28 = 210`

is an exact geometric decomposition, not merely the coarse RH total.

Let `k_j` be the number of `m=2` contacts incident to first cusp `j`. Then

`sum_j k_j = 28`,

`r_j = C.L_j + k_j`,

`s_j = 105 - 2 r_j`.

Grouping the retained 48 exceptional capacities by the audited first-factor incidence and replaying all `m1/m2` node splits compresses the `43949136035405189` weighted node assignments to exactly `214239` distinct first-cusp cycle-type vectors. The accompanying certifier source-locks that quotient and the per-cusp ranges.

## New exact leaf

The vague leaf “degree-105 etale first projection geometry” is now reduced to a concrete Hurwitz compatibility problem:

1. for one of the 214239 reachable cycle-type vectors, determine whether six involutions in `S_105` with those cycle types can form a transitive product-one tuple;
2. if such tuples survive, impose the simultaneous degree-81 map `Y->C0` with ramification 48 and the common Beauville/V4 geometry.

This note does not assert that every permutation tuple is algebraically realized by the fixed modular six branch values. Conversely, failure to exclude the permutation tuples is not carrier existence.

## Firewalls

- O=188 remains CLOSED_AUDITED and must not be reopened.
- O=210 is not excluded by this note.
- FULL178 remains inactive.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit is released.
- Promotion of this reduction requires its own bounded hostile audit.
