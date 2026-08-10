# Proved one-cell adaptive sieve cookbook

```yaml
ID: TB-RECIPE-cookbook-one-cell-18-19
TYPE: RECIPE
STATUS: CURRENT
TITLE: Proved one-cell shared-xi adaptive sieve checklist yielding historical 18/19 checkpoint
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-08
SOURCE_PR: 417
SOURCE_MERGE_SHA: 29e08fea3ebc1838fde2418957b9c0490456e1b1
SOURCE_FILES:
  - stages/stage14/14-s7-07/result.md
  - stages/stage14/14-s7-08/result.md
  - stages/stage14/14-4bv/result.md
```

## INPUT

The hard product-square/same-kernel sector after the denominator, square-part, and numerator decomposition, with the exact shared squarefree label retained.

## OUTPUT

The proved checkpoint estimate

```text
V(B) << B^(18/19+o(1))
```

from the exact four-cell factorization, one-cell square-root sieve saving, and exhaustive threshold optimization.

## VARIABLE DICTIONARY

```text
a=r*s
b=t*j
c=r*t
d=s*j
xi=r*s*t*j
lambda=9/19
tau=2/19
theta=8/19
```

## USED BY

- Reusing the one-cell thin receiver inside later architectures such as 4bx.
- Historical comparison with the first post-20/21 one-cell optimum.
- Any future attempt to improve the one-cell thin mechanism itself.

## DO NOT USE FOR

- Do not call `18/19` current after merged 4bx; read the terminal CURRENT ledger.
- Do not multiply two one-cell savings unless a joint two-variable theorem is proved.
- Do not promote a conditional two-cell target to a theorem.

## PROVENANCE NOTES

Merged s7-08 is the canonical first source of the proved `18/19` theorem; later stages may reuse the receiver while superseding its whole-family checkpoint.