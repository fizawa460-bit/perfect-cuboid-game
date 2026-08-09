# Stage13-13fj — Claude R05 verdict

```text
PROVENANCE=USER_RELAYED_EXTERNAL_REVIEW
REVIEWER=Claude
TARGET_BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R05
TARGET_CONTENT_SHA256=4214a6e3621b52ce39373799b48fc8325351f650514e732d6e2244d28d475458
RECORDED_VERDICT=OPEN
OBJECTION_LEVEL=THEOREM_LEVEL_EXTERNAL_BOUNDARY
COUNT_AS_INDEPENDENT_CLOSED_R05_VERDICT=false
SUBSTANTIVE_REPAIR_REQUIRED=TO_BE_DETERMINED
R05_IMMUTABLE=true
```

## Reviewer conclusion

Claude independently recalculated the numerical Wiener and box-accounting portions and found them internally consistent, but explicitly concluded that calling R05 `CLOSED` is premature while the H1/H2 Gaussian-Hecke external citation boundary remains unverified.

## Independently verified arithmetic

Claude reports successful independent checks of:

- `||a||_rho <= (8/3) rho` from the Poisson-kernel coefficients;
- `||b||_rho <= (44/9) rho` via the Chebyshev-U series;
- `||M||_rho <= (32/9) rho^2` under the reconstructed intended mixed-part definition;
- `||E_vartheta||_rho <= (17744/243) rho^2`, with numerator decomposition `1728+6336+5808+3872=17744`;
- `||C_vartheta-1||_rho <= (3465625/6561) rho^2 < 529 rho^2`;
- Gate-C exponent bookkeeping: `Lambda^(2-N)=Lambda^-62`, `O(Lambda^27)` boxes, total `Lambda^-35`, and stretched-exponential power-tail saving;
- Gate-D harmonic aggregation exponent `Lambda^(4 C_H + D_H + 6)`;
- SHA-256 formatting in the bundle.

These checks materially strengthen the internal arithmetic evidence for Gates B--D.

## Recorded objections

### 1. Mixed-part definition `M` not explicit enough

The reviewer says the canonical text describes `M` only as the positive-height/base mixed part. Reproducing the `32/9` constant required reconstructing the intended one-side mixed term from the later formula. The definition should be written explicitly so the bound is locally verifiable without reverse engineering.

Classification:

```text
M_DEFINITION_EXPLICITNESS_DEFECT=true
M_DEFINITION_DEFECT_LEVEL=PRESENTATION_OR_LOCAL_PROOF_EXPLICITNESS
```

### 2. H1/H2 Gaussian-Hecke citation boundary not independently verified

The reviewer did not verify directly from Huang--Liu--Rudnick §2.1 and Merikoski §2.7 that the exact family used here, in particular `k=8 ell` for every `ell>=1` and the relevant fixed twists, has the proof-facing analytic continuation / functional equation / no-pole-at-s=1 properties required by R05.

Because this boundary underlies nonzero harmonic cancellation and the fixed-S nonprincipal pole-loss mechanism, Claude treats the unresolved citation verification as theorem-level for freeze purposes.

```text
HECKE_H1_H2_PRIMARY_SOURCE_VERIFICATION_REQUIRED=true
HECKE_H1_H2_OBJECTION_LEVEL=THEOREM_LEVEL_EXTERNAL_BOUNDARY
```

### 3. Why `p>=7` in the inert contraction should be explicit

The reviewer notes that

```text
lambda_3=(3+5)/(2(3+1))=1,
```

so `p=3` gives no contraction and must be excluded from the `(3/4)^k` squeeze. The proof uses inert primes `p>=7` correctly, but should explicitly state this reason.

```text
P3_DEGENERACY_EXPLICITNESS_REQUIRED=true
```

### 4. Finite-data wording should be stronger

The reviewer agrees the `100k -> 5m` data do not contradict the asymptotic theorem, but stresses that the logarithmic range is too short to provide meaningful evidence of convergence either. The R05 text already denies an effective convergence-rate claim; Claude recommends stating equally clearly that the finite trajectory is not positive evidence for the limiting ratio.

```text
FINITE_DATA_IS_NOT_CONVERGENCE_EVIDENCE=true
```

## Overall classification

The numerical/Wiener objections that motivated part of the R05 repair are substantially closed by independent recalculation. However, the external Gaussian-Hecke theorem interface has not been independently source-verified in this review, and Claude explicitly declines `CLOSED` on that basis.

```text
VERDICT=OPEN
THEOREM_LEVEL_OBJECTION=true
PROMOTE_TO_13_13G=false
R05_REPAIR_OR_EXTERNAL_BOUNDARY_CLOSURE_AUDIT_REQUIRED=true
```
