# Stage27-20-r305 — coefficient-separation large-sieve route

```text
TASK_ID=Stage27-20-r305
ROUTE_KIND=UPPER_REPARAMETRIZATION
PARENT_ROADMAP=Stage27-20-r304a
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
R302_REMAINS_FROZEN=true
R303_REMAINS_THEOREM_GATE_PAUSED=true
```

## Imported StructureRadar weapons

- `SR-STR-161`: separated quadratic/Jacobi large-sieve package;
- `SR-STR-165`: Gaussian prime-ideal allocation and quadratic-Hecke large-sieve package.

Both are ACTIVE only after genuine one-variable coefficient separation. Neither applies to an arbitrary correlated coefficient matrix `W(u,v)`.

## Exact target

Take the surviving Stage27-20 wall/T correlation after all already-charged physical masks and common-core conditions. The only legal new step in this route is to prove an exact representation

\[
W(u,v)=\sum_{j\le J(B)} \alpha_j(u)\beta_j(v),
\qquad J(B)=B^{o(1)},
\]

or a stronger rank-one factorization, with the transformation preserving the original physical measure up to `B^{o(1)}` multiplicity and without discarding a fixed-power part of the population.

If such a decomposition exists, apply the corresponding quadratic/Jacobi or Gaussian-Hecke large-sieve estimate blockwise, including conductor, coprimality, ray/primary normalization, and physical-height bookkeeping.

If the exact physical coefficient remains genuinely two-variable and correlated, the route stops. Replacing it by a complete or ambient bilinear family is illegal.

## Success condition

A legal separated-block estimate must produce a fixed-power saving after summing the `B^{o(1)}` blocks and restoring every retained mask. No additional unproved correlation saving may be multiplied into the ledger.

```text
SR_STR_161_IMPORTED=true
SR_STR_165_IMPORTED=true
LOW_RANK_SEPARATION_PROVED=false
ARBITRARY_MATRIX_LARGE_SIEVE_ALLOWED=false
FIXED_POWER_BLOCK_SAVING_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r305a
```
