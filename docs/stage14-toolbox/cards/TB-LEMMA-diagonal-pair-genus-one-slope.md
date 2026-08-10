# Diagonal-pair moving slope genus-one quartics

```yaml
ID: TB-LEMMA-diagonal-pair-genus-one-slope
TYPE: LEMMA
STATUS: CURRENT
TITLE: Fixing one diagonal pair puts the opposite reduced slope on a smooth genus-one quartic
SCOPE: MAIN
SOURCE_STAGE: Stage14-4bq
SOURCE_PR: 395
SOURCE_MERGE_SHA: aa21a3604cf72e06f797c8ba2ecff96b49e60f44
SOURCE_FILES:
  - stages/stage14/14-4bq/result.md
  - stages/stage14/14-t22/result.md
```

## INPUT

A merged 4bq normalized good-cell core `(a0,b0,c0,d0)` and pairwise-coprime variables `q11,q12,q21,q22`, with

```text
F=(q12^2*a0*d0)^2-(q21^2*b0*c0)^2,
G=(q22^2*b0*d0)^2-(q11^2*a0*c0)^2,
F*G=square>0.
```

## OUTPUT

Define diagonal products

```text
U=q11*q22,
V=q12*q21,
UV=Q.
```

Fix `(q12,q21)` and the core. With `x=q11`, `y=q22`, reduced slope `t=x/y`, and `W=Y/y^2`, the opposite diagonal lies on

```text
W^2=F0*((b0*d0)^2-(a0*c0)^2*t^4),
F0=F(q12,q21)!=0.
```

Fixing `(q11,q22)` instead gives symmetrically

```text
W^2=G0*((a0*d0)^2*t^4-(b0*c0)^2),
G0=G(q11,q22)!=0.
```

Both are smooth genus-one quartics in the reduced slope.

Because each diagonal pair is coprime, the reduced rational slope uniquely recovers the corresponding integer pair.

## VARIABLE DICTIONARY

- `U,V` = products of the two diagonal pairs in the 4-cell factorization.
- `t=x/y` = reduced slope of the moving diagonal pair.
- `F0,G0` = nonzero value of the detector factor frozen by the opposite diagonal.

## USED BY

- Turning a moving two-variable diagonal into a one-dimensional genus-one rational-point problem.
- Applying the merged bounded-height multiplicity mechanism after one diagonal is fixed.
- Avoiding four independent `q_ij` enumerations in the good-cell residual.

## DO NOT USE FOR

- Do not identify this quartic with the fixed witness curve `C_sigma` in `P^3`.
- The slope-to-integer-pair injection uses pairwise coprimality; without it, scale multiplicity returns.
- Do not apply the quartic formula when `F0=0` or `G0=0`; 4bq treats the good-cell residual with nonzero detector factors.

## PROVENANCE NOTES

Merged PR #395 proves both diagonal quartic normal forms and the reduced-slope injection, importing the bounded-height mechanism already established on the t route.