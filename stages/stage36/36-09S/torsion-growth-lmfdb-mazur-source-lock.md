# Stage36 36-09S torsion-growth source lock

Status: source lock for exact external arithmetic facts used only in 36-09S.

## LMFDB 64.a3 / Cremona 64a1

Source: https://www.lmfdb.org/EllipticCurve/Q/64.a3/

Locked facts:
- minimal/simplified equation: `y^2 = x^3 - 4*x`;
- Mordell-Weil rank over Q: `0`;
- torsion structure over Q: `Z/2 x Z/2`.

Therefore its rational points are exactly the point at infinity and the three rational 2-torsion points with `x=0,2,-2`.

## LMFDB 24.a4 / Cremona 24a1

Source: https://www.lmfdb.org/EllipticCurve/Q/24/a/4
Isogeny-class corroboration: https://www.lmfdb.org/EllipticCurve/Q/24/a/

Locked facts:
- minimal/simplified equation: `y^2 = x^3 - x^2 - 4*x + 4 = (x-2)*(x-1)*(x+2)`;
- Mordell-Weil rank over Q: `0`;
- torsion structure over Q: `Z/2 x Z/4`.

The eight rational points are independently checked in the Stage36 verifier as
`O`, `(-2,0)`, `(1,0)`, `(2,0)`, `(0,+2)`, `(0,-2)`, `(4,+6)`, `(4,-6)`.
The LMFDB rank/torsion lock is used to certify that this explicit eight-point list is exhaustive.

## Mazur torsion classification over Q

Reference statement: Mazur's theorem: for an elliptic curve over Q,
`E(Q)_tors` is either `Z/n` for `n=1,...,10,12`, or `Z/2 x Z/(2n)` for `n=1,2,3,4`.
A convenient secondary reference with the exact statement is Andrew Sutherland, MIT 18.782 Lecture Notes 24, Theorem 24.20:
https://math.mit.edu/classes/18.782/2013fa/LectureNotes24.pdf

Use in 36-09S is narrow: because every retained `E_sigma_tau` fiber already has full rational 2-torsion `Z/2 x Z/2`, any strict torsion growth must be one of
`Z/2 x Z/4`, `Z/2 x Z/6`, or `Z/2 x Z/8`.
Thus it is enough to exclude rational order 4 and rational order 3 on retained fibers.

## Firewall

These sources do not imply any rank-jump exclusion, simultaneous-growth exclusion, S34-W03 intersection closure, receiver emptiness, R29/Q11/endpoint closure, or perfect-cuboid existence/nonexistence claim.
