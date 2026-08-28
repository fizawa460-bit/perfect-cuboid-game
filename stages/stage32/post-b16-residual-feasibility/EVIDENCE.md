# Stage32 post-B16 residual feasibility gate

Status: **MAIN EVIDENCE COMPLETE — PENDING FRESH HOSTILE AUDIT**.

This gate measures the remaining full-window `R29-LG2` numerical-production problem after the hostile-audited D16/B16 bounded close and the hostile-audited literature/receiver reconciliation. It authorizes no heavy run and grants no new numerical, receiver, theorem, route, or endpoint credit.

## Locked inputs

- main base: `babfc120f738f5a1ca7ae9a20996314bf923300c`
- repaired B16 close: `stages/stage32/32-18BG/D16_B16_REPAIRED_CLOSE_EVIDENCE.md`
- post-B16 literature audit: `stages/stage32/post-b16-literature-receiver-exact-audit/AUDIT.md`
- Stage29 receiver contract: `stages/stage29/29-02c-LG2/finite-search-contract.md`
- Stage32 roadmap: `stages/stage32/ROADMAP.md`
- exact positive-dual certificate: PR #1341, hostile audit `PASS_POLYTAIL_EXACT_POSITIVE_DUAL_CERTIFICATE`
- graded checkpoint planner: PR #1342, hostile audit `PASS_CHECKPOINT_PLANNER_ONLY_WITH_VERIFIER_SCOPE_NOTE`
- remote-CloseVectors residual: PR #1343, hostile audit `PASS_AS_BOUNDED_PROGRESS_WITH_EXACT_CLASS2_RESIDUAL`
- exact materialized-signature prototype: PR #1354, hostile audit `PASS_AFTER_CONTROLLER_AND_REPO_LOCAL_EVIDENCE_REPAIR`

Static counts are independently reproducible by `analyze_full_window_feasibility.py`; expected payload SHA256 is

`e787c75b845b691c934fcba5a09a1a76c3c95a82a2deb6563bb7e8fbcd636897`.

## Full-window scale

The audited unibranch window has exactly 183 `(g,d)` rows:

- genus 0: 88 even degrees `2..176`;
- genus 1: 95 even degrees `4..192`.

For `r=gcd(d,16)`, `m=16/r`, the exact Stage29 `H^perp` norm bound is

- genus 0: `m^2*(d^2/16+d+2)`;
- genus 1: `m^2*(d^2/16+d)`.

For `(g,d)=(0,16)`, the complete norm window is `B34`. The audited Stage32 close is only `B16`; therefore it is a bounded calibration, not a complete d16 row.

Across the full receiver window:

- 181/183 rows have norm bound greater than `34`;
- 92/183 rows have norm bound greater than `10,000`;
- the maximum is `B156560` at `(g,d)=(1,190)` where `m=8`;
- `m=8` occurs on 91 rows.

The exact d16 history already shows severe tail growth before the full d16 bound: b8 exact baseline required about 32m48s; b12 required sharding and recursive rescue; b16 required the repaired cut39 parent namespace, pairwise exact KKT propagation, and selective deep residual splits. Consequently, continuing `B18,B20,...` as the full-window driver is rejected as an execution architecture. This is a tractability decision, not a mathematical impossibility statement.

```text
DIRECT_NORM_SHELL_CONTINUATION_AS_FULL_WINDOW_DRIVER=false
AUTOMATIC_B18_RELEASE=false
```

## Positive-dual bounded coordinates

The hostile-audited Stage32-01 identity is

`19*(H.x) = sum_92 D.x + 5*sum_48 E.x`.

Together with all 140 nonnegative known-curve intersections and the hostile-audited full-rank 64-row subsystem, every fixed positive-degree slice is bounded.

The existing graded planner yields 65,249 coarse `(g,d,e)` exceptional-mass strata. Consuming the audited degree-`<=6` classification instead of re-enumerating those five rows, then applying the already-audited necessary exceptional-incidence lower bounds

- genus-0 residual nonconics: `sum E.x >= 8`;
- genus 1: `sum E.x >= 4`,

still leaves 64,111 coarse exceptional-mass strata across 178 residual rows. Thus `one Actions job per (g,d,e)` is also rejected: it is a checkpoint namespace, not a safe execution fan-out.

