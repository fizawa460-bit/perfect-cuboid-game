# Dispatch a physical pair through compact half-angle selectors

```yaml
ID: TB-RECIPE-dispatch-compact-half-angle-physical
TYPE: RECIPE
STATUS: CURRENT
TITLE: Route a physical pair through dual compact torsion and half-angle selectors
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-4bl/result.md
```

## INPUT

A physical two-face pair with partner half-angle roots `s,t` and dual compact selectors `D_+,D_-`.

## OUTPUT

Use

```text
D_+ k_+=s,
D_- k_-=t,
Q=D_+D_-,
K=k_+k_-,
QK=X2/kappa.
```

Then route odd good prime powers into the exact four-cell gcd matrix

```text
D_- -> q-+
k_- -> q--
D_+ -> q+-
k_+ -> q++
```

and choose the receiver associated with denominator size, cancellation size, or shared half-angle incidence.

## VARIABLE DICTIONARY

- `D_±` = compact reduced denominator roots.
- `k_±` = complementary cancellation cofactors.
- `q**` = deterministic good-odd gcd cells.

## USED BY

- Physical same-edge incidence arguments.
- Denominator/cancellation dichotomies.
- Translating torsion formulas into half-angle arithmetic.

## DO NOT USE FOR

- The four cells are not independent Bernoulli samples.
- A large cell is structural until a counting receiver consumes it.
- Do not identify `D_±` with generic witness `D` or abstract `D_min`.

## PROVENANCE NOTES

Merged 4bl combines the two compact selectors and their exact product identity; merged s6-07 supplies the gcd-cell allocation.