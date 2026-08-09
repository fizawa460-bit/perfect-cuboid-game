# Stage14 — exactly-two integral-face population

Current canonical source: `stages/stage14/main.md`.

```text
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
MAX_VERIFIED_B=2000000
FULL_RANK_SELMER_CENSUS_MAX_H=20000
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=false
FULL_LOCAL_SELMER_MATRIX_COMPLETE=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4ao Q2 completion plus height-weighted descent-class count
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

## Next

`Stage14-4ao` finishes/imports the 64-state `Q_2` covering classification, combines it with the complete odd matrix, and then formulates a height-weighted descent-class count retaining the physical small-point window.

Primary 4an artifacts:

```text
stages/stage14/14-4an/result.md
stages/stage14/archive/stage14-4an-character-gate-matrix.md
stages/stage14/data/14-4/character_gate_matrix_summary.json
stages/stage14/scripts/14-4/character_gate_matrix_audit.py
.github/workflows/stage14-4an-character-gate-matrix.yml
```
