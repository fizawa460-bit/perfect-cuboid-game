# Stage14-4ai — reduce the extremal degree-four bisection problem

## Purpose

Stage14-4ah proved that every fixed physical rational curve `C` on the raw Kummer surface satisfies

\[
M\cdot C\ge4,
\]

and that a fixed rational curve can produce polynomial height exponent `1/2` only in the extremal case

\[
M\cdot C=4,
\qquad
\deg(C\to\mathbf P^1_r)=2.
\]

Stage14-4ai classifies the geometry of such a putative minimal bisection as far as the present argument genuinely reaches.

The rigorous conclusion is **not** that all degree-four bisections are absent.  The complete genus-zero image mechanisms are eliminated, but one singular anticanonical contact mechanism remains:

\[
\boxed{
D\in|L|=|-K_Y|,
\quad p_a(D)=1,
\quad \widetilde D\simeq\mathbf P^1,
\quad \pi^{-1}(D)\text{ splits over }\mathbf Q.
}
\]

Thus the fixed-curve square-root mechanism has been reduced to one precise contact problem.

## 1. Frozen geometry

Let

\[
Y=\operatorname{Bl}_{4}(\mathbf P^1_r\times\mathbf P^1_s),
\qquad
L=2H_r+2H_s-E_{++}-E_{+-}-E_{-+}-E_{--}=-K_Y,
\]

and let

\[
\pi:X\to Y
\]

be the resolved double cover defined by the Stage14 space-square condition.  Its branch class is `2L`, and

\[
M=\pi^*L,
\qquad M^2=8,
\qquad H_M=d.
\]

In Euclid half-angle parameters,

\[
t(r)=\frac{2r}{1-r^2},
\qquad
t(s)=\frac{2s}{1-s^2},
\]

and the double-cover numerator is

\[
F(r,s)=(1+r^2)^2(1+s^2)^2-16r^2s^2.
\]

Assume `C/Q` is an irreducible physical rational curve with

\[
M\cdot C=4,
\qquad
\deg(C\to\mathbf P^1_r)=2.
\]

Put

\[
D=\pi(C),
\qquad
\delta=\deg(C\to D)\in\{1,2\}.
\]

## 2. A second degree bound that must not be omitted

Because `t(s)=y/e` is also a quotient of two global `M`-sections on `X`, its restriction to `C` has degree at most `M.C=4`.  Since the rational map

\[
s\longmapsto\frac{2s}{1-s^2}
\]

has degree two,

\[
\boxed{\deg(C\to\mathbf P^1_s)\le2.}
\]

This is what makes the image-class problem finite.

We use the convention

\[
D=aH_r+bH_s-\sum m_jE_j,
\]

so `b` is the degree of `D->P1_r` and `a` is the degree of `D->P1_s`.

## 3. New symmetric Kummer coordinates

Define

\[
\boxed{
\lambda=\frac{1-rs}{r-s},
\qquad
\mu=\frac{1+rs}{r+s}.
}
\]

On the physical chamber `0<r<s<1`,

\[
\boxed{\lambda<-1<1<\mu.}
\]

Eliminating `r,s` gives

\[
(\lambda+\mu)r^2-2(\lambda\mu+1)r+(\lambda+\mu)=0,
\]

whose discriminant is

\[
4(\lambda^2-1)(\mu^2-1).
\]

Indeed

\[
\boxed{
(\lambda^2-1)(\mu^2-1)
=
\left(
\frac{(1-r^2)(1-s^2)}{(r-s)(r+s)}
\right)^2.
}
\]

The space-square equation becomes

\[
\boxed{
(\lambda^2+1)(\mu^2+1)
=
\frac{F(r,s)}{(r-s)^2(r+s)^2}.
}
\]

Hence the two rational square conditions combine to the standard product-Kummer form

\[
\boxed{
(\lambda^4-1)(\mu^4-1)=\square.
}
\]

These coordinates are not used to claim the missing contact theorem, but they give the clean coordinate system for Stage14-4aj and the Gaussian-CM/Kummer comparison.

## 4. Case `delta=2`: a connected double cover of a rational image

Here `C->D` has degree two. Since `C->P1_r` has degree two, `D->P1_r` has degree one. The second degree bound gives `deg(D->P1_s)<=1`, so

\[
D=aH_r+H_s-\sum m_jE_j,
\qquad a\in\{0,1\}.
\]

Projection formula gives

\[
L\cdot D=2,
\qquad
\sum m_j=2a.
\]

Since the normalization of `D` is rational and `a<=1`, the only irreducible movable cores are:

