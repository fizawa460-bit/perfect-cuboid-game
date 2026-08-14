# Stage23-70 aggressive-search ledger

STATUS=CANDIDATE_PENDING_FRESH_AUDIT
STAGE=Stage23
TRANSITION=Stage17 -> Stage19
PURPOSE=freeze all aggressive upper/lower attacks before closeout

## 1. Contract

Source population `N1(B)` is primitive canonical exactly-one-face cuboids with integral space diagonal `d=R<=B`. Target population `N2(B)` is the matching primitive canonical exactly-two-face stratum with the same integral space diagonal and cutoff. The ratio is a matched adjacent-stratum population-size ratio, not literal objectwise survival.

## 2. Frozen quantitative facts

- `N1(B) ~ kappa/(24*pi) * B(log B)^3`, `kappa>0`.
- `N2(B) <<_epsilon B^(1/2+epsilon)`.
- Therefore `N2(B)/N1(B) <<_epsilon B^(-1/2+epsilon)/(log B)^3 -> 0`.
- Exact census plus monotonicity gives only the constant lower floor `N2(B)>=3495` for `B>=500000000`.
- `N2(B)->infinity` is not proved.
- No positive-power lower bound is proved.
- No matching half-power lower bound is proved.
- The true polynomial exponent of `N2(B)` is not identified.
- Whether the half-power upper scale is intrinsic is unresolved.

## 3. Stage23 attack chronology

### Checkpoint20: Stage17-family slicing

The AR-039 Stage17 infinite family was attacked from the source side rather than rebuilding the Stage14/15 target-first parametrization. The second-face conditions reduce to higher-genus square-value problems. The initial finite scan found no hits and was retained only as diagnostic evidence, never as a death proof.

### Checkpoint30/40: consecutive slice and Q03 repair

For the consecutive AR-039 slice `n=t, m=t+1`, one candidate second-face equation becomes

`w^2=(t^2+1)(t^2+2t+2)`.

A later deep repair replaced an incorrect rational-basepoint statement by the exact global congruence obstruction: for every integer `t`, the right side is `2 mod 8`, hence never a square. This selected slice is globally empty.

Q03 is therefore exhausted for this slice by a genuine local obstruction, not by finite search.

### Checkpoint40: Q06 transverse Kummer/Jacobi boundary

The Q06 moving-family receiver was pushed to the explicit physical-height boundary. The physical height is the Stage19 space diagonal itself. No transferred point-count theorem was found that simultaneously preserves the literal Stage19 population, physical height and multiplicity while beating the inherited `B^(1/2+epsilon)` exponent. No optimality claim was made.

### Checkpoint50: fresh Stage19 surgeon search

Four fresh candidates F50-S1 through F50-S4 were generated from the Stage17 Pythagorean-chain interface before reserve routes were reconsidered. The search produced synchronized two-level square-value receivers including

`Q^2=u^8+14u^4v^4+v^8`,
`W^2=2(u^4+v^4)`.

Other candidates were eliminated by positivity, primitive homothety collapse, or local/high-degree square-value gates. No fresh candidate proved target unboundedness, a positive-power lower bound, a stronger upper bound, or a matching half-power lower bound.

The near-diagonal `d~v^4` scale was explicitly corrected: mere infinitude of survivors would not imply a `B^(1/4)` lower bound without a quantitative density statement for the surviving parameters.

### Checkpoint60: old-dead-branch revalidation

Eight high-value Stage14/15 attack clusters were reopened at source level and retested against the literal Stage19 contract: Q01, Q03, Q04, Q05, Q07, Q08, Q09, Q10.

Verdicts:

- Q01: `DEAD_CONFIRMED_GLOBAL_MOD16` for the canonical Stage15-2 explicit linear ambient family.
- Q03: `DEAD_CONFIRMED_SELMER_ONLY` as an independent lower-bound certificate.
- Q04: `DEAD_CONFIRMED_AS_INDEPENDENT_ROUTE`; absorbed by the sharper moving-family boundary.
- Q05: `NEEDS_NEW_INPUT`.
- Q07: `NEEDS_NEW_INPUT`.
- Q08: `DEAD_REASON_WEAKENED`.
- Q09: `NEEDS_NEW_INPUT`.
- Q10: `DEAD_CONFIRMED_CURRENT_CHARACTER_INPUTS` only at the current theorem/adapter boundary.

No `REVIVED_LIVE` branch was found at current input.

## 4. Strongest fresh obstruction promoted from revalidation

The Stage15-2 canonical explicit exactly-two family is

`e=4pq`, `x=4p^2-q^2`, `y=4q^2-p^2`

for coprime odd `p,q` in its injective cone, with

`R^2=e^2+x^2+y^2=17(p^4+q^4)`.

Stage19 would require `R` integral. For odd `p,q`,

`p^4=q^4=1 mod 16`,

hence

`17(p^4+q^4)=2 mod 16`.

Square residues modulo 16 are `0,1,4,9`, so this entire linear-size ambient exactly-two family has zero Stage19 survivors.

This is a family-specific global obstruction. It does not imply that all exactly-two ambient families fail to lift to Stage19.

## 5. What aggressive search did not establish

```text
TARGET_UNBOUNDEDNESS_PROVED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
HALF_POWER_OPTIMALITY_CLAIMED=false
PERFECT_CUBOID_EXISTENCE_CONCLUSION=NONE
PERFECT_CUBOID_NONEXISTENCE_CONCLUSION=NONE
FINITE_ZERO_HIT_USED_AS_PROOF=false
```

## 6. Closeout role

The aggressive policy is considered executed for Stage23 because the stage did not stop at the inherited upper bound: it generated new source-specific families, proved a global mod-8 slice obstruction, pushed the moving Kummer/Jacobi boundary, generated four fresh Stage19 surgeon candidates, and source-revalidated eight older routes with lower-bound relevance prioritized.

The unresolved lower-bound questions are therefore frozen as open problems, not silently converted into negative theorems.

```text
AGGRESSIVE_SEARCH_LEDGER_REQUIRED=true
AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true
LOWER_BOUND_ATTACK_REQUIRED=true
LOWER_BOUND_ATTACK_EXECUTED=true
EXPLICIT_UNBOUNDED_FAMILY_SEARCH_EXECUTED=true
POSITIVE_POWER_LOWER_BOUND_SEARCH_EXECUTED=true
STOP_ON_EXISTING_UPPER_BOUND_ONLY=false
CLOSEOUT_WITH_OPEN_LOWER_BOUND_GATE=true
```
