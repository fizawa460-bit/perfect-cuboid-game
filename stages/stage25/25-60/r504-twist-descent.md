# R504 twist-descent certificate

STATUS=SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504

Let

\[
K=\mathbf Q(k),\qquad F=k^4+1,
\]

and

\[
E_F/K:\quad Y^2=X^3-4F^2X.
\]

This note records the exact descent calculation behind the rank-one claim in `r504-section-lattice.md`.

## 1. Untwisting cover

Over

\[
L=K(s),\qquad s^2=F,
\]

`E_F` becomes the constant curve

\[
E_0:\quad v^2=u^3-4u
\]

under

\[
u=X/F,\qquad v=Y/(Fs).
\]

The cover curve

\[
C:\quad s^2=k^4+1
\]

is `Q`-birational to `E_0` by

\[
Q=\psi(k,s)=
\left(
\frac{2(s+1)}{k^2},
\frac{4(s+1)}{k^3}
\right).
\]

Indeed direct substitution gives `v^2=u^3-4u`, and the inverse has

\[
k=\frac{2u}{v}.
\]

## 2. Deck involution

Let `tau(k,s)=(k,-s)` and `T=(0,0) in E_0[2]`.

For `Q=(u,v)=psi(k,s)`, the transformed x-coordinate is

\[
u(\tau Q)=\frac{2(1-s)}{k^2}=-\frac4u.
\]

On `E_0`, translation by `T` sends

\[
(u,v)\longmapsto
\left(-\frac4u,\frac{4v}{u^2}\right).
\]

The y-coordinate comparison gives

\[
\boxed{\tau(Q)=T-Q.}
\]

## 3. Anti-invariant morphisms

A `K`-rational point on the twist corresponds after untwisting to a map `R:C->E_0` satisfying

\[
\tau(R)=-R.
\]

Modulo constant translations, every nonconstant `Q`-defined map `C->E_0` is an element of

\[
\operatorname{Hom}_{\mathbf Q}(J(C),E_0).
\]

Because `psi` identifies `J(C)` with `E_0`, this is `End_Q(E_0)`. The curve `E_0` has `j=1728`; the nonintegral CM endomorphisms require `i`, hence

\[
\boxed{\operatorname{End}_{\mathbf Q}(E_0)=\mathbf Z.}
\]

Write a map as `[n]Q+S`, where `S` is constant. Using `tau(Q)=T-Q`, anti-invariance gives

\[
[n](T-Q)+S=-[n]Q-S,
\]
so

\[
\boxed{nT+2S=0.}
\]

The nonconstant coefficient must therefore be even. Constant non-torsion translations cannot satisfy this equation; they do not contribute to the twist rank.

Thus the nonconstant anti-invariant lattice has rank one and its primitive coefficient is `2`.

## 4. The explicit Stage25 section is the primitive descended class

The obvious quartic section `(t,z)=(k,1)` maps to

\[
P(k)=(-4k^2,4k(k^4-1))\in E_F(K).
\]

After untwisting,

\[
\widetilde P=
\left(
-\frac{4k^2}{F},
\frac{4k(k^4-1)}{Fs}
\right).
\]

Starting from `Q=psi(k,s)`, exact duplication on `E_0` gives

\[
x([2]Q)=\frac{F}{k^2}.
\]

Translation by `T` then gives

\[
x(T+[2]Q)=-\frac{4k^2}{F}.
\]

The y-coordinate calculation gives the opposite sign of the displayed `widetilde P`, hence

\[
\boxed{\widetilde P=-(T+[2]Q).}
\]

Therefore `P` has nonconstant coefficient `-2`, exactly the primitive allowed coefficient in the anti-invariant lattice. It is not a nontrivial multiple of another `Q(k)` free section.

Consequently

\[
\boxed{E_F(\mathbf Q(k))_{\rm free}=\mathbf Z\,P}
\]

and

\[
\boxed{\operatorname{rank}E_F(\mathbf Q(k))=1.}
\]

## 5. Scope

This certificate concerns the original base `Q(k)`. It does not claim that finite base changes have rank one. A base change can create new sections, which is why the low-degree base-change/multisection lane remains an explicit R504 OPEN_GATE.

```text
R504_TWIST_COVER_IS_E0=true
R504_DECK_ACTION=Q->T-Q
R504_END_Q_E0=Z
R504_ANTI_INVARIANT_COEFFICIENT_PARITY=EVEN
R504_EXPLICIT_P_COEFFICIENT=2_UP_TO_SIGN_AND_TORSION
R504_EXPLICIT_P_PRIMITIVE_IN_TWIST_FREE_LATTICE=true
R504_GENERIC_QK_RANK=1
R504_BASE_CHANGE_RANK_CLAIM=NOT_MADE
```
