# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION
STAGE14_4AJ=COMPLETE_SHIMADA_LATTICE_INTERFACE
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
STAGE14_4AN=COMPLETE_SELECTED_PRIME_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
MAX_VERIFIED_B=2000000
FULL_RANK_SELMER_CENSUS_MAX_H=20000
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED=true
SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2=true
SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4=true
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4ao full local matrix plus height-weighted descent-class count
```

Canonical source: `stages/stage14/main.md`.

## Core reduction

For a primitive oriented Pythagorean base `F=(S,X,H)`,

\[
E_F:Y^2=Z(Z-S^2)(Z+X^2)
\]

has full rational 2-torsion. The Stage14 pair surface is the level-4 modular K3; its physical polarization satisfies

\[
M^2=8,\qquad H_M=d.
\]

Stages 14-4ah through 14-4ak eliminate every fixed rational `M`-degree-four bisection capable of explaining a square-root exponent. Thus any finite `sqrt(B)` signal is collective.

For the collective count,

\[
V(B)=\#\{F:\mu(F)\le B\},\qquad A(B)=B/\pi+O(\sqrt B\log B),
\]

and 4am separates

```text
A ⊇ Sigma ⊇ R ⊇ V,
V/A=(Sigma/A)(R/Sigma)(V/R).
```

At `H<=20,000`, the complete census gives

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.81748
V/R in [0.01274,0.01427]
```

so the dominant finite thinning is after positive rank, in the first-small-point gate.

## Stage14-4an

Merged s5b/s5c selected-prime rows compress, using `d1*d2*d3` square, to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Therefore any selected odd `X`-prime has `p=1 mod 4`. For fixed support this is a three-block affine `F2` reciprocity matrix.

The exact `H<=20,000` support audit finds that these selected-prime rows thin support choices to about `16.96%` on average, but exclude **zero bases**. Every primitive Pythagorean base has an admissible singleton support at an `S`- or `H`-prime.

Thus

```text
SELECTED_ODD_ROWS_ALONE_FORM_COMPLETE_SELMER_TEST=false
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true
```

Even the completed Selmer gate will not by itself address the dominant `R -> V` first-small-point thinning.

## Next

Stage14-4ao imports/completes the unselected-odd and exhaustive `Q_2` local matrix and, in parallel, formulates a height-weighted descent-class count that keeps the physical small-point window visible.

Primary 4an artifacts:

```text
stages/stage14/14-4an/result.md
stages/stage14/archive/stage14-4an-character-gate-matrix.md
stages/stage14/data/14-4/character_gate_matrix_summary.json
stages/stage14/scripts/14-4/character_gate_matrix_audit.py
.github/workflows/stage14-4an-character-gate-matrix.yml
```
