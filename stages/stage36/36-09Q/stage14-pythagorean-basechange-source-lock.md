# Stage36 36-09Q source lock — Stage14 Pythagorean rank-zero/torsion theorem

Accessed from repository authority at Stage36 base `c17f1a681c220292f93880a726f1f571174f53b9`.

## Authoritative retained source

- path: `stages/stage14/archive/stage14-4af-specialization-triple.md`
- blob SHA: `f14d6840d10aaa36df63b2d4a70a07d509b596ce`
- unit: Stage14-4af, COMPLETE

The exact Stage14 facts reused in 36-09Q are only:

1. the signed family
   `E_t: Y^2 = X*(X-1)*(X+t^2)`;
2. on the rational Pythagorean base `h^2=1+t^2`, parameterized by
   `t=2*u/(1-u^2)`, `h=(1+u^2)/(1-u^2)`, the pulled-back elliptic surface has geometric generic Mordell-Weil rank zero;
3. for every genuine rational Pythagorean base, the rational torsion is exactly `Z/2 x Z/4`; in particular there is no rational 8-torsion and no larger rational torsion group;
4. Stage14 does **not** prove a uniform exclusion of positive-rank specializations, nor a rank-jump frequency theorem.

Stage36 independently proves the rational isomorphism from its `E_tau` family to this signed Stage14 family and independently proves the additional second base-change condition on `u`. No Stage35-EX provisional claim is imported as authority.

## Stage36 adapter boundary

For Stage36 notation

`D=p*(p^2-1)`

`C=p^4-6*p^2+1`

`H=(p^2+1)^2`

`Nminus=p^2-2*p-1`

`Nplus=p^2+2*p-1`,

36-09Q derives

`t=C/(4*D)`, `h14=H/(4*D)`, and `h14^2=1+t^2`.

The Stage14 Pythagorean parameter is exactly

`u=Nminus/Nplus`,

with

`t=2*u/(1-u^2)`

and the additional Stage36 image condition

`2*(1+u^2) = (2*(p^2+1)/Nplus)^2`.

Conversely, away from the retained boundary denominators, the quadratic equation for `p`

`(u-1)*p^2 + 2*(u+1)*p + (1-u)=0`

has discriminant `8*(u^2+1)`, so the displayed conic square condition is exactly the rational-lift condition back to the Stage36 `p`-base.

## Credit firewall

This source lock supports only the Stage14 family theorem stated above after the explicit Stage36 adapter is verified. It does not prove:

- absence of positive-rank Stage36 specializations;
- emptiness of the Stage36 receiver condition `R^2-4 in Q^{x2}`;
- S34-W03 intersection exclusion;
- top genus-three rational-point exhaustion;
- receiver/R29-CAMP2/Q11/endpoint/perfect-cuboid closure.
