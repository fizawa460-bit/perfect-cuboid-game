# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage20-50-AUDIT-PASS
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_STATUS=CLOSED_R01_AUDIT_PASS
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE18_STATUS=CLOSED_R01_AUDIT_PASS
STAGE19_STATUS=CLOSED_R01_AUDIT_PASS
STAGE20_STATUS=OPEN_CHECKPOINT_50_AUDIT_PASS
STAGE20_CONTROLLER=stages/stage20/20-controller.json
STAGE20_CURRENT_RESULT=stages/stage20/20-50/result.md
STAGE20_CURRENT_PROOF=stages/stage20/20-50/construction-proof.md
STAGE20_CURRENT_AUDIT=stages/stage20/20-50/audit.md
STAGE20_CURRENT_DATA=stages/stage20/20-20/counts.csv
STAGE20_CURRENT_ENUMERATOR=stages/stage20/20-20/enumerate.py
STAGE20_UPPER_BOUND_PROVENANCE=Stage14-e8
STAGE20_STRONGEST_CERTIFIED_UPPER=M3(B)<<B^(1+o(1))
STAGE20_LOWER_BOUND_PROVENANCE=20-50a_SAUNDERSON_CONSTRUCTION
STAGE20_CERTIFIED_LOWER=M3(B)>>B^(1/6)
STAGE20_POPULATION_INFINITE=true
STAGE20_AUDIT_PERSISTENCE=COMMITTED
STAGE20_NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage20-main-batch
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
```

## Current operation

Stage20 checkpoints10-50 are fresh-audited. Checkpoint50 proves a genuine quantitative lower bound using a one-parameter primitive Pythagorean subfamily of the classical Saunderson Euler-brick identities.

For every even `m>=10`, let `u=m^2-1`, `v=2m`, `w=m^2+1` and

```text
A=u|4v^2-w^2|,
B=v|4u^2-w^2|,
C=4uvw.
```

The internal proof verifies all three face diagonals are integral, `gcd(A,B,C)=1`, canonical order `B<C<A`, injectivity in the allowed parameter, and `R<31m^6`. Therefore every even `m>=10` with `m<=(B/31)^(1/6)` contributes one distinct Stage20 object and

\[
M_3(B)\ge \left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4
\]

for all sufficiently large `B`. Hence

\[
M_3(B)\gg B^{1/6}.
\]

Combined with checkpoint40,

\[
B^{1/6}\ll M_3(B)\ll_\varepsilon B^{1+\varepsilon}
\]

for every fixed `epsilon>0`. This proves the Stage20 population is infinite. It does not identify the true exponent, give an asymptotic, or match the upper envelope. Checkpoint30 therefore remains `OPEN_GATE_AUDITED_PASS` for the unresolved population growth law. Stage18-to-Stage20 thinning remains Stage26; no integral-space-diagonal condition or perfect-cuboid conclusion is introduced.

```text
STAGE_STATUS=OPEN
CHECKPOINT=50
CHECKPOINT_STATUS=PROVED_AUDITED_PASS
SUBLANE=20-50a_SAUNDERSON_CONSTRUCTION
POPULATION_INFINITE=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
CERTIFIED_LOWER_EXPONENT=1/6
MATCHING_LOWER_BOUND_PROVED=false
TRUE_EXPONENT_IDENTIFIED=false
ASYMPTOTIC_FORMULA_PROVED=false
OPEN_GATE_30=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_50=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED
STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26
AUDIT_STATUS=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=true
MERGE_ALLOWED=true
NEXT_CHECKPOINT=60
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage20-main-batch
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
