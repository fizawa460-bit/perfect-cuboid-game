# Stage20-70 — bounded maximal synthesis / intrinsic-status closeout candidate

EVIDENCE_LEVEL=PROVED
CHECKPOINT=70
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## Repository-wide reuse preflight

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
STRONGER_PRIOR_RESULT=Stage14-e11_PR188_explicit_thin_cover_log_saving
NEW_RESEARCH_JUSTIFIED=bounded_synthesis_only; no new large theorem or computation opened
```

The preflight found that Stage14-e11 / PR #188 is the strongest audited project upper theorem currently available for the exact Stage20 Euler-brick population. It supersedes the checkpoint60 strongest-known metadata from Stage14-e10 while leaving the e10 and e8 theorems valid as weaker provenance layers.

Stage14-e11 proves, under the same primitive/canonical Euclidean cutoff and with no space-diagonal integrality condition,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}
\qquad\text{for every fixed }\eta<1/46.
\]

In particular the endpoint-free concrete bound

\[
\boxed{M_3(B)\ll B(\log B)^{5-1/50}}
\]

is certified. The endpoint `eta=1/46` is not claimed.

No Stage14-e12 or later e-supplement exists in the repository search, and no audited stronger Stage20 lower bound than checkpoint50a was found.

## Numerical reuse preflight

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R03
NUM_POPULATION_MATCH=NO_MATCH
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CONTROL_ONLY
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

NUM-R01 is integral-space-diagonal prefiltered and therefore is not the Stage20 ambient Euler population. Its finite triple record is only a perfect-cuboid-intersection control and is not used as a Stage20 count or nonexistence argument. No new census is opened at checkpoint70.

The compatible Stage14-e exact Euler census is retained only as computed evidence. Representative same-population values include `M_3(2000)=7` and `M_3(10^6)=219`; the square-root-looking finite scale remains diagnostic only.

## KNOWN_RESULTS

1. **Population contract.** Stage20 counts primitive canonical Euler cuboids
   \[
   0<a<b<c,\quad \gcd(a,b,c)=1,\quad R=\sqrt{a^2+b^2+c^2}\le B,
   \]
   with all three face diagonals integral and with no requirement that `R` be integral.
2. **Finite baseline.** The Stage20 enumerator gives counts
   `0,0,0,1,3,5,5,7` at `B=50,100,200,400,800,1200,1600,2000`; larger compatible Stage14-e census data are computation only.
3. **Growth-law gate.** No asymptotic formula and no true growth exponent are proved.
4. **Strongest certified upper theorem.** For every fixed `eta<1/46`,
   \[
   M_3(B)\ll_\eta B(\log B)^{5-\eta}.
   \]
   A concrete frozen choice is `eta=1/50`.
5. **Certified constructive lower theorem.** The Stage20-50a primitive Saunderson subfamily gives
   \[
   M_3(B)\ge \left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4
   \]
   for all sufficiently large `B`, hence
   \[
   M_3(B)\gg B^{1/6}.
   \]
6. **Infinitude.** The primitive/canonical Stage20 population is infinite.
7. **Causal model.** The two-face shared-edge Pythagorean host acquires a structured third-face condition represented by a degree-two K3 cover; this is not modeled as an independent random-square filter.
8. **Local obstruction law.** Stage14-e10 gives exact blocker masses
   \[
   \delta_2=2/9,\qquad
   \delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}=\frac2p+O(p^{-2})
   \]
   for odd primes, explaining systematic rarity without determining the global exponent.
9. **No double charge.** K3 thin-cover, local blocker, divisor-envelope, and explicit-family mechanisms are kept as distinct proof roles and are not multiplied as independent probabilities.

## ADDITIONAL_DEDUCTIONS

The current certified Stage20 envelope can be frozen as

\[
\boxed{
B^{1/6}\ll M_3(B)\ll B(\log B)^{5-1/50}.
}
\]

More generally the right side may use any fixed `eta<1/46`. Consequently Stage20 has a positive-power lower floor and polynomial upper exponent at most one, but the gap is far too large to identify the true exponent.

The finite `sqrt(B)` signal from the extended census is compatible with the certified interval but is not promoted to a theorem, asymptotic, or exponent claim.

The Stage14-e11 explicit upper interface and the Stage20-50a lower interface together make Stage20 ready for downstream transition stages without reopening Euler-population existence or reconstructing its strongest bounds from scattered sources.

## CAUSAL_SYNTHESIS

Stage20's third-face rarity has three certified, non-identical descriptions:

- **geometric:** a degree-two K3 cover of the two-face toric host;
- **local arithmetic:** positive-density residue blockers at each prime with sieve dimension two;
- **constructive survival:** an explicit primitive Saunderson family proves that the blockers do not annihilate the population.

These descriptions are complementary. The K3/thin-cover theorem pays the strongest global logarithmic saving currently known; the local blockers explain a concrete arithmetic source of rarity and admit an independent growing-prime sieve; the Saunderson lane proves quantitative survival. None currently identifies the true Stage20 asymptotic.

## LOWER_STAGE_REINTERPRETATIONS

- Checkpoint30 remains a valid audited OPEN_GATE, but its meaning is now narrower: growth is definitely unbounded and at least `B^(1/6)`; what remains unresolved is the true growth law/exponent and any asymptotic constant.
- Checkpoint40's historical ambient-cubic and e8 bounds remain valid but are superseded as strongest-known metadata first by e10 and finally by e11.
- Checkpoint50a upgrades the stage from finite existence evidence to an infinite primitive/canonical family with a quantitative height lower bound.
- Checkpoint60's causal decomposition remains valid; e11 only sharpens the quantitative thin-cover exponent and adds growing-prime uniformity.

## REFINEMENT_CANDIDATES

1. improve the constructive lower exponent beyond `1/6` by a higher-dimensional injective primitive family;
2. improve the global upper bound beyond the current explicit thin-cover logarithmic saving;
3. turn the observed near-square-root finite scale into either a theorem or a certified counter-signal;
4. study the transition ratio from Stage18 to Stage20 only in Stage26, where source and target measures are explicitly compared;
5. use the exact local blocker law in Stage26/27/28 without interpreting it as probabilistic independence.

## NEW_HEURISTICS

```text
SQRT_B_FINITE_CANDIDATE_ONLY=true
HEURISTIC_TRUE_EXPONENT_APPROX_HALF=UNPROVED
```

No heuristic is used in any proved bound or closeout decision.

## OPEN_GATES

```text
OPEN_GATE_1=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_2=TRUE_EXPONENT_UNRESOLVED
OPEN_GATE_3=MATCHING_LOWER_BOUND_UNRESOLVED
OPEN_GATE_4=ASYMPTOTIC_CONSTANT_UNRESOLVED
OPEN_GATE_5=SQRT_B_SIGNAL_THEOREM_STATUS_UNRESOLVED
```

These gates are not reopened inside checkpoint70 because resolving them would require a substantially new theorem, new family program, or new large computation.

## NEXT_STAGE_QUESTIONS

- Stage21 begins the transition program at `16 -> 17` against Stage16S.
- Stage26 is the designated receiver for `18 -> 20`; it may reuse the frozen Stage18 asymptotic together with this Stage20 e11 upper interface to study zero density and the true conditional thinning law, but Stage20 does not claim that transition theorem here.
- Stage27 may reuse the same Stage20 upper/lower interfaces for `16 -> 20`.
- Stage28 may compare K3, local-sieve, and explicit-family mechanisms against the other condition transitions.

## SYNTHESIS_STOP_REASON

Further progress on the true Euler-cuboid growth law would require genuinely new research beyond the certified Stage20-10 through Stage20-60 inputs: a stronger counting theorem, a stronger construction family, or a new large-scale arithmetic program. The bounded synthesis therefore stops here.

```text
SYNTHESIS_STOP_RULE_SATISFIED=YES
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
OPEN_GATE_REENTRY_JUSTIFIED=NOT_APPLICABLE
ARSENAL_SUPERSESSION_CHECK=PASS
DOUBLE_CHARGE_CHECK=PASS
```

## Stage-end artifact decisions

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage20 combines scattered Stage14-e8/e10/e11 interfaces with a new Stage20 lower family and will be reused by Stages26-28; a stable source is safer than reconstructing the claims from chronology.
ARSENAL_PROMOTION_REQUIRED=YES
ARSENAL_CANDIDATES=S20-W01_EXPLICIT_EULER_THIN_COVER_UPPER,S20-W02_PRIMITIVE_SAUNDERSON_LOWER,S20-W03_EULER_LOCAL_BLOCKER_LAW
```

The reusable contracts are written in `docs/stage20-arsenal.md` in this closeout candidate.

## Boundary / nonclaims

Stage20 does not impose an integral space diagonal and says nothing about perfect-cuboid existence or nonexistence. It does not prove `M_3(B)~CB^alpha`, `M_3(B)\asymp B^{1/2}`, a matching lower bound, the endpoint `eta=1/46`, or an independence law for the third-face condition. Stage18-to-Stage20 conditional thinning remains owned by Stage26.

```text
AUDIT_STATUS=PENDING
AUDIT_PERSISTENCE_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=
NEXT_STAGE=Stage21
NEXT_EXPECTED_COMMAND=Stage20-audit
CODEX_REQUIRED=false
```
