# Stage27-19-r8b — polynomial cancellation divisor receiver

```text
TASK_ID=Stage27-19-r8b
PARENT_ROUTE=Stage27-19-r8a
ROUTE_KIND=LOWER_CANCELLATION_RECEIVER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

For homogeneous toric data `(P,Q)` of degree `d_x` and `(R,S)` of degree `d_y`, the raw reconstructed edges are

\[
E_0=4PQRS,
\quad X_0=2RS(P^2-Q^2),
\quad Y_0=2PQ(R^2-S^2).
\]

A nonconstant common factor `G` capable of lowering physical degree must divide all three expressions. Because primitive homogeneous pairs satisfy `gcd(P,Q)=gcd(R,S)=1` in the polynomial ring after removing pairwise content, any such common divisor must arise from cross-incidences between factors of `PQ`, `RS`, `P^2-Q^2`, and `R^2-S^2`.

More precisely, after pairwise primitive normalization, every irreducible factor of a common `G` must divide at least one of the cross gcds

\[
\gcd(PQ,R^2-S^2),\qquad \gcd(RS,P^2-Q^2),
\]

or be one of the harmless constant/characteristic-two factors. Thus the cancellation mechanism is not mysterious: a new lower family with `g>0` requires a **polynomial cross-divisibility identity** coupling the two Pythagorean parameters.

R502 is the calibration example: its degree-four common factor is exactly produced by such a cross-coupling. Therefore the next constructive receiver is:

> Find a rational physical curve on the Stage19 host for which the two toric parameter pairs satisfy a new cross-divisibility identity of degree large enough that `2d_x+2d_y-g<=7`.

This is stronger and more searchable than the generic phrase “stronger cancellation.” It also separates genuine structural cancellation from residual integer gcd effects, which cannot improve the exponent when uniformly bounded.

No new cross-divisibility identity is proved here.

```text
COMMON_FACTOR_REDUCED_TO_CROSS_DIVISIBILITY=true
CANCELLATION_RECEIVER_MATERIALIZED=true
TARGET=deg(cross common factor) > 2dx+2dy-8
R502_CALIBRATION_CONSISTENT=true
NEW_CROSS_IDENTITY_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r8c
```
