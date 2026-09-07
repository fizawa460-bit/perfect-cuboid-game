# Stage32 post1648AM — source lock for the two Beauville/factor fibration classes

Scratch-only source-lock adapter. This note upgrades the retained Picard pattern in the AM diagnostic to a semantic identification of the two factor-fibration fibre classes. It gives necessary conditions for a hypothetical integral geometric-genus-1 V6 carrier only. It does not materialize or exclude such a carrier and grants no MAIN theorem/receiver/route/endpoint credit.

## Parent retained leaves

- post1648AL certificate: `stages/stage32/residual-32-01-production/post1648al-beauville-cover-projection-genus-bound.json`
- AL canonical SHA256: `ce2eafff49e379b87b8bc4d753dc28811b738becce32caf2f90b7495c6d6c316`
- AM successful diagnostic head: `ede8833d5284dc536dcdee3bef69113085156c17`
- AM diagnostic script blob SHA1: `b2b8a65ff028d0a30fe1b51de8227b0f2dca810b`
- AM diagnostic output blob SHA1: `ed95cfdb157104cfc56314986a48d17c09bc0347`

The two permanent retained Picard payload modules are not inspected in chat/context. They are consumed only by the runner-side diagnostic/verifier adapter.

## Primary source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`.

Author preprint:
`https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`

Exact locators used here:

- Theorem 2.4, printed p.7: the complexified box variety is the diagonal modular quotient `B ~= (H*/Gamma[8] x H*/Gamma[8]) / (Gamma[4]/Gamma[8])`.
- Section 2, printed pp.7–8: the first product cover has deck group `G = Gamma[4]/Gamma[8] ~= (Z/2)^3`; the 48 singular points are one cusp orbit; near `(infinity,infinity)` the translation `(z,w)->(z+4,w+4)` acts on `p=exp(2*pi*i*z/8), q=exp(2*pi*i*w/8)` by `(p,q)->-(p,q)`, giving the node `C^2/{+/-1}`.
- Proposition 2.7, printed p.9: the Satake boundary is the union of images of `H* x {a}` and `{a} x H*`, consists of exactly 12 smooth elliptic curves, and each boundary elliptic contains 8 singular zero-dimensional cusps.
- The discussion immediately after Proposition 2.9, printed p.9: the 32 rational curves, 12 Satake-boundary elliptics, and 48 nonboundary elliptics coincide with the 92 nonexceptional curves of Stoll–Testa; together with the 48 exceptional curves they generate Picard.
- Lemma 4.1 and Section 4, printed pp.12–13: `H = Gamma'[4]/Gamma[8] ~= (Z/2)^2` is an index-two subgroup of `G` acting freely on `C8=H*/Gamma[8]`; `X=(C8 x C8)/H_diag` is smooth and maps two-to-one to the box variety, and the resolved cover is ramified along the 48 exceptional curves.

The deductions below are elementary quotient/resolution and projection-formula adapters from those source-locked statements; they are not quoted as separate theorems of Freitag–Salvati Manni.

## Two factor directions and the 6+6 boundary split

Put `C8=H*/Gamma[8]`, `G=Gamma[4]/Gamma[8]`, and `Z=C8/G`. The two factor projections of `C8 x C8` descend through the diagonal `G`-quotient to two fibrations

`g1,g2 : B -> Z`.

Proposition 2.7 identifies every Satake-boundary elliptic as a special fibre component coming from one of the two source directions `C8 x {a}` or `{a} x C8`.

The factor-swap involution `(z,w)->(w,z)` is an automorphism of the box variety and exchanges the two directions. Since Proposition 2.7 gives 12 irreducible boundary elliptics in total and a one-dimensional horizontal component cannot equal a vertical component, there are exactly 6 boundary elliptics in each direction.

## Special-fibre class on the minimal resolution

Consider the source direction with local second-factor cusp parameter `q=exp(2*pi*i*w/8)`. At a cusp fixed by the order-two translation `w->w+4`, one has `q->-q`, so a local parameter on the quotient base `Z` is `t=q^2`. Hence the special fibre `t=0` has multiplicity 2 along the boundary elliptic.

At one of the 8 singular cusps lying on that boundary elliptic, use the source-locked node coordinates

`x=p^2, y=pq, z=q^2`, with `xz=y^2`.

Here the base parameter is `t=z`. Blowing up the `A1` node resolves it. In the chart `y=xu, z=xu^2`, the total transform is

