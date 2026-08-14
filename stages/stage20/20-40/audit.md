# Stage20-40 audit

Status: PASS

This fresh re-audit supersedes the prior ambient-cubic-only checkpoint40 audit from PR #935. The prior bound `M_3(B)=O(B^3)` remains true, but the claim that it was the strongest certified project upper bound was incomplete because the already-audited Stage14-e8 Euler-brick theorem was missed.

Stage14-e8 counts exactly the Stage20 population: primitive canonical `0<a<b<c`, `gcd(a,b,c)=1`, all three face diagonals integral, Euclidean height `R=sqrt(a^2+b^2+c^2)<=B`, and no integral-space-diagonal requirement. Its elementary Pythagorean projection plus divisor-envelope argument proves

\[
M_3(B)\ll B\log B\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right)=B^{1+o(1)},
\]

equivalently `M_3(B)=O_epsilon(B^(1+epsilon))` for every fixed `epsilon>0`. Population, cutoff and physical-object multiplicity match literally; no measure or quantifier adapter is required.

This is an upper envelope only. It does not prove a matching lower bound, a two-sided `B^(1+o(1))` growth law, sharpness of polynomial ceiling one, or an asymptotic formula. Checkpoint30 therefore remains `OPEN_GATE_AUDITED_PASS` for the unresolved Stage20 population growth law. The Stage18->Stage20 conditional ratio remains reserved for Stage26. Finite data are not used as proof and no space-diagonal or perfect-cuboid conclusion is introduced.

PRIOR_AUDIT_SUPERSEDED=true
PRIOR_AMBIENT_CUBIC_BOUND=true_but_not_strongest
CHECKPOINT_STATUS=PROVED_AUDITED_PASS
UPPER_BOUND_PROVENANCE=Stage14-e8
STRONGEST_CERTIFIED_PROJECT_BOUND=M_3(B)=B^(1+o(1))
FOR_ALL_EPSILON=M_3(B)=O_epsilon(B^(1+epsilon))
TRUE_UPPER_EXPONENT_IDENTIFIED=false
SHARPNESS_PROVED=false
MATCHING_LOWER_BOUND_PROVED=false
OPEN_GATE=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED
FINITE_DATA_USED_AS_PROOF=false
STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26

AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=PENDING_STATUS_SYNC
UNSYNCED_AUDIT_STATE=stages/stage20/20-controller.json,docs/00_CURRENT_RESEARCH_STATUS.md
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=50
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
