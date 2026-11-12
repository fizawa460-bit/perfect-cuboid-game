# Stage35-EX frozen (2026-11-12)

Decision: the user froze Stage35-EX on 2026-11-12. This note records the reason.
STATE, ledger and credit flags are unchanged. Formal authority stays V74 / Goal4AK. Existing
scoped results are retained as they are.

Details are in `review-20261112/CONTINUATION-JUDGEMENT.md` (judgement) and
`review-20261112/AUDIT-CLAUDE-20261112.md` (audit, PASS).

## Why

1. **The target E1 is the perfect cuboid problem itself.**
   - In the notation of `stages/stage29/29-08`, H = (W1U2)² + (U1V2)² = e² + x² + y² is the
     squared space diagonal, and ξ² + η² = H / g0².
   - So "ξ² + η² is a square" for a Master-Hit means "that Euler brick is perfect".
   - E1 is not a weaker replacement. The word "weaker" in `MAIN-START-HERE.md` is wrong about
     strength.
2. **Line (a), the V74 local evaluation of (−1, F_B), cannot decide.**
   - It evaluates finitely many Brauer classes on an open subset of the same Stoll–Testa surface.
   - The degenerate rational point (3,4,0;4,3,5;5) forces a nonempty Brauer–Manin set
     (Stage33 Theorem 1, `stages/stage33/STAGE33-FROZEN-20261112.md`).
3. **Line (b), R3-07 and the Ward-exponent reduction, cannot reach E1.**
   - It covers only indexed points. The non-indexed part has no reduction (`06-cross-lane.md`).
   - Inside the indexed part, MID, HIGH, the odd range and Branch B all need new theorems.
     HIGH is a wall of the Stage32 shape: finite for each fixed m, but no bound on m.
   - Unconditional −30 would need the 2-part of the class group of a degree-105 field with
     norm bound 2^94, about 3e26 primes. The available discriminant bounds help only under GRH.

## Retained scoped results

Each result holds only for indexed points and the stated exponent. None gives credit for E1 or
for the perfect cuboid problem.

- ±18 excluded
- the listed Ward 3/5/7 exponents excluded
- +12 and +30 excluded
- −30 excluded under GRH (row381, audit PASS_SCOPED_DEPENDENT)
- the 155/197 uniform lower bounds

## Restart rule

Do not resume the P953 relation search, the row394+ class-group work, or the (−1, F_B) local
evaluation. A restart needs one of the following:

- a theorem that reduces non-indexed points to indexed ones, or handles them directly;
- a uniform upper bound for HIGH (the correlation bound).
