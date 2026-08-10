# Proof-receiver composition boundary

```yaml
ID: TB-WARNING-proof-receiver-composition-boundary
TYPE: WARNING
STATUS: CURRENT
TITLE: Compose receiver savings only across proved handoffs with matching quantifiers
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-08
SOURCE_PR: 417
SOURCE_MERGE_SHA: 29e08fea3ebc1838fde2418957b9c0490456e1b1
SOURCE_FILES:
  - stages/stage14/14-s6-09/result.md
  - stages/stage14/14-s7-07/result.md
  - stages/stage14/14-s7-08/result.md
  - stages/stage14/14-4bv/result.md
```

## INPUT

Two or more valid Stage14 lemmas or savings that one wants to combine.

## OUTPUT

Before composing them, verify all four gates:

```text
1. same counted universe or an explicit injective/majorant transfer,
2. compatible conditioning and no reused automatic factor,
3. source output level equals receiver input level,
4. complementary sectors are exhausted before declaring a whole-family exponent.
```

If any gate is missing, the composition is only a heuristic plan, not a proved saving.

## VARIABLE DICTIONARY

- `source output level` / `receiver input level` refer to the `L0..L8` receiver dictionary.
- `automatic factor` includes gcd/square factors already absorbed into the parametrization.

## USED BY

- Combining local, incidence, genus-one, compact-selector, and square-sieve tools safely.
- Auditing whether a proposed shortcut actually changes the current exponent.

## DO NOT USE FOR

- Do not multiply relative savings from overlapping conditioned events automatically.
- Do not add exponent improvements proved on different non-exhaustive sectors.
- Do not replace an explicit transfer theorem with a plausibility argument.

## PROVENANCE NOTES

The warning packages the quantifier discipline used in the merged s7-08 exhaustive recombination and the earlier fixed-fiber/sector boundaries.