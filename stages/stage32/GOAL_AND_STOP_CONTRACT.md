# Stage32 goal and stop contract

Status: ACTIVE prospective execution guardrail for Stage32 mainline, integrated by the active `stages/stage32/controller.json`.

## Authority split

The hostile-audited Stage32-00 roadmap / PR #1339 is authoritative for the **finite mathematical target and receiver semantics**: the frozen unibranch `d<=176 / d<=192` windows, separation of numerical census from effectivity, and the separate multibranch ledger.

The choice of **b16 as the default final d16 calibration bound**, the no-automatic-b18 rule, and the mandatory post-b16 feasibility gate are new operational guardrails introduced by PR #1418. They are not claimed as already audited by #1339 and grant no mathematical, theorem, receiver, or endpoint credit.

The active controller must obey this guardrail for Stage32-main execution. If an older controller field such as `next_norm_wall=TO_BE_SELECTED_BY_RESOURCE_PROFILE` conflicts with this contract, the stop-contract restriction controls d16 calibration: selection is bounded by b16 unless the explicit post-b16 exception below is satisfied.

## Final Stage32 goal and dependency DAG

Stage32 is not complete when one d16 norm bound closes. The inherited audited finite target is the Stage29/Stage32 low-genus Picard production contract.

The dependency structure is **not** a strict 32-01 -> 32-02 -> 32-03 chain:

- `32-01`: complete the required unibranch numerical orbit census over the frozen `d<=176 / d<=192` windows, then set `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true` and only the numerical component of `R29-LG2` complete.
- `32-03`: complete the separately firewalled multibranch-at-node ledger `R29-LG2-MB`. This unit may run after or in parallel with `32-01` when resource and evidence safety permit, exactly as the active controller allows.
- `32-02`: after `32-01`, rigorously dispose every numerical survivor by effectivity / boundary / explicit-carrier evidence until `UNKNOWN_EFFECTIVITY_SURVIVOR_COUNT=0`; only then may `R29-LG2` and `R29-LG2-EFF` be discharged.
- `32-04`: blocked until **32-01, 32-02, and 32-03 are all complete**; then synthesize the low-genus carrier result and final certificate required by the active controller.
- `32-05`: after 32-04, hostile audit the integrated result. Only after all required closure criteria pass may `STAGE32_CLOSED=true`.

None of these steps by itself proves Perfect Cuboid existence or nonexistence.

## d16 calibration stop rule

The active d16 Aut-canonical exact route is a production-engine calibration route, not an unbounded mathematical objective.

`b16` is the default final d16 calibration bound.

The current Stage32-18X..18AB chain must finish the exact b16 real-leaf tail experiment and, if needed, refine only unresolved resource-wall descendants until the selected b16 pilot geometry is exact. Closed components must never be recomputed merely to increase the split modulus.

After that, Stage32 may run the resource-safe **full b16 exact production census and hostile audit** needed to characterize the production engine. Once audited b16 is available, the next mandatory step is the feasibility gate below.

### No automatic b18 rule

Do **not** advance automatically to `b18`, `b20`, or any larger d16 calibration bound.

A larger d16 bound is permitted only if the feasibility gate itself identifies one narrowly specified missing empirical quantity that is necessary to decide reachability of the frozen `d<=176 / d<=192` target, and the new bound is the cheapest way to measure that quantity. "It is the next bound" or "more confidence would be useful" is not sufficient.

## Post-b16 feasibility gate

Use the audited b10/b12/b14/b16 evidence, including measured descendant-work skew, adaptive split depth, resource-wall pattern, exact survivor growth, artifact sizes, and concurrency/storage behavior, to answer one question:

> Can the current exact production architecture be turned into a finite, auditable execution plan that reaches the frozen `d<=176 / d<=192` numerical census under the repository's current execution policies?

The gate must produce a compact machine-readable certificate with:

- exact target population/window definition inherited from the audited Stage32-00 / Stage29 contract;
- conservative projected heavy-job count or packet count, including rescue work;
- maximum required adaptive split depth justified from evidence, or an explicit statement that no justified bound is known;
- projected peak artifact/storage usage under the 500 MB operating ceiling;
- effective concurrent heavy jobs under the Stage ceiling of 18;
- projected wall-clock/work envelope stated separately from mathematical credit;
- assumptions and extrapolations, each identified explicitly;
- the sensitivity of the projection to tail growth and survivor growth;
- a concrete execution architecture if feasible.

The gate has exactly four allowed outcomes:

### `PASS_FEASIBLE_TO_FROZEN_CENSUS`
A conservative finite production plan exists under current policy, with no unresolved algorithmic wall hidden behind unsupported extrapolation. Proceed to the actual 32-01 production plan; do not return to d16 calibration by default.

### `BLOCKED_RESOURCE_NOT_PRACTICAL`
The route is mathematically finite but the conservative projection is not practically executable under current resource policy. Stop Stage32 main execution and report the estimated scale plainly to the user before any new heavy route is armed.

### `BLOCKED_ALGORITHM_OR_UNBOUNDED_TAIL`
The evidence does not justify a finite split-depth/work bound, or tail growth makes the present architecture unreliable. Stop bounded escalation. The next work must change the algorithm/compression/pruning architecture, not merely increase d16 `b`.

### `UNKNOWN_FEASIBILITY`
The available measurements are insufficient to decide. Stop and identify the single missing measurement or theorem. Do not launch a larger d16 bound unless it satisfies the narrow exception in the no-automatic-b18 rule.

For every non-PASS outcome, the next user-facing report must explain in ordinary language: what failed, approximately how large the obstruction is, why more of the same computation will not solve it, and what the smallest credible alternative is.

## Firewalls

Until the corresponding audited closure step is actually complete:

```text
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
STAGE32_CLOSED=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
