# Sector-to-whole-family warning

```yaml
ID: TB-WARNING-sector-to-whole-family
TYPE: WARNING
STATUS: CURRENT
TITLE: A sector bound changes the whole-family exponent only after complementary sectors close
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-4bl/result.md
```

## INPUT
A power-saving estimate proved on a restricted branch, size range, or structural sector.

## OUTPUT
Record the estimate as sector-only until all complementary branches have bounds at least as strong. The whole-family exponent is the maximum surviving branch exponent.

## VARIABLE DICTIONARY
- sector = subset defined by a split such as small partner leg, large denominator, or large cancellation.
- whole family = union of all physical branches.

## USED BY
- Exponent bookkeeping and recombination.

## DO NOT USE FOR
- Do not replace the global exponent by a stronger sector exponent.
- Do not ignore a complementary branch whose exponent is larger.

## PROVENANCE NOTES
4bl proves a genuine `20/21` small-partner-leg sector while explicitly refusing to promote it to a full-family exponent at that stage.