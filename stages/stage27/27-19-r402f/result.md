# Stage27-19-r402f — dyadic tau-height support/collision contract

```text
TASK_ID=Stage27-19-r402f
PARENT_ROUTE=Stage27-19-r402e
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
STATUS=SUBMITTED_AS_MULTI_ROUTE_BATCH_PENDING_FRESH_AUDIT
```

Stage27-19-r402a gives

\[
H(\tau)<2B^2,
\]

and r402c gives, on a dyadic band

\[
T\le H(\tau)<2T,
\]

the common-core restriction

\[
\boxed{g\ll B^2/T}.
\]

Let `T` range over powers of two up to `2B^2`, and define

\[
\mathcal T_T(B)=\{t\in\mathcal T(B):T\le H(t)<2T\},
\]

\[
S_T(B)=\#\mathcal T_T(B),
\]

\[
C_T(B)=\sum_{t\in\mathcal T_T(B)}w_B(t)(w_B(t)-1),
\]

\[
N_T(B)=\sum_{t\in\mathcal T_T(B)}w_B(t).
\]

The r402e argument applies bandwise and gives exactly

\[
\boxed{N_T(B)\le S_T(B)+\sqrt{S_T(B)C_T(B)}}.
\]

There are only `O(log B)` nonempty dyadic height bands, so

\[
N_2(B)=\sum_T N_T(B).
\]

Hence a sufficient bandwise fixed-power contract is: there exists `delta>0` such that uniformly for every dyadic `T<=2B^2`,

\[
\boxed{S_T(B)+\sqrt{S_T(B)C_T(B)}\ll B^{1/2-\delta+o(1)}}.
\]

Then the logarithmic number of bands is absorbed into `B^{o(1)}` and

\[
N_2(B)\ll B^{1/2-\delta+o(1)}.
\]

In exponent notation, if uniformly on every dyadic band

\[
S_T(B)\ll B^{\sigma_T+o(1)},\qquad
C_T(B)\ll B^{\kappa_T+o(1)},
\]

then it suffices that for one fixed `delta>0`,

\[
\boxed{\sup_T\max\{\sigma_T,(\sigma_T+\kappa_T)/2\}\le 1/2-\delta.}
\]

The new arithmetic input from r402c is the simultaneous restriction `g<<B^2/T`. Thus high-height tau bands force small common core, and low-height bands contain fewer rational labels by height. This creates a genuine two-axis future attack, but no representation theorem strong enough to satisfy the displayed uniform bandwise gate is proved here.

The r402c-f batch therefore stops at a precise same-measure restart contract rather than opening another purely formal subroute. A future continuation should estimate the representation multiplicities of

\[
s^2(m^2+n^2)=pg,\qquad n^2(r^2-s^2)=qg
\]

uniformly in dyadic `(H(tau),g)` ranges, or provide an equivalent horizontal-support/off-diagonal-collision theorem.

```text
TAU_DYADIC_HEIGHT_DECOMPOSITION_PROVED=true
TAU_BAND_CORE_TRADEOFF_PROVED=true
TAU_BAND_HYBRID_BOUND_PROVED=true
TAU_BAND_HYBRID_BOUND=N_T<=S_T+sqrt(S_T*C_T)
TAU_BAND_COUNT=O(log_B)
TAU_BAND_STRICT_SUBHALF_CONTRACT_MATERIALIZED=true
TAU_BAND_STRICT_SUBHALF_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
BATCH_STOP_REASON=EXACT_ARITHMETIC_REPRESENTATION_THEOREM_REQUIRED
NEXT_DERIVED_ROUTE=27-19-r402g
```
