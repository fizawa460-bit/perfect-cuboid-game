# Stage32 MB104 source note — cuboid-surface complement mod-2 homology

Status: **SOURCE LOCK / STANDARD TOPOLOGY + PUBLISHED CUBOID PICARD INPUT / NO STAGE32 CREDIT BY ITSELF**

## Sources

1. Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388, Proposition 6 and Theorem 7. In particular the geometric Picard group of the minimal desingularization `S` is a free abelian group of rank `64`; Proposition 6 also records `h^1(S,O_S)=0` and proves absence of Picard torsion.
2. Stacks Project, Étale Cohomology, Section 59.28, `Kummer theory`, tag `03PK`. For `n=2` over `C`, the Kummer sequence identifies the degree-one `mu_2` torsors on a proper connected variety with `Pic[2]`, since every nonzero complex constant has a square root, and injects `Pic/2Pic` into `H^2_et(-,mu_2)`.
3. Stacks Project, Étale Cohomology, Section 59.5, `Feats of the étale topology`, tag `03N7`, for comparison of finite-coefficient étale and Betti cohomology over `C`.
4. Allen Hatcher, *Algebraic Topology*, the long exact sequence of a pair together with excision, and the Thom isomorphism for a real rank-two normal disk bundle (Corollary 4D.9 in the online text). With `F_2` coefficients no orientation choice is required.

## Locked specialization

Let `S` be the smooth minimal desingularization of the cuboid surface and let

```text
B_abs = E_16+...+E_23+E_40+...+E_47
```

be the union of the sixteen pairwise-disjoint absent-type exceptional `(-2)` curves. Put

```text
U = S \ B_abs.
```

The retained Stage32 half-branch relation is

```text
2 L_abs ~ B_abs.
```

The retained exact Picard64 computation in

```text
GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json
```

computes the span of these sixteen absent exceptional classes in `Pic(S)/2Pic(S)` to have rank exactly `15`.

Because `Pic(S)` is torsion-free, `Pic(S)[2]=0`. Kummer plus finite-coefficient comparison therefore gives

```text
H^1(S(C),F_2)=0,
```

and the sixteen classes retain their rank `15` after passage from `Pic(S)/2Pic(S)` to `H^2(S(C),F_2)`. The relation `2L_abs~B_abs` supplies the all-ones relation among them, so it is the unique mod-two relation.

For the pair `(S,U)`, excision to disjoint tubular neighborhoods of the sixteen exceptional curves and Thom give

```text
H_2(S,U;F_2) ~= F_2^16.
```

The map

```text
H_2(S;F_2) -> H_2(S,U;F_2)
```

is the vector of mod-two intersections with the sixteen exceptional curves. By Poincare duality its rank is the rank of their cohomology classes, namely `15`. Since `H_1(S;F_2)=0`, the long exact sequence of the pair gives

```text
H_1(U;F_2) ~= coker(H_2(S;F_2)->F_2^16) ~= F_2.
```

The basis vectors of `F_2^16` are the meridian disks; their boundaries are the sixteen deleted-divisor meridians in `U`.

## Stage32 consequence allowed by this source lock

The absent half-branch double cover on `U` has local monodromy `1` around every absent exceptional component. Hence its ambient character

```text
alpha_abs : H_1(U,F_2) -> F_2
```

is nonzero. Since `H_1(U,F_2)` is one-dimensional, `alpha_abs` is the unique nonzero character and is an isomorphism. In particular all sixteen absent meridians represent the same nonzero generator of `H_1(U,F_2)`.

Therefore, for every conductor identification loop `lambda` from the active `e=2` leaf,

```text
alpha_abs(lambda)=0  <=> [lambda]=0 in H_1(U,F_2),
alpha_abs(lambda)=1  <=> [lambda] is the unique nonzero class.
```

This converts the residual-sheet evaluation into a mod-two null-homology test in the fixed complement `U`.

## Scope firewall

- This source note does not compute the homology class of any Stage32 conductor loop.
- It does not prove a numerical upper bound for the weighted opposite-sheet cut.
- It does not close `e=2`, `e=4`, or `000707000f0f`.
- It grants no MB104, receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit.
- It authorizes no heavy compute, merge, or rebase.
