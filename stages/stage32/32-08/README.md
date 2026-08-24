# Stage32-08 — high-mass signature-cell Class-2 attack

Stage32-07 closed the audited numerical orbit slice `(d,g,e)=(8,0,2)` but exposed the higher-mass signature-cell wall.  This unit tests an exact symmetry-breaking adapter before attempting a larger lattice redesign.

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

For the locked action its exact order is `64`.  The full Aut action preserves the 48 exceptional divisors, hence `H_a` acts on the selected exceptional intersection coordinates by a permutation.  The solver imposes lexicographic minimality of the 48-vector under every element of `H_a`.

This symmetry-breaking is exact **for the union of all signature cells in one fixed `(d,g,e,a)` parent**.  A group element may move a class from one signature cell to another, so an individual symmetry-reduced cell becoming UNSAT is not interpreted as original-cell emptiness.  Parent closure is legal only if every signature cell has been searched under the same global canonicality rule and no canonical survivor remains.

## First benchmark

Run a paired deterministic A/B on the first 16 immutable signature cells for both hard representatives:

```text
e8/a36
e10/a30
```

with identical solver seed, one thread, exact constraints, and a short per-cell timeout.  Compare:

```text
baseline                 : no symmetry canonicality
a-stabilizer-symmetry    : exact order-64 H_a lex canonicality
```

### Advance rule

- If the symmetry run materially reduces UNKNOWN count / node time, run the full parent inventory with the exact symmetry adapter.
- If it does not, stop adding timeout and move to the lattice-aware signature-cell backend.
- Never infer closure from sampled/A-B cells.

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
