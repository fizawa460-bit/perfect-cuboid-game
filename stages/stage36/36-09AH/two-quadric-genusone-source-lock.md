# Stage36 36-09AH source lock: smooth (2,2) complete intersections in P3

Accessed: 2026-09-07

This leaf uses only the standard complete-intersection facts needed after the smoothness calculation is performed directly in the Stage36 verifier.

## Source

MIT 18.726 Algebraic Geometry, Model Answers to Homework #5, problem on complete intersections:
https://math.mit.edu/~mckernan/Teaching/11-12/Spring/18.726/model5.pdf

The cited solution records:

- positive-dimensional complete intersections are connected;
- for a complete intersection `Y` of hypersurface degrees `d_1,...,d_r` in `P^n`, adjunction gives
  `K_Y = (sum d_i - n - 1) H|_Y`.

For a smooth complete intersection of two quadrics in `P^3`, this gives

`K_C = (2+2-3-1)H|_C = 0`.

A smooth connected projective curve with trivial canonical bundle has genus one.

## Stage36-specific smoothness is not imported

The current common-`u:v` curve is checked directly.  Its two equations are

```text
Qminus = A*u^2 - B*v^2 - eta*2^e*C*r^2
Qplus  = A*u^2 + B*v^2 - 2^f*D*s^2
```

with `A,B,C,D` nonzero positive odd squarefree, `eta=+/-1`, and `e,f in {0,1}`.

The verifier computes the pencil determinant exactly and checks every singular pencil kernel direction against the other quadric.  Thus no generic-smoothness assertion is imported from the source.

## Scope firewall

This source grants only the genus-one classification of the already-certified smooth `(2,2)` complete intersection.  It does not identify a `Q`-Jacobian, a Weierstrass model, a twist squareclass, Mordell-Weil group, rational point, receiver point, or endpoint conclusion.
