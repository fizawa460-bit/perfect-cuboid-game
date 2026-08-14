# Stage23-70 — bounded maximal synthesis and closeout

EVIDENCE_LEVEL=PROVED_TRANSITION_PLUS_AUDITED_ATTACK_BOUNDARY
CHECKPOINT=70
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Population contract

Stage23 compares the disjoint adjacent strata under one identical physical contract:

- primitive canonical `0<a<b<c`, `gcd(a,b,c)=1`;
- integral space diagonal `d=R=sqrt(a^2+b^2+c^2)`;
- common cutoff `R=d<=B`;
- source `N1(B)`: exactly one integral face diagonal;
- target `N2(B)`: exactly two integral face diagonals.

The ratio `N2/N1` is a matched population-size ratio, not literal objectwise survival.

## 2. Frozen transition theorem

The audited Stage17 source law is

`N1(B) ~ kappa/(24*pi) * B(log B)^3`, `kappa>0`.

The audited Stage19 target theorem is

`N2(B) <<_epsilon B^(1/2+epsilon)`.

Therefore

`N2(B)/N1(B) <<_epsilon B^(-1/2+epsilon)/(log B)^3 -> 0`.

Hence

```text
STAGE23_ZERO_DENSITY_TRANSITION_PROVED=true
RATIO_LIMIT=0
```

No matching target asymptotic is known, so no sharp ratio scale or leading constant is claimed.

## 3. Causal synthesis accepted at checkpoint60

Stage17 already contains an integral face and an integral space diagonal. In oriented coordinates its source structure is

`x^2+y^2=p^2`,
`p^2+z^2=d^2`.

Entering Stage19 adds one second-face cross-leg condition

`x^2+z^2=q^2`

or

`y^2+z^2=q^2`.

The frozen Stage13/Stage17 pair-overlap theorem gives

`P(B)=o(B(log B)^3)`

for the relevant pair-overlap loci inside the same already-space-integral host, and every Stage19 target lies in such a locus. Thus

`N2(B)<=P(B)=o(B(log B)^3)`

and the source asymptotic gives `N2/N1->0` directly.

This is the certified qualitative causal explanation. It does not derive the stronger half-power target bound. The half-power exponent remains inherited from Stage19 and its intrinsic status is unresolved.

## 4. What is not double-charged

Integral space diagonal is already present in Stage17 and cannot be counted again as a Stage23 transition cost. Canonicalization, primitivity, common cutoff and physical-object multiplicity are shared interfaces. Stage22's free-complementary-edge causal description also does not transfer literally, because the Stage17 complementary edge already participates in `p^2+z^2=d^2`.

```text
SPACE_SQUARECLASS_DOUBLE_CHARGE=false
COMMON_INTERFACE_DOUBLE_CHARGE=false
STAGE22_FREE_EDGE_CAUSE_TRANSFERS_LITERALLY=false
```

## 5. Aggressive lower-bound and exponent search

Stage23 explicitly did not stop at the inherited upper bound. The required aggressive-search ledger is materialized at

`stages/stage23/23-70/aggressive-search-ledger.md`.

The search executed:

- Stage17-family slicing and higher-genus square-value reductions;
- a consecutive source slice with a proved global mod-8 exclusion;
- deep Q06 moving Kummer/Jacobi physical-height analysis;
- four fresh Stage19 surgeon candidates F50-S1 through F50-S4;
- eight source-level revalidations of old Stage14/15 routes before checkpoint60 synthesis.

The strongest fresh revalidation result is the Stage15-2 ambient-family obstruction. For its canonical explicit linear exactly-two family,

`R^2=17(p^4+q^4)`

with odd `p,q`, so `R^2=2 mod16`, impossible for a square. The entire family has zero Stage19 space-integral survivors. This is global for that family only.

No searched route proves Stage19 target unboundedness or a positive-power lower bound.

## 6. Frozen lower-bound frontier

The exact census gives

`N2(500000000)=3495`.

By cutoff monotonicity,

`N2(B)>=3495` for `B>=500000000`.

This is the strongest certified lower statement frozen by Stage23.

```text
TARGET_UNBOUNDEDNESS_PROVED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
HALF_POWER_OPTIMALITY_CLAIMED=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
```

## 7. Mandatory closeout decisions

### 7.1 Self-contained bundle

The Stage23 result has a reusable population contract, zero-density theorem, source-host causal interpretation, explicit double-charge firewalls, family-obstruction diagnostics, and a nontrivial open lower-bound frontier. Reuse would otherwise require reconstructing Stages17/19 and the Stage23 attack history.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_DECISION=YES
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
SELF_CONTAINED_BUNDLE_PATH=stages/stage23/23-70/self-contained-bundle.md
```

### 7.2 Arsenal promotion

The matched Stage17 -> Stage19 transition law is reusable, especially its exact contract and its warning that space integrality is already paid in the source. The Stage15-2 mod-16 family obstruction is also reusable as a lower-family filter.

```text
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_DECISION=YES
ARSENAL_PROMOTION_MATERIALIZED=true
ARSENAL_PROMOTION_PATH=docs/stage23-arsenal-promotion.md
NEW_STANDALONE_ANALYTIC_THEOREM_PROMOTED=false
```

The arsenal artifact packages audited Stage23 interfaces; it does not claim a new external counting theorem.

### 7.3 Aggressive-search ledger

```text
AGGRESSIVE_SEARCH_LEDGER_REQUIRED=true
AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true
AGGRESSIVE_SEARCH_LEDGER_PATH=stages/stage23/23-70/aggressive-search-ledger.md
```

## 8. Final reusable ledger

```text
TRANSITION=Stage17 -> Stage19
SOURCE=exactly one integral face + integral space diagonal
TARGET=exactly two integral faces + integral space diagonal
COMMON_CUTOFF=R=d<=B
LITERAL_SUBSET_TRANSITION=false
SOURCE_ASYMPTOTIC=N1(B)~kappa/(24*pi)*B(log B)^3
TARGET_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
RATIO_UPPER=N2/N1<<_epsilon B^(-1/2+epsilon)/(log B)^3
RATIO_LIMIT=0
SOURCE_HOST_PAIR_OVERLAP=N2(B)<=P(B)=o(B(log B)^3)
STRONG_HALF_POWER_RATE_CAUSALLY_DERIVED_HERE=false
CERTIFIED_CONSTANT_LOWER_FLOOR=N2(B)>=3495_FOR_B>=500000000
TARGET_UNBOUNDEDNESS_PROVED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
STAGE15_2_AMBIENT_LINEAR_FAMILY_STAGE19_SURVIVORS=0_BY_MOD16
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_MATERIALIZED=true
AGGRESSIVE_SEARCH_LEDGER_REQUIRED=true
AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true
PERFECT_CUBOID_CONCLUSION=NONE
```

## 9. Exit

Stage23 mathematics is not reopened at checkpoint70. Fresh audit must verify the maximal synthesis, three required closeout artifacts/decisions, and that the unresolved lower-bound frontier is stated without overclaim.

```text
UPSTREAM_PREMISE_CHECK=PASS
DOUBLE_CHARGE_CHECK=PASS
NEW_COMPUTATION_REQUIRED=false
NEW_ANALYTIC_INPUT=false
MATHEMATICS_REOPEN_REQUIRED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage23-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CLOSE_STAGE_AFTER_AUDIT_PASS=true
CODEX_REQUIRED=false
```
