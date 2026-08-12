# Stage15-6ar — exact binary-quartic Jacobian and rational j=1728 twist parameter

Base: merged Stage15-6aq (`PR #844`, merge commit `10b87c5f`). Stage15-6aq isolated two possible continuations for the remaining global norm-core gate. Stage15-6ar audits the `j=1728` route first and computes the exact rational twist family attached to the small-coordinate-core quartic.

This substage is an **audit/adapter stage**. Verdict: `PASS` for the exact twist identification. No point count is claimed here.

## 1. Stage15 quartic

Fix one primitive Gaussian core

\[
K=A+iB_1,\qquad A^2+B_1^2=k,
\]

and a squarefree coordinate core `kappa` with `(k,kappa)=1`. From 6am the one-state receiver is

\[
\kappa T^2=f_K(a,b)g_K(a,b),
\]

where

\[
f_K=A(a^2-b^2)-2B_1ab,
\qquad
g_K=B_1(a^2-b^2)+2Aab.
\]

Put `F_K=f_K g_K`. Expanding gives

\[
F_K=AB_1a^4+2(A^2-B_1^2)a^3b-6AB_1a^2b^2
-2(A^2-B_1^2)ab^3+AB_1b^4.
\]

Since `kappa*T^2=F_K`, setting `Y=kappa*T` gives the ordinary binary-quartic model

\[
Y^2=G(a,b):=\kappa F_K(a,b).
\]

## 2. Exact invariants

For a binary quartic

\[
g=ax^4+bx^3z+cx^2z^2+dxz^3+ez^4,
\]

use the standard invariants

\[
I=12ae-3bd+c^2,
\]

\[
J=72ace-27ad^2-27b^2e+9bcd-2c^3.
\]

Substitution of the coefficients of `G=kappa*F_K` gives

\[
\boxed{I(G)=12(k\kappa)^2,\qquad J(G)=0.}
\]

The discriminant is

\[
\Delta(G)=\frac{16}{27}(4I^3-J^2)
=2^{12}(k\kappa)^6\ne0.
\]

This independently rechecks the smooth genus-one conclusion from 6am/6an.

## 3. Jacobian

The standard binary-quartic Jacobian formula is

\[
E_{I,J}: y^2=x^3-27Ix-27J.
\]

Hence the exact Jacobian of the Stage15 quartic is

\[
\boxed{E_{k,\kappa}: y^2=x^3-324(k\kappa)^2x}
\]

or equivalently

\[
y^2=x^3-(18k\kappa)^2x.
\]

Primary source for the invariant/Jacobian normalization: Tom Fisher, *On binary quartics and the Cassels--Tate pairing*, Research in Number Theory 8 (2022), Eq. (1)--(2), arXiv:2208.14977.

## 4. Exact squarefree twist parameter

Let

\[
\boxed{d=\operatorname{sf}(18k\kappa)=\operatorname{sf}(2k\kappa).}
\]

Write `18*k*kappa=c^2*d`. The rational scaling

\[
x=c^2X,\qquad y=c^3Y
\]

identifies `E_{k,kappa}` over `Q` with

\[
\boxed{E_d: Y^2=X^3-d^2X.}
\]

Thus the Stage15 quartics are 2-coverings of the classical congruent-number `j=1728` quadratic-twist family.

Because `k` and `kappa` are coprime and squarefree, `s=k*kappa` is squarefree. Therefore

\[
d=\begin{cases}
2s,&2\nmid s,\\
s/2,&2\mid s.
\end{cases}
\]

Conversely

\[
\boxed{s=k\kappa=\begin{cases}
d/2,&2\mid d,\\2d,&2\nmid d.
\end{cases}}
\]

So the twist parameter `d` determines the product `k*kappa` uniquely, up to no polynomial ambiguity at all.

The remaining split of `s` into coprime squarefree `(k,kappa)` has exactly `2^{omega(s)}` ordered prime allocations before the fixed 2-primary convention, hence only `s^{o(1)}` possibilities. Gaussian core orientations and coordinate-cell allocations add only another `s^{o(1)}` factor.

## 5. What this changes

The global obstruction from 6aq can no longer be described merely as a polynomial sum over unrelated norm cores `k`. On the small-kappa branch both one-state quartics share the same `(k,kappa)`, hence the same exact twist parameter

\[
d=sf(2k\kappa).
\]

The correct twist-side packet is therefore

```text
one squarefree twist d
-> s=k*kappa determined uniquely
-> B^o(1) coprime splits s=k*kappa
-> B^o(1) Gaussian/core/cell decorations
-> two rational points on Stage15 2-coverings of the same E_d
-> exact product-height and physical masks retained
```

This is a material sharpening of the theorem gate.

## 6. Audit verdict

```text
AUDIT_STAGE=Stage15-6ar
AUDIT_TARGET=EXACT_J1728_TWIST_PARAMETER
AUDIT_VERDICT=PASS
BINARY_QUARTIC_INVARIANTS_EXACT=true
BINARY_QUARTIC_I=12*(k*kappa)^2
BINARY_QUARTIC_J=0
JACOBIAN_EXACT=true
JACOBIAN_MODEL=y^2=x^3-324*(k*kappa)^2*x
TWIST_PARAMETER_EXACT=true
TWIST_PARAMETER=d=sf(2*k*kappa)
TWIST_PRODUCT_k_times_kappa_RECOVERABLE_FROM_d=true
SPLITS_PER_TWIST=B^o(1)
POINT_COUNT_PROVED=false
```

## 7. Firewalls

- AR-023/024: no scalar twist count is substituted for the physical population; this is only an exact packet label.
- AR-027: no average-twist theorem is applied.
- AR-028: `d` packages the already-existing pair `(k,kappa)` and is not charged as a third independent saving modulus.
- The quartic remains a 2-covering. A rational point on the quartic is **not yet** silently identified with a non-torsion point on `E_d`.

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ar
STAGE15_6AR_AUDIT=true
STAGE15_6AR_AUDIT_VERDICT=PASS
STAGE15_6AR_EXACT_JACOBIAN=true
STAGE15_6AR_EXACT_TWIST_PARAMETER=true
STAGE15_6AR_TWIST_PARAMETER=d=sf(2*k*kappa)
STAGE15_6AR_PRODUCT_k_kappa_DETERMINED_BY_d=true
STAGE15_6AR_SPLIT_MULTIPLICITY=B^o(1)
STAGE15_6AR_TWIST_POINT_COUNT_PROVED=false
STAGE15_6AR_EXIT=EXACT_CONGRUENT_NUMBER_TWIST_PACKET_READY_FOR_HEIGHT_AUDIT
```

Next: Stage15-6as must audit a twist-height theorem against the **actual 2-covering map and point type** before using any canonical-height lower bound.