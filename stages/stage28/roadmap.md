# Stage28 — Stage19 -> Stage20 population-thinning analysis

```text
STAGE=Stage28
ROLE=STAGE19_TO_STAGE20_SURVIVAL_ANALYSIS
STATUS=ROADMAP_DRAFT
PRIMARY_GOAL=quantify how much of the Stage19 population survives the additional Stage20 predicate
SOURCE_STAGE=Stage19
TARGET_STAGE=Stage20
ADVANCE_POLICY=do not infer a fixed-power thinning without a same-measure proof
```

## 1. Scope

Stage28 compares the literal Stage19 and Stage20 physical populations under matched primitive/canonical conventions and the same geometric cutoff wherever the upstream interfaces permit it.

The central question is not the separate absolute size of Stage19 or Stage20, but the transition

`Stage19 population -> impose the Stage20-only condition -> Stage20 population`.

Stage28 should measure the resulting survival/thinning, preserving the exact physical measure and avoiding independence assumptions or double charging of conditions already paid in Stage19.

## 2. Main route

### 28-10 — POPULATION_INTERFACE_LOCK

- identify the exact Stage19 source population and Stage20 target population;
- isolate the predicate(s) added only at Stage20;
- verify cutoff, primitivity, canonical ordering, object multiplicity, and any orientation conventions;
- materialize any required measure/height adapter explicitly.

### 28-20 — FINITE_BASELINE_AND_SANITY_CHECK

- compute or import matched finite counts where already available;
- verify literal set inclusion `Stage20 subset Stage19` on the matched census;
- use finite data only as diagnostics, never as an asymptotic theorem.

### 28-30 — EXACT_SURVIVAL_OPERATOR

Define the Stage20 survivor indicator on the Stage19 source measure and write the exact identity

`M20(B) = sum_{omega in Omega19(B)} I20(omega)`

or its exact packetized version.

No probability-factor interpretation is allowed unless separately proved.

### 28-40 — UPPER_THINNING

Seek a same-measure upper survival estimate. Useful outputs include:

- fixed-power survival deficit;
- packetwise exceptional-set plus regular-packet suppression;
- support/energy or second-moment deficit;
- determinant/incidence or sieve suppression with a zero-loss adapter.

Existing Stage19/20 upper inputs may be combined only when the charged conditions are demonstrably independent or the hybrid inequality is explicitly proved.

### 28-50 — LOWER_SURVIVOR_FAMILY

Seek an explicit Stage20-surviving subfamily inside Stage19 with controlled height and finite-to-subpower multiplicity. Record the resulting lower survival exponent or lower ratio when one is genuinely proved.

### 28-60 — STRUCTURERADAR_ARSENAL_REMATCH

Rematch the exact Stage19 -> Stage20 receiver against StructureRadar/Arsenal. Prioritize tools that become legal only after the source and target measures are aligned. Do not re-open frozen routes by renaming an existing theorem gate.

### 28-70 — THINNING_SYNTHESIS

Combine the best certified upper and lower information and state exactly what is known about the transition. Distinguish:

- fixed-power thinning;
- zero-density only;
- logarithmic thinning;
- unresolved upper/lower gap.

### 28-80 — HANDOFF_TO_STAGE29

Export a compact interface for Stage29 containing:

- source and target population definitions;
- best Stage19 and Stage20 absolute bounds/asymptotics;
- best certified 19 -> 20 survival/thinning information;
- unresolved theorem/construction gates;
- no speculative exponent interpolation.

## 3. Anti-loop policy

Forbidden:

- treating the ratio of unrelated upper/lower bounds as a proved survival law;
- assuming independence between Stage20's new predicate and Stage19 constraints;
- double charging a Stage19 condition as a new Stage20 saving;
- using a theorem on a larger host without a same-measure adapter;
- converting finite census ratios into asymptotic claims;
- extending a frozen theorem gate by a renamed subroute with no new input.

## 4. Success criteria

Stage28 succeeds if it produces at least one of:

1. an exact Stage19 -> Stage20 same-measure survival operator;
2. a certified quantitative thinning law or stronger upper survival bound;
3. a certified Stage20-surviving lower family;
4. a precise StructureRadar theorem/construction receiver;
5. a complete handoff describing what is and is not known about the 19 -> 20 population drop.

```text
NEXT_EXPECTED_COMMAND=Stage28-audit
FINAL_HANDOFF=Stage29
```
