# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed foundation

- `14-1` through `14-3`: exact definition, independent enumeration, finite reconnaissance.
- `14-4aa` through `14-4ae`: exact two-face gluing, height envelope, elliptic reduction, generic rank zero.
- `14-4af` through `14-4ag`: Pythagorean-base K3, level-4/Kummer identification, active rank-jump graph.
- `14-4ah` through `14-4ak`: physical polarization `M`, minimum bisection reduction, Shimada lattice interface, exact split-root parity-coset void; the full fixed `M.C=4` rational-curve square-root mechanism is closed.
- `14-4al`: collective first-hit identity `V(B)=#{F:mu(F)<=B}` and inverse-square-root activation-density reformulation.
- `14-4am`: exact factorization `A -> Sigma -> R -> V` plus a complete rank/Selmer census through `H<=20,000`; finite thinning is dominated by `R -> V`.
- `14-4an`: compressed selected-prime character matrix; exact proof that selected-prime rows alone thin support choices but cannot sieve bases.

Frozen Stage13 upstream remains `R03 + Stage13-12ag`, including

\[
N_2(B)=o(B(\log B)^3),
\]

with no true Stage14 exponent yet.

## Fixed-curve branch — closed

Status: [x] Complete through `14-4ak`.

A fixed physical rational curve capable of exponent `1/2` must have `M.C=4`. The last split anticanonical possibility reduces to an anti-invariant norm-16 parity-coset problem in Shimada's level-4 Neron--Severi lattice. The norm-16 shell has 1020 vectors, but the required parity coset is empty by two independent exact enumerators.

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

## 14-4al — collective activation

Status: [x] Complete.

For primitive oriented Pythagorean bases,

\[
V(B)=\#\{F:\mu(F)\le B\},\qquad A(B)=B/\pi+O(\sqrt B\log B).
\]

Thus a hypothetical `V(B)~c sqrt(B)` is equivalent to `V(B)/A(B)~pi c/sqrt(B)`. Finite data through `2m` remain strikingly close to this scale, but no asymptotic is claimed.

## 14-4am — separate Selmer, rank, and first-small-point thinning

Status: [x] Complete.

Define

```text
A      eligible bases
Sigma  nontrivial full-2-Selmer beyond rational 2-torsion
R      positive Mordell--Weil rank
V      physical first hit by B
```

Then exactly

\[
V/A=(\Sigma/A)(R/\Sigma)(V/R).
\]

The complete `H<=20,000` census gives

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.81748
V/R in [0.01274,0.01427].
```

So finite Selmer and positive rank are common; the dominant observed thinning is the height-sensitive first-small-point gate after rank jump.

## 14-4an — selected-prime character matrix and gate reach

Status: [x] Complete.

The five Euclid-factor columns are

```text
m, n, m-n, m+n, m^2+n^2,
```

pairwise disjoint at odd primes. Merged s5c routes selected primes as

```text
S -> 12
X -> 13
H -> 23.
```

Using `d1*d2*d3` square, the supported-prime character rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Hence a selected odd `X`-prime must satisfy `p=1 mod 4`. For fixed support this is a three-block affine `F2` reciprocity system.

The complete support audit through `H<=20,000` finds

```text
eligible oriented bases                         6372
mean odd bad-prime count                         6.7875
mean fraction of support subsets surviving       0.16958
bases with no nonempty surviving support         0
```

The zero is structural: an `S`- or `H`-prime singleton always satisfies the selected-prime subsystem. Therefore selected rows alone cannot even define a base-level `A -> Sigma` sieve.

Locked boundary:

```text
SELECTED_ODD_ROWS_ALONE_FORM_COMPLETE_SELMER_TEST=false
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
```

Artifacts:

```text
stages/stage14/14-4an/result.md
stages/stage14/archive/stage14-4an-character-gate-matrix.md
stages/stage14/data/14-4/character_gate_matrix_summary.json
stages/stage14/scripts/14-4/character_gate_matrix_audit.py
.github/workflows/stage14-4an-character-gate-matrix.yml
```

## 14-4ao — complete local matrix + height-weighted descent count

Status: [>] Next.

Two pieces must now be joined rather than pursued separately:

1. **Complete the local Selmer matrix.** Import the parallel s5d work on odd bad primes omitted from the support and the exhaustive `Q_2` squareclass table. Only then can the reciprocity matrix become a genuine `A -> Sigma` base sieve.
2. **Do not stop at Selmer density.** Build a height-weighted descent-class counting object that keeps the Stage14-s3 physical logarithmic canonical-height window. The target must address the finite-dominant `R -> V` first-small-point gate.
3. Quantify whether the completed local matrix contributes any asymptotic exponent or only a constant/logarithmic factor.
4. Identify a theorem input capable of controlling globally represented non-torsion classes of sufficiently small height across primitive Euclid parameters.
5. Keep the raw-pair/exactly-two transfer separate until the triple track proves adequate `T(B)` control.

## 14-5 — directionwise asymptotic structure

Status: pending Stage14-4.

## Parallel arithmetic track

Stage14-s is now a direct computational/theorem-input branch for the main track. s5a formulated the Euclid-parameter descent sieve; s5b built the reciprocity skeleton; s5c derived exact selected-prime rows; s5d is the natural source for the missing unselected-prime and `Q_2` matrix required by 4ao.

## Triple gate

The exact identity remains

\[
N_2(B)=E(B)-3T(B).
\]

A future raw-pair law cannot transfer to exactly-two until sufficiently strong triple control is proved, ideally `T(B)=o(sqrt(B))`.

## Scope boundary

No true growth exponent, leading constant, limiting directional vector, perfect-cuboid nonexistence theorem, family large-sieve theorem, uniform first-small-point lower-tail theorem, or `T=o(sqrt(B))` theorem is established.

```text
NEXT=Stage14-4ao complete local matrix plus height-weighted descent-class count
```
