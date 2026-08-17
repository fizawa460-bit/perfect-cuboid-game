# Stage27-19-r5aj — cross-gcd residual chart and exact physical-edge budget

```text
TASK_ID=Stage27-19-r5aj
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ai
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

Stage27-19-r5ah proved the exact primitive scale

\[
\Gamma=2\delta\varepsilon C,
\qquad
C=c_0c_sc_n,
\]

where

\[
c_0=(m,r),\qquad c_s=(m,s_0),\qquad c_n=(r,n_0)
\]

are pairwise coprime and

\[
n=\delta n_0,\qquad s=\delta s_0.
\]

The purpose of r5aj is to absorb those three cross-gcd channels into residual coprime-scale variables before doing any counting.

Write

\[
m=c_0c_s\mu,\qquad r=c_0c_n\rho,
\]

\[
s_0=c_s\sigma,\qquad n_0=c_n\nu,
\]

with positive integers \(\mu,\rho,\sigma,\nu\). These are exact definitions.

## 1. Exact physical coordinate chart

The raw toric coordinates are

\[
E=4mnrs,
\qquad
X=2rs(m^2-n^2),
\qquad
Y=2mn(r^2-s^2).
\]

Divide by

\[
\Gamma=2\delta\varepsilon c_0c_sc_n.
\]

Since

\[
n=\delta c_n\nu,\qquad s=\delta c_s\sigma,
\]

direct cancellation gives the physical edge

\[
\boxed{
e=\frac{E}{\Gamma}
 =\frac{2\delta}{\varepsilon}
 C\mu\rho\nu\sigma.
}
\]

Likewise

\[
\boxed{
x=\frac{X}{\Gamma}
 =\frac{\rho\sigma}{\varepsilon}(m^2-n^2),
}
\]

and, using \(r^2-s^2=hb\),

\[
\boxed{
y=\frac{Y}{\Gamma}
 =\frac{\mu\nu}{\varepsilon}(r^2-s^2)
 =\frac{\mu\nu}{\varepsilon}hb.
}
\]

These are identities in the physical primitive cuboid, not upper bounds.

## 2. The two integral face diagonals also factor exactly

The two toric Pythagorean identities are

\[
E^2+X^2=[2rs(m^2+n^2)]^2
\]

and

\[
E^2+Y^2=[2mn(r^2+s^2)]^2.
\]

With \(m^2+n^2=ha\), division by \(\Gamma\) yields

\[
\boxed{
d_{ex}=\sqrt{e^2+x^2}
 =\frac{\rho\sigma}{\varepsilon}ha,
}
\]

\[
\boxed{
d_{ey}=\sqrt{e^2+y^2}
 =\frac{\mu\nu}{\varepsilon}(r^2+s^2).
}
\]

Thus the same residual variables controlling cross-gcd cancellation are visible directly in the physical edges and face diagonals.

## 3. Exact edge budget under the physical cutoff

Every physical edge is at most the physical space diagonal, so on \(R\le B\),

\[
e\le R\le B.
\]

Insert the exact formula for \(e\):

\[
\frac{2\delta}{\varepsilon}C\mu\rho\nu\sigma\le B.
\]

Therefore

\[
\boxed{
\delta C\mu\rho\nu\sigma
\le \frac{\varepsilon}{2}B
\le B.
}
\]

This is the first exact physical budget in the r5 route in which the cross-gcd cancellation product \(C\) appears with positive exponent rather than in a denominator. A large cancellation product is therefore not free: increasing \(C\) consumes the physical edge budget linearly.

This still does **not** prove that the population with large \(C\) is fixed-power sparse. The remaining variables can compensate, and a counting theorem is still required.

## 4. Scope

The route proves an exact coordinate reparametrization and a necessary physical-height budget. It does not prove a strict sub-square-root upper bound, a new exponent \(\mu<1/2\), or the true exponent of \(N_2\).

```text
CROSS_GCD_RESIDUAL_CHART_PROVED=true
RESIDUAL_FACTORIZATION=m=c0*cs*mu;r=c0*cn*rho;s0=cs*sigma;n0=cn*nu
PHYSICAL_EDGE_RESIDUAL_FORMULA=e=(2*delta/epsilon)*C*mu*rho*nu*sigma
PHYSICAL_X_RESIDUAL_FORMULA=x=(rho*sigma/epsilon)*(m^2-n^2)
PHYSICAL_Y_RESIDUAL_FORMULA=y=(mu*nu/epsilon)*(r^2-s^2)
INTEGRAL_FACE_DIAGONAL_RESIDUAL_FORMULAS_PROVED=true
EXACT_EDGE_BUDGET=delta*C*mu*rho*nu*sigma<=(epsilon/2)*B<=B
LARGE_C_CANCELLATION_FREE=false
LARGE_C_POPULATION_FIXED_POWER_SPARSE_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ak
```