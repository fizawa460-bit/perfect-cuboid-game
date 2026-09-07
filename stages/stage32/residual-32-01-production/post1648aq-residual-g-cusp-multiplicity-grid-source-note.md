# Stage32 post1648AQ — residual deck action and cusp multiplicity grid source lock

Scratch-only source-lock adapter. This leaf identifies the retained order-eight boundary stabilizer with the residual modular deck group of the factor-pair map, reconstructs the exact V6 orbit sum on Picard, and resolves the gap between the strict-transform orbit sum and the full pullback as an effective exceptional divisor. It then interprets the exceptional coefficients as multiplicities of the birational image curve at the target cusp points.

This is a necessary-structure leaf only. The resulting cusp multiplicity and factor-fibre budgets are feasible; V6 is not excluded here. Shared Stage32 MAIN authority is unchanged.

## Parents

- AP finalized scratch head: `cc6f38d5e6706aabdf134294d6213a5d92d199f6`.
- AP canonical SHA256: `35c1f8ff265250ccda9bd44f0ce815022e7fde1f30120ba18722a6cf12bb8b3d`.
- AO finalized scratch head: `aa57ac29404bae75f93aadcd4e134cba9eb91563`.
- AO canonical SHA256: `39e217c7223732b1834b7e9b96b4361807227f823a5624842a97eddf71390378`.
- V6 witness canonical SHA256: `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`.

The permanent retained Picard payload modules remain runner-side imports only and are not copied into this note.

## Primary modular source and full automorphism source lock

Primary geometry is Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675--691, DOI `10.1307/mmj/1480734014`.

Exact locators used:

- Theorem 2.4, printed p.7: the complex box variety is the diagonal modular quotient.
- Section 2, printed p.6: `G=Gamma[4]/Gamma[8] ~= (Z/2)^3`.
- printed p.7: the modular automorphisms together with factor swap give a subgroup of order 1536, and the full automorphism group has order 1536.
- Proposition 2.7, printed p.9: the Satake boundary consists of exactly 12 smooth elliptic curves.
- the local node calculation, printed pp.7--8: near a singular cusp, `p,q` are source parameters, diagonal `(-1)` sends `(p,q)->(-p,-q)`, and the box node is `C^2/{+/-1}`.

The retained automorphism permutations are source-locked to Michael Stoll's verification repository, exact commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, file `Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`, raw SHA256 `5dc3ae961d872ff96420385880edf0f4225a12d3f906c614e1ccd2220399ce89`. That source explicitly sets up the automorphism action on `Pic(S)` and forms `AutS`; its verification output has `#Aut(S)=1536`.

The retained action closes to order 1536 as well, so these source-bound geometric permutations realize the full automorphism group on the retained 140 curves.

## Identifying the residual deck group inside retained Aut

Put `C8=H*/Gamma[8]` and `G=Gamma[4]/Gamma[8]`. The diagonal quotient description is

`B = (C8 x C8)/G_diag`.

Since `G` is abelian, the quotient

`Hsrc := (G x G)/G_diag ~= G ~= (Z/2)^3`

acts on `B`, with quotient

`B/Hsrc = (C8/G) x (C8/G) = Z x Z`.

This is the residual degree-eight deck action behind AP's factor-pair map. It lifts uniquely to the minimal resolution.

AM identifies the 12 retained boundary elliptics, labels 33--44, as the two six-packs of special-fibre boundary components for the two factor maps. The residual action is over `Z x Z`, hence preserves every factor fibre. Each of the 12 special fibres has a unique nonexceptional boundary elliptic component, so `Hsrc` fixes each of labels 33--44 as a curve.

Inside the retained full automorphism group, the pointwise stabilizer of labels 33--44 has exactly 8 elements, with element-order histogram `{1:1,2:7}`. Therefore the source residual deck group is exactly this retained subgroup:

`Hsrc = Stab_Aut({33},...,{44})`.

This is an exact semantic identification, not an arbitrary order-eight subgroup choice.

## Exact V6 orbit and full pullback correction

For this residual group `H`, the V6 Picard class has orbit size 8. The seven nonidentity intersection numbers are

`[1112,1266,1284,1286,1360,1480,1498]`

with sum `9286`.

Let `F81` and `F105` be the AM source-bound fibre classes characterized by

`C.F81=81`, `C.F105=105`.

