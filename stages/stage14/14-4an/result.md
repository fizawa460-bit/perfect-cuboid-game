# Stage14-4an — complete odd character matrix and gate reach

Merged s5c supported-prime rows compress, using `d1*d2*d3` square, to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Hence every selected odd `X`-prime must satisfy `p=1 mod 4`.

Merged s5d supplies the complementary unselected odd rows:

```text
p|S : chi_p(d3)=+1
p|H : chi_p(d1)=+1
p|X : chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

Thus **all odd bad-prime local rows are explicit** in the s5b reciprocity bits. The only remaining local-place gap is covering-specific `Q_2` solubility; s5d reduces it to 64 product-square squareclass states but does not classify them.

The `H<=20,000` audit checks every primitive oriented base and every odd support subset. In the homogeneous odd-only slice:

```text
eligible oriented bases                         6372
mean / median / max odd bad-prime count        6.7875 / 7 / 9
selected rows: mean surviving support fraction  0.1695801
selected rows: bases with no nonempty support    0
full odd matrix: mean surviving support fraction 0.04556219
full odd matrix: mean surviving supports          4.09149
full odd matrix: median / max                      4 / 32
full odd matrix: bases with no nonempty odd support 779
```

The selected-only zero is structural: an `S`- or `H`-prime singleton always passes the selected-prime subsystem. Adding the s5d unselected rows cuts the homogeneous support space much more strongly, but the `779` figure is **not** a Selmer base sieve: sign/2 affine data and covering-specific `Q_2` solubility are not classified in this slice, and the empty odd support always passes the odd matrix.

Merged 4am gives

```text
Sigma/A at 20k = 0.8174827369742624
V/R at 20k     in [0.012738853503184714, 0.01427061310782241].
```

Therefore the completed odd reciprocity matrix belongs to the local `A -> Sigma` interface only. It does not control `Sigma -> R`, and it contains no physical-height information for the finite-dominant `R -> V` gate.

```text
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
S5C_SUPPORTED_ROWS_COMPRESSED_USING_GLOBAL_SQUARECLASS=true
SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2=true
SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4=true
S5D_ALL_ODD_BAD_PRIME_ROWS_IMPORTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=false
FULL_LOCAL_SELMER_MATRIX_COMPLETE=false
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4ao finish Q2 covering-specific 64-state classification, then formulate a height-weighted descent-class count for R->V
```
