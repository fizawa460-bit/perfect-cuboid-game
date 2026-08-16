# Stage27-19-r402e — off-diagonal collision/support hybrid gate

```text
TASK_ID=Stage27-19-r402e
PARENT_ROUTE=Stage27-19-r402d
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
STATUS=SUBMITTED_AS_MULTI_ROUTE_BATCH_PENDING_FRESH_AUDIT
```

Retain

\[
S=\#\mathcal T(B),\qquad N=N_2(B),\qquad C=C_\tau(B)=\sum_t w_t(w_t-1).
\]

Because every occupied fiber has `w_t>=1`,

\[
N-S=\sum_t(w_t-1).
\]

For every integer `w>=1`,

\[
w-1\le \frac{w(w-1)}2,
\]

so

\[
\boxed{N-S\le C/2}.
\]

A sharper quadratic interface comes from

\[
N^2\le S\sum_t w_t^2=S(N+C).
\]

Solving the quadratic inequality in `N` yields

\[
N\le \frac{S+\sqrt{S^2+4SC}}2
\le S+\sqrt{SC}.
\]

Hence

\[
\boxed{N_2(B)\le S(B)+\sqrt{S(B)C_\tau(B)}}.
\]

If future same-measure estimates give

\[
S(B)\ll B^{\sigma+o(1)},\qquad C_\tau(B)\ll B^{\kappa+o(1)},
\]

then

\[
\boxed{N_2(B)\ll B^{\max\{\sigma,(\sigma+\kappa)/2\}+o(1)}}.
\]

A sufficient strict-subhalf gate is therefore

\[
\boxed{\sigma<1/2\quad\text{and}\quad \sigma+\kappa<1}.
\]

This explicitly shows why off-diagonal control alone cannot break the wall if the support term itself remains at exponent `1/2`: the `S(B)` term survives even when collisions vanish.

There is also an exact heavy-fiber interface. For any integer `L>=2`,

\[
\#\{t:w_t\ge L\}\le \frac{C}{L(L-1)},
\]

and

\[
\sum_{w_t\ge L} w_t\le \frac{C}{L-1}.
\]

Thus a collision theorem can legally control exceptional heavy-fiber mass, but a strict global upper still needs a complementary horizontal support theorem.

```text
TAU_OFFDIAGONAL_EXCESS_BOUND_PROVED=true
N_MINUS_SUPPORT_LE_C_OVER_2=true
TAU_HYBRID_BOUND_PROVED=true
TAU_HYBRID_BOUND=N<=S+sqrt(S*C)
TAU_HYBRID_EXPONENT=max(sigma,(sigma+kappa)/2)
TAU_HYBRID_STRICT_SUBHALF_GATE=sigma<1/2_and_sigma+kappa<1
TAU_HEAVY_FIBER_COUNT_BOUND_PROVED=true
TAU_HEAVY_FIBER_MASS_BOUND_PROVED=true
OFFDIAGONAL_ALONE_BREAKS_HALFWALL=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r402f
```
