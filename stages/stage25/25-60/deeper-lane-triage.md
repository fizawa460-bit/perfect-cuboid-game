# Stage25-60 deeper-lane triage

STATUS=R505_R506_BOUNDARY_SUBMITTED_FOR_FRESH_AUDIT

The route IDs below are persistent allocations inherited from checkpoint50. They are not audit-round numbers and must not be renamed between audits.

## Route registry

```text
R501=Meskhishvili_first_positive_power_family
R502=Meskhishvili_third_parametrization_fallback
R503=Yoshida_uniform_varying_fiber_height
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
```

## Historical verifier compatibility and audited base

```text
R501_STATUS=PROVED_AUDITED_Theta_B_QUARTER
R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R507_STATUS=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R502_GCD_GLOBAL_BOUND=2592
HISTORICAL_R502_SUBMISSION_MARKER=R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
HISTORICAL_R503_GATE_MARKER=R503_UNIFORM_VARYING_FIBER_HEIGHT_COUNT=NOT_PROVED
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
```

The global audited Stage19 envelope remains

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Neither R501 nor R502 family-specific `Theta(B^(1/4))` is a global upper bound.

## R503 — audited external/base-change gate

R503 passed hostile audit. The original Yoshida surface has geometric generic rank zero, so its direct generic-section route is closed. The displayed fixed-fiber orbit and displayed positive-rank-parameter sequence are height-sparse. Base change, exceptional positive-rank fibers, and a uniform physical small-point theorem remain future-input gates.

```text
R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED
R503_EXPONENT_UPGRADE_PROVED=false
```

## R504 — audited original base; residual gate submitted

R504's hostile-audited original-base theorem is

\[
\operatorname{rank}E_F(\mathbf Q(k))=1,
\]

with no second independent `Q(k)`-section. The first nondegenerate fixed section gives

\[
N_{R504,3P}(B)=\Theta(B^{1/10}),
\]

so it does not beat the quarter-power lower.

```text
R504_STATUS=ORIGINAL_SURFACE_SECTION_ROUTE_CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R504_GENERIC_QK_RANK=1
R504_SECOND_INDEPENDENT_QK_SECTION_EXISTS=false
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_3P_EXACT_FAMILY_GROWTH=Theta(B^(1/10))
R504_CURRENT_SECTION_BEATS_QUARTER=false
```

The residual low-degree-base-change / multisection / growing-multiple directions were searched as a bounded continuation. No ready same-measure Stage19 polynomial-count adapter was found. These mechanisms are not claimed impossible; a genuinely new explicit base change or suitable uniform theorem reopens R504.

```text
R504_LOW_DEGREE_BASE_CHANGE_EXPLICIT_UPGRADE_FOUND=false
R504_RESIDUAL_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R504_NEW_EXPLICIT_BASE_CHANGE_REOPENS_ROUTE=true
```

See `r504-base-change-boundary.md`.

## R505 — exact common-core target receiver

For Stage19 toric parameters,

\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2,
\]

and

\[
E^2+X^2+Y^2=4AB.
\]

Hence integral space is exactly

\[
\operatorname{sf}(A)=\operatorname{sf}(B)
\iff
A=kP^2,\ B=kQ^2.
\]

R505 is therefore the exact target condition, not a construction family by itself.

The Stage15 attack ledger was reused through its moving-genus-one, 2-covering/descent, physical-product-height, fixed-diagonal-fiber, codimension-two congruence, blind-rediscovery, channel-gcd, and physical complementary-divisor reductions. Those attacks repeatedly reduce the whole-family problem to new physical-height uniformity/average input; no new non-equivalent executable lower construction was found in the bounded Stage25 rediscovery.

```text
R505_EXACT_TARGET_RECEIVER=true
R505_RECEIVER_IS_NOT_CONSTRUCTION_BY_ITSELF=true
R505_STAGE15_INTERNAL_ROUTE_SEARCH_REUSED=true
R505_STATUS=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505_REOPEN_CONDITION=NEW_UNIFORM_PHYSICAL_HEIGHT_THEOREM_OR_NEW_EXPLICIT_PARAMETRIC_FAMILY
```

See `r505-common-core-gate.md` and `r505-r506-discovery-ledger.md`.

## R506 — common-leg coordinates are R505 coordinates

Set

\[
u=mr,\quad v=ns,\quad w=ms,\quad z=nr.
\]

Then

\[
uv=wz,
\qquad
A=u^2+v^2,
\qquad
B=w^2+z^2.
\]

The relation `uv=wz` is rank one and conversely reconstructs the two toric projective ratios. Thus R506 has no independent parameter dimension or target equation: it is R505 written in common-leg coordinates.

```text
R506_RANK_ONE_IDENTITY=uv=wz
R506_INDEPENDENT_PARAMETER_DIMENSION=false
R506_SUBSUMED_BY_R505_EXACT_TORIC_RECEIVER=true
R506_STATUS=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
```

See `r506-common-leg-subsumption.md`.

## Current checkpoint60 boundary

The proposed route classes, pending fresh hostile audit, are now:

```text
R501=PROVED_AUDITED
R502=CLOSED_AUDITED
R503=EXTERNAL_THEOREM_GATE_AUDITED
R504_ORIGINAL_BASE=CLOSED_AUDITED
R504_RESIDUAL=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
R507=PROVED_AUDITED
```

No new global exponent is asserted.

```text
GLOBAL_STAGE25_LOWER_CHANGED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
CHECKPOINT60_SINGLE_SHOT=false
AUDIT_PASS_DOES_NOT_CLOSE_LIVE_ROUTES=true
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
DEEP_STOP_PENDING_HOSTILE_AUDIT=true
STAGE70_ALLOWED=false
```

If the audit accepts the proposed R504-residual/R505/R506 boundary classifications, checkpoint60 has a deep-stop candidate: every currently assigned route is then proved, closed with certificate, or reduced to a genuinely new external/new-parametric input gate. This is not a permanent mathematical-exhaustion claim; new input can reopen a route.
