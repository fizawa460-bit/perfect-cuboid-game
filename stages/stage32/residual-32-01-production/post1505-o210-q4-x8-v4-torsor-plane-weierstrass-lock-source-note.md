# Stage32 post-1505 O210 exact X(8) V4 torsor-plane Weierstrass lock

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, after the post-1503 relative-V4 mod-2 coupling left 28 residue classes. This leaf identifies the actual global character plane
`W=image(H^* -> H^1(C0,F2))` of the connected etale cover `X(8)->C0`
as an abstract subgroup of `J(C0)[2]` in the audited six-Weierstrass labeling.
It does not yet identify the coordinates of that plane in the retained
`(e1,e2,r*e1,r*e2)` lattice basis.

## Audited retained inputs

Use the following already-retained exact assets.

- `post1473-x8-v4-cusp-quotient.json`, canonical
  `2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5`:
  `Z=X(8) -> C0=Z/H` is a connected finite etale `H ~= V4` torsor.
- `post1473-boundary-label-weierstrass-adapter.json`, canonical
  `b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f`:
  hostile bounded re-audit PASS review `5083834097` source-locks the six
  quotient cusps as the six Weierstrass points and fixes the three pairs
  `Z1={1,6}`, `Z2={3,5}`, `Z3={2,4}` with inertia
  `T4*u`, `T4*uv`, `T4*1`, respectively.
- `post1473-boundary-label-weierstrass-adapter-source-note.md` fixes the
  theta-ratio values
  `1 -> +1`, `6 -> -1`, `3 -> +i`, `5 -> -i`, `2 -> 0`, `4 -> infinity`.
- `post1490-o210-q4-bolza-principal-rosati-lock.json`, canonical
  `8d828cdf6d1f5cb1d790c46292535dc252e503356e1047ce972c41e61f524529`,
  fixes `C0` as the Bolza curve `y^2=x^5-x` and the retained principal
  lattice basis `(e1,e2,r*e1,r*e2)`, `r^2=-2`.
- `post1503-o210-q4-relative-v4-torsor-mod2-coupling.json`, canonical
  `312aa78d5a89c7c4d48e0afc2988e5ecf2b605d68820d123fea8ca8c48f6d669`,
  fixes `W=image(H^* -> H^1(C0,F2))`, `dim_F2 W=2`.

The general genus-2 2-torsion convention used below is the standard
Richelot kernel description: for a factorization of the hyperelliptic
branch divisor into three unordered pairs, the three corresponding
Weierstrass pair classes are the nonzero elements of a maximal
2-Weil-isotropic subgroup of `J[2]`. A public reference is the Magma
handbook, “Richelot Isogenies”, which describes Richelot kernels by the
three quadratic factors of the hyperelliptic polynomial.

## Character pushout calculation

Write `H=<u,v> ~= F2^2`, and let `tau=T4` denote the class outside `H`
that induces the hyperelliptic involution on `C0 -> X(4)`.
The three audited Weierstrass pairs have full-cover inertia

- `Z1={1,6}`: `tau*u`;
- `Z2={3,5}`: `tau*u*v`;
- `Z3={2,4}`: `tau`.

For a nonzero character `chi:H->F2`, the pushout
`X(8)/ker(chi) -> C0` is the etale double cover representing
`alpha_chi in H^1(C0,F2)`. Extend `chi` to the elementary-abelian
full cover by taking `chi(tau)=0`. The induced quadratic cover of
`X(4)` is branched exactly at the Weierstrass points whose inertia
has nonzero `chi`-value. Replacing that branch subset by its complement
does not change the associated class on the hyperelliptic curve.

With character coordinates `(chi(u),chi(v))` this gives exactly

- `(1,0)`: branch pairs `Z1 union Z2`, hence complement `Z3={2,4}`;
- `(0,1)`: branch pair `Z2={3,5}`;
- `(1,1)`: branch pair `Z1={1,6}`.

Therefore the actual global plane has nonzero classes

`W\{0} = { [w_1-w_6], [w_3-w_5], [w_2-w_4] }`.

Under the audited theta-ratio/Bolza normalization these are

`{ [P_{+1}-P_{-1}], [P_{+i}-P_{-i}], [P_0-P_infinity] }`.

The three unordered pairs are disjoint and partition all six
Weierstrass points. In the even-subset model of `J(C0)[2]` their
three classes sum to zero, and the standard Weil-pairing formula for
Weierstrass pair classes shows they are pairwise orthogonal.
Thus these are exactly the three nonzero points of a two-dimensional
maximal isotropic subgroup.

Equivalently, this is the Richelot kernel attached to the exact factorization

`x^5-x = x * (x^2-1) * (x^2+1)`

with the linear factor interpreted as the pair `{0,infinity}`.

## Decision / remaining leaf

This closes the abstract geometric identity of the actual `X(8)->C0`
torsor plane. It is no longer permissible to range over arbitrary
two-planes of `J(C0)[2]`.

What remains is narrower: translate the three locked classes above into
the retained principal lattice coordinates
`(e1,e2,r*e1,r*e2) mod 2`, then evaluate the already-certified 28
post-1503 residues pointwise on that one plane.

Firewalls:

- no coordinate vector in `F2^4` is guessed here;
- no arbitrary symplectic basis change is credited as the retained basis;
- `Q=602` and `O=210` remain open;
- O212+ remains blocked;
- no receiver, route, theorem, endpoint, FULL178, existence, or
  nonexistence credit follows.
