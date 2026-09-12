# Stage32 MB104 source note — Stoll--Testa canonical invariants and the `c=0` conic section

Status: **SOURCE NOTE / EXTERNAL PUBLISHED GEOMETRY / NO CREDIT BY ITSELF**

## Source

Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388, Section 2, Lemma 3 and the paragraph immediately following it.

Stable source:
- https://arxiv.org/abs/1009.0388
- HTML rendering used for the present transcription: https://arxiv.org/html/1009.0388

The statements below are source facts needed by the current MB104 effectivity/incidence leaf. This note does not upgrade any Stage32 claim by itself.

## Exact source facts used

Let `bar S` be the singular cuboid surface and `b:S->bar S` its minimal resolution.

1. `bar S` is a geometrically integral complete intersection of multidegree `(2,2,2,2)` in `P^6` with 48 isolated `A1` singularities.
2. The hyperplane section `bar S cap {c=0}` is reduced and is the union of the eight smooth conics
   ```text
   c=0,
   b1=eps1*i*a1,
   b2=eps2*i*a2,
   b3=eps3*i*a3,
   a1^2+a2^2+a3^2=0,
   ```
   indexed by `(eps1,eps2,eps3) in {+1,-1}^3`.
3. The canonical divisor satisfies
   ```text
   K_S = b^* O_barS(1),
   K_S^2 = 16,
   chi(O_S) = 8.
   ```
4. `K_S` is big and nef; its morphism contracts exactly the 48 exceptional curves and then embeds the canonical model `bar S` in `P^6`.

These are the only Stoll--Testa facts imported by the current leaf.

## Derived `c=0` node/conic incidence adapter

At a singular point in the `c=0` hyperplane, one of the three rank-three triples is

```text
a_j=b_j=c=0.
```

For the other two indices the signs `eps` in the eight-conic equations are fixed. At the zero pair `(a_j,b_j)=(0,0)`, the sign `eps_j` is free. Therefore every `c=0` box node lies on **exactly two** of the eight `c=0` conics.

Locally the rank-three equation is an `A1` cone. In standard coordinates it is `xz=y^2`; the hyperplane `c=0` becomes the union of the two smooth local branches through the node. Under the minimal `A1` resolution each such smooth conic branch meets the exceptional curve transversely once. Consequently, for the strict transform `Q_eps` of one of the eight conics,

```text
H.Q_eps = 2,
E_i.Q_eps = 1  if node i lies on Q_eps,
E_i.Q_eps = 0  otherwise,
```

where `H=K_S=b^*O_barS(1)`.

The last local-resolution sentence is compatible with the retained Stage32 A1 strict-transform adapter
`stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`.

## Firewalls

- This note is a provenance/source adapter only.
- It does not assert effectivity or irreducibility of any MB104 formal class.
- It does not grant finite-window, receiver, theorem, endpoint, or Perfect-Cuboid credit.
