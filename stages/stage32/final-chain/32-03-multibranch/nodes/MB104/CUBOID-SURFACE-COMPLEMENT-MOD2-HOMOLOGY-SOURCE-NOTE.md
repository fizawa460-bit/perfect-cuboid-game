# Stage32 MB104 source note — cuboid-surface complement homology

Status: **SOURCE LOCK / STANDARD TOPOLOGY + PUBLISHED CUBOID PICARD INPUT / NO STAGE32 CREDIT BY ITSELF**

## Sources

1. Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388, Proposition 6, Theorem 7, and the discussion after Theorem 10. For the smooth minimal desingularization `S`, the geometric Picard group is free abelian of rank `64`; Proposition 6 records `h^1(S,O_S)=0` and absence of Picard torsion, and the paper also explicitly states that `S` is simply connected.
2. Stacks Project, Étale Cohomology, Section 59.28, `Kummer theory`, tag `03PK`, and Section 59.5, tag `03N7`, for Kummer and finite-coefficient étale/Betti comparison over `C`.
3. Allen Hatcher, *Algebraic Topology*: long exact sequence of a pair, excision, universal coefficients, and Thom isomorphism. The complex normal line bundles of the exceptional curves are canonically oriented over `Z`.

## Locked specialization

Let

```text
B_abs = E_16+...+E_23+E_40+...+E_47,
U = S \ B_abs.
```

The sixteen `E_p` are pairwise-disjoint exceptional `(-2)` curves. The retained Stage32 half-branch relation is

```text
2 L_abs ~ B_abs.
```

The retained exact Picard64 certificate computes the span of these sixteen classes in `Pic(S)/2Pic(S)` to have rank exactly `15`. Thus the all-ones relation supplied by `2L_abs~B_abs` is the unique mod-two relation.

Because `Pic(S)` is torsion-free, `Pic(S)[2]=0`. Kummer and finite-coefficient comparison give

```text
H^1(S,F_2)=0,
H_1(S,F_2)=0.
```

Integrally, the published simply-connected statement gives directly

```text
H_1(S,Z)=0.
```

The same conclusion also follows from `h^1(S,O_S)=0`, universal coefficients, the exponential sequence, and torsion-freeness of `Pic(S)`.

## Complement calculation over F2

Excision and Thom for the pair `(S,U)` give

```text
H_2(S,U;F_2) ~= F_2^16.
```

The map `H_2(S;F_2)->F_2^16` records mod-two intersections with the sixteen exceptional curves. By Poincare duality its rank is the rank of their cohomology classes, namely `15`. Therefore the pair sequence gives

```text
H_1(U;F_2) ~= F_2.
```

Its intersection-map image is the even-weight hyperplane: `2L_abs~B_abs` forces every closed surface class to have even total intersection with `B_abs`, and both this hyperplane and the actual image have dimension `15`. Every absent meridian therefore represents the same nonzero class.

## Integral refinement and exact image lattice

Integral excision and Thom give

```text
H_2(S,U;Z) ~= Z^16.
```

The sixteen exceptional classes are linearly independent over `Q`, since their intersection matrix is `-2 I_16`, so the integral intersection map has full rational rank and its cokernel is finite. Moreover the surface class `E_p` maps to `-2 e_p`; hence

```text
2 Z^16 subset image(H_2(S,Z)->Z^16).
```

Every image vector has even coordinate sum because its sum is intersection with `B_abs~2L_abs`. Conversely, modulo two the image is the full even-weight hyperplane. If `v` is any integral vector of even coordinate sum, choose an image vector `w` with `w==v (mod 2)`; then `w-v in 2Z^16` also lies in the image, hence `v` lies in the image. Therefore the integral image is exactly

```text
image(H_2(S,Z)->Z^16)
 = {v in Z^16 : sum_i v_i is even}.             (IMAGE-Z)
```

This lattice has index `2`, so

```text
H_1(U,Z) ~= Z/2,
H_1(U,F_2) ~= F_2.
```

All sixteen absent meridians are the unique nonzero integral class.

An exact Smith replay of the model generators

```text
2e_1,...,2e_16,
e_1+e_16,...,e_15+e_16
```

has invariant factors

```text
1,...,1,2
```

and index `2`; this is a computational cross-check of `(IMAGE-Z)`, not an additional geometric assumption.

## Linking-parity evaluator

Since `H_1(S,Z)=0`, every loop `lambda` in `U` bounds an integral singular 2-chain `Gamma` in `S`. Define

```text
ell_abs(lambda) := Gamma . B_abs mod 2.
```

This is independent of the chosen bounding chain: two choices differ by a closed 2-cycle, whose intersection with `B_abs~2L_abs` is even. The meridian has value `1`, so

```text
ell_abs : H_1(U,Z) ~= Z/2 -> F_2
```

is the unique nonzero character. In the relative-meridian coordinates of `(IMAGE-Z)`, it is simply

```text
(v_1,...,v_16) |-> sum_i v_i mod 2.             (LINK-Z)
```

The absent half-branch double cover has local monodromy `1` around every absent exceptional component. Therefore its ambient Kummer character equals this linking character:

```text
alpha_abs(lambda)=ell_abs(lambda)=Gamma.B_abs mod 2.
```

For every Stage32 conductor-identification loop `lambda`, same/opposite residual sheet is therefore exactly the parity of the total intersection of any ambient bounding 2-chain with `B_abs`.

## Scope firewall

- This note does not construct the bounding 2-chain for any Stage32 conductor loop.
- It does not assign a conductor sign or prove a weighted-cut upper bound.
- It does not close `e=2`, `e=4`, or `000707000f0f`.
- It grants no MB104, receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit.
- It authorizes no heavy compute, merge, or rebase.
