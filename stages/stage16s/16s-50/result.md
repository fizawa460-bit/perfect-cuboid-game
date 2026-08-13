# Stage16S-50 — lower-bound / construction ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Fresh-audited Stage16S-30 proves

\[
N_S^{all}(B)\sim B^2/(32G),\qquad N_S^0(B)\sim B^2/(32G).
\]

Therefore

\[
\boxed{N_S^{all}(B)\gg B^2},\qquad
\boxed{N_S^0(B)\gg B^2}.
\]

These match checkpoint-40 upper bounds and are order-sharp, with audited leading constant `1/(32G)`.

The sharp lower bound source is the audited Hürlimann cumulative primitive-Pythagorean-quadruple asymptotic after the Stage16S adapter. The Stage16S-20 finite enumerator remains replay evidence only and is not used as an asymptotic proof. No new order-sharp project-specific parametrized subfamily is claimed at this checkpoint.

For `SPACE_ONLY`, the same lower bound survives because checkpoint 30 proves the deleted faceful complement is `O_epsilon(B^(1+epsilon))=o(B^2)`.

```text
LOWER_BOUND_SPACE_AT_LEAST=N_S^all(B) >> B^2
LOWER_BOUND_SPACE_ONLY=N_S^0(B) >> B^2
ORDER_SHARP_SPACE_AT_LEAST=true
ORDER_SHARP_SPACE_ONLY=true
LEADING_CONSTANT=1/(32G)
SHARP_LOWER_BOUND_SOURCE=AUDITED_STAGE16S_30
FINITE_ENUMERATOR_ROLE=REPLAY_ONLY
EXPLICIT_ORDER_SHARP_PROJECT_PARAMETRIC_SUBFAMILY=NOT_CLAIMED
EVIDENCE_LEVEL=EXTRACTED_FROM_AUDITED_STAGE16S_30
POPULATION_CONTRACT_CHANGED=NO
CAUSAL_CLAIM_ADDED=false

MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=50
CHECKPOINTS_ATTEMPTED=40,50
CHECKPOINTS_SUBMITTED=40,50
NEW_CLAIMS=NONE; lower-bound ledger extracted from audited Stage16S-30
REUSED_WEAPONS=Stage16S-20,Stage16S-30,Hurlimann-2015-after-audited-adapter
CODEX_REQUIRED=false
CODEX_REASON=Direct ledger extraction only.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
```

Checkpoint 60 is causal synthesis, so this batch stops before 60 for fresh audit.
