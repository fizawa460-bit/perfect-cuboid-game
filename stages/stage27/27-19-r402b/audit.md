# Stage27-19-r402b hostile audit

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R402B_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE

FIXED_TAU_AMBIENT_CONIC_ACCEPTED=true
FIXED_TAU_TORIC_EQUATION_ACCEPTED=true
FIXED_TAU_STAGE19_FIBER_GENUS_ONE_ACCEPTED=true
FIXED_TAU_PHYSICAL_FIBER_SMOOTH_ACCEPTED=true

FIXED_TAU_Z_HEIGHT_BOUND_ACCEPTED=true
FIXED_TAU_Z_HEIGHT_BOUND=H(z)<3B
FIXED_TAU_U_HEIGHT_BOUND_ACCEPTED=true
FIXED_TAU_U_HEIGHT_BOUND=H(u)<5B^(3/2)

POINTWISE_FIXED_TAU_SUBPOWER_ACCEPTED=true
POINTWISE_FIXED_TAU_BOUND=w_B(t)<<_t(1+log B)^(rank(E_t(Q))/2)
POINTWISE_UNIFORM_IN_T=false
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
POINTWISE_TO_UNIFORM_PROMOTION_FORBIDDEN=true

EXTERNAL_THEOREM_BOUNDARY=Mordell-Weil finite generation plus Neron-Tate positive-definite height pairing on each fixed elliptic curve E_t/Q
EXTERNAL_THEOREM_UNIFORM_MOVING_T_FAMILY_INPUT=false

FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED_ACCEPTED=true
FIBER_PLUS_STRICT_SUPPORT_CAN_REOPEN=true
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false

AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
NEXT_DERIVED_ROUTE=27-19-r402c
MERGE_ALLOWED=true
```

## Hostile findings

The exact fixed-label identity is correct: for reduced positive `t=p/q`, fixing the r402 label gives

\[
p y^2-q x^2=p+q,
\]

and in homogeneous toric variables

\[
pn^2(r^2-s^2)=qs^2(m^2+n^2).
\]

This is only the ambient exactly-two-face fiber. Reimposing the Stage19 integral-space receiver gives the previously audited smooth genus-one curve `C_t` for every physical `t>0`.

The physical-height transfer is also valid. From r402a one has `m^2+n^2<2B`, `r^2+s^2<2B`, and the corresponding bounds on `n,s`. After reducing the rational square defining `z`, these imply `H(z)<3B`. Since `x=m/n`, `H(x-1)<sqrt(2B)`; with `u=(x-1)/(z-1)` and the physical exclusion `z!=1`, one obtains the safe coarse estimate `H(u)<5B^(3/2)`. Hence on each fixed `C_t`, physical `R<=B` points lie in a projective height ball with logarithmic height `O_t(log B)`.

For a fixed rational `t`, if `C_t(Q)` is nonempty, choosing one rational point identifies the torsor with its elliptic Jacobian up to translation. Mordell-Weil finite generation and the positive-definite Neron-Tate pairing then reduce bounded canonical-height counting to lattice-point counting in rank `r_t`, yielding

\[
w_B(t)\ll_t (1+\log B)^{r_t/2}=B^{o_t(1)}.
\]

This is accepted only pointwise in fixed `t`. The rank, regulator/minimal vector geometry, generators, torsor translation, and naive/canonical height comparison may all vary with `t`; no uniform estimate over `H(t)<2B^2` is supplied. Therefore the result correctly forbids promotion to `max_t w_B(t)=B^{o(1)}`.

Even a hypothetical uniform subpower fiber bound would not by itself improve the global exponent while the only certified support upper is `#T(B)<<_eps B^(1/2+eps)`. Thus the scoped statement `FIBER_ALONE_STRICT_SUBHALF_ROUTE_CLOSED=true` is accepted. It does not close joint support-plus-fiber approaches.

## CI / lifecycle

The dedicated `Stage27-19-r402b fixed tau fiber preflight` workflow on submission head `56b69dfda04476670abbd07fb62b05167ff1668a` is SUCCESS. The parent r402a regression is lifecycle-only: its historical verifier still requires r402a itself to be `SUBMITTED_PENDING_FRESH_AUDIT`, whereas r402b correctly synchronizes r402a as hostile-audited PASS and merged PR #1038. Older r402/r401 regressions are the same successor-state debt and are non-blocking for the fresh r402b mathematics.

Checkpoint40 remains active. Checkpoint50 stays blocked. The next exact r402-native object is same-tau collision energy / horizontal correlation (`27-19-r402c`).
