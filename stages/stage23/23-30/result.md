# Stage23-30 — zero-density theorem plus fresh low-genus attack

EVIDENCE_LEVEL=PROVED_PLUS_SEARCH_LEDGER
CHECKPOINT=30
STATUS=RESUBMITTED_FOR_FRESH_AUDIT

For the matched primitive/canonical populations under `R=d<=B`, the audited interfaces give

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,\qquad N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]
so
\[
\boxed{N_2(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0}.
\]
This proves zero density only; it does not identify the true order of `N2` or the ratio.

## Fresh checkpoint30 attack

Checkpoint30 now contains an attack independent of checkpoint20. Starting from the audited AR-039 Stage17 family, impose the moving slice
\[
n=t,\qquad m=t+1,\qquad t\equiv1\pmod{14}.
\]
This preserves an explicit infinite primitive Stage17 source slice. The second candidate face satisfies
\[
y^2+z^2=4t^2(t+1)^2(t^2+1)(t^2+2t+2),
\]
so the `yz` second-face condition is exactly
\[
\boxed{w^2=(t^2+1)(t^2+2t+2)}.
\]
The quartic is squarefree in characteristic zero, hence its smooth projective model has genus 1. Thus checkpoint30 finds a genuine low-genus degeneration, unlike checkpoint20's fixed-`n=1` genus 2/3 slices.

An exact scan over `t=1 mod 14`, `1<=t<1,000,000` found zero hits. This is diagnostic only; no rank-zero, finiteness, or nonexistence theorem is inferred. Full derivation: `stages/stage23/23-30/new-slice-attack.md`.

The next arithmetic question is whether this elliptic curve has an admissible positive-rank/integral-point mechanism capable of producing infinitely many Stage19 objects.

```text
ZERO_DENSITY_TRANSITION_PROVED=true
FRESH_CHECKPOINT30_ATTACK=true
ATTACK_ID=AR039_CONSECUTIVE_PARAMETER_SLICE
GENUS_0_DEGENERATION_FOUND=false
GENUS_1_DEGENERATION_FOUND=true
GENUS_1_EQUATION=w^2=(t^2+1)(t^2+2t+2)
ELLIPTIC_ARITHMETIC_RESOLVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
TARGET_UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_STAGE19_FAMILY_FOUND=false
POSITIVE_POWER_TARGET_LOWER_BOUND_FOUND=false
MATCHING_HALF_POWER_FAMILY_FOUND=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
FINITE_DATA_USED_AS_PROOF=false
OLD_STAGE14_15_PRIMARY_ROUTE_REUSED=false
LOWER_BOUND_OR_OBSTRUCTION_ATTACK_STATUS=PASS_FRESH_CHECKPOINT30_ATTACK_MATERIALIZED
NEXT_CHECKPOINT_AFTER_PASS=40
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
```
