# Stage32 MB104 — `000707000f0f` e=2 gamma_Q principal-gluing wall

Status: **RETAINED CONDITIONAL NEGATIVE RESULT / ZERO-QUARTIC FOUR-COMPONENT GLUING ADDS NO CONDITION BEYOND COMPONENTWISE 2-TORSION / CONDUCTOR COMPARISON STILL REQUIRED / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The retained zero-quartic torsion leaf gives, conditionally on the retained ambient-H1 linearization,

```text
2D_0 ~ 0 on Q0^+,
2D_1 ~ 0 on Q1^+.
```

The explicit `gamma_Q` leaf now determines the lifted intersection graph:

```text
R_+: Q0+--Q1+,  Q0---Q1-,
R_-: Q0+--Q1-,  Q0---Q1+.
```

A tempting continuation is to glue the componentwise principal functions around this four-component cycle and hope for one extra relation coupling `D_0` and `D_1`. This note shows that the cycle obstruction is automatically trivial once the deck reciprocity forced by the global principal relation is included.

## 1. Deck-normalized principal function

The retained candidate linearization gives effective conjugate divisors

```text
G_1 ~ G_2,
tau(G_1)=G_2.
```

Choose a rational function `F` on the residual double-cover model with

```text
div(F)=G_1-G_2.
```

Then

```text
div(tau^*F)=-(G_1-G_2)=div(1/F),
```

so

```text
tau^*F=c/F
```

for one nonzero complex constant `c`. Rescaling `F` by a constant square root normalizes this to

```text
tau^*F=1/F.                                    (RECIP)
```

The two smooth intersections `R_+,R_-` are away from the divisor of `F`, so all values below are nonzero and finite.

## 2. Component functions and the four gluing equations

Let

```text
f_0 = F|_(Q0+),
f_1 = F|_(Q1+).
```

Their divisors are the retained componentwise classes `2D_0,2D_1` up to the fixed sign convention. By `(RECIP)`, after identifying deck-conjugate components with their downstairs quartics,

```text
F|_(Q0-) = 1/f_0,
F|_(Q1-) = 1/f_1.                              (MINUS)
```

For arbitrary nonzero representatives of the componentwise principal functions, write

```text
a_+ = f_0(R_+),  a_- = f_0(R_-),
b_+ = f_1(R_+),  b_- = f_1(R_-).
```

Allow one nonzero scaling constant on each irreducible component before gluing. The four edge equations are

```text
Q0+--Q1+ at R_+,
Q0---Q1- at R_+,
Q0+--Q1- at R_-,
Q0---Q1+ at R_-.
```

For a four-cycle, existence of component scalings is equivalent to one multiplicative cycle obstruction. Substituting `(MINUS)`, the obstruction is

```text
[(a_-/(1/b_-))*((1/b_+)/(1/a_+))]
 /
[(a_+/b_+)*(b_-/(1/a_-))]
 = 1.                                          (AUTO)
```

All factors cancel identically. No value of `a_±,b_±` is used.

An exact Wolfram simplification of the left side of `(AUTO)` returns `1` symbolically.

## 3. Consequence

The newly materialized nontrivial graph monodromy `gamma_Q` does **not** create an additional divisor-class condition by merely gluing the componentwise principal functions for `2D_0` and `2D_1` around the lifted zero-quartic cycle.

Once the global deck relation `tau^*F=1/F` is imposed, the four-cycle gluing compatibility is tautological. Therefore the retained componentwise restrictions

```text
O_Q0(D_0) in Pic^0(Q0)[2],
O_Q1(D_1) in Pic^0(Q1)[2]
```

and their resulting mod-4 congruences are not strengthened by this particular union-gluing replay.

This is consistent with the orientation/numerical wall: `gamma_Q` fixes the meaning of the nonzero ambient bit, but does not couple it to the hypothetical carrier conductor without a separate map from conductor loops to the ambient cycle.

## Routing consequence

Do not continue the route

```text
gamma_Q
 -> glue the already-known zero-quartic 2-torsion functions around R_±
 -> expect a new allocation congruence.
```

The load-bearing continuation remains

```text
lambda_(p;i,j) in H_1(U,Z)
 -> compare with 0 or gamma_Q
```

through an actual conductor descent map, an ambient bounding two-chain, or an equivalent residual square-root transition.

## Firewalls

- The principal-function argument inherits the candidate status of the retained `G_1~G_2` ambient-H1 linearization.
- No conductor loop is evaluated.
- No branch allocation is claimed geometrically realizable.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
