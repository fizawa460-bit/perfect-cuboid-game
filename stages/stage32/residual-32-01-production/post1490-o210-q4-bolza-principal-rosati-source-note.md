# Stage32 post-1490 O210 q'=4 Bolza principal polarization / Rosati lock

Scope: fixed recovered V6 class `g1-d186` only, at retained `O=210`, `q'=4`. This note source-locks the principal polarization on the already-identified Bolza Jacobian in the `E^2`, `E=C/Z[sqrt(-2)]`, coordinates. It does not exclude O210 and does not construct a carrier.

## External source lock

Primary public source: Sergio Cecotti, *Symplectic Singularities, Color Confinement, and the Quantum Dirac Sheaf*, arXiv:2509.24605v1.

Use exactly:

- Section 3.2, equations (3.19)-(3.20): an irreducible unitary reflection group has, up to normalization, a unique invariant positive Hermitian form over its imaginary quadratic field; the Hermitian form gives the rational alternating/Riemann form on the integral lattice.
- Appendix B, equations (B.1)-(B.6), especially Fact 18: for `G12`, the torus is `E_{sqrt(-2)} x E_{sqrt(-2)}`, the displayed integral matrices act on `Z[sqrt(-2)]^2`, the unique `G12`-invariant principal polarization has period matrix
  `[[1/2+sqrt(-2), sqrt(-2)/2], [sqrt(-2)/2, 1/2+sqrt(-2)]]`, and the ppav is the Jacobian of the Bolza curve `y^2=x^5-x`.

This is consistent with the already-retained Koziarz--Rito--Roulleau Bolza identification. The new datum here is the exact polarization/Rosati model, not a new target identification.

## Exact Hermitian form

Put `r=sqrt(-2)`, so `r^2=-2` and `bar(r)=-r`. Write a generic Hermitian matrix over `Q(r)` as

`H(a,b,c,d) = [[a, c+d*r], [c-d*r, b]]`.

From Appendix B (B.1), use

`b1=[[-1+r,-2],[-r,1-r]]`,
`b2=[[1,r],[r,-1]]`.

Solving the exact linear invariance equations

`bar(bi)^t H bi = H`,  `i=1,2`,

gives the one-dimensional solution space

`(a,b,c,d)=d*(2,2,1,1)`.

Taking the positive primitive normalization gives

`H = [[2,1+r],[1-r,2]]`.

Its determinant is `1`, and its leading principal minor is `2`, hence it is positive definite.

## Principal Riemann form replay

Following the source normalization in (3.20), on the ordered Z-basis

`e1, e2, r*e1, r*e2`

of `Z[r]^2`, the alternating form is

`[[ 0, 1, 2, 1],
 [-1, 0, 1, 2],
 [-2,-1, 0, 2],
 [-1,-2,-2, 0]]`.

Its determinant is exactly `1`. Therefore the polarization is principal. It is not the product polarization; the off-diagonal `1+r` is essential.

Since `det(H)=1`,

`H^{-1}=[[2,-1-r],[-1+r,2]]`.

Thus the exact Rosati involution on `End(J(C0))=M_2(Z[r])` is

`T^dagger = H^{-1} * bar(T)^t * H`.

## Exact finite-box consequence

The retained correspondence inequality is

`T^dagger*T <= 8505`.

With the locked `H`, this is equivalent to

`bar(T)^t H T <= 8505 H`.

Also `H >= (1/4) I_2`: the matrix `H-(1/4)I_2` has leading minor `7/4` and determinant `1/16`.

For either standard basis vector `ej`, the j-th column `v=T ej` therefore satisfies

`H(v,v) <= 8505 H(ej,ej)=17010`,

hence

`|v1|^2+|v2|^2 <= 68040`.

For an entry `a+b*r`, `|a+b*r|^2=a^2+2b^2`. Consequently every entry of every admissible `T` lies in the exact finite coefficient box

`|a|<=260`, `|b|<=184`.

This box is only a finite exact search boundary; it is not an assertion that every point in the box satisfies the Rosati inequality or is geometrically realizable.

## Firewalls / next leaf

- `O=210` is not excluded here.
- No product Rosati is substituted.
- No Abel--Jacobi-zero route is reopened.
- No completeness claim is made for the still-unrun endomorphism enumeration.
- O186/O188 remain closed; FULL178 remains inactive.
- Next exact leaf: enumerate `T in M_2(Z[sqrt(-2)])` under `bar(T)^t H T <= 8505 H`, using the locked Rosati form and the exact finite box above, then add only independently source-locked common-cover / six-Weierstrass constraints.
