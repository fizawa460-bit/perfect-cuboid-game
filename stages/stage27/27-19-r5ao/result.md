# Stage27-19-r5ao — dyadic kappa slope-sieve count

```text
TASK_ID=Stage27-19-r5ao
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5am-r5an
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

r5an proves that every Stage19 survivor has a squarefree odd integer `kappa` such that

\[
\kappa\mid m^2-n^2,\qquad
\kappa\mid r^2+s^2,\qquad
(\kappa,mnrs)=1,
\]

and every prime divisor of \(\kappa\) is \(1\pmod 4\).

This route counts the resulting congruence receiver on a raw slope box.

## 1. Dyadic counting function

For \(H\ge2\) and \(K\ge1\), let \(\mathcal S(H;K)\) be the set of primitive ordered slope quadruples

\[
1\le n<m\le H,\qquad 1\le s<r\le H,
\]

for which there exists a squarefree odd

\[
K\le k<2K
\]

with

\[
k\mid m^2-n^2,\qquad k\mid r^2+s^2,\qquad (k,mnrs)=1.
\]

The actual Stage19 block with \(K\le\kappa<2K\) is a subset of \(\mathcal S(H;K)\).

## 2. Fixed-modulus count

For a fixed admissible squarefree \(k\), the congruence

\[
(mn^{-1})^2\equiv1\pmod k
\]

has exactly \(2^{\omega(k)}\) unit roots. For each root \(u\), fixing \(n\le H\) leaves at most \(H/k+1\) possible \(m\le H\). Hence

\[
\#\{(m,n):k\mid m^2-n^2\}
\ll 2^{\omega(k)}\left(\frac{H^2}{k}+H\right).
\]

Likewise, because every prime factor of \(k\) is \(1\pmod4\),

\[
(rs^{-1})^2\equiv-1\pmod k
\]

has exactly \(2^{\omega(k)}\) unit roots, and

\[
\#\{(r,s):k\mid r^2+s^2\}
\ll 2^{\omega(k)}\left(\frac{H^2}{k}+H\right).
\]

Therefore

\[
\#\mathcal S_k(H)
\ll 4^{\omega(k)}
\left(\frac{H^2}{k}+H\right)^2.
\]

## 3. Dyadic theorem

**Theorem.** Uniformly for \(1\le K\le H^2\),

\[
\boxed{
\#\mathcal S(H;K)
\ll_\varepsilon
H^\varepsilon\left(\frac{H^4}{K}+H^3\right).
}
\]

### Case 1: \(K\le H\)

Sum the fixed-modulus estimate over \(K\le k<2K\). Since

\[
4^{\omega(k)}\ll_\varepsilon k^\varepsilon,
\]

we obtain

\[
\sum_{k\sim K}
4^{\omega(k)}
\left(
\frac{H^4}{k^2}+\frac{H^3}{k}+H^2
\right)
\ll_\varepsilon
H^\varepsilon
\left(
\frac{H^4}{K}+H^3+H^2K
\right).
\]

For \(K\le H\), the final term is at most \(H^3\).

### Case 2: \(H<K\le H^2\)

Switch the divisor summation. For each primitive \((m,n)\), any admissible \(k\) must divide the nonzero integer \(m^2-n^2\), whose absolute value is less than \(H^2\). Hence the number of such dyadic divisors is

\[
\ll_\varepsilon H^\varepsilon.
\]

For each one, because \(k>H\), the second slope pair has

\[
\ll 2^{\omega(k)}\left(\frac{H^2}{k}+H\right)
\ll_\varepsilon H^{1+\varepsilon}
\]

choices. There are \(O(H^2)\) first slope pairs, giving

\[
\#\mathcal S(H;K)\ll_\varepsilon H^{3+O(\varepsilon)}.
\]

Renaming \(\varepsilon\) gives the displayed theorem. For \(K>H^2\), the set is empty.

## 4. Stage19 specialization

The existing Stage27 physical-height preflight gives

\[
m,n,r,s\ll B^{1/2}
\]

on \(R\le B\). Hence, for a dyadic Stage19 block \(K\le\kappa<2K\), the r5an receiver alone gives the raw slope-box estimate

\[
\boxed{
N_{2,\mathrm{raw}}(B;\kappa\sim K)
\ll_\varepsilon
B^\varepsilon
\left(\frac{B^2}{K}+B^{3/2}\right).
}
\]

This is a genuine fixed-power sparsity statement relative to the ambient four-slope box when \(K\) grows, but it is not yet a useful global Stage19 upper bound.

```text
DYADIC_KAPPA_RAW_SLOPE_SIEVE_PROVED=true
DYADIC_KAPPA_RAW_SLOPE_BOUND=H^eps*(H^4/K+H^3)
FIXED_MODULUS_PAIRED_ROOT_COUNT=4^omega(k)
DIVISOR_SWITCH_FOR_K_GT_H_PROVED=true
STAGE19_RAW_SPECIALIZATION=B^eps*(B^2/K+B^(3/2))
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ap
```
