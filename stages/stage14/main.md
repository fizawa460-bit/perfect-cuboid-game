# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AP_COMPLETE_CHARACTER_GLOBAL_HEIGHT_TRANSFER_BOUNDARY_14_4AQ_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer

Stage14 studies primitive canonical cuboids

\[
0<a<b<c,\quad \gcd(a,b,c)=1,\quad a^2+b^2+c^2=d^2,\quad d\le B,
\]

with exactly two integral face diagonals. Detailed derivations are retained in the archive; this is the canonical synthesis through Stage14-4ap.

## 1. Locked exact population

Let `T(B)` count all-three-face objects and `E(B)` raw two-face incidences. Then

\[
\boxed{E(B)=N_2(B)+3T(B)}.
\]

At `B=2,000,000`, two independent exact generators give

```text
(Na,Nb,Nc)=(142,134,80)
N2=356
T=0
```

The finite zero triple census is not a perfect-cuboid nonexistence theorem. Frozen Stage13 `R03 + 13-12ag` gives only `N2(B)=o(B(log B)^3)`.

## 2. Elliptic/Kummer reduction and fixed-curve closure

For a primitive oriented Pythagorean base `F=(S,X,H)`,

\[
E_F:\quad Y^2=Z(Z-S^2)(Z+X^2)
\]

has full rational 2-torsion and generic Mordell--Weil rank zero over the moving base. Physical pairs therefore require a positive-rank specialization plus a sufficiently small non-torsion point.

The pair surface is the level-4 modular K3. Its physical polarization satisfies

\[
M=\pi^*(-K_Y),\qquad M^2=8,\qquad H_M=d.
\]

Stages 14-4ah through 14-4ak eliminate the complete fixed rational `M`-degree-four bisection mechanism. The final Shimada anti-invariant lattice target has 1020 norm-16 vectors but zero vectors in the required parity coset.

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

Any square-root phenomenon must therefore be collective.

## 3. Collective activation and three gates

Define `mu(F)` as the first physical Stage14 height for `F`, or infinity. Then

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

The eligible primitive oriented Pythagorean base count is

\[
A(B)=B/\pi+O(\sqrt B\log B).
\]

Hence a hypothetical `V(B)~c sqrt(B)` is equivalent to inverse-square-root activation density `V(B)/A(B)~pi c/sqrt(B)`.

Stage14-4am separates

```text
A(B)      eligible bases
Sigma(B)  dim Sel_2(E_F)>2
R(B)      rank E_F(Q)>0
V(B)      mu(F)<=B
```

with

\[
V\subset R\subset\Sigma\subset A,
\qquad
\boxed{V/A=(\Sigma/A)(R/\Sigma)(V/R)}.
\]

The complete `H<=20,000` census gives

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.8174827369742624
V/R in [0.012738853503184714,0.01427061310782241]
```

Thus in the finite family nontrivial Selmer and positive rank are common; the dominant observed thinning occurs after positive rank in the first-small-point gate. No asymptotic is inferred.

## 4. Euclid-factor descent coordinates

For primitive opposite-parity Euclid parameters

\[
S=m^2-n^2,\quad X=2mn,\quad H=m^2+n^2,
\]

the moving bad-prime support is carried by

```text
m, n, m-n, m+n, m^2+n^2,
```

which are pairwise coprime at odd primes.

Merged s5b/s5c routes selected odd primes as

```text
p|S -> 12
p|X -> 13
p|H -> 23.
```

## 5. Stage14-4an — complete odd character matrix

At a selected odd prime write `di=p^ei ai`. Since `d1*d2*d3` is a square class,

\[
\chi_p(a_1)+\chi_p(a_2)+\chi_p(a_3)=0\quad\text{in }\mathbf F_2.
\]

The two s5c rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Therefore

\[
\boxed{p\mid X\text{ selected}\implies p\equiv1\pmod4}.
\]

For fixed support this is a three-block affine `F2` reciprocity system.

Merged s5d supplies every **unselected** odd bad-prime row:

```text
p|S : chi_p(d3)=+1
p|H : chi_p(d1)=+1
p|X : chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

The X-unselected condition is automatic for `p=3 mod 4`; for `p=1 mod 4` it reduces to `chi_p(d2)=+1`.

Hence

```text
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
```

The odd local problem is now closed at the character-matrix level.

## 6. Exact support audit and gate reach

Every primitive oriented base through `H<=20,000` and every odd support subset is checked.

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

The selected-only zero is structural: every base has an `S`- or `H`-prime singleton which passes all selected-prime rows.

The `779` complete-odd figure is **not** a Selmer base count. It is the homogeneous odd-only slice. Sign/2 affine data and the covering-specific `Q_2` condition are not classified there, and the empty odd support always passes the odd matrix.

Thus the exact current local boundary is

