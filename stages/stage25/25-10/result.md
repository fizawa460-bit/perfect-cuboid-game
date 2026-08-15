# Stage25-10 — Stage16 to Stage19 combined-transition contract

EVIDENCE_LEVEL=PROVED_INTERFACE_ADAPTER
CHECKPOINT=10
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
EXPLORATION_PHASE=FULL_TRANSITION_RESEARCH
FORMULA_SUBSTITUTION_ONLY=false

## 1. Transition owned by Stage25

Stage25 studies the combined population change

```text
Stage16 -> Stage19
exactly one integral face, no space requirement
  -> exactly two integral faces + integral space diagonal
```

under the common physical cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B.
\]

Define

\[
\mathcal B_1(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly one face diagonal integral}\},
\]
\[
M_1(B)=\#\mathcal B_1(B),
\]

and

\[
\mathcal A_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly two face diagonals integral},\ R\in\mathbf Z\},
\]
\[
N_2(B)=\#\mathcal A_2(B).
\]

The source and target are **not** a literal subset pair: the exactly-one and exactly-two face masks are disjoint. Therefore

\[
\boxed{N_2(B)/M_1(B)}
\]

is a matched population-size ratio measuring the combined thinning scale across two added conditions, not an objectwise survival probability.

```text
LITERAL_SUBSET_TRANSITION=false
RATIO_SEMANTICS=MATCHED_COMBINED_POPULATION_SIZE_RATIO
OBJECTWISE_SURVIVAL_INTERPRETATION=false
```

## 2. Population/cutoff/multiplicity adapter

Stage16 and Stage19 use the same physical conventions:

- strict canonical ordering `0<a<b<c`;
- global primitivity `gcd(a,b,c)=1`;
- one count per physical canonical object;
- Euclidean physical cutoff `R<=B`.

On Stage19 objects the positive integral space diagonal is `d=R` exactly. No height conversion occurs.

The only intended change is the face mask plus the space-integrality predicate. Hence the two endpoint counts are directly comparable as population sizes under the same cutoff, although not as a literal subset.

