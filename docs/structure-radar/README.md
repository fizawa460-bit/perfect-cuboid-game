# StructureRadar controller

```text
PROGRAM=STRUCTURE_RADAR
PRIMARY_OPERATOR=ChatGPT
CANONICAL_MAIN_COMMAND=StructureRadar-main-batch
CANONICAL_AUDIT_COMMAND=StructureRadar-audit
CORPUS_SCOPE=ALL_MERGED_STAGES_AND_FUTURE_STAGE_DIRECTORIES
STAGE14_15_ROLE=HIGH_PRIORITY_BOOTSTRAP_CORPUS_NOT_SCOPE_BOUNDARY
```

StructureRadar turns mathematical structures already present in this repository
into normalized mathematical names, English search terms, theorem species, and
perfect-cuboid weapon decisions.  It is a recurring discovery program, not a
one-shot claim that every useful theorem has been found.

## Canonical inputs

The source manifest is rebuilt from tracked files on the checked-out merged
branch.  It always includes:

- the project-wide research arsenal and every stage arsenal/promotion file;
- every tracked Markdown and machine-readable JSON contract/report under `docs/`
  and `stages/`, including `result.md`, supporting proofs, toolbox cards,
  computational reports, Stage26, Stage27, and future `stages/stageNN`
  directories;
- the Stage14/15 attack map and deep-review queue;
- the complete Stage14 q-research literature radar;
- stage roadmaps and top-level stage controllers as lower-evidence context.

Stage14/15 is deliberately a high-priority bootstrap corpus because it contains
the large historical attack ledger.  It is not an allow-list.  A newly merged
Stage26, Stage27, or future-stage result must enter the manifest without a schema
or prompt change.  Unmerged PR heads are excluded until merged; a main batch may
cite an open PR separately, but it cannot silently treat it as canonical input.

Generated data, scripts, workflows, and HTML copies are not primary census inputs;
their mathematical Markdown/JSON sources are.  `scripts/structure_radar.py
refresh` rebuilds the manifest, queue, and controller.
The manifest records a content fingerprint for each source, so new and changed
files return to the queue while unchanged reviewed sources remain reviewed.
`source-manifest.json` is the compact index; its `parts` field points to bounded
machine-readable shards under `source-manifest/` so the full corpus remains easy
to diff and transport.

## Structure card contract

`structure-registry.json` is the mathematical registry.  Each non-draft card must
contain at least:

```text
STRUCTURE_ID
CANONICAL_MATH_NAME
EXACT_EQUATIONS_OR_OBJECT
SEARCH_TERMS_PRIMARY
SEARCH_TERMS_ALIASES
THEOREM_SPECIES
REPO_PROVENANCE=(source_id,path,locator,fingerprint)
TARGET_POPULATIONS
POTENTIAL_WEAPON_TYPES
APPLICABILITY_GAPS
EXISTING_RADAR_OVERLAP
SEARCH_STATUS
ARSENAL_DECISION
```

Equivalent notation is deduplicated by mathematical object and hypotheses, not
by spelling.  A changed population, cutoff, measure, multiplicity, quantifier, or
height is a distinct applicability profile even when the displayed equation is
the same.

Allowed arsenal decisions are:

- `ACTIVE`: audited and currently reusable for an exact receiver;
- `PARKED`: valid, but specialized or without a current receiver;
- `EXTERNAL_GATE`: a precise missing theorem/adapter with a falsifiable test;
- `REJECTED`: tempting but incompatible, superseded, or disproved for the stated
  receiver.

`ACTIVE` is never awarded from vocabulary similarity.  A literature lead must
record its exact theorem, variable dictionary, verified and unverified
hypotheses, quantitative loss, source URL/identifier, and smallest repo-native
transfer test.

## `StructureRadar-main-batch`

On each invocation ChatGPT must:

1. run or conceptually reproduce `structure_radar.py refresh` on current merged
   main and read `controller.json`;
2. consume the current `READY` source-census or structure-search work unit;
3. normalize new structures and merge genuine duplicates without erasing their
   provenance;
4. generate primary and alias search terms in English plus theorem-species terms;
5. check the existing q-ledger and research arsenal before opening web research;
6. search primary literature when the queue phase requires it, then test exact
   perfect-cuboid applicability;
7. update `progress.json`, `structure-registry.json`, and any arsenal proposal;
8. refresh again and submit a Draft PR with the batch state.

A single invocation may consume several small work units, but it must not mark
unread sources reviewed.  Source census, normalization, literature search, and
weapon classification are separate evidence transitions.

The controller reports a range rather than promising a fixed number of chats.
For the initial corpus, one main invocation should normally consume three to six
compatible source tasks; materially new cards still force an audit boundary.

Minimum main-batch handoff:

```text
MAIN_BATCH_STATUS=SUBMITTED|BLOCKED|COMPLETE
CORPUS_FINGERPRINT=
TASKS_CONSUMED=
SOURCES_REVIEWED=
STRUCTURES_ADDED=
STRUCTURES_DEDUPED=
SEARCHES_COMPLETED=
ARSENAL_DECISIONS=
ARSENAL_BACKFLOW_GAPS=
CODEX_REQUIRED=true|false
CODEX_REASON=
AUDIT_REQUIRED=true|false
NEXT_EXPECTED_COMMAND=StructureRadar-audit|StructureRadar-main-batch|human-input
```

## `StructureRadar-audit`

Audit is independent and batch-scoped.  It checks source coverage, equation and
provenance accuracy, deduplication, search-term quality, literature citations,
population/height compatibility, and over-promotion.  A PASS certifies the
submitted batch; it does not claim globally exhaustive literature coverage and
does not close the campaign while another queue item is ready.

Minimum audit output:

```text
AUDIT_VERDICT=PASS|FAIL|BLOCKED
AUDITED_TASKS=
SOURCE_COVERAGE_AUDIT=PASS|FAIL
STRUCTURE_NORMALIZATION_AUDIT=PASS|FAIL
LITERATURE_APPLICABILITY_AUDIT=PASS|FAIL|NOT_APPLICABLE
ARSENAL_PROMOTION_AUDIT=PASS|FAIL|NOT_APPLICABLE
CAMPAIGN_CLOSE_ALLOWED=true|false
CODEX_REQUIRED=true|false
CODEX_REASON=
NEXT_EXPECTED_COMMAND=StructureRadar-main-batch|StructureRadar-audit|human-input
```

## Codex boundary

Routine source reading, mathematical normalization, literature search, transfer
analysis, and arsenal judgment remain ChatGPT work.  Delegate to Codex only for:

- extractor or verifier failure;
- manifest/progress inconsistency;
- a large deterministic re-index or migration;
- conflicting provenance mappings that need repository-wide mechanical repair;
- CI/workflow failure.

Codex output never self-certifies a mathematical or literature claim.

## Stop and close conditions

A batch stops for audit after material new cards or weapon decisions.  It may
also stop on a precise external theorem gate, a population-contract conflict, or
a human policy choice.  "Many files exist" and "the previous search found no
direct theorem" are not valid close conditions.

The initial campaign may close only when all current source fingerprints are
reviewed, all normalized cards have a completed or explicitly deferred search
state, dedup conflicts are resolved, all weapon decisions are audited, no arsenal
backflow gap is unclassified, and a final independent audit passes.  Closure is
always relative to the recorded corpus fingerprint and search date.  Later
merged/changed sources automatically reopen delta work; a full census is needed
again only after a schema change or an explicit audit finding that invalidates
the previous extraction partition.
