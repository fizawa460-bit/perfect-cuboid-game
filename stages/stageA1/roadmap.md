# StageA1 roadmap — anchored Hilbert cubes

## Mission

Test a genuinely different formulation of the perfect-cuboid problem: an anchored three-dimensional Hilbert cube in the set of squares. The first phase is deliberately short and is designed to answer one question quickly:

> Does the Hilbert-cube viewpoint generate a new necessary condition on an arbitrary perfect cuboid, rather than merely proving that some special parametrized Hilbert-cube families miss `a0=0`?

## Reconnaissance phase

### A1-1 — Exact anchored-cube dictionary

Prove and freeze the exact equivalence between a perfect cuboid `(A,B,C)` and

`H(0; A^2, B^2, C^2)`

being contained in the integer squares. Record symmetry, primitiveness/scaling, degeneracy, and positivity conventions.

Exit: exact dictionary only; no existence/nonexistence claim.

### A1-2 — Published-family anchor cuts

For each explicit 2026 dimension-3 Hilbert-cube family, impose `a0=0` and classify the rational parameter locus:

- genuine nondegenerate rational solutions;
- degenerate solutions (`ai=0`, repeated/zero increments, forbidden parameter denominator);
- rational impossibility via discriminant/factorization/local obstruction;
- unresolved curve.

Start with Theorem 1.5 and Theorem 1.6 families. Do not infer universality.

Exit: certified family-specific anchor-boundary statements.

### A1-3 — General parametric boundary geometry

Take the paper's more general parametrization before its one-parameter specializations and impose `a0=0`. Normalize by projective scaling and exploit reciprocal/permutation symmetries.

Required outputs:

1. factorization of the anchor polynomial;
2. dimension count after removing trivial/degenerate components;
3. birational classification where feasible: rational / genus 1 / genus >=2 / surface;
4. explicit map from a nondegenerate rational boundary point to an anchored Hilbert cube;
5. explicit statement of what part of the full anchored-cube moduli space this parametrization covers.

This is the first go/no-go checkpoint.

## Expansion phase — only if A1-3 passes

### A1-4 — Rational-point closure

For each nontrivial boundary curve/component from A1-3, determine rational points using elementary factorization/local methods first, then elliptic/genus-2 machinery where justified.

A family-exclusion theorem is useful but remains family-specific unless coverage is proved.

### A1-5 — Reverse map from an arbitrary perfect cuboid

Assume an arbitrary anchored cube exists and ask whether it admits the coordinates/invariants used by the published Hilbert-cube parametrization. Seek a dominance/coverage statement or a new invariant obstruction.

This stage is crucial: without a reverse map, StageA1 has not reached the general perfect-cuboid problem.

### A1-6 — Local and computational reconnaissance

Apply congruence, squareclass, 2-adic/odd-prime local tests and bounded rational searches only to the exact boundary equations produced by A1-3/A1-5. Convert observed patterns into explicit lemmas or discard them.

### A1-7 — Integration verdict

Classify StageA1 as exactly one of:

- `NEW_GENERAL_CONSTRAINT`: a new necessary condition for every perfect cuboid;
- `NEW_FAMILY_EXCLUSION`: a rigorous exclusion of a substantial parametrized Hilbert-cube family, but no general coverage;
- `NEW_STAGE27_WEAPON`: an exact adapter produces a reusable constraint for the main proof line;
- `RECONNAISSANCE_NEGATIVE`: published families are too special and no general constraint appears.

## Anti-loop rule

A task counts as substantive progress only if it does at least one of:

- proves a new identity or rational-point statement;
- removes a genuine boundary component;
- strictly enlarges the proved coverage of anchored cubes;
- derives a necessary condition for arbitrary anchored cubes;
- supplies an exact adapter to an existing proved theorem.

Renaming a boundary curve, introducing a stronger sufficient condition, or repeatedly searching literature without a changed exact receiver does not count.

### Hard stop after A1-3

If A1-1 through A1-3 only establish that special published families avoid `a0=0`, and no reverse-map/coverage mechanism or new arbitrary-cube invariant is visible, set

`STAGE_A1_STATUS=RECONNAISSANCE_NEGATIVE`

and stop. Do not proceed to A1-4 through A1-7 merely to keep the side line alive.

## Batch operation

Recommended commands after bootstrap:

- `StageA1-main-batch` — advance up to four compatible logical tasks in one PR;
- `StageA1-audit` — independently verify algebra, degeneracies, source locators, and the anti-loop decision before merge.

The reconnaissance target is A1-1 through A1-3; it should be possible to decide whether this line deserves expansion within a small number of batches.
