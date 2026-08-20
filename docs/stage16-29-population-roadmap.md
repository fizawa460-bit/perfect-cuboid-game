# Stage16-29 Population / Condition-Interaction Roadmap

Status: **canonical numbering overlay extending the Stage16-28 roadmap through Stage29**.

This document supersedes `docs/stage16-28-population-roadmap.md` for stage numbering from Stage27 onward. All population contracts, checkpoint rules, audit-persistence rules, reuse-preflight rules, Stage16S rules, Stage20 literature-reuse rules, Stage19 carry-over cautions, Stage70 policy references, and operational safety invariants from the Stage16-28 roadmap remain in force unless explicitly overridden here.

The purpose of this overlay is narrow: Stage27 has in repository reality become the `Stage18 -> Stage19` strict reattack. Therefore the next comparison `Stage19 -> Stage20` is assigned to Stage28, and the former Stage28 interaction-synthesis role moves to Stage29.

## Canonical population states

| Stage | Population state | Primary question |
|---|---|---|
| **Stage16** | exactly one integer face diagonal | Why is the one-face population abundant, and what are its natural parameter freedoms? |
| **Stage16S** | auxiliary space-diagonal baseline | How large is the population with integral space diagonal before any integer-face condition is imposed? |
| **Stage17** | one integer face diagonal + integer space diagonal | What does the space-diagonal condition remove from Stage16? |
| **Stage18** | exactly two integer face diagonals | Why does adding the second integer face diagonal thin Stage16 so strongly? |
| **Stage19** | exactly two integer face diagonals + integer space diagonal | Determine the true growth scale and sharpen the certified bounds for the Stage14/15 target population. |
| **Stage20** | three integer face diagonals (Euler cuboids), no space-diagonal requirement | Establish and sharpen the Euler-cuboid population baseline. |

`Stage16S` remains an auxiliary parallel baseline and does not change the numbered sequence.

## Canonical transition / comparison stages

Stages through Stage26 retain their already established contracts. The numbering correction begins at Stage27.

| Stage | Transition / comparison | Canonical role |
|---|---|---|
| **Stage21** | **16 -> 17**, compared against **16S** | space-diagonal cost after one face |
| **Stage22** | **16 -> 18** | second-face cost from the one-face population |
| **Stage23** | **17 -> 19** | second-face cost with space integrality already imposed |
| **Stage24** | **18 -> 19** | original two-face-to-two-face-plus-space comparison |
| **Stage25** | **16 -> 19** | combined thinning and double-charge analysis |
| **Stage26** | **18 -> 20** | two-face to Euler comparison |
| **Stage27** | **18 -> 19** | strict research reattack/closure of the two-face-to-space-survivor transition; repository controller contract governs |
| **Stage28** | **19 -> 20** | matched Stage19/Stage20 bridge comparison under common cutoff/canonicalization; do not assume a literal subset relation |
| **Stage29** | **interaction synthesis** | compare all certified transition laws, overlaps, dependencies, and dominant population-killing mechanisms |

### Stage27 authority

`stages/stage27/27-controller.json` is authoritative for Stage27. Its frozen transition is:

```text
Stage18 -> Stage19
```

The Stage27 work tree may contain historically named `27-20-*` checkpoint or derived-route artifacts. Those names are provenance inside Stage27 and are **not** evidence that the stage-level population transition is `Stage19 -> Stage20`. Do not bulk-move or renumber those historical artifacts solely because of this roadmap correction.

### Stage28 contract

Stage28 studies the relationship between the already established Stage19 and Stage20 populations under matched conventions:

```text
SOURCE_POPULATION = Stage19 population
TARGET_POPULATION = Stage20 population
COMPARISON         = Stage19 -> Stage20
```

Because Stage19 includes integral space diagonal while Stage20 is the Euler-cuboid population without a space-diagonal requirement, Stage28 must not silently describe the comparison as literal subset thinning. Checkpoint 10 must freeze the exact comparison semantics and any host/intersection adapter before ratios or exponent differences are interpreted causally.

Stage28 uses the ordinary checkpoint sequence:

```text
Stage28-10
Stage28-20
Stage28-30
Stage28-40
Stage28-50
Stage28-60
Stage28-70
```

with canonical commands:

```text
Stage28-main-batch
Stage28-audit
```

The stage should reuse the audited Stage19 and Stage20 controllers/final bundles before opening new research. In particular, it must preserve the distinction between certified bounds and true asymptotic exponents.

### Stage29 contract

Stage29 inherits the former Stage28 role: interaction/exception synthesis across the completed population map. It is not a new population state and must not manufacture an extra condition merely to justify the new number.

Its primary outputs are:

1. a common-cutoff comparison table for all certified populations and transitions;
2. a dependency/overlap ledger preventing the same arithmetic restriction from being charged twice;
3. identification of condition independence, dependence, and interaction effects;
4. a strongest-certified upper/lower-bound ledger with true-exponent status kept explicit;
5. a residual-obstruction statement describing what remains before the perfect-cuboid endpoint is opened.

Stage29 uses the ordinary checkpoint sequence and commands:

```text
Stage29-10,20,30,40,50,60,70
Stage29-main-batch
Stage29-audit
```

## Renumbering compatibility rules

For documents or prompts that predate this correction:

```text
legacy "Stage27 = 16 -> 20"          -> obsolete; use the Stage27 controller (18 -> 19)
legacy "Stage28 = interaction synthesis" -> Stage29
legacy roadmap range "Stage16-28"   -> Stage16-29 when referring to the full current roadmap
```

These semantic substitutions do **not** rename stable supporting policy filenames such as `docs/stage16-28-stage70-policy.md` or `docs/stage16-28-reuse-preflight.md`. Those filenames remain valid dependencies until a separate repository-wide rename is deliberately performed.

## Common completion gates

Stage28 and Stage29 inherit the standard StageX checkpoints from the Stage16-28 roadmap:

- `10`: population/comparison contract;
- `20`: finite-data baseline;
- `30`: ratio/thinning/comparison law;
- `40`: strongest certified upper-bound ledger;
- `50`: strongest certified lower-bound/construction ledger;
- `60`: causal decomposition and double-charge check;
- `70`: bounded maximal synthesis, intrinsic-status classification, artifact/arsenal decision, and closeout synchronization.

Every checkpoint must keep `PROVED`, `LITERATURE`, `COMPUTED`, and `HEURISTIC` evidence separate. An audited `OPEN_GATE` is a legitimate endpoint when the missing input is precisely identified. Re-running the same route without a genuinely new theorem, dataset, reusable weapon, or literature input is not progress.

## Endpoint remains deferred

The perfect-cuboid population — three integral face diagonals plus an integral space diagonal — remains outside the Stage16-29 numbering. Stage29 synthesizes the population map and identifies the residual obstruction; it does not assume existence or nonexistence of the endpoint.

## Migration note

`docs/stage16-28-population-roadmap.md` remains as the detailed legacy roadmap and policy source for pre-correction material. For any conflict in stage numbering from Stage27 onward, this Stage16-29 document is authoritative. Historical stage artifacts are retained unchanged for audit provenance.