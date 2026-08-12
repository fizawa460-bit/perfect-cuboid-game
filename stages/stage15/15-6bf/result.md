# Stage15-6bf — exact denominator rigidity of the Stage15 congruent-number point

Base: Stage15-6be in the current cycle. The old 6bc gate suggested integral-point / twist second-moment literature. Before auditing those theorems, 6bf determines whether the explicit Stage15 point on

\[
E_d:Y^2=X^3-d^2X
\]

is integral or has a genuinely moving rational denominator.

Audit verdict: `PASS` for exact denominator rigidity.

## 1. Primitive coordinate-square split

For one state,

\[
f=\kappa_f c^2,\qquad g=\kappa_g e^2,
\qquad (f,g)=1,
\qquad (\kappa_f,\kappa_g)=1.
\]

Primitivity immediately implies

\[
(c,e)=1,
\qquad (c,\kappa_g e)=1,
\qquad (e,\kappa_f c)=1.
\]

The norm identity is

\[
\boxed{f^2+g^2=kZ^2.}
\]

## 2. Odd denominator primes cannot cancel

Let `p` be an odd prime dividing `c`. Then `p` divides `f`, while `p` does not divide `g`. Hence

\[
kZ^2=f^2+g^2\not\equiv0\pmod p,
\]

so `p` divides neither `k` nor `Z`. The same argument holds for every odd prime dividing `e`.

Therefore

\[
\boxed{(ce,kZ)_{\mathrm{odd}}=1.}
\]

The moving square denominators are not secretly absorbed by the norm core or Gaussian norm.

## 3. Exact 2-primary cases

From 6ay,

\[
U=\frac{kZ}{\lambda ce},
\qquad
\lambda=\begin{cases}
1,&k\kappa\text{ odd},\\
2,&k\kappa\text{ even}.
\end{cases}
\]

Recall `(k,kappa)=1`.

- If `k*kappa` is odd, `lambda=1`; the reduced denominator of `U` is exactly `ce`.
- If `2|k`, primitive sum-of-two-squares parity forces `f,g` odd, hence `c,e` odd. The factor `2=lambda` cancels against the even numerator `kZ`, and the reduced denominator is again exactly `ce`.
- If `2|kappa`, then `k` and `Z` are odd while `lambda=2`; the factor `2` cannot cancel. The reduced denominator is exactly `2ce`.

Thus, with

\[
q(U)=\operatorname{den}(U)>0,
\]

we have the exact formula

\[
\boxed{
q(U)=\begin{cases}
ce,&2\nmid\kappa,\\
2ce,&2\mid\kappa.
\end{cases}}
\]

and since `X=U^2`, the reduced denominator of the elliptic `x`-coordinate is `q(U)^2`.

## 4. Consequence

A generic Stage15 point is a genuine rational point with a point-dependent denominator. It is integral only in the exceptional denominator-one branch, which requires

```text
2 does not divide kappa
c=e=1.
```

Therefore integral-point theorems on the minimal twist model cannot be silently substituted for the Stage15 rational-point packet.

The same odd-prime noncancellation applies to `V_+` and `V_-`: primes dividing `c` or `e` do not disappear from the common descent denominator.

## 5. Frozen exit

```text
STAGE15_6_SUBSTAGE=6bf
STAGE15_6BF_AUDIT_VERDICT=PASS
STAGE15_6BF_GCD_c_e=1
STAGE15_6BF_ODD_DENOMINATOR_COPRIME_TO_kZ=true
STAGE15_6BF_REDUCED_U_DENOMINATOR=ce_if_kappa_odd;2ce_if_kappa_even
STAGE15_6BF_X_DENOMINATOR_IS_POINT_DEPENDENT_SQUARE=true
STAGE15_6BF_GENERIC_STAGE15_POINT_INTEGRAL=false
STAGE15_6BF_EXIT=INTEGRAL_POINT_SECOND_MOMENT_DIRECT_REUSE_AUDIT_READY
```

Next: Stage15-6bg audits the exact available integral-point / second-moment theorems against this denominator structure and freezes the genuinely minimal remaining theorem gate.
