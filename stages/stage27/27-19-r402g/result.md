# Stage27-19-r402g — realized-core support/energy receiver after fixed-core multiplicity removal

```text
TASK_ID=Stage27-19-r402g
PARENT_ROUTE=Stage27-19-r402f
BRIDGE_INPUT=Stage27-19-r6d
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
CURRENT_MU=1/2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The r6 family is frozen.  Its r6d bridge nevertheless discharged the representation-multiplicity gate that stopped r402f:

\[
\#\{(m,n,r,s):s^2(m^2+n^2)=pg,\ n^2(r^2-s^2)=qg\}
\le 4\tau(pg)^2=B^{o(1)}.
\]

We therefore return to the r402 dyadic tau-height route with no polynomial loss hidden inside a fixed `(p,q,g)` core.

For a reduced tau `t=p/q`, let

\[
\mathcal G_t(B)=\{g:\text{at least one physical Stage19 object occurs at }(p,q,g)\},
\qquad G_t(B)=\#\mathcal G_t(B).
\]

On a dyadic height band `T<=H(t)<2T`, r402c gives

\[
\boxed{g<2B^2/H(t)\ll B^2/T.}
\]

Let

\[
\mathcal T_T(B)=\{t:T\le H(t)<2T,\ w_B(t)>0\},
\quad S_T=\#\mathcal T_T(B),
\quad M_T=\sum_{t\in\mathcal T_T}G_t,
\quad E_T=\sum_{t\in\mathcal T_T}G_t^2.
\]

The r6d fixed-core theorem gives uniformly

\[
\boxed{M_T\le N_T\le B^{o(1)}M_T}
\]

and

\[
\boxed{C_T\le B^{o(1)}E_T},
\]

where `N_T=sum_t w_B(t)` and `C_T=sum_t w_B(t)(w_B(t)-1)` are the r402f physical mass and collision count.

Conversely every realized core contributes at least one physical object, so `M_T<=N_T` is exact.  Thus, up to subpower factors, the entire bandwise polynomial mass is now the **incidence count of realized pairs `(t,g)`**.  The old representation entropy is gone.

Since each `g` lies in `[1,O(B^2/T)]`, the trivial support bounds are

\[
G_t\ll B^2/T,
\qquad
M_T\ll S_T B^2/T,
\qquad
E_T\le (\max_tG_t)M_T\ll (B^2/T)M_T.
\]

These bounds alone do not beat `B^{1/2}`: at low `T` they are far too large, while at high `T` the core interval is short but the number of possible reduced tau labels can still be large.  Hence the height/core tradeoff plus fixed-core multiplicity theorem is a genuine reduction, not yet a fixed-power saving.

The exact next quantitative target is now unambiguous.  It is enough to prove, uniformly in dyadic `T`, a fixed `delta>0` such that

\[
\boxed{M_T\ll B^{1/2-\delta+o(1)}}.
\]

Equivalently, because `N_T=B^{o(1)}M_T`, a direct realized `(tau,g)` incidence theorem of this strength closes the upper route without separately estimating collision energy.  A weaker energy route can instead combine

\[
N_T\le S_T+\sqrt{S_TC_T}
\]

with `C_T<=B^{o(1)}E_T`, but after r6d the first-moment incidence target is the cleaner receiver.

Thus r402g removes one layer from the old r402f contract:

```text
OLD_TARGET=representation multiplicity + core support/energy
NEW_TARGET=realized (tau,g) incidence/core support only
```

No fixed-power incidence theorem is proved here.

```text
R6D_FIXED_CORE_MULTIPLICITY_IMPORTED=true
FIXED_CORE_POLYNOMIAL_ENTROPY_REMOVED=true
TAU_BAND_CORE_BOUND_REUSED=g<<B^2/T
REALIZED_CORE_INCIDENCE_DEFINED=true
BAND_MASS_EQ_CORE_INCIDENCE_UP_TO_SUBPOWER=true
BAND_COLLISION_LE_CORE_ENERGY_UP_TO_SUBPOWER=true
FIRST_MOMENT_SUFFICIENT_CONTRACT=M_T<<B^(1/2-delta+o(1)) uniformly in T
REALIZED_CORE_FIXED_POWER_INCIDENCE_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-19-r402h
```
