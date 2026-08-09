# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed foundation

- `14-1`: definition/counting interface.
- `14-2`: two independent exact finite enumerators through `B=2,000,000`.
- `14-3`: finite directional reconnaissance.
- `14-4aa`: common shared-edge parametrization.
- `14-4ab`: exact face-pair bijection, multiplicity one.
- `14-4ac`: rational slope/lcm height envelope.
- `14-4ad`: elliptic reduction `E_t:Y^2=X(X-1)(X+t^2)`.
- `14-4ae`: physical fiber height `v asymp sqrt(Bg/S1)` and generic rank zero.
- `14-4af`: six-`I4` Pythagorean-base K3; torsion nonphysical; fixed-base triple genus 5.
- `14-4ag`: exact level-4/Kummer identification; active rank-jump graph; raw-edge and active-vertex polynomial exponents equal.
- `14-4ah`: exact physical Kummer polarization `M=pi^*(-K_Y)`, `M^2=8`, `H_M=d`; fixed physical rational curves have `M.C>=4`.

Frozen Stage13 upstream remains `R03 + Stage13-12ag`, including

\[
N_2(B)=o(B(\log B)^3),
\]

with no imported growing-modulus power saving.

## 14-4ai — minimum bisection reduction

Status: [x] Complete.

Stage14-4ah showed that a fixed rational curve can produce exponent `1/2` only if

\[
M\cdot C=4,
\qquad
\deg(C\to\mathbf P^1_r)=2.
\]

Stage14-4ai first adds

\[
\deg(C\to\mathbf P^1_s)\le2,
\]

because the second half-angle map `t(s)=y/e` is also a quotient of `M`-sections.

Let `D=pi(C)` and `delta=deg(C->D)`.

### `delta=2`

After the second degree bound and boundary reduction, only constant sections and opposite-corner `(1,1)` pencils remain. Exact branch-discriminant calculations show that their connected inverse images are genus one throughout the physical chamber; every rational degeneration is boundary/reducible.

```text
DEGREE_TWO_IMAGE_M4_MECHANISM_ELIMINATED=true
```

### `delta=1`, arithmetic genus zero

Writing

\[
D=aH_r+2H_s-\sum m_iE_i,
\]

one has `a<=2` and `L.D=4`.

- `a=1`: the physical genus-zero cores reduce to same-`r` and opposite-corner `(1,2)` contact families. Exact resultant/discriminant identities eliminate every irreducible square-contact member.
- `a=2`, multiplicities `(2,1,1,0)`: every arithmetic-genus-zero class reduces by forced null-boundary components to an `a=1` core or a section.

```text
GENUS_ZERO_SPLIT_M4_MECHANISM_ELIMINATED=true
```

### The remaining class

The all-simple `a=2` class is

\[
\boxed{D=L=-K_Y},
\]

with

\[
D^2=4,
\qquad p_a(D)=1.
\]

A singular member may have normalization `P1`. If the Kummer branch restricts evenly to such a singular rational anticanonical curve, the pullback splits and gives an `M`-degree-four rational bisection.

Therefore the correct 14-4ai boundary is

```text
ONLY_REMAINING_FIXED_SQRTB_CURVE_TARGET=split singular anticanonical D in |L|
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=false
```

The earlier shortcut `rational normalization => arithmetic genus zero` is explicitly forbidden.

### Symmetric Kummer coordinates

14-4ai also introduces

\[
\lambda=\frac{1-rs}{r-s},
\qquad
\mu=\frac{1+rs}{r+s},
\]

for which

\[
(\lambda^2-1)(\mu^2-1)=\square,
\qquad
(\lambda^2+1)(\mu^2+1)=\square,
\]

and hence

\[
\boxed{(\lambda^4-1)(\mu^4-1)=\square.}
\]

These are the preferred coordinates for the remaining contact/CM audit.

### Triple restriction

The third-face cover has branch class `2M`. On a hypothetical minimal bisection its branch degree is `8`; with transverse branch the restricted double cover has genus `3`. Special tangencies remain open and belong to the parallel triple gate.

Artifacts:

```text
stages/stage14/archive/stage14-4ai-degree4-bisections.md
stages/stage14/scripts/14-4/degree4_bisection_audit.py
stages/stage14/data/14-4/degree4_bisection_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## 14-4aj — singular anticanonical contact / CM-lattice classification

Status: [>] Next.

There is now a single fixed-curve square-root target.

Tasks:

1. parameterize the singular locus in the anticanonical system `|L|`;
2. impose the exact even-contact / splitting condition against the space branch `B~2L`;
3. classify the resulting splitting classes over `Q` and over `Q(i)`;
4. compare them with the Gaussian-CM/Kummer lattice using the `(lambda,mu)` model;
5. determine which classes meet the physical chamber `0<r<s<1`;
6. if a physical Q-rational splitting curve exists, compute its `M`-height first-hit law and restrict the third-face cover to it;
7. if none exists, reject the complete fixed-curve `sqrt(B)` mechanism and return to a genuinely collective rank-jump/CM-strata count.

No square-root asymptotic is promoted before this last minimal contact case is decided.

## 14-5 — directionwise asymptotic structure

Status: pending Stage14-4.

## Parallel triple gate

Stage14-t1 is merged and has its own quantitative roadmap. The exact identity remains

\[
N_2(B)=E(B)-3T(B).
\]

The main-track raw law cannot be transferred to exactly-two until the triple track proves a sufficient bound, ideally

\[
T(B)=o(\sqrt B).
\]

## Scope boundary

No true Stage14 growth exponent, leading constant, limiting directional vector, perfect-cuboid existence/nonexistence theorem, or `T=o(sqrt(B))` theorem is established yet.

```text
NEXT=Stage14-4aj singular anticanonical contact discriminant / CM-Kummer lattice classification
```
