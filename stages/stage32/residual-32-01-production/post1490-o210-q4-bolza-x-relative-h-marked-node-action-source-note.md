# Stage32 post-1490 O210 relative-H marked-node action

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`. This note closes only the named `H ~= V4` translation permutations on the 48 marked node lifts. It does **not** identify `Pic(B)` with `Pic(X)`, does not identify the recovered exceptional masses with local multiplicities of the upstairs carrier `D`, and does not compute any individual `D.t(D)`.

## Quotient geometry

Let `P=X(8) x X(8)`, `G=Gamma[4]/Gamma[8]` and `H=Gamma'[4]/Gamma[8]`. Freitag--Salvati Manni, arXiv:1303.6495, Section 4, identifies

`B=P/G_diag`, `X=P/H_diag`,

with `H ~= V4` of index two in `G`. The paper describes `X -> B` as the smooth two-fold Beauville covering, unramified away from the 48 nodes, and explicitly blows up `X` at the **48 inverse images** of the nodes of `B`; the resulting cover of the blowups is ramified along the 48 exceptional lines. Thus each marked node of `B` has one distinguished inverse-image point of `X`.

The map relevant to the Bolza reduction is

`q : X=P/H_diag -> P/(H x H)=C0 x C0`.

Its deck group is `(H x H)/H_diag ~= H`; a named deck element `h` may be represented by `(h,1)`. Since the relevant mod-8 group is elementary abelian, first-factor `(h,1)` is compatible with the diagonal quotients and induces the corresponding modular automorphism on `B`. By uniqueness of the X-point over each B node, its permutation of the 48 B nodes is therefore also the permutation of the 48 marked X node lifts. This uses the B-side automorphism interface only as a finite node-permutation source, never as a Picard action on `X`.

## Modular element to Stoll generator

Using the theta transformation rules and the box-coordinate formulas in Freitag--Salvati Manni Section 2, on the first factor:

- `T` acts as Stoll `g9` (sign of `b3`),
- `T'` acts as `g7` (sign of `b1`),
- `R` acts projectively as `g7*g8*g9` (signs of `b1,b2,b3`).

For the three nonidentity classes of `H` used by the retained X(8) quotient replay,

- `u = T T' = g7*g9`,
- `v = R T = g7*g8`,
- `uv = R T' = g8*g9`.

Stoll's source order for `g7,g8,g9` is pinned by `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, retained blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Exact replay result

The retained 140-class automorphism permutations and the exact 48-node boundary-pair incidence were replayed on PR #1490. Run `33696522871`, job `100466451269`, succeeded. The diagnostic canonical is `59698dfcc3e7133611012ea689421e05acaf1a0bb93d1d3c0f085f5c23ad2760`.

The three named actions form `V4`, fix all 12 quotient boundary labels, preserve every one of the 12 realized four-node fibers, have no fixed marked node, and act regularly on every four-node fiber. Consequently the named translation pairings `x <-> u(x)`, `x <-> v(x)`, `x <-> uv(x)` are source-locked on all 48 marked X node lifts. An arbitrary absolute choice of origin in each H-torsor is unnecessary: `D.t(D)` only requires the named translation permutation.

## Remaining bridge

The recovered V6 `all140_pairings` supply nonnegative numbers on the 48 exceptional classes, but this leaf does **not** yet prove that those numbers are the local multiplicities of the upstairs branch `D` at the corresponding X points. Therefore products of paired exceptional masses must not yet be accumulated into `D.t(D)` or `c_t`.

Next: source-lock the local multiplicity adapter relating the recovered exceptional pairing/mass to the local branch of `D` on `X`, including any strict-transform/branch correction. Only then may the local intersection inequality for `D` and `t(D)` be applied.
