# Stage28-40-r2 — exact relative local Euler product

```text
ROUTE=U11_RELATIVE_LOCAL_EULER_PRODUCT
STATUS=DERIVED_PENDING_FRESH_AUDIT
ROLE=sharpen_equal_sieve_dimension_to_finite_local_constant
```

Checkpoint40 U2 proved only the first-order statement

\[
\log(\alpha_p/\beta_p)=-2\chi_4(p)/p+O(p^{-2}),
\]

so the two local systems have the same sieve dimension `2`.  The exact frozen local laws allow a stronger normalization.

## 1. Exact acceptance ratios

For Stage19 space completion, `stages/stage19/final.md` gives

\[
\alpha_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)}
\]

for good split primes `p=1 mod4`, while `alpha_p=1` for inert odd primes.

For Stage20 third-face completion,

\[
\beta_p=1-\frac{2(p-\chi_4(p))}{p^2+6p+1}.
\]

Hence, outside the fixed bad-prime set:

### Split primes `p=1 mod4`

\[
\boxed{
\frac{\alpha_p}{\beta_p}
=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^3(p+3)}.
}
\]

### Inert primes `p=3 mod4`

\[
\boxed{
\frac{\alpha_p}{\beta_p}
=
\frac{p^2+6p+1}{p^2+4p-1}.
}
\]

The logarithmic expansions are

\[
\log(\alpha_p/\beta_p)=
\begin{cases}
-2/p+20/p^2-218/(3p^3)+O(p^{-4}),&p=1\pmod4,\\
\phantom{-}2/p-8/p^2+122/(3p^3)+O(p^{-4}),&p=3\pmod4.
\end{cases}
\]

## 2. Absolutely normalized constant

Uniformly over good odd primes,

\[
\boxed{
\frac{\alpha_p}{\beta_p}
=
(1-\chi_4(p)/p)^2\left(1+O(p^{-2})\right).
}
\]

Therefore

\[
C_{\rm abs}:=
\prod_{p\text{ odd, good}}
\frac{\alpha_p/\beta_p}{(1-\chi_4(p)/p)^2}
\]

converges absolutely to a positive finite constant.

Let `S_bad` denote the fixed finite odd-prime set excluded by the common good-reduction/local-law interface.  Since

\[
L(1,\chi_4)=\prod_p(1-\chi_4(p)/p)^{-1}=\pi/4,
\]

the good-prime relative product has the conditionally convergent normalization

\[
\boxed{
C_{\rm rel}
=C_{\rm bad}\,L(1,\chi_4)^{-2}C_{\rm abs}
=C_{\rm bad}\frac{16}{\pi^2}C_{\rm abs}
\in(0,\infty),
}
\]

where the explicit finite nonzero factor `C_bad` only corrects the omitted fixed bad primes.  If the frozen exact formulas are valid for every odd prime, then `C_bad=1`.

Thus the Stage19/Stage20 local comparison has not merely equal sieve dimension: after removing the quadratic-character first-order oscillation, it has a genuine finite Euler-product constant.

## 3. Finite diagnostic only

Using the displayed exact formulas for all odd primes in the diagnostic and truncating at `p<=10^6` gives

```text
RAW_PRODUCT_prod(alpha_p/beta_p) ~= 2.11225405
ABSOLUTELY_NORMALIZED_Cabs_TRUNCATED ~= 1.30295010
RECONSTRUCTED_Crel_WITH_Cbad_1 ~= 2.11226314
```

The small difference between the two displayed relative-product diagnostics is only finite truncation of the Dirichlet Euler product.  No limiting numerical constant and no value of `C_bad` are certified by this computation.

```text
FINITE_TRUNCATION_AS_THEOREM=false
C_BAD_PROVED_EQUAL_1=false
C_REL_GREATER_THAN_1_PROVED=false
```

## 4. Stage28 consequence and firewall

The exact local data now say:

```text
POLYNOMIAL_LOCAL_DRIFT=0
FIRST_ORDER_LOG_LOCAL_DRIFT=0
RELATIVE_LOCAL_EULER_CONSTANT_EXISTS=true
```

This sharpens the negative certificate.  Any nonconstant asymptotic scale in `M3/N2` must come from global arithmetic/height/correlation effects rather than the already-known product of good-prime marginal densities.

But `C_rel` is **not** the global bridge constant.  Stage19 and Stage20 count different global rational-lift problems, and primitivity, physical chambers, bad places, the real place, and global correlations are not encoded by this good-prime quotient alone.

```text
M3_OVER_N2_ASYMPTOTIC_CONSTANT_PROVED=false
SOURCE_TARGET_ORDERING_PROVED=false
LOCAL_CONSTANT_MULTIPLIED_INTO_GLOBAL_COUNT=false
```
