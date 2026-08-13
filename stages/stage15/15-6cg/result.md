# Stage15-6cg — repaired two-range receiver parking audit

Base: repaired Stage15-6cf. Main-batch audit repair.

The prior split decision is withdrawn pending fresh audit. Stage15-6cf now supplies the exact statewise decomposition
\[
\sum_{P\in A(B)}G_S(P)G_O(P)
=\mathcal M_{\le D_0}(B)+\mathcal M_{>D_0}(B),
\]
with a bijective complementary-cofactor switch in the large range, exact `phi(d)phi(e)` weights until the certified `phi<=id` inequality, and unchanged primitive physical measure `R<=B`.

Candidate receivers after repair:

1. `SMALL`: prove a physical-height root-line count for `de<=D0` strong enough after the exact `phi(d)phi(e)` summation.
2. `LARGE`: prove a complementary-cofactor/form-size average for the switched large range.

They look analytically different, but the controller split condition is **not** asserted here. A fresh audit must check whether one range can dominate or reconstruct the other after the exact weight/multiplicity bookkeeping, and whether the choice of `D0` couples the two bounds so strongly that they remain one optimization problem rather than independent split targets.

The exploration-safety state from 6cd is retained. The pointwise domination candidate tested in 6ce remains BLOCKED in the current normal form.

```text
STAGE15_6_SUBSTAGE=6cg
STAGE15_6CG_REPAIRED_RECEIVER=true
STAGE15_6CG_SMALL_RANGE_RECEIVER=PHYSICAL_ROOT_LINE_COUNT_WITH_EXACT_PHI_WEIGHTS
STAGE15_6CG_LARGE_RANGE_RECEIVER=COMPLEMENTARY_COFACTOR_FORM_SIZE_AVERAGE
STAGE15_6CG_TWO_NON_EQUIVALENT_LIVE_OBSTRUCTIONS=UNRESOLVED_PENDING_AUDIT
STAGE15_6CG_SPLIT_TRIGGER=false
STAGE15_6CG_AUDIT_REQUIRED=true
STAGE15_6CG_CODEX_REQUIRED=false
STAGE15_6CG_MERGE_ALLOWED=false
STAGE15_6CG_EXIT=FRESH_AUDIT_OF_REPAIRED_DIVISOR_SWITCH
```