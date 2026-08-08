# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
LAMBDA_MU_KUMMER_COORDINATES_LOCKED=true
DEGREE_TWO_IMAGE_M4_MECHANISM_ELIMINATED=true
GENUS_ZERO_SPLIT_M4_MECHANISM_ELIMINATED=true
ONLY_REMAINING_FIXED_SQRTB_CURVE_TARGET=split singular anticanonical D in |L|
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=false
T_O_SQRT_B_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
NEXT=Stage14-4aj singular anticanonical contact discriminant / CM-Kummer lattice classification
```

Canonical source: `stages/stage14/main.md`.

## Locked population and finite ceiling

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exact ledgers satisfy

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

At `B=2,000,000`, two independent exact generation routes give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

The finite zero triple census is not a perfect-cuboid nonexistence theorem.

## Kummer/rank-jump reduction

For Pythagorean half-angle parameters `r,s`, the raw pair surface is

\[
\boxed{Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.}
\]

Over `Q(i)` it is the level-4 elliptic modular K3; over `C` it is `Km(E_i x E_i)`.

The physical compactification is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=2H_r+2H_s-\sum E_j=-K_Y,
\]

with resolved double cover `pi:X->Y`. Stage14-4ah identifies

\[
\boxed{M=\pi^*L},\qquad \boxed{M^2=8},\qquad \boxed{H_M=d}.
\]

Let `V(B)` count active oriented first-face states and `E(B)` raw pair incidences. Dujella's bounded-height input gives maximum fiber degree `B^{o(1)}`, so `E(B)` and `V(B)` have the same polynomial growth exponent. Finite `V(B)/sqrt(B)` remains strikingly stable through `2m`, but no square-root theorem is claimed.

## Stage14-4ai — what happened to the degree-four suspect

Stage14-4ah showed that any fixed rational curve capable of a `sqrt(B)` exponent must satisfy

\[
M\cdot C=4,
\qquad
\deg(C\to\mathbf P^1_r)=2.
\]

Stage14-4ai adds the second bound

\[
\deg(C\to\mathbf P^1_s)\le2
\]

and classifies the image `D=pi(C)` by `delta=deg(C->D)`.

- `delta=2`: constant sections and opposite-corner `(1,1)` pencils exhaust the movable cases after boundary reduction; exact branch-discriminant calculations eliminate every physical rational inverse image.
- `delta=1`, arithmetic genus zero: all `(1,2)` contact cores and their `(2,2)` genus-zero ancestors are eliminated by exact resultant/discriminant identities.
- one case remains: the anticanonical class
  \[
  \boxed{D=L=-K_Y,\qquad p_a(D)=1.}
  \]
  A singular member can have normalization `P1`; if its branch restriction is even, the pullback can split into an `M`-degree-four rational bisection.

Therefore the correct theorem boundary is

\[
\boxed{
\text{any remaining fixed-curve }\sqrt B\text{ mechanism must come from a split singular anticanonical curve }D\in|L|.
}
\]

Stage14-4ai does **not** yet prove that this remaining locus is empty.

## New symmetric coordinates

Define

\[
\lambda=\frac{1-rs}{r-s},
\qquad
\mu=\frac{1+rs}{r+s}.
\]

Then

\[
(\lambda^2-1)(\mu^2-1)=\square
\]

encodes rational recovery of `r,s`, while the space-square condition is

\[
(\lambda^2+1)(\mu^2+1)=\square.
\]

Hence

\[
\boxed{(\lambda^4-1)(\mu^4-1)=\square.}
\]

This is the preferred Kummer/CM coordinate system for 14-4aj.

## Triple gate

The third-face-square relative cover has branch class `2M`. On a hypothetical minimal bisection its branch degree is `8`, giving a genus-3 double cover in the transverse case. Special tangencies still need auditing. The independent Stage14-t track continues to target

\[
T(B)=o(\sqrt B),
\]

which is not yet proved.

## Artifacts

```text
stages/stage14/archive/stage14-4ai-degree4-bisections.md
stages/stage14/scripts/14-4/degree4_bisection_audit.py
stages/stage14/data/14-4/degree4_bisection_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## Next

Stage14-4aj will classify singular anticanonical members `D in |L|`, impose the splitting/even-contact condition against the Kummer branch, and compare the survivors with the Gaussian-CM lattice in `(lambda,mu)` coordinates. If that locus is empty, the entire fixed-curve square-root mechanism is rejected; otherwise its physical first-hit law can be counted explicitly.
