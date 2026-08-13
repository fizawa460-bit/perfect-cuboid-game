# Stage14-t61 — polar Schatten obstruction and signed rectangle reopening

## Purpose

Merged Stage14-t60 gives a correct polar/SVD factorization of the exact t57 two-coordinate Kummer coefficient matrix and shows that two one-side polar fourth moments would be sufficient for the t59 orthogonal-rectangle receiver.

Stage14-t61 asks the next required question:

> can either one-side fourth moment be obtained from the existing tH4-style one-variable `L2` large-sieve transfer, with only `B^{o(1)}` overhead?

The answer is **no**.  The obstruction is already present in the one-prime Kummer matrix itself.  Passing from the signed matrix `C_r` to the positive polar operator `|C_r|=(C_rC_r^*)^{1/2}` creates a genuine Schatten/leverage mass.  A complete one-prime row-correlation argument shows that every singleton evaluation vector has polar energy at least `r^{1/4}` up to an absolute constant.  For two primes `p,q~L`, the polar energy is therefore at least `L^{1/2}`, and its square carries an unavoidable `L` fixed-power scale.

This does **not** invalidate the algebraic implication proved in t60.  It proves that the t60 one-side fourth moments cannot be promoted from generic arbitrary-support tH4 `L2` technology, and that any successful proof of them must exploit the actual physical canonical-prime / primitive-cover support.  More importantly, it identifies the zero-loss route that must be preferred next: keep the signed Kummer matrix inside the `(p,q)` average and attack the t59 orthogonal rectangles directly.

No Stage14 global power saving is claimed.

---

## 1. The aggregated Mellin matrix is unitarily equivalent to the physical Kummer matrix

Let `r == 1 mod 4`, put

\[
n=r-1,
\]

and let

\[
K_r(t,x)
=\chi_r\bigl((x^2-t^2)(1-t^2x^2)\bigr),
\qquad t,x\in\mathbf F_r^*.
\tag{61.1}
\]

Let `C_r(alpha,beta)` be the aggregated coefficient matrix defined in merged t60, so that

\[
K_r(t,x)
=\sum_{\alpha,\beta} C_r(\alpha,\beta)\alpha(t)\beta(x).
\tag{61.2}
\]

Write `U_r` for the unitary multiplicative Fourier matrix

\[
U_r(t,\alpha)=n^{-1/2}\alpha(t).
\]

Then (61.2) is exactly

\[
\boxed{K_r=n\,U_r C_r U_r^T.}
\tag{61.3}
\]

Hence all singular values satisfy

\[
\boxed{s_j(C_r)=s_j(K_r)/n.}
\tag{61.4}
\]

In particular

\[
\|C_r\|_{op}=\|K_r\|_{op}/n,
\qquad
\|C_r\|_{S_1}=\|K_r\|_{S_1}/n.
\tag{61.5}
\]

This is an exact change of basis, not an estimate.

---

## 2. Complete row correlations have only bounded resonant multiplicity

For `t,t' in F_r^*`, define the row correlation

