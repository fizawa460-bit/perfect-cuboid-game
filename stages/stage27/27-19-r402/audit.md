# Stage27-19-r402 — hostile audit

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R402_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
```

## Accepted core

The natural Stage19/r401a coordinate is a legal upper-side physical pushforward label. On the Stage19 survivor surface,

\[
\tau=\frac{x^2-z^2}{z^2-1}=\frac{x^2+1}{y^2-1}
=\frac{s^2(m^2+n^2)}{n^2(r^2-s^2)}.
\]

The final toric expression is defined on the positive exactly-two-face host before imposing integral space diagonal, so the label is not manufactured from the target condition.

The exact same-tau collision receiver is accepted:

\[
s_1^2(m_1^2+n_1^2)n_2^2(r_2^2-s_2^2)
=s_2^2(m_2^2+n_2^2)n_1^2(r_1^2-s_1^2).
\]

## Polynomial realized tau support

The previously audited R501/R502 calibrations give degree-eight reduced rational maps to the tau-line and quarter-power physical family growth. Together with the audited bounded physical parameter multiplicity, this implies

\[
\#\operatorname{Supp}_\tau(N_2(B))\gg B^{1/4}.
\]

This is accepted only as a support lower bound and a route-separation fact. It is not promoted to an upper saving.

```text
TAU_SUPPORT_POLYNOMIAL_LOWER_ACCEPTED=true
TAU_SUPPORT_LOWER_EXPONENT=1/4
FIXED_U_SUBPOLY_CLASS_OBSTRUCTION_AUTOMATICALLY_APPLIES_TO_TAU=false
TAU_CARDINALITY_ALONE_GIVES_UPPER_SAVING=false
```

## Upper interfaces

For survivor weights w_B(t), the exact decomposition

\[
N_2(B)=\sum_t w_B(t)
\]

gives the accepted sufficient gates

\[
\#\mathcal T(B)\ll B^{\sigma+o(1)},\quad \max_t w_B(t)\ll B^{\phi+o(1)}
\Rightarrow N_2(B)\ll B^{\sigma+\phi+o(1)},
\]

with strict-subhalf gate `sigma+phi<1/2`, and

\[
E_\tau(B)=\sum_t w_B(t)^2,\quad
N_2(B)^2\le \#\mathcal T(B)E_\tau(B),
\]

with strict-subhalf gate `sigma+eta<1` when `E_tau(B)<<B^(eta+o(1))`.

These are interfaces only. No support upper theorem, uniform fiber theorem, or weighted energy theorem is proved here.

```text
TAU_MAX_FIBER_UPPER_GATE_ACCEPTED=sigma+phi<1/2
TAU_SECOND_MOMENT_UPPER_GATE_ACCEPTED=sigma+eta<1
TAU_SUPPORT_STRICT_SUBHALF_THEOREM_PROVED=false
TAU_UNIFORM_FIBER_SUBPOWER_THEOREM_PROVED=false
TAU_WEIGHTED_SECOND_MOMENT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
```

## CI / lifecycle note

Dedicated `Stage27-19-r402 tau pushforward upper reentry` CI on submission head `36dde2c8786575093c832ed2307b19255cfe7819` is SUCCESS. Several historical r401/r401a/r401b/r401c workflows are red only because their verifiers freeze earlier `next_expected_command` / pending-successor lifecycle states. The observed r401 failure is exactly `next_expected_command == Stage27-19-r401-audit` after the controller has legally moved to r402; the others are the same successor-state verifier debt already seen in the prior chain. These failures do not contradict r402 mathematics or its dedicated lifecycle verifier and are non-blocking for this intermediate audit. They should be made successor-aware as maintenance rather than interpreted as theorem failures.

## Next route

Checkpoint40 remains open. The most direct derived continuation is `Stage27-19-r402a`: quantify reduced tau height/support on `R<=B` and test whether a genuine support upper exponent `sigma<1/2` is available; otherwise proceed to fixed-tau fiber or collision-energy attacks.

```text
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
NEXT_DERIVED_ROUTE=27-19-r402a
PERFECT_CUBOID_CONCLUSION=NONE
```
