# Stage14-t7 — shared-q compatibility and local-sieve boundary

## Purpose

Stage14-t6 reduced a physical triple to simultaneous logarithmic small points on the reflected elliptic pair `E_R(s), E_W(s)`, with both quotient points arising from the same physical parameter `q`. Stage14-t7 extracts the exact arithmetic consequence of that shared-`q` lift and tests whether it already yields a fixed-prime saving.

No estimate `T(B)=o(sqrt(B))` is claimed.

## Exact shared-q identity

For a genuine physical first-face parameter put

\[
s=t^2,\qquad A=\frac{1-s}{1+s},\qquad C=\frac2s-1.
\]

The two square conditions are

\[
W^2=q^4+2Aq^2+1,
\]

\[
R^2=q^4+2Cq^2+1.
\]

Subtracting gives

\[
C-A=\frac{2}{s(1+s)},
\]

hence

\[
\boxed{R^2-W^2=\frac{4q^2}{s(1+s)}}.
\]

A physical Pythagorean base has `s=t^2` and `1+t^2=h^2` for a rational first-face hypotenuse ratio `h`. Therefore

\[
K:=\frac{2q}{t h}\in\mathbf Q
\]

and every physical triple satisfies

\[
\boxed{W^2+K^2=R^2}.
\]

Thus the shared lift forces a third rational Pythagorean relation between the two elliptic-quotient square roots. Equivalently, away from `R+W=0`, there is a rational parameter `u` with

\[
W/R=(1-u^2)/(1+u^2),\qquad K/R=2u/(1+u^2).
\]

The moving triple problem may therefore be viewed as a simultaneous small-point problem plus one explicit conic compatibility parameter.

## Fixed-prime square-class boundary

The coefficient in the difference identity is already a rational square on every physical base:

\[
\frac{4}{s(1+s)}=\left(\frac{2}{th}\right)^2.
\]

Hence the naive square-class test on

\[
(R-W)(R+W)=\frac{4q^2}{s(1+s)}
\]

adds no extra good-prime obstruction beyond the physical Pythagorean-base condition itself. In particular, one may not infer an independent `1/2` local loss from this difference and multiply such losses over fixed primes.

This does not make the reflected condition vacuous. The individual quartics

\[
q^4+2Aq^2+1,\qquad q^4+2Cq^2+1
\]

still carry distinct 2-descent data. The useful next sieve must retain those individual classes and work on the moving bad-prime support attached to the physical first face and point coordinates.

## Handoff from Stage14-s

Stage14-s4a/s4b found that physical Kummer square-class support is contained in the moving support `p|2SXH`, while the actual small-point fingerprints are highly dispersed. Stage14-s4c separately shows that a collective higher-degree explanation of a hypothetical `sqrt(B)` raw activation law would require polynomial proliferation of strata.

The t-side question is orthogonal: after a raw small point occurs, how often does the reflected family simultaneously admit a compatible small point with the same `q`? The natural t8 input is therefore the pair of reflected 2-descent classes restricted to the same moving prime support, not another fixed-prime density product.

## Honest boundary

Stage14-t7 does **not** prove nonisogeny, rank-event independence, a positive-density local loss, or `T(B)=o(sqrt(B))`. It does prove the exact shared conic relation and closes the cheapest but invalid local-sieve shortcut.

```text
STAGE14_T7=COMPLETE_SHARED_Q_CONIC_AND_LOCAL_SIEVE_BOUNDARY
SHARED_Q_DIFFERENCE_IDENTITY=R^2-W^2=4q^2/(s(1+s))
PHYSICAL_BASE_COEFFICIENT_IS_RATIONAL_SQUARE=true
TRIPLE_FORCES_AUXILIARY_RATIONAL_PYTHAGOREAN_RELATION=true
NAIVE_FIXED_PRIME_DIFFERENCE_SQUARECLASS_SAVING=false
MOVING_PRIME_SECOND_DESCENT_REQUIRED=true
SIMULTANEOUS_SMALL_POINT_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t8 reflected-pair 2-descent classes on moving bad-prime support
```
