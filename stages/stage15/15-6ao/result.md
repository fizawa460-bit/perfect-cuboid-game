# Stage15-6ao - exact P3 embedding and uniform degree-four rational-point bound

Base: Stage15-6an in the current cycle. Stage15-6an proved that the small-`kappa` one-point quartic is an isotrivial `j=1728` family and identified Heath-Brown's uniform degree-four projective-curve theorem as the exact pointwise theorem species.

Stage15-6ao constructs the ordinary projective embedding and applies that theorem.

## 1. Exact coordinate squareclass split

Fix

```text
squarefree norm core k
Gaussian core orientation K=A+iB with N(K)=k
coordinate core kappa
primitive z=a+ib with N(z)~Z
```

and write

\[
x=f_K(a,b),\qquad y=g_K(a,b).
\]

In the Stage15 receiver `(x,y)=1` and

\[
\operatorname{sf}(xy)=\kappa.
\]

Hence there are unique coprime squarefree positive integers

\[
\kappa_x=\operatorname{sf}(x),
\qquad \kappa_y=\operatorname{sf}(y),
\qquad \kappa_x\kappa_y=\kappa,
\]

and positive integers `c,d` such that

\[
\boxed{x=\kappa_xc^2,\qquad y=\kappa_yd^2.}
\]

For fixed `kappa`, the number of possible prime allocations `(kappa_x,kappa_y)` is at most

\[
2^{\omega(\kappa)}=B^{o(1)}.
\]

The actual point chooses one allocation uniquely.

## 2. Ordinary P3 model

For fixed `(K,kappa_x,kappa_y)` define

\[
\mathcal C_{K,\kappa_x,\kappa_y}\subset\mathbf P^3_{a:b:c:d}
\]

by the two homogeneous quadrics

\[
\boxed{
A(a^2-b^2)-2Bab-\kappa_xc^2=0,
}
\]

\[
\boxed{
B(a^2-b^2)+2Aab-\kappa_yd^2=0.
}
\]

Multiplying these equations recovers

\[
\kappa(cd)^2=f_K(a,b)g_K(a,b).
\]

Conversely, for an actual Stage15 point the coordinate squareclass split reconstructs `c,d` uniquely as positive square roots. Thus the map from retained primitive `z` to this `P^3` curve has `O(1)` multiplicity.

The quartic branch divisor of the projection to `[a:b]` is the separable binary quartic from 6am/6an. Therefore the two-quadric intersection is geometrically smooth and geometrically integral. Its degree is `4` and its genus is `1`.

```text
STAGE15_6AO_EXACT_P3_MODEL=TWO_QUADRICS
STAGE15_6AO_P3_CURVE_DEGREE=4
STAGE15_6AO_P3_CURVE_GEOMETRICALLY_INTEGRAL=true
```

## 3. Physical Gaussian scale gives projective height

On the dyadic block `N(z)~Z`,

\[
|a|,|b|\ll Z^{1/2}.
\]

Since

\[
x+iy=Kz^2,
\]

we have

\[
|x|,|y|\le |Kz^2|\ll k^{1/2}Z.
\]

Thus

\[
|c|^2=|x|/\kappa_x\ll k^{1/2}Z,
\qquad
|d|^2=|y|/\kappa_y\ll k^{1/2}Z,
\]

so

\[
\boxed{
|a|,|b|,|c|,|d|\ll k^{1/4}Z^{1/2}.
}
\]

Because `(a,b)=1`, the four-vector `(a,b,c,d)` is already primitive as a projective representative. Dividing by any common projective gcd is unnecessary, and in any case could only reduce height.

Therefore every retained `z` maps to a rational point of projective height

\[
\boxed{H\ll k^{1/4}Z^{1/2}.}
\]

This is a direct physical/Gaussian height bridge. No elliptic canonical height is used.

## 4. Direct application of Heath-Brown Theorem 5

Heath-Brown's uniform projective-curve theorem gives, for an irreducible projective curve of degree `d`,

\[
N(C;H)\ll_{d,\varepsilon}H^{2/d+\varepsilon},
\]

uniformly in the curve coefficients.

For the degree-four curve above,

\[
N(\mathcal C_{K,\kappa_x,\kappa_y};H)
\ll_\varepsilon H^{1/2+\varepsilon}.
\]

Substituting the Stage15 height bound yields

\[
\boxed{
\#\{z:\ N(z)\asymp Z,\ \operatorname{sf}(f_Kg_K)=\kappa\}
\ll_\varepsilon
B^{o(1)} k^{1/8}Z^{1/4+\varepsilon}.
}
\]

Here the `B^o(1)` factor pays the squareclass allocation `(kappa_x,kappa_y)` and finite sign/unit conventions. Since all parameters are polynomially bounded in physical `B`, the extra `H^epsilon` may be absorbed into `B^epsilon` in later ledgers.

Freeze the pointwise fiber bound as

\[
\boxed{
M_K(\kappa;Z)
\ll_\varepsilon B^\varepsilon k^{1/8}Z^{1/4}.
}
\]

Primary theorem source:

```text
D. R. Heath-Brown,
The density of rational points on curves and surfaces,
Ann. of Math. 155 (2002), 553-598,
arXiv:math/0405392,
Theorem 5.
```

```text
STAGE15_6AO_HEATH_BROWN_THEOREM_APPLIED=true
STAGE15_6AO_POINTWISE_KAPPA_FIBER_BOUND=k^(1/8)*Z^(1/4)*B^epsilon
```

## 5. Quantifier audit

This application is pointwise for every fixed

```text
k, K, kappa, squareclass allocation, dyadic Z.
```

The implied constant depends only on `epsilon` and degree `4`, not on `K`, `kappa`, or their coefficient size. Therefore:

```text
AR-027_EXCEPTIONAL_SET_BRIDGE_REQUIRED=false
```

No average rank or average Selmer statement is used.

## 6. Physical masks

The projective curve count is an upper bound before the final Stage15 masks. Positivity, canonical direction, exact toric reconstruction, primitive physical normalization, `R<=B`, and exactly-two postfilters only delete candidates after the curve equation is imposed.

Thus retaining them as postfilters is legal for the upper bound.

## 7. What remains

The one-point small-`kappa` quartic is now quantitatively counted. The Stage15 survivor requires **two** Gaussian states `z,w` with the same coordinate core `kappa` and exact product height

\[
kN(z)N(w)\le2B.
\]

Stage15-6ap must combine the two pointwise `kappa`-fiber bounds without summing `kappa` as an unrestricted polynomial variable.

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ao
STAGE15_6AO_STARTING_GATE=UNIFORM_DEGREE4_P3_HEIGHT_ADAPTER
STAGE15_6AO_EXACT_P3_MODEL=TWO_QUADRICS
STAGE15_6AO_P3_CURVE_DEGREE=4
STAGE15_6AO_P3_CURVE_GEOMETRICALLY_INTEGRAL=true
STAGE15_6AO_PROJECTIVE_HEIGHT_BOUND=k^(1/4)*Z^(1/2)
STAGE15_6AO_HEATH_BROWN_THEOREM_APPLIED=true
STAGE15_6AO_POINTWISE_KAPPA_FIBER_BOUND=k^(1/8)*Z^(1/4)*B^epsilon
STAGE15_6AO_AVERAGED_THEOREM_USED=false
STAGE15_6AO_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AO_EXIT=TWO_SIDED_KAPPA_FIBER_COUPLING_READY
```
