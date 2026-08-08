# Euler-cuboid side — face-diagonal-first research track

> **ROLE:** independent research track beside the existing space-diagonal-first stages
>
> **STATUS:** E-1d raw directional structural asymptotic complete
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

For structural work, `A_q(B)` denotes the corresponding **raw** incidence count: face `q` is integral and the other two faces are unrestricted.

## 4. E-1b finite enumeration

At `B=10000`:

```text
N_ab = 31,593,274
N_ac = 14,373,282
N_bc = 16,389,285
```

so

```text
N_ab:N_ac:N_bc
≈ 1.927679 : 0.876993 : 1.
```

The optimized enumerator is independently checked against literal canonical triple enumeration at `B=20,30,50,80`, with exact agreement in every direction.

## 5. E-1c cutoff scaling

E-1c extends the profile to `B=500000`.

```text
B=50000:  ab/bc = 1.996995, ac/bc = 0.910181
B=100000: ab/bc = 2.021880, ac/bc = 0.921911
B=500000: ab/bc = 2.069731, ac/bc = 0.944629
```

Thus `ab/bc` crosses `2`; the finite profile does not settle at `2:1:1`.

Diagnostic extrapolations in `1/log B` bracket the already-proved Stage13 chamber ratio

```text
2.431684750178191 : 1.115756428951881 : 1.
```

E-1c left the common-limit question open.

## 6. E-1d structural explanation

E-1d identifies the raw Euler-side asymptotic mechanism.

For one distinguished integral face

```text
F_q=x_i^2+x_j^2-p^2=0,
```

eliminating the positive face diagonal `p` gives the real density factor

```text
1/(2p).
```

On the sphere `(a,b,c)=r*omega`, this becomes the directional weight

```text
w_q(omega)=1/s_q(omega),
s_q=sqrt(omega_i^2+omega_j^2).
```

These are exactly the Stage13-3b chamber weights. With

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
I_ab+I_ac+I_bc = pi^2/8,
```

the primitive Pythagorean / totient summation gives

```text
A_q(B) ~ [6 I_q/pi^4] B^2 log B,
A_total(B) ~ [3/(4 pi^2)] B^2 log B.
```

Therefore the raw normalized Euler-side vector is

```text
(8 I_ab/pi^2, 8 I_ac/pi^2, 8 I_bc/pi^2)
=
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913),
```

or

```text
ab:ac:bc
-> 2.431684750178191 : 1.115756428951881 : 1.
```

This is **exactly the Stage13 chamber vector**.

The two raw tracks differ only in their common scale/arithmetic factor:

```text
Euler side:
A_q^E(B) ~ [6 I_q/pi^4] B^2 log B

space-diagonal side:
A_q^S(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3.
```

So imposing an integral space diagonal strongly changes the absolute population and growth scale while leaving the leading directional factor `I_q` unchanged.

E-1d does **not** yet transfer this raw theorem to exactly-one. The remaining target is

```text
O_qr(B)=o(B^2 log B)
```

for every pair overlap.

Assets:

```text
stages/euler-cuboid/E-1d/result.md
stages/euler-cuboid/scripts/E-1d/structural_chamber.py
stages/euler-cuboid/data/E-1d/structural_chamber_report.json
```

## 7. Roadmap

```text
E-1a  counting object / primitive convention / common D<=B cutoff       [complete]
E-1b  enumerate ab/ac/bc exactly-one populations and first profile       [complete]
E-1c  cutoff scaling and directional-ratio analysis                      [complete]
E-1d  structural explanation / raw directional asymptotic                [complete]
E-1e  pair-overlap lower order and exact-one asymptotic synthesis         [next]
```

After the exactly-one layer is closed, move to the three exactly-two-face types

```text
ab+ac
ab+bc
ac+bc
```

and finally the Euler-brick population where all three face diagonals are integral.

## 8. Separation from the space-diagonal track

```text
stages/stage13/       space-diagonal-first side
stages/euler-cuboid/  face-diagonal-first / Euler side
```

The two sides use the same geometric height `D<=B`; the Euler side simply removes the condition `D in Z`. No active Stage13 file is changed by this track.

## 9. Next

`E-1e`: prove the pair-overlap populations are `o(B^2 log B)`, transfer the E-1d raw asymptotic to exactly-one, and close the first Euler-side `ab/ac/bc` population layer.
