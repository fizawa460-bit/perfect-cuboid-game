# Stage36 36-09FD — fixed-Frobenius seed prime CRT forcing

## Purpose

36-09FC proved that on the exact FB factor shape the retained Selmer condition is exactly the fixed splitting condition

```text
F(Y)=Y^4-2Y^2-1 has type (2,2) modulo either P1 factor.
```

FD turns that criterion into an actual parametric forcing mechanism. Instead of factoring `P(u)/7` and then asking which Frobenius class its prime factors occupy, choose one prime `p0` in the desired fixed-quartic class first and force `p0 | P(u)` by CRT.

Entry authority is V292, exact promotion head `da9d2de92e34e4e2879370f58968d3c8e95bfa5c`, CI `34419317648 / 102691087835`. The exact fixed-p registry is 224; exact full-template count 17; partial-Legendre charts 3; one-bit criterion 1; fixed-quartic criterion 1.

## Retained arithmetic family

Write

```text
U0=17627,
M=34440,
K=729,
u=U0+M*j,
P(u)=8u^2-K^2.
```

The modulus is

```text
M=2^3*3*5*7*41.
```

The stronger progression already supplies the uniform EH no-4/no-3 conditions used by FA/FB.

## Good Frobenius seed prime

Call a prime `p0` a good FD seed if

```text
p0 = 1 (mod 8),
gcd(p0,M)=1,
F(Y)=Y^4-2Y^2-1 has factorization type (2,2) modulo p0.
```

Because `p0=1 mod 8`, `2` is a square modulo `p0`. Choose `r` with

```text
r^2=2 (mod p0).
```

Then the two solutions of

```text
P(u)=0 (mod p0)
```

are exactly

```text
u = +K/(2r) (mod p0),
u = -K/(2r) (mod p0).
```

Indeed `8u^2=K^2` is equivalent to `(2r*u)^2=K^2`. Both roots are nonzero and distinct because `p0` is odd and does not divide `K`.

Since `gcd(M,p0)=1`, each root gives one and only one residue class

```text
j=j_+(p0) (mod p0),
j=j_-(p0) (mod p0)
```

under `u=U0+Mj`. Therefore every good seed produces two infinite CRT subprogressions modulo `M*p0` on which `p0 | P(u)` identically.

## Conditional forcing theorem

Now restrict to either FD CRT subprogression and suppose an actual arithmetic row has the exact FB factor shape

```text
d=u prime,
f=2u+729 prime,
e=4u+729 prime,
P=7*p1*p2 with distinct p1,p2 primes =1 mod 8,
|Q|=41*q1*q2 with distinct q1,q2 primes =7 mod 8.
```

Because `p0 | P`, `p0 != 7`, and the displayed factorization is squarefree away from 7,

```text
p0 is exactly one of p1,p2.
```

By construction `F mod p0` has type `(2,2)`. The exact FC theorem then gives

```text
B=-1
=> rank_F2 M_Sel2=22
=> dim_F2 Sel^2(E_rho,p/Q)=2
=> the retained fixed-p physical receiver sector is empty.
```

Thus the desired Frobenius sign is not checked after factorization: it is forced before factorization by the choice of the CRT progression.

The theorem is uniform over every FB-factor-shape realization lying on either subprogression. It does not assert that infinitely many such factor-shape realizations occur.

## Concrete seed p0=17

Take

```text
p0=17.
```

Modulo 17, `6^2=2` and

```text
F(Y)=(Y^2-7)(Y^2-12).
```

The nonzero quadratic residues mod 17 are

```text
1,2,4,8,9,13,15,16,
```

so both 7 and 12 are nonsquares. Hence the factorization type is exactly `(2,2)`.

The roots of `P(u)=0 mod 17` are

```text
u=3,14 (mod 17).
```

Since

```text
U0=15 (mod 17),
M=15 (mod 17),
```

these become

```text
j=6,9 (mod 17).
```

Equivalently the two forced u-progressions are

```text
u=224267 (mod 585480),
u=327587 (mod 585480),
```

where `585480=34440*17`.

Two already-promoted FB witnesses lie on the first branch:

```text
j=47691 = 6 (mod 17),  u=1642495667,
j=73259 = 6 (mod 17),  u=2523057587.
```

In both rows the fixed P1 factor is literally 17, exactly as the theorem predicts.

## More seed primes

The construction is not special to 17. For example, direct exact finite-field checks give good seeds

```text
17, 73, 89, 97, 193, 233, 241, 281, 401, 433, ...
```

Only the general seed theorem and the concrete seed 17 are promoted here; the displayed list is illustrative and carries no density claim.

## What FD changes

The route has now compressed and then forced the Selmer condition:

```text
full 45-bit Legendre pattern
 -> partial charts
 -> one moving bit B
 -> one fixed quartic Frobenius type
 -> two explicit CRT progressions from any good seed prime.
```

No new finite fixed-p orbit is needed for the theorem, so the exact registry remains 224.

The next leaf is

```text
36-09FE_RHO_FORCED_CRT_FACTOR_SHAPE_REALIZATION_PREFLIGHT.
```

FE asks whether the remaining FB factor-shape conditions can be realized or controlled along one of the forced CRT progressions. The Frobenius bit itself is no longer an open condition there.

## Credit firewall

FD does not prove infinitely many FB-factor-shape realizations on the forced progressions, does not prove simultaneous primality of `u,2u+729,4u+729`, does not prove the required two-prime factorizations of `P/7` and `|Q|/41`, does not claim the FB sign necessary, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
