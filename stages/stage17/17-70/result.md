# Stage17-70 — bounded maximal synthesis / intrinsic-status closeout

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## 1. Frozen Stage17 theorem

Stage17 counts primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\]

with exactly one integral face diagonal, integral space diagonal

\[
d^2=a^2+b^2+c^2,
\]

and common cutoff `R<=B`, where `R=sqrt(a^2+b^2+c^2)`. On every Stage17 object positivity gives the exact identity

\[
d=R,
\]

so `d<=B` and `R<=B` are identical cutoffs.

The audited Stage13 interface is literally this target population and gives

\[
\boxed{N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3},
\qquad \frac{\kappa}{24\pi}>0.
\]

Hence Stage17 identifies its absolute growth law at full asymptotic resolution:

```text
TRUE_ORDER_IDENTIFIED=true
POLYNOMIAL_EXPONENT=1
LOG_POWER=3
LEADING_CONSTANT_PROVED=true
LEADING_CONSTANT=kappa/(24*pi)
ABSOLUTE_INTRINSIC_STATUS=PROVED_ASYMPTOTIC
```

## 2. Matched Stage16 -> Stage17 survival law

The audited Stage16 source law is

\[
M_1(B)\asymp B^2\log B
\]

for the same primitive/canonical exactly-one population before integral space diagonal is imposed.

Therefore

\[
\boxed{\frac{N_1(B)}{M_1(B)}\asymp\frac{(\log B)^2}{B}\to0}.
\]

So imposing integral space diagonal after the one-face condition costs one polynomial power of `B`, with net `(log B)^2` compensation.

No leading constant for this ratio is certified because Stage16 proves only a `Theta` law for `M_1(B)`.

```text
SURVIVOR_RATIO_CLASS=POLYNOMIALLY_SMALL_WITH_LOG_SQUARED_CORRECTION
SURVIVOR_RATIO_LIMIT=0
LEADING_SURVIVOR_RATIO_CONSTANT_PROVED=false
```

## 3. Additional bounded deduction: exactly-one dominates among space-diagonal cuboids having a face

Let `H_{1,d}(B)` count the same primitive canonical integral-space-diagonal population under `d=R<=B` but require **at least one** integral face diagonal instead of exactly one.

Stage13 defines the three raw face-incidence counts and proves every pair overlap

\[
A_{ab,ac},\ A_{ab,bc},\ A_{ac,bc}
=o(B(\log B)^3).
\]

Let

\[
P(B)=A_{ab,ac}+A_{ab,bc}+A_{ac,bc}.
\]

Every object counted by `H_{1,d}(B)-N_1(B)` has at least two integral faces and therefore contributes at least once to `P(B)`. Hence

\[
0\le H_{1,d}(B)-N_1(B)\le P(B)=o(B(\log B)^3).
\]

Combining this with the positive Stage13 main term gives

\[
\boxed{H_{1,d}(B)\sim N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3}
\]

and therefore

\[
\boxed{\frac{N_1(B)}{H_{1,d}(B)}\to1}.
\]

Thus, inside the integral-space-diagonal population that has at least one integral face, objects with two or three integral faces are zero-density at the Stage13 theorem scale. This statement does not assume that perfect cuboids do not exist.

## 4. Causal synthesis

Write the unique Stage17 integral face as

\[
x^2+y^2=p^2.
\]

Stage16 permits the complementary edge `z` subject only to the common cuboid cutoff. Stage17 additionally requires

\[
p^2+z^2=d^2.
\]

So the genuinely new Stage16-to-Stage17 arithmetic predicate is a second Pythagorean extension sharing the face diagonal `p`.

The certified net effect of that new predicate is exactly the already-audited survival scale

\[
\Theta((\log B)^2/B).
\]

The following are not newly charged causes at Stage17:

- canonical ordering;
- global primitivity;
- the exactly-one source contract;
- the common `R<=B` cutoff;
- the identity adapter `d=R`.

Stage13's extra-face overlaps are lower order, so exactly-one subtraction is not the leading mechanism for the Stage16-to-Stage17 loss. AR-039 remains an explicit survivor subfamily, not an explanation of the full asymptotic.

## 5. Intrinsic-status boundary

Two meanings of “intrinsic” must remain separate.

1. **Absolute Stage17 population order:** settled. `N_1(B)` has the proved asymptotic `kappa/(24*pi) B(log B)^3`.
2. **Whether the space-diagonal condition itself is intrinsically strong, independent, correlated, or interaction-dependent:** not settled inside Stage17.

The second question requires comparison with the auxiliary Stage16S ambient space-diagonal baseline and belongs to Stage21. Stage16S is parallel and does not block Stage17 closure. If the needed Stage16S comparison remains unresolved when Stage21 closes, Stage21 must record an explicit `OPEN_GATE` rather than infer independence.

```text
ABSOLUTE_STAGE17_ORDER_INTRINSIC=YES
SPACE_DIAGONAL_COST_INTRINSICNESS=DEFER_TO_STAGE21_WITH_STAGE16S
INDEPENDENCE_CLAIM=false
```

## 6. Bounded StageX-70 synthesis

