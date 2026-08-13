# Stage16S-40 — upper-bound ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage16S-30 is fresh-audited and proves

\[
N_S^{all}(B)\sim B^2/(32G),\qquad N_S^0(B)\sim B^2/(32G),
\]

and, for the faceful complement `C_F(B)=N_S^{all}(B)-N_S^0(B)`, 

\[
C_F(B)=O_\varepsilon(B^{1+\varepsilon})\quad(\forall\varepsilon>0).
\]

Therefore the strongest certified upper bounds are

\[
\boxed{N_S^{all}(B)\ll B^2},\qquad
\boxed{N_S^0(B)\ll B^2},\qquad
\boxed{C_F(B)\ll_\varepsilon B^{1+\varepsilon}}.
\]

The first two are order-sharp because the same audited asymptotics give matching `\gg B^2` bounds. Sharpness of the faceful-complement bound is not known.

Mechanisms are already certified at checkpoint 30: the adapted Hürlimann primitive-Pythagorean-quadruple count supplies the quadratic order; the strict repeated-edge correction is `O(B)`; and marking an integral face gives the nested two-square system `a^2+b^2=e^2`, `e^2+c^2=d^2`, where `r_2(n)<=4 tau(n)` yields the complement bound.

```text
UPPER_BOUND_SPACE_AT_LEAST=N_S^all(B) << B^2
UPPER_BOUND_SPACE_ONLY=N_S^0(B) << B^2
UPPER_BOUND_FACEFUL_COMPLEMENT=C_F(B) <<_epsilon B^(1+epsilon)
ORDER_SHARP_SPACE_AT_LEAST=true
ORDER_SHARP_SPACE_ONLY=true
FACEFUL_COMPLEMENT_SHARPNESS=UNKNOWN
EVIDENCE_LEVEL=EXTRACTED_FROM_AUDITED_STAGE16S_30
FINITE_DATA_USED_AS_PROOF=false
POPULATION_CONTRACT_CHANGED=NO
CAUSAL_CLAIM_ADDED=false

MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=40
CHECKPOINTS_ATTEMPTED=40
CHECKPOINTS_SUBMITTED=40
NEW_CLAIMS=NONE; upper-bound ledger extracted from audited Stage16S-30
REUSED_WEAPONS=Stage16S-30,Hurlimann-2015-after-audited-adapter
CODEX_REQUIRED=false
CODEX_REASON=Ledger extraction only.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
```
