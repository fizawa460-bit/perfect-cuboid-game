# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed main-track foundation

- `14-1` through `14-3`: definition, independent exact enumeration, finite reconnaissance.
- `14-4aa` through `14-4ae`: two-face gluing, height envelope, elliptic reduction, generic rank zero.
- `14-4af` through `14-4ag`: Pythagorean-base K3, level-4/Kummer identification, rank-jump graph.
- `14-4ah` through `14-4ak`: physical polarization and complete closure of fixed `M.C=4` rational-curve square-root mechanisms.
- `14-4al`: collective first-hit measure `V(B)=#{F:mu(F)<=B}`.
- `14-4am`: exact activation factorization `A -> Sigma -> R -> V` and complete `H<=20k` rank/Selmer census.
- `14-4an`: compress selected-prime rows, import s5d unselected rows, and close the **entire odd-prime local character matrix**; identify its exact gate reach.

## Locked geometry

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

Any square-root phenomenon must be collective.

## Locked activation factorization

```text
A      eligible primitive oriented Pythagorean bases
Sigma  nontrivial full-2-Selmer beyond rational torsion
R      positive Mordell--Weil rank
V      physical first hit by B
```

Exactly

\[
V/A=(\Sigma/A)(R/\Sigma)(V/R).
\]

At `H<=20,000`:

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.81748
V/R in [0.01274,0.01427]
```

Thus finite Selmer and positive rank are common; the dominant observed thinning is `R -> V`.

## 14-4an — complete odd reciprocity matrix

Status: [x] Complete.

For selected odd bad primes the s5c rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Hence selected odd `p|X` requires `p=1 mod 4`.

Merged s5d gives all unselected odd bad-prime rows:

```text
p|S : chi_p(d3)=+1
p|H : chi_p(d1)=+1
p|X : chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

Therefore

```text
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
```

The `H<=20,000` support audit gives

```text
selected-row mean surviving support fraction       0.1695801
selected-row bases with no nonempty support        0
complete-odd mean surviving support fraction       0.04556219
complete-odd mean surviving supports                4.09149
bases with no nonempty homogeneous odd support     779
```

The `779` count is not a Selmer base count: it is the homogeneous odd-only slice. The remaining local problem is covering-specific `Q_2` solubility; s5d has already reduced the product-square state space to 64 states.

Locked boundary:

```text
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
S5D_ALL_ODD_BAD_PRIME_ROWS_IMPORTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=false
FULL_LOCAL_SELMER_MATRIX_COMPLETE=false
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
```

## 14-4ao — Q2 completion + height-weighted descent count

Status: [>] Next.

1. Finish/import the covering-specific classification of the 64 product-square `Q_2` descent states.
2. Combine it with the complete odd matrix to obtain the full local Selmer matrix.
3. Quantify the actual `A -> Sigma` family sieve produced by that matrix.
4. Do **not** stop there: formulate a height-weighted descent-class counting object retaining the Stage14-s3 physical logarithmic canonical-height window.
5. Target the finite-dominant `R -> V` gate, separating global representability from first-small-point size.
6. Seek any rigorous power saving before attempting a `sqrt(B)` law or leading constant.

## Parallel arithmetic track

The s-track is a direct input to the main line:

- s5a: Euclid-parameter descent target;
- s5b: odd reciprocity skeleton;
- s5c: selected-prime local rows;
- s5d: complete odd local rows and 64-state `Q_2` reduction;
- later s5 stages: exact `Q_2` covering classification and family-level analytic estimates.

## Triple gate

The exact identity remains

\[
N_2(B)=E(B)-3T(B).
\]

A future raw-pair law cannot transfer to exactly-two until sufficiently strong triple control is proved, ideally `T(B)=o(sqrt(B))`.

## Scope boundary

No true Stage14 growth exponent, leading constant, family large-sieve theorem, uniform first-small-point lower-tail theorem, perfect-cuboid nonexistence theorem, or `T=o(sqrt(B))` theorem is established.

```text
NEXT=Stage14-4ao Q2 completion plus height-weighted descent-class count
```
