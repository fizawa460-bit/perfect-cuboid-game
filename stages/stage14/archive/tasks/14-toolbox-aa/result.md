# Stage14-toolbox-aa — permanent reusable research toolbox foundation

## Purpose

Create a durable infrastructure track for reusable Stage14 `14-4` / `s` formulas, lemmas, bounds, dictionaries, recipes, exponent ledgers, and warnings.

This stage intentionally does not extract a large batch of mathematical cards. It freezes the registry/schema/numbering/provenance system first so later toolbox stages can mine historical merged work safely and indefinitely.

## Core decision

The toolbox uses spreadsheet-style two-letter lowercase numbering:

```text
aa, ab, ... az, ba, bb, ... zz
```

There is no fixed mathematical roadmap. Each stage selects one coherent high-value maintenance theme from unprocessed or stale merged assets.

Therefore toolbox progress does not depend on a future `14-4` or `s` result.

## Permanent role

```text
merged Stage14 asset
-> reusable card
-> explicit hypotheses
-> exact output
-> variable dictionary
-> source PR + merge SHA
-> CURRENT / SUPERSEDED / DEPRECATED / PARKED
-> DO_NOT_USE_FOR warning
```

The track owns research infrastructure, not a new Stage14 theorem.

## Canonical card types

```text
FORMULA
LEMMA
BOUND
DICTIONARY
RECIPE
LEDGER
WARNING
```

## Canonical statuses

```text
CURRENT
SUPERSEDED
DEPRECATED
PARKED
```

Older valid formulas are not deleted when sharpened. A compatible stronger statement creates a supersession chain. Bounds with different hypotheses/scales are not compared merely by exponent size.

## Provenance gate

Canonical mathematical cards must come from merged repository work and record:

```text
SOURCE_STAGE
SOURCE_PR
SOURCE_MERGE_SHA
SOURCE_FILES
```

Open PRs may inform future maintenance but cannot be the sole canonical theorem source.

## Safety / misuse library

The foundation explicitly forbids the common Stage14 failure modes:

- finite `T(B)=0` -> nonexistence;
- p-value -> theorem;
- local solubility -> global solubility;
- coordinate-density saving -> packet-existence saving without transfer;
- silent `M`-scale / `B`-scale confusion;
- silent reuse of a superseded exponent;
- notation substitution without exact normalization hypotheses.

## Independence from current progress

The toolbox can keep working even if both proof routes stop. Historical tasks include:

- variable and normalization dictionaries;
- old-to-current bound upgrades;
- Pythagorean/Euclid conversion chains;
- 2-descent/five-column interfaces;
- witness and kernel-packet formula extraction;
- genus-one/two-quadrics recipes;
- compact torsion/denominator identities;
- invalid-shortcut warnings;
- exact exponent ledgers and deterministic transcription audits.

## Foundation artifacts

```text
docs/stage14-toolbox/README.md
docs/stage14-toolbox/card-schema.md
docs/stage14-toolbox/card-template.md
docs/stage14-toolbox/index.json
stages/stage14/scripts/14-toolbox-aa/toolbox_foundation_audit.py
.github/workflows/stage14-toolbox-aa.yml
```

## First extraction theme

The nonbinding bootstrap queue begins with the highest cross-route reuse/risk target:

```text
Stage14-toolbox-ab
cross-route variable and normalization dictionary
```

This remains useful even if `14-4` or `s` has advanced several stages before `ab` begins.

## Boundary

```text
STAGE14_TOOLBOX_AA=COMPLETE_PERMANENT_REUSABLE_RESEARCH_TOOLBOX_FOUNDATION
TOOLBOX_NUMBERING=TWO_LETTER_SPREADSHEET_AA_TO_ZZ
FIXED_MATHEMATICAL_ROADMAP=false
ONE_COHERENT_THEME_PER_STAGE=true
CANONICAL_CARDS_REQUIRE_MERGED_SOURCE=true
OPEN_PR_CANONICAL_SOURCE=false
CURRENT_SUPERSEDED_DEPRECATED_PARKED_STATUS_SYSTEM=true
SUPERSESSION_HISTORY_PRESERVED=true
TOOLBOX_REQUIRES_FUTURE_MAIN_RESULT=false
TOOLBOX_REQUIRES_FUTURE_S_RESULT=false
TOOLBOX_CAN_MINE_HISTORICAL_MERGED_RESULTS=true
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
TOOLBOX_MAY_EXPOSE_GAPS=true
TOOLBOX_MAY_REPACKAGE_PROVED_RESULTS=true
NEXT=Stage14-toolbox-ab cross-route variable and normalization dictionary
```
