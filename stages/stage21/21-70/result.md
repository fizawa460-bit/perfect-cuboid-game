# Stage21-70 — bounded maximal synthesis / intrinsic status / closeout

EVIDENCE_LEVEL=PROVED_SYNTHESIS
CHECKPOINT=70
STATUS=SYNTHESIS_CANDIDATE_PENDING_FRESH_AUDIT

## Certified transition

Under the frozen primitive/canonical common cutoff, Stage21 compares Stage16 (exactly one integral face) to Stage17 (exactly one integral face plus integral space diagonal), with Stage16S as the ambient space-diagonal control.

The audited law is

\[
\frac{N_1(B)}{M_1(B)}\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

The ambient Stage16S comparison is

\[
\frac{N_S^{all}(B)}{U(B)}\sim \frac{9\zeta(3)}{8\pi G}\frac1B.
\]

Hence the space-diagonal condition has the same intrinsic polynomial cost `B^-1` in the ambient and one-face populations, but the one-face population is asymptotically enriched by an exact logarithmic factor `(log B)^2` relative to the ambient baseline.

Equivalently,

\[
\frac{N_1/M_1}{N_S^{all}/U}
\sim
\frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty.
\]

This proves that the space-diagonal condition is neither asymptotically independent of the pre-existing one-face condition nor subject to an additional polynomial penalty from it. The interaction is positive and logarithmic.

## Causal synthesis

The polynomial loss and logarithmic compensation are distinct layers.

1. `B^-1` is the intrinsic quadratic/Pythagorean space-diagonal cost already visible in Stage16S.
2. The target condition is exactly the nested shared-`P` system
   \[
   x^2+y^2=P^2,\qquad P^2+z^2=d^2.
   \]
3. AR-038 gives the exact shared-`P` representation convolution, so the target bulk is assembled from representation multiplicities rather than isolated examples.
4. Stage13 R07 proves the `B(log B)^3` target main term is carried by the full principal multiplicative sector of the outer `h,r,s` architecture; nonprincipal sectors are lower order.
5. Canonical directional geometry changes directional constants but cancels from the matched transition ratio.
6. Pair/triple overlap corrections are lower order and cannot create the main logarithmic enhancement.
7. The entire explicit AR-039 survivor family has size `Theta(B^(1/2))=o(N1)` and therefore cannot explain the bulk enhancement.

Thus the certified mechanism is

```text
INTRINSIC_SPACE_COST=B^-1
INTERACTION_COMPENSATION=(log B)^2
INTERACTION_SIGN=POSITIVE
INTERACTION_LOCATION=bulk multiplicative shared-P nested-Pythagorean principal sector
```

The remaining fine question is not whether the enhancement exists or where its bulk architecture lives, but whether the two net logarithms admit a canonical decomposition into individually named pole slots or local factors. The current repository does not prove such a decomposition.

## Additional deductions

### A. Polynomial exponent is intrinsic

Checkpoint30 gives a sharp asymptotic, not merely an upper bound. Therefore the exponent `-1` in the Stage16 -> Stage17 survival ratio is the true polynomial exponent. The `(log B)^2` term is a slowly varying compensation and does not change that intrinsic polynomial classification.

### B. One-face conditioning helps survival relative to ambient

Since the enhancement ratio tends to infinity, a cuboid drawn from the one-face population is asymptotically more likely, by an unbounded logarithmic factor, to have integral space diagonal than an ambient primitive/canonical cuboid. This is a conditional population statement, not stochastic independence of arithmetic events.

### C. No direction-specific interaction at leading order

The same leading conditional constant occurs for `q=ab,ac,bc`. Therefore the Stage13 real chamber bias controls how one-face objects distribute among directions, but the additional space-diagonal thinning does not introduce a new leading directional preference.

### D. Known thin constructions are witnesses, not population models

AR-039 proves explicit infinite survival but contributes zero asymptotic proportion even inside the Stage17 target. Future explicit families should therefore not be treated as explanations of the transition law without a matched population-scale lower bound.

### E. Stage21 supplies a reusable control template

The useful comparison pattern is: isolate an ambient intrinsic condition cost with a control population, then compare the same condition after prior arithmetic conditioning. This separates polynomial intrinsic cost from interaction enhancement/suppression and guards against double charging. This method is directly relevant to Stage24 and the Stage28 interaction synthesis.

## Lower-stage reinterpretations

No lower stage is reopened. Stage16S is reinterpreted as proving the intrinsic `B^-1` space cost. Stage17's `B(log B)^3` law is reinterpreted, relative to Stage16, as intrinsic `B^-1` thinning plus positive `(log B)^2` arithmetic compensation. Stage13's principal-sector theorem supplies the bulk location of that compensation but its theorem is unchanged. Stage11 AR-038/039 retain their original contracts; Stage21 only classifies their roles in the transition.

## Refinement candidates

The following are legitimate future refinements but are outside bounded Stage21 closeout:

- canonical map from the Stage13 five principal pole slots to the two net logarithms relative to Stage16;
- a local-factor decomposition proving or disproving any independent-factor interpretation;
- analogous ambient-control comparisons for later transitions, especially Stage18 -> Stage19;
- a general interaction coefficient formalism for Stage28.

Each would require new theorem work or a broader synthesis and therefore is not required for Stage21 closure.

## New heuristics

No new heuristic is promoted as a Stage21 result. In particular, no stochastic independence, independent local-probability product, or two-independent-log-factor model is asserted.

## Open gates

```text
OPEN_GATE=LOG_SQUARED_FINE_POLE_OR_LOCAL_FACTOR_DECOMPOSITION_UNRESOLVED
OPEN_GATE_BLOCKS_TRANSITION_LAW=false
OPEN_GATE_BLOCKS_INTRINSIC_POLYNOMIAL_STATUS=false
OPEN_GATE_BLOCKS_CAUSAL_LOCALIZATION=false
```

## Stage-end artifact decisions

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage21 combines Stage16, Stage16S, Stage17, Stage13 and Stage11 into a subtle reusable transition theorem whose intrinsic-vs-interaction distinction is unsafe to reconstruct from scattered files.
ARSENAL_PROMOTION_REQUIRED=YES
ARSENAL_CANDIDATES=Stage21 ambient-control interaction adapter; Stage21 one-face-to-space transition law
```

Proposed arsenal contracts after fresh audit:

```text
NAME=ambient-control interaction adapter
TYPE=method
SOURCE_STAGE=Stage21
ASSUMPTIONS=compatible primitive/canonical populations and common cutoff; audited ambient control for the added condition
VALID_RANGE=population-transition comparisons satisfying the assumptions
WHAT_IT_DOES=separates intrinsic condition cost from interaction enhancement/suppression after prior conditioning
WHAT_IT_DOES_NOT_DO=does not imply probabilistic independence or factorization of arithmetic events
POTENTIAL_RECEIVERS=Stage24,Stage25,Stage28
AUDIT_STATUS=PENDING_STAGE21_70_AUDIT
```

```text
NAME=one-face to space-diagonal transition law
TYPE=theorem
SOURCE_STAGE=Stage21
ASSUMPTIONS=Stage16/17 frozen primitive canonical contract and common cutoff R<=B with target d=R
VALID_RANGE=B->infinity
WHAT_IT_DOES=proves N1/M1~(kappa*pi/18)(log B)^2/B and identifies B^-1 as intrinsic space cost with positive logarithmic interaction compensation
WHAT_IT_DOES_NOT_DO=does not canonically assign the two logarithms to independent pole slots/local factors and does not address later two-face or Euler populations
POTENTIAL_RECEIVERS=Stage24,Stage25,Stage28,perfect-cuboid endpoint planning
AUDIT_STATUS=PENDING_STAGE21_70_AUDIT
```

## Required policy fields

```text
KNOWN_RESULTS=exact transition asymptotic; ambient B^-1 control; sharp intrinsic polynomial exponent; AR039 negligible; bulk principal-sector localization
ADDITIONAL_DEDUCTIONS=positive logarithmic interaction; no leading directional interaction; explicit-family witness/model distinction; reusable ambient-control comparison method
CAUSAL_SYNTHESIS=intrinsic B^-1 space cost plus (log B)^2 compensation localized to shared-P multiplicative principal bulk
LOWER_STAGE_REINTERPRETATIONS=Stage16S intrinsic-cost control; Stage17 interaction-enriched target; Stage13 principal-sector mechanism source; no reopening
REFINEMENT_CANDIDATES=fine pole/local-factor decomposition; later ambient controls; Stage28 interaction coefficient formalism
NEW_HEURISTICS=NONE_PROMOTED
OPEN_GATES=LOG_SQUARED_FINE_POLE_OR_LOCAL_FACTOR_DECOMPOSITION_UNRESOLVED
NEXT_STAGE_QUESTIONS=Stage22 second-face thinning; preserve Stage21 ambient-control method for Stage24/28
SYNTHESIS_STOP_REASON=further refinement requires a new theorem or broader cross-stage interaction program
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

## Closeout candidate

```text
STAGE21_70=BOUNDED_MAXIMAL_SYNTHESIS_COMPLETE_PENDING_FRESH_AUDIT
TRUE_POLYNOMIAL_EXPONENT_IDENTIFIED=true
INTRINSIC_SPACE_DIAGONAL_COST=B^-1
PRIOR_ONE_FACE_INTERACTION=POSITIVE_LOG_SQUARED_ENHANCEMENT
INDEPENDENT_OF_PRIOR_CONDITIONS=false
DOUBLE_CHARGE_CHECK=PASS
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=
NEXT_STAGE=Stage22
NEXT_EXPECTED_COMMAND=Stage21-audit
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
