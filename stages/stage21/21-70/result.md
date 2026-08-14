# Stage21-70 — bounded maximal synthesis / intrinsic status / closeout

EVIDENCE_LEVEL=PROVED
CHECKPOINT=70
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT

## Certified transition

Under the frozen primitive/canonical common cutoff, Stage21 compares Stage16 exactly-one-face objects with Stage17 exactly-one-face plus integral-space-diagonal objects, using Stage16S as the ambient space-diagonal control.

\[
\frac{N_1(B)}{M_1(B)}\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Stage16S gives

\[
\frac{N_S^{all}(B)}{U(B)}\sim \frac{9\zeta(3)}{8\pi G}\frac1B.
\]

Therefore

\[
\frac{N_1/M_1}{N_S^{all}/U}\sim
\frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty.
\]

The intrinsic polynomial cost of the space-diagonal condition is `B^-1`, while prior one-face conditioning produces a positive logarithmic enhancement of exact order `(log B)^2`. Hence direct asymptotic independence is false, but there is no additional polynomial penalty.

## Causal synthesis

The target condition is the exact nested shared-`P` system

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2.
\]

AR-038 gives the exact shared-`P` representation convolution. Stage13 R07 proves that the `B(log B)^3` target main term is carried by the full principal multiplicative sector of the outer `h,r,s` architecture, while nonprincipal sectors lose at least one pole and are lower order. Directional chamber factors cancel from the matched transition ratio; pair/triple overlaps are lower order; and Stage21-50 proves the entire AR-039 family is `Theta(B^(1/2))=o(N1)`. Thus the net logarithmic enhancement is rigorously localized to the bulk multiplicative shared-`P` nested-Pythagorean principal sector.

The repository does not yet prove a canonical assignment of the two net logarithms to individually named pole slots or local factors. That remains the nonblocking open gate:

```text
OPEN_GATE=LOG_SQUARED_FINE_POLE_OR_LOCAL_FACTOR_DECOMPOSITION_UNRESOLVED
OPEN_GATE_BLOCKS_TRANSITION_LAW=false
OPEN_GATE_BLOCKS_INTRINSIC_POLYNOMIAL_STATUS=false
OPEN_GATE_BLOCKS_CAUSAL_LOCALIZATION=false
```

## Additional deductions

- The polynomial exponent `-1` is intrinsic and sharp because the transition has a full leading asymptotic.
- One-face conditioning increases space-diagonal survival relative to ambient by an unbounded logarithmic factor.
- The leading conditional constant is the same for `q=ab,ac,bc`, so there is no new leading direction-specific interaction.
- AR-039 is a valid explicit witness family but not a population model for the bulk transition.
- The ambient-control comparison method is reusable for later transition stages, especially Stage24 and Stage28.

## Lower-stage reinterpretations

No lower stage is reopened. Stage16S is the intrinsic `B^-1` control; Stage17 is the interaction-enriched target; Stage13 supplies the principal-sector bulk localization; Stage11 AR-038/039 retain their original contracts.

## Stage-end artifact decisions

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_PRESENT=YES
SELF_CONTAINED_BUNDLE=stages/stage21/final.md
ARSENAL_PROMOTION_REQUIRED=YES
ARSENAL_PROMOTION_PRESENT=YES
ARSENAL_ARTIFACT=docs/stage21-arsenal.md
ARSENAL_CANDIDATES=ambient-control interaction adapter; one-face to space-diagonal transition law
MANIFEST_PRESENT=YES
MANIFEST=stages/stage21/manifest-r01.md
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

## Repair submission

```text
STAGE21_70=BOUNDED_CLOSEOUT_REPAIR_SUBMITTED_FOR_FRESH_AUDIT
MATHEMATICS_CHANGED=false
EVIDENCE_LEVEL=PROVED
POST_AUDIT_PROMOTION_REQUIRED=false
PROMOTIONS_ALREADY_MATERIALIZED=true
AUDIT_STATUS=PENDING_REAUDIT
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage21-audit
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
