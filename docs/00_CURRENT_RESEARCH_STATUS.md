# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage20-60-SUBMITTED
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_STATUS=CLOSED_R01_AUDIT_PASS
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE18_STATUS=CLOSED_R01_AUDIT_PASS
STAGE19_STATUS=CLOSED_R01_AUDIT_PASS
STAGE20_STATUS=OPEN_CHECKPOINT_60_SUBMITTED
STAGE20_CONTROLLER=stages/stage20/20-controller.json
STAGE20_CURRENT_RESULT=stages/stage20/20-60/result.md
STAGE20_PRIOR_PROOF=stages/stage20/20-50/construction-proof.md
STAGE20_PRIOR_AUDIT=stages/stage20/20-50/audit.md
STAGE20_CURRENT_DATA=stages/stage20/20-20/counts.csv
STAGE20_CURRENT_ENUMERATOR=stages/stage20/20-20/enumerate.py
STAGE20_UPPER_BOUND_PROVENANCE=Stage14-e10_PR184
STAGE20_SECONDARY_UPPER_PROVENANCE=Stage14-e8_PR163
STAGE20_STRONGEST_CERTIFIED_UPPER_CANDIDATE=M3(B)<<B(logB)^(5-eta_EB),eta_EB>0
STAGE20_LOWER_BOUND_PROVENANCE=20-50a_SAUNDERSON_CONSTRUCTION
STAGE20_CERTIFIED_LOWER=M3(B)>>B^(1/6)
STAGE20_POPULATION_INFINITE=true
STAGE20_AUDIT_PERSISTENCE=PENDING
STAGE20_NEXT_CHECKPOINT=70
NEXT_EXPECTED_COMMAND=Stage20-audit
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
```

## Current operation

Stage20 checkpoints10-50 are fresh-audited. Checkpoint60 decomposes the Euler population into distinct causal layers without treating the third face as an independent random-square event.

The two-face host is the shared-edge Pythagorean geometry. Adding the third-square equation produces the Stage14-e8 degree-two cover of the toric two-face base; after normalization/minimal resolution this is the Euler-brick K3 surface. Stage14-e10 supplies exact local blocker masses `delta_2=2/9` and `delta_p=2(p-chi_4(p))/(p^2+6p+1)=2/p+O(p^-2)` for odd primes. These blockers explain systematic rarity but do not determine the true global exponent.

A stronger frozen upper theorem was also recovered at checkpoint60: Stage14-e10 proves
\[
M_3(B)\ll B(\log B)^{5-\eta_{EB}}
\]
for some fixed `eta_EB in (0,1)`. This is asymptotically stronger than the previously reused Stage14-e8 divisor envelope `B log B exp(O(log B/log log B))`. Therefore checkpoint40's `strongest-known` metadata is reinterpreted, while the e8 theorem itself remains valid.

Checkpoint50a supplies the complementary survival mechanism: a primitive/canonical one-parameter Saunderson family with `R<31m^6`, hence `M_3(B)>>B^(1/6)`. Current certified causal envelope:
\[
B^{1/6}\ll M_3(B)\ll B(\log B)^{5-\eta_{EB}}.
\]
This is not a matched growth law. The local sieve, K3 thin-cover theorem, and divisor projection are not multiplied as independent costs. Stage18-to-Stage20 ratio/independence questions remain reserved for Stage26.

```text
STAGE_STATUS=OPEN
CHECKPOINT=60
CHECKPOINT_STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
CAUSAL_MODEL=TWO_FACE_HOST_TO_DEGREE2_K3_COVER
LOCAL_BLOCKERS_PROVENANCE=Stage14-e10_PR184
STRONGEST_UPPER_CANDIDATE=M3(B)<<B(logB)^(5-eta_EB)
ETA_EB_EXPLICIT=false
CERTIFIED_LOWER=M3(B)>>B^(1/6)
DOUBLE_CHARGE_CHECK=PASS
OPEN_GATE_30=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_60=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED
STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26
INDEPENDENT_OF_PRIOR_CONDITIONS=DEFER_STAGE26
AUDIT_STATUS=PENDING
AUDIT_PERSISTENCE_STATUS=PENDING
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage20-audit
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