`z = x*u^2`.

Therefore the exceptional curve occurs with multiplicity 1 and the strict transform of the boundary elliptic occurs with multiplicity 2. Repeating at the 8 singular cusps on the boundary elliptic gives the resolved special-fibre divisor

`F_E = 2 E + sum_{8 incident nodes} E_exc`.

The same argument applies to every boundary elliptic and to either factor direction.

Consequently all six boundary elliptics from one source direction give the same fibre class `F1`, and all six from the other direction give the same fibre class `F2`.

## Identification with the retained Picard classes

The retained AM runner-side diagnostic reconstructs the 92 nonexceptional known curves and their full automorphism action. It finds exactly three normal-curve orbits:

- 32 curves of degree 2;
- 12 curves of degree 4, labels 33–44;
- 48 curves of degree 4.

The source decomposition above is exactly 32 rational + 12 Satake-boundary elliptic + 48 nonboundary elliptic curves. Thus the unique retained 12-curve orbit, labels 33–44, is the source-bound Satake-boundary orbit.

For every label `E` in 33–44 the AM diagnostic constructs exactly the source-derived divisor

`B_E = 2E + sum(8 incident exceptional curves)`.

It proves that these 12 divisors collapse to exactly two distinct Picard classes of multiplicity `6+6`, with

`B1^2=B2^2=0`,
`K.B1=K.B2=8`,
`B1.B2=8`,
`B1+B2=K`.

Since the source geometry has exactly two factor directions, each contributing six special fibres, and the two retained classes are distinct, the two retained classes are exactly the two source-bound factor-fibration fibre classes, up to swapping `B1` and `B2`.

This is the semantic step that was intentionally withheld in the raw AM diagnostic.

## Relation to the Beauville projection degrees

Let `H=Gamma'[4]/Gamma[8]` and `Y=C8/H`. By Lemma 4.1, `H` has order 4 and acts freely on the genus-5 curve `C8`, so `g(Y)=2`. Since `H` has index 2 in `G`, the natural map

`q:Y -> Z=C8/G`

has degree 2.

Let `pi:X=(C8 x C8)/H_diag -> B=(C8 x C8)/G_diag` be the Beauville double cover, and let

`f_i:X->Y`, `g_i:B->Z`

be the factor maps. They satisfy `g_i o pi = q o f_i`.

For a general point of `Z`, its inverse image in `Y` has two points, so the pullback of a general `g_i`-fibre is the sum of two linearly equivalent `f_i`-fibres. If `C` is the strict transform of a hypothetical integral V6 carrier and `D` is the connected normalized Beauville pullback used in AL, then the projection formula on a general fibre gives

`2*(C.F_i) = D.(f_i^{-1}(y)+f_i^{-1}(y')) = 2*n_i`.

Hence

`n_i = C.F_i`.

The retained V6 intersections are `81` and `105`. Therefore the source-locked statement is the unordered equality

`{n1,n2} = {81,105}`.

No orientation between the two factor labels is claimed or needed.

## Strengthened necessary bounds

AL proves for the connected Beauville pullback that the ramification count `r` satisfies

`r >= 2*n_i`

for each positive projection degree. Therefore

`r >= 2*105 = 210`.

Using the exact V6 exceptional mass vector:

- total normalization preimages over the 47 met surface nodes are at least `210`;
- branch excess over those 47 nodes is at least `210-47=163`;
- `g(D)=1+r/2 >= 106`;
- the parity-refined exceptional-mass capacity is at most `204` with at most 18 multibranch surface nodes, and reaches `210` only at 19 nodes, so at least 19 distinct met surface nodes must be multibranch.

These are necessary conditions only. They do not prove that any 19-node configuration exists and do not exclude a V6 genus-one carrier.

## Arsenal cross-check

The relevant Arsenal contracts were checked before finalization:

- `S36-PW01` is a PROVISIONAL structural character-quotient/genus inventory. It is compatible with the cover bookkeeping but supplies no Stage32 counts or closure and is not used as proof authority here.
- formal `S31-W01` is a genus-one quartic/elliptic birational adapter. Stage36 `DISC-S36-B08` adds a PROVISIONAL successive-cover genus preflight before routing a genus-one layer to S31-W01. AM does not construct such a quartic/genus-one layer, so neither contract is invoked for the present semantic fibre-class identification.

## Firewalls

- Scratch only; shared `MAIN-STATE.json` and Stage32 authority are unchanged.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit is granted.
