# Stage25-60 deeper-lane triage

STATUS=R504_RESIDUAL_FAIL_REPAIR_SUBMITTED_FOR_FRESH_AUDIT

Persistent route IDs are unchanged.

```text
R501=Meskhishvili_first_positive_power_family
R502=Meskhishvili_third_parametrization_fallback
R503=Yoshida_uniform_varying_fiber_height
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
```

## Audited base

```text
R501_STATUS=PROVED_AUDITED_Theta_B_QUARTER
R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504_ORIGINAL_BASE_STATUS=CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R507_STATUS=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
```

Global envelope remains

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

## R504 — hostile-FAIL repair

The previous audit accepted the original-base rank-one result but rejected a blanket residual `EXTERNAL_THEOREM_GATE` classification because the three OPEN mechanisms had not been concretely executed.

The repair now does the following.

1. identifies the exact product-Kummer model `Km(E0xE0)` with `E0:y^2=x^3-4x`;
2. proves rational finite base change + new section is equivalent to a rational multisection on the original surface;
3. executes the twist-killing cover `BC0`;
4. executes `BC1: k=u^2`, proving the genus-three pullback has quotient `j` values `1728,8000,8000` and no extra `E0` factor;
5. executes `BC2: k=(u^2-1)/(2u)`, proving quotient `j` values `1728,10976,10976` and again no extra `E0` factor;
6. closes aggregation over the existing rank-one multiplication graphs using the exact Lattes degree `n^2` and physical height, obtaining

\[
N_{R504,\mathrm{all\ multiples}}(B)
\ll B^{1/9}\sqrt{\log B}=o(B^{1/4}).
\]

The remaining rational-base-change/multisection problem is now the exact new-object gate: find a degree-two (or other low-degree) `phi` for which the twist cover `C_phi` has an additional `E0`-isogeny factor in its Jacobian, and then prove the Stage19 physical-height/exactly-two adapter.

```text
R504_BC0=CLOSED_NO_QUARTER_UPGRADE
R504_BC1=CLOSED_NO_RANK_JUMP
R504_BC2=CLOSED_NO_RANK_JUMP
R504_GROWING_MULTIPLES=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE
R504_RATIONAL_BASE_CHANGE_EQUIVALENT_TO_RATIONAL_MULTISECTION=true
R504_DEGREE2_GENERAL_GATE=EXTRA_E0_FACTOR_IN_JACOBIAN_OF_C_phi
R504_RESIDUAL=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE_SUBMITTED_FOR_FRESH_AUDIT
R504_RESIDUAL_ROUTE_BOUNDARY_EVIDENCE_COMPLETE_CANDIDATE=true
```

See `r504-base-change-boundary.md` and `r505-r506-discovery-ledger.md`.

## R505/R506 — previous hostile-audit acceptance retained

The previous audit explicitly accepted both mathematical claims and said they need not be reopened.

```text
R505_EXACT_TARGET_RECEIVER_ACCEPTED=true
R505_STAGE15_REUSE_CHAIN_ACCEPTED=true
R505_STATUS=EXTERNAL_THEOREM_GATE_PREVIOUS_MATH_ACCEPTED_BOUNDARY_RECHECK_ONLY
R506_TORIC_SUBSUMPTION_ACCEPTED=true
R506_STATUS=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_PREVIOUS_MATH_ACCEPTED
```

R505 remains the exact common-squarefree-core target receiver

\[
\operatorname{sf}(A)=\operatorname{sf}(B)
\iff A=kP^2,\ B=kQ^2,
\]

and R506 remains its rank-one common-leg coordinate presentation `uv=wz`.

## Reuse/discovery FAIL repair

The mandatory handoff is now materialized rather than implied:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSED_RESULTS=MATERIALIZED_IN_r505-r506-discovery-ledger.md
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=MATERIALIZED
POPULATION_ADAPTERS_PROVED=MATERIALIZED
REPO_REUSE_HANDOFF_COMPLETE_CANDIDATE=true
DISCOVERY_EVIDENCE_BLOCK_COMPLETE_CANDIDATE=true
```

## Current checkpoint60 boundary

```text
R501=PROVED_AUDITED
R502=CLOSED_AUDITED
R503=EXTERNAL_THEOREM_GATE_AUDITED
R504_ORIGINAL_BASE=CLOSED_AUDITED
R504_BC0=CLOSED_CANDIDATE
R504_BC1=CLOSED_CANDIDATE
R504_BC2=CLOSED_CANDIDATE
R504_GROWING_MULTIPLES=CLOSED_CANDIDATE
R504_RESIDUAL=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505=EXTERNAL_THEOREM_GATE_PREVIOUS_MATH_ACCEPTED
R506=CLOSED_PREVIOUS_MATH_ACCEPTED
R507=PROVED_AUDITED
GLOBAL_STAGE25_LOWER_CHANGED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
DEEP_STOP_PENDING_HOSTILE_AUDIT=true
STAGE70_ALLOWED=false
```

Fresh hostile audit is required because this repair newly closes the growing-multiple lane and supplies concrete route-boundary certificates for the previously open R504 base-change/multisection lane. A PASS may certify deep-stop; a FAIL restores only the rejected residual sublane to live status.
