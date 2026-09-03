# Stage35-EX 35EX-05 — four-factor square descent

## Purpose

Use the additive information that 35EX-04 deliberately did not spend. The goal is to eliminate the original `(a,b)` scale from a hypothetical E1 counterexample and expose a factor-square receiver suitable for the formal Stage34 weapon `S34-W01`.

This is a new exact conditional reduction, not a proof of E1.

---

## Branch L: `k1<k2`

From 35EX-03:

```text
p*(r^2-s^2) = W1*U2/c,
q*(u^2-v^2) = V1*U2/c,
p*r*s = q*u*v.
```

Use the Euclid identities

```text
W1-V1=(a-b)^2,
W1+V1=(a+b)^2.
```

Subtract and add the first two displayed equations:

```text
p(r^2-s^2)-q(u^2-v^2) = (a-b)^2*U2/c,
p(r^2-s^2)+q(u^2-v^2) = (a+b)^2*U2/c.
```

Multiply by `u*v` and use `q*u*v=p*r*s`. The two elementary identities

```text
u*v*(r^2-s^2)-r*s*(u^2-v^2)
  = (r*u+s*v)*(r*v-s*u),

u*v*(r^2-s^2)+r*s*(u^2-v^2)
  = (r*u-s*v)*(r*v+s*u)
```

give

```text
u*v*(a-b)^2*U2/c
  = p*(r*u+s*v)*(r*v-s*u),

u*v*(a+b)^2*U2/c
  = p*(r*u-s*v)*(r*v+s*u).
```

All factors on the right are positive: the first identity forces `r*v>s*u`, and the second forces `r*u>s*v`.

Taking the ratio cancels `p`, `u*v`, and `U2/c`:

```text
((a-b)/(a+b))^2
 = [(r*u+s*v)*(r*v-s*u)]
   /[(r*u-s*v)*(r*v+s*u)].
```

Therefore the integer product

```text
L1*L2*L3*L4
```

is a square, where

```text
L1=r*u+s*v,
L2=r*v-s*u,
L3=r*u-s*v,
L4=r*v+s*u.
```

Equivalently:

```text
(r*u+s*v)*(r*v-s*u)*(r*u-s*v)*(r*v+s*u) = square.
```

This condition involves only the two primitive Pythagorean parameter pairs `(r,s)` and `(u,v)`.

---

## Branch R: `k1>k2`

Now 35EX-03 gives

```text
p*(r^2-s^2) = W1*U2/c,
2*q*u*v      = V1*U2/c,
2*p*r*s      = q*(u^2-v^2).
```

Subtract/add the first two equations and multiply by `u^2-v^2`. Using the cross-equation gives

```text
(u^2-v^2)*(a-b)^2*U2/c
 = p*[(r^2-s^2)(u^2-v^2)-4*r*s*u*v],

(u^2-v^2)*(a+b)^2*U2/c
 = p*[(r^2-s^2)(u^2-v^2)+4*r*s*u*v].
```

Factor the brackets:

```text
(r^2-s^2)(u^2-v^2)-4rsuv
 = [r(u-v)-s(u+v)]*[r(u+v)+s(u-v)],

(r^2-s^2)(u^2-v^2)+4rsuv
 = [r(u-v)+s(u+v)]*[r(u+v)-s(u-v)].
```

The first factor in each second bracket is positive; positivity of the whole identities therefore forces the remaining factors positive as well. Taking the ratio gives

```text
((a-b)/(a+b))^2
 = [R1*R2]/[R3*R4],
```

where

```text
R1 = r*(u-v)-s*(u+v),
R2 = r*(u+v)+s*(u-v),
R3 = r*(u-v)+s*(u+v),
R4 = r*(u+v)-s*(u-v).
```

Hence

```text
R1*R2*R3*R4 = square.
```

Again the original `(a,b)` parameter has disappeared from the square condition.

---

## Why this is materially stronger than 35EX-04

35EX-04 showed that the multiplicative cross-equation alone is a coprime product rectangle and therefore cannot be treated as an obstruction.

35EX-05 spends the additive equations and obtains a **new four-factor square receiver** in each branch. This is precisely the structural shape routed by formal Arsenal weapon

```text
S34-W01 SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT.
```

The source contract still has to be re-proved here: Stage34 branch counts, squareclasses, coefficients, local primes, and family theorem do not transfer.

## Next exact leaf

```text
35EX-06_FOUR_FACTOR_GCD_AND_SQUARECLASS_SUPPORT
```

Required before any finite branch claim:

1. derive exact pairwise gcd support for the four `L_i` and four `R_i`;
2. separate odd-prime valuation parity from the 2-adic part;
3. decide whether shared-prime support reduces to a finite squareclass family or still contains an unbounded cross-gcd;
4. only if finite exhaustiveness is proved may low-genus/local closure be invoked.

## Credit boundary

```text
FOUR_FACTOR_SQUARE_REDUCTION_PROVISIONAL=true
FINITE_SQUARECLASS_REDUCTION_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
