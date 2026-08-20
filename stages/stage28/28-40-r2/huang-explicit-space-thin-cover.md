# Stage28-40-r2 — explicit Huang thin-cover exponent for the Stage19 space cover

```text
ROUTE=U12_HUANG_EXPLICIT_SPACE_THIN_COVER
STATUS=LITERATURE_ADAPTED_PENDING_FRESH_AUDIT
SOURCE=Zhizhong Huang, arXiv:2111.01509v3, revised 2026-07-17
```

PR #1276 used Huang v3 to give Stage19 a growing-prime dimension-two upper sieve, but left the independent thin-cover saving only as `some positive iota_sp`.  The proof of Huang Theorem 1.6(1) is explicit enough to match the Stage20 `eta<1/46` range exactly at theorem-species level.

## 1. Huang proof input

For a generically finite cover `f:Z->X` of degree greater than one over a smooth proper split toric base, the proof of Theorem 1.6(1) gives

\[
N_{\rm loc}(f;B)
\ll_\varepsilon
\frac{B(\log B)^{r-1}}{N^{1-\varepsilon}}
+
N^{2(r+2\dim X+1)+\varepsilon}
B(\log B)^{r-3/2+\varepsilon}.
\]

Huang then permits

\[
N=(\log B)^\lambda,
\qquad
0<\lambda<\frac1{4(r+2\dim X+1)}.
\]

Source locators: Huang v3, proof of Theorem 1.6(1), equations/lines corresponding to (10.5)--(10.6) and the displayed estimate immediately before the choice of `N`.

## 2. Exact Stage19 adapter

The already-audited Stage19/Stage24 and merged PR #1042 interfaces give:

```text
BASE_X=Y=Bl_4(P1xP1)
Y_SMOOTH_PROPER_SPLIT_TORIC=true
ANTICANONICAL_PHYSICAL_HEIGHT_MATCH=true
PICARD_RANK_r=6
DIMENSION=2
SPACE_COVER_GENERIC_DEGREE=2
SPACE_COVER_GEOMETRICALLY_INTEGRAL=true
```

The Stage19 space condition is exactly the rational-lift condition for the normalization of

\[
w^2=1+t_1^2+t_2^2.
\]

After resolving boundary rational double points, the composition to `Y` remains a proper generically finite degree-two morphism.  Every global Stage19 lift is in the adelic image counted by Huang's `N_loc`, so the theorem gives a valid upper bound for the physical Stage19 count after the already-frozen finite chamber/canonical adapters.

## 3. Explicit exponent

For this base,

\[
r=6,
\qquad \dim X=2,
\qquad 2(r+2\dim X+1)=22.
\]

With `N=(log B)^lambda`, ignoring arbitrarily small epsilon losses, the two relative log savings are

\[
\lambda
\qquad\text{and}\qquad
\frac12-22\lambda.
\]

They balance at

\[
\lambda=\frac1{46},
\]

which is strictly inside Huang's admissible range `lambda<1/44`.  Because epsilon losses remain, the endpoint is not asserted.  Therefore for every fixed

\[
0<\eta<\frac1{46}
\]

one obtains

\[
\boxed{
N_2(B)\ll_\eta B(\log B)^{5-\eta}.
}
\]

In particular one may take the endpoint-free concrete value

\[
\boxed{N_2(B)\ll B(\log B)^{5-1/50}.}
\]

## 4. Comparative significance

Stage20 already has the identical explicit Huang range from merged Stage14-e11 / PR #188:

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}
\qquad(0<\eta<1/46).
\]

Hence the two Stage28 completion covers now have matching certified **thin-cover theorem species and explicit log-saving exponent range** on the common toric base.

```text
SPACE_HUANG_ETA_ANY_LT_1_OVER_46=true
THIRD_FACE_HUANG_ETA_ANY_LT_1_OVER_46=true
THIN_COVER_EXPLICIT_ETA_RANGE_MATCH=true
```

This does not imply equal constants, equal asymptotic counts, or `M3/N2=Theta(1)`.  The proof bound depends on the cover through constants and the two rational-lift problems have different branch divisors.

It also does not improve the strongest Stage19 whole-family upper

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

which remains far stronger polynomially.

```text
GLOBAL_N2_STRONGEST_UPPER_REPLACED=false
M3_OVER_N2_ORDERING_RESOLVED=false
THIN_COVER_CONSTANTS_COMPARED=false
```
