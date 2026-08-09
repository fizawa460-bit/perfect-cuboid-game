# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AN_COMPLETE_SELECTED_PRIME_CHARACTER_MATRIX_14_4AO_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer

Stage14 studies primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

with exactly two integral face diagonals. Detailed derivations are retained in the stage archive; this file is the canonical synthesis through Stage14-4an.

## 1. Exact ledger and finite ceiling

Let `T(B)` count all-three-face objects and `E(B)` the raw two-face incidences. Then

\[
\boxed{E(B)=N_2(B)+3T(B)}.
\]

At `B=2,000,000`, two independent exact generators give

```text
(Na,Nb,Nc)=(142,134,80)
N2=356
T=0
```

The finite zero triple census is not a perfect-cuboid nonexistence theorem. Frozen Stage13 `R03 + 13-12ag` supplies only

\[
N_2(B)=o(B(\log B)^3).
\]

## 2. Elliptic and Kummer reduction

For a primitive oriented Pythagorean first face `F=(S,X,H)`, the integral elliptic fiber is

\[
E_F:\quad Y^2=Z(Z-S^2)(Z+X^2),
\]

with full rational 2-torsion. The generic Mordell--Weil rank over the moving base is zero; every physical pair therefore lies on a positive-rank specialization and needs a sufficiently small non-torsion point.

The raw pair surface in half-angle coordinates is

\[
Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.
\]

Over `Q(i)` this is the level-4 modular K3 and over `C` it is `Km(E_i x E_i)`. On the resolved double cover of

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad L=-K_Y,
\]

the physical polarization is

\[
\boxed{M=\pi^*L},\qquad M^2=8,\qquad H_M=d.
\]

## 3. Fixed-curve square-root mechanism is closed

Stages 14-4ah through 14-4ai reduce every fixed rational curve capable of exponent `1/2` to an `M`-degree-four bisection, then to one possible split singular anticanonical case.

Stage14-4aj identifies the deck involution as

\[
\delta(P)=(0,0)-P.
\]

For a hypothetical final split component, `x=2C-M` must satisfy

\[
\delta(x)=-x,\qquad x^2=-16,\qquad x\equiv M\pmod2.
\]

Stage14-4ak ingests Shimada's published level-4 lattice data. The relevant anti-invariant lattice has rank `6`, positive determinant `256`, and `1020` norm-16 vectors, but none lies in the required parity coset. PARI/Fincke--Pohst and an independent exact LDL enumeration agree.

Hence

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

The finite square-root signal, if asymptotic, is collective.

## 4. Collective activation measure

For each primitive oriented Pythagorean base define `mu(F)` as its first physical Stage14 height, or infinity if none exists. Then

\[
\boxed{V(B)=\#\{F:\mu(F)\le B\}}.
\]

If `A(B)` counts all primitive oriented Pythagorean bases with `H<=B`, then

\[
\boxed{A(B)=B/\pi+O(\sqrt B\log B)}.
\]

Thus

\[
V(B)\sim c\sqrt B\iff V(B)/A(B)\sim \pi c/\sqrt B
\]

whenever either asymptotic exists. This is a reformulation, not a theorem.

The finite late profile is

```text
B          A(B)      V(B)      sqrt(B)*V/A
200,000     63,638      155       1.0892565339
500,000    159,164      254       1.1284280517
1,000,000  318,278      347       1.0902418640
2,000,000  636,640      490       1.0884717353
```

No square-root asymptotic is claimed.

## 5. Three nested arithmetic gates

Stage14-4am defines

```text
A(B)      all eligible bases
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

A complete PARI census of every oriented base through `H<=20,000` gives

```text
B        A       Sigma      R interval       V
2,000      638      476       371..385         7
5,000     1584     1234       916..989        25
10,000    3186     2553      1875..2057       39
20,000    6372     5209      3784..4239       54
```

At `20k`,

```text
Sigma/A = 0.8174827369742624
R/A     in [0.5938480853735091,0.6652542372881356]
V/R     in [0.012738853503184714,0.01427061310782241]
```

So in the complete finite family, nontrivial Selmer and positive rank are common; the dominant observed thinning occurs after positive rank in the first-small-point gate. This is finite evidence only.

## 6. Euclid-factor reciprocity interface

For primitive opposite-parity Euclid parameters

\[
S=m^2-n^2,\quad X=2mn,\quad H=m^2+n^2,
\]

the moving odd bad-prime support is carried by

```text
m, n, m-n, m+n, m^2+n^2,
```

which are pairwise coprime at odd primes.

Merged Stage14-s5b/s5c forces the selected-prime labels

```text
p|S -> 12
p|X -> 13
p|H -> 23
```

and gives the supported-prime local character rows.

## 7. Stage14-4an — selected-prime character matrix and its exact reach

Write locally `di=p^ei ai`. Because `d1*d2*d3` is a square class,

\[
\chi_p(a_1)+\chi_p(a_2)+\chi_p(a_3)=0\quad\text{in }\mathbf F_2.
\]

The two s5c rows therefore compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

In particular,

\[
\boxed{p\mid X\text{ selected}\implies p\equiv1\pmod4}.
\]

For fixed odd support the system is an affine `F2` character matrix. The odd cross-prime coefficients are reciprocity bits; sign and the prime 2 contribute affine offsets. When support itself varies, the rows are support-gated and the support-selection problem becomes quadratic over `F2`.

### Exact gate-reach boundary

The selected-prime subsystem alone cannot exclude any primitive Pythagorean base. Every genuine base has an odd prime dividing `S` or `H`; choosing such a prime as a singleton support automatically satisfies all selected-prime rows.

The complete `H<=20,000` audit verifies the original s5c rows and compressed rows support-by-support:

```text
eligible oriented bases                         6372
mean / median / max odd bad-prime count        6.7875 / 7 / 9
mean admissible supports incl empty            18.4936
median                                           16
max                                              76
mean admissible fraction of all supports         0.1695801
bases with no nonempty admissible support        0
```

Therefore

```text
SELECTED_ODD_ROWS_ALONE_FORM_COMPLETE_SELMER_TEST=false
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true
```

The omitted bad-prime rows and complete `Q_2` table are logically necessary before the reciprocity skeleton becomes a base-level Selmer sieve.

More importantly for the main track, even a complete Selmer matrix only addresses `A -> Sigma`. It does not settle `Sigma -> R`, and it contains no first-small-point height information for the dominant finite `R -> V` gate.

## 8. Current theorem boundary

```text
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
STAGE14_4AN=COMPLETE_SELECTED_PRIME_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY

FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED=true
SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2=true
SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4=true
SELECTED_ODD_ROWS_ALONE_SIEVE_BASES=false
UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA=true
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true

POSITIVE_RANK_DENSITY_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```

## 9. Next

`Stage14-4ao` has two coupled inputs:

1. import/complete the Stage14-s5d omitted-odd-prime and exhaustive `Q_2` local matrix, turning the reciprocity skeleton into a genuine `A -> Sigma` test;
2. formulate a **height-weighted descent-class count** that retains the physical logarithmic small-point window and targets the dominant `R -> V` gate rather than stopping at Selmer density.

The independent triple track still must establish sufficiently strong control on `T(B)` before a future raw-pair law can transfer to exactly-two.

## Primary current artifacts

```text
stages/stage14/archive/stage14-4an-character-gate-matrix.md
stages/stage14/14-4an/result.md
stages/stage14/data/14-4/character_gate_matrix_summary.json
stages/stage14/scripts/14-4/character_gate_matrix_audit.py
.github/workflows/stage14-4an-character-gate-matrix.yml
```
