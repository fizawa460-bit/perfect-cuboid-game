# Stage32 post1648N source note — canonical period basis / marked ppav torsor obstruction

This is a scratch-only source note. It does not promote MAIN authority or arithmetic credit.

## Source-side marked homology datum

Klein–Kokotov–Korotkin, *Extremal properties of the determinant of the Laplacian in the Bergman metric on the moduli space of genus two Riemann surfaces*, Math. Z. 261 (2009), §3.2.4, equations (3.39)–(3.44), use the Burnside/Bolza model

`y^2 = z(z^4-1)`

and the generator `mu1: z -> i z`. In their displayed canonical cycle basis `(b1,b2,a1,a2)`, equation (3.43) gives the exact integral cycle-action matrix

```
[[ 0,-1, 1,-1],
 [ 0, 1, 0, 1],
 [-1, 1,-1, 1],
 [-1,-1, 0, 0]]
```

and equation (3.44) gives the normalized period matrix

```
[[(-1+r)/2, 1/2],
 [1/2, (-1+r)/2]]
```

with `r=i*sqrt(2)`, so `r^2=-2`.

Cecotti, arXiv:2509.24605v1 / JHEP 2026, Appendix B, identifies the principal `G12` ppav with the Bolza Jacobian, gives the retained `Z[r]^2` action by `b1,...,b4`, sets `S=b4`, `T=-b3`, and lists the order-8 curve automorphism (B.9)

`(x,y) -> (i*x, exp(i*pi/4)*y)`.

Thus KKK `mu1` and Cecotti B.9 have the same named x-map on the same curve model. Hyperelliptic sign ambiguity does not affect the mod-2 fixed-line conclusion.

## Target retained polarization

The retained Stage32 source lock
`post1490-o210-q4-bolza-principal-rosati-lock.json`
fixes the `O^2` basis `(e1,e2,r e1,r e2)` and the principal Riemann form

```
[[ 0, 1, 2, 1],
 [-1, 0, 1, 2],
 [-2,-1, 0, 2],
 [-1,-2,-2, 0]]
```

with determinant 1.

## Exact finite calculation

Write a complex-linear lattice map as a `2x2` matrix `A` over `Z[r]`. The source period lattice has covolume `1/4` relative to the retained `O^2` lattice, so an isomorphism to `O^2` has `Norm(det A)=4`; in the exact solutions below `det A=±2`.

The verifier materializes 48 distinct complex-linear, integral, unimodular maps carrying the KKK period lattice to retained `O^2` and carrying the KKK symplectic form to the retained principal Riemann form. This list is exhaustive for a reason stronger than the bounded coefficient search: once one ppav isomorphism exists, all ppav isomorphisms form a torsor under the target ppav automorphism group, whose retained `G12` order is 48. Materializing 48 distinct valid maps therefore exhausts the torsor.

Conjugating the KKK `mu1` coordinate action through those 48 maps gives exactly six retained order-8 `G12` elements, each occurring eight times. On the retained plane `W=span_F2(r e1,r e2)`, each has one fixed nonzero line. The 48 maps split exactly

`L1:16, L2:16, L3:16`.

Source-side `mu1: x->i x` fixes the pair `{0,infinity}` and swaps `{±1}` with `{±i}`, so its unique fixed nonzero line in the Richelot plane is `Z3=delta_0inf`. Consequently the canonical period basis plus the named B.9/mu1 homology action still sends `delta_0inf` to all three retained W-lines equally often.

This closes the unnormalized period-matrix / named-order-8-anchor route as nonpruning. A further normalization selecting one element of the 48-element polarized ppav-isomorphism torsor is still required.
