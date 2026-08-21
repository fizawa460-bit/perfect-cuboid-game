# Stage29-03 audit contract

Fresh audit must attack the **execution-location decision**, not re-audit all of Stage29-02.

## Required adversarial checks

1. **False no-backflow risk**
   - Check whether any of `R29-KUM3A`, `R29-KUM3B`, `R29-KUM4`, `R29-PESCH1` actually requires changing an audited Stage16–28 contract rather than merely consuming it.
   - If yes, replace `STAGE29_INTERNAL_ADAPTER_ONLY` with `TARGETED_BACKFLOW_REQUIRED` and name the exact old stage/addendum.

2. **KUM3A/KUM3B dependency direction**
   - Verify that 29-02b's audited joint-V4 model can remain Stage29-native while the F7-to-Stage28 host comparison is open.
   - Do not infer KUM3B merely from matching deck-group ranks or square-root counts.

3. **KUM4 population firewall**
   - Verify that no statement silently identifies exact Stage16–20 strata with nested sign-cover floors.
   - Preserve physical height, primitive normalization, canonical ordering, and multiplicity as independent adapter obligations.
   - Preserve `N2/M2` as a literal finite survival only where already audited; do not reinterpret `M3/M2` or `M3/N2` as survival probabilities.

4. **Peschmann scope**
   - Preserve the 29-02hd audit repair: matching residual condition patterns do not prove an F2 adapter.
   - `PESCHMANN_PROVEN_F2_ADAPTER=false` and `PESCHMANN_INDEPENDENCE_RESOLVED=false` must survive unless new exact mathematics is added in this PR.

5. **Anti-loop rule**
   - Confirm that no old frozen Stage16–28 gate is reopened merely for reinterpretation.
   - Confirm that a future addendum requires a named exact receiver and a reason the Stage29-native record is insufficient.

6. **Roadmap sequencing**
   - Check that 29-04 precedes KUM4 population interpretation and that 29-05/GAP_SCAN_A occur before 29-07.
   - Check that Peschmann remains owned by 29-08.

7. **No premature route pruning**
   - 29-03 must not choose a primary endpoint route or retire Campedelli/Beauville/modular/K3/local/full-surface routes.

## Acceptable audit verdicts

```text
PASS
PASS_AFTER_BOUNDED_REPAIR
FAIL_MATERIAL_BACKFLOW_MISROUTED
```

A bounded repair may change one or more receiver execution locations without rewriting completed audited history.

## Submission firewall

```text
MAIN_LANE_SELF_AUDIT=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
