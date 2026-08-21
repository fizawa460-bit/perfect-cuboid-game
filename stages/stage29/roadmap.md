# Stage29 — interaction synthesis and perfect-cuboid endpoint routing

```text
STAGE=Stage29
ROLE=INTERACTION_SYNTHESIS_AND_ENDPOINT_ROUTING
NUMBERING=INCREMENTAL_01_02_03...
LEGACY_10_70_SEQUENCE_USED=false
PERFECT_CUBOID_ENDPOINT_ITSELF_DEFERRED=true
```

Stage29 is not a new population stage. It synthesizes Stage16–28 and decides how the project should move from population thinning/interaction analysis to a direct perfect-cuboid endpoint attack.

The stage uses ordinary incremental numbering. If a genuinely new branch appears between planned items, use suffixes such as `29-04a`, `29-04b`; do not force the work into a 10/20/30/40/50/60/70 template.

## Core questions

1. Which conditions are genuinely independent, dependent, or repeated descriptions of the same arithmetic restriction?
2. Which mechanisms actually dominate population loss: extra face integrality, space-diagonal integrality, or their interaction?
3. Which endpoint entrance is mathematically more tractable?
   - Entrance A: Stage19 (`two faces + space`) + third face.
   - Entrance B: Stage20 (`three faces`) + space diagonal.
4. Can the successful StageA2 method species — low-dimensional reduction, cover decomposition, elliptic/hyperelliptic descent, rank/torsion/rational-point closure — be transferred to a natural endpoint slice without pretending that the A2 published family is universal?
5. What is the smallest precise theorem/construction/adapter receiver that should be handed to a later direct endpoint stage?

## Incremental roadmap

### 29-01 — GLOBAL_CERTIFIED_MAP_LOCK

Freeze the current certified Stage16–28 population/transition map under common physical conventions. Separate merged/audited facts from pending candidates. Materialize the Stage29 operating rules and first gap scan.

### 29-02 — CONDITION_COST_MATRIX

Put one-face, second-face, third-face, and space-diagonal costs on a common ledger. Keep exact asymptotics, power corridors, log effects, zero-density statements, local sieve dimensions, and geometric branch data separate.

### 29-03 — DEPENDENCY_AND_DOUBLE_CHARGE_LEDGER

Classify squareclass, Gaussian norm, common-core/divisor, local parity sieve, thin-cover, branch-profile, and construction information as independent/new/reused/correlated. Forbid multiplying different proof descriptions of the same predicate.

### GAP_SCAN_A — after 29-03

Explicitly ask whether any essential comparison is still missing before endpoint routing. If yes, open a narrowly scoped `29-03a/b/...`; if not, record `NO_ADDITIONAL_ANALYSIS_REQUIRED` and continue.

### 29-04 — ENDPOINT_ENTRANCE_A

Derive the exact algebraic form of adding the third face to the Stage19 physical family. Record parameter freedom, height, multiplicity, covers/fibrations, local obstructions, and natural low-dimensional slices.

### 29-05 — ENDPOINT_ENTRANCE_B

Derive the exact algebraic form of adding the space diagonal to the Stage20 Euler family under the same audit discipline.

### 29-06 — ENTRANCE_COMPARISON_AND_ROUTING

Compare A and B by exact equation complexity, geometry, genus/fibration type, parameter freedom, height distortion, reconstruction multiplicity, known constructions, and available theorem species. Select a primary and reserve entrance only if justified.

### GAP_SCAN_B — after 29-06

Ask whether the entrance comparison omitted a necessary model, family, height adapter, or symmetry quotient. Open a narrow interstitial analysis only when the omission is material.

### 29-07 — A2_METHOD_TRANSFER_PREFLIGHT

Use StageA2 only as a method source. Test whether the selected endpoint entrance has natural slices/covers that can be reduced to quartic, genus-1, genus-2/3, or finite descent problems. Preserve the firewall `A2 family-specific exclusion != arbitrary perfect-cuboid exclusion`.

### 29-08 — NATURAL_SLICE_COVER_DESCENT_TEST

On one or more natural high-relevance endpoint slices, attempt exact quotient/cover/descent reductions with height and multiplicity tracked. A negative family-specific closure is useful only if the slice is naturally connected to the Stage19/20 host; coverage claims require proof.

### GAP_SCAN_C — after 29-08

Ask whether the chosen slices are too special to inform endpoint routing. If representativeness/coverage is the real missing input, state it explicitly instead of opening arbitrary new families.

### 29-09 — ENDPOINT_ARSENAL_REMATCH

Rematch StructureRadar, prior Stage14/15/19/20 weapons, StageA2 method components, geometry, sieve, determinant/incidence, character sums, and rational-point technology against the exact endpoint receiver(s).

### 29-10 — RESIDUAL_RECEIVER_COMPRESSION

Compress unresolved work to at most a small number of precise receivers. Each receiver must state the exact population/variety, measure/height, quantifiers, multiplicity, required strength, and what perfect-cuboid consequence would follow.

### GAP_SCAN_FINAL — before handoff

Perform one final missing-analysis scan: unused repo-native weapon, missing symmetry/height adapter, overlooked endpoint entrance, or unjustified coverage assumption. `NONE_FOUND` is an acceptable result.

### 29-11 — PERFECT_CUBOID_HANDOFF

Freeze the primary endpoint entrance, best algebraic model, best analytic/geometric route, StageA2-transfer verdict, residual receivers, and the recommended contract for a later direct endpoint stage.

### 29-close

Close Stage29 after fresh audit. Stage29 need not solve the perfect-cuboid problem; its success criterion is a correct, non-double-counted synthesis and a sharply routed endpoint attack.

## Gap-scan rule

Gap scans are mandatory at the named synthesis points but are not forced to create work. Each scan records one of:

```text
GAP_SCAN=NONE_FOUND
GAP_SCAN=FOUND_INTERNAL_ANALYSIS_REQUIRED
GAP_SCAN=FOUND_EXTERNAL_INPUT_REQUIRED
GAP_SCAN=FOUND_PENDING_UPSTREAM_CERTIFICATION
```

A gap may create an interstitial route only if it is mathematically distinct and necessary for the next decision. Cosmetic subdivisions and renamed theorem gates are forbidden.

## Stage28 late-binding rule

Stage29 may start while a late Stage28 branch is still pending, but only merged/audited Stage28 material is certified input. Any still-open Stage28 PR is `CANDIDATE_ONLY` and cannot alter Stage29 conclusions until audited and merged. Before Stage29 makes the endpoint-entrance decision, it must refresh the Stage28 frontier.

```text
PENDING_STAGE28_CANDIDATE_MAY_BE_CITED_AS_CERTIFIED=false
STAGE28_REFRESH_REQUIRED_BEFORE_29_06=true
```
