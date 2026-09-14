# Stage32 MB104 — genus-one P5 compact-etale correspondence cusp-width obstruction

Status: **CANDIDATE RETAINED CLOSURE OF THE UNIFORM F1-P5 EQUALITY FACE / HOSTILE AUDIT REQUIRED / NO MB104 CREDIT YET**

## Scope

Assume the exact retained equality-rigidity hypothesis:

```text
C8 = H*/Gamma[8],
Z -> C8 x C8
```

is a connected normalized product-cover component attached to an actual uniform genus-one F1-P5 carrier, and both coordinate projections

```text
f1,f2 : Z -> C8
```

are finite etale of equal degree

```text
n = 14*e*l,  e in {1,2,4}, l>=1.
```

The map `(f1,f2)` is generically one-to-one onto the irreducible product-cover component whose normalization is `Z`.

This leaf tests whether such a compact etale self-correspondence of `C8=X(8)` can have degree greater than one.

## 1. Universal-cover reduction

Let `Gamma` denote the image of `Gamma[8]` in `PSL_2(R)`. Since `C8` has genus five, its universal cover is the upper half-plane.

Choose the universal-cover coordinate on `Z` so that a lift of `f1` is the identity. Then there are

```text
Lambda <= Gamma
g in PSL_2(R)
```

with `Lambda` finite index in `Gamma`, such that a lift of `f2` is `z |-> g z` and

```text
g Lambda g^{-1} <= Gamma.
```

Put

```text
Lambda0 = Gamma cap g^{-1} Gamma g.
```

The pair map factors through `H/Lambda0`. Because `Z` is the normalization of its image in `C8 x C8`, the pair map has generic degree one. Hence

```text
Lambda = Lambda0.                                      (1)
```

In particular `g` commensurates `Gamma`.

## 2. Rationality of the commensurator element

Every finite-index subgroup of `Gamma[8]` has cusp set `P^1(Q)`. Since `Lambda0` has finite index both in `Gamma` and in `g^{-1}Gamma g`, the element `g` permutes `P^1(Q)`.

A real Möbius transformation carrying `infinity,0,1` to rational points has rational coefficients up to a common scalar. Therefore choose a primitive integral representative

```text
A = [[a,b],[c,d]],  gcd(a,b,c,d)=1,
Delta = det(A) > 0.
```

## 3. Compact etaleness forces primitive cusp widths on both standard cusps

Because `f1 : H*/Lambda0 -> H*/Gamma` is etale at the compactified cusps, its local degree above every cusp is one.

At `infinity` and `0`, the primitive parabolic generators of `Gamma[8]` are represented by

```text
U_inf = [[1,8],[0,1]],
U_0   = [[1,0],[-8,1]].
```

Thus

```text
Gamma_inf <= Lambda0 <= g^{-1}Gamma g,
Gamma_0   <= Lambda0 <= g^{-1}Gamma g,
```

so

```text
A U_inf A^{-1} in Gamma[8],
A U_0   A^{-1} in Gamma[8].                           (2)
```

For `U_inf`,

```text
A E12 A^{-1}
 = (1/Delta) * [[-ac,a^2],[-c^2,ac]].
```

Membership in `Gamma[8]` in `(2)` implies

```text
Delta | a^2, ac, c^2.
```

Likewise the `U_0` calculation gives

```text
Delta | b^2, bd, d^2.                                 (3)
```

Let

```text
x=gcd(a,c),  y=gcd(b,d),
a=x*a0, c=x*c0, b=y*b0, d=y*d0,
gcd(a0,c0)=gcd(b0,d0)=1.
```

Write

```text
Delta = x*y*delta,
delta = a0*d0-b0*c0 != 0.
```

From `(3)` we obtain

```text
|x*y*delta| divides x^2,
|x*y*delta| divides y^2.
```

Hence

```text
y*|delta| <= x,
x*|delta| <= y.
```

Therefore `|delta|=1` and `x=y`. Primitivity of `A` then gives `x=y=1`, so

```text
Delta=1.                                               (4)
```

Thus `g` is represented by an element of `SL_2(Z)`.

## 4. Degree collapse

The principal congruence subgroup `Gamma[8]` is normal in `SL_2(Z)`. By `(4)`,

```text
g^{-1} Gamma g = Gamma.
```

Using `(1)`,

```text
Lambda = Gamma,
deg(f1)=deg(f2)=1.                                     (5)
```

But equality rigidity requires

```text
deg(f1)=deg(f2)=14*e*l >= 14.
```

Contradiction.

## Candidate consequence

Conditional on the exact equality-rigidity setup and on `Z` being the normalization of its product-image (so the pair map is generically degree one), **no uniform genus-one F1-P5 equality realization exists**.

This candidate obstruction is support-independent on the equality face. If hostile audit confirms the normalization/image and compact-etale interfaces, it dominates the later `000707` e=2/e=4 conductor-sheet analysis and closes the retained uniform F1-P5 equality packet for every support to which `GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY` applies.

## Audit-critical points

A hostile audit must verify all of the following before any promotion:

1. `Z` in the retained equality-rigidity leaf is indeed the normalization of an irreducible curve component in `C8 x C8`, so `(f1,f2)` is generically degree one.
2. `etale` in the retained leaf is etale for the compact curves, including the cusps, not merely on the open modular locus.
3. Passing to `PSL_2` does not weaken the cusp-width argument; the trace-two conjugated parabolics must represent the `+I mod 8` class.
4. The degree formula `n=14*e*l` is unchanged.

## Firewalls

- This is a **candidate closure checkpoint**, not yet a hostile-audited retained closure.
- No arbitrary unequal-Picard class is closed here.
- No P6 sector is closed here.
- MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain zero pending audit and state promotion.
- No merge authorization.
