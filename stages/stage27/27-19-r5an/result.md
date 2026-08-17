# Stage27-19-r5an — squarefree-kernel growing-modulus slope receiver

```text
TASK_ID=Stage27-19-r5an
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5am
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Residual forms

Write

\[
A=c_s^2\sigma^2,\quad B=c_n^2\nu^2,
\quad D=c_0^2\mu^2,\quad E=\delta^2\sigma^2,
\]

so that

\[
Q_1=aA+bB=\kappa c_0^2c'^2,
\qquad
Q_2=bD+aE=\kappa c_n^2w'^2.
\]

Also put

\[
F=c_0^2\rho^2,\qquad G=\delta^2\nu^2,
\]

so

\[
Q_3=aF-bG=\kappa c_s^2w'^2.
\]

Because \(p=a c_s^2\sigma^2\) and \(q=b c_n^2\nu^2\) are coprime and \(Q_1=p+q\), every prime divisor of \(\kappa\) is coprime to \(a,b,c_s,c_n,\sigma,\nu\).

## 2. First exact divisibility

Since \(\kappa\mid Q_1,Q_2\), it divides

\[
D Q_1-B Q_2
=a(AD-BE)
=a\sigma^2(m^2-n^2),
\]

and also

\[
A Q_2-E Q_1
=b(AD-BE)
=b\sigma^2(m^2-n^2).
\]

As \((a,b)=1\),

\[
\kappa\mid \sigma^2(m^2-n^2).
\]

The coprimality above gives \((\kappa,\sigma)=1\), hence

\[
\boxed{\kappa\mid m^2-n^2.}
\]

## 3. Second exact divisibility

Since \(\kappa\mid Q_1,Q_3\),

\[
GQ_1+BQ_3
=a(GA+BF)
=a\nu^2(r^2+s^2),
\]

while

\[
FQ_1-AQ_3
=b(BF+AG)
=b\nu^2(r^2+s^2).
\]

Again \((a,b)=1\) and \((\kappa,\nu)=1\), so

\[
\boxed{\kappa\mid r^2+s^2.}
\]

## 4. Primitive consequence and residue-line receiver

If a prime \(\ell\mid\kappa\) divided \(m\), then the first divisibility would force \(\ell\mid n\), contradicting \((m,n)=1\). Likewise the second divisibility and \((r,s)=1\) show that \(\ell\nmid rs\). Thus

\[
\boxed{(\kappa,mnrs)=1.}
\]

For every prime \(\ell\mid\kappa\), therefore,

\[
(mn^{-1})^2\equiv1\pmod\ell,
\qquad
(rs^{-1})^2\equiv-1\pmod\ell.
\]

The r5 squareclass analysis already gives that \(\kappa\) is odd; the second congruence also forces every \(\ell\mid\kappa\) to admit a square root of \(-1\), hence \(\ell\equiv1\pmod4\). Therefore each prime factor confines the two occupied slopes to at most four paired residue lines:

\[
\boxed{
 m/n\equiv\pm1,\qquad r/s\equiv\pm i_\ell\pmod\ell.
}
\]

By CRT, modulo squarefree \(\kappa\) the survivor lies in at most

\[
4^{\omega(\kappa)}=\kappa^{o(1)}
\]

paired slope classes. Because \((\kappa,mnrs)=1\), both slope ratios are units modulo \(\kappa\), so the ambient ordered unit-slope-pair universe has exactly

\[
\boxed{\varphi(\kappa)^2}
\]

pairs. Uniformly in squarefree \(\kappa\), the standard lower bound for Euler's totient gives

\[
\varphi(\kappa)=\kappa^{1-o(1)},
\qquad
\boxed{\varphi(\kappa)^2=\kappa^{2-o(1)}}.
\]

Thus the local receiver occupies only \(\kappa^{o(1)}\) classes inside a \(\kappa^{2-o(1)}\) unit-pair universe. The fixed-power density gap therefore survives without the false uniform assertion \(\varphi(\kappa)^2\asymp\kappa^2\). This is a genuine growing-modulus local receiver attached to the actual survivor-dependent \(\kappa\).

## 5. Barrier at small kappa

This receiver alone is not a global fixed-power theorem. There is an explicit exactly-two Stage19 survivor

\[
(m,n,r,s)=(7,4,5,3),\qquad R=1073,
\]

with

\[
\kappa=1.
\]

Hence no argument may assume that every survivor carries a growing \(\kappa\). A useful next step must split the population dyadically in \(\kappa\): exploit the residue-line density when \(\kappa\) is large, and combine r5am Pell compression plus the exact diagonal relation

\[
R=(h/\varepsilon)\kappa L
\]

on the small-\(\kappa\) side.

```text
KAPPA_DIVIDES_M2_MINUS_N2_PROVED=true
KAPPA_DIVIDES_R2_PLUS_S2_PROVED=true
KAPPA_COPRIME_TO_MNRS_PROVED=true
KAPPA_PAIRED_SLOPE_RESIDUE_RECEIVER_PROVED=true
KAPPA_MODULUS_CLASS_COUNT=4^omega(kappa)=kappa^o(1)
KAPPA_UNIT_SLOPE_PAIR_UNIVERSE=phi(kappa)^2=kappa^(2-o(1))
KAPPA_ASYMP_KAPPA2_UNIT_PAIR_CLAIM_USED=false
KAPPA_EQ_1_STAGE19_WITNESS_RETAINED=true
GLOBAL_GROWING_KAPPA_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ao
NEXT_TARGET=DYADIC_KAPPA_SPLIT_COMBINING_LARGE_MODULUS_SLOPE_SIEVE_WITH_SMALL_KAPPA_PELL_COMPRESSION
```
