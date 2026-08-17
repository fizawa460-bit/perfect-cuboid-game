# Stage27-20-r301p — full-2-torsion descent gives a uniform subpolynomial Selmer universe

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301o
SOURCE_STAGE=Stage20

## 1. Integral common-Jacobian model

Write the fixed first torus coordinate in lowest terms as

\[
x=\frac ab,\qquad a>b>0,\qquad (a,b)=1.
\]

R301n gives the delta-independent common Jacobian

\[
E_{a,b}:\qquad
V^2=-U(U-a^4)(U-b^4),
\]

with full rational 2-torsion.

Let

\[
S_{a,b}:=\{p:\ p\mid 2ab(a^4-b^4)\}.
\]

The displayed discriminant

\[
16a^8b^8(a^4-b^4)^2
\]

shows that every odd prime outside `S_{a,b}` is a prime of good reduction for this model.

## 2. Standard full-2-torsion descent support

For an elliptic curve with three rational 2-torsion points, the usual Kummer map may be represented by squareclasses of two of the three factors

\[
U,\qquad U-a^4,\qquad U-b^4,
\]

with the product relation supplied by the curve equation (the fixed sign is absorbed into the archimedean squareclass).

At a finite prime of good reduction away from `2`, a 2-Selmer class is unramified, so its Kummer squareclasses have even valuation there. Consequently every 2-Selmer class is represented by squareclasses supported only on `S_{a,b}` together with sign.

If

\[
\mathbf Q(S,2)
:=\{d\in\mathbf Q^*/\mathbf Q^{*2}:v_p(d)=0\pmod2\ \text{for }p\notin S\},
\]

then

\[
\boxed{
\operatorname{Sel}_2(E_{a,b})
\hookrightarrow
\mathbf Q(S_{a,b},2)^2.
}
\]

Since

\[
|\mathbf Q(S,2)|=2^{|S|+1},
\]

we obtain the completely explicit crude bound

\[
\boxed{
|\operatorname{Sel}_2(E_{a,b})|
\le 2^{2(|S_{a,b}|+1)}.
}
\]

Because `E_{a,b}(Q)[2]` has order four,

\[
2^{r_x+2}
=|E_{a,b}(\mathbf Q)/2E_{a,b}(\mathbf Q)|
\le |\operatorname{Sel}_2(E_{a,b})|,
\]

and therefore

\[
\boxed{r_x\le 2|S_{a,b}|.}
\]

This is a uniform rank-support estimate over the whole moving `x` family.

## 3. Physical cutoff makes the Selmer universe subpolynomial

R301h gives

\[
H(x)=\max(a,b)\le 2B.
\]

Hence

\[
|2ab(a^4-b^4)|\ll B^6.
\]

The standard divisor/maximal-order estimate

\[
2^{\omega(n)}=n^{o(1)}
\]

therefore gives, uniformly over every physical `x`,

\[
\boxed{
2^{|S_{a,b}|}=B^{o(1)},
\qquad
|\operatorname{Sel}_2(E_{a,b})|=B^{o(1)}.
}
\]

Equivalently,

\[
\boxed{r_x=O\!\left(\frac{\log B}{\log\log B}\right)}
\]

is available uniformly at this coarse level.

This also shows that the universe of soluble 2-covering/Kummer classes attached to one moving `x` is subpolynomial. It is consistent with, and structurally explains, the earlier r301h subpolynomial squareclass count.

## 4. Why this still does not break the half-power wall

A subpolynomial 2-Selmer **cardinality** is not the same thing as a uniform subpolynomial count of rational points of physical height.

The lattice estimate for rank `r_x` has schematic size

\[
(1+\log B)^{r_x/2}
\]

only after controlling canonical-height comparison and the Mordell--Weil lattice. Inserting the worst-case uniform bound

\[
r_x=O(\log B/\log\log B)
\]

can still produce a fixed power of `B`; without a lower regulator/minimum-height theorem it is not a subpower fiber estimate.

Thus this route proves a new **Selmer-universe compression**, but does not prove the quantitative input `phi=0` required by r301j/r301o.

The next genuinely useful theorem would have to provide at least one of:

1. a uniform or averaged regulator/minimum-height lower bound for `E_{a,b}`;
2. a uniform polynomially controlled covering-height map strong enough to turn the common-Jacobian structure into an aggregate fixed-`x` subpower point count;
3. an average-rank/average-Selmer theorem on the actually occupied `x` support with enough quantitative strength to satisfy the half-wall gate;
4. an independent strict support deficit for occupied `x`.

```text
STAGE27_20_R301P_STATUS=AUDITED_PASS_MERGED
COMMON_JACOBIAN_FULL_2_DESCENT_AVAILABLE=true
SELMER_BAD_PRIME_SUPPORT=2*a*b*(a^4-b^4)
SELMER_2_INJECTS_INTO_S_UNIT_SQUARECLASSES_SQUARED=true
UNIFORM_SELMER2_CARDINALITY_SUBPOLYNOMIAL=true
UNIFORM_RANK_BOUND=O(log B/log log B)
UNIFORM_POINT_COUNT_SUBPOWER_FROM_RANK_PROVED=false
UNIFORM_REGULATOR_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301q
STOP_REASON=UNIFORM_OR_AVERAGED_REGULATOR_HEIGHT_OR_OCCUPIED_SUPPORT_THEOREM_REQUIRED
```
