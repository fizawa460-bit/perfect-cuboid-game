# E-1a — counting definition

> **STATUS:** `E_1A_COUNTING_CONVENTION_LOCKED`
>
> **TRACK:** face-diagonal-first / Euler side
>
> **SPACE-DIAGONAL INTEGRALITY:** not required

## Object

Count positive integer edge triples in canonical order

```text
0 < a < b < c
```

with primitive normalization

```text
gcd(a,b,c)=1.
```

Define

```text
d_ab^2 = a^2+b^2
d_ac^2 = a^2+c^2
d_bc^2 = b^2+c^2
D^2    = a^2+b^2+c^2.
```

## Cutoff

Use the same geometric space-diagonal height as the space-diagonal-first track:

```text
D <= B.
```

On this Euler-side track, `D` need not be an integer. The cutoff is tested exactly without floating point by

```text
a^2+b^2+c^2 <= B^2.
```

Thus the comparison with the space-diagonal-first population changes only the acceptance condition `D in Z`, not the geometric height convention.

## Exactly-one directional populations

For each primitive canonical triple under the cutoff, test the three face sums for being perfect squares.

```text
N_ab(B): a^2+b^2 is a square,
         a^2+c^2 and b^2+c^2 are not squares.

N_ac(B): a^2+c^2 is a square,
         a^2+b^2 and b^2+c^2 are not squares.

N_bc(B): b^2+c^2 is a square,
         a^2+b^2 and a^2+c^2 are not squares.
```

The total exactly-one population is

```text
N_1(B)=N_ab(B)+N_ac(B)+N_bc(B).
```

No condition is imposed on whether `D^2` is a perfect square.

## Separation from the space-diagonal-first track

The two populations can therefore be compared under one common height:

```text
space-diagonal-first:
  D <= B and D is integral

Euler-side E-1:
  D <= B with no integrality requirement on D
```

This is the canonical E-1a counting convention unless a later task explicitly introduces a different control cutoff.

## Next

`E-1b`: enumerate `N_ab(B), N_ac(B), N_bc(B)` at increasing cutoffs and record the first directional population profile.
