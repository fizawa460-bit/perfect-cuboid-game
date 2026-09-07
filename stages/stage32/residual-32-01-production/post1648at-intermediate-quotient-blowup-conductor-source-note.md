# Stage32 post1648AT — intermediate residual quotient, blowup model, and conductor split

Scratch-only correction/source-lock leaf. This leaf refines AP/AQ/AS by inserting the actual intermediate quotient surface between the resolved box surface and `P1 x P1`. It also corrects a tempting but wrong interpretation of the composite canonical discrepancy: exceptional curves fixed as **labels** by node inertia are not divisorial ramification, because the inertia acts nontrivially on the exceptional coordinate. No MAIN authority or theorem/receiver/route/endpoint credit is changed.

## Parent locks

- AP canonical SHA256: `35c1f8ff265250ccda9bd44f0ce815022e7fde1f30120ba18722a6cf12bb8b3d`.
- AQ canonical SHA256: `1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e`.
- AS finalized scratch head: `ce27a8aac8094c5b503ef1020306fa2e1d4a5d70`.
- AS canonical SHA256: `3211e758e5b4ec4e96e91b8844a0de429f08fb031e1fd99ba01ac0f9ccea5907`.

Primary geometry remains Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), DOI `10.1307/mmj/1480734014`, through the AM/AQ/AS source locks.

Write `S` for the minimal resolution of the box surface and `H ~= (Z/2)^3` for AQ's source-identified residual factor-pair deck group. Let

`q : S -> Y := S/H`

and let

`pi : Y -> P1 x P1`

be the remaining contraction in the factor-pair map.

## Local quotient is a blowup, not extra divisorial ramification

At a resolved box cusp use the AS local chart

`x=p^2`, `y=pq`, `z=q^2`, `xz=y^2`, `u=y/x`,

so `z=x*u^2` and the exceptional curve is `x=0`. The nontrivial cusp inertia acts

`(x,u) -> (x,-u)`.

Hence the local quotient has coordinates

`X=x`, `v=u^2`,

and the factor-pair target coordinates satisfy

`Z=z=x*u^2=X*v`.

Thus locally `Y -> P1 x P1` is exactly the blowup chart of the target cusp point: `X=x`, `v=Z/X`. In particular:

- the quotient is smooth at this chart;
- the image of the exceptional curve is a `(-1)`-curve;
- the exceptional generic point is **not** ramified under `q`, since `u -> -u` is nontrivial there;
- the fixed divisorial locus is the boundary direction `u=0` (and the symmetric chart gives the other boundary direction).

Globally AQ gives 12 `H`-orbits of exceptional curves, each orbit of size four. If `Ebar` is the quotient image of one such orbit, then generically the four `(-2)` curves are unramified and

`q^*Ebar = E1+E2+E3+E4`.

Therefore

`8*Ebar^2 = (q^*Ebar)^2 = 4*(-2) = -8`,

so `Ebar^2=-1`. Contracting the 12 quotient exceptional curves gives the source-locked factor target `P1 x P1`.

## Correct ramification divisor for q

The modular cover `C8 -> X(4)` is unramified on the interior; residual ramification occurs at the compactification cusps. On `S`, the divisorial ramification of `q` is therefore the union of the 12 Satake-boundary elliptics, not the 48 exceptional curves.

For the V6 class, the boundary labels 33--44 have intersections

`[11,26,31,22,16,26,25,11,28,40,34,22]`,

whose sum is

`R_boundary . C = 292`.

AS partitions these 12 boundary labels among the three node-inertia elements. Their boundary intersection sums are respectively

- labels `[33,34,35,36]`: `90`;
- labels `[37,38,39,40]`: `78`;
- labels `[41,42,43,44]`: `124`.

The accompanying exceptional mass sums `96,108,62` make each **setwise fixed-curve block** intersect C in 186, but those exceptional terms must not be inserted into the ramification divisor. This is the scope correction made by AT.

Riemann--Hurwitz for the smooth surface quotient gives

`K_S = q^*K_Y + R_boundary`.

Since AP has `K_S.C=186`, the birational image curve `C_Y=q(C)` satisfies

`K_Y.C_Y = C.(K_S-R_boundary) = 186-292 = -106`.

## Arithmetic genus on the intermediate quotient

AQ gives the orbit sum

`S_C = sum_{h in H} hC`

with

`S_C^2 = 80352`.

AP proves that the full factor-pair map is birational on the hypothetical carrier, hence `q|_C` is birational as well. Therefore

`q^*C_Y = S_C`

and, since `deg(q)=8`,

`C_Y^2 = 80352/8 = 10044`.

Adjunction on the smooth intermediate surface gives

`p_a(C_Y) = 1 + (C_Y^2 + K_Y.C_Y)/2`
`         = 1 + (10044-106)/2`
`         = 4970`.

The normalization genus is still one, so

`delta(C_Y)=4969`.

The V6 strict transform on `S` has arithmetic genus 473 and intrinsic delta 472. Hence the residual finite quotient contributes exactly

`4969-472 = 4497`

additional conductor length.

Equivalently, using AQ/AS pairwise intersections,

`4497 = (9286-292)/2`.

The three node-inertia contributions split as

- `(1360-90)/2 = 635`;
- `(1286-78)/2 = 604`;
- `(1498-124)/2 = 687`;

and the four non-node elements contribute

`1112/2 + 1266/2 + 1284/2 + 1480/2 = 2571`.

Thus `635+604+687+2571=4497`.

## Blowdown contribution to P1 x P1

AQ gives 12 target-cusp multiplicities

`m = [35,24,18,19,28,21,25,34,20,5,5,32]`,

with

`sum m_i = 266`,
`sum m_i^2 = 6966`.

The AQ exceptional correction `P-S_C` is constant on each four-curve exceptional orbit with exactly these coefficients. Under the local blowup identification this is precisely

`pi^*D = C_Y + sum_i m_i Ebar_i`,

where `D` is AP's bidegree `(81,105)` image in `P1 x P1`.

Consequently

`D^2-C_Y^2 = sum m_i^2 = 6966`,

and

`K_Y.C_Y = K_{P1xP1}.D + sum m_i`
`         = -2*(81+105) + 266`
`         = -106`,

independently recovering the quotient calculation above.

The arithmetic-genus jump under the 12 blowdowns is

`p_a(D)-p_a(C_Y)`
`= (sum(m_i^2-m_i))/2`
`= sum binom(m_i,2)`
`= (6966-266)/2`
`= 3350`.

Since AP has `p_a(D)=8320` and `delta(D)=8319`, this gives

`4970+3350=8320`,
`4969+3350=8319`.

Finally the AP conductor demand splits exactly as

`7847 = 4497 + 3350`.

The composite canonical-discrepancy term `558` must therefore be read as

`558 = 292 + 266`

(boundary ramification plus blowup exceptional mass), **not** as `3*K.C`.

## Decision / firewall

This exact factorization is structural, not exclusionary. It explains all of AP's conductor demand rather than bounding it below the required value. The missing input after AS remains member-level landing/jet information or some independent global restriction on the singularities of `C_Y`/`D`.

- `V6_carrier_excluded=false`.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- scratch only; shared `MAIN-STATE.json` and Stage32 authority unchanged.
