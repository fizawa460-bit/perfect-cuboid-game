# Stage36 36-09DU explicit Phi-descent character-function source lock

## Exact-green parent

36-09DT exact-green fixes the degree-8 isogeny `Phi:A->J`, its Q-rational constant kernel `K=ker(Phi)=(Z/2Z)^3`, and the split dual kernel `K^D=ker(Psi)=mu_2^3`, with `Psi=Phi^vee`.

## Function-evaluation descent protocol

For an isogeny of Jacobians with rational dual-kernel classes represented by divisor classes `D_i` and rational functions `f_i` satisfying `div(f_i)=2D_i` (after choosing degree-zero representatives), the connecting/Kummer map can be represented by function evaluation on a divisor representing a Jacobian point: `D |-> (f_1(D),...,f_r(D))` modulo squares. This is the standard functions-on-the-curve descent formalism; see E. F. Schaefer, *Computing a Selmer group of a Jacobian using functions on the curve*, Math. Ann. 310 (1998), 447--471, and B. Poonen--E. F. Schaefer, *Explicit descent for Jacobians of cyclic covers of the projective line*, J. Reine Angew. Math. 488 (1997), 141--188.

36-09DU uses this only to construct the explicit coordinate map. It does not infer the local image without computing `J(Q_v)/Phi A(Q_v)`.

## Fixed branch notation

Use the 36-09DT labels
`1=2i, 2=-2i, 3=i/2, 4=-i/2, 5=3i, 6=-3i, 7=i/3, 8=-i/3`.

The kernel of `Psi=(pi_tau,*,pi_sigma,*,pi_rho,*)` on `J[2]` is found by the parity condition that, for every quotient orbit partition, the pushforward subset has either even occupancy on all four orbits or odd occupancy on all four orbits. The verifier enumerates all 64 hyperelliptic `J[2]` classes and obtains exactly eight kernel classes.

A basis is

- `lambda1=[{1,2,3,4}]`,
- `lambda2=[{1,2,5,6}]`,
- `lambda3=[{1,4,5,8}]`.

## Rational descent functions

For `lambda1` and `lambda2`, take

- `F1=(t^2+4)(t^2+1/4)`,
- `F2=(t^2+4)(t^2+9)`.

For `lambda3`, over `Q(i)` the direct branch product is

`g=(t-2i)(t+i/2)(t-3i)(t+i/3)=a-i b`,

where

`a=(t^2-1)^2`, `b=(25/6)t(t^2+1)`.

Its conjugate is `a+i b`, and the curve equation gives

`z^2=(a-i b)(a+i b)=a^2+b^2`.

The exact identity

`(z+g)^2 = 2(z+a) g`

holds on the curve. Therefore `g` and the Q-rational function

`F3=2(z+(t^2-1)^2)`

represent the same squareclass over `Q(i)(C3_2)`, so `F3` is a rational function representative for the rational dual-kernel class `lambda3`.

## Credit boundary

The resulting triple `(F1,F2,F3)` source-binds the coordinate formula for the `Phi` connecting map on divisor representatives. It does not compute any local image `delta_v(J(Q_v))`, the global `Phi`-Selmer group, a pro-Selmer cokernel cardinality, `T_2 Sel(J)`, the retained-open Abel-Jacobi intersection, a Brauer-Manin obstruction, or receiver/endpoint closure.