\[
R_r(t,t')
=\sum_{x\in\mathbf F_r^*}K_r(t,x)K_r(t',x).
\tag{61.6}
\]

The zero set of one row polynomial is

\[
\{\pm t,\pm t^{-1}\}.
\tag{61.7}
\]

Therefore the two row root sets agree only if

\[
\boxed{t'\in\{\pm t,\pm t^{-1}\}.}
\tag{61.8}
\]

There are at most four such resonant rows.

Outside (61.8), after deleting square factors if one of the exceptional equations `t^4=1` occurs, the product

\[
(x^2-t^2)(1-t^2x^2)
(x^2-t'^2)(1-t'^2x^2)
\tag{61.9}
\]

has a nonconstant squarefree part of degree at most eight and is not a square.  The elementary Weil bound for a quadratic character sum therefore gives

\[
\boxed{|R_r(t,t')|\le 7\sqrt r+8}
\tag{61.10}
\]

for nonresonant pairs.  The harmless `+8` covers removal of zeroes/square factors and the omission of `x=0`.

For resonant pairs the trivial bound is

\[
|R_r(t,t')|\le n.
\tag{61.11}
\]

Thus every row of the Gram matrix `K_rK_r^*` has absolute row sum at most

\[
\boxed{n(7\sqrt r+12).}
\tag{61.12}
\]

By Schur/Gershgorin,

\[
\boxed{
\|K_r\|_{op}
\le \sqrt{n(7\sqrt r+12)}.
}
\tag{61.13}
\]

Consequently

\[
\boxed{
\|C_r\|_{op}
\le \sqrt{\frac{7\sqrt r+12}{r-1}}
\ll r^{-1/4}.
}
\tag{61.14}
\]

The deterministic audit verifies the root-set resonance classification and the safe envelope (61.10) on the frozen split-prime test set.

---

## 3. Every physical evaluation vector has fixed-power polar leverage

For one row point `t`, define the Fourier evaluation vector

\[
a_t(\alpha)=\overline{\alpha(t)}.
\tag{61.15}
\]

Then `a_t^*C_r` is exactly the multiplicative Fourier coefficient vector of the physical row `x -> K_r(t,x)`.  Parseval gives

\[
\boxed{
a_t^*C_rC_r^*a_t
=\frac1n\sum_{x\in\mathbf F_r^*}|K_r(t,x)|^2.
}
\tag{61.16}
\]

A row has at most four zeroes and every nonzero value of `K_r` has modulus one.  Hence

\[
\boxed{
a_t^*C_rC_r^*a_t\ge\frac{n-4}{n}.}
\tag{61.17}
\]

Now put

\[
H_r=(C_rC_r^*)^{1/2}.
\]

Since every singular value `s` satisfies `s^2 <= ||C_r||_{op}s`, spectral calculus gives the positive-operator inequality

\[
C_rC_r^*\le \|C_r\|_{op} H_r.
\tag{61.18}
\]

Therefore, for **every** `t in F_r^*`, not merely on average,

\[
\boxed{
\begin{aligned}
D_r(t)
&:=a_t^*H_r a_t\\
&\ge
\frac{n-4}{n\|C_r\|_{op}}\\
&\ge
\frac{r-5}{\sqrt{r-1}\sqrt{7\sqrt r+12}}.
\end{aligned}
}
\tag{61.19}
\]

Thus uniformly

\[
\boxed{D_r(t)\gg r^{1/4}.}
\tag{61.20}
\]

This is the key t61 obstruction.  The positive polar half-packet is not an `L2`-safe weight of size `B^{o(1)}`.  It has unavoidable fixed-power leverage even on one physical point.

The same statement holds on the column side because, for `r == 1 mod 4`,

\[
K_r(t,x)=K_r(x,t)
\]

(the sign introduced by swapping is invisible since `chi_r(-1)=1`).

---

## 4. Schatten-1 mass is also necessarily polynomial

Averaging (61.19) over all `t` and using multiplicative-character orthogonality gives

\[
\frac1n\sum_t D_r(t)
=\operatorname{Tr}H_r
=\|C_r\|_{S_1}.
\tag{61.21}
\]

Hence

\[
\boxed{
\|C_r\|_{S_1}
\ge
\frac{r-5}{\sqrt{r-1}\sqrt{7\sqrt r+12}}
\gg r^{1/4}.
}
\tag{61.22}
\]

So the issue is not an unlucky singleton.  The complete polar operator itself carries polynomial Schatten mass.

This is fully compatible with t57/t60:

```text
Hilbert--Schmidt energy of C_r = O(1)
Schatten-1 mass of C_r       >= r^(1/4)
```

There is no contradiction: bounded `S2` does not imply bounded `S1` when the effective rank grows.

---

## 5. Two-prime polar leverage multiplies exactly

Merged t60 proves

\[
C_{pq}=C_p\otimes C_q.
\]

Functional calculus on tensor products gives

\[
\boxed{
(C_{pq}C_{pq}^*)^{1/2}
=H_p\otimes H_q.
}
\tag{61.23}
\]

The CRT evaluation vector is also a tensor product.  Therefore for every good residue point `t`,

\[
\boxed{D_{pq}(t)=D_p(t)D_q(t).}
\tag{61.24}
\]

If

\[
p,q\asymp L,
\]

then (61.20) gives

\[
\boxed{D_{pq}(t)\gg L^{1/2}.}
\tag{61.25}
\]

and hence

\[
\boxed{D_{pq}(t)^2\gg L.}
\tag{61.26}
\]

Thus a generic target-scale one-side fourth-moment theorem which treats a singleton row/column as costing only its source `L2` mass cannot be true uniformly over arbitrary residue supports.  The loss is already a full factor `L` after squaring.

This does not assert that the actual t59 physical family violates the t60 sufficient contracts.  It proves that **generic arbitrary-support** tH4 transfer cannot establish them: any proof must exploit cancellation/distribution specific to the physical canonical-prime or primitive-cover set.

```text
ARBITRARY_SUPPORT_POLAR_FOURTH_MOMENT_TARGET_VALID=false
T60_ONE_SIDE_FOURTH_MOMENTS_REQUIRE_PHYSICAL_SUPPORT_STRUCTURE=true
```

---

## 6. Why tH4 cannot close either side

Merged tH4 provides a weighted transfer rule of the form

\[
\text{base second moment}
\times
\text{coefficient }L2\text{ energy}
\times B^{o(1)}.
\]

Its safe weights are bounded masks, divisor lifts, Gaussian representation lifts, unit phases, and spectral packets whose **coefficient `L2` energy** is bounded.

The t60 polar operation is qualitatively different.  It changes the signed matrix `C_r` into the positive operator `H_r=|C_r|`.  Equations (61.20)--(61.22) show that bounded `S2` energy of `C_r` does not prevent polynomial `S1`/leverage mass of `H_r`.

Therefore neither

```text
CanonicalPrimePolarKummerFourthMoment
PrimitiveCoverPolarKummerFourthMoment
```

is a corollary of the current tH4 one-variable large-sieve transfer.

```text
TH4_DIRECTLY_PROVES_CANONICAL_PRIME_POLAR_FOURTH_MOMENT=false
TH4_DIRECTLY_PROVES_PRIMITIVE_COVER_POLAR_FOURTH_MOMENT=false
```

The old t36/t38 row/column squareclass energies also do not apply: they concern equal-squareclass collisions after one **physical opposite coordinate** is fixed, while `H_r` is obtained by spectral absolute value after summing over the entire opposite character coordinate.

```text
T36_T38_DIRECTLY_CONTROL_POLAR_OPERATOR=false
```

---

## 7. Repair: keep the signed Kummer matrix inside the outer average

The exact t59 rectangle trace is

\[
T_{\mathcal R}(p,q)
=\sum_j X_j^T C_{pq}Y_j.
\tag{61.27}
\]

The t60 polar inequality

\[
|T|^2\le E_AE_B
\]

is algebraically valid, but (61.25) shows why proving `E_A` and `E_B` separately at zero loss is too expensive: taking the positive square root removes the signed/oscillatory cancellation in `C_{pq}` before the auxiliary-prime average can use it.

The zero-loss route must therefore retain

\[
\boxed{
\sum_{p\ne q}
\left|\sum_j X_j^T C_{pq}Y_j\right|^2
}
\tag{61.28}
\]

as a signed matrix-valued bilinear object.

Define the sharpened receiver

```text
SignedOrthogonalRectangleKummerBilinearLargeSieve
```

as the t59 target with the following mandatory theorem contract:

- the `C_{pq}` signs/phases remain inside the `(p,q)` average;
- the t59 row and column projections remain pairwise disjoint within each family;
- the t59 aspect-energy balance is retained;
- the same auxiliary pair `(p,q)` is shared by both coordinates;
- no entrywise absolute value, polar positive operator, squareclass pre-collapse, or independent-modulus tensorisation is allowed.

This is not a new numerical target; it is the **correct theorem shape** for `SharedUEnergyBalancedOrthogonalRectangleSecondMoment` after t61 rules out the generic polar shortcut.

```text
POLAR_ZERO_LOSS_SHORTCUT_VALID=false
SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED=false
```

---

## 8. tH decision

Stage14-t61 **does trigger tH17**.

The reason is new and precise.  tH16 audited the pre-t59 broad toroidal packet and rejected quadratic-large-sieve, naive full-mode Cauchy, direct FI, and direct Wilson imports.  After t59, the physical selector gained the strong orthogonal-rectangle structure.  t60 tried to exploit it through polar factorization.  t61 now proves that this polar shortcut itself carries a fixed-power Schatten/leverage loss.

The remaining theorem is therefore genuinely narrower than the object audited by tH16 and genuinely different from the false/generic polar fourth-moment route.

### Requested Stage14-tH17 task

Independently audit/prove

```text
SignedOrthogonalRectangleKummerBilinearLargeSieve
```

for the exact t59/t61 packet.  In particular test:

1. same-modulus bilinear/trace large-sieve methods applied **before** polar absolute value;
2. `TT*` or dual large-sieve arguments which use pairwise-disjoint rectangle row/column projections;
3. operator-valued / matrix-valued large-sieve formulations preserving the signed `C_{pq}` kernel;
4. whether the t59 aspect-energy balance is sufficient to absorb the rectangle family without a rectangle-count Cauchy factor;
5. any Gaussian-prime / primitive-cover arithmetic input needed on the two physical sides.

It must explicitly reject any route that replaces `C_{pq}` by `|C_{pq}|`, because (61.19)--(61.26) prove a fixed-power polar leverage obstruction.

The live t route does not need to wait:

```text
TH17_NEEDED=true
T_ROUTE_BLOCKED_WAITING_FOR_TH17=false
```

Stage14-t62 can attack the same signed rectangle receiver directly in parallel.

---

## Locked boundary

```text
STAGE14_T61=COMPLETE_POLAR_SCHATTEN_OBSTRUCTION_AND_SIGNED_RECTANGLE_REOPENING
MERGED_T60_IMPORTED=true
ONE_PRIME_KUMMER_MATRIX_FOURIER_EQUIVALENCE_PROVED=true
ONE_PRIME_NONRESONANT_ROW_CORRELATION_WEIL_BOUND=true
ONE_PRIME_KUMMER_OPERATOR_NORM_UPPER=O(r^(-1/4))
ONE_PRIME_POLAR_EVALUATION_LEVERAGE_LOWER=Omega(r^(1/4))
ONE_PRIME_KUMMER_SCHATTEN1_LOWER=Omega(r^(1/4))
TWO_PRIME_POLAR_EVALUATION_LEVERAGE_LOWER=Omega((p*q)^(1/4))
AUXILIARY_SCALE_L_POLAR_SQUARED_LOSS=Omega(L)
ARBITRARY_SUPPORT_POLAR_FOURTH_MOMENT_TARGET_VALID=false
T60_ONE_SIDE_FOURTH_MOMENTS_REQUIRE_PHYSICAL_SUPPORT_STRUCTURE=true
TH4_DIRECTLY_PROVES_CANONICAL_PRIME_POLAR_FOURTH_MOMENT=false
TH4_DIRECTLY_PROVES_PRIMITIVE_COVER_POLAR_FOURTH_MOMENT=false
T36_T38_DIRECTLY_CONTROL_POLAR_OPERATOR=false
POLAR_ZERO_LOSS_SHORTCUT_VALID=false
SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED=false
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false
SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false
SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
TH17_NEEDED=true
TH17_REQUESTED_OBJECT=SignedOrthogonalRectangleKummerBilinearLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH17=false
NEXT=Stage14-t62 attack the signed orthogonal-rectangle Kummer bilinear large sieve directly; run Stage14-tH17 in parallel
```
