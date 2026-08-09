# Stage14-4an — selected-prime character matrix gate boundary

The merged s5c supported-prime rows compress, using `d1*d2*d3` square, to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Hence every selected odd `X`-prime must satisfy `p=1 mod 4`. For fixed support these are affine `F2` character rows on the three `S/X/H` prime blocks; sign and 2-adic normalization supply affine offsets.

The complete `H<=20,000` oriented-base audit checks the compression against the original s5c equations for every odd support subset. At the ceiling:

```text
eligible oriented bases                         6372
mean / median / max odd bad-prime count        6.7875 / 7 / 9
mean admissible selected-row supports           18.4936
median                                           16
max                                              76
mean fraction of all support subsets             0.1695801
bases with no nonempty admissible support        0
```

The last line is structural, not accidental: every primitive Pythagorean base has an odd prime in `S` or `H`, and that prime as a singleton support satisfies all selected-prime rows. Therefore the selected-prime subsystem thins support choices but **cannot sieve bases at all** without the local rows at omitted bad primes and the complete `Q_2` table.

Merged 4am gives

```text
Sigma/A at 20k = 0.8174827369742624
V/R at 20k     in [0.012738853503184714, 0.01427061310782241].
```

Thus even the full exact nontrivial-Selmer gate is common in the finite family. The reciprocity matrix belongs to `A -> Sigma`; it does not control `Sigma -> R`, and it contains no physical-height information for the dominant finite `R -> V` gate.

```text
STAGE14_4AN=COMPLETE_SELECTED_PRIME_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
S5C_SUPPORTED_ROWS_COMPRESSED_USING_GLOBAL_SQUARECLASS=true
SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2=true
SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4=true
SELECTED_ODD_ROWS_ALONE_FORM_COMPLETE_SELMER_TEST=false
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4ao complete full local matrix via s5d handoff, then formulate a height-weighted descent-class count for R->V
```
