# Stage16-28 Repository-Wide Reuse Preflight

Status: **normative preflight for every Stage16-28 main checkpoint**.

## Purpose

The reusable arsenal and numerical reuse index are curated indexes, not a complete inventory of prior research. Strong audited results may remain in stage task files, supplement tracks, archive trees, result bundles, proof files, or historical pull-request descriptions and patches.

Therefore `StageX-main-batch` must search for reusable prior results before opening a new proof, computation, or literature route.

This rule was added after Stage20 recovered progressively stronger already-audited Euler-cuboid results from Stage14-e8 and Stage14-e10 after an initially weaker checkpoint40 ledger had already passed audit. The earlier audit was mathematically valid, but its claim to be the strongest currently certified project bound was incomplete because repository-wide reuse discovery had not been performed first.

## Mandatory search order

For the current checkpoint target, search in this order:

1. canonical arsenal and arsenal indexes;
2. `docs/stage14-num-reuse-index.md` when finite evidence or computation is relevant;
3. frozen final bundles, manifests, and current stage controllers;
4. prior stage result/proof files under `stages/`;
5. supplement and auxiliary tracks, including archived task trees;
6. repository code search for the target population, cutoff, theorem shape, mechanism, and likely synonyms;
7. historical pull requests, including PR body and changed-file patches when repository files are not discoverable by code search;
8. external literature only after repository reuse has been classified.

The arsenal is therefore a fast index, not an exclusive allow-list. Failure to find an item in the arsenal does not justify re-proving it.

## Matching contract

Every candidate prior result must be classified against the current stage contract:

```text
REUSE_POPULATION_MATCH=EXACT|ADAPTER_REQUIRED|NO_MATCH
REUSE_CUTOFF_MATCH=EXACT|ADAPTER_REQUIRED|NO_MATCH
REUSE_MULTIPLICITY_MATCH=EXACT|ADAPTER_REQUIRED|NO_MATCH
REUSE_MEASURE_MATCH=EXACT|ADAPTER_REQUIRED|NO_MATCH
REUSE_QUANTIFIER_MATCH=EXACT|ADAPTER_REQUIRED|NO_MATCH
```

Direct theorem reuse requires exact agreement on all material dimensions or a separately proved adapter. Similar-looking formulas under a different cutoff, primitive convention, symmetry convention, face mask, counting measure, or quantifier are not direct inputs.

## Strongest-known check

Before checkpoint30, 40, 50, 60, or 70 is submitted, the controller must also search for results that strictly strengthen the proposed ledger entry.

Examples:

- a stronger upper bound than the candidate checkpoint40 bound;
- a stronger lower family than the candidate checkpoint50 construction;
- a later supplement that supersedes an earlier local or geometric mechanism;
- a theorem that converts an apparent `OPEN_GATE` into a proved statement;
- a later audited result that changes only the `strongest currently certified` metadata while leaving an older theorem mathematically valid.

If a stronger audited input is found before submission, use it immediately. If it is discovered only after an audit PASS, do not label the old PASS mathematically false when its theorem remains correct. Instead record explicit supersession and re-audit only the strengthened claim or metadata that changed.

## Required handoff

Every `StageX-main-batch` checkpoint submission must emit:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=<IDs/paths/PRs or NONE>
REUSE_MATCH_STATUS=EXACT|ADAPTER_PROVED|MIXED|NO_MATCH
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true|false
NEW_RESEARCH_JUSTIFIED=<reason or NOT_REQUIRED>
```

When computation is proposed, the existing numerical preflight remains additionally mandatory:

```text
NUM_REUSE_CHECK=PASS
...
```

`REPO_REUSE_PREFLIGHT` does not replace `NUM_REUSE_CHECK`; it generalizes reuse discovery to theorem, proof, construction, mechanism, verifier, and historical PR assets.

## Audit rule

The audit lane checks that the preflight was performed whenever a checkpoint claims any of the following:

```text
STRONGEST_CERTIFIED_*
BEST_UPPER_BOUND
BEST_LOWER_BOUND
NO_KNOWN_CONSTRUCTION
NO_KNOWN_THEOREM
OPEN_GATE
NEW_ARITHMETIC_MECHANISM
```

Missing repository-wide reuse discovery does not by itself invalidate a theorem proved in the checkpoint. It does invalidate an unsupported claim that the theorem is the strongest known project result or that no prior project input exists.

## Stop rule

Repository search is bounded discovery, not infinite archaeology. Once the mandatory search surfaces above have been checked with population/cutoff-aware queries and no stronger compatible result is found, record `STRONGEST_KNOWN_CHECK=PASS` and proceed. Repeating the same searches without new input is not required.

## Search-evidence attachment for Stage21–28

Stage21–28 may not satisfy repository-wide reuse preflight with scope names alone. Each checkpoint-specific pass must attach concrete search evidence:

```text
DISCOVERY_CHECKPOINT=
SEARCHED_PATHS=
SEARCH_TERMS=
STRUCTURAL_SIGNATURES=
DEPENDENCY_NEIGHBORS=
CANDIDATES_FOUND=
CANDIDATES_ACCEPTED=
CANDIDATES_REJECTED_WITH_REASON=
POPULATION_ADAPTERS_PROVED=
DISCOVERY_LEDGER_STATUS=COMPLETE|INCOMPLETE
```

When `REUSE_MATCH_STATUS=NO_MATCH`, the rejected-candidate ledger is mandatory. When a candidate is accepted only after an adapter, the exact population/cutoff/multiplicity/measure/quantifier map must be named. An empty candidate result is credible only when searched paths, synonyms, structural signatures, and dependency neighbors are all recorded.

### Stage14/15 bound-attack ledger

Before a Stage21–28 checkpoint asserts a strongest upper/lower bound, absence of a compatible construction, a new mechanism, or an `OPEN_GATE`, it must search `docs/stage14-15-bound-attack-map.md` and the complete sharded ledger under `docs/stage14-15-bound-attack-ledger/`.

The consumer must record accepted and rejected `S1415-ATTACK-*` IDs. Entries with `review_required=true`, especially `UNCLASSIFIED`, `PARTIAL`, or `BLOCKED` outcomes, must receive targeted source reading before a claim that no prior project route applies. Automatic classifications are discovery hints only and never replace population/cutoff/multiplicity/measure/quantifier or audit checks.
