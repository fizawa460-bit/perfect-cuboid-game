# Stage27-19-r5av — fixed-R coefficient-cell summation and boundary barrier

```text
TASK_ID=Stage27-19-r5av
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5au
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

r5au proves, for one fixed physical diagonal \(R\), one coefficient cell \((\delta,c_0,c_s,c_n)\), and a dyadic kernel block \(\kappa\sim K\),

\[
T_R\ll_\varepsilon
R^\varepsilon
\left(
\frac{X_R}{K}+\sqrt{X_R}
\right),
\qquad
X_R=\frac{R}{\delta c_0c_sc_n}.
\]

This route sums that host over coefficient cells and locates the remaining loss.

## 1. Sum over the coefficient product

Write

\[
t=\delta c_0c_sc_n.
\]

Ignoring the pairwise-coprimality restrictions only enlarges the host. The number of ordered positive quadruples with product \(t\) is \(d_4(t)\). Positive residual variables require \(t\le R\). Hence

\[
\sum_{\delta,c_0,c_s,c_n}
\frac{X_R}{K}
\le
\frac RK\sum_{t\le R}\frac{d_4(t)}t
\ll
\frac RK(\log(2R))^4.
\]

For the boundary term, using the standard divisor bound \(d_4(t)\ll_\varepsilon t^\varepsilon\),

\[
\sum_{\delta,c_0,c_s,c_n}\sqrt{X_R}
\le
\sqrt R\sum_{t\le R}\frac{d_4(t)}{\sqrt t}
\ll_\varepsilon R^{1+\varepsilon}.
\]

Therefore the complete fixed-R raw coefficient-cell host obeys

\[
\boxed{
T_R^{\mathrm{all\ cells}}(\kappa\sim K)
\ll_\varepsilon
R^\varepsilon\left(\frac RK+R\right).
}
\]

After renaming \(\varepsilon\), this is simply \(R^{1+\varepsilon}\) in the worst case.

## 2. What has and has not been solved

The first term retains the desired growing-modulus saving \(1/K\). The obstruction is now isolated in the accumulated square-root boundary term:

\[
\sum \sqrt{X_R}=R^{1+o(1)}.
\]

Thus the varying-modulus entropy identified in r5ar is no longer the active obstruction after conditioning on \(R\); the active obstruction is the boundary population of the hyperbolic congruence count, together with the unresolved support count over physical diagonals.

A useful successor must either:

1. factor the congruences \(\kappa\mid(m^2-n^2)\) and \(\kappa\mid(r^2+s^2)\) more sharply on the boundary so that the \(\sqrt{X_R}\) contribution acquires a modulus saving; or
2. prove a fixed-power bound for the actual fixed-R outer support, using (S1)-(S3) rather than the raw coefficient host.

No such global theorem is claimed here.

```text
FIXED_R_COEFFICIENT_CELL_SUM_PROVED=true
FIXED_R_ALL_CELL_BOUND=R^eps*(R/K+R)
ONE_OVER_K_MAIN_TERM_SURVIVES=true
SQRT_BOUNDARY_ACCUMULATES_TO_R1_PLUS_O1=true
MODULUS_ENTROPY_IS_CURRENT_PRIMARY_BARRIER=false
HYPERBOLIC_BOUNDARY_IS_CURRENT_PRIMARY_BARRIER=true
FIXED_R_OUTER_SUPPORT_FIXED_POWER_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5aw
NEXT_TARGET=BOUNDARY_FACTORIZATION_OR_FIXED_R_OUTER_SUPPORT_COUNT
```