AP's birational image `D` has bidegree `(81,105)`. With fibre-class conventions, the full pullback of the divisor class of `D` is

`P = 105*F81 + 81*F105`.

It satisfies

`P^2 = 136080 = 8*(2*81*105)`,
`C.P = 17010 = 2*81*105`.

Let

`S = sum_{h in H} hC`.

The retained Picard replay gives

`S^2=80352`, `C.S=10044`.

The missing divisor

`T=P-S`

lies uniquely in the span of the 48 exceptional curves and is effective. Its coefficients, in exceptional labels 93--140, are

`[5,5,5,5,5,5,5,5,21,21,21,21,25,25,25,25,24,24,24,24,18,18,18,18,19,19,35,35,35,35,19,19,28,28,34,34,34,34,28,28,32,32,20,20,20,20,32,32]`.

They have sum 1064, maximum 35, and positive support 48. Moreover

`C.T=6966`, `T^2=-55728`, `S.T=55728`.

The opposite coefficient convention `81*F81+105*F105` does not differ from `S` by an exceptional class, providing an independent orientation check.

## Local meaning of the exceptional coefficients

At a source singular cusp, use `p,q` upstairs. The diagonal node quotient has invariant coordinates

`x=p^2`, `y=pq`, `z=q^2`, with `xz=y^2`.

For the factor-pair quotient to `Z x Z`, local target parameters are

`u=p^2=x`, `v=q^2=z`.

On the A1 resolution chart

`y=xw`, `z=xw^2`,

the target map is

`(x,w) -> (u,v)=(x,xw^2)`.

If `D` has local reduced equation `f(u,v)=0` of multiplicity `m` at the target point, then

`f(x,xw^2)`

has exceptional order exactly `m`: the least power of `x` is the least total degree of a monomial of `f`. Therefore the coefficient of an exceptional curve in `P-S` is exactly the multiplicity of `D` at the corresponding target point.

The residual group has 12 orbits on the 48 exceptional curves, all of size 4. Hence the 48 nodes map to 12 target cusp points. Their image multiplicities are

`[35,24,18,19,28,21,25,34,20,5,5,32]`

up to ordering by the retained factor-cusp grid, and sum to 266. In every orbit the image multiplicity also equals the sum of the V6 exceptional masses over the four nodes in that orbit.

For a reduced plane curve singularity of multiplicity `m`, the first blowup contributes `m(m-1)/2` to delta. The 12 target cusp multiplicities therefore force only

`delta_cusp >= 3350`,

which is compatible with AP's total `delta(D)=8319`.

## Factor-fibre intersection budgets

Using the retained boundary incidence, the six degree-81-direction special fibres receive target-cusp multiplicity sums

`[59,37,49,59,25,37]`

for labels `[33,36,37,40,41,44]`.

The six degree-105-direction special fibres receive

`[53,43,53,55,25,37]`

for labels `[34,35,38,39,42,43]`.

Every sum is at most the corresponding projection degree. Thus the elementary factor-fibre Bezout budget does not exclude the image.

## Conductor decomposition

AP requires conductor length 7847. AQ decomposes this number exactly:

`sum_{h != 1} C.hC = 9286`,
`C.T = 6966`.

The canonical contribution changes from `K_B.C=186` to
`K_(P1xP1).D=-2*(81+105)=-372`, a difference of `558`. Hence adjunction gives

`(9286 + 6966 - 558)/2 = 7847`.

So the global intersection/conductor route is an identity after the exceptional correction is included; it is not by itself an upper-bound contradiction.

## New branch-count consequence and next route

AO gives at least `B=238` normalization preimages over the met surface nodes, while total exceptional intersection mass is 266. If the local exceptional multiplicities of these branches are `a_j>=1`, then

`sum_j(a_j-1)=266-B <= 28`.

Therefore at least `B-28 >= 210` of those node branches have exceptional multiplicity exactly one. The hypothetical carrier is consequently forced into a near-transverse regime at the exceptional divisor.

The next exact route is to source-lock the residual deck action on the local exceptional coordinate `w` and determine whether the at-least-210 transverse branches can choose enough distinct target tangent directions across the 12 cusp points. A forced tangent collision would increase local delta beyond the first-blowup budget and is the remaining plausible closure mechanism.

## Firewalls

- Scratch only; shared `MAIN-STATE.json` and Stage32 authority are unchanged.
- `V6_carrier_excluded=false`.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit is granted.
