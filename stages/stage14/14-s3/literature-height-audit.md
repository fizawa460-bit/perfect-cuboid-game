# Stage14-s3 literature / computation audit

## Primary height theorem used

Joseph H. Silverman, *The difference between the Weil height and the canonical height on elliptic curves*, Mathematics of Computation 55 (1990), 723--743.

Stage14-s3 uses only the theorem-level fact needed here: the difference between logarithmic x-height and canonical height admits an explicit bound in terms of elliptic-curve invariants. Since the Stage14 integral family

\[
W^2=Z(Z-S^2)(Z+X^2)
\]

has coefficients and discriminant of polynomial height in the primitive Pythagorean data `(S,X,H)`, the comparison contributes `O(log H)` along this family.

No Lang height conjecture, Szpiro conjecture, BSD, parity conjecture, or uniform positive lower bound for non-torsion height is imported.

## PARI/GP computational contract

The official PARI/GP elliptic-curve documentation states that `ellheight(E,P)` computes the global Neron--Tate height for a rational point and that `ellrank(E,0)` returns unconditional rank bounds together with a list of independent non-torsion points that the descent found.

Stage14-s3 therefore uses:

- `ellheight` on exact physical first-hit points;
- `ellrank(E,0)` only to obtain deterministic positive-rank witnesses for finite inactive controls;
- no claim that the returned witness list is a saturated Mordell--Weil basis;
- no claim that its smallest returned height is the true least non-torsion height.

## Boundary

The missing theorem is not a single-fiber height comparison. It is a **uniform/average least-physical-point theorem across the moving Pythagorean-base family** strong enough to count

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

Stage14-s3 does not claim such a theorem exists in the cited sources and does not import generic elliptic-family heuristics.
