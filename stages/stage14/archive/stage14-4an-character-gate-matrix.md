# Stage14-4an — complete odd character matrix and gate reach

Stage14-4am fixed

```text
A ⊇ Sigma ⊇ R ⊇ V,
V/A=(Sigma/A)(R/Sigma)(V/R).
```

This stage integrates the merged s5b/s5c/s5d local-descent work and states exactly which gate the reciprocity matrix can reach.

## Selected-prime compression

At a selected odd prime write `di=p^ei ai`. The global square-class relation gives

```text
chi_p(a1)+chi_p(a2)+chi_p(a3)=0.
```

Hence the two s5c rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Thus any selected odd `p|X` has `p=1 mod 4`. For fixed support this is a three-block affine `F2` character matrix; reciprocity gives the odd cross-prime coefficients, while sign/2 normalization gives affine offsets.

## Complete odd local matrix from s5d

For odd bad primes omitted from the support, s5d proves

```text
p|S : chi_p(d3)=+1
p|H : chi_p(d1)=+1
p|X : chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

The X-unselected row is automatic for `p=3 mod 4` and reduces to `chi_p(d2)=+1` for `p=1 mod 4`.

Together with the compressed selected rows, every odd bad-prime local condition is explicit in the s5b reciprocity bits.

```text
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
```

## Complete-base support audit

Every primitive oriented Pythagorean base through `H<=20,000` and every odd support subset is enumerated.

At the ceiling:

```text
eligible oriented bases                            6372
mean / median / max odd bad-prime count           6.7875 / 7 / 9
selected-row mean surviving support fraction       0.1695801
selected-row bases with no nonempty support        0
complete-odd mean surviving support fraction       0.04556219
complete-odd mean surviving supports                4.09149
complete-odd median / max                           4 / 32
bases with no nonempty homogeneous odd support     779
```

The selected-only zero is exact and structural: every base has an odd prime in `S` or `H`, and that prime as a singleton support passes every selected-prime row.

The `779` complete-odd number is only a homogeneous odd-only diagnostic. It is not a count of bases excluded from the Selmer set: sign/2 affine data and the covering-specific `Q_2` condition are not part of that slice, and the empty odd support always satisfies the odd matrix.

## Remaining local boundary: Q2

Merged s5d reduces `Q_2^*/Q_2^{*2}` to eight classes and the product-square descent state to 64 ordered states, but does not classify covering-specific solubility. Therefore

```text
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=false
FULL_LOCAL_SELMER_MATRIX_COMPLETE=false.
```

The odd reciprocity problem is closed; the remaining local classification is finite and 2-adic.

## Main-track interpretation

At `20k`, 4am gives

```text
Sigma/A = 0.8174827369742624
V/R     in [0.012738853503184714,0.01427061310782241].
```

Thus even the exact full nontrivial-Selmer gate is common in the finite family. The odd character matrix is part of `A -> Sigma`; it does not control Sha/global representability in `Sigma -> R`, and no local reciprocity matrix contains the first-small-point height needed for `R -> V`.

The main theorem target must therefore remain height-weighted even after the final `Q_2` classification is finished.

## Locked decision

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
```

## Next

`Stage14-4ao`: finish/import the covering-specific 64-state `Q_2` classification, then formulate a height-weighted descent-class count targeting the finite-dominant `R -> V` first-small-point gate.
