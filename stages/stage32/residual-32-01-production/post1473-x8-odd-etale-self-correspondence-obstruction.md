# Stage32 post-1473 — odd étale self-correspondence obstruction on X(8)

## Scope

This note attacks only the hostile-audited extremal branch of the fixed V6 class
`g1-d186`, `d=186`, `e=266`.

The audited product-cover wall says that `O=186` can survive only with

- `q'=4` and full `V4` monodromy;
- `n1=n2=93`;
- both projections from the normalized pullback component `D` to
  `C=X(8)` étale of degree `93`.

The purpose here is to test whether such a degree-93 étale correspondence on
`X(8)` can exist.

## Source locks

Primary modular source:

- E. Freitag, R. Salvati Manni, *Parametrization of the box variety by theta functions*,
  arXiv `1303.6495`, DOI `10.1307/mmj/1480734014`.
- The modular product is `P=X(8) x X(8)`, with `X(8)=H/Gamma[8]`; Section 4
  supplies the finite étale modular-cover description used by the retained Stage32 wall.

Commensurator source:

- T. Koberda, M. Mj, *Commutators, commensurators, and PSL2(Z)*,
  DOI `10.1112/topo.12200`.
- Section 1.4 recalls that the commensurator in `PSL2(R)` of `PSL2(Z)`, and
  therefore of any finite-index subgroup, is represented projectively by rational
  matrices.

Retained audited Stage32 source:

- `post1473-specific-class-multibranch-product-cover-monodromy-extremal-wall.md`
- blob `c6430ca94a4897f9f50104ab76a4eaae60df4268`.

## Lemma

Let `C=X(8)`. Let `Dbar` be the normalization of an irreducible curve
`D subset C x C`, and suppose both projections

`p1,p2 : Dbar -> C`

are finite étale. If the projection degree is odd, then it is `1`.
In particular there is no such correspondence of degree `93`.

### Proof

Let `Gamma` be the projective image of `Gamma(8)`.

Use the first étale projection to identify the universal cover of `Dbar` with
the upper half-plane and its fundamental group with a finite-index subgroup
`Lambda < Gamma`.

Because the second projection is also étale, its lift between the two universal
covers is an automorphism of the upper half-plane, hence an element
`h in PSL2(R)`.

Since `Dbar -> D subset C x C` is birational, two points of the universal cover
have the same pair of projection values exactly when they differ by `Lambda`.
Therefore

`Lambda = Gamma intersect h^{-1} Gamma h`.

Thus the first projection degree is

`n = [Gamma : Gamma intersect h^{-1} Gamma h]`.

The two groups are commensurable, so `h` belongs to the commensurator of
`Gamma`. Since `Gamma` has finite index in `PSL2(Z)`, the cited commensurator
result allows `h` to be represented projectively by a rational matrix.

Choose a primitive integral representative `A`. Smith normal form gives

`A = U diag(1,m) V`

with `m>=1` and `U,V in GL2(Z)`. The principal congruence group `Gamma(8)`
is normal under integral conjugation, so left/right multiplication by `U,V`
does not change the intersection index. It is enough to study

`h = diag(1,m)`.

Write an element of `Gamma(8)` as

`gamma = [[a,b],[c,d]]`

with `a,d = 1 mod 8` and `b,c = 0 mod 8`. The condition that
`h gamma h^{-1}` again lie in `Gamma(8)` forces `b` to be divisible by `8m`.

If an odd prime `p` divides `m`, reduce modulo `p`. The two elements

`[[1,8],[0,1]]`, `[[1,0],[8,1]]`

belong to `Gamma(8)`. Since `8` is invertible modulo `p`, their powers give all
upper and lower elementary unipotents, hence the reduction of `Gamma(8)`
surjects onto `PSL2(F_p)`. The intersection subgroup has upper-right entry
zero modulo `p`, so its image lies in a Borel subgroup. A Borel has index
`p+1` in `PSL2(F_p)`. Hence `n` is divisible by `p+1`, so `n` is even.

If `2` divides `m`, define

`phi(gamma) = (b/8) mod 2`.

Multiplication in `Gamma(8)` shows that `phi` is a homomorphism to `F2`,
and `[[1,8],[0,1]]` shows that it is surjective. The intersection subgroup,
where `16` divides `b`, lies in `ker(phi)`. Hence `n` is again even.

Therefore an odd index forces `m=1`. Then `h` is integral and normalizes
`Gamma(8)`, so the intersection is all of `Gamma` and `n=1`.

This proves the lemma.

## Fixed-target consequence

The audited `O=186`, `q'=4` survivor requires both projections to be étale of
degree `93`. The lemma rules this out because `93` is odd and greater than `1`.

The other product-cover cases already give:

- `q'=1` impossible for `d=186`;
- `q'=2` impossible at `O=186`.

Therefore every surviving multibranch genus-one carrier in this fixed V6 class
must satisfy

`O >= 188`.

With `e=266`, the retained odd-branch mass inequality gives

`S1 >= ceil((3*188-266)/2) = 149`.

The exact coarse partition state `(B,O,S1)=(188,188,149)` was already retained
as reachable, so this is still a necessary-condition NONEXCLUSION wall, not a
carrier exclusion.

## Audit / firewalls

This lemma is provisional until hostile audit checks:

- the universal-cover/commensurator passage;
- the equality `Lambda = Gamma intersect h^{-1}Gamma h` from birationality;
- Smith-normal-form invariance of the index;
- the mod-`p` surjectivity/Borel-index argument;
- projective/sign conventions for `Gamma(8)`.

Do not use this note for global curve existence, general genus-`<=1`
classification, FULL178 authorization, receiver/route/theorem/endpoint credit,
or any perfect-cuboid conclusion.
