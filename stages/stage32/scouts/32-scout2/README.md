# Stage32 scout2 — fast b10 floating-state drift diagnosis

## Archived historical diagnostic

This directory is retained on `main` as a non-executable research archive. The original GitHub Actions workflow has been deliberately removed and must not be restored or rerun as part of normal Stage32 execution.

The scout's causal result was subsequently cross-checked by the exact Stage32-18C recovery: the snapshot-restored fast b10 set contained exactly the same 1,430 canonical records as the hostile-audited exact b10 census. This preserves the diagnostic value of scout2 without granting global fast-traversal completeness.

Scout-only side experiment. This branch does not modify the active Stage32 controller and cannot grant numerical, theorem, receiver, or full-row credit.

Observed trigger from Stage32-18C: the fast b10 traversal completed but lost 22 hostile-audited b8 canonical representatives: one norm-0, two norm-4, and nineteen norm-8. Since the same lower-norm points passed the same fast source at b8, this violates the expected cumulative monotonicity and proves the fast floating traversal is not complete at b10.

The fast DFS keeps transformed cap and symmetry partial sums in mutable `long double` arrays and restores them after each child with `+= delta` followed later by `-= delta`. Floating arithmetic does not guarantee this round trip returns the exact parent value. A much larger b10 traversal can therefore make a later branch depend on earlier sibling history.

Scout2 tests that hypothesis with three source-locked variants of `stages/stage32/32-18/d16_aut_canonical_enum.cpp` (Git blob `f9479ee73c9a5960cb8a3a8bc11a0c1c0fe8f4ba`):

1. `cap`: parent-snapshot restore for the 140 cap partial sums only;
2. `sym`: parent-snapshot restore for the 64 symmetry-breaker partial sums only;
3. `both`: parent-snapshot restore for both arrays.

The snapshot variants compute each child state from the immutable parent state for that DFS node instead of attempting a floating add/subtract round trip. The LDL, radius bounds, reach bounds, guards, 64 breakers, exact leaf checks, and full order-1536 canonicalization are otherwise unchanged.

Each variant was compared against:

- hostile-audited exact b8 artifact `9551029604`, ZIP SHA256 `e5cb3fca37cf8d4df9cabfcd8830e8d3e0cb702c13fd9e4ba20ed6b5829461d7`;
- Stage32-18C baseline b10 prepared artifact `9553484252`, ZIP SHA256 `76b9d7738f2a8125ee5f56f485877663f02f6cca76ccad7237d1515272e8fc01`.

Final scout diagnosis:

- cap snapshot only: still 1,407 canonical records;
- symmetry snapshot only: 1,430 canonical records and all 22 known predecessor losses recovered;
- cap + symmetry snapshot: the same 1,430 canonical set, with lower wall time than the broken baseline;
- exact Stage32-18C recovery later proved that this 1,430-record snapshot-restored set is exactly identical to the complete exact b10 set.

This establishes the cause of the known b10 predecessor loss as symmetry-accumulator floating roundtrip drift. It does **not** prove the remaining floating LDL/radius/reach traversal complete at arbitrary bounds.

```text
ARCHIVED_SCOUT=true
EXECUTABLE_WORKFLOW_RETIRED=true
SCOUT_ONLY=true
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
CERTIFIED_FAST_ENGINE_ESTABLISHED=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```
