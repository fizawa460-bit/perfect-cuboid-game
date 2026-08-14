# Stage21-28 full exploration policy

Status: **normative addendum to `docs/stage16-28-population-roadmap.md`**.

## Phase boundary

Stages16-20 and Stage16S primarily establish **population baselines and stable theorem interfaces**. Their job is to freeze the objects, cutoff, multiplicity, finite baselines, absolute growth laws, usable upper/lower bounds, and intrinsic causal descriptions that later comparisons need. They may contain substantial mathematics, but they are not required to exhaust every refinement of those populations before the transition program begins.

Stages21-28 are a different research phase. They are the **full condition-interaction exploration program**. A transition stage must not be treated as complete merely because two frozen formulas can be substituted and divided. Formula substitution is the starting calculation, not the default stopping point.

The intended Stage21-28 objective is to extract as much rigorous information as is reasonably available from the transition before closeout, while preserving the existing OPEN_GATE and evidence-level safety rules.

## Mandatory exploration depth for Stage21-28

For every transition stage, the controller should pursue the following layers when mathematically relevant.

1. **Strongest source/target interfaces.** Search not only the immediately preceding final bundles but also earlier stages, auxiliary tracks, supplements, archives, historical PRs, arsenal entries, and exact adapters for stronger asymptotics, explicit constants, directional laws, error terms, constructions, local laws, or superseding bounds.
2. **Exact transition law.** Derive the strongest matched source-to-target ratio supported by the interfaces. If a leading constant is recoverable, do not stop at `Theta`. If a directional or chamberwise law is recoverable, test it explicitly.
3. **Intrinsic versus conditional comparison.** Compare the transition with the appropriate control population or alternate path through the condition lattice. Stage21 must use Stage16S; later stages should use the comparison square and previously audited arrows whenever available.
4. **Interaction diagnosis.** Test whether the new condition behaves as an independent baseline filter, is enhanced or suppressed after previous conditions, shares a previously charged mechanism, or introduces a genuinely new obstruction. Do not infer probabilistic independence merely from matching polynomial exponents.
5. **Refinement search.** Look for explicit constants, log-power refinements, directional cancellation, local-density factors, squareclass/valuation structure, secondary bounds, sharper constructions, and exact inclusion/intersection identities that strengthen the first ratio calculation.
6. **Independent proof routes.** When genuinely different mechanisms are available, open bounded sublanes rather than forcing everything into one proof. Suitable lanes include analytic/global counting, algebraic/parametric normal forms, local/sieve obstructions, construction/lower-bound families, and finite computation/regression.
7. **Targeted computation.** Reuse existing numerical assets first. New computation is justified when it discriminates between live hypotheses, validates an adapter or enumerator, locates a transition regime, or tests a causal mechanism. It must not substitute for proof.
8. **Literature and repository exploration.** Search by direct terminology, synonyms/notation, mathematical structural signatures, and dependency neighbors. A result should not be missed merely because an earlier task used different vocabulary.
9. **New deductions.** Once the main transition theorem is established, derive nontrivial consequences that follow from the combined interfaces, including normalized comparisons, relative enhancement/suppression factors, directionwise statements, or implications for later transition stages.
10. **Portable weapons.** Promote reusable transition laws, adapters, mechanisms, warnings, and verifiers when they are likely to matter to later stages.

## Checkpoint interpretation in the exploration phase

The ordinary `10/20/30/40/50/60/70` checkpoint numbers remain in force, but their role changes in Stage21-28.

- `10` freezes the transition source/target and comparison lattice.
- `20` establishes or reuses the finite matched baseline and validates adapters.
- `30` establishes the **first** quantitative transition law. A simple quotient of known formulas may close checkpoint30, but it does not by itself close the stage.
- `40` searches for the strongest certified upper/refinement side, including stronger buried interfaces.
- `50` searches for lower/construction or converse information and determines how much of the observed transition is forced.
- `60` performs the full causal/interaction decomposition, including alternate-path and intrinsic-baseline comparisons.
- `70` performs bounded maximal synthesis and closeout after the exploratory work above has been attempted.

The Stage70 stopping rule does **not** prohibit substantial new research during checkpoints30-60. Its purpose is only to prevent the closeout checkpoint itself from recursively opening an unbounded new research program. If a promising new theorem, computation, or independent proof route is identified before Stage70, it may be opened as a bounded sublane and audited normally.

## Exploration is bounded by evidence, not by convenience

