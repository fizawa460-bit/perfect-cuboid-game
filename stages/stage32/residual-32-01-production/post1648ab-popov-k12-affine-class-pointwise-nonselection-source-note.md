# Stage32 post1648AB scratch source note — Popov K12* affine cohomology class is explicit but not the missing pointwise conjugator

This leaf is scratch-only and grants no MAIN or arithmetic credit.

## External sources

Vladimir L. Popov, *Discrete complex reflection groups*, Communications in Mathematics 30 (2022), 303–375; arXiv:2304.08941 (modern publication/reprint of the classification).

Exact locators used:

- §1.6.2 and Table 1: Popov states that his numbering agrees with Shephard–Todd; No. 12 is `GL(2,3)`, dimension 2, with cyclic-product ring `Z[i*sqrt(2)]`.
- §2.4: for an affine group with linear part `K` and translation lattice `T`, choosing a base point gives a cocycle `s:K -> V/T`; changing the base point changes `s` by a 1-coboundary. Translation-conjugacy classes are therefore parameterized by `H^1(K,V/T)` before the further affine-equivalence quotient.
- Table 2: `[K12]` has translation lattice `[1,i*sqrt(2)]e1 + [1,i*sqrt(2)]e2` and cocycle `c=0`; `[K12]*` has `c(r1)=c(r2)=0`, `c(r3)=((1+i)/2)e3` in Popov's displayed reflection-root coordinates.
- Theorem 2.8.1: `[K12]*` is one of the non-semidirect crystallographic reflection groups.
- Theorem 2.8.2: for fixed irreducible reflection group `K` and invariant lattice `T`, crystallographic reflection-group extension classes form a subgroup of `H^1(K,V/T)` of order at most 2.

Vincent Koziarz, Carlos Rito, Xavier Roulleau, *The Bolza curve and some orbifold ball quotient surfaces*, arXiv:1904.00793v4.

Exact locators used in §4:

- The Bolza branch set is `{0,infinity,+/-1,+/-i}`.
- Up to conjugation there are two `GL2(F3)` actions on `A`: the affine `G48` action, which has no global fixed point, and the action obtained by forgetting its translation part, which fixes `0`.
- The Abel–Jacobi embedding `alpha` sends the branch point `infinity` to `0` in `J(theta)=A`.
- With base point `infinity`, the curve-preserving affine action has translation term `[g(infinity)]-[infinity]`.
- Corollary 6 gives existence of an automorphism `g` of `A` with `H48 = g G48 g^-1`.
- After Proposition 7 the paper says that one may change the embedding by composing with this `g` and then identify `H48` with `G48`; the checked source does not give a pointwise formula for `g` on the six Weierstrass points.

## What this adds

This is stronger than merely knowing that an affine action exists. Popov materializes the two crystallographic extension types for Shephard–Todd No. 12 and gives an explicit cocycle representative for the non-split `[K12]*` class. It therefore supplies class-level provenance for the affine-versus-linear dichotomy used by KRR.

However, the current Stage32 missing interface is not the existence/classification of that affine extension. It is a pointwise marked adapter: for example, a source-locked statement that the Bolza branch point `infinity` (or `0`) is sent by the conjugating automorphism to one specific member of the explicit six-point Deraux orbit in the retained lattice coordinates.

Popov's explicit cocycle does not provide that datum. Its table uses Popov's own reflection generators and displayed `e_i`/`epsilon_i` coordinates, and no checked source contract identifies those generators/basis vectors with the KKK named curve generators or with the retained Stage32 lattice basis pointwise. More fundamentally, §2.4 explicitly records that changing the chosen base point changes a cocycle representative by a 1-coboundary. Thus an affine-extension class is not itself a distinguished marked point.

KRR's statement `alpha(infinity)=0` is also not enough to cross the interface: it is stated for the Abel–Jacobi embedding before the unspecified conjugating automorphism `g` is used to identify the curve-preserving action with Deraux `G48`. Promoting that pre-conjugacy `0` to a specific retained Deraux point would assume the missing `g`.

## Relation to retained scratch evidence

Post1648AA already source-locks a genuine two-sided **set-level** correspondence: the six Bolza Weierstrass/2-torsion points correspond, after the unspecified conjugacy, to Deraux's explicit six-point special orbit. Its exact B9 test is balanced across `L1,L2,L3`.

Post1648W separately shows that the Rains ST12 theta-torsor cohomology class does not select a distinguished retained characteristic representative. This AB leaf does **not** identify Popov's `H^1(K,V/T)` class with the Rains `H^1(S4,A[2])` class; the two are used only as parallel evidence that class-level data must not be promoted to a chosen representative without an exact adapter.

Accordingly this leaf closes only:

`Popov explicit [K12]* affine extension class + KRR two-action classification -> pointwise image of source infinity/zero in the retained Deraux six-point orbit`.

It does not claim that no external source contains an explicit integral conjugating `g`. A distinct remaining route is to reconstruct the source affine cocycle / Weierstrass characteristic marking in the KKK canonical basis and match that full affine six-point action exactly against Deraux.