# Euler-cuboid side — face-diagonal-first research track

> **ROLE:** independent research track beside the existing space-diagonal-first stages
>
> **STATUS:** bootstrap / population enumeration
>
> **IMPORTANT:** this track does not modify or reinterpret the active `stages/stage13/` work.

## 1. Purpose

This directory starts the **face-diagonal-first** side of the perfect-cuboid research.

The existing Stage13 line approaches the problem from the space-diagonal side. This track deliberately starts from the opposite direction: count and classify integer-edge cuboids having integral **face diagonals**, without requiring the space diagonal to be integral.

The first target mirrors the existing exactly-one-face analysis, but removes the space-diagonal-integrality condition entirely.

```text
exactly one integral face
    -> directional populations ab / ac / bc
    -> two integral faces
    -> three integral faces (Euler brick)
    -> later compare with the perfect-cuboid condition
```

## 2. Canonical notation

Use positive integer edges in canonical order

```text
0 < a < b < c
```

and, unless a task explicitly says otherwise, primitive normalization

```text
gcd(a,b,c) = 1.
```

Define the three face diagonals

```text
d_ab^2 = a^2 + b^2
d_ac^2 = a^2 + c^2
d_bc^2 = b^2 + c^2
```

and the space diagonal only as a recorded quantity

```text
D^2 = a^2 + b^2 + c^2.
```

For this track's initial population counts, **integrality of `D` is not an acceptance condition**.

## 3. Initial exactly-one populations

Define the three primitive canonical populations by which single face diagonal is integral.

### `ab`

```text
d_ab is integral
d_ac is nonintegral
d_bc is nonintegral
```

### `ac`

```text
d_ac is integral
d_ab is nonintegral
d_bc is nonintegral
```

### `bc`

```text
d_bc is integral
d_ab is nonintegral
d_ac is nonintegral
```

Write the corresponding counts, once a cutoff is fixed, as

```text
N_ab
N_ac
N_bc
```

The immediate question is the size and directional ratio of these three populations when the space-diagonal condition is absent.

## 4. Bootstrap plan

```text
E-1a  fix the counting object, cutoff and primitive convention
E-1b  enumerate the ab-only population
E-1c  enumerate the ac-only population
E-1d  enumerate the bc-only population
E-1e  combine and compare N_ab : N_ac : N_bc
E-1f  audit overlaps, boundary effects and normalization
```

The first stage should establish reliable finite population data before introducing asymptotic claims.

## 5. Next structural step

After the exactly-one populations are understood, introduce the three exactly-two-face types

```text
ab+ac
ab+bc
ac+bc
```

and finally the three-face condition

```text
d_ab, d_ac, d_bc all integral,
```

which is the Euler-brick population.

The space diagonal remains a separate condition until a later explicit bridge to the perfect-cuboid problem.

## 6. Separation from the space-diagonal track

Keep this directory logically independent from `stages/stage13/` while both investigations are active.

```text
stages/stage13/       space-diagonal-first side
stages/euler-cuboid/  face-diagonal-first / Euler side
```

No active Stage13 file is changed merely to start this track.

## 7. Immediate next task

Start with `E-1a`: lock the exact finite counting definition and cutoff, then enumerate the three `ab / ac / bc` exactly-one populations under the same convention.
