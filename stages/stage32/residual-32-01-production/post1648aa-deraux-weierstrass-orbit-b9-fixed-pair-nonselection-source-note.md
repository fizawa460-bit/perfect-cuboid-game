# Stage32 post1648AA scratch source note — Deraux affine six-point orbit is a two-sided set-level anchor but not a marked pair selector

This leaf is scratch-only and grants no MAIN or arithmetic credit.

## External sources

Martin Deraux, *Non-arithmetic ball quotients from a configuration of elliptic curves in an Abelian surface*, arXiv:1611.05112v2 / Comment. Math. Helv. 93 (2018), 533–554.

Exact locators used:

- §4, Definition 4.1: explicit affine generators `R1,R2,R3` acting on `C^2`, with lattice `Lambda=(Z + r Z)^2`, `r=i*sqrt(2)`.
- §4, Proposition 4.1: the linear part is the Shephard–Todd group `G12` of order 48.
- §4, Proposition 4.4 and Table 2: outside the mirrors there is an orbit with isotropy order 8; a representative is `(1/2,(1+r)/2)` fixed by an order-8 subgroup. Hence the orbit has size `48/8=6`.

Vincent Koziarz, Carlos Rito, Xavier Roulleau, *The Bolza curve and some orbifold ball quotient surfaces*, arXiv:1904.00793v4.

Exact locators used:

- §4, Lemma 5 / Corollary 6: the Bolza theta automorphism group `H48` is conjugate to Deraux's `G48` by an automorphism of the Abelian surface.
- §4, Proposition 7 discussion: after this conjugacy, the six Weierstrass points on theta are six 2-torsion points and the corresponding Deraux special orbit has six order-2 torsion points.
- The Bolza automorphism `B9: x -> i*x` fixes the two Weierstrass branch points `0` and `infinity`; on the six branch points its permutation cycle type is therefore `1,1,4`.

## Exact retained-coordinate replay

Use the retained target lattice basis `[e1,e2,r*e1,r*e2]`. Reduce Deraux's affine generators on `A[2]=(1/2 Lambda)/Lambda`.

Starting from the Table-2 order-8-orbit representative

`q=(1/2,(1+r)/2)`, i.e. bit vector `(1,1,0,1)`,

the affine `G48` orbit has exactly six points:

- `(0,0,1,0)`,
- `(0,0,1,1)`,
- `(1,0,0,0)`,
- `(1,0,1,1)`,
- `(1,1,0,1)`,
- `(1,1,1,1)`.

Their 15 unordered pair differences are all 15 nonzero vectors of `A[2]`, as expected for the six Weierstrass points of a genus-2 Jacobian.

The full affine group has 48 elements. Exactly 12 actual order-8 elements induce cycle type `1,1,4` on this six-point orbit. Their linear traces split into six with `+r` and six with `-r`.

For each such element, take the difference of its two fixed orbit points. In each trace class the differences are distributed

- `L1=(0,0,1,0)`: 2,
- `L2=(0,0,0,1)`: 2,
- `L3=(0,0,1,1)`: 2.

Across both trace classes the counts are `4,4,4`.

Thus even after adding Deraux's explicit target affine geometry and KRR's identification of the six-point orbit with the Bolza Weierstrass/2-torsion set, the B9 branch-cycle constraint does not select an absolute retained W-line.

## Semantic boundary

This is stronger than a source-only marking: it is a genuine two-sided **set-level** anchor. It is still not a pointwise marked adapter. KRR's conjugating automorphism `g` is not materialized, and no checked source identifies which source Weierstrass point (`infinity`, `0`, etc.) maps to which one of the six explicit Deraux target points. Choosing the Table-2 representative as the image of `infinity` would be a gauge choice, not a source-locked fact.

Accordingly this leaf closes only the route

`Deraux explicit six-point target orbit + KRR set-level Bolza identification + B9 cycle type -> absolute W-line`.

It does not claim global nonexistence of a marked ppav adapter.