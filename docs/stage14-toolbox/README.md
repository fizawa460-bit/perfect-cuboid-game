# Stage14-toolbox — reusable research infrastructure for Stage14 main/s

## Purpose

`Stage14-toolbox` is a permanent research-infrastructure track for the Stage14 `14-4` main route and the `s` route.

It does **not** own a new proof strategy. Its job is to make already-proved mathematics easier, safer, and faster to reuse:

```text
merged proof result
-> extract reusable formula / lemma / dictionary / bound / warning
-> normalize hypotheses and notation
-> record exact provenance
-> mark the strongest current version
-> keep supersession history
-> expose a short reusable card
```

The toolbox is deliberately useful even when `14-4` and `s` are stalled, moving in parallel, or temporarily inactive. It may continuously mine older merged work for buried reusable assets.

## Stage numbering

Toolbox stages use spreadsheet-style two-letter lowercase codes:

```text
aa, ab, ac, ... az, ba, bb, ... bz, ca, ... zz
```

`aa` is the foundation stage. There is no preallocated `aa..az` mathematical roadmap.

After each completed toolbox stage, the next stage is the lexicographic spreadsheet successor. The next stage chooses one coherent maintenance theme from the highest-value unprocessed reusable asset.

Examples:

```text
aa -> ab
az -> ba
bz -> ca
```

Do not create substage suffixes such as `aa1` merely because one topic is large. Split only by advancing the normal two-letter sequence.

## Independence contract

Toolbox progression must not require a future result from `14-4` or `s`.

Allowed work when no new proof PR has merged:

- extract formulas and lemmas from old merged PRs;
- reconcile notation across historical stages;
- replace stale bounds with stronger merged bounds;
- add `DO_NOT_USE_FOR` warnings to prevent known misapplications;
- build variable dictionaries and conversion chains;
- build exact exponent ledgers;
- assemble proof recipes from already-proved components;
- add deterministic audits for reusable identities;
- identify duplicate statements and choose one canonical card.

A new merge may create new toolbox work, but it is never required for the toolbox to continue.

```text
TOOLBOX_REQUIRES_FUTURE_MAIN_RESULT=false
TOOLBOX_REQUIRES_FUTURE_S_RESULT=false
TOOLBOX_CAN_MINE_HISTORICAL_MERGED_RESULTS=true
```

## Source policy

A card marked `CURRENT`, `SUPERSEDED`, or `DEPRECATED` must be grounded in merged repository work.

Every mathematical card records at least:

```text
SOURCE_STAGE
SOURCE_PR
SOURCE_MERGE_SHA
```

Open/draft PRs may be mentioned only in a noncanonical maintenance note and may not become the provenance of a canonical card.

Toolbox extraction must not silently strengthen a source theorem. If the source proves only an upper bound, finite diagnostic, one-sided implication, regular-box statement, or sectoral saving, the card must preserve that scope exactly.

## Canonical card types

The canonical types are:

- `FORMULA` — exact algebraic identity or transformation;
- `LEMMA` — reusable implication with hypotheses;
- `BOUND` — asymptotic, incidence, height, or counting bound;
- `DICTIONARY` — exact correspondence between route notations/objects;
- `RECIPE` — ordered use of already-proved ingredients;
- `LEDGER` — exact exponent/constant dependency calculation;
- `WARNING` — known invalid shortcut, quantifier mismatch, or theorem boundary.

A stage may add multiple cards only when they form one coherent reusable module.

## Card status

Canonical statuses are:

- `CURRENT` — preferred reusable statement;
- `SUPERSEDED` — valid but a stronger/current card should normally be used;
- `DEPRECATED` — historically present but should not be used for new work;
- `PARKED` — valid specialized tool with no current receiver.

`SUPERSEDED` cards must point to `SUPERSEDED_BY`.

`DEPRECATED` cards must include a reason.

No card is deleted merely because a stronger result appears. The toolbox preserves the upgrade chain.

## Canonical card fields

See `card-schema.md`. At minimum each card answers:

```text
WHAT is the reusable statement?
INPUT: exactly when may it be applied?
OUTPUT: exactly what does it give?
SOURCE: where was it proved?
STATUS: is it the current strongest form?
USED_BY: main / s / both?
DO_NOT_USE_FOR: what tempting misuse is forbidden?
```

## File layout

```text
docs/stage14-toolbox/
  README.md
  card-schema.md
  card-template.md
  index.json
  cards/
    ... future canonical cards ...

stages/stage14/14-toolbox-XX/result.md
stages/stage14/scripts/14-toolbox-XX/
.github/workflows/stage14-toolbox-XX.yml
```

`index.json` is the machine-readable canonical registry. Human-readable cards live under `cards/` once extraction begins.

## Selection rule for each new stage

At the start of each toolbox stage:

1. inspect the canonical toolbox index;
2. inspect merged `14-4` / `s` history and recent upgrades;
3. list unprocessed or stale reusable assets;
4. choose one theme maximizing:
   - reuse frequency,
   - risk of notation/provenance mistakes,
   - risk of accidentally using a superseded bound,
   - cross-route value;
5. normalize and audit that theme;
6. update the canonical index;
7. set `NEXT` to the next two-letter code.

Do **not** block because the current main/s stage is waiting on a theorem.

## Anti-duplication with proof routes

Toolbox may reorganize, verify, cross-reference, and package a proved result. It must not claim a theorem not already proved by the source route.

If extraction exposes a genuine missing lemma, record it as a gap/warning and hand it back to the owning proof route. Do not quietly prove a new main theorem under a toolbox stage unless the user explicitly changes the toolbox charter.

```text
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
TOOLBOX_MAY_EXPOSE_GAPS=true
TOOLBOX_MAY_REPACKAGE_PROVED_RESULTS=true
```

## Current strongest-version rule

When several valid cards address the same use case:

1. prefer the strongest merged theorem whose hypotheses fit;
2. preserve older cards as `SUPERSEDED` if they remain mathematically valid;
3. never compare exponents without first confirming identical scale/normalization;
4. record conversions such as `M`-scale to physical `B`-scale explicitly;
5. exact rational exponents are preferred over decimals.

## Safety locks

- no finite `T(B)=0` -> nonexistence inference;
- no numerical p-value -> theorem promotion;
- no open PR -> canonical theorem card;
- no unproved converse;
- no local-solubility -> global-solubility reversal;
- no coordinate-density saving -> packet-existence saving without a proved transfer;
- no silent reuse of superseded exponents;
- no notation substitution unless the dictionary hypotheses are explicit.

## Bootstrap queue

This is **not** a fixed roadmap. It is only an initial value ordering and may be reprioritized after every merge.

Likely high-value early themes include:

- cross-route variable/normalization dictionary;
- current exponent and saving ledger;
- Pythagorean/Euclid conversion formulas;
- local 2-descent / five-column interface;
- integral global-small-point witness formulas;
- odd kernel edge packet / full-radical incidence tools;
- two-quadrics / genus-one geometry;
- compact torsion / denominator / half-angle identities;
- quantifier-mismatch and invalid-shortcut warning library.

The foundation selects the first concrete extraction theme as:

```text
NEXT=Stage14-toolbox-ab cross-route variable and normalization dictionary
```

This choice is intentionally useful regardless of how far `14-4` or `s` advances before `ab` starts.
