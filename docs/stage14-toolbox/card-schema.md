# Stage14-toolbox canonical card schema

Each reusable mathematical asset is recorded as one canonical card. Cards are short interfaces to already-proved work; they are not replacements for the source proof.

## Required header

```yaml
ID: TB-<type>-<slug>
TYPE: FORMULA|LEMMA|BOUND|DICTIONARY|RECIPE|LEDGER|WARNING
STATUS: CURRENT|SUPERSEDED|DEPRECATED|PARKED
TITLE: short human-readable title
SCOPE: MAIN|S|BOTH
SOURCE_STAGE: exact Stage14 stage
SOURCE_PR: integer PR number
SOURCE_MERGE_SHA: full merge commit SHA
SOURCE_FILES:
  - repository path
```

## Required mathematical body

Every card must contain these sections.

### INPUT

State all hypotheses needed to use the card. Include normalization, orientation, primitivity, parity, dyadic/height restrictions, local-prime exclusions, and whether a statement is pointwise, averaged, sectoral, cumulative, or fixed-packet.

### OUTPUT

State the exact formula/lemma/bound/dictionary. Preserve quantifiers from the source.

### VARIABLE DICTIONARY

Define every nonstandard symbol used by the card or point to another `CURRENT` dictionary card.

### USED BY

List natural receiver routes/stages. This is advisory; it does not create a proof dependency.

### DO NOT USE FOR

Record the most likely invalid strengthening or quantifier mistake.

Examples:

- local soluble does not imply global soluble;
- coordinate-density saving cannot be multiplied into packet count without a transfer theorem;
- fixed-packet bound is not automatically uniform over moving packets;
- finite diagnostic is not an asymptotic law;
- an `M`-scale exponent is not a `B`-scale exponent until the conversion is stated.

### PROVENANCE NOTES

Explain whether the source statement was later imported, sharpened, or reorganized elsewhere.

## Status-specific fields

### SUPERSEDED

Must add:

```yaml
SUPERSEDED_BY: TB-...
```

The superseding card must exist and normally have `STATUS=CURRENT`.

### DEPRECATED

Must add:

```yaml
DEPRECATED_REASON: precise reason
```

Examples: invalid shortcut discovered later; theorem scope was misread; normalization retired.

### PARKED

Should add:

```yaml
PARK_REASON: no current receiver / specialized branch / waiting for trigger
```

## Optional exact-ledger fields

Bounds and ledgers should prefer exact rationals:

```yaml
EXPONENT_SCALE: M|B|X|other
EXPONENT_EXACT: 41/42
SAVING_EXACT: 1/42
TARGET_EXACT: 1/2
CONVERSION: M<=sqrt(B)
```

If a decimal is useful for readability, it is secondary to the exact rational.

## Source admissibility

Canonical cards require a merged source. `SOURCE_MERGE_SHA` must not be empty.

A toolbox stage may inspect an open PR to identify future maintenance work, but the open PR must not be the only provenance of a canonical card.

## One-card/one-use-case rule

A card should answer one reusable question. If one source proves several logically distinct tools, split them unless the statements are inseparable in practical use.

Conversely, do not create multiple cards merely because the same theorem appears in several historical PRs. Choose one canonical statement and record later import/upgrade history in provenance notes.

## Supersession rule

A stronger statement supersedes an older one only if the normalization and applicable hypotheses are compatible.

For example, a stronger `M`-scale saving does not silently supersede a `B`-scale theorem until the scale conversion is certified. Likewise an unweighted bound does not supersede an arbitrary-weight bound merely because its numerical exponent is stronger.

## Formula verification rule

For algebraic identities, toolbox audits should independently verify representative symbolic/finite cases when feasible. This validation checks transcription and normalization; it is not a substitute for the source proof.

## Card ID stability

`ID` is semantic and stable. Do not encode stage numbers into the ID unless the stage is part of the mathematical meaning. A card may change `STATUS` or provenance metadata without changing ID when its mathematical use case remains the same.
