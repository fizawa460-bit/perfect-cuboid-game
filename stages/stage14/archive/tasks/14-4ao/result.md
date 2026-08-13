# Stage14-4ao — full local matrix and height-weighted descent interface

## Result

Merged Stage14-s5f classifies the covering-specific prime-2 image. Of the 64 ordered product-square states in `Q_2^*/Q_2^{*2}`, exactly eight occur:

```text
(1,1,1) (3,7,5) (5,1,5) (7,7,1)
(2,1,2) (6,7,10) (10,1,10) (14,7,2).
```

Together with the complete odd rows imported in 4an, this closes the **local algebra** of the moving full-2-descent system. It does not close global solubility/Sha or the first-small-point problem.

## Finite `A -> Sigma` sieve

The complete `H<=20,000` census already measures the actual full local gate:

```text
A=6372
Sigma=5209
Sigma/A=0.8174827369742624.
```

Thus the full local filter is not the rare finite event. The dominant observed thinning remains after positive rank:

```text
R in [3784,4239]
V=54
V/R in [0.012738853503184714,0.01427061310782241].
```

These are exact finite statements, not limiting densities.

## Height-weighted descent-class count

For an eligible primitive oriented base `F`, let `C_{F,xi}` denote the 2-cover attached to a nontrivial locally soluble class `xi`, and let `phi_xi` map a rational point on the cover to `E_F`. Define the existence count

\[
\mathcal H(B;C)=\sum_{F\in\mathcal A(B)}
1\{\exists\xi,\exists P\in C_{F,\xi}(\mathbf Q):
\widehat h(\phi_\xi(P))\le C(\log B+\log H(F))\}.
\]

Each base is counted once, regardless of the number of classes or points. The quantifiers deliberately retain all three gates:

1. `xi` is locally admissible (`A -> Sigma`);
2. `C_{F,xi}(Q)` is nonempty (`Sigma -> R`, including the Sha obstruction);
3. its image contains a point in the s3 logarithmic canonical-height window (`R -> V`).

For the constant supplied by the s3 height comparison, every physical hit contributes to this count, so

\[
V(B)\le \mathcal H(B;C).
\]

The inclusion may be strict because the descent point must also satisfy the frozen physical-coordinate conditions. This formulation prevents a Selmer-class multiplicity from being mistaken for a base count.

## Boundary

```text
STAGE14_4AO=COMPLETE_FULL_LOCAL_MATRIX_AND_HEIGHT_WEIGHTED_COUNTING_INTERFACE
Q2_COVERING_SPECIFIC_64_STATE_SOLUBILITY_CLASSIFIED=true
FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE=true
FINITE_A_TO_SIGMA_SIEVE_QUANTIFIED=true
HEIGHT_WEIGHTED_DESCENT_COUNT_FORMULATED=true
GLOBAL_SOLUBILITY_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No power saving, `sqrt(B)` law, or leading constant is proved here. The next step must average the explicit moving character system without discarding global solubility or the physical height window.

```text
NEXT=Stage14-4ap prove or sharply delimit a family character-sum estimate coupled to global solubility and the s3 height window
```