```text
S5D_ALL_ODD_BAD_PRIME_ROWS_IMPORTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=false
FULL_LOCAL_SELMER_MATRIX_COMPLETE=false
```

Merged s5d has already reduced `Q_2^*/Q_2^{*2}` to eight classes and the product-square descent state to 64 ordered states. What remains locally is a finite covering-specific `Q_2` classification, not more odd-prime algebra.

## 7. What the character matrix can and cannot prove

The complete odd matrix is part of the local `A -> Sigma` interface. It does not decide:

- global representability / Tate--Shafarevich contribution in `Sigma -> R`;
- the physical first-small-point height in `R -> V`.

Since 4am finds `Sigma/A≈0.8175` but `V/R≈1.3–1.4%` at `20k`, a theorem aligned with the observed finite mechanism cannot stop at Selmer density. The final counting object must retain the physical logarithmic height window.

## 8. Stage14-4ao — prime 2 and height-weighted descent

Merged s5f proves that exactly eight of the 64 product-square `Q_2` states occur in the covering-specific local image:

```text
(1,1,1) (3,7,5) (5,1,5) (7,7,1)
(2,1,2) (6,7,10) (10,1,10) (14,7,2).
```

Together with the odd rows above, the full local 2-descent character system is explicit. The exact finite full-local gate at `H<=20,000` is `A=6372`, `Sigma=5209`, and `Sigma/A=0.8174827369742624`.

For a nontrivial locally soluble cover `C_{F,xi}`, 4ao locks the base-counted existence statistic

\[
\mathcal H(B;C)=\sum_{F\in\mathcal A(B)}1\{\exists\xi,\exists P\in C_{F,\xi}(\mathbf Q):
\widehat h(\phi_\xi(P))\le C(\log B+\log H(F))\}.
\]

It retains local admissibility, global solubility/Sha, and the s3 first-small-point window, and counts each base once. Physical activation implies membership for the s3 comparison constant, but the converse can fail because the physical-coordinate conditions are stronger.

## 9. Stage14-4ap — reach of character sums and conditional transfer

Merged s5g shows that raw prime-level quadratic-character traces require exact local mean subtraction; local resonances at `p=3,5,17` make the uncentered cancellation target false. After centering, the character system still controls only the local retainer `Sigma/A`.

Set `N0=A(B)`, `N1=Sigma(B)`, `N2=R(B)`, and `N3=H(B;C)`. The exact gate identity is

\[
N_3=N_0\frac{N_1}{N_0}\frac{N_2}{N_1}\frac{N_3}{N_2}.
\]

Consequently, conditional bounds `N0(B)<<B` and `Ni/N{i-1}<<B^{-delta_i}` imply

\[
\mathcal H(B;C)\ll B^{1-\delta_{\rm loc}-\delta_{\rm glob}-\delta_{\rm ht}}.
\]

Since `V(B)<=H(B;C)`, this transfers conditionally to `V`. A square-root upper-bound scale requires combined saving at least `1/2`. No one of the three retainer estimates is proved here: centered local cancellation cannot decide the global-solubility/Sha or first-small-point gates.

## 10. Locked decision

```text
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
STAGE14_4AO=COMPLETE_FULL_LOCAL_MATRIX_AND_HEIGHT_WEIGHTED_COUNTING_INTERFACE
STAGE14_4AP=LOCAL_CHARACTER_REACH_AND_CONDITIONAL_GLOBAL_HEIGHT_TRANSFER_BOUNDARY

FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED=true
SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2=true
SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4=true
S5D_ALL_ODD_BAD_PRIME_ROWS_IMPORTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=true
FULL_LOCAL_SELMER_MATRIX_COMPLETE=true
FINITE_A_TO_SIGMA_SIEVE_QUANTIFIED=true
HEIGHT_WEIGHTED_DESCENT_COUNT_FORMULATED=true
EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true
LOCAL_CHARACTERS_DETERMINE_GLOBAL_SOLUBILITY=false
LOCAL_CHARACTERS_DETERMINE_FIRST_SMALL_POINT_HEIGHT=false
LOCAL_LARGE_SIEVE_ALONE_CONTROLS_HEIGHT_WEIGHTED_COUNT=false
CONDITIONAL_THREE_RETAINER_TRANSFER_FORMULATED=true
GLOBAL_SOLUBILITY_AVERAGED=false
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true

FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```

## 11. Next

`Stage14-4aq`: isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve. The separate s3 first-small-point retainer remains explicit.

The independent triple track still must supply strong enough `T(B)` control before a future raw-pair law can transfer to exactly-two.

## Primary 4ap artifacts

```text
stages/stage14/14-4ap/result.md
stages/stage14/data/14-4/character_global_height_transfer_summary.json
stages/stage14/scripts/14-4/character_global_height_transfer_audit.py
.github/workflows/stage14-4ap-character-global-height.yml
```