A transition stage should stop exploration when further progress requires an identified new theorem/input outside the current feasible program, not merely because the first algebraic ratio has been written down. An audited `OPEN_GATE` remains a valid endpoint when the missing input is precise.

Conversely, the controller must not prolong a stage with repeated paraphrases of the same failed route. Existing `NEW_INPUT_REQUIRED` and OPEN_GATE re-entry rules still apply.

## Required Stage21-28 exploration markers

Before Stage21-28 checkpoint70 submission, record:

```text
EXPLORATION_PHASE=FULL_TRANSITION_RESEARCH
FORMULA_SUBSTITUTION_ONLY=false
SOURCE_INTERFACE_UPGRADE_CHECK=PASS|FAIL
TARGET_INTERFACE_UPGRADE_CHECK=PASS|FAIL
CONSTANT_REFINEMENT_CHECK=PASS|NOT_APPLICABLE
DIRECTIONAL_REFINEMENT_CHECK=PASS|NOT_APPLICABLE
STRUCTURAL_SIGNATURE_SEARCH=PASS
DEPENDENCY_NEIGHBOR_SEARCH=PASS
INTRINSIC_BASELINE_COMPARISON=PASS|OPEN_GATE|NOT_APPLICABLE
ALTERNATE_PATH_COMPARISON=PASS|OPEN_GATE|NOT_APPLICABLE
INTERACTION_CLASSIFICATION=PROVED|PARTIAL|OPEN_GATE
NEW_SUBLANES_OPENED=<list or NONE>
NEW_DEDUCTIONS_RECORDED=<list or NONE>
EXPLORATION_STOP_REASON=<specific reason>
```

`FORMULA_SUBSTITUTION_ONLY=false` means the stage has considered the exploration layers above. It does not require that every layer yield a positive theorem.

## Known Stage21/22 preflight candidates

The following already-discovered repository results must be inspected when Stage21 and Stage22 begin. They are candidate inputs until the transition stage performs its own exact population/cutoff audit.

### Stage21 candidates

- `stages/euler-cuboid/E-1e/result.md` / PR #128: exact-one, no-space-diagonal asymptotic with explicit total and directional constants under the same Euclidean cutoff candidate.
- `stages/stage17/final.md` and Stage13 frozen interfaces: exact-one plus integral-space asymptotic with explicit `kappa` and directional `I_q` factors.
- `stages/stage16s/final.md`: intrinsic ambient space-diagonal baseline with explicit constant.

Stage21 should test whether these interfaces upgrade the old `Theta` survival law to a leading-constant law, whether the common directional factors cancel, and whether comparison with Stage16S proves enhancement/suppression relative to the intrinsic space-diagonal baseline.

### Stage22 candidates

- `stages/euler-cuboid/E-1e/result.md` / PR #128: explicit exactly-one source constant.
- Stage14-e6 / PR #159: explicit Peyre/Tamagawa constant for the ambient exactly-two population under the physical Euclidean height candidate.
- `stages/stage18/final.md`: exact Stage18 population/cutoff contract.

Stage22 should test literal population equality and, if certified, upgrade the source-to-target comparison to an explicit leading-constant transition law. Because exactly-one and exactly-two masks are disjoint, it should also determine whether an at-least-one to at-least-two filtration gives the cleanest literal survivor interpretation.

## Codex / auxiliary-agent use

Codex or another bounded auxiliary agent may be used when repository-scale source discovery, algebraic verification, computational regression, or an independent proof subtask would materially improve the exploration. It is not mandatory merely because a stage is numbered 21-28. The main controller remains responsible for population adapters, theorem scope, evidence level, and the final audited claim.

## Research intent lock

The project intent for Stage21-28 is therefore:

```text
BASELINE_PHASE=Stage16-20_and_Stage16S
FULL_EXPLORATION_PHASE=Stage21-28
TRANSITION_FORMULA_IS_STARTING_POINT_NOT_DEFAULT_STOP=true
PROACTIVE_REFINEMENT_SEARCH=true
PROACTIVE_INTERACTION_SEARCH=true
BOUNDED_NEW_RESEARCH_SUBLANES_ALLOWED=true
MAXIMIZE_RIGOROUS_DEDUCTIONS_WITHIN_STAGE_SCOPE=true
STAGE70_PREVENTS_CLOSEOUT_EXPLOSION_NOT_STAGE_RESEARCH=true
```
