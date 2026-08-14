# Stage23-50 — fresh Stage19 surgeon search and reserve fallback

EVIDENCE_LEVEL=ATTACK_LEDGER
CHECKPOINT=50
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT

## Ordered policy

The accepted order remains: fresh Stage19 surgeon first; new compatible attack if found; otherwise Q04 then Q11. Q04/Q11 were accepted by audit and are not reopened in this repair.

## Deep fresh surgeon repair

The previous theorem-stack reread was insufficient. The repair now materializes `stages/stage23/23-50/fresh-surgeon-candidate-ledger.md`, containing four newly generated candidate mechanisms and literal Stage19 failure/survival tests.

The strongest fresh construction is a synchronized two-level Pythagorean chain. For coprime `u>v`,

\[
x=(u^2-v^2)^2,\ y=2uv(u^2-v^2),\ p=u^4-v^4,
\]
\[
z=2uv(u^2+v^2),\ d=(u^2+v^2)^2,
\]

so `x^2+y^2=p^2` and `p^2+z^2=d^2` identically. The two added-face conditions become the explicit fresh receivers

\[
Q^2=u^8+14u^4v^4+v^8
\]

and

\[
W^2=2(u^4+v^4).
\]

The latter is locally impossible when `u,v` have opposite parity (`2 mod 16`). Same-parity primitive-parameter classes and the binary octic branch remain arithmetic gates; no infinite Stage19 family is certified.

A second fresh construction factors the desired second face by `r=q-z`. Coupled to the unit-gap Stage17 space extension, `r=1` forces `x=p` and hence `y=0`; every fixed `r>1` gives a sign contradiction after elimination. This whole subfamily is globally excluded by positivity.

A third candidate, proportional synchronization of the two Pythagorean parameter pairs, collapses after primitive normalization: the extra parameter creates only homothetic copies and cannot contribute a primitive lower bound.

A fourth near-diagonal slice `u=v+h` of the synchronized family has physical height `d~v^4`, so an infinite survivor sequence would have supplied a constructive `B^(1/4)`-scale lower-bound candidate. Odd `h` is killed by the same mod-16 obstruction; the residual even-gap class reaches explicit quartic/octic square-value gates but no identity or infinite solution family.

```text
FRESH_STAGE19_SURGEON_SEARCH=COMPLETE_WITH_GENERATED_CANDIDATE_LEDGER
FRESH_CANDIDATES_GENERATED=4
COPIED_FROM_STAGE14_15_LEDGER=false
STAGE19_CONTRACT_TESTED=true
NEW_STAGE19_SPECIFIC_ATTACK_FOUND=true
NEW_PROMOTABLE_BREAKTHROUGH=false
FRESH_NEGATIVE_RESULT=SUPPORTED
SURGEON_SEARCH_PROVES_EXHAUSTIVENESS=false
```

## Accepted Q04/Q11 outcome retained

Q04 remains accepted as source-compatible but with no independent stronger global count beyond the Q06/t64 moving transverse Jacobi/Kummer boundary. Q11 remains accepted: fixed finitely many primes give only constant-density loss, while exponent/log improvement needs a growing prime set with uniformity not presently proved. Neither was re-attacked in this repair.

## Current boundary

The frozen theorem remains

\[
N_2(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0.
\]

No fresh candidate proves a stronger upper bound, target unboundedness, or a positive-power Stage19 lower bound. The surgeon repair is a concrete negative search, not an exhaustiveness theorem.

```text
TRUE_TARGET_EXPONENT_IDENTIFIED=false
TARGET_UNBOUNDEDNESS_PROVED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_FOUND=false
MATCHING_HALF_POWER_LOWER_BOUND_FOUND=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
Q04_Q11_REOPENED=false
FINITE_DATA_USED_AS_PROOF=false
NEXT_CHECKPOINT_AFTER_PASS=60
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
```