```text
EXCEPTIONAL_MASS_IS_VALID_COARSE_CHECKPOINT=true
ONE_ACTIONS_JOB_PER_EXCEPTIONAL_MASS_STRATUM=false
```

## Reusable exact assets

The feasibility gate does not start over. The repository already contains exact components that can be composed into the residual production enumerator:

1. exact Picard source lock and rank-64 primitive coordinates;
2. 140 known-curve intersection forms;
3. hostile-audited positive-dual boundedness certificate;
4. deterministic 65,249-stratum manifest machinery and hardened stable-ID verifier;
5. exact exceptional/signature assignment materialization from the d8 route;
6. exact affine-coset/HNF refinement machinery;
7. exact low-dimensional qtail enumeration used in the audited d8 selected tiers;
8. exact order-1536 `Aut(S)` reconstruction and orbit verification;
9. exact rank-63 `H^perp` LDL/cap machinery and exact pairwise KKT propagation from the d16 route.

The old `run_numeric_magma_curvegroup_adaptive.py` is retained only as a prototype of exact `(d,e,a)` partition semantics. Its dependency on the public Magma calculator and timeout-subdivision behavior is not accepted as the production engine; PR #1343 already exposed that as a Class-2 tool wall.

## Production architecture selected by this gate

`RESIDUAL_32_01_PRODUCTION`, if released by hostile audit of this gate, must begin with a local/offline exact intersection-coordinate enumerator, not a direct B18 run.

The required first implementation is:

1. rebuild and hash-lock the Picard core from the immutable upstream source;
2. choose and verify a deterministic full-rank 64-row pairing subsystem from the 140 known classes;
3. compute an exact Smith/Hermite description of the image lattice so partial pairing assignments receive congruence/membership pruning before lattice enumeration;
4. reconstruct Picard classes exactly from accepted pairing coordinates and recheck all 140 inequalities;
5. branch first on exceptional/node-incidence coordinates under the positive-dual mass identity and audited lower bounds;
6. encode the literature node-count/spanning filters only after their geometric-to-exceptional-coordinate adapters are explicitly verified; they are not silently assumed by this gate;
7. apply exact `Aut(S)` canonical augmentation during the branch tree, rather than orbit-deduplicating only after materializing every candidate;
8. descend to the existing exact affine-coset/qtail or `H^perp` certifier only for sufficiently small residual leaves;
9. checkpoint compactly by content-derived branch IDs; one worker may consume many small strata, so GitHub Actions fan-out remains bounded;
10. use the audited d<=6 catalogue and previously exact small-degree results as regression fixtures, not as extrapolation.

The first production run must be a bounded implementation/cost calibration over representative audited rows from each `m in {1,2,4,8}` class. It must establish a safe shard/work-unit policy before any attempt to cover all 178 residual rows. No result from that calibration may be promoted to full-window credit.

## Feasibility verdict

The full 176/192 numerical receiver remains finite and there is now a concrete exact production architecture assembled from already-audited repository components. The current repository does **not** yet contain the complete local/offline intersection-coordinate enumerator or a measured safe full-window cost model.

Therefore the gate verdict is:

`PASS_RESIDUAL_FEASIBILITY_EXACT_ARCHITECTURE_IDENTIFIED_IMPLEMENTATION_AND_CALIBRATION_REQUIRED`

Proposed downstream release, only after a fresh hostile audit of this checkpoint:

`RESIDUAL_32_01_PRODUCTION`

Its initial scope is implementation + representative calibration of the exact intersection-coordinate engine. It is **not** authorization for raw B18 continuation or an all-178-row heavy sweep.

## Firewalls

- `D16_B16_NUMERICAL_CREDIT = true`
- `FULL_D16_G0_ROW_COMPLETE = false`
- `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS = false`
- `R29_LG2 = NOT_DISCHARGED`
- `R29_LG2_EFF = NOT_DISCHARGED`
- `R29_LG2_MB = NOT_DISCHARGED`
- `G10_LOWGENUS_PICARD = AMBER`
- theorem credit = false
- receiver credit = false
- route-color change authorized = false
- endpoint credit = false
- B18 release authorized = false
- heavy compute armed = false
- perfect-cuboid existence claim = false
- perfect-cuboid nonexistence claim = false
