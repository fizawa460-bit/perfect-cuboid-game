# StructureRadar independent audit — pause and return to Stage27

```text
AUDIT_VERDICT=PASS_WITH_ROUTING_AND_PAUSED_CORPUS_REPAIR
AUDITED_PR=1244
AUDITED_SUBMISSION_HEAD=239cc6332e3bbd335da6155ca5254cfac1edd846
BASE_MAIN=389d3d9b935691efc46e0af8e5679dcefb507a7b
BASE_MAIN_AUDIT=PASS_CURRENT_MAIN
PAUSE_NOT_GLOBAL_MATHEMATICAL_CLOSURE_AUDIT=PASS
SR_STR_169_DISPOSITION_AUDIT=PASS_WORK_FAIL_EXTERNAL_GATE_RETAINED
SR_STR_024_DISPOSITION_AUDIT=PASS_WORK_FAIL_EXTERNAL_GATE_RETAINED
SR_STR_021_DISPOSITION_AUDIT=PASS_WORK_FAIL_EXTERNAL_GATE_RETAINED
ANTI_LOOP_POLICY_AUDIT=PASS
STAGE27_EARLY_RETURN_POLICY_AUDIT=PASS
EXTERNAL_GATE_TAIL_MAY_REMAIN_UNRESOLVED_AUDIT=PASS
PERFECT_CUBOID_FIREWALL_AUDIT=PASS
CONTROLLER_ROUTING_AUDIT=FAIL_THEN_REPAIRED
PAUSED_CORPUS_SCOPE_AUDIT=FAIL_THEN_REPAIRED
A1_A2_GENERAL_WEAPON_PROMOTION=false
A1_PAUSE_SCOPE_DISPOSITION=EXCLUDED_AUXILIARY_INVALID_UPSTREAM_LINE
A2_PAUSE_SCOPE_DISPOSITION=EXCLUDED_FAMILY_SPECIFIC_LOCAL_CLOSURE
OTHER_FUTURE_CORPUS_CHANGE_DETECTION=PRESERVED
AUDIT_REPAIR_PERFORMED=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
```

## Independent disposition check

The pause record is consistent with the merged StructureRadar boundary.

- `SR-STR-169` remains `EXTERNAL_GATE` at the exact same-`H_phys^MAIN` arbitrary-coefficient quadratic-form receiver. The focused Work literature audit concluded `FAIL`: no published theorem currently discharges the exact receiver while preserving the correlated modulus, nested common-parent allocation, physical masks and quantifier order. This is a search/applicability failure, not a mathematical closure.
- `SR-STR-024` remains `EXTERNAL_GATE` at `UniformFilteredQuotientCharacterVoronoiFunctionalEquationAdapter`. The merged deep reduction and focused Work search both stop at the missing legal functional-equation/one-variable coefficient adapter; generic `tau_3`, Voronoi or average-modulus substitutions are not legal replacements.
- `SR-STR-021` remains `EXTERNAL_GATE` at `ExceptionalZeroRepelledLogFreeZeroDensityForGaussianAngularRayCharacters`. The focused primary-literature search found joint `(chi,k)` density without the required exceptional-zero repulsion factor, finite-order repulsion results that do not cover nonzero infinity type, and ranges below the required super-Kai regime. No exact published discharge theorem was found.

These three outcomes support a pause/freeze decision, not `CLOSED` theorem claims.

## Anti-loop and Stage27 routing check

The merged anti-loop policy requires an overall pause once all Stage27-relevant lanes are stalled, and the external-gate closure policy says Stage27-19/20 need not wait for every remaining external gate. Batch 40D already recommends the same pause of normal StructureRadar deepening and return to Stage27-relevant work.

The submitted pause record follows those policies and preserves selective reopening on genuinely new mathematics, a changed receiver, a legal adapter, or a bypass route.

## Routing repair

The submitted snapshot still advertised `next_expected_command=StructureRadar-main-batch` in the generated controller despite routing active work back to Stage27. The audit repaired that inconsistency. The controller now records:

```text
campaign_state=PAUSED_RETURN_TO_STAGE27
normal_deepening_paused=true
remaining_external_gates_mandatory_before_stage27=false
return_targets=Stage27-19,Stage27-20
next_expected_command=NONE_STRUCTURE_RADAR_PAUSED
```

The top-level historical `status=CLOSED` continues to mean the initial census/review campaign is closed; the post-close external-gate campaign is explicitly paused.

## Generated-state / paused-corpus repair

The first repaired head exposed a second operational issue in CI. `scripts/structure_radar.py verify` correctly detected stale generated manifests because the later StageA1/StageA2 side-line files had entered the repository after the last StructureRadar corpus snapshot.

Those A-lines are not promoted as general StructureRadar weapons:

- StageA1 is the historical auxiliary `-8` line invalidated for the published equation-(6) family.
- StageA2 is the correct published `-18` equation-(6) family-specific closure. It remains useful as a local family theorem but is not a general perfect-cuboid weapon.

The audit therefore made this scope decision explicit rather than weakening verification globally. `docs/structure-radar/pause-scope-policy.json` lists only `stages/stageA1/` and `stages/stageA2/` as paused-corpus exclusions. The original repository-wide generator is preserved as `scripts/structure_radar_core.py`; the thin `scripts/structure_radar.py` entry point applies the explicit pause policy and controller routing overlay.

Any other newly added or changed source remains visible to the core verifier and still causes corpus drift / refresh rather than being silently ignored. Thus future main-stage evidence detection remains intact.

The first pause-aware repair head `f5d5a9b2fa42a5ca6e07f277ac88b4e7be90b251` passed the exact-head `StructureRadar controller` workflow (run `32339600083`).

No mathematical receiver is closed by this audit. No strict sub-square-root saving is claimed, and no perfect-cuboid existence/nonexistence claim is made.
