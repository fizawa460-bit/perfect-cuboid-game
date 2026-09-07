# Stage36 36-09W source lock: quadratic Hilbert symbols and global reciprocity

Accessed: 2026-09-06

This leaf uses only the standard quadratic Hilbert-symbol formulas listed below. No stronger Brauer-Manin, Selmer, or uniformity theorem is imported.

## A. Odd local Hilbert-symbol formula

Source:
- MIT 18.785 Number Theory, Problem Set 11 (2021), Problem 2(h): https://math.mit.edu/classes/18.785/2021fa/ProblemSet11.pdf

For a nonarchimedean local field of odd residue cardinality q, writing
`a = u_a*pi^alpha`, `b = u_b*pi^beta`, the quadratic Hilbert symbol is

`(a,b) = (-1)^(alpha*beta*(q-1)/2) * (u_a/pi)^beta * (u_b/pi)^alpha`.

For the present Q_q application, when exactly one argument has odd q-adic valuation and the other is a q-adic unit, the symbol is therefore the corresponding Legendre symbol of that unit modulo q.

## B. Global product formula

Source:
- MIT 18.782 Introduction to Arithmetic Geometry, Lecture Notes 10, Theorem 10.11: https://math.mit.edu/classes/18.782/2013fa/LectureNotes10.pdf

For `x,y in Q^x`, `(x,y)_v = 1` at all but finitely many places and

`product_v (x,y)_v = 1`.

## Scope firewall

The product formula is used only as a checksum for the parameter-only pair `(C0,D0)`. A global product equal to 1 is not an obstruction by itself. To obtain a receiver-matched obstruction one must additionally prove that receiver/Kummer local solvability forces a prescribed incompatible pattern of local Hilbert evaluations. 36-09W does not assume such a pattern.