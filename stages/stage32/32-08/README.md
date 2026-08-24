# Stage32-08 — high-mass signature-cell Class-2 attack

Stage32-07 closed the audited numerical orbit slice `(d,g,e)=(8,0,2)` but exposed the higher-mass signature-cell wall.  This unit tests exact parent-preserving symmetry and then pivots to a lattice-aware cell backend where symmetry alone does not solve the wall.

## Exact symmetry used here

The source-locked nine geometric generators of `Aut(S)` close to order `1536` on the 140 known classes.  The artificial Stage32 parent coordinate

```text
a = sum_{i=1}^{46} (K_i . C)
```

is not preserved by the full group.  Therefore full-Aut canonicality is **not** legal inside one fixed `(e,a)` parent.

Instead Stage32-08 independently closes the subgroup

```text
H_a = { g in Aut(S) : g preserves {K_1,...,K_46} setwise }.
```

For the locked action its exact order is `64`.  The full Aut action preserves the 48 exceptional divisors, hence `H_a` acts on the selected exceptional intersection coordinates by a permutation.  The benchmark imposes lexicographic minimality of the 48-vector under every element of `H_a`.

This symmetry-breaking is exact **for the union of all signature cells in one fixed `(d,g,e,a)` parent**.  A group element may move a class from one signature cell to another, so an individual symmetry-reduced cell becoming UNSAT is not interpreted as original-cell emptiness.  Parent closure is legal only if every signature cell has been searched under the same global canonicality rule and no canonical survivor remains.

## Paired deterministic A/B result

Workflow run `32676167623` benchmarked the same first 16 immutable cells in each hard parent, with seed 0, one thread and a 3-second per-cell limit.

```text
parent      mode                 UNKNOWN  UNSAT  solver seconds
----------------------------------------------------------------
e8/a36      baseline                 15      1       47.603500
e8/a36      H_a symmetry             10      6       37.976102

e10/a30     baseline                 13      3       41.704205
e10/a30     H_a symmetry             13      3       86.878605
```

Verdict:

- `e8/a36`: exact symmetry is useful as a reducer; UNKNOWN falls `15 -> 10` and runtime also falls.
- `e10/a30`: exact symmetry does **not** improve the solved-cell count and roughly doubles runtime.
- Therefore symmetry is **not** promoted as the general higher-mass solver.  In particular, do not run the full `e10/a30` parent merely with longer SMT timeouts or the same 63 lex constraints.
- A full-parent symmetry pass for `e8/a36` may be used later as a reducer/checkpoint, but the 16-cell benchmark itself has no closure credit.

The declared advance/stop rule therefore selects the next backend: an exact lattice/coset adapter for unresolved signature cells, reusing the Stage32-03 affine-lattice machinery rather than inventing a new approximate search.

## Lattice successor contract

A signature cell contributes exact linear equalities and mod-8 congruences on the 64 selected coordinates:

```text
- Picard-image congruences M*y = 0 (mod 8)
- left/right exceptional quotient signatures (mod 8)
- exact left/right A/B/C multiplicity sums
- exact q-head total
- fixed parent d/e/a identities
```

The successor must convert these into an exact affine lattice/coset, then apply the existing exact quadratic/ellipsoid machinery and all 140 intersection inequalities.  The existing Stage32-03 backend already contains exact partial-form/dual-norm pruning; that is reused, not claimed as a new theorem or algorithmic invention.

First target: one deterministic `e10/a30` cell that remains UNKNOWN in the A/B run, plus one `e8/a36` UNKNOWN cell as a control.  No all-parent launch until this bounded adapter closes or sharply reduces those cells.

## Firewalls

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PENDING
RECEIVER_CREDIT=false
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

This unit is Class-2 numerical infrastructure only.
