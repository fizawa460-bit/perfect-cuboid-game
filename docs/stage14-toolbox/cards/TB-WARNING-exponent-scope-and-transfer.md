# Exponent scope and transfer warning

```yaml
ID: TB-WARNING-exponent-scope-and-transfer
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not promote sectoral or structural exponents to whole-family savings
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-4bl/result.md
```

## INPUT

Any Stage14 statement containing an exponent that is one of:

- a whole-family counting exponent;
- an `M`-scale saving;
- a physical `B`-scale saving;
- a sector threshold;
- a sector-only count;
- a coordinate-density saving;
- a forced variable/incidence size;
- a method ceiling or optimization budget.

## OUTPUT

Before combining exponents, classify each one by both **scale** and **quantifier**. Only subtract/add exponents when a merged source proves the relevant transfer.

Canonical examples:

```text
1/21       = current whole local-system saving on M-scale
41/42      = current whole physical upper-bound exponent
10/21      = whole-family post-local saving still required to reach 1/2
20/21      = 4bl sector-only count exponent
1/42       = 4bl saving versus 41/42 on that sector only
41/420     = s6-07 forced variable/incidence scale, not count saving
1/20       = s5 single-edge module ceiling, not current whole-system saving
```

## VARIABLE DICTIONARY

Use the toolbox variable dictionary and the individual bound/ledger cards.

## USED BY

- Every main/s stage that performs exponent arithmetic.
- Toolbox audits and supersession maintenance.

## DO NOT USE FOR

Forbidden shortcuts include:

```text
forced variable >= B^alpha
  => count gains B^-alpha
```

```text
sector count exponent beta
  => whole family count exponent beta
```

```text
coordinate-density saving
  × packet-existence upper bound
```

without a merged transfer theorem.

Also forbidden is treating a smaller numerical fraction as a stronger result when the scales or quantifiers differ.

## PROVENANCE NOTES

Stage14-4bl is a canonical example: it proves a real `1/42` improvement on the small-partner-leg sector while explicitly retaining `FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false`. Stage14-s6-07 provides another current example through a forced positive-power incidence cell without yet proving a full-family saving.
