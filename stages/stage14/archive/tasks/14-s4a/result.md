# Stage14-s4a — full active arithmetic fingerprint census

## Purpose

Stage14-s4a is independent of the main Kummer classification. It freezes a uniform arithmetic fingerprint for every active primitive oriented first face through the exact Stage14 ceiling `B=2,000,000`.

The full 490-row census is regenerated deterministically in CI and uploaded as an artifact; a compact exact summary is committed in the repository and checked against every regeneration.

## Record contract

For every active face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

the generated record contains exact first physical height `mu(F)` and partner, Euclid half-angle `r=X/(H+S)`, `omega(2SXH)`, the actual first-hit elliptic point on

\[
W^2=Z(Z-S^2)(Z+X^2),
\]

its canonical height, exact Kummer square classes of `(Z,Z-S^2,Z+X^2)`, unconditional PARI `ellrank(E,0)` lower/upper bounds, Cassels-pairing term `s`, full-2-torsion Selmer dimension `r2+2+s`, and root number.

Selmer dimension is never identified with Mordell--Weil rank without independent certification, and the first-hit point is not assumed to be a generator or height minimum.

## Full-census findings

```text
active vertices                         490
mu range                                697 .. 1,990,997
canonical height min                    1.1987017557
canonical height median                 3.8736557739
canonical height mean                   3.8795332950
canonical height max                    6.5242571012
mean hhat/log(mu)                       0.3102761746
omega(2SXH) min / mean / max            4 / 8.8244897959 / 13
```

PARI rank-bound census:

```text
1..1   254
2..2   188
0..2    15
1..3    10
3..3    22
4..4     1
```

Thus `475/490` active fibers already have positive Mordell--Weil rank certified at `ellrank` effort zero, and `465/490` have an exact rank certified there. Every one of the 490 has 2-Selmer dimension strictly beyond the rational 2-torsion baseline.

The most useful structural diagnostic is the Kummer-class diversity:

```text
distinct exact Kummer square-class triples = 483 / 490
maximum observed multiplicity              = 2
```

So the finite active population is **not** concentrated in a handful of literally identical full-2-descent square-class triples. Any meaningful Stage14-s4b clustering must therefore coarsen the arithmetic data (prime-support patterns, rank type, height profile, symmetry/orbit data, or future higher-degree geometric labels) rather than grouping by exact Kummer-class equality alone.

This remains finite arithmetic structure, not an asymptotic theorem.

## Scope

This stage does not require an `M`-degree-four bisection. It does not classify higher-degree Kummer curves, prove that any coarse fingerprint cluster comes from an algebraic multisection, or prove the observed `sqrt(B)` growth law.

## Decision

```text
STAGE14_S4A=COMPLETE_FULL_ACTIVE_ARITHMETIC_FINGERPRINT_CENSUS
ALL_ACTIVE_VERTICES_FINGERPRINTED=true
ACTIVE_VERTEX_COUNT=490
FIRST_HIT_POINTS_RECONSTRUCTED_EXACTLY=true
KUMMER_SQUARE_CLASSES_RECORDED=true
PARI_RANK_SELMER_ENVELOPE_RECORDED=true
CANONICAL_HEIGHT_RECORDED=true
EXACT_KUMMER_CLASS_TRIPLES=483_OF_490_DISTINCT
BISECTION_CLASSIFICATION_REQUIRED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s4b cluster active arithmetic fingerprints / compare with higher-degree strata
```

## Artifacts

```text
stages/stage14/scripts/14-s4a/active_fingerprint_census.py
stages/stage14/data/14-s4a/active_fingerprint_summary.json
.github/workflows/stage14-s4a-active-fingerprint.yml
```

CI additionally uploads the full generated `active_fingerprint_census.json` as `stage14-s4a-active-fingerprint-census`.
