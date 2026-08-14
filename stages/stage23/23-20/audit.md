# Stage23-20 fresh audit

Status: **PASS**

The prior failure was limited to missing concrete candidate-family generation. That defect is repaired without reopening the finite census or upstream theorems.

The matched finite baseline remains valid: `N1(2000)=1434`, `N2(2000)=5`, used only diagnostically.

The repaired submission now materializes a nontrivial explicit Stage17 source family using the AR-039 slice `n=1`, `m=t≡2 (mod 14)`, with explicit formulas for `x,y,p,z,d`. Positivity, canonical ordering, integral space diagonal, primitivity, source exactly-one status, infinitude, and unbounded height are carried by the frozen AR-039 source contract. The two candidate second-face conditions are then derived explicitly as square-value equations on this family.

For the `x-z` face the condition becomes a degree-8 hyperelliptic square-value model, generically genus 3; for the `y-z` face it becomes a degree-6 hyperelliptic model, generically genus 2 after removing the obvious square factor. The exact integer scan on the certified congruence slice `2<=t<200000`, `t≡2 mod 14`, reports zero hits for both added-face conditions. This finite scan is correctly kept exploratory and is not promoted to a nonexistence theorem.

Therefore the strengthened aggressive-search requirement is now genuinely satisfied: a concrete infinite candidate family was generated, the Stage19 gates were applied in order, the failure point was localized to the new second-face square condition on the tested slice, and the resulting higher-genus obstruction was recorded. No infinite Stage19 family, positive-power lower bound, matching half-power family, or true target exponent is claimed.

The natural next attack remains live at checkpoint30: rational-point analysis or alternative Stage17 slices/families that may degenerate to genus 0/1, together with the certified Stage19 upper-bound comparison. Upper-bound-only completion remains forbidden.

```text
AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=30
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
REPAIR_SCOPE=COMPLETE
FINITE_CENSUS_REOPEN_REQUIRED=false
UPSTREAM_THEOREM_REOPEN_REQUIRED=false
AGGRESSIVE_SEARCH_POLICY=REQUIRED
CANDIDATE_FAMILY_GENERATION_STATUS=PASS_MATERIALIZED
TRUE_EXPONENT_IDENTIFIED=false
```
