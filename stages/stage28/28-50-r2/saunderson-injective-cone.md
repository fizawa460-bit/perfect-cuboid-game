# Stage28-50-r2 — injective Saunderson cone and explicit one-third coefficient

```text
ROUTE=L8_SAUNDERSON_INJECTIVE_CONE
CHECKPOINT=50
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_THEOREM=Stage28-50 audited M3(B)>>B^(1/3)
```

The audited checkpoint50 bounded-fiber theorem can be sharpened on a positive-density Euclid-parameter cone.  The gain is not a new exponent; it is an injective physical subfamily and an explicit positive coefficient on the `B^(1/3)` scale.

## 1. Exact height sharpened from `72T^6` to `8r^6`

For primitive Euclid parameters

\[
r>s>0,\qquad (r,s)=1,\qquad r-s\equiv1\pmod2,
\]

put

\[
u=r^2-s^2,\qquad v=2rs,\qquad w=r^2+s^2.
\]

The generalized Saunderson Euler brick is

\[
A=u|4v^2-w^2|,\qquad B_1=v|4u^2-w^2|,\qquad C=4uvw.
\]

Its distinguished face diagonal is `w^3`, so

\[
A^2+B_1^2=w^6.
\]

Hence the physical Euclidean cutoff quantity is exactly

\[
R^2=A^2+B_1^2+C^2=w^6+16u^2v^2w^2.
\]

Set `y=(s/r)^2`.  Direct substitution gives

\[
\frac{R^2}{r^{12}}
=(1+y)^2\bigl((1+y)^4+64y(1-y)^2\bigr).
\]

The difference from `64` factors as

\[
64-(1+y)^2\bigl((1+y)^4+64y(1-y)^2\bigr)
=(1-y)\bigl(y^5+71y^4+86y^3-22y^2-7y+63\bigr).
\]

For `0<=y<=1`, the second factor is at least `63-22-7=34>0`.  Therefore

\[
\boxed{R\le 8r^6.}
\]

This is a theorem-level strengthening of the old sufficient bound `R<72T^6`; it uses the exact Saunderson identities and does not change the population or cutoff.

## 2. A positive-density cone where the output map is injective

Restrict to

\[
\boxed{\frac18\le \frac{s}{r}\le\frac45.}
\]

Write

\[
\alpha=\frac{u}{w}=\frac{1-t^2}{1+t^2},\qquad
\beta=\frac{v}{w}=\frac{2t}{1+t^2},\qquad t=s/r.
\]

On this cone,

\[
\alpha\ge\frac9{41},\qquad \beta\ge\frac{16}{65}.
\]

Both lower bounds exceed

\[
c_0=\frac{\sqrt2-1}{2},
\]

the positive root of `4x^2+4x-1=0`.  For `c_0<x<1`,

\[
x(5-4x^2)-1=-(x-1)(4x^2+4x-1)>0.
\]

The other two face diagonals satisfy

\[
\frac{D_{AC}}{w^3}=\alpha(4\beta^2+1)=\alpha(5-4\alpha^2)>1,
\]

\[
\frac{D_{BC}}{w^3}=\beta(4\alpha^2+1)=\beta(5-4\beta^2)>1.
\]

Thus `w^3` is the **unique smallest physical face diagonal** throughout this cone.

A canonical physical output therefore identifies `w` uniquely.  The edge opposite that face is `C`, so

\[
uv=C/(4w).
\]

Together with `u^2+v^2=w^2`, this determines the unordered pair `{u,v}`.  Primitive Euclid orientation fixes `u` as the odd leg and `v` as the even leg.  Hence the input `(u,v,w)`, and therefore `(r,s)`, is unique.

```text
INJECTIVE_CONE=[1/8,4/5]
DISTINGUISHED_CUBE_FACE=UNIQUE_SMALLEST
PHYSICAL_OUTPUT_FIBER_ON_CONE=1
```

## 3. Exact primitive-parameter density on the cone

Let

\[
\mathcal C(T)=\{(r,s):1\le r\le T,\ r/8\le s\le4r/5,\ (r,s)=1,\ r-s\text{ odd}\}.
\]

The planar cone has area

\[
\frac12\left(\frac45-\frac18\right)T^2=\frac{27}{80}T^2.
\]

The density of coprime opposite-parity ordered integer pairs is `4/pi^2`.  Standard Möbius/inclusion-exclusion lattice counting therefore gives

\[
\#\mathcal C(T)=\frac{27}{20\pi^2}T^2+O(T\log T).
\]

Every such input gives a distinct primitive physical Euler cuboid, and `R<=8T^6`.  Put `T=(B/8)^(1/6)`.  Then

\[
M_3(B)\ge
\left(\frac{27}{40\pi^2}+o(1)\right)B^{1/3}.
\]

Therefore the candidate strengthening is

\[
\boxed{
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}
\ge \frac{27}{40\pi^2}>0.
}
\]

Numerically the coefficient is about `0.06839`.

## 4. Firewalls

This does not prove `M3(B)~cB^(1/3)`, does not identify the true `M3` exponent, and does not order `M3` against `N2`.  It is a lower theorem on one explicit injective target family only.

```text
SAUNDERSON_HEIGHT_R_LE_8_R6_CANDIDATE=true
SAUNDERSON_POSITIVE_DENSITY_INJECTIVE_CONE_CANDIDATE=true
M3_EXPLICIT_ONE_THIRD_LIMINF_COEFFICIENT_CANDIDATE=27/(40*pi^2)
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
FULL_M3_VS_N2_ORDERING_PROVED=false
AUDIT_REQUIRED=true
```
