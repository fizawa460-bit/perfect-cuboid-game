# Stage32 O=188 q'=4 genus-2 descent authority note

Scope: this note repairs the proof/source-lock gap identified by hostile audit review 5083453635. It does not reopen the already-audited O=186 leaf or canonical cusp-ramification budget `318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328`.

## Pinned inputs

- audited cusp-ramification budget canonical: `318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328`
- X(8) V4 cusp quotient canonical: `2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5`
- Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495v1, Section 4 Lemma 4.1 and the Section 2 genus statement, as already locked by the V4 quotient certificate.

## Cartesian torsor lemma

Let `G=V4`. Suppose

- `p:D -> Y` and `q:X(8) -> C0` are finite etale `G`-torsors of degree 4,
- `phi:D -> X(8)` is `G`-equivariant,
- `f:Y -> C0` is the induced quotient map, so `q o phi = f o p`.

Then the natural map

`alpha: D -> Y x_C0 X(8), d |-> (p(d), phi(d))`

is a `G`-equivariant morphism of `G`-torsors over `Y`. A morphism of torsors is automatically an isomorphism, hence the square is Cartesian.

Source lock for the general torsor fact:

- Stacks Project, Cohomology on Sites, Section 21.4, tag `03AG`: a morphism of `G`-torsors is automatically an isomorphism.
- Stacks Project, Section 95.14, tag `036Z`: morphisms in the torsor category over varying bases are expressed by the corresponding Cartesian pullback diagram.

No receiver-specific existence statement is imported from these references; they justify only the formal torsor descent step once the two degree-4 etale torsors and equivariance are given.

## Degree and ramification consequences

Because the square is Cartesian, `phi:D -> X(8)` is the base change of `f:Y -> C0` along the finite etale map `q`.

Therefore:

1. finite degree is preserved by base change, so `deg(f)=deg(phi)=93`;
2. `p:D -> Y` is the base change of `q`, hence finite etale of degree 4;
3. for finite separable maps of smooth curves, the ramification/different is compatible with etale base change, so
   `R_phi = p^* R_f`;
4. taking degrees gives `deg(R_phi)=4 deg(R_f)`.

The locked q'=4 symmetric profile has `deg(R_phi)=8`, hence `deg(R_f)=2`.

Differential/base-change source lock:

- Stacks Project, Algebra Section 10.131, tag `00RM` (base change for Kahler differentials; in particular Lemma 10.131.12);
- Stacks Project, Morphisms Section 37.6, tag `02H7` (unramifiedness is stable under base change).

Thus the Stage32 replay step

`degree 93 -> degree 93` and `ramification 8 -> 2`

is a formal consequence of the Cartesian V4-torsor square, not a numerical heuristic.

## Firewalls

- This note does not prove existence of a global O=188 carrier.
- It does not identify a retained boundary label with a hypothetical defect branch.
- It does not exclude A, B, or C by itself.
- O=188 remains OPEN.
- FULL178 remains inactive.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit is released.
