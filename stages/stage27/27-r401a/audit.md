# Stage27-r401a hostile intermediate audit

AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
TASK_ID=Stage27-r401a
PR=1026
AUDIT_SCOPE=INTERMEDIATE_CHECKPOINT40_UPPER_EXPLORATION
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true

## 1. Off-wall bound

Accepted. Stage14's complete balanced-packet bounds are `E_k<=3theta-1/4` for the low-theta side and `E_RRF<=1-2theta` for the high-theta nonempty side, with the proportional branch already at most `7/16` and `chi>1/4` nonproportional cells empty. For fixed `gamma>0`, `theta<=1/4-gamma` gives `1/2-3gamma`, while `theta>=1/4+gamma` gives `1/2-2gamma`. The `B^o(1)` decorated/dyadic covering preserves the uniform off-wall theorem

`N2,off(gamma)(B) << B^(1/2-2gamma+o(1))`.

No new measure or independence assumption is introduced.

## 2. Critical wall prior-art correction

Accepted. The Stage14 frozen final bundle identifies X13 as the active square-root closure theorem and records the balanced packet with `alpha,delta=B^(theta+o(1))`, `beta,gamma=B^(1/2-theta+o(1))`. The terminal case split saturates at `theta=1/4`; hence r401a correctly treats the wall as prior Stage14/X13 knowledge rather than a new Stage27 discovery. The new content of r401a is the fixed-width off-wall formulation and current synchronization, not discovery of the wall.

## 3. MAIN / T / S terminal gates

Accepted at the repository-contract level. The frozen Stage14 source map and closeout record MAIN at `14-4gh/14-4ghH`, T at `14-t157` plus `14-tH31..33`, and S at `14-s7-162..164`, with all active analytic routes parked and no legal cross-promotion. r401a's terminal gate labels are consistent with those route families:

- MAIN: nested K-free quadratic-divisor CRT first moment on primitive rectangles;
- T: individual super-Kai Gaussian-residue long-interval prime occupancy;
- S: uniform domination of moving witness-coupled target character classes.

No hypothetical savings are multiplied.

## 4. Stage15 / Stage26 reusable fixed-power input

Accepted as a negative compatibility result. Stage15 Q07--Q10 are executed or negatively certified without the materially new same-measure theorem needed to reopen them; Q11 gives exact same-measure local acceptance but only logarithmic Euler-product thinning. Stage26's strongest new positive-power theorem is a lower construction for the distinct `M3` no-space/Euler population and is not an upper theorem for `N2`. No legal fixed-power crossing from these sources into the critical-wall `N2` upper has been exhibited.

## 5. Repo-native branch completeness firewall

The mathematical conclusion is accepted only with this scope restriction:

`NO_CURRENTLY_IDENTIFIED_COMPATIBLE_REPO_NATIVE_FIXED_POWER_ROUTE=true`

The stronger absolute statement `NO_REPO_NATIVE_UNEXECUTED_ROUTE_EXISTS=true` is NOT audited. The repository's own deep-review queue explicitly states that its curated review does not constitute theorem-level manual audit of every remaining review-required record. Therefore PASS does not authorize closing exploration on an exhaustiveness claim.

The following candidates remain mandatory checkpoint40 continuation targets even after this PASS:

1. `R401-NEXT-MAIN-CRT2`: second-order / two-level CRT first-moment attack on the MAIN nested quadratic-divisor receiver, seeking a same-measure fixed-power deficit on the critical wall rather than another one-progression estimate.
2. `R401-NEXT-T-AVG-ADAPTER`: build an exact adapter from an averaged prime-distribution theorem (BV/BDH/Kai-type input or a new average theorem) to the T super-Kai residue family with a chargeable exceptional set; do not promote an average theorem pointwise without this adapter.
3. `R401-NEXT-WALL-STRUCTURE`: new structural attack intrinsic to `theta=1/4`, exploiting common-core/root-line/reduced-column coupling or another independent equation on the fully balanced four-coefficient wall.

These are exploration candidates, not proved routes or theorem claims.

## Lifecycle verdict

PASS is an intermediate acceptance of r401a only. It does not close Stage27 checkpoint40, does not close the upper attack, and does not authorize checkpoint50.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
R401A_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
OFF_WALL_FIXED_POWER_SAVING_ACCEPTED=true
OFF_WALL_EXPONENT=1/2-2gamma+o(1)
CRITICAL_WALL_PRIOR_ART_ACCEPTED=true
CRITICAL_WALL_NEW_DISCOVERY=false
MAIN_TERMINAL_GATE_TRACE_ACCEPTED=true
T_TERMINAL_GATE_TRACE_ACCEPTED=true
S_TERMINAL_GATE_TRACE_ACCEPTED=true
POST_STAGE14_COMPATIBLE_FIXED_POWER_INPUT_FOUND=false
ABSOLUTE_REPO_NATIVE_EXHAUSTIVENESS_PROVED=false
NO_CURRENTLY_IDENTIFIED_COMPATIBLE_REPO_NATIVE_FIXED_POWER_ROUTE=true
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_UPPER_CANDIDATES=R401-NEXT-MAIN-CRT2,R401-NEXT-T-AVG-ADAPTER,R401-NEXT-WALL-STRUCTURE
NEXT_EXPECTED_COMMAND=merge PR #1026; then Stage27-main-batch with checkpoint40 upper exploration retained
```
