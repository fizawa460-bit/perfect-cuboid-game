# Stage36 frozen (2026-11-12)

Decision: the user froze Stage36 on 2026-11-12. It had been PARKED_PROVISIONAL since 36R-06
(2026-10-16). STATE, ledger and credit flags are unchanged, and R29-CAMP2 stays OPEN.
Stage38 (the Drive-side helper stage) has been CLOSED_FOR_NOW since 2026-10-14. Its L3
candidates were transferred into Stage36 and are frozen with it.

Kernel: Stage29 `K16-C3-CAMPEDELLI-UNIFORM-TORSOR`, receiver `R29-CAMP2`.
The idea: every perfect cuboid maps to a rational point of each Campedelli quotient
C_H = S/H, with H ≅ (Z/2)^3.

## Why

Stage36's own findings are in `ROADMAP-CURRENT.md` §2 (36R-04 to 36R-06; external review not
yet done).

1. **C_H(Q) is infinite** (36R-06 Prop. A). The degenerate Pythagorean points with a3 = 0 give
   smooth rational points on every C_H, so quotient emptiness is false.
2. **Brauer–Manin cannot decide** (36R-06 Prop. B). This matches Stage33 Theorem 1
   (`stages/stage33/STAGE33-FROZEN-20261112.md`).
3. **Descent cannot decide** (36R-05 §4.3). The trivial and boundary torsor classes carry
   genuine degenerate points at every p.
4. **The remaining theorem (T′) is the full problem.** (T′) says that for all p ∈ Q∖{0,±1},
   E_p(Q) ⊂ {t ∈ {0, ±1, ∞}}. 36R-04 shows (T′) ⇔ U(Q) = ∅.

The same obstruction stopped Stage33 and Stage35-EX: degenerate cuboids sit on the same cover as
any perfect cuboid. So local conditions, Brauer classes and descent cannot separate the two.

## Retained results

None of these gives credit for R29-CAMP2 or for the perfect cuboid problem. All are unreviewed
unless marked otherwise.

- The J vs C_H relation and the endpoint condition δ1δ2 = square (36R-04).
- A fixed-p criterion: if F1 or F2 has rank 0 (torsion Z/4×Z/2), then E_p has no retained
  point. This covers 66% of p with a < 40 (36R-05).
- The counterexample 53/8 to the uniform Selmer guess (36R-05).
- The fixed-λ results of 36-R5.

## Restart rule

Do not aim at C_H(Q) = ∅, at Brauer–Manin on U_H, or at killing the trivial or boundary classes
by local conditions. Do not extend the fixed-p register for its own sake.

Restart only with one of the following:

- a uniform theorem for the family E_p that separates degenerate points;
- an arithmetic U_H-version of a Campedelli theorem from the literature (B7);
- a usable uniform non-abelian Chabauty for the family (N5).
