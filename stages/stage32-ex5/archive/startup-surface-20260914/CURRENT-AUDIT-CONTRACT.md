# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` remains the historical Cycle1 source-locked contract.

## Current audit target

There is **no active EX5 hostile-audit target at ordinary startup**. PR #1765 / BC2-24 is already merged at `98c5710dad4ca9a006e93b273ecf5259733e03aa` and is historical retained provenance.

`stage32ex5-audit` becomes applicable only after `stage32ex5-mainbatch` freezes a new exact retained post-merge checkpoint (BC2-25 or later). Do not re-audit #1765 merely because EX5 research resumes.

## Required checks for the next checkpoint

At the next exact retained boundary, hostile audit must at minimum establish:

1. current-main / Stage32 routing freshness and exact-head identity;
2. preserved historical Cycle1 and early-BC2 authority provenance;
3. exact replay of the BC2-24 predecessor locks and the new checkpoint's own source/certificate/verifier chain;
4. UNKNOWN is not relabelled UNSAT and unretained identities are not inferred;
5. no local obstruction is promoted to whole-stratum/FULL178 credit without an exact population adapter;
6. no EX5 result self-promotes Stage32 MAIN/N350/receiver/effectivity/theorem/endpoint/Perfect Cuboid credit;
7. workflow lifecycle remains fail-closed for historical/retired leaf workflows;
8. merge authorization remains a separate explicit user action.

Until a new checkpoint exists, `stage32ex5-audit` should stop with `NO_ACTIVE_EX5_AUDIT_BOUNDARY` rather than audit historical #1765 again.
