# Euler-cuboid side — face-diagonal-first research track

> **ROLE:** independent research track beside the space-diagonal-first stages
>
> **STATUS:** E-1 exactly-one population layer complete
>
> **IMPORTANT:** this track does not require the space diagonal to be integral.

## 1. Purpose

This directory is the **face-diagonal-first** side of the perfect-cuboid research.

The Stage13 line approaches from an integral space diagonal.  This track starts from the opposite direction: classify integer-edge cuboids by integral **face diagonals** while leaving the space diagonal unrestricted.

```text
exactly one integral face
    -> exactly two integral faces
    -> three integral faces (Euler brick)
    -> later bridge back toward the perfect-cuboid condition
```

## 2. Canonical counting convention

Throughout E-1,

```text
0 < a < b < c
gcd(a,b,c)=1
a^2+b^2+c^2 <= B^2.
```

Define

```text
d_ab^2 = a^2+b^2
d_ac^2 = a^2+c^2
d_bc^2 = b^2+c^2
D^2    = a^2+b^2+c^2.
```

`D<=B` is the common geometric cutoff, but **`D` need not be an integer**.

## 3. E-1 exactly-one populations

```text
N_ab(B): d_ab integral; d_ac,d_bc nonintegral
N_ac(B): d_ac integral; d_ab,d_bc nonintegral
N_bc(B): d_bc integral; d_ab,d_ac nonintegral
N_1(B) = N_ab+N_ac+N_bc.
```

`A_q(B)` denotes the corresponding raw incidence count where face `q` is integral and the other two faces are unrestricted.

## 4. Finite profile: E-1b / E-1c

At `B=10000`,

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

E-1c extends to `B=500000`:

```text
B=50000:  ab/bc = 1.996995, ac/bc = 0.910181
B=100000: ab/bc = 2.021880, ac/bc = 0.921911
B=500000: ab/bc = 2.069731, ac/bc = 0.944629
```

Thus the visible near-`2:1:1` profile is pre-asymptotic rather than the final limit.

## 5. Raw structural theorem: E-1d

For a distinguished integral face, eliminating its positive diagonal gives the real-place Gelfand--Leray weight

```text
w_q(omega)=1/s_q(omega),
s_q=sqrt(omega_i^2+omega_j^2).
```

These are exactly the Stage13 chamber weights.  With

```text
I_ab = 0.659705248705705...
I_ac = 0.3026997526726076...
I_bc = 0.2712955487578571...
I_ab+I_ac+I_bc = pi^2/8,
```

E-1d gives

```text
A_q(B) ~ [6 I_q/pi^4] B^2 log B,
A_total(B) ~ [3/(4 pi^2)] B^2 log B.
```

So the raw normalized vector is

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

or

```text
ab:ac:bc
-> 2.431684750178191 : 1.115756428951881 : 1.
```

## 6. Exactly-one theorem: E-1e

E-1e closes the overlap gap by a fixed-edge divisor argument.

For a fixed edge `n`, every Pythagorean partner `x` satisfies

```text
n^2+x^2=y^2
=>
(y-x)(y+x)=n^2.
```

Hence the number of partners is bounded by

```text
|P(n)| <= tau(n^2).
```

Any two integral faces share one edge.  Fixing that shared edge therefore gives at most `tau(n^2)^2` choices, so each pair overlap obeys

```text
O_qr(B)
 <= sum_{n<B} tau(n^2)^2
 = B^(1+o(1))
 = o(B^2 log B).
```

The triple overlap is a subset of every pair overlap and is lower order as well.

Inclusion-exclusion therefore gives

```text
N_q(B)
 = A_q(B) + o(B^2 log B)
 ~ [6 I_q/pi^4] B^2 log B.
```

Thus the final E-1 theorem is

```text
N_1(B) ~ [3/(4 pi^2)] B^2 log B
```

and

```text
(N_ab,N_ac,N_bc)/N_1
->
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913),
```

or

```text
ab:ac:bc
-> 2.431684750178191 : 1.115756428951881 : 1.
```

This is **the same normalized limit as the Stage13 integral-space-diagonal side**.

## 7. What the comparison means

The two exactly-one tracks now have parallel asymptotics:

```text
Euler / unrestricted-D:
N_q^E(B) ~ [6 I_q/pi^4] B^2 log B

space-diagonal-integral:
N_q^S(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3.
```

The space-diagonal integrality condition drastically changes the absolute density and growth scale, but the leading directional factor `I_q` survives unchanged.  This is why the two populations can exhibit the same limiting `ab/ac/bc` law despite being very different sets of cuboids.

## 8. E-1 assets

```text
E-1a/definition.md
E-1b/result.md
E-1c/result.md
E-1d/result.md
E-1e/result.md

scripts/E-1b/population_enumeration.py
scripts/E-1c/cutoff_scaling.py
scripts/E-1d/structural_chamber.py
scripts/E-1e/exact_one_synthesis_audit.py

data/E-1b/population_report.json
data/E-1c/scaling_report.json
data/E-1d/structural_chamber_report.json
data/E-1e/exact_one_synthesis_audit_report.json
```

## 9. Roadmap

```text
E-1a  counting object / primitive convention / common D<=B cutoff       [complete]
E-1b  finite ab/ac/bc exactly-one enumeration                            [complete]
E-1c  cutoff scaling and directional-ratio analysis                      [complete]
E-1d  raw structural asymptotic                                          [complete]
E-1e  overlap lower order + exactly-one synthesis                        [complete]

E-1   EXACTLY-ONE LAYER                                                   [COMPLETE]

E-2a  define exactly-two populations and begin finite census             [next]
```

The three exactly-two types are

```text
ab+ac
ab+bc
ac+bc.
```

E-1e already implies the coarse bound

```text
N_{>=2}(B)=B^(1+o(1)),
```

so this next layer is asymptotically much sparser than the exactly-one `B^2 log B` population.

## 10. Separation from the space-diagonal track

```text
stages/stage13/       space-diagonal-first side
stages/euler-cuboid/  face-diagonal-first / Euler side
```

The two sides use the same geometric height `D<=B`; the Euler side removes only the condition `D in Z`.

## 11. Next

`E-2a`: lock the exactly-two classification and run the first `ab+ac / ab+bc / ac+bc` census under the same canonical cutoff.
