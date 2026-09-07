# Stage32 post1648AO — factor-special-fibre Hurwitz budget

Scratch-only necessary-condition adapter. This leaf combines the AM source-locked factor fibrations with the exact V6 intersections against their six multiplicity-two boundary components. It strengthens the required surface-node branch count for a hypothetical integral geometric-genus-1 V6 carrier. It does not construct or exclude such a carrier and grants no MAIN theorem/receiver/route/endpoint credit.

## Parent locks

- AM finalized scratch head: `a09446f18019cc866e5303bdc352710a9831a36b`.
- AM canonical SHA256: `184debdb65c679242fadcc1e1ca176faf720c651b67f09368bc45c14dabb44c8`.
- AN finalized scratch head: `3806f6476bf96d23b93558cfa78d67cf72bda3d0`.
- AN canonical SHA256: `fc2568ae2cb6df0c0da319950a7e5b8edb7b9e356812c2f3d86c575593883a29`.
- V6 witness canonical SHA256: `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`.

## Factor base is genus zero

AM source-locks the two factor maps
`g_i : B -> Z`, where `Z=C8/G=H*/Gamma[4]` and `G=Gamma[4]/Gamma[8]`.

The genus of `Z=X(4)` is checked directly from the standard compact modular-curve genus formula. Since `-I` is not in `Gamma[4]`,
the PSL index is

`mu = (1/2)*4^3*(1-1/2^2)=24`.

For `Gamma[4]` the cusp count is

`c = (1/2)*4^2*(1-1/2^2)=6`.

Principal level 4 is torsion-free, hence there are no elliptic points of orders 2 or 3. Therefore

`g(Z)=1+mu/12-c/2=1+2-3=0`.

No table lookup or point-classification theorem is used in this step.

## FSM/AM special fibres

Primary geometry remains Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), DOI `10.1307/mmj/1480734014`.

Relevant retained locators are AM's:
- Theorem 2.4 and Section 2: `B` is the diagonal modular quotient and `G=Gamma[4]/Gamma[8]`.
- Proposition 2.7: the Satake boundary is 12 smooth elliptic curves from the two factor directions, each through 8 singular cusps.
- the local node quotient `(p,q)->-(p,q)` and AM's resolution calculation.
- AM proves six boundary elliptics in each factor direction and the resolved special-fibre formula
  `F_E = 2E + sum(8 incident exceptional curves)`.

The six special fibres in one factor direction are distinct. Their exceptional components partition the 48 exceptional curves: an irreducible exceptional curve cannot be a component of two distinct fibres of the same morphism, while the six fibres contain `6*8=48` exceptional components in total.

AM semantically identifies the two fibre classes and gives the unordered V6 fibre degrees `{81,105}`.

## Exact boundary intersections

From the V6 all140 pairing vector, boundary labels 33--44 have intersections

`[11,26,31,22,16,26,25,11,28,40,34,22]`.

AM's degree-81 six-pack is labels `[33,36,37,40,41,44]`, so

`q_81 = 11+22+16+11+28+22 = 110`.

AM's degree-105 six-pack is labels `[34,35,38,39,42,43]`, so

`q_105 = 26+31+26+25+40+34 = 182`.

As an independent fibre-class consistency check, with exact exceptional mass `e=266`,

`6*81 = 2*q_81 + e = 486`,
`6*105 = 2*q_105 + e = 630`.

## Hurwitz budget

Assume a hypothetical integral V6 carrier has normalization `Cbar` of genus 1. Restrict either factor fibration to obtain a finite map

`h_i : Cbar -> Z ~= P1`

of degree `n_i` (81 or 105). Riemann--Hurwitz gives total ramification

`R_i = 2*n_i`.

Fix one factor direction and its six special fibres. At a normalization point over such a fibre, let:
- `a>=0` be its local intersection multiplicity with the exceptional component, if present;
- `b>=0` be its local intersection multiplicity with the multiplicity-two boundary elliptic component, if present.

The source-locked fibre divisor has local pullback order `a+2b`, hence the ramification contribution is `a+2b-1` whenever `a+2b>0`.

If `a>0`, then
`a+2b-1 >= (a-1)+b`.
If `a=0,b>0`, then
`2b-1 >= b`.

Let `B` be the total number of normalization preimages over the 47 met surface nodes. Summing over the six special fibres:
- the exceptional `a`-mass is exactly `e=266`;
- subtracting one for each exceptional preimage gives `e-B`;
- the total boundary `b`-intersection is `q_i`.

Therefore

`R_i >= e - B + q_i`.

Since `R_i=2n_i`,

`B >= e + q_i - 2n_i`.

For the two directions this gives

- degree 81: `B >= 266+110-162 = 214`;
- degree 105: `B >= 266+182-210 = 238`.

Hence every hypothetical integral geometric-genus-1 V6 carrier must have at least

`B >= 238`

normalization preimages over its 47 met box-surface nodes, i.e. surface-node branch excess at least

`238-47 = 191`.

## Distinct multibranch nodes

At a met node with exceptional mass `M`, at most `M` normalization branches can lie over it, so making that node multibranch can increase the branch count above the one-branch baseline by at most `M-1`.

For the exact V6 exceptional vector, the 23 largest values of `M-1` sum to `190`, which is insufficient for the required excess 191. The 24 largest sum to `194`.

Thus at least

`24`

distinct met surface nodes must be multibranch.

This is a necessary condition only. It does not assert that a 24-node configuration is globally realizable, does not force exceptional landing collisions, and does not turn the genus-defect 472 into exceptional mass.

## Firewalls

- Scratch only; shared `MAIN-STATE.json` and Stage32 authority remain unchanged.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit.
