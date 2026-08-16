# Stage27-19-r402d — tau collision-energy diagonal barrier

```text
TASK_ID=Stage27-19-r402d
PARENT_ROUTE=Stage27-19-r402c
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
STATUS=SUBMITTED_AS_MULTI_ROUTE_BATCH_PENDING_FRESH_AUDIT
```

Let

\[
S(B)=\#\mathcal T(B),\qquad
w_B(t)=\#\{Q\in\mathcal A_2(B):\tau(Q)=t\},
\]

so

\[
N_2(B)=\sum_t w_B(t).
\]

Define the full second moment

\[
E_\tau(B)=\sum_t w_B(t)^2
\]

and the ordered off-diagonal collision count

\[
C_\tau(B)=\sum_t w_B(t)(w_B(t)-1).
\]

Then exactly

\[
\boxed{E_\tau(B)=N_2(B)+C_\tau(B)}
\]

and therefore

\[
\boxed{E_\tau(B)\ge N_2(B)}.
\]

The generic Cauchy interface remains

\[
N_2(B)^2\le S(B)E_\tau(B).
\]

However, with only the current support upper

\[
S(B)\le N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

a second-moment theorem strong enough to use the old gate `sigma+eta<1` must, at the half-power support boundary, have `eta<1/2`. Since `E_tau>=N_2`, such a theorem would itself already imply the desired strict sub-half bound directly.

Thus the raw full-energy route does not furnish a cheaper shortcut at the present support boundary. This is a scoped diagonal-barrier statement, not an impossibility theorem for off-diagonal or bandwise energy estimates.

```text
TAU_FULL_ENERGY_IDENTITY_PROVED=true
TAU_OFFDIAGONAL_COLLISION_DEFINED=true
TAU_ENERGY_DIAGONAL_LOWER_BOUND_PROVED=true
TAU_ENERGY_DIAGONAL_LOWER_BOUND=E_tau>=N2
RAW_SECOND_MOMENT_SHORTCUT_CLOSED_AT_HALFWALL=true
OFFDIAGONAL_COLLISION_ROUTE_REMAINS=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r402e
```