```text
KNOWN_RESULTS=N_1(B) ~ kappa/(24*pi) B(log B)^3; N_1(B)/M_1(B) ASYM (log B)^2/B -> 0; upper and lower orders match B(log B)^3; AR-039 is an explicit B^(1/2) survivor subfamily; Stage17-20 finite census is COMPUTED diagnostic evidence
ADDITIONAL_DEDUCTIONS=polynomial exponent 1, log power 3, and leading constant kappa/(24*pi) are intrinsic for the absolute Stage17 count; if H_{1,d}(B) counts integral-space cuboids with at least one integral face then H_{1,d}(B) ~ N_1(B) and N_1(B)/H_{1,d}(B)->1
CAUSAL_SYNTHESIS=the new Stage16-to-17 predicate is the second Pythagorean extension p^2+z^2=d^2 sharing the integral-face diagonal p; the net cost is one power of B with (log B)^2 compensation; exactly-one overlap removal is lower order and d=R is only an identity adapter
LOWER_STAGE_REINTERPRETATIONS=Stage17-20 finite ratios are samples of the proved zero-density law and do not determine an exponent; Stage17-40 and 50 are sharp corollaries of the frozen Stage13 asymptotic; Stage17-60 is a structural predicate decomposition, not a probabilistic independence factorization
REFINEMENT_CANDIDATES=leading constant for M_1(B), hence a leading Stage16-to-17 ratio constant; effective error term/secondary term for N_1(B); effective convergence rate for N_1/H_{1,d}; Stage16S comparison of ambient space-diagonal cost
NEW_HEURISTICS=NONE
OPEN_GATES=No gate blocks Stage17 absolute classification; leading ratio constant and effective rates require new input; intrinsic/independent/correlated/interaction-dependent classification of the space-diagonal cost is deferred to Stage21 with the audited Stage16S baseline
NEXT_STAGE_QUESTIONS=Stage18 should establish the exactly-two-face population under the common cutoff; Stage21 should consume Stage16, Stage17, and Stage16S to classify the 16->17 transition without double charging
SYNTHESIS_STOP_REASON=Further refinement requires a new Stage16 leading-constant theorem, a new effective Stage13 error theorem, additional Stage16S work, or transition-stage comparison outside Stage17
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

No lower checkpoint is reopened because no Stage17 population definition, cutoff, canonicalization rule, theorem, finite baseline, or audited adapter has been invalidated.

## 7. Checkpoint classification

```text
CHECKPOINT_10=PROVED_AUDIT_PASS
CHECKPOINT_20=COMPUTED_AUDIT_PASS
CHECKPOINT_30=PROVED_AUDIT_PASS
CHECKPOINT_40=PROVED_AUDIT_PASS
CHECKPOINT_50=PROVED_AUDIT_PASS
CHECKPOINT_60=PROVED_AUDIT_PASS
CHECKPOINT_70=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=IDENTITY_ONLY_d_equals_R
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
OPEN_GATE_REENTRY_JUSTIFIED=NOT_APPLICABLE
ARSENAL_SUPERSESSION_CHECK=NOT_APPLICABLE
```

## 8. Stage-end artifact decisions

Stage17 combines two frozen major interfaces, Stage13 and Stage16, through a subtle but exact population/cutoff adapter and produces a transition law that Stage21 will reuse. Reconstructing those assumptions from scattered checkpoints is error-prone. A single final Markdown bundle is therefore required.

The bundle uses the frozen-earlier-stage-interface rule of `SELF_CONTAINED_REVIEW_STANDARD_V1`: upstream theorem statements are printed exactly enough to audit the transfer, while the Stage17 adapters and deductions are proved internally.

A new arsenal entry is not required. The principal reusable output is the Stage17 population theorem/transition interface itself, and Stage21 can cite the stable final bundle directly. Creating a duplicate arsenal item would add a second source of truth without adding a more general method.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage17 combines frozen Stage13 and Stage16 theorem interfaces through an exact d=R population adapter and produces a repeatedly reusable Stage16-to-Stage17 survival law; one stable bundle prevents population/cutoff drift.
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
```

## 9. Proposed stage transition

A fresh `Stage17-audit` must certify this checkpoint, `stages/stage17/final.md`, and `stages/stage17/manifest-r01.md` before Stage17 closes.

If PASS is durably persisted:

```text
STAGE_STATUS=CLOSED
ADVANCE_ALLOWED=true
NEXT_STAGE=Stage18
```

Stage16S remains a parallel lane and Stage21 remains the receiver for the intrinsic-versus-interaction comparison.

Until that audit passes, Stage17 remains open at checkpoint 70.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage17
CURRENT_CHECKPOINT=70
CHECKPOINTS_ATTEMPTED=70
CHECKPOINTS_SUBMITTED=70
NEW_CLAIMS=absolute intrinsic-status verdict; exactly-one dominance within the at-least-one-face integral-space population; bounded synthesis and artifact decisions; no new upstream asymptotic theorem
REUSED_WEAPONS=Stage13 exact-one asymptotic and overlap theorem,Stage16 source law,AR-039(regression/construction only)
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 70 is a bounded mathematical synthesis and interface-bundle assembly from audited sources; no repository-heavy implementation is required.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage17-audit
MERGE_ALLOWED=false
```
