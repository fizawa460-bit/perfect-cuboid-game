# Stage23-50 — fresh Stage19 surgeon search and reserve fallback

EVIDENCE_LEVEL=ATTACK_LEDGER
CHECKPOINT=50
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT

## Ordered policy

The accepted order remains: fresh Stage19 surgeon first; new compatible attack if found; otherwise Q04 then Q11. Q04/Q11 were accepted by audit and are not reopened in this repair.

## Deep fresh surgeon repair

The fresh-surgeon depth is accepted. The materialized ledger `stages/stage23/23-50/fresh-surgeon-candidate-ledger.md` contains four new candidates generated from the Stage17 Pythagorean-chain interface and pushed through the literal Stage19 contract.

The synchronized two-level Pythagorean candidate reaches the fresh receivers

\[
Q^2=u^8+14u^4v^4+v^8,
\qquad
W^2=2(u^4+v^4).
\]

Other fresh candidates are killed by positivity, primitive homothety collapse, or local-parity/high-degree square-value gates. No candidate proves a stronger upper bound or an unbounded Stage19 family.

## Current certified Stage19 lower bound

The current proved lower bound is explicitly

\[
\boxed{N_2(B)\ge3495\qquad(B\ge500{,}000{,}000)}.
\]

This is obtained from the exact Stage19 census `N2(500000000)=3495` together with monotonicity of the nested height cutoff. It is a genuine certified constant floor, not an asymptotic extrapolation.

It does **not** imply any of the following:

```text
STAGE19_UNBOUNDEDNESS_PROVED=false
STAGE19_POSITIVE_POWER_LOWER_BOUND_PROVED=false
STAGE19_MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
```

Thus the current lower-bound hierarchy is: certified constant floor 3495; unboundedness open; every positive-power lower bound open; matching half-power lower bound open.

## F50-S4 correction

For the near-diagonal slice `u=v+h`,

\[
d=((v+h)^2+v^2)^2\asymp v^4.
\]

The previous wording "an infinite survivor sequence would yield a `B^(1/4)` lower bound" was too strong and is withdrawn. Mere infinitude gives no quantitative counting rate because the surviving parameters could be arbitrarily sparse.

The correct statement is conditional: if the surviving parameters have a quantitatively dense count of order `V` up to `v<=V`, then `d\asymp v^4` would place that construction on a natural `B^(1/4)` counting scale.

```text
F50_S4_INFINITE_SEQUENCE_IMPLIES_B_QUARTER=false
F50_S4_DENSE_SURVIVOR_COUNT_COULD_YIELD_B_QUARTER_SCALE=true
```

## Accepted Q04/Q11 outcome retained

Q04 remains accepted as source-compatible but without an independent stronger global count beyond the Q06/t64 moving transverse Jacobi/Kummer boundary. Q11 remains accepted: finitely many fixed primes give only constant-density loss, while exponent/log improvement requires a growing prime range with uniformity not presently proved. Neither is re-attacked here.

## Current Stage23 boundary

The frozen theorem remains

\[
N_2(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0.
\]

No checkpoint50 repair changes the true-exponent gate or produces target unboundedness.

```text
FRESH_STAGE19_SURGEON_DEPTH_ACCEPTED=true
FRESH_CANDIDATE_GENERATION_ACCEPTED=true
STAGE19_CERTIFIED_CONSTANT_LOWER_FLOOR=N2(B)>=3495_FOR_B>=500000000
STAGE19_UNBOUNDEDNESS_PROVED=false
STAGE19_POSITIVE_POWER_LOWER_BOUND_PROVED=false
STAGE19_MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
Q04_Q11_REOPENED=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
NEXT_CHECKPOINT_AFTER_PASS=60
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
