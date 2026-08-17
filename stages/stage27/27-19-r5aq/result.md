# Stage27-19-r5aq — physical-weighted fixed-kappa hyperbolic sieve

```text
TASK_ID=Stage27-19-r5aq
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ao-r5ap
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

The r5 residual chart is

\[
m=c_0c_s\mu,\quad n=\delta c_n\nu,\quad
r=c_0c_n\rho,\quad s=\delta c_s\sigma,
\]

with \(C=c_0c_sc_n\), and the exact physical edge budget is

\[
\delta C\mu\rho\nu\sigma\le B.
\]

Fix \((\delta,c_0,c_s,c_n)\), and write

\[
X:=\frac{B}{\delta C}.
\]

Every Stage19 survivor in this coefficient cell satisfies

\[
\mu\nu\rho\sigma\le X.
\]

For a fixed admissible squarefree kernel \(k\), r5an gives

\[
k\mid m^2-n^2,\qquad k\mid r^2+s^2,\qquad (k,mnrs)=1.
\]

Hence every coefficient and residual variable occurring above is a unit modulo \(k\). For each choice of signs and square roots of \(-1\), the two congruences become

\[
\mu\equiv A\nu\pmod k,
\qquad
\rho\equiv D\sigma\pmod k,
\]

for units \(A,D\pmod k\). There are at most \(4^{\omega(k)}=k^{o(1)}\) paired choices.

## 1. Hyperbolic pair lemma

For a unit \(A\pmod k\), define

\[
P_A(Y;k)=\#\{(u,v)\in\mathbf Z_{>0}^2:uv\le Y,\ u\equiv Av\pmod k\}.
\]

Then uniformly in \(A,k,Y\),

\[
\boxed{
P_A(Y;k)\ll \frac{Y\log(2Y)}{k}+\sqrt Y.
}
\]

Indeed split at \(v\le\sqrt Y\). For such \(v\), the number of admissible \(u\le Y/v\) is at most \(Y/(kv)+1\), giving

\[
\ll \frac{Y\log(2Y)}k+\sqrt Y.
\]

For \(v>\sqrt Y\), necessarily \(u<\sqrt Y\); invert the unit congruence and sum over \(u\le\sqrt Y\), giving the same bound.

## 2. Fixed-kappa weighted four-variable theorem

Let \(T(X;k)\) count positive \((\mu,\nu,\rho,\sigma)\) with

\[
\mu\nu\rho\sigma\le X
\]

and the two r5an residue relations modulo fixed admissible \(k\). Dyadically decompose the two pair-products \(\mu\nu\) and \(\rho\sigma\). There are only \(X^{o(1)}\) dyadic cells. On a cell with pair-product scales \(U,V\) and \(UV\ll X\), the pair lemma gives

\[
\ll X^{o(1)}
\left(\frac Uk+\sqrt U\right)
\left(\frac Vk+\sqrt V\right).
\]

Using \(UV\ll X\) and

\[
U\sqrt V\le X,\qquad V\sqrt U\le X,
\]

we obtain, after absorbing logarithms and the \(4^{\omega(k)}\) residue choices,

\[
\boxed{
T(X;k)\ll_\varepsilon X^\varepsilon
\left(\frac Xk+\sqrt X\right).
}
\]

Thus the kappa congruence saving survives after the exact physical product budget is imposed, for each fixed modulus.

## 3. Stage19 cell specialization

For one fixed coefficient cell \((\delta,c_0,c_s,c_n)\),

\[
X=\frac{B}{\delta c_0c_sc_n},
\]

so the fixed-kappa survivor host is bounded by

\[
\boxed{
\ll_\varepsilon B^\varepsilon
\left(
\frac{B}{\delta C\,k}
+\sqrt{\frac{B}{\delta C}}
\right).
}
\]

This is a physical-weighted local sieve theorem. It still ignores the stronger residual squareclass equations (S1)-(S3), so it is only an upper host for the actual survivor population.

```text
PHYSICAL_WEIGHTED_FIXED_KAPPA_SIEVE_PROVED=true
HYPERBOLIC_PAIR_LEMMA_PROVED=true
FIXED_KAPPA_WEIGHTED_BOUND=X^eps*(X/k+sqrt(X))
PHYSICAL_CELL_X=B/(delta*C)
RESIDUAL_S1_S3_USED_IN_COUNT=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ar
```
