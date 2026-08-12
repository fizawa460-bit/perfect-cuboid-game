# Stage15-6aw — non-torsion image audit for the explicit twist map

Base: Stage15-6av in the current cycle. The explicit image of a positive primitive Stage15 coordinate pair `(f,g)` on

\[
E_d:Y^2=X^3-d^2X
\]

has

\[
\boxed{X=d\frac{f^2+g^2}{2fg}.}
\]

This substage addresses Gate B from Stage15-6au: prove that retained physical states supply non-torsion points, or isolate the torsion-image branch.

Audit verdict: `PASS`.

## 1. Rational torsion on the congruent-number twist

The curve has the three nonzero rational 2-torsion points

\[
(0,0),\qquad(d,0),\qquad(-d,0).
\]

For a rational point `P=(x,y)`, the duplication formula is

\[
\boxed{x(2P)=\frac{(x^2+d^2)^2}{4x(x^2-d^2)}.}
\]

Hence:

- `2P=(0,0)` would force `x^2+d^2=0`, impossible over `Q`;
- `2P=(d,0)`, after `u=x/d`, gives
  \[
  (u^2-2u-1)^2=0,
  \]
  so `u=1+-sqrt(2)`, not rational;
- `2P=(-d,0)` gives
  \[
  (u^2+2u-1)^2=0,
  \]
  again no rational solution.

Thus there is no rational 4-torsion (and hence no 8-torsion).

The 3-division polynomial is

\[
\psi_3(x)=3x^4-6d^2x^2-d^4.
\]

A rational 3-torsion x-coordinate would give, with `t=x^2/d^2`,

\[
3t^2-6t-1=0,
\]

whose discriminant is `48`, not a rational square. Thus there is no rational 3-torsion.

By Mazur's rational-torsion classification, an elliptic curve over `Q` with full rational 2-torsion has torsion group `Z/2 x Z/2m` with `m=1,2,3,4`; the exclusions above leave only

\[
\boxed{E_d(\mathbf Q)_{tors}\cong(\mathbf Z/2\mathbf Z)^2.}
\]

## 2. Stage15 image cannot hit torsion except a unit branch

For physical Stage15 states the primitive Gaussian coordinates satisfy

\[
f>0,\quad g>0,\quad (f,g)=1.
\]

The explicit map gives

\[
\frac Xd=\frac12\left(\frac fg+\frac gf\right)\ge1.
\]

Therefore `X` cannot be `0` or `-d`. Equality `X=d` occurs exactly when

\[
f=g.
\]

Primitivity then forces

\[
\boxed{f=g=1.}
\]

Using

\[
f^2+g^2=kZ^2,
\]

this unit branch forces

\[
\boxed{k=2,\qquad Z=1.}
\]

Also `fg=kappa*T^2=1` forces `kappa=T=1`.

Thus the torsion-image branch is an absolute finite unit-state decoration. It has no asymptotic mass and may be removed before the Petit theorem is invoked.

Every non-unit retained Stage15 state maps to

\[
\boxed{E_d(\mathbf Q)\setminus E_d(\mathbf Q)_{tors}.}
\]

## 3. Proof-accounting verdict

```text
AUDIT_STAGE=Stage15-6aw
AUDIT_TARGET=NONTORSION_IMAGE
AUDIT_VERDICT=PASS
Ed_RATIONAL_TORSION=(Z/2Z)^2
RATIONAL_3_TORSION=false
RATIONAL_4_TORSION=false
STAGE15_TORSION_IMAGE_IFF_UNIT_BRANCH=true
TORSION_UNIT_BRANCH=k=2,kappa=1,Z=1,f=g=1
NONUNIT_STAGE15_IMAGE_NONTORSION=true
PETIT_GATE_B_CLOSED=true
```

No rank or Selmer average is used. The torsion computation is pointwise for every squarefree twist `d`.

## 4. Frozen exit

```text
STAGE15_6_SUBSTAGE=6aw
STAGE15_6AW_AUDIT=true
STAGE15_6AW_AUDIT_VERDICT=PASS
STAGE15_6AW_NONTORSION_IMAGE_PROVED=true
STAGE15_6AW_TORSION_BRANCH_FINITE=true
STAGE15_6AW_PETIT_GATE_B_CLOSED=true
STAGE15_6AW_EXIT=NONTORSION_IMAGE_READY_FOR_CANONICAL_HEIGHT_AUDIT
```

Next: Stage15-6ax audits Gate C. The existence of a non-torsion image is not enough; the physical/product height must force a point small enough in canonical height to enter Petit's almost-minimal twist family.
