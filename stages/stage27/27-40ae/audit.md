# Stage27-40ae hostile intermediate audit

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
TASK_ID=Stage27-40ae
PR=1030
STAGE27_40AE_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
OUTER_U_CARDINALITY_ALREADY_CHARGED_ACCEPTED=true
OUTER_U_CARDINALITY_ALONE_FIXED_POWER_SAVING=false
OUTER_U_DOUBLE_CHARGE_FIREWALL_ACCEPTED=true
OUTER_WEIGHTED_EXCEPTIONAL_MASS_CONTRACT_ACCEPTED=true
OUTER_WEIGHTED_SECOND_MOMENT_CONTRACT_ACCEPTED=true
OUTER_PHYSICAL_WEIGHTED_EXCEPTIONAL_MASS_BOUND_PROVED=false
OUTER_PHYSICAL_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=merge PR #1030; then Stage27-main-batch with checkpoint40 upper exploration retained
```

## Verdict

PASS as an intermediate checkpoint40 upper-route audit. This audit does not close checkpoint40 and does not authorize checkpoint50.

## Source check

Stage14 final Lemma 3.4 explicitly charges the primitive `(U,V)` root-line support inside the same physical host. In the surviving nonproportional region it sets `U=L_x^+`, `V=L_x^-`, `gcd(U,V)=1` and includes the fixed-power cost `(2 phi-chi)` for the primitive pair in the charged ledger. Therefore the mere polynomial cardinality of outer `U` values cannot be multiplied into the existing half-power host as an additional random-class, Cauchy, or reciprocal-cardinality saving.

## Accepted reduction

The route correctly separates already-counted outer-label cardinality from a genuinely new theorem about the distribution of T-incidence mass across those already-counted physical fibers. A legal T-side crossing may therefore come from a same-measure weighted exceptional-baseline estimate, or an equivalently strong weighted mean-square/BDH theorem, provided its exact modulus/sector/headroom decorations match the frozen Stage14 receiver and leave a fixed positive power after the complete capacity ledger.

The displayed sufficient second-moment form is accepted as a reopen contract, not as a theorem already present in the repository. Ordinary unweighted class/modulus averaging is not automatically transferable to the physical `U`-fiber measure.

## Non-claims

No strict sub-square-root theorem is proved. No weighted outer-physical discrepancy theorem is proved. No independence product is claimed, and no perfect-cuboid conclusion is drawn.

## CI note

Submission head `35b479bb0b0d76a703aef8eb0ced9886543971fa` had SUCCESS for the dedicated Stage27-40ae workflow, Stage27-40, Stage27-40aa, Stage27-40ad, Stage27-30/20/10 and relevant Stage26 regressions. The lone Stage27-r401a regression failure was a lifecycle-only `KeyError` on the removed historical convenience key `continue_upper_exploration`; the verifier was made successor-route aware without changing r401a mathematics.
