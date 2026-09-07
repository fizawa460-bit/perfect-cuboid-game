# Stage36 36-09BC source lock: punctured good-prime boundary neighborhoods and elliptic quotient no-loop

This leaf uses only the exact BB equations plus an elementary unit-Jacobian Hensel/implicit-function argument. The local statement is recorded self-containedly here rather than importing a new external theorem species.

## BB closed joint system

Write

```text
F1 = R^2  - kappa*(1-t^2),
F2 = S^2  - 2*(1+t^2),
F3 = Zm^2 - kappa*(1-lambda^2*t^2),
F4 = Zp^2 - 2*(1+lambda^2*t^2).
```

At the AY boundary choose the rational point

```text
t0 = 1/lambda,
Zm0 = 0,
Zp0 = 2,
R0^2 = kappa*(1-t0^2),
S0^2 = 2*(1+t0^2),
```

where hostile-audited AY/BA supplies rational nonzero `R0,S0` on the retained parameter open.

Treat `Zm` as the local parameter and solve the four equations for `(R,S,t,Zp)`. The Jacobian minor at the boundary, using columns `(R,S,t,Zp)`, has diagonal factors after elementary row elimination

```text
2*R0,
2*S0,
2*kappa*lambda,
4.
```

Therefore its exact determinant is

```text
(2*R0)*(2*S0)*(2*kappa*lambda)*(4)
= 32*R0*S0*kappa*lambda != 0.
```

The 36-09BC verifier reconstructs the full 4x4 Jacobian minor and computes its determinant exactly; the coefficient `32` is not supplied to that determinant routine as an input.

Hence for every odd prime `ell` at which `2,R0,S0,kappa,lambda` are all units, the unit-Jacobian Hensel recursion uniquely solves `(R,S,t,Zp)` for every sufficiently small `Zm in ell Z_ell`. Taking nonzero sufficiently divisible `Zm` gives `Q_ell` points arbitrarily close to the boundary but off `Zm=0`. Thus the punctured retained-open neighborhood is locally nonempty at every such good prime.

This statement is only a local-neighborhood result. It does not assert a global rational point, nor local solubility at the finite set of bad primes dividing `2*R0*S0*kappa*lambda`.

## Elliptic quotient no-loop

From a BB point define

```text
X = 1/t^2,
Wminus = R*Zm/(kappa*t^3),
Wplus  = S*Zp/(2*t^3).
```

Then exact multiplication gives

```text
Wminus^2 = X*(X-1)*(X-lambda^2),
Wplus^2  = X*(X+1)*(X+lambda^2).
```

These are exactly the normalized `E_minus` / `E_plus` same-`X` equations already isolated in 36-09AA/36-09AC with `lambda=k=P/M`. Therefore discarding the individual BB square-root data and attacking only these elliptic quotients strictly forgets information and returns to an already-audited weaker receiver. It may be used as a consistency quotient, but not charged as a new filter.

## Cycle consequence

The two natural BC subroutes are therefore classified as follows:

- generic good-prime boundary-neighborhood local exclusion: structurally blocked, because punctured local points exist near the boundary;
- quotient-only elliptic correspondence: dominated by the previously audited AA/AC same-`X` receiver.

Any next local attack must use the finite parameter-dependent bad places, while any global attack must retain the full BB cover data rather than only the elliptic quotient.
