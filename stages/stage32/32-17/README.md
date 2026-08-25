# Stage32-17 — e20/a0 exact continuation to the pre-115712 plateau boundary

This batch advances only the `d=8, g=0, e=20, a=0` numerical parent from the hostile-audited cumulative `materialized branches/cell <= 65536` checkpoint.

The Stage32-14 profile has a natural execution boundary immediately before a 128-cell equal-cost plateau:

- audited predecessor: `301` cells / `6,834,114` branches;
- selected delta: `65536 < branches/cell <= 114186`;
- delta: `116` cells / `9,890,148` branches;
- cumulative target: `417` cells / `16,724,262` branches;
- next profile value: `115,712`, with multiplicity `128` cells.

Stage32-17 therefore stops before the `115712 x 128` plateau instead of silently absorbing another `14,811,136` branches into the same audit unit.

Execution preserves the audited Stage32-16 exact solver semantics. The Stage32-17 runner is a thin schema adapter over `32-16/run_e20_work_bundle.py`; no search, cap, rational, branch, UNKNOWN, or node-budget semantics are changed. Dynamic global-index modulo shards remain bounded by `32,768` branches. The exact delta produces `364` work items, deterministically LPT-packed into `80` bundles over four dependency-ordered waves with `max-parallel: 8`.

A maximum-load bundle is executed as the pilot. The pilot also recomputes audited predecessor cell `48`, shard `s0of2` (`26,496` branches) and must reproduce branch-evidence-stream SHA-256 `b6d30e4f6d73d6e545d9594c29cebcbc4394f854d493b49b6c6aaa91233534b0` before fanout receives credit.

Raw exhaustive branch evidence remains runner-local and is deleted only after complete exact verification and compact-certificate creation. The conservative incremental retained-artifact bound is `27,280,000` bytes, below the repo policy's `100 MB` fallback ceiling and independent of deletion of historical evidence.

## Execution result and recovery provenance

The exact computation is complete and audit-ready.

- predecessor imported from the hostile-audited `<=65536` state: `301` cells / `6,834,114` branches / `1,881,870` search nodes;
- Stage32-17 delta: `116` cells / `9,890,148` branches / `1,583,294` search nodes;
- cumulative exact tier: `417` cells / `16,724,262` branches / `3,465,164` search nodes;
- exact UNKNOWN count: `0`;
- exact numerical survivors: `0`;
- delta work items verified: `364 / 364`;
- bundle receipts verified: `80 / 80` (`60` retained source-run bundles plus `20` recovered wave3 bundles);
- cumulative canonical SHA-256: `c3680e432b12a61314c1852336a55e50f53ea23b151a05729d7f86db6b2e1d5c`.

The original long run `32779320736` completed the pilot and waves 0–2, but ancestor Actions artifacts expired before wave3 could acquire the source-locked core. This was an artifact-lifetime failure, not a solver failure. Recovery run `32796303960` independently re-derived the pinned Picard core, cap certificate, and 1182-cell profile, matched the exact locked profile SHA, retained the successful 60 bundles, and executed only the missing 20 wave3 bundles. All 20 recovered bundles completed with no UNKNOWN.

The first recovery aggregate exposed a historical metadata transcription typo in `stages/stage32/32-16/execution-state.json`: its recorded `profile_sha256` is a 61-character string, while the regenerated profile and the Stage32-17 plan independently lock the correct 64-character SHA-256 `e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5`. Stage32-17 does not modify the hostile-audited historical state. `aggregate_recovery_adapter.py` accepts exactly that legacy typo, independently re-locks the predecessor canonical SHA and recorded independent reaggregation, and patches only an ephemeral adapter copy for the existing aggregate verifier.

Aggregate-only run `32802240965` then re-read the existing 60+20 bundle evidence without re-running any solver branch and verified the complete 364-work-item partition. The final self-contained artifact is `stage32-17-e20-a0-le114186-recovered-exact-tier`, artifact `9546895729`, ZIP SHA-256 `37e4b66f2f6f62d05d9017b7f378edec9c7ea7b60d539c161a578fc59656e08a`, containing 451 files including all 364 compact certificates and all 80 receipts. Repository policy clamps artifact retention to 5 days despite the workflow's larger requested retention.

No `115712` plateau cell was executed. The next wall remains `115712 x 128`, and the `e20/a0` parent still has `765` of `1182` profile cells outside this completed tier.

Audit boundary:

```text
AUDIT_FINAL_VERDICT=WAIT
HOSTILE_AUDIT_REQUIRED=true
E20_A0_PARENT_COMPLETE=false
STAGE32_01_COMPLETE=false
STAGE32_CLOSED=false
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```

Any UNKNOWN, node-budget exhaustion, missing/duplicate modulo residue, failed pilot/regression, artifact/storage gate failure, or incomplete wave blocks aggregate credit. The exact execution evidence currently passes those main-stage gates, but hostile audit has not yet granted final credit. No `115712` plateau cell is part of this batch.
