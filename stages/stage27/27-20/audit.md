# Stage27-20 hostile audit

AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
CHECKPOINT20_STATUS=DERIVED_EXACT_FINITE_AUDITED_PASS_AWAITING_MERGE
PR=1023

The exact finite diagnostic panel is accepted under the frozen primitive/canonical exactly-two-face integral-space `N2` population with exact Euclidean cutoff `R<=B`.

Source joins are consistent. Stage19 supplies the exact early counts and the exact endpoint `N2(500,000,000)=3495`; Stage24 r203 explicitly records an exact same-population ladder through one million and the one-million directional vector `(98,101,56)`. Population, cutoff, and physical multiplicity therefore remain matched.

The derived diagnostics recompute correctly. In particular

`alpha_eff(1,000,000,500,000,000)=log(3495/255)/log(500)=0.421237360111...`,

`N2/sqrt(B)` changes from `0.255000000` to `0.156301152`, and `N2/B^(1/4)` changes from `8.063808033` to `23.372473659`. The directional broad-window effective exponents also recompute as approximately `0.424888256`, `0.419684576`, and `0.417519733`.

These are finite diagnostics only. They do not identify the asymptotic exponent, disprove half-power growth, prove quarter-power sharpness, prove a strict sub-square-root whole-family upper, or prove a lower exponent above one quarter. Using the panel to prioritize the later sub-half upper attack while keeping the lower-family lane open is a research-routing decision, not a theorem promotion.

The dedicated Stage27-20 workflow is SUCCESS on submission head `2ef8f20455cff525d82f480d7d08157fd3793706`. One historical Stage25 reentry phase10 regression fails only because its verifier still requires a removed historical status-line token in the current research-status document; its own frozen controller/audit contracts are otherwise intact. This lifecycle debt is outside the Stage27-20 mathematical scope and does not alter this verdict.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
CHECKPOINT20_STATUS=DERIVED_EXACT_FINITE_AUDITED_PASS_AWAITING_MERGE
EXACT_FINITE_PANEL_ACCEPTED=true
EXACT_SOURCE_JOIN_ACCEPTED=true
BROAD_WINDOW_ALPHA_EFF_ACCEPTED=true
DIRECTIONAL_FINITE_DIAGNOSTICS_ACCEPTED=true
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
TRUE_N2_EXPONENT_IDENTIFIED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=30
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=merge PR #1023; then Stage27-main-batch
```
