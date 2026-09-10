# Stage32 32-01-178 N354 — two-sided scalar Hurwitz interval

Status: `AUDIT_REQUIRED`. Necessary-condition adapter only.

## Audited prerequisites

N353 hostile audit PASS is review `5163144778` on exact head `0f8cee995e5c982cdb7ceceae14d69f91e65588d`, with credit bounded to the N351→N352→N353 scalar-Hurwitz chain.

For each of the two retained factor fibrations, N351 supplies integers `n_i>0`, `q_i>=0` and exceptional mass `e>=0` with

`6*n_i = 2*q_i + e`.

N352 supplies the exact retained Picard64 identity

`n_1 + n_2 = d`.

The already-audited N353 upper condition is

`d <= e + 4*g - 4`.

## New exact scalar consequences

Because `6*n_i` and `2*q_i` are even, the identity `6*n_i=2*q_i+e` forces

`e ≡ 0 (mod 2)`.

Because `q_i>=0`,

`6*n_i >= e`,

hence for each factor

`n_i >= ceil(e/6)`.

Summing both factors and using `n_1+n_2=d` gives the lower scalar condition

`d >= 2*ceil(e/6)`.

Therefore every admissible class in the N351 geometric scope must satisfy the two-sided scalar interval

`e even` and `2*ceil(e/6) <= d <= e+4*g-4`.

N354 is evaluated only on the externally audited N353 remaining population. Thus the new N354 rejection predicate is exactly

`e odd OR d < 2*ceil(e/6)`.

The predicate uses no individual exceptional vector, fixed `x4`, self-square, N260/N280/N310/N341/N349 local equality, or production-leaf assumption.

## Credit boundary

Before a fresh external hostile audit, N354 is diagnostic only. It grants no MAIN pruning credit, no N350 producer registration, no production COMPLETE/N104 release, no FULL178 completion, no theorem/receiver/endpoint/Stage32 closure, no Perfect Cuboid claim, no heavy authorization, and no merge authorization.
