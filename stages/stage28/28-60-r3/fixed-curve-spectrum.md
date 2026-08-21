# Stage28-60-r3 — fixed rational-curve spectrum comparison

```text
ROUTE=R21_FIXED_CURVE_SPECTRUM_COMPARISON_PLUS_R26_ODD_DEGREE_OBSTRUCTION
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

Checkpoint60-r2 reduced the direct bridge to the interaction-curvature threshold

\[
J_{28}=I_{face}/I_{sp}\quad\text{versus}\quad (\log B)^{-2}.
\]

r3 asks whether the two completion covers already differ at the level of low-degree physical rational curves under the common quasi-polarization.

## 1. Stage19 space cover: degree four is absent

The audited Stage14-4ah/4ai/4ak chain identifies

\[
M=\pi^*(-K_Y),\qquad M^2=8,
\]

and proves that every physical rational curve has `M.C>=4`. Stage14-4ak then closes the complete physical `M.C=4` stratum by the exact Shimada anti-invariant-lattice parity-coset computation:

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

Thus there is no physical Q-rational fixed curve of M-degree four.

## 2. New r3 theorem candidate: every physical odd M-degree is impossible

Let `delta` be the physical deck involution. The audited Stage28-50-r2 branch firewall proves that the branch divisor has no point on the positive physical real torus. Hence an irreducible physical curve `C` of odd degree

\[
m=M\cdot C
\]

cannot be a connected degree-two pullback from the base: such a curve would have even `M`-degree. Therefore it must occur in a split pair

\[
C+\delta C=\pi^*D
\]

with `pi|_C` birational onto `D`.

Put

\[
x=C-\delta C.
\]

Then `delta(x)=-x`, so `x` lies in the deck anti-invariant lattice. Since

\[
D^2=(C+\delta C)^2/2=C^2+C\cdot\delta C,
\]

one gets

\[
x^2=2C^2-2C\cdot\delta C=4C^2-2D^2.
\]

The K3 Neron--Severi lattice is even, hence `4C^2` is divisible by `8`. On the base, adjunction gives

\[
D^2-K_Y\cdot(-D)=D^2-m=2p_a(D)-2,
\]

or simply

\[
D^2\equiv m\pmod2.
\]

Consequently

\[
\boxed{-x^2\equiv 2m\pmod4.}
\]

The exact Stage14-4ak Shimada embedding was reconstructed in r3 CI. The positive form on the rank-six anti-invariant lattice has Gram matrix

\[
Q=\begin{pmatrix}
4&0&-2&2&-4&-2\\
0&4&-2&2&0&-2\\
-2&-2&4&-2&0&0\\
2&2&-2&4&-2&0\\
-4&0&0&-2&8&4\\
-2&-2&0&0&4&8
\end{pmatrix},
\qquad \det Q=256.
\]

Every diagonal entry is divisible by four and every off-diagonal entry is even. Therefore

\[
\boxed{q(v)=v^TQv\equiv0\pmod4\quad\text{for every }v\in\mathbf Z^6.}
\]

For odd `m`, however, the split-curve identity requires `-x^2 congruent 2 (mod 4)`, a contradiction. Hence

\[
\boxed{\text{there is no physical Stage19 fixed rational curve of odd }M\text{-degree}.}
\]

In particular,

\[
\boxed{M\cdot C=5\text{ is impossible}.}
\]

This argument does not assume that `C` or its image is smooth; singular rational curves are covered because only lattice parity and adjunction parity are used.

Exact-head GitHub Actions independently reconstructed the two equivalent physical Shimada labelings, the rank-six anti-invariant lattice, determinant `256`, and the norm divisibility. Run `32437537363` concluded success with

```text
STAGE28_60_R3_M5_NORM_OBSTRUCTION=PASS
ODD_PHYSICAL_M_DEGREE_OBSTRUCTION=PASS_CANDIDATE_FROM_EXACT_LATTICE
```

The fresh Stage28 audit must still validate the mathematical promotion.

## 3. Consequence for fixed-curve counting

Combining the audited M4 void with the new odd-degree obstruction, every physical Stage19 fixed rational curve has

\[
\boxed{M\cdot C\ge6.}
\]

For a fixed rational curve of M-degree `m`, the pulled-back height on its normalization has degree `m`, so its bounded-height polynomial exponent is at most `2/m`. Thus any finite union of fixed physical Stage19 rational curves contributes at most

\[
\boxed{O(B^{1/3})}
\]

at the polynomial-exponent level.

This remains a fixed-curve statement only. Stage14-4al shows that the observed source signal, if asymptotic, may arise from a collective moving-fibre/rank-jump/first-small-point mechanism rather than from finitely many fixed curves.

## 4. Stage20 third-face cover: degree-six rational family present

The audited generalized Saunderson map is homogeneous of degree six in the coprime Euclid parameters `(r,s)`:

```text
u=r^2-s^2
v=2rs
w=r^2+s^2
A=u(4v^2-w^2)
B=v(4u^2-w^2)
C=4uvw
```

(up to harmless signs/absolute values on the physical chamber). The three edge coordinates have no common nonconstant polynomial factor. On the audited injective cone `1/8<=s/r<=4/5`,

\[
r^6\le w^3\le R\le8r^6,
\]

so this fixed rational target curve contributes

\[
\boxed{\Theta(B^{1/3})}
\]

on a positive-density rational parameter sector.

## 5. What the sharpened spectrum comparison proves

The previous possible `2/5` source fixed-curve contribution is now eliminated. At the fixed-curve polynomial-exponent level the two sides have reached the same critical scale:

```text
STAGE19_FIXED_M4_CURVE=ABSENT
STAGE19_FIXED_ODD_M_DEGREE_CURVES=ABSENT_CANDIDATE
STAGE19_FIXED_M5_CURVE=ABSENT_CANDIDATE
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CANDIDATE=1/3
STAGE20_FIXED_DEGREE6_SAUNDERSON_CURVE=PRESENT
STAGE20_FIXED_CURVE_EXPONENT_AT_LEAST=1/3
```

This still does **not** order `M3` and `N2`. Stage19 may possess physical M-degree-six rational curves, and its whole population may be dominated by the moving/collective mechanism rather than any finite fixed-curve spectrum.

The remaining finite spectrum question is therefore only

```text
NEXT_FIXED_CURVE_FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
```

and the global complement theorem remains mandatory.

```text
FIXED_CURVE_SPECTRUM_IS_A_REAL_CAUSAL_DIFFERENTIAL=true
ODD_DEGREE_ANTI_INVARIANT_CONGRUENCE_IS_NEW_R3_INPUT=true
FIXED_CURVE_SPECTRUM_ALONE_RESOLVES_J28_THRESHOLD=false
GLOBAL_COMPLEMENT_RECEIVER_STILL_REQUIRED=true
ENDPOINT_COUNT_USED=false
AUDIT_REQUIRED=true
```