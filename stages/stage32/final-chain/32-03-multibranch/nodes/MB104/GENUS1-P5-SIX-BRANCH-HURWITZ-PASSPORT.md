# Stage32 MB104 — historical explicit F1-P5 six-branch capacity wall

Status: **REPAIRED RETAINED CAPACITY EQUALITY / PRIOR FINITE-SPLIT CLAIM RETRACTED / NON-FRONTIER / NO CLOSURE / NO CREDIT**

## Scope

This file concerns only the original explicit formal F1-P5 support `S_P5_14` with node-stabilizer type counts `(5,5,4)`.  That support is historical/non-frontier: it was already excluded as an irreducible carrier by the retained negative `c=0` conic argument.

The full-deck equality leaf conditionally forces, for that explicit packet,

```text
Z subset C8 x C8,
G ~= (Z/2)^3,
Z/G=E,
g(E)=1,
Z->C8 etale of degree 56l.
```

The factor quotient `C8/G` is `P^1` with six order-two branch values, two for each of the three singular stabilizer types.  Thus the induced map

```text
phi:E -> P^1
```

has degree `56l` and is ramified only over those six values.

## Exact capacity equality

For a branch value `q`, write

```text
u_q = number of unramified points over q,
r_q = number of simple ramification points over q.
```

Then

```text
u_q+2r_q=56l.
```

Riemann--Hurwitz on the genus-one domain gives

```text
sum_q r_q=112l,
sum_q u_q=112l.
```

The explicit formal packet has exactly `112l` supported odd/minimal normalization branches.  Each such normalization point is unramified for `phi` over a branch value of its own stabilizer type.  Hence these supported branches exhaust all unramified points over the six values.

The three type totals are therefore exactly

```text
sum_(two type-1 values) u_q = 40l,
sum_(two type-2 values) u_q = 40l,
sum_(two type-3 values) u_q = 32l.
```

Equivalently the corresponding pair totals of ramified points are

```text
36l, 36l, 40l.
```

For each individual branch value only

```text
0<=u_q<=56l,
u_q even,
r_q=(56l-u_q)/2
```

is retained here.

## Retraction of the former finite-split claim

The earlier version of this file asserted

```text
u_q=8l*m_q
```

and reduced the problem to six integers whose pair sums were `(5,5,4)`.  That step implicitly assumed that all `8l` normalization branches supported at one box node must descend to the same first-factor quotient branch value.

That concentration statement has not been proved.  Different normalization branches through the same box node may lift to different fixed points in the finite product-cover fiber.  Therefore:

```text
u_q divisible by 8l
```

is **not retained**, and the former finite six-integer/Nielsen-passport reduction is withdrawn.

The valid retained conclusion is only the global capacity equality and the three stabilizer-type pair totals above.

## Frontier firewall

This historical support is not one of the current balanced16 survivors.  No `(5,5,4)` conclusion is transferred to the active masks `0000770000ff`, `00007b0000ff`, or `000707000f0f`.

No support orbit is closed by this repaired leaf; MB104/receiver/theorem/endpoint credit remains zero.  No merge authorization.
