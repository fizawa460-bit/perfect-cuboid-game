# Transverse coefficient improvement contract

```yaml
ID: TB-RECIPE-transverse-coefficient-improvement-contract
TYPE: RECIPE
STATUS: CURRENT
TITLE: A genuine transverse gain beyond C^(-1/3) gives a strict improvement below 7/8
SCOPE: BOTH
SOURCE_STAGE: Stage14-4cb
SOURCE_PR: 438
SOURCE_MERGE_SHA: 3fdad0c0673526ea39fed935b4ea69fcaf52a125
SOURCE_FILES:
  - stages/stage14/14-4cb/result.md
```

## INPUT

A theorem that improves the selected adjacent coefficient saving from

```text
C^(-1/3)
```

to

```text
C^(-1/3-eta)
```

for fixed `eta>0` by genuinely transverse information.

## OUTPUT

Merged 4cb gives the shared-label analytic branch

```text
1-gamma*(1/6+eta/2)
```

and exact new crossing

```text
gamma_eta=3/(4+3*eta)
E_eta=(7+3*eta)/(8+6*eta)<7/8.
```

## VARIABLE DICTIONARY

- `eta`: extra coefficient saving beyond the already-proved adjacent two-cell exponent.
- `E_eta`: resulting whole-family exponent after recombination with unchanged support.

## USED BY

- Testing whether a new mean-square/collision theorem produces enough analytic gain to move the main/s ledger.

## DO NOT USE FOR

- Do not manufacture `eta>0` by multiplying the correlated `a` and `b` two-cell estimates.
- Reapplying the current `C^(-1/3)` theorem gives `eta=0` and leaves the barrier at `7/8`.

## PROVENANCE NOTES

The sufficient conversion formula is a merged 4cb result.