# Stage32 post-1505 O210 retained F2^4 adapter via the self-Richelot sqrt(-2) endomorphism

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, after hostile re-audit PASS review `5099888513` promoted the abstract X(8)->C0 character plane

`W\{0} = {[P_{+1}-P_{-1}], [P_{+i}-P_{-i}], [P_0-P_infinity]}`.

This note identifies that audited abstract plane inside the already-retained lattice presentation

`J(C0) ~= E^2`, `End(J(C0)) ~= M_2(Z[r])`, `r^2=-2`,

with ordered Z-basis `(e1,e2,r*e1,r*e2)`. The identification uses a self-Richelot isogeny; it does not choose an arbitrary symplectic basis.

## Locked Stage32 inputs

- post1505 abstract-W certificate canonical `c84242981cbf81c9935c6851d8a95dc4dc0f1d8afbdba7ba7bbe16385bf1282f`, hostile re-audit PASS review `5099888513`;
- Bolza principal Rosati certificate canonical `8d828cdf6d1f5cb1d790c46292535dc252e503356e1047ce972c41e61f524529`, fixing `C0:y^2=x^5-x`, `r^2=-2`, and the retained ordered basis `(e1,e2,r*e1,r*e2)`;
- post1503 relative-V4 coupling canonical `312aa78d5a89c7c4d48e0afc2988e5ecf2b605d68820d123fea8ca8c48f6d669`, fixing the 28 Q602 mod-2 survivors and the requirement that both correspondence orientations act as the identity on the actual W.

## Richelot normalization

External source: Matvey Smirnov, *An explicit expression of the Richelot isogeny through Kleinian hyperellyptic functions*, arXiv:2603.20754v1 (2026), Section 2.2--2.3, especially equation (2.9), Proposition 2.3 and Definition 2.4.

Use Smirnov's convention

- `[a,b]=a' b-b' a`;
- `Delta(p,q,s)` is the determinant of the coefficient matrix of the three degree-at-most-two factors;
- for `f=p q s`, the Richelot polynomial is
  `fhat = [q,s][s,p][p,q] / (4 Delta(p,q,s))`;
- the Richelot isogeny `R_{p,q,s}: Jac(X_fhat) -> Jac(X_f)` is induced by the identity on the two-dimensional holomorphic-differential coordinate space; its dual is induced by multiplication by 2.

For the audited splitting of the Bolza branch divisor take

`p=x`, `q=x^2-1`, `s=x^2+1`.

Direct exact arithmetic gives

- `Delta(p,q,s)=2`;
- `[q,s]=4x=4p`;
- `[s,p]=x^2-1=q`;
- `[p,q]=-(x^2+1)=-s`.

Hence

`fhat = -(1/2) p q s = -(1/2)(x^5-x)`.

The three hatted factors differ from `(p,q,s)` only by nonzero scalar factors and permutation/sign, so their root pairs are the same three audited pairs `{0,infinity}`, `{+1,-1}`, `{+i,-i}`. Thus the Richelot kernel on either side is the same audited maximal isotropic plane W.

## Transport to the retained CM model

Let `X_f : y^2=f(x)` and `X_fhat : yhat^2=fhat(x)`. Because the retained CM element satisfies `r^2=-2`, there is the exact curve isomorphism

`iota : X_fhat -> X_f`, `(x,yhat) |-> (x,r*yhat)`.

For the standard holomorphic differentials `omega1=dx/y`, `omega2=x dx/y`,

`iota^*(omega_j) = (1/r) * omegahat_j`.

Therefore the induced Jacobian isomorphism `iota_* : Jac(X_fhat) -> Jac(X_f)` is multiplication by `1/r` in the same analytic coordinates in which Smirnov's Richelot map R is the identity. Consequently the transported self-endomorphism

`rho := R o iota_*^{-1} : Jac(X_f) -> Jac(X_f)`

is multiplication by `r`.

Since the Richelot kernel is the audited W, this gives the exact retained identification

`W = ker([r] : J(C0) -> J(C0))`.

No change of symplectic basis is involved.

## Retained F2^4 coordinates

In the ordered retained Z-basis `(e1,e2,r*e1,r*e2)`, multiplication by r has columns

- `e1 -> r*e1`;
- `e2 -> r*e2`;
- `r*e1 -> -2*e1`;
- `r*e2 -> -2*e2`.

Modulo two its kernel is therefore exactly

`W = span_F2{(0,0,1,0),(0,0,0,1)}`.

Thus the three nonzero retained vectors are

`(0,0,1,0)`, `(0,0,0,1)`, `(0,0,1,1)`.

The post1503 verifier already uses the same module order `e1,e2,eps*e1,eps*e2` with `eps=r mod 2`, so no further coordinate permutation is inserted.

## Immediate finite consequence

Applying the exact pointwise requirement

`T(w)=w` and `T^dagger(w)=w` for every `w in W`

to the 28 audited post1503 Q602 residues leaves exactly 16 mod-2 residues:

`65,67,73,75,97,99,105,107,193,195,201,203,225,227,233,235`.

Equivalently in hexadecimal:

`0x41,0x43,0x49,0x4b,0x61,0x63,0x69,0x6b,0xc1,0xc3,0xc9,0xcb,0xe1,0xe3,0xe9,0xeb`.

This is a further exact pruning, not an exclusion: 16 residues remain.

## Firewalls

- the abstract W authority is exactly review `5099888513`; this leaf does not alter it;
- no arbitrary symplectic basis, numerical period matching, or unlabeled J[2] identification is used;
- the Richelot source fixes the direction/period convention used above, and the special splitting is self-dual up to scalar factors so the kernel orientation ambiguity does not change W;
- Q602 and O210 remain OPEN;
- O212+ remains BLOCKED;
- no FULL178, receiver, route, theorem, endpoint, existence, or nonexistence credit follows from the 28->16 pruning.
