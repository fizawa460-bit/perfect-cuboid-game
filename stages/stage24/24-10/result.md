# Stage24-10 — literal Stage18 to Stage19 transition contract

EVIDENCE_LEVEL=PROVED_INTERFACE_ADAPTER
CHECKPOINT=10
STATUS=SUBMITTED_FOR_FRESH_AUDIT
EXPLORATION_PHASE=FULL_TRANSITION_RESEARCH
FORMULA_SUBSTITUTION_ONLY=false

## 1. Transition owned by Stage24

Stage24 studies

```text
Stage18 -> Stage19
exactly two integral faces
  + integral space diagonal
```

under the common physical cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B.
\]

Let

\[
\mathcal B_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly two face diagonals integral}\},
\]

and

\[
M_2(B)=\#\mathcal B_2(B).
\]

Define

\[
\mathcal A_2(B)=\{(a,b,c)\in\mathcal B_2(B):R\in\mathbf Z\},
\qquad N_2(B)=\#\mathcal A_2(B).
\]

Therefore the transition is literally

\[
\boxed{\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\}}.
\]

Unlike Stage22/23 adjacent-stratum comparisons, `N2(B)/M2(B)` is a genuine objectwise survivor ratio on one fixed source population.

## 2. Exact adapter audit

Stage18 and Stage19 both use:

- strict canonical ordering `0<a<b<c`;
- primitivity `gcd(a,b,c)=1`;
- physical-object multiplicity one;
- exactly two, not at least two, integral face diagonals;
- the exact same geometric cutoff `R<=B`.

On Stage19 objects the positive integral space diagonal is exactly `d=R`, so no `d` versus `R` height conversion occurs.

```text
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
COMPARISON_ADAPTER_REQUIRED=false
LITERAL_SUBSET_TRANSITION=true
```

## 3. Frozen source and target interfaces

The audited Stage18 source law is

\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5},\qquad C_{M_2}>0.
\]

Stage19 supplies the current certified target information

\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}},
\]

and the exact finite lower floor

\[
\boxed{N_2(B)\ge3495\qquad(B\ge500,000,000)}.
\]

The following remain open and are explicitly owned by later Stage24 attack checkpoints rather than silently inherited as settled:

```text
STAGE19_UNBOUNDEDNESS_PROVED=false
STAGE19_POSITIVE_POWER_LOWER_BOUND_PROVED=false
STAGE19_MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
STRICT_SUB_SQRT_UPPER_PROVED=false
```

Checkpoint10 records these interfaces but does not close checkpoint30/40/50 by quotienting or repeating them.

## 4. Exact new arithmetic predicate

Use the positive shared-edge toric coordinates inherited from the Stage15/19 interface. With

\[
A=m^2r^2+n^2s^2,
\qquad
B=m^2s^2+n^2r^2,
\]

the physical identity gives

\[
G^2R^2=4AB.
\]

The frozen primitive divisibility adapter proves the exact equivalence

\[
\boxed{R\in\mathbf Z\iff AB\in\mathbf Z^2\iff\operatorname{sf}(A)=\operatorname{sf}(B)}.
\]

Thus Stage24's new condition is a paired Gaussian-norm squareclass coincidence imposed on the Stage18 double-Pythagorean host. This is an exact predicate, not an independence heuristic.

## 5. Interaction question deliberately left open at checkpoint10

Stage16S proves that imposing an integral space diagonal on the unrestricted primitive/canonical ambient population intrinsically costs one polynomial power:

\[
N_S^{all}(B)/U(B)\asymp B^{-1}.
\]

Stage24 must determine whether the same condition, after two integral faces are already imposed, is:

- approximately independent of the two-face structure;
- enhanced by the two-face arithmetic;
- suppressed by it;
- or governed by a new correlated squareclass/valuation mechanism.

The current Stage19 half-power upper theorem does not answer that question by itself. In particular, an upper bound for `N2` cannot be promoted to the true survivor scale without a matching lower theorem.

## 6. Required comparison lattice

Later Stage24 checkpoints must compare:

1. Stage16S ambient `+space` baseline;
2. Stage21 `one face -> one face + space` once its relevant audit state is certified;
3. Stage22 `one face -> two faces` without space;
4. Stage23 `one face + space -> two faces + space` at audited scope;
5. Stage24 `two faces -> two faces + space` itself.

Matching polynomial exponents alone will not be treated as probabilistic independence. Common constraints and already-charged mechanisms must be audited before any interaction classification.

## 7. Exploration commitments

The checkpoint10 discovery ledger is materialized at

`stages/stage24/24-10/discovery-ledger.md`.

The controller fixes the following future order:

```text
CP40: FRESH_STAGE19_UPPER_SURGEON_FIRST
CP50: FRESH_STAGE19_LOWER_SURGEON_FIRST
CP50: EXPLICIT_UNBOUNDED_FAMILY_SEARCH_REQUIRED
CP50: POSITIVE_POWER_LOWER_BOUND_SEARCH_REQUIRED
CP50: NEW_CANDIDATE_GENERATION_REQUIRED_BEFORE_NEGATIVE_RESULT
CP50: MIN_FRESH_CANDIDATES_IF_NO_BREAKTHROUGH=4
CP50: OLD_DEAD_BRANCH_REVALIDATION_REQUIRED_IF_NEGATIVE
CP60: INTRINSIC_AND_ALTERNATE_PATH_COMPARISON_REQUIRED
CP60: INDEPENDENCE_CORRELATION_CLASSIFICATION_REQUIRED
```

Finite zero-hit evidence cannot certify death, and later stronger results or corrections must be back-propagated to the earliest relevant history entry by supersession/addendum or source repair as appropriate.

## 8. Checkpoint10 exit

```text
TRANSITION=Stage18->Stage19
SOURCE_POPULATION=primitive canonical exactly-two integral faces under R<=B
TARGET_POPULATION=source plus R integral
SOURCE_COUNT=M2(B)
TARGET_COUNT=N2(B)
LITERAL_SUBSET_TRANSITION=true
COMMON_CUTOFF=R<=B
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
SOURCE_INTERFACE_UPGRADE_CHECK=PASS_AT_CURRENT_FROZEN_INTERFACE
TARGET_INTERFACE_UPGRADE_CHECK=PASS_AT_CURRENT_FROZEN_INTERFACE
STRUCTURAL_SIGNATURE_SEARCH=PASS
DEPENDENCY_NEIGHBOR_SEARCH=PASS
DISCOVERY_LEDGER_STATUS=COMPLETE
UPSTREAM_PREMISE_CHECK=PASS
RETURN_TO_SOURCE_REQUIRED=false
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=10
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage24-audit
CODEX_REQUIRED=false
```
