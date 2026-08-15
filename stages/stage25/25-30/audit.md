# Stage25-30 fresh audit

Status: **FAIL — global endpoint theorem accepted; directional channel repair required**

## Accepted checkpoint30 mathematics

The global endpoint theorem is correct under the audited Stage25 population contract.

From

- `M1(B) ~ 3/(4*pi^2) B^2 log B`, and
- `sqrt(log B) << N2(B) <<_epsilon B^(1/2+epsilon)`,

we obtain

```text
B^-2 (log B)^(-1/2) << N2(B)/M1(B)
N2(B)/M1(B) <<_epsilon B^(-3/2+epsilon) (log B)^(-1)
N2(B)/M1(B) -> 0
N2(B) -> infinity
```

The classification

```text
ENDPOINT_RATIO_CLASS=VANISHING_POPULATION_RATIO_WITH_INFINITE_TARGET
```

is accepted.

Path A and Path B are also correct:

```text
(M2/M1)(N2/M2)=N2/M1
(N1/M1)(N2/N1)=N2/M1
```

and both reproduce the direct endpoint polynomial/logarithmic envelope. These are exact count cancellations only; no probabilistic independence is inferred.

## Blocking defect — directional source channel mismatch

The submitted directional refinement is not currently justified by the cited Stage21 interface.

Stage21's directional asymptotic is written in terms of `M1,q(B)` and `N1,q(B)` with the common positive **order-chamber** factor `I_q`. Its final bundle explicitly uses the chamber index `q` in the imported formulas

```text
M1,q(B) ~ 6 I_q/pi^4 * B^2 log B
N1,q(B) ~ kappa I_q/(3*pi^3) * B(log B)^3.
```

By contrast, the post-Stage24 Stage23 result defines `N2,c` as the exactly-two target channel whose two integral faces are `ac` and `bc`, i.e. a **shared-edge / face-mask channel**.

The checkpoint30 submission silently replaces these two different indexing systems by a common symbol `j` and states

```text
M1,j(B) ~ c_j B^2 log B, c_j>0
```

for the Stage23 `a,b,c` target directions. No adapter proving that a Stage23 shared-edge channel is a fixed union of Stage21 order chambers, with the required positive leading source constant under the same counting convention, is supplied.

Therefore the following checkpoint30 claims are **not accepted yet**:

```text
DIRECTIONAL_UPPER_ALL=PROVED
DIRECTIONAL_C_TWO_SIDED_ENVELOPE=PROVED
```

The Stage23 theorem `N2,c(B) >> sqrt(log B)` itself remains accepted. What is missing is the matching denominator theorem for the same `c`-channel source classification.

### Allowed repair

Either:

1. remove/downgrade the checkpoint30 directional ratio claims and retain only the accepted global theorem; or
2. prove an explicit channel adapter from the Stage21 `q`-chambers to the Stage25 `a,b,c` shared-edge/face-mask source channels, and prove the corresponding `M1,j(B) ~ c_j B^2 log B` with `c_j>0` before reasserting the directional envelopes.

No global ratio theorem, count, Stage24 lower bound, or Path A/B exponent arithmetic needs to be reopened.

## Controller-history preservation defect

The checkpoint30 controller rewrite also deletes multiple already-audited checkpoint10/20 provenance fields that are present on `main`, including checkpoint20's replay/workflow/source/manifest/cross-oracle paths and the fresh-audit flags

```text
num_r01_manifest_binding=PASS
num_r01_exactly_two_row_check=PASS
committed_matched_grid=PASS
```

as well as several checkpoint10 repair/provenance fields.

Those deletions do not falsify checkpoint30 mathematics, but they weaken the controller as a durable AI-readable audit record. The repair must restore the prior audited checkpoint10/20 controller payload and append checkpoint30 state rather than compacting away accepted provenance.

## CI interpretation

Submission CI run `31856999392` succeeded, but its ratio verifier checked exponent addition and marker presence; it did not prove the missing chamber-to-shared-edge adapter. CI success therefore does not remove this audit blocker.

During this fresh audit, `ratio_audit.py` was made audit-state aware and now preserves the accepted global arithmetic while mechanically recognizing the checkpoint30 FAIL state and the missing directional adapter. The latest verifier-hardening commit is `cb4e6a30eb5137f1c0b1189a7093bdcb948b96b1`.

```text
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=FAIL
GLOBAL_ENDPOINT_RATIO_ACCEPTED=true
PATH_A_PRODUCT_ACCEPTED=true
PATH_B_PRODUCT_ACCEPTED=true
THREE_WAY_CONSISTENCY_ACCEPTED=true
PROBABILISTIC_INDEPENDENCE_INFERRED=false
RATIO_LIMIT_ZERO_ACCEPTED=true
TARGET_UNBOUNDEDNESS_ACCEPTED=true
DIRECTIONAL_STAGE23_C_LOWER_ACCEPTED=true
DIRECTIONAL_REFINEMENT_ACCEPTED=false
DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false
DIRECTIONAL_UPPER_ALL_ACCEPTED=false
DIRECTIONAL_C_TWO_SIDED_ENVELOPE_ACCEPTED=false
CONTROLLER_HISTORY_PRESERVATION_REQUIRED=true
FINITE_DATA_USED_AS_PROOF=false
COUNTS_RECOMPUTE_REQUIRED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=30
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
REPAIR_SCOPE=DIRECTIONAL_CHANNEL_ADAPTER_OR_DOWNGRADE_PLUS_CONTROLLER_HISTORY_RESTORE
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```
