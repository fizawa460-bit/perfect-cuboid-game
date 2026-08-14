# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage21-50-REPAIR-PENDING-REAUDIT
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_BASELINE_READY_FOR_STAGE21=true
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE18_STATUS=CLOSED_R01_AUDIT_PASS
STAGE19_STATUS=CLOSED_R01_AUDIT_PASS
STAGE20_STATUS=CLOSED_R01_AUDIT_PASS
STAGE21_STATUS=OPEN_CHECKPOINT_50_REPAIR_PENDING_REAUDIT
STAGE21_CONTROLLER=stages/stage21/21-controller.json
STAGE21_CURRENT_RESULT=stages/stage21/21-50/result.md
STAGE21_REUSE_PREFLIGHT=PASS
STAGE21_STRONGER_SOURCE_INTERFACE=E-1e_PR128
STAGE21_STAGE16S_BASELINE_READY=true
STAGE21_AUDIT_PERSISTENCE=PENDING_REAUDIT
STAGE21_NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage21-audit
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
STAGE21_28_EXPLORATION_POLICY=docs/stage21-28-exploration-policy.md
STAGE16_28_REUSE_PREFLIGHT=docs/stage16-28-reuse-preflight.md
```

## Current operation

Stage21 checkpoint50 bounded repair follows the fresh audit FAIL. The original AR-039 source was traced through PR #878 to the Stage11 two-parameter construction. For admissible coprime `m>n`,

\[
p=m^2+n^2,\qquad d=((m^2+n^2)^2+1)/2.
\]

AR-039 is an injective two-parameter family and already has the audited lower bound

\[
N_{AR039}(B)\ge \frac{\sqrt2}{120\pi^2}B^{1/2}-O(B^{1/4}\log B).
\]

The exact height formula now supplies the missing upper bound: `d<=B` implies `m<(2B)^(1/4)`, and even after dropping congruence/coprimality there are at most `sum_{m<M}(m-1)=O(M^2)=O(B^(1/2))` parameter pairs. Injectivity therefore gives

\[
N_{AR039}(B)=\Theta(B^{1/2}).
\]

Consequently

\[
N_{AR039}(B)/M_1(B)=\Theta(B^{-3/2}(\log B)^{-1})
\]

and, since `N1(B)~const*B(log B)^3`, the **whole** AR-039 family satisfies `N_AR039=o(N1)`. This repairs the exact logical gap identified by audit; checkpoint30/40 claims are unchanged.

```text
STAGE_STATUS=OPEN
CHECKPOINT=50
CHECKPOINT_STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
AR039_SOURCE=PR878_STAGE11_TWO_PARAMETER_FAMILY
AR039_EXACT_HEIGHT=d=((m^2+n^2)^2+1)/2
AR039_INJECTIVE=true
AR039_UPPER=O(B^1/2)
AR039_COUNT=Theta(B^1/2)
AR039_CONDITIONAL_SCALE=Theta(B^-3/2*(logB)^-1)
AR039_NEGLIGIBLE_IN_N1=true
OPEN_GATE=LOG_SQUARED_ENHANCEMENT_BULK_MECHANISM_UNRESOLVED
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING_REAUDIT
AUDIT_PERSISTENCE_STATUS=PENDING_REAUDIT
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=60
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage21-audit
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