1. a constant section `s=c`;
2. an opposite-corner `(1,1)` pencil.

Adjacent corner pairs force one of the four `L`-null toric boundary rulings as a component.

### 4.1 Constant section

For `s=c`,

\[
\operatorname{disc}_rF(r,c)
=2^{16}c^4(c-1)^4(c+1)^4(c^2+1)^4.
\]

For rational `0<c<1` this is nonzero, so the connected inverse image is genus one, not rational.

### 4.2 Opposite-corner pencil

A representative is

\[
1-rs+k(s-r)=0.
\]

After substitution and removal of the automatic squares from the resolved corner intersections, the branch quartic is

\[
Q_k(r)
=(k^2+1)r^4-8kr^3+6(k^2+1)r^2-8kr+(k^2+1),
\]

with

\[
\boxed{
\operatorname{disc}Q_k
=2^{14}(k-1)^6(k+1)^6.
}
\]

The only rational degenerations are `k=+/-1`, and there the `(1,1)` curve itself factors into toric boundary rulings.

Therefore

\[
\boxed{\delta=2\text{ contributes no physical irreducible }M\text{-degree-4 bisection}.}
\]

## 5. Case `delta=1`: splitting/contact curves

Now `C` maps birationally to `D`, so `D->P1_r` has degree two. The second degree bound gives

\[
D=aH_r+2H_s-\sum m_jE_j,
\qquad a\le2.
\]

Projection formula gives

\[
L\cdot D=4,
\qquad
\boxed{\sum m_j=2a.}
\]

For an irreducible `D`, adjunction gives

\[
p_a(D)=1+\frac{D^2-4}{2}\ge0.
\]

This leaves exactly the following geometric possibilities after removing forced `L`-null boundary components.

### 5.1 `a=1`: genus-zero `(1,2)` cores

Here `sum m_j=2`. Nonnegative arithmetic genus forces two simple corner conditions. Same-`s` pairs contain a horizontal boundary ruling and reduce to a section. Four genuine bisection-position classes remain, in two symmetry orbits:

- two corners with the same `r` sign;
- two opposite corners.

Both orbits can be eliminated exactly.

### 5.2 `a=2`, arithmetic genus zero

Here `sum m_j=4`. If the multiplicity pattern is

\[
(2,1,1,0),
\]

then `p_a(D)=0`.  Exhausting all twelve placements and subtracting any boundary curve with negative intersection reduces every class to an `a=1` genus-zero core or to a degree-one section.  Hence this case adds no new contact mechanism.

### 5.3 `a=2`, arithmetic genus one — the crucial survivor

The all-simple pattern

\[
(1,1,1,1)
\]

gives

\[
D=2H_r+2H_s-E_{++}-E_{+-}-E_{-+}-E_{--}=L,
\]

and

\[
D^2=4,
\qquad
p_a(D)=1.
\]

A **singular** member of `|L|` may nevertheless have normalization `P1`. If the branch restriction to such a rational singular anticanonical curve is an even divisor / square in `Q(D)`, the K3 pullback splits and produces exactly the kind of `M.C=4` rational bisection sought in 14-4ah.

This case is not eliminated in 14-4ai.

The earlier tempting inference

```text
D rational => p_a(D)=0
```

is invalid for singular rational curves and must not be used.

## 6. Exact elimination of the genus-zero `(1,2)` same-r orbit

A representative through `(1,+/-1)` can be written

\[
P(r,s)=r\{(-c-d-f)s^2-es+c\}+ds^2+es+f=0.
\]

Substitute `r=-Q/A` into `F`. After removing the automatic square `(s^2-1)^2`, the residual factors as

\[
R_-(s)R_+(s),
\]

with the key difference identity

\[
\boxed{R_+-R_-=4s(c+f)^2(s^2+1).}
\]

Their resultant factors as

\[
\begin{aligned}
\operatorname{Res}(R_-,R_+)
=2^{10}(c+f)^8&(c^2+f^2)
((d-f)^2+e^2)\\
&((c+d+f)^2+d^2)
((2c+d+f)^2+e^2).
\end{aligned}
\]

Every rational zero of these sum-of-squares factors either forces a toric boundary factor or reduces to a lower-degree case.  In the coprime case, a square product forces `R_+` and `R_-` to lie in the same square class. The difference identity then forces the odd coefficients of `R_++R_-` to vanish, so either

\[
e=0,
\]

or

\[
f=c,\qquad d=-c.
\]

In the second branch the quartics have nonzero discriminant unless the defining curve is boundary-degenerate. In the first branch,

