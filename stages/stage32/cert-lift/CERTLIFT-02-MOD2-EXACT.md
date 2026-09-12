# CERTLIFT-02 — exact mod-2 MASS7 discriminator

Status: implementation ready; execution result not yet promoted. No MAIN/theorem/closure credit.

CERTLIFT-01 found the audited separator `fixed_exceptional_mass >= 7`: 1,049 closed blocks and 0 residual controls in CUT193..CUT198. CERTLIFT-02 now tests whether that separator is explained by the exact mod-2 Picard64 necessity used by CUT, without rerunning Z3/CP-SAT.

`mass7_mod2_obstruction.py` reconstructs the retained 140x64 Picard pairing matrix and the two six-boundary fibre partitions. It computes the full left kernel of `P^T mod 2`, so every integral Picard64 completion must satisfy those parity equations. For a MASS7 block, `e=8` leaves only residual exceptional mass 1; for MASS8 it leaves 0. Thus every exceptional completion is finite and exact. The script enumerates those completions, enumerates `n1+n2=8`, solves the exact equations `2*y_boundary + incidence_sum = n_pack` for the 12 boundary-normal variables, applies the exact CUT pairwise incidence inequality, and then eliminates the remaining 80 normal parities from the Picard mod-2 system.

The elimination is deterministic: row reduction of the coefficient matrix is performed once, and zero rows yield consistency masks on the right-hand side. If every exact exceptional/fibre completion violates at least one consistency mask, the block is rigorously UNSAT in the mod-2 relaxation; because this is a necessary relaxation of the integral completion problem, that contradiction is a sound obstruction and has no timeout semantics.

Two scopes are provided. `--scope current-main` tests every current-MAIN e8 prefix-surviving block, not only the six audited CUT waves. `--scope unfiltered` tests the entire 11,318-block compressed e8 terminal universe before N220/N355 filtering. A PASS in either scope is still e8/d8-specific and cannot be transferred to e10 or another stratum without an exact adapter.

Commands:

`python stages/stage32/cert-lift/mass7_mod2_obstruction.py --scope current-main --self-check`

`python stages/stage32/cert-lift/mass7_mod2_obstruction.py --scope unfiltered --self-check`

Promotion rule: only `PASS_MASS7_EXACT_MOD2_OBSTRUCTION` with zero counterexamples may advance MASS7 from an audited separator to an exact bounded-family obstruction candidate. Any surviving projected-mod2 completion is retained as a counterexample to this proof route, not relabelled UNSAT.
