# Stage36 36-09AG source lock: Hilbert norm criterion and Hasse-Minkowski for conics

Accessed: 2026-09-07

This leaf reuses the audited Stage36 Hilbert-symbol source interface and adds only the standard local norm criterion and Hasse-Minkowski theorem needed to promote exact local conic solubility to a rational conic point.

## A. Reused audited Stage36 Hilbert interface

Path: `stages/stage36/36-09W/hilbert-reciprocity-source-lock.md`

Locked blob: `52952e2afd1db636a236c6bd254acadc779fe09f`

This supplies:

- the exact odd-prime quadratic Hilbert-symbol formula;
- the global product formula `prod_v (x,y)_v = 1` for `x,y in Q^x`.

No stronger Brauer-Manin, Selmer, or uniformity theorem is imported from 36-09W.

## B. Hilbert symbol as a quadratic norm criterion

Source:
- MIT 18.782 Introduction to Arithmetic Geometry, Lecture Notes 10 (Fall 2013), Definition 10.1 and Lemma 10.2:
  https://math.mit.edu/classes/18.782/2013fa/LectureNotes10.pdf

For `a,b in Q_p^x`, `(a,b)_p=1` is equivalent to the ternary quadratic form `z^2-a*x^2-b*y^2` representing zero. Equivalently, one argument is a norm from the quadratic algebra obtained by adjoining the square root of the other. The equivalence is squareclass-invariant and also covers the split case.

For this leaf the two diagonal conics are rewritten as the norm equations

```text
Qminus: A*u^2 - B*v^2 = eta*2^e*C*r^2
        <=> (AB, eta*2^e*A*C)_v = +1

Qplus:  A*u^2 + B*v^2 = 2^f*D*s^2
        <=> (-AB, 2^f*A*D)_v = +1
```

at each completion `Q_v`.

## C. Hasse-Minkowski / local-global principle for plane conics

Source:
- MIT 18.782 Introduction to Arithmetic Geometry, Lecture Notes 11 (Fall 2013), Theorem 11.12 (Hasse-Minkowski):
  https://math.mit.edu/classes/18.782/2013fa/LectureNotes11.pdf
- The same lecture, Theorem 11.1, records that a nondegenerate ternary diagonal form with all coefficients `p`-adic units is isotropic at every odd good prime.

A nondegenerate quadratic form over `Q` represents zero iff it represents zero over every completion. Hence a smooth projective plane conic has a `Q`-point iff it has a point over every `Q_v`.

## Scope firewall

The theorem is applied to `Qminus` and `Qplus` **separately**. It does not imply that the two rational points have the same projective ratio `u:v`. Therefore it does not produce a point on the coupled two-conic intersection, the genus-three receiver, `R29-CAMP2`, or the perfect-cuboid endpoint.