```text
POPULATION_CONTRACT_CHANGED=NO
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
COMPARISON_ADAPTER_REQUIRED=NO
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

## 3. Strongest frozen endpoint interfaces

### Source — Stage16 / audited Stage21 upgrade

The strongest audited exact-one/no-space source interface imported by Stage21 is

\[
\boxed{M_1(B)\sim\frac{3}{4\pi^2}B^2\log B}.
\]

This is stronger than the older Stage16 order statement `M1(B) asymp B^2 log B` and matches the Stage25 source population literally.

### Target — Stage19 after audited Stage24 supersession

The current consumer-facing Stage19 interface is

\[
\boxed{N_2(B)\gg\sqrt{\log B}},
\qquad
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

Thus Stage19 is now known to be unbounded and to contain an infinite primitive canonical exactly-two-plus-space family, while all of the following remain open:

```text
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
```

Checkpoint10 freezes these endpoint interfaces but deliberately does **not** promote their quotient to the Stage25 checkpoint30 theorem.

## 4. Two exact comparison paths

Stage25 has two audited intermediate factorizations.

### Path A — second face first, then space

\[
M_1\xrightarrow{\text{Stage22}}M_2\xrightarrow{\text{Stage24}}N_2.
\]

Frozen interfaces:

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
\frac{M_2(B)}{M_1(B)}
\sim \frac{4\pi^2C_{M_2}}{3}\frac{(\log B)^4}{B},
\]

and Stage24 proves

\[
B^{-1}(\log B)^{-9/2}
\ll \frac{N_2(B)}{M_2(B)}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

### Path B — space first, then second face

\[
M_1\xrightarrow{\text{Stage21}}N_1\xrightarrow{\text{Stage23}}N_2.
\]

Frozen interfaces:

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\qquad \kappa>0,
\]

\[
\frac{N_1(B)}{M_1(B)}
\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B},
\]

and the audited post-Stage24 Stage23 strengthening gives

\[
B^{-1}(\log B)^{-5/2}
\ll \frac{N_2(B)}{N_1(B)}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

For every `B` with nonzero intermediate counts the identities

\[
\boxed{
\frac{N_2}{M_1}
=
\frac{M_2}{M_1}\frac{N_2}{M_2}
=
\frac{N_1}{M_1}\frac{N_2}{N_1}
}
\]

are exact algebraic count-ratio identities. They do **not** assert probabilistic independence and do not turn the non-subset horizontal comparisons into objectwise conditional probabilities.

Checkpoint30 must derive and audit the combined ratio law independently/directly and then verify both path factorizations agree at the certified level.

## 5. Mechanism map frozen at entry

Path A:

1. Stage22: a second Pythagorean face couples the previously freer complementary edge and costs the sharp scale `(log B)^4/B` in the one-face host;
2. Stage24: space integrality on the two-face toric host is a genuine new squareclass/space-square condition; its target is `THIN_BUT_INFINITE`, but the global interaction sign relative to ambient space cost remains unresolved.

Path B:

1. Stage21: space integrality has intrinsic polynomial cost `B^-1` but one-face conditioning produces a positive `(log B)^2` enhancement;
2. Stage23: the second face is an additional cross-leg Pythagorean compatibility inside an already-space-integral chain; the transition is zero-density with infinite target.

Stage25 must determine what can be attributed to each mechanism **without multiplying logically independent-looking savings merely because two proofs exist**.

```text
DOUBLE_CHARGE_CHECK_REQUIRED=true
PATH_FACTOR_PRODUCT_IS_ALGEBRAIC_IDENTITY=true
PATH_FACTOR_PRODUCT_IS_INDEPENDENCE_CLAIM=false
STAGE24_LOCAL_SIEVE_SAVING_MULTIPLIED_SEPARATELY=false
STAGE24_THIN_COVER_SAVING_MULTIPLIED_SEPARATELY=false
```

## 6. Interaction question owned by Stage25

Stage24 left the second-order comparison

\[
\mathcal I(B)
=
\frac{N_2/M_2}{N_1/M_1}
=
\frac{N_2/N_1}{M_2/M_1}
\]

with sign relative to `1` unresolved. Stage25 must consume that result rather than silently treating the two added conditions as independent.

The combined endpoint ratio may be sharply classifiable even while the internal allocation of cost between the two conditions is not. Stage25 therefore separates total combined thinning, pathwise decomposition, interaction sign/order sensitivity, and mechanism attribution.

## 7. Numerical reuse preflight

The mandatory Stage14 numerical reuse index was inspected before any new computation.

- `NUM-R01` matches the Stage25 target after selecting the exactly-two face mask from the integral-space census;
- `NUM-R06` and `NUM-R07` are retained only as exact/derived intermediate-path diagnostics and are not a direct Stage25 denominator oracle;
- no large new computation is justified at checkpoint10.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R06,NUM-R07
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_TARGET_ORACLE_PLUS_INTERMEDIATE_PATH_DIAGNOSTICS
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10
```

The exact adapter is: `NUM-R01` -> select canonical primitive records with exactly two integral face diagonals, preserving `d=R<=B`, giving the Stage19 target `N2`. `NUM-R06/R07` are not used as direct evidence for `M1`; they are reserved for path/intersection diagnostics at checkpoint20/60.

## 8. Repository-wide reuse / discovery handoff

