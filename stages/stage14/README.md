# Stage14 — exactly-two integral-face population

Current canonical source: `stages/stage14/main.md`.

Reusable Stage14 tools and audited no-go results are indexed in `docs/stage14-arsenal.md`; use `docs/stage14-arsenal-index.md` for obstruction-shape lookup and `docs/stage14-arsenal-stage15-map.md` for Stage15 promotion guards.

```text
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
STAGE14_4AO=COMPLETE_FULL_LOCAL_MATRIX_AND_HEIGHT_WEIGHTED_COUNTING_INTERFACE
STAGE14_4AP=LOCAL_CHARACTER_REACH_AND_CONDITIONAL_GLOBAL_HEIGHT_TRANSFER_BOUNDARY
MAX_VERIFIED_B=2000000
FULL_RANK_SELMER_CENSUS_MAX_H=20000
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=true
FULL_LOCAL_SELMER_MATRIX_COMPLETE=true
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true
LOCAL_LARGE_SIEVE_ALONE_CONTROLS_HEIGHT_WEIGHTED_COUNT=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4aq isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve
```

## Current reduction

For a primitive oriented Pythagorean base `F=(S,X,H)`,

\[
E_F:Y^2=Z(Z-S^2)(Z+X^2)
\]

has full rational 2-torsion. The fixed rational-curve square-root mechanism is closed by 4ak, so the count is collective.

Stage14-4am separates

```text
A ⊇ Sigma ⊇ R ⊇ V,
V/A=(Sigma/A)(R/Sigma)(V/R).
```

At `H<=20,000`:

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.81748
V/R in [0.01274,0.01427]
```

so the dominant finite thinning is after positive rank, at the first-small-point gate.

## 4an

Using the global square-class relation, the selected s5c rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Hence a selected odd `X`-prime must have `p=1 mod 4`.

Merged s5d supplies the unselected odd rows

```text
p|S : chi_p(d3)=+1
p|H : chi_p(d1)=+1
p|X : chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

Therefore **all odd bad-prime local rows are explicit** and reduced to reciprocity bits.

The complete `H<=20,000` support audit gives

```text
selected-row mean surviving support fraction       0.1695801
selected-row bases with no nonempty support        0
complete-odd mean surviving support fraction       0.04556219
complete-odd mean surviving supports                4.09149
bases with no nonempty homogeneous odd support     779
```

The last number is only a homogeneous odd-only diagnostic, not a Selmer base count. The remaining local gap is covering-specific `Q_2` solubility. Merged s5d reduces the product-square `Q_2` state space to 64 states.

The character matrix remains an `A -> Sigma` local interface; it does not control `Sigma -> R` or the height-sensitive `R -> V` gate.

## 4ao, 4ap, and next

Merged s5f leaves exactly 8 covering-soluble `Q_2` states among the 64 product-square states. Stage14-4ao combines this with 4an, records the exact finite full-local gate `Sigma/A=5209/6372`, and formulates a base-counted descent object retaining global solubility and the s3 logarithmic height window.

Stage14-4ap imports the s5g centering obstruction and sharply delimits the analytic reach: a centered local character estimate addresses only `Sigma/A`. Global solubility/Sha and first-small-point height require separate uniform retainers. Their three exponents add conditionally; a square-root upper-bound scale needs combined saving at least `1/2`.

`Stage14-4aq` must isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve.

Primary 4ap artifacts:

```text
stages/stage14/14-4ap/result.md
stages/stage14/data/14-4/character_global_height_transfer_summary.json
stages/stage14/scripts/14-4/character_global_height_transfer_audit.py
.github/workflows/stage14-4ap-character-global-height.yml
```