\[
\operatorname{disc}R_\pm
=64(c+f)^4(d+f)^4\mathcal R,
\]

where, with

\[
p=c-f,\qquad q=d+f,
\]

one has the sum-of-squares identity

\[
\boxed{
\mathcal R=(p^2+2pq)^2+4q^2(p+2f)^2.
}
\]

A square quartic must have zero discriminant; the resulting rational cases again force a boundary factor. Hence no irreducible same-r genus-zero split curve survives.

## 7. Exact elimination of the genus-zero `(1,2)` opposite orbit

A representative through `(1,1),(-1,-1)` is

\[
P(r,s)=r\{-(c+e)s^2-(d+f)s+c\}+ds^2+es+f=0.
\]

After substitution and removal of `(s^2-1)^2`, the residual is

\[
U_2(s)U_6(s),
\]

with

\[
\boxed{
\operatorname{disc}U_2=-4(c^2+ce+df)^2.
}
\]

The resultant factors as

\[
\begin{aligned}
\operatorname{Res}(U_2,U_6)=2^6&(c^2+f^2)(c^2+ce+df)^4\\
&((c+e)^2+d^2)((d-f)^2+e^2)\\
&((2c+e)^2+(d+f)^2).
\end{aligned}
\]

If the resultant is nonzero, `U2` is a nonsquare quadratic and the product cannot be a square.

The only nontrivial resultant-zero branch is

\[
c^2+ce+df=0.
\]

On the patch `c=1`, write

\[
e=-1-df.
\]

Then

\[
U_2=(1+f^2)(ds-1)^2,
\]

\[
U_6=(ds-1)^2Q_f(s),
\]

where

\[
Q_f=(1+f^2)s^4-8fs^3+6(1+f^2)s^2-8fs+(1+f^2).
\]

Its discriminant is

\[
\boxed{
\operatorname{disc}Q_f=2^{14}(f-1)^6(f+1)^6.
}
\]

Thus the only rational square degenerations are `f=+/-1`; there `P` factors into toric boundary pieces. The remaining resultant-zero sum-of-squares branches similarly reduce to boundary or lower-degree classes.

Hence no irreducible opposite-corner genus-zero split curve survives.

## 8. Deterministic cross-check

The script

```text
stages/stage14/scripts/14-4/degree4_bisection_audit.py
```

recomputes the divisor-class reduction and checks the new `(lambda,mu)` identities exactly over rational samples.

As a deliberately secondary finite algebra check, it searches coefficient boxes `[-5,5]^4` in the two `(1,2)` representative families. It finds many square specializations caused by reducible/boundary factors, but

```text
same-r orbit:   gcd-1 full-bidegree square candidates = 0
opposite orbit: gcd-1 full-bidegree square candidates = 0
```

This finite search is not used as the proof; the resultant/discriminant identities above are the proof for the genus-zero classes.

## 9. Triple restriction on a hypothetical minimal survivor

The third-face relative cover from 14-4ah has branch class `2M`. Therefore on any hypothetical minimal rational bisection `C` with `M.C=4`, the branch degree is

\[
(2M)\cdot C=8.
\]

If the eight intersections are simple, the induced double cover of `C\simeq P^1` has genus

\[
\boxed{g=3}.
\]

Special tangencies or splitting can lower this genus, so this observation alone does not prove a triple saving.  It does, however, give the exact restriction problem to hand to the Stage14-t track once the singular anticanonical contact locus is classified.

## 10. What 14-4ai has and has not proved

Proved:

```text
LAMBDA_MU_KUMMER_COORDINATES_LOCKED=true
DEGREE_TWO_IMAGE_M4_MECHANISM_ELIMINATED=true
GENUS_ZERO_SPLIT_M4_MECHANISM_ELIMINATED=true
ONLY_REMAINING_FIXED_SQRTB_CURVE_TARGET=split singular anticanonical D in |L|
```

Not proved:

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
```

## 11. Next

Stage14-4aj should work entirely on the remaining finite-dimensional problem:

1. parameterize the singular locus in the anticanonical system `|L|`;
2. impose even contact / splitting against the space branch `B~2L`;
3. compare the resulting contact classes with the Gaussian-CM/Kummer lattice in the new `(lambda,mu)` coordinates;
4. determine whether any Q-rational physical member exists;
5. if it exists, compute its first-hit height law and restrict the third-square cover to it;
6. if it does not exist, reject the entire fixed-curve `sqrt(B)` mechanism and return to a genuinely collective rank-jump count.

```text
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION
NEXT=Stage14-4aj singular anticanonical contact discriminant / CM-Kummer lattice classification
```
