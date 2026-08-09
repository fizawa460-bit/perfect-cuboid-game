# Stage14-4an — selected-prime character matrix and gate reach

Stage14-4am fixed the exact nested activation gates

```text
A(B) ⊇ Sigma(B) ⊇ R(B) ⊇ V(B)
V/A = (Sigma/A)(R/Sigma)(V/R).
```

Merged Stage14-s5b/s5c supplies the Euclid-factor reciprocity skeleton and the exact odd local rows at primes which are selected in a full-2-descent support. Stage14-4an compresses those rows and determines their precise theorem reach.

## 1. Compression by the global square-class relation

At a selected odd prime write `di=p^ei ai`, with `ai` p-adic units. Since

```text
d1*d2*d3 = square class,
```

we have in quadratic-character bits

```text
chi_p(a1)+chi_p(a2)+chi_p(a3)=0.
```

Therefore the two s5c equations at each supported prime reduce to

```text
S / 12 : chi_p(a3)=0
H / 23 : chi_p(a1)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0.
```

The X-row has a genuine independent sign obstruction:

```text
selected odd p|X  =>  p == 1 (mod 4).
```

For a fixed support this is an affine F2 character system. The affine offsets contain the p-unit contribution of signs and the prime 2; the odd cross-prime coefficients come from the s5b reciprocity matrix.

In the homogeneous odd-only normalization the three block rows are

```text
p in S : sum_{q selected in X union H} [q/p] = 0
p in X : p=1 mod 4 and sum_{q selected in S union H} [q/p] = 0
p in H : sum_{q selected in S union X} [q/p] = 0.
```

Here `[q/p]` is the F2 Legendre bit. Allowing the support itself to vary gates each row by its support bit, so globally the support-selection problem is quadratic over F2 even though the character row for a fixed support is linear.

## 2. Exact gate-reach obstruction

The selected-prime subsystem is not a complete local Selmer test. In fact it cannot exclude a single primitive Pythagorean base by itself.

Every genuine primitive oriented base has an odd prime dividing `S` or `H`. Choose one such prime as a singleton odd support. There are no cross-block selected primes, so its compact selected row is automatically satisfied. Hence every base has a nonempty homogeneous odd support passing all selected-prime rows.

Therefore

```text
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true.
```

The omitted odd bad-prime rows and the exhaustive Q2 squareclass table are not technical cleanup; they are logically necessary before the reciprocity skeleton becomes an actual base-level Selmer sieve.

## 3. Deterministic complete-base audit

All primitive oriented Pythagorean bases through `H<=20,000` are enumerated, and every odd support subset is checked against both the original s5c supported rows and the compressed 4an rows.

At `B=20,000`:

```text
eligible oriented bases                         6372
mean / median / max odd bad-prime count        6.7875 / 7 / 9
mean admissible supports incl empty            18.4936
median admissible supports incl empty          16
max admissible supports incl empty             76
mean admissible fraction of all support sets   0.1695801
bases with no nonempty admissible support       0
mean guaranteed singleton supports              5.27919
min / max guaranteed singleton supports         1 / 9
```

Thus the selected rows do significantly thin *support choices* but have zero base-level exclusion power without the missing local rows.

## 4. Relation to the 4am activation gates

Stage14-4am gives at `20k`

```text
Sigma/A = 0.8174827369742624
V/R     in [0.012738853503184714, 0.01427061310782241].
```

So even the complete nontrivial-Selmer gate is common in the finite family, while physical first activation conditional on positive rank is rare. The reciprocity matrix belongs to the local `A -> Sigma` interface. It does not control Sha/global representability in `Sigma -> R`, and it contains no first-small-point height information for `R -> V`.

Consequently a proof aligned with the observed finite mechanism must eventually combine descent/local arithmetic with the physical logarithmic height window; a Selmer-density theorem alone is not the main-track endpoint.

## Locked boundary

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
```

## Next

`Stage14-4ao`: import/complete the s5d unselected-odd and Q2 local matrix, then formulate a height-weighted descent-class count whose target is the dominant `R -> V` gate rather than Selmer density alone.
