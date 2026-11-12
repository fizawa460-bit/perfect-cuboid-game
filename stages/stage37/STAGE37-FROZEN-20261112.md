# Stage37 frozen (2026-11-12)

Decision: the user froze Stage37 on 2026-11-12.

- Status before the freeze: RESEARCH_PRODUCTION_HOLD since 2026-10-12. The current item was
  A47 (`229HI-A47`), and gate `M3-T11-GATE-001` was OPEN.
- Unchanged: STATE, ledger, credit flags (`GLOBAL_COUNTING_CREDIT=0`), and the Drive-snapshot
  files.

Kernel: Stage29 `K16-C3-TERMINAL-P-OVER-M3`. The goal is P(B)/M3(B) → 0, where:

- P(B) counts perfect cuboids;
- M3(B) counts Euler bricks;
- both are primitive, with height R ≤ B.

This goal is weaker than nonexistence. Closing it would still have been a result in its own
right.

Review: `review-20261112/CONTINUATION-JUDGEMENT.md` (judgement) and
`review-20261112/AUDIT-CLAUDE-20261112.md` (audit: PASS).

## Why

Stage37 is not stopped by the degenerate-point trap that stopped Stage33, 35-EX and 36. It stops
because no known tool reaches the target.

Known bounds:

- numerator: P(B) ≪ B^{1/2+ε} (29-10);
- denominator: M3(B) ≫ B^{1/3} (29-13).

Neither route can close the gap.

1. **Numerator route: P = o(B^{1/3}).**
   - It needs a saving of B^{1/6} on the best bound. Stage14 records that even a saving of
     B^{δ} below B^{1/2} is unproved.
   - A47 covers only a special subset: the 7-full Wminus values with a small multiplier. Its
     exponents were chosen to land exactly on B^{1/3}.
   - No mechanism forces a general cuboid into that subset.
   - The card history repeats one pattern under new names (hard7 → hard10 → hard13 → Wminus):
     "small side negligible, rest OPEN".
2. **Denominator route: M3 ≫ B^{1/2+δ}.**
   - The report proves that there are no nondegenerate rational curves of degree ≤ 3 on the
     surface (Lemma L, checked by script).
   - Under the Batyrev–Manin conjecture for K3 surfaces (McKinnon, arXiv:1011.5825,
     Conj. 4.1), Lemma L gives M3 ≪ B^{1/2+ε}. So this target is expected to be false.
3. **General counting theorems (determinant method).**
   - These give exponents ≥ 3/4 for this degree-16 surface (Salberger, PLMS 2023, Thm 0.8; the
     statement was not checked against the source).
   - That is weaker than the known 1/2.
   - Removing the low-degree curves with Stage32 does not change the main term.

Under Bombieri–Lang together with the Stage32 record, P/M3 → 0 follows. This is a restatement of
a known conjecture and earns **no credit**.

## Retained results

All results below are scoped. None was re-audited unless marked.

- P(B) ≪ B^{1/2+ε} (29-10).
- M3(B) ≥ (27/(40π²)+o(1))·B^{1/3} (29-13).
- No perfect cuboid lies in the Saunderson family.
- A44: fixing Wminus leaves finitely many fibre points.
- A47: scoped to the 7-full Wminus values with a small multiplier.
- Lemma L: the curves have degree n ≥ 4. Audited by Claude, PASS.

## Open question (not a task)

Is there a degree-4 or degree-5 rational family of Euler bricks?

- The answer is a finite computation.
- A degree-4 family would give M3 ≫ B^{1/2}.
- The census suggests M3 ≈ 0.19·B^{1/2}.
- It would still not close P/M3 → 0, because o(B^{1/2}) for P is open (Stage14).

## Restart rule

Do not resume:

- forcing toward A47 / Wminus, or new "small side negligible" cards;
- route H "DEN" (M3 ≫ B^{1/2+δ});
- determinant-method attempts on the whole surface.

Restart only with one of these:

- an external theorem giving P(B) ≪ B^{1/2−δ};
- a degree-4 Euler-brick family together with a way to remove the B^{o(1)} loss in Stage14.
