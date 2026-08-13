# Stage14-t4 — three elliptic types and Kummer-cover restriction

> STATUS: `STAGE14_T4_COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION`

Stage14-t4 refines the five-elliptic splitting from t3 and compares it directly with the physical Kummer height geometry of Stage14-4ah.

## 1. Five quotient factors collapse to three geometric j-types

Put

\[
s=t^2.
\]

The t3 Humbert--Edge orbifold has branch set

\[
\mathcal B_s=\left\{\infty,0,1,-\frac1s,\frac1{1-s}\right\}.
\]

Each coordinate involution quotient is the double cover of `P^1` branched at four of these five points. A convenient Legendre parameter and the resulting j-invariant are:

| factor | omitted branch | one Legendre parameter | j-invariant |
|---|---:|---:|---:|
| `E_U0` | `infinity` | `s/(s+1)` | `256 (s^2+s+1)^3 / [s^2(s+1)^2]` |
| `E_U1` | `0` | `s^2/[(s-1)(s+1)]` | `256 (s^4-s^2+1)^3 / [s^4(s-1)^2(s+1)^2]` |
| `E_U2` | `1` | `s/(s-1)` | `256 (s^2-s+1)^3 / [s^2(s-1)^2]` |
| `E_W` | `-1/s` | `-1/(s-1)` | `256 (s^2-s+1)^3 / [s^2(s-1)^2]` |
| `E_R` | `1/(1-s)` | `-1/s` | `256 (s^2+s+1)^3 / [s^2(s+1)^2]` |

Hence

\[
\boxed{j(E_{U_0})=j(E_R)},
\qquad
\boxed{j(E_{U_2})=j(E_W)}.
\]

Thus over `Qbar(s)` there are only three geometric elliptic isomorphism types. Writing them as `E_+`, `E_0`, `E_-`,

\[
\boxed{
J(C_t)_{\overline{\mathbf Q}(s)}\sim E_+^2\times E_0\times E_-^2.
}
\]

Over `Q(s)` the five t3 quotient curves remain the canonical safe factors: equal j-invariant only implies that the paired factors are twists, not automatically `Q(s)`-isomorphic. No twist-triviality is claimed in t4.

## 2. Two factors have direct Stage14 meanings

The quotient by `sigma_R` forgets the third-square coordinate `R`. Therefore `E_R` is exactly the space-square/raw-pair elliptic quotient already studied in the main `14-4` track. Its j-invariant agrees with

\[
E_t:\quad y^2=x(x-1)(x+t^2),
\]

since `s=t^2` gives

\[
j(E_t)=256\frac{(s^2+s+1)^3}{s^2(s+1)^2}.
\]

The quotient by `sigma_W` forgets the space-square coordinate `W`; it is the elliptic curve attached to the third-face quartic

\[
R^2=q^4+2\left(\frac2s-1\right)q^2+1.
\]

So the five-factor decomposition is not abstract bookkeeping: it contains the raw-pair elliptic family and the third-face elliptic family as two distinguished factors, together with three companion twists/combinations.

## 3. Imported rank/torsion information on the raw-pair factor

Stage14-4af already proves, after the actual Pythagorean base change, that the raw-pair elliptic surface has geometric generic Mordell--Weil rank zero, that genuine rational fibers have torsion

\[
\mathbf Z/2\mathbf Z\times\mathbf Z/4\mathbf Z,
\]

and that every physical raw-pair point is non-torsion and therefore lies on a positive-rank specialization.

Every triple point is in particular a raw-pair point. Consequently:

\[
\boxed{
\text{every physical triple point lies over a positive-rank specialization of }E_R.
}
\]

Thus triple bases are already contained in the main-track rank-jump locus. This is a genuine structural restriction, but it does not by itself give an additional power saving because the raw-pair population itself lives on that same locus.

No generic-rank theorem is promoted in t4 for `E_W`, `E_U0`, `E_U1`, or `E_U2`; equal j-invariant does not transfer rational rank across an uncontrolled quadratic twist.

## 4. Exact comparison with the Kummer third-square cover

Stage14-4ah locks the physical Kummer surface

