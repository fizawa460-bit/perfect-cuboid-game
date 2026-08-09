# Stage14-t16 — square-x divisor and ramified-cover boundary

## Divisor of `x` on the elliptic fiber product

On

\[
C_{0,t}:\quad U^2=A_t(x),\qquad V^2=B_t(x),
\]

both quadratics satisfy `A_t(0)=B_t(0)=1`. Hence the fiber above `x=0` consists of four distinct rational points

\[
P_{\epsilon,\delta}=(0,\epsilon,\delta),\qquad \epsilon,\delta\in\{\pm1\}.
\]

The degree-four map `x:C_{0,t}->P^1` is also unramified over infinity and has four points there. Therefore

\[
\operatorname{div}(x)=D_0-D_\infty,
\]

where `D_0` and `D_infinity` are reduced degree-four divisors.

## Consequence for the square lift

The required condition `x=r^2` adjoins `r` with

\[
r^2=x.
\]

Because all eight coefficients of `D_0+D_infinity` are odd, this quadratic extension is ramified at exactly those eight points. Riemann--Hurwitz gives

\[
2g(C_t)-2=2(2g(C_{0,t})-2)+8=8,
\]

so `g(C_t)=5`, consistently recovering t15.

This identifies an important boundary: the square-x lift is **not** an ordinary unramified elliptic `2`-cover or an `E[2]` Kummer torsor. Its class lies in

\[
\mathbf Q(C_{0,t})^*/\mathbf Q(C_{0,t})^{*2}
\]

with ramification divisor `D_0+D_infinity`. Thus ordinary Mordell--Weil modulo `2E(Q)` does not by itself count the lift. The appropriate next interface is a square-value sieve on this branched quadratic cover, equivalently through its Prym/generalized-Jacobian data, with the physical height cutoff retained.

## Boundary

```text
STAGE14_T16=COMPLETE_SQUARE_X_DIVISOR_AND_RAMIFIED_COVER_BOUNDARY
SQUARE_X_LIFT_BRANCH_COUNT=8
SQUARE_X_LIFT_GENUS=5
SQUARE_X_IS_ETALE_E2_TORSOR=false
ORDINARY_MW_MOD_2_KUMMER_REDUCTION_SUFFICIENT=false
PHYSICAL_HEIGHT_WINDOW_RETAINED=true
T_O_SQRT_B_PROVED=false
```

No bound for `T(B)` follows from the divisor calculation alone.

```text
NEXT=Stage14-t17 formulate a square-value/branched-cover sieve on C0 using the Prym or generalized-Jacobian interface and the physical height window
```