The checkpoint10 repair executed the normative repository-wide reuse preflight, including the Stage14/15 824-record attack map and curated deep-review queue. The concrete accepted/rejected candidate ledger and exact population adapters are in `25-10/discovery-ledger.md`.

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=Stage21-final;Stage22-controller;Stage23-post-Stage24-R01;Stage24-final;Stage19-post-Stage24-50-supersession;NUM-R01/R06/R07;PR#967,#977,#978,#979
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10_CONTRACT_FREEZE
DISCOVERY_CHECKPOINT=Stage25-10
SEARCHED_PATHS=RECORDED_IN_DISCOVERY_LEDGER
CANDIDATES_FOUND=RECORDED_IN_DISCOVERY_LEDGER
CANDIDATES_ACCEPTED=RECORDED_IN_DISCOVERY_LEDGER
CANDIDATES_REJECTED_WITH_REASON=RECORDED_IN_DISCOVERY_LEDGER
POPULATION_ADAPTERS_PROVED=RECORDED_IN_DISCOVERY_LEDGER
DISCOVERY_LEDGER_STATUS=COMPLETE
```

The Stage14/15 deep-review queue was used as a negative/supersession filter. In particular, Q05/Q06 remain future uniformity/support gates, Q07-Q10 are exhausted internal routes absent materially new input, and Q11 is qualitative zero density only; none supersedes the current audited Stage24 target interfaces at checkpoint10.

## 9. Required later-stage exploration

```text
CP20=BUILD_MATCHED_M1_N2_FINITE_BASELINE_BY_REUSE_FIRST
CP20=NO_NEW_LARGE_CENSUS_UNLESS_EXISTING_SOURCE_TARGET_GRIDS_CANNOT_BE_MATCHED
CP30=DIRECT_COMBINED_RATIO_AND_TWO_PATH_CONSISTENCY_REQUIRED
CP40=UPPER_BOUND_PROVENANCE_AND_NO_FAKE_PRODUCT_SAVING_REQUIRED
CP50=LOWER_BOUND_CONSTRUCTION_LEDGER_REUSE_C17_FIRST_AND_SEARCH_STAGE25_SPECIFIC_UPGRADES
CP60=FULL_TWO_PATH_CAUSAL_DECOMPOSITION_AND_DOUBLE_CHARGE_AUDIT_REQUIRED
CP60=ORDER_OF_CONDITIONS_INTERACTION_CLASSIFICATION_REQUIRED
CP70=BOUNDED_MAXIMAL_SYNTHESIS
```

## 10. Repair boundary

The first checkpoint10 audit accepted the mathematics and failed only the mandatory reuse/discovery evidence and controller taxonomy. This repair therefore does not change any theorem, ratio, count, or endpoint definition.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
MATHEMATICS_CONTRACT_ACCEPTED=true
COUNTS_RECOMPUTE_REQUIRED=false
MATHEMATICS_REOPEN_REQUIRED=false
PARENT_CLASS_NORMALIZED_TO=transition
REPAIR_SCOPE=REUSE_DISCOVERY_EVIDENCE_AND_CONTROLLER_TAXONOMY_ONLY
```

## 11. Checkpoint10 exit

```text
TRANSITION=Stage16->Stage19
SOURCE_COUNT=M1(B)
TARGET_COUNT=N2(B)
COMMON_CUTOFF=R<=B
LITERAL_SUBSET_TRANSITION=false
RATIO_SEMANTICS=MATCHED_COMBINED_POPULATION_SIZE_RATIO
SOURCE_INTERFACE=M1(B)~3/(4*pi^2) B^2 log B
TARGET_LOWER_INTERFACE=N2(B)>>sqrt(log B)
TARGET_UPPER_INTERFACE=N2(B)<<_epsilon B^(1/2+epsilon)
PATH_A=Stage22_then_Stage24
PATH_B=Stage21_then_Stage23
PATH_IDENTITIES_FROZEN=true
INTERACTION_SIGN_CURRENTLY_UNRESOLVED=true
DOUBLE_CHARGE_CHECK_REQUIRED=true
SOURCE_INTERFACE_UPGRADE_CHECK=PASS
TARGET_INTERFACE_UPGRADE_CHECK=PASS_WITH_STAGE24_50_SUPERSESSION
REPO_REUSE_PREFLIGHT=PASS
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
DISCOVERY_CHECKPOINT=Stage25-10
DISCOVERY_LEDGER_STATUS=COMPLETE
UPSTREAM_PREMISE_CHECK=PASS
RETURN_TO_SOURCE_REQUIRED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=10
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
CODEX_REQUIRED=false
```