\[
\pi:X\to Y,
\qquad M=\pi^*(-K_Y),
\qquad M^2=8,
\]

with physical height exactly `H_M=d`. The third-square condition defines a generically degree-two cover

\[
\rho:Z\to X
\]

whose branch divisor has class

\[
\boxed{B_\rho\sim2M}.
\]

Let `C` be a physical rational curve on `X`, not contained in the branch divisor, and put

\[
m=M\cdot C.
\]

Then the restricted branch divisor has total degree

\[
\boxed{\deg(B_\rho|_C)=2m}.
\]

If `C` is one of the extremal square-root candidates from Stage14-4ah, then

\[
C\cong\mathbf P^1,
\qquad M\cdot C=4,
\]

so the restricted third-square double cover has total branch degree `8`.

Let `r` be the number of points of `Cbar` at which the branch multiplicity is odd. After normalization, Riemann--Hurwitz gives

\[
\boxed{g(\widetilde{\rho^{-1}(C)})=\frac{r-2}{2}}.
\]

For a transverse restriction, `r=8`, hence

\[
\boxed{g=3}.
\]

Therefore a generic `M`-degree-4 rational bisection that can carry a `B^{1/2+o(1)}` raw-pair population lifts to a genus-3 curve under the triple condition. Its rational triple lifts are finite by Faltings.

This is the key t4 separation:

\[
\boxed{
\text{a generic raw-pair square-root accumulating curve does not remain rational/elliptic after imposing the third square.}
}
\]

## 5. Exact exceptional restriction that can still threaten the square-root scale

Because the total restricted branch degree is eight, the normalized lift can have genus at most one only when

\[
r\le4.
\]

Equivalently, at least four units of branch multiplicity must be absorbed into even tangency/contact. The possibilities are:

```text
r=8 -> genus 3
r=6 -> genus 2
r=4 -> genus 1
r=2 -> genus 0
r=0 -> unramified/split after normalization
```

Thus any degree-four bisection capable of supporting an infinite rational triple family must lie in the special **branch-contact locus** where the restriction of the third-square branch divisor has at most four odd support points.

This converts the vague thin-set obstruction from 14-4ah into a concrete divisor problem:

> classify `Q`-rational `M`-degree-4 bisections and determine for which of them the `2M` branch divisor has `r<=4` after restriction.

If the main `14-4ai` classification produces only finitely many physical degree-four bisections and each has `r>=6`, then their total triple contribution is finite. That implication is conditional on the still-separate bisection classification; t4 does not assume it.

## 6. What remains open

The universal five-elliptic decomposition does not itself prove `T(B)=o(sqrt(B))`. The exact remaining routes are now much narrower:

1. determine the rational twist classes and generic/specialized ranks of the three geometric elliptic types `E_+,E_0,E_-`;
2. use torsion/lift intersections on `E_W` and the companion factors to eliminate positive-rank `E_R` specializations whenever possible;
3. classify the physical `M`-degree-4 bisections from the main Kummer track;
4. audit the `2M` branch contact on each such bisection, with `r<=4` as the only low-genus danger;
5. sum any surviving special restrictions under the physical height.

```text
STAGE14_T4=COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION
ELLIPTIC_FACTOR_COUNT=5
GEOMETRIC_ELLIPTIC_J_TYPES=3
JACOBIAN_GEOMETRIC_SHAPE=Eplus^2*Ezero*Eminus^2
RAW_PAIR_FACTOR=E_R
THIRD_FACE_FACTOR=E_W
PHYSICAL_TRIPLE_IMPLIES_E_R_POSITIVE_RANK_SPECIALIZATION=true
KUMMER_TRIPLE_BRANCH_CLASS=2M
M_DEGREE4_RESTRICTED_BRANCH_DEGREE=8
GENERIC_M_DEGREE4_TRIPLE_LIFT_GENUS=3
LOW_GENUS_TRIPLE_RESTRICTION_REQUIRES_ODD_BRANCH_SUPPORT_LE_4=true
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t5 transfer gate only after main-track bisection classification / branch-contact audit, or extend t4 with explicit twist-rank analysis
```
