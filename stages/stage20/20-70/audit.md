# Stage20-70 audit

Status: FAIL

The bounded synthesis mathematics is substantively sound, including the Stage14-e11 upper interface

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}\qquad(\text{every fixed }\eta<1/46),
\]

its concrete endpoint-free form `M_3(B)<<B(log B)^(5-1/50)`, the audited Stage20-50a lower theorem `M_3(B)>>B^(1/6)`, the exact Stage14-e10 local blocker law, the no-double-charge boundary, and the deferral of `Stage18->Stage20` transition analysis to Stage26.

The closeout nevertheless fails `SELF_CONTAINED_REVIEW_STANDARD_V1` because `stages/stage20/final.md` declares `SELF_CONTAINED_BUNDLE_REQUIRED=YES` but does not yet satisfy the required proof-facing artifact boundary.

## Failure 1: current-Stage load-bearing proof is summarized instead of embedded

The Stage20-50a Saunderson construction is load-bearing for the final lower theorem and infinitude. The final bundle currently lists the conclusions

```text
all three face diagonals integral
gcd(A,B1,C)=1
canonical order 0<B1<C<A
injective parameterization
R<31m^6
```

but does not transcribe the internal proofs of the square identities, primitivity, canonical inequalities, injectivity, and cutoff estimate. Under V1, an internal proof from the current Stage cannot be replaced by a repository path or summary.

Required repair: embed the proof-complete Stage20-50a derivation from `stages/stage20/20-50/construction-proof.md` into `final.md` in dependency order.

## Failure 2: frozen upstream interfaces are not printed in the mandatory contract form

The final bundle imports Stage14-e8, Stage14-e10, and Stage14-e11 as frozen upstream results. V1 requires each load-bearing frozen import to print an explicit interface containing at least

```text
UPSTREAM_STAGE=<stage>
UPSTREAM_THEOREM=<exact theorem statement>
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

The current final bundle states the theorem conclusions and provenance, but does not print these auditable transfer contracts. This is especially load-bearing for the Stage14-e11 explicit `eta<1/46` upper theorem and Stage14-e10 local blocker law.

Required repair: add exact frozen-interface blocks for every load-bearing Stage14 import, including the exact Stage20 population/cutoff/multiplicity match and quantifier limitations. If any adapter is actually required, mark it and prove it internally rather than declaring `false`.

## What does not need repair

- The Stage14-e11 theorem itself was checked against the frozen source and is correctly quoted: every fixed `eta<1/46`, with concrete `eta=1/50`; endpoint `1/46` is not claimed.
- The Stage20-50a theorem was already fresh-audited at checkpoint50 and its mathematics remains valid.
- The bounded synthesis stop rule is satisfied.
- The OPEN_GATE set is legitimate and does not need to be reopened.
- No new computation, literature program, or theorem discovery is required.
- Stage26 remains the owner of the `M_3/M_2` transition and independence/correlation classification.

```text
CHECKPOINT_STATUS=FAIL_REPAIR_REQUIRED
MATHEMATICAL_SYNTHESIS_STATUS=PASS_SUBSTANTIVELY
SELF_CONTAINED_REVIEW_GATE=FAIL
REPAIR_SCOPE=FINAL_BUNDLE_EMBED_CURRENT_STAGE_PROOF_AND_PRINT_FROZEN_UPSTREAM_INTERFACES
NEW_THEOREM_REQUIRED=false
NEW_COMPUTATION_REQUIRED=false
OPEN_GATE_REENTRY_JUSTIFIED=NO
SYNTHESIS_STOP_RULE_SATISFIED=YES

AUDIT_VERDICT=FAIL
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=false
```
