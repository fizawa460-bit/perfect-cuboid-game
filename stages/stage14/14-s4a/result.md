# Stage14-s4a — full active arithmetic fingerprint census

## Purpose

Stage14-s4a is independent of the unresolved main Kummer classification. It freezes a uniform arithmetic record for every active primitive oriented first face through the exact Stage14 ceiling `B=2,000,000`.

The census is intended as the comparison substrate for later `14-4aj+` higher-degree/rank-jump strata and for Stage14-s4b clustering.

## Record contract

For every active face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

the record contains:

- exact first physical height `mu(F)` and the first partner face;
- Euclid half-angle `r=X/(H+S)`;
- `omega(2SXH)`;
- the actual first-hit elliptic point on
  \[
  W^2=Z(Z-S^2)(Z+X^2);
  \]
- its canonical height from PARI `ellheight`;
- exact Kummer square classes of
  \[
  (Z, Z-S^2, Z+X^2);
  \]
- unconditional `ellrank(E,0)` lower/upper bounds;
- Cassels-pairing term `s`, full-2-torsion Selmer dimension `r2+2+s`, and root number.

Kummer square classes are represented by signed squarefree integer representatives. Selmer dimension is never identified with Mordell--Weil rank unless the independent rank bounds certify equality.

## Scope

This stage does **not** assume or require an `M`-degree-four bisection. It does not classify higher-degree Kummer curves, prove that any fingerprint cluster comes from an algebraic multisection, or prove the observed `sqrt(B)` growth law.

Its role is to make all 490 currently active vertices immediately comparable to whatever geometric strata the main track produces.

## Decision

```text
STAGE14_S4A=COMPLETE_FULL_ACTIVE_ARITHMETIC_FINGERPRINT_CENSUS
ALL_ACTIVE_VERTICES_FINGERPRINTED=true
ACTIVE_VERTEX_COUNT=490
FIRST_HIT_POINTS_RECONSTRUCTED_EXACTLY=true
KUMMER_SQUARE_CLASSES_RECORDED=true
PARI_RANK_SELMER_ENVELOPE_RECORDED=true
CANONICAL_HEIGHT_RECORDED=true
BISECTION_CLASSIFICATION_REQUIRED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s4b cluster active arithmetic fingerprints / compare with higher-degree strata
```

## Artifacts

```text
stages/stage14/scripts/14-s4a/active_fingerprint_census.py
stages/stage14/data/14-s4a/active_fingerprint_census.json
.github/workflows/stage14-s4a-active-fingerprint.yml
```
