# Stage32-04: exact dual caps and residual replay

This successor does not modify the audited Stage32-02/32-03 backends. It adds a new exact reduction before replaying the 28 PR #1343 `d=6,g=1` residual singletons.

For each of the 140 source-locked known classes `K_j`, a nonnegative rational relation is discovered numerically and then checked coordinate-by-coordinate over the primitive Picard lattice:

- for the 92 nonexceptional curves, `q H = 2 q K_j + sum a_i K_i`;
- for the 48 exceptional curves, `q H = 4 q K_j + sum a_i K_i`;
- every `a_i >= 0` and the target class is omitted from its own sum.

Consequently every genuinely new irreducible candidate satisfying the existing 140 nonnegative-intersection necessary conditions obeys

- `K_j.C <= floor(d/2)` for nonexceptional classes;
- `K_j.C <= floor(d/4)` for exceptional classes.

SciPy/HiGHS receives no theorem credit: it is only a candidate finder. `derive_intersection_caps.py` accepts a relation only after exact integer verification in all 64 Picard coordinates. `run_cap_z3_budget.py` then monkey-patches the audited Stage32-02 exact Z3 shard at runtime, adding only these verified upper bounds; the predecessor source remains byte-for-byte untouched.

The batch replays all 28 PR #1343 residual `(e,a)` singletons under the new caps and records exact Z3 outcomes. Even if all 28 close, this is only the `d=6,g=1` residual layer: genus-0 rows, the complete 183-row census, automorphism/orbit reduction, effectivity, and multibranch receivers remain outside scope.
