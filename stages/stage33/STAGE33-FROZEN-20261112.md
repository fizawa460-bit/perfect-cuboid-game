# Stage33 frozen (2026-11-12)

Decision: the user froze Stage33 on 2026-11-12. This note records the reason.
STATE, ledger and credit flags are unchanged. Progress stays 6/11. Retained evidence, including
V34 (the J2-adapted Kummer column, 1/10), is kept as is.

## Why the BRAUER-EXPLICIT-DAG mechanism cannot decide the problem

Details are in `review-20261112/STRATEGY-REVIEW.md` (proposal) and
`review-20261112/AUDIT-CLAUDE-20261112.md` (audit).

1. **Finite scope gives NONEMPTY, always** (Theorem 1, audit PASS with fix F1).
   - P0 = (3,4,0;4,3,5;5) is a smooth Q-point of the cuboid surface on the boundary a3 = 0.
   - Harari's formal lemma, in density form, then shows the following. For every finite
     B ⊂ Br(U), U(A)^B is nonempty, and it can be chosen arbitrarily close to P0 at finitely many
     places, the real ordered chamber included.
2. **Full scope is circular** (audit F2, Claude's argument; independent check welcome).
   - 33-03 retains Br_a(U) ⊃ X_Q^14 / ⟨…⟩, which comes from unit–character classes (χ, u).
   - An adele orthogonal to all of them has every unit value equal to one rational number at
     every place.
   - The units a2/a1, a3/a1, (b1−a2)/a3, (b2−a1)/a3, (b3−a1)/a2 and (c−b3)/a3 fix all seven
     coordinates. So the orthogonal set is just the diagonal image of U(Q).
   - "BM set empty" is therefore the perfect cuboid problem itself.

Either way, no local–global computation in Stage33 (33-13 columns, 33-08, 33-40, 33-41)
can produce a new decision.

## How this was missed

- Stage29-16 classified the kernel as "Class 2: current tools, decision-capable".
- It noted that completion "may produce a nonempty set". It did not check that the degenerate
  rational points force a nonempty set for every finite scope.
- 33-03 recorded the infinite character part, but nobody noted that it makes the
  Brauer–Manin condition tautological.

## Not covered by this argument

Descent via covers (e.g. Stage29 K16-C3-BEAUVILLE-ONE-STEP-DESCENT, étale-Brauer) is outside
this argument.

## Restart rule

Do not reopen 33-13 or any Brauer–Manin evaluation on U. A restart needs a mechanism that is not
defeated by the degenerate rational points, for example a cover whose compactification has no
trivial rational points.
