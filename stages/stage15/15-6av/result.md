# Stage15-6av — explicit binary-quartic 2-covering map

Base: merged Stage15-6ar--6au (`PR #846`, merge commit `cb27d626`). Stage15-6au left four mandatory adapters before the Petit small-height twist theorem can be applied. This substage addresses Gate A: construct an explicit rational map from the Stage15 binary quartic to its exact congruent-number twist.

Audit verdict: `PASS` for the covering-map adapter. No canonical-height or counting theorem is applied here.

## 1. Stage15 quartic and notation

Fix

\[
K=A+iB,\qquad A^2+B^2=k,
\]

with squarefree norm core `k`, and a squarefree coordinate core `kappa`, `(k,kappa)=1`. For primitive

\[
z=a+ib,
\qquad Z=a^2+b^2,
\]

define

\[
f=A(a^2-b^2)-2Bab,
\]

\[
g=B(a^2-b^2)+2Aab.
\]

The Stage15 small-coordinate-core receiver is

\[
\boxed{\kappa T^2=fg.}
\]

The ordinary binary quartic is

\[
Y^2=G(a,b):=\kappa f g,
\qquad Y=\kappa T.
\]

From Stage15-6ar,

\[
I(G)=12(k\kappa)^2,\qquad J(G)=0,
\]

and the Jacobian is

\[
E_{k,\kappa}: y^2=x^3-324(k\kappa)^2x.
\]

## 2. Fisher Hessian collapses exactly

For a binary quartic

\[
G=c_0a^4+c_1a^3b+c_2a^2b^2+c_3ab^3+c_4b^4,
\]

use Fisher's Hessian normalization

\[
\begin{aligned}
h(a,b)=&(3c_1^2-8c_0c_2)a^4
+4(c_1c_2-6c_0c_3)a^3b\\
&+2(2c_2^2-24c_0c_4-3c_1c_3)a^2b^2\\
&+4(c_2c_3-6c_1c_4)ab^3
+(3c_3^2-8c_2c_4)b^4.
\end{aligned}
\]

Direct substitution of the Stage15 coefficients gives the exact identity

\[
\boxed{
h(a,b)=12\kappa^2k^2(a^2+b^2)^2
=12\kappa^2k^2Z^2.
}
\]

This is stronger than a coefficient-height bound: the quartic covariant itself becomes a perfect square in the physical Gaussian norm.

## 3. Exact covering x-coordinate

Classical invariant theory gives the x-coordinate of the binary-quartic covering map to `E_{I,J}` as

\[
\xi=\frac{3h(a,b)}{4G(a,b)}.
\]

Because `G=(kappa*T)^2`, the Stage15 image is

\[
\boxed{
\xi=\frac{9k^2Z^2}{T^2}.
}
\]

Let

\[
s=k\kappa,
\qquad d=\operatorname{sf}(2s)
\]

as in Stage15-6ar, and write

\[
18s=c^2d.
\]

The rational scaling `x=c^2X`, `y=c^3Y` identifies `E_{k,kappa}` with

\[
E_d:Y^2=X^3-d^2X.
\]

Since `s` is squarefree,

\[
c^2=\begin{cases}9,&s\text{ odd},\\36,&s\text{ even}.
\end{cases}
\]

Therefore

\[
X=\xi/c^2.
\]

Using

\[
f^2+g^2=kZ^2,
\qquad fg=\kappa T^2,
\]

both parity cases combine into the particularly simple exact formula

\[
\boxed{
X=d\,\frac{f^2+g^2}{2fg}.
}
\]

This is the frozen Stage15 covering coordinate.

## 4. Exact y-coordinate up to covering sign

The Weierstrass equation determines the second coordinate up to sign. Since

\[
\left(\frac{f^2+g^2}{2fg}\right)^2-1
=\frac{(f^2-g^2)^2}{4f^2g^2},
\]

one may take

\[
\boxed{
Y=\pm
\begin{cases}
\displaystyle \frac{k^2Z(f^2-g^2)}{T^3},&s\text{ odd},\\[1ex]
\displaystyle \frac{k^2Z(f^2-g^2)}{8T^3},&s\text{ even}.
\end{cases}}
\]

A direct substitution verifies

\[
Y^2=X^3-d^2X.
\]

The sign is immaterial for the height and torsion audits below.

## 5. Height information already visible from the map

For physical Stage15 states, `f,g>0`. Hence

\[
\boxed{
\frac{X}{d}=\frac12\left(\frac fg+\frac gf\right)\ge1.
}
\]

The covering point is therefore on the positive real component and equality occurs exactly when `f=g`.

The key point for the next audit is that the map is now explicit in the original primitive coordinate pair. There is no longer an unspecified covering coefficient or hidden rational-map height.

## 6. Proof-accounting verdict

```text
AUDIT_STAGE=Stage15-6av
AUDIT_TARGET=EXPLICIT_BINARY_QUARTIC_2COVERING_MAP
AUDIT_VERDICT=PASS
FISHER_HESSIAN_COLLAPSE=true
HESSIAN=12*kappa^2*k^2*(a^2+b^2)^2
COVERING_X_ON_JACOBIAN=9*k^2*Z^2/T^2
COVERING_X_ON_Ed=d*(f^2+g^2)/(2*f*g)
COVERING_Y_RATIONAL_FORM=true
COVERING_MAP_COEFFICIENT_HEIGHT_OBSTRUCTION=false
CANONICAL_HEIGHT_BRIDGE_PROVED=false
PETIT_THEOREM_APPLIED=false
```

AR-023/024 pass: the map is evaluated on each actual Stage15 state. AR-028 pass: `d` repackages `(k,kappa)` and is not charged as another modulus.

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6av
STAGE15_6AV_AUDIT=true
STAGE15_6AV_AUDIT_VERDICT=PASS
STAGE15_6AV_EXPLICIT_2COVERING_MAP=true
STAGE15_6AV_COVERING_X=d*(f^2+g^2)/(2*f*g)
STAGE15_6AV_HESSIAN_PERFECT_SQUARE=true
STAGE15_6AV_CANONICAL_HEIGHT_BRIDGE_PROVED=false
STAGE15_6AV_EXIT=EXPLICIT_IMAGE_READY_FOR_NONTORSION_AUDIT
```

Next: Stage15-6aw audits whether retained physical states map to non-torsion points, isolating any finite torsion-image branch before a small-height theorem is considered.
