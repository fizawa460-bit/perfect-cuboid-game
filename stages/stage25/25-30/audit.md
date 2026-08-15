# Stage25-30 fresh re-audit

Status: **PASS — previous directional overclaim repaired**

## Re-audit scope

This re-audit checks only the two blockers from the previous checkpoint30 FAIL:

1. the unsupported identification of Stage21 order chambers `q` with Stage23 shared-edge / face-mask channels `a,b,c`;
2. loss of already-audited checkpoint10/20 controller provenance during checkpoint30 compaction.

The previously accepted global checkpoint30 mathematics is not reopened.

## Global theorem retained and accepted

Under the frozen Stage25 endpoint contract,

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore

\[
\boxed{
B^{-2}(\log B)^{-1/2}
\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}
}
\]

and hence

\[
\boxed{N_2(B)/M_1(B)\to0},
\qquad N_2(B)\to\infty.
\]

Path A and Path B remain exact count identities:

```text
(M2/M1)(N2/M2)=N2/M1
(N1/M1)(N2/N1)=N2/M1
```

Both reproduce the same polynomial/logarithmic envelope. No probabilistic independence statement is inferred.

## Directional repair — accepted

The repair correctly chooses **downgrade rather than inventing an adapter**.

Stage21 `q` indexes order chambers with factors `I_q`. Stage23 `N2,c` indexes the exactly-two shared-edge channel with faces `ac` and `bc` integral. These are kept distinct.

The following target-only Stage23 theorem remains accepted:

\[
\boxed{N_{2,c}(B)\gg\sqrt{\log B}}.
\]

But checkpoint30 now explicitly makes no source denominator theorem for the same shared-edge channel and therefore no directional ratio theorem:

```text
DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false
DIRECTIONAL_UPPER_ALL=NOT_PROVED
DIRECTIONAL_C_TWO_SIDED_ENVELOPE=NOT_PROVED
DIRECTIONAL_RATIO_REFINEMENT_STATUS=OPEN_GATE_ADAPTER_REQUIRED
```

This exactly resolves the previous audit blocker without weakening or altering the global theorem.

## Controller-history repair — accepted

The checkpoint30 branch preserves the full audited checkpoint10/20 payload from `main` and appends checkpoint30 rather than replacing older provenance.

In particular checkpoint20 retains:

```text
replay
workflow
source_counts
target_object_ledger
target_manifest
target_cross_oracle
num_r01_manifest_binding=PASS
num_r01_exactly_two_row_check=PASS
committed_matched_grid=PASS
```

Checkpoint10 also retains its prior FAIL/repair provenance and frozen population/ratio-contract flags. `audit_history` records checkpoint10 PASS, checkpoint20 PASS, checkpoint30 FAIL, and this checkpoint30 PASS re-audit.

## Discovery and final audited-head CI

The repaired discovery ledger explicitly records the chamber/shared-edge mismatch and the absence of a proved directional adapter. It no longer claims the rejected directional ratio result.

Repair head `fe14d7bdf738518e918f6344a8eef7793a58acce` first passed all three Stage25 workflows. After audit persistence and controller synchronization, audited head `54fdf02c06d00a1d7de29903b4644fe3c8b9eb79` was verified again:

```text
Stage25-10 contract audit        run 31861962115  SUCCESS
Stage25-20 matched-grid replay   run 31861962210  SUCCESS
Stage25-30 ratio consistency     run 31861962058  SUCCESS
```

The checkpoint30 verifier is audit-state aware and checks the repaired downgrade, controller-history restoration, and accepted global exponent arithmetic.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
PREVIOUS_AUDIT_VERDICT=FAIL
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
DIRECTIONAL_OVERCLAIM_REPAIRED=true
DIRECTIONAL_RATIO_REFINEMENT_STATUS=OPEN_GATE_ADAPTER_REQUIRED
CONTROLLER_HISTORY_PRESERVATION_ACCEPTED=true
FINITE_DATA_USED_AS_PROOF=false
COUNTS_RECOMPUTE_REQUIRED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #982; then Stage25-main-batch
```
