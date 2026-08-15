# Stage25-60 R504/R505/R506 hostile re-audit 2

Status: **PASS for the submitted repair; checkpoint60 remains open**

The previous hostile re-audit left three narrow repair items. This re-audit checks only those items and preserves all earlier accepted mathematics.

## A. Normative stop rule — REPAIRED

The continuation policy again requires remaining open items to require genuinely new external mathematics, and the submission no longer treats `new parametric input` as a deep-stop class. The exceptional R504 base-change/multisection residual is explicitly kept `LIVE_EXPLICIT_CURVE_SEARCH`, with `CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false` and `STAGE70_ALLOWED=false`.

```text
NORMATIVE_STOP_RULE_RESTORED=true
CONTINUATION_POLICY_SELF_RELAXATION_ACCEPTED=false
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
R504_RESIDUAL_DEEP_STOP_CLASS_ACCEPTED=false
```

## B. Q-Kummer scope — REPAIRED

The exact-Q overclaim `Km(E0xE0)` has been removed. The route now records the safe class

```text
R504_STANDARD_Q_KUMMER_IDENTIFICATION=false
R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER
R504_KUMMER_MODEL_EXACT_OVER_Q=false
```

which matches the audited deck action `Q -> T-Q`, with `T` not rationally divisible by two. Previously accepted BC1/BC2 direct pullback certificates are unaffected.

## C. Growing multiples parity lemma — REPAIRED and ACCEPTED

For `F=k^4+1>0`, every real quartic image has

\[
X(t)=-\frac{4Ft^2}{t^4+1}\in[-2F,0],
\]

the bounded/non-identity real component of `E_F(R)`. The generator `P` lies on this component, and the component group is `Z/2`; hence odd multiples lie on the bounded component, while even multiples lie on the identity component `x>=2F` and cannot be real quartic images. Since `P` is the degenerate first class, every nondegenerate physical multiple has odd index `n>=3`.

Together with the already accepted physical-height identities and Lattes degree `n^2`, this closes the submitted graph-lattice aggregate:

\[
N_{R504,\mathrm{all\ multiples}}(B)\ll B^{1/9}\sqrt{\log B}=o(B^{1/4}).
\]

This theorem applies only to the audited rank-one multiplication graph lattice and does not include a genuinely new rational multisection/base change.

```text
R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_ACCEPTED=true
R504_ALL_MULTIPLES_COUNT_UPPER_ACCEPTED=true
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_AUDITED_PASS
```

## D. Checkpoint60 remains iterative

The repair is accepted, but it does not satisfy the normative deep-stop rule because the exceptional rational base-change/multisection search remains live. Therefore this is a PASS-to-continue result, not a PASS-to-Stage70 result.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
REPO_REUSE_HANDOFF_COMPLETE=true
DISCOVERY_EVIDENCE_BLOCK_COMPLETE=true
R505_EXACT_TARGET_RECEIVER_ACCEPTED=true
R506_TORIC_SUBSUMPTION_ACCEPTED=true
R504_BC1_NO_RANK_JUMP_ACCEPTED=true
R504_BC2_NO_RANK_JUMP_ACCEPTED=true
NORMATIVE_STOP_RULE_RESTORED=true
R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER
R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_ACCEPTED=true
R504_ALL_MULTIPLES_COUNT_UPPER_ACCEPTED=true
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_AUDITED_PASS
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
R505_MATHEMATICS_REOPEN_REQUIRED=false
R506_MATHEMATICS_REOPEN_REQUIRED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
NEXT_EXPECTED_COMMAND=merge PR #990; then Stage25-main-batch at checkpoint60
```
