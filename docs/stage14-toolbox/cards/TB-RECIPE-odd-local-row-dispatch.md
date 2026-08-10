# Odd bad-prime local row dispatcher

```yaml
ID: TB-RECIPE-odd-local-row-dispatch
TYPE: RECIPE
STATUS: CURRENT
TITLE: Selected and unselected odd bad-prime local rows
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5d
SOURCE_PR: 222
SOURCE_MERGE_SHA: 87c5bec65d36db55de11f07e1d315a640f418673
SOURCE_FILES:
  - stages/stage14/14-s5c/result.md
  - stages/stage14/14-s5d/result.md
```

## INPUT

An odd bad prime `p|SXH`, its actual `S/X/H` role, and whether it occurs in the squarefree support of the covering class.

## OUTPUT

For a selected prime, write `di=p^ei ai` with unit parts `ai`.

```text
SELECTED p|S / 12:
  chi(a1*a2)=+1
  chi(a3)=+1

SELECTED p|X / 13:
  chi(a1*a3)=+1
  chi(-a2)=+1

SELECTED p|H / 23:
  chi(a2*a3)=+1
  chi(a1)=+1
```

Using the product-square unit relation, a convenient compressed form is

```text
S/12 : chi(a3)=+1
X/13 : chi(a2)=+1 AND chi(-1)=+1
H/23 : chi(a1)=+1.
```

For an unselected odd bad prime:

```text
UNSELECTED p|S : chi(d3)=+1
UNSELECTED p|H : chi(d1)=+1
UNSELECTED p|X : chi(d2)=+1 OR chi(-d2)=+1.
```

Thus

```text
p|X, unselected, p==3 mod4 : automatic
p|X, unselected, p==1 mod4 : chi(d2)=+1
p|X, selected               : p must be 1 mod4.
```

## VARIABLE DICTIONARY

- `chi` = Legendre symbol on the indicated p-adic unit part.
- `selected` = `p` occurs in the parity support of the `di`.
- `unselected` = all three `di` are p-adic units at `p`.

## USED BY

- Constructing the complete odd local character system.
- Testing whether a five-column support packet survives all odd local places.
- Explaining special primes such as `p=7`, where the selected/unselected `X` behavior differs sharply.

## DO NOT USE FOR

- Never apply a selected row to an unselected prime.
- Never replace the disjunctive unselected `X` row by the selected `X` row.
- `p==3 mod4` automaticity applies only to the unselected `X` row.
- These are local conditions; they do not imply global solubility or a rational point.

## PROVENANCE NOTES

- Selected rows: merged PR #218.
- Unselected rows and completion of the odd local matrix: merged PR #222.
