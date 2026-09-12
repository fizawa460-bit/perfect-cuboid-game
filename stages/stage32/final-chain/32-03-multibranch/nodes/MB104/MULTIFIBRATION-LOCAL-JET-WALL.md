# MB104 — multfibration minimal-cusp local-jet wall

Status: **RETAINED LOCAL WALL / MB104 INCOMPLETE / NO CREDIT**

## Question

Can one close the `R8` gap simply by declaring that every FSM-minimal branch `(A,B)=(1,1)` is automatically a ramification point for each genus-5 fibration whose base block contains that node, and then summing Riemann--Hurwitz over many fibrations?

Answer: **no, not from the retained cusp packet alone**. The minimal cusp type fixes transverse exceptional multiplicity and a landing point, but leaves a first tangential jet free. At a generic point of an exceptional section that free jet can make the induced map to the fibration base unramified.

## Rank-3 fiber / exceptional intersection

For one of the six rank-3 genus-5 fibrations, Stoll--Testa give on the minimal resolution

```text
2F_Q = H - sum_{i in B_Q} E_i,
```

where `B_Q` is its eight-node base block. Since

```text
H.E_i=0,
E_i^2=-2,
E_i.E_j=0  (i!=j),
```

for `i in B_Q` one has

```text
2 F_Q.E_i = 2,
F_Q.E_i = 1.
```

Thus each such exceptional curve maps with degree one to the fibration base; away from finitely many special points it is a local section and the fibration is a submersion along it.

## Minimal cusp branch has a free tangential jet

Use the A1 resolution chart

```text
y=x*u,
z=x*u^2.
```

A minimal cusp branch has `A=B=1`, exceptional multiplicity one, and a nonzero landing coordinate `lambda`. The retained MB101/A1 data allow germs

```text
x=t,
u=lambda+c*t+O(t^2),
```

for arbitrary first tangential coefficient `c`. Downstairs this is

```text
x=t,
y=lambda*t+c*t^2+O(t^3),
z=lambda^2*t+2*lambda*c*t^2+O(t^3),
```

so the invariant orders remain `(1,1,1)` and the same minimal cusp type and landing point are preserved for every `c`.

## No automatic ramification

At a generic smooth point of the exceptional section choose local coordinates `(s,tau)` on the resolved surface such that

```text
fibration map = s,
E_i = {tau=0}.
```

The minimal branch is transverse to `E_i`, so after reparametrization it has

```text
tau=t,
s=s0+c'*t+O(t^2).
```

The cusp packet fixes `s0` (the landing point after changing section coordinate) but does not fix `c'`. For `c'!=0`, the induced map from the normalization branch to the fibration base has nonzero derivative and is unramified there.

Equivalently, in any local submersion coordinate, ramification imposes one additional first-jet equation. The `(A,B)=(1,1)` condition alone does not impose that equation.

## Consequence for the 28-fibration idea

The existence of many fibrations does not by itself multiply-charge each minimal branch in Riemann--Hurwitz. To obtain a useful summed ramification bound one must prove an additional **global tangent/jet constraint** showing that an actual low-genus carrier cannot choose the locally free first jet independently and is forced to be critical for sufficiently many fibrations.

This wall does not say that such a global constraint is impossible. It only prevents the invalid inference

```text
minimal cusp branch
=> automatic ramification in every incident genus-5 fibration.
```

## Firewalls

- No global curve is constructed.
- No statement is made at special points where the chosen fibration is not locally a submersion along the exceptional section.
- No finite `R8` bound is proved.
- MB104 remains incomplete; finite Picard enumeration is unreleased.
- No receiver/effectivity/final-milestone/theorem/endpoint/Perfect-Cuboid or merge credit.
