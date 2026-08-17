# Stage27-19-r5au — fixed-R dyadic physical-weighted host

```text
TASK_ID=Stage27-19-r5au
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5at
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

r5aq proved the general fixed-modulus physical-weighted estimate

\[
T(X;k)\ll_\varepsilon (Xk)^\varepsilon
\left(\frac Xk+\sqrt X\right).
\]

r5at observes that at a fixed physical space diagonal \(R\), every actual Stage19 kernel satisfies \(k=\kappa\mid R\).

## 1. Replace the ambient cutoff by the actual diagonal

Fix \(R\) and one coefficient cell \((\delta,c_0,c_s,c_n)\), with \(C=c_0c_sc_n\). The exact physical edge formula and \(e\le R\) give

\[
\delta C\mu\rho\nu\sigma\le R.
\]

Set

\[
X_R:=\frac{R}{\delta C}.
\]

For every admissible \(k\mid R\), both \(X_R\le R\) and \(k\le R\). Therefore the general r5aq prefactor may be written, after renaming \(\varepsilon\), as \(R^\varepsilon\):

\[
T_R(X_R;k)
\ll_\varepsilon
R^\varepsilon
\left(\frac{X_R}{k}+\sqrt{X_R}\right).
\]

## 2. Dyadic kernel block at fixed R

Restrict to \(K\le k<2K\). Since every admissible kernel divides \(R\), there are at most \(\tau(R)=R^{o(1)}\) such moduli. Also \(1/k\le1/K\). Hence

\[
\boxed{
T_R(X_R;\kappa\sim K)
\ll_\varepsilon
R^\varepsilon
\left(
\frac{X_R}{K}+\sqrt{X_R}
\right).
}
\]

Thus the varying-modulus factor `K` from r5ar disappears after conditioning on the physical diagonal. In particular the `1/K` density gain survives at the fixed-R coefficient-cell level.

## 3. Boundary term

The square-root term remains. It comes from the boundary part of the hyperbolic congruence count and is not removed by the divisor restriction \(k\mid R\). Therefore the theorem does not by itself imply a strict sub-square-root global bound.

```text
FIXED_R_DYADIC_WEIGHTED_HOST_PROVED=true
FIXED_R_CELL_X=R/(delta*C)
FIXED_R_DYADIC_BOUND=R^eps*(X_R/K+sqrt(X_R))
VARYING_MODULUS_K_FACTOR_REMOVED_AT_FIXED_R=true
ONE_OVER_K_GAIN_SURVIVES_AT_FIXED_R=true
SQRT_X_BOUNDARY_REMOVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5av
```