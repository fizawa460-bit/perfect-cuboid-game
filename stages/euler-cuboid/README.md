# Euler-cuboid side — face-diagonal-first research track

> **ROLE:** independent research track beside the existing space-diagonal-first stages
>
> **STATUS:** E-1b finite population profile complete
>
> **IMPORTANT:** this track does not modify or reinterpret the active `stages/stage13/` work.

## 1. Purpose

This directory is the **face-diagonal-first** side of the perfect-cuboid research.

The existing Stage13 line approaches the problem from the space-diagonal side. This track starts from the opposite direction: count and classify integer-edge cuboids having integral **face diagonals**, without requiring the space diagonal to be integral.

```text
exactly one integral face
    -> directional populations ab / ac / bc
    -> two integral faces
    -> three integral faces (Euler brick)
    -> later compare with the perfect-cuboid condition
```

## 2. Canonical counting convention

E-1a locks positive integer edges in canonical order

```text
0 < a < b < c
```

with primitive normalization

```text
gcd(a,b,c) = 1.
```

Define

```text
d_ab^2 = a^2 + b^2
d_ac^2 = a^2 + c^2
d_bc^2 = b^2 + c^2
D^2    = a^2 + b^2 + c^2.
```

Use the same geometric space-diagonal height as the space-diagonal-first track:

```text
D <= B
```

implemented exactly as

```text
a^2+b^2+c^2 <= B^2.
```

The crucial Euler-side difference is that **`D` need not be an integer**.

Full definition:

```text
stages/euler-cuboid/E-1a/definition.md
```

## 3. Exactly-one populations

```text
N_ab(B): d_ab integral; d_ac,d_bc nonintegral
N_ac(B): d_ac integral; d_ab,d_bc nonintegral
N_bc(B): d_bc integral; d_ab,d_ac nonintegral
N_1(B) = N_ab+N_ac+N_bc
```

## 4. E-1b finite enumeration

E-1b enumerates all three populations under one common cutoff. At `B=10000`:

```text
N_ab = 31,593,274
N_ac = 14,373,282
N_bc = 16,389,285
N_1  = 62,355,841
```

so

```text
N_ab:N_ac:N_bc
≈ 1.927679 : 0.876993 : 1.
```

The normalized vector is

```text
(ab,ac,bc)
≈ (0.5066610, 0.2305042, 0.2628348).
```

Across `B=100` through `B=10000`, both `ab/bc` and `ac/bc` increase toward the finite shape `2:1:1`. This is an observation only; no limiting theorem is claimed.

The optimized enumerator is independently checked against literal canonical triple enumeration at `B=20,30,50,80`, with exact agreement in every direction.

Result and assets:

```text
stages/euler-cuboid/E-1b/result.md
stages/euler-cuboid/scripts/E-1b/population_enumeration.py
stages/euler-cuboid/data/E-1b/population_report.json
```

## 5. Roadmap

```text
E-1a  counting object / primitive convention / common D<=B cutoff       [complete]
E-1b  enumerate ab/ac/bc exactly-one populations and first profile       [complete]
E-1c  cutoff scaling and directional-ratio analysis                      [next]
E-1d  structural explanation of the directional profile
E-1e  finite/asymptotic synthesis of the exactly-one Euler-side layer
```

After the exactly-one layer is understood, move to the three exactly-two-face types

```text
ab+ac
ab+bc
ac+bc
```

and finally the Euler-brick population where all three face diagonals are integral.

## 6. Separation from the space-diagonal track

```text
stages/stage13/       space-diagonal-first side
stages/euler-cuboid/  face-diagonal-first / Euler side
```

The two sides use the same geometric height `D<=B`; the Euler side simply removes the condition `D in Z`. No active Stage13 file is changed by this track.

## 7. Next

`E-1c`: extend and analyze the finite cutoff profile, with particular attention to whether the observed movement toward `2:1:1` persists or eventually bends toward a different directional law.
