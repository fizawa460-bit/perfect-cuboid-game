# Stage32 goal and stop contract

Status: ACTIVE prospective execution guardrail for Stage32 mainline, integrated by the active `stages/stage32/controller.json`.

## Authority split

The hostile-audited Stage32-00 roadmap / PR #1339 is authoritative for the **finite mathematical target and receiver semantics**: the frozen unibranch `d<=176 / d<=192` windows, separation of numerical census from effectivity, and the separate multibranch ledger.

The choice of **b16 as the default final d16 calibration bound**, the no-automatic-b18 rule, and the mandatory post-b16 feasibility gate are new operational guardrails introduced by PR #1418. They are not claimed as already audited by #1339 and grant no mathematical, theorem, receiver, or endpoint credit.

The post-b16 literature-receiver reduction audit is a later operational priority. It does not alter the inherited finite target by assertion: it may reduce the production population only where independently source-locked published results are exactly adapted and hostile-audited against the Stage32 population.

The active controller must obey this guardrail for Stage32-main execution. If an older controller field such as `next_norm_wall=TO_BE_SELECTED_BY_RESOURCE_PROFILE` conflicts with this contract, the stop-contract restriction controls d16 calibration: selection is bounded by b16 unless the explicit post-b16 exception below is satisfied.

## Final Stage32 goal and dependency DAG

Stage32 is not complete when one d16 norm bound closes. The inherited audited finite target is the Stage29/Stage32 low-genus Picard production contract.

The dependency structure is **not** a strict 32-01 -> 32-02 -> 32-03 chain:

- `32-01`: complete the required unibranch numerical orbit census over the frozen `d<=176 / d<=192` windows, after first applying any hostile-audited literature receiver reductions to define the exact residual production population; then set `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true` and only the numerical component of `R29-LG2` complete.
- `32-03`: complete the separately firewalled multibranch-at-node ledger `R29-LG2-MB`. This unit may run after or in parallel with `32-01` when resource and evidence safety permit, exactly as the active controller allows.
- `32-02`: after `32-01`, rigorously dispose every numerical survivor by effectivity / boundary / explicit-carrier evidence until `UNKNOWN_EFFECTIVITY_SURVIVOR_COUNT=0`; only then may `R29-LG2` and `R29-LG2-EFF` be discharged.
- `32-04`: blocked until **32-01, 32-02, and 32-03 are all complete**; then synthesize the low-genus carrier result and final certificate required by the active controller.
- `32-05`: after 32-04, hostile audit the integrated result. Only after all required closure criteria pass may `STAGE32_CLOSED=true`.

None of these steps by itself proves Perfect Cuboid existence or nonexistence.

## d16 calibration stop rule

The active d16 Aut-canonical exact route is a production-engine calibration route, not an unbounded mathematical objective.

`b16` is the default final d16 calibration bound.

The current Stage32-18X..18AB chain must finish the exact b16 real-leaf tail experiment and, if needed, refine only unresolved resource-wall descendants until the selected b16 pilot geometry is exact. Closed components must never be recomputed merely to increase the split modulus.

After that, Stage32 may run the resource-safe **full b16 exact production census and hostile audit** needed to characterize the production engine. Once audited b16 is available, the next mandatory Stage32-main item is the literature-receiver reduction audit below; the feasibility gate follows only after that audit has produced an exact residual population.

### No automatic b18 rule

Do **not** advance automatically to `b18`, `b20`, or any larger d16 calibration bound.

A larger d16 bound is permitted only if the feasibility gate itself identifies one narrowly specified missing empirical quantity that is necessary to decide reachability of the frozen `d<=176 / d<=192` target, and the new bound is the cheapest way to measure that quantity. "It is the next bound" or "more confidence would be useful" is not sufficient.

## Post-b16 literature-receiver reduction gate — highest priority

After audited d16/b16 calibration closes, and before a large 183-window production campaign or the resource feasibility gate, Stage32-main must execute `stages/stage32/POST_B16_LITERATURE_RECEIVER_ROADMAP.md` under `stages/stage32/post-b16-literature-receiver-contract.json`.

The four receiver families are:

- `LIT32-FSM`: Freitag--Salvati Manni box-variety low-genus bound and its exact hypotheses/refinements;
- `LIT32-GF`: García-Fritz / García-Fritz--Urzúa nodal-surface and symmetric-differential bounds, with explicit local-node hypothesis adapters;
- `LIT32-BTVA`: Bruin--Thomas--Várilly-Alvarado symmetric-differential/node-incidence special-locus constraints;
- `LIT32-TS`: Testa--Stoll low-degree classification plus K3/Picard/Aut compression machinery.

The gate is not a bibliography exercise. It must source-lock exact statements and produce a hostile-auditable theorem mask over **all 183 frozen `(genus,degree)` rows**. Every row must be marked as fully discharged/classified, partially reduced, unchanged, or applicability-unknown, with exact residual subpopulation definitions where a theorem covers only part of a row.

Critical semantic rules:

- `smooth at a surface node` must not be silently identified with `unibranch at that node`;
- a theorem applying only to a certified subpopulation cannot delete an entire row;
- a bounded low-degree classification cannot be extrapolated above its proved range;
- overlapping restrictions cannot be double-counted;
- discovery of a plausible paper grants no theorem or receiver credit until the Stage32 adapter and hostile audit pass.

Required aggregate output includes the initial row count `183`, fully discharged/classified row count, partially reduced row count, unchanged row count, unknown-applicability row count, exact residual row list, finer residual masks, and the revised residual production target.

If a credible literature theorem could remove a large part of the target but its Stage32 applicability adapter remains unresolved, Stage32-main must stop the comparable brute-force escalation and resolve that bounded adapter first.

This priority does not change the Stage32 dependency DAG: `32-03` may still run in parallel with `32-01` when safe.

## Post-b16 feasibility gate

The feasibility gate is run **after** the literature-receiver audit and against the exact residual production population, not blindly against all 183 rows if audited theorem reductions have already removed or restricted some of them.

Use the audited b10/b12/b14/b16 evidence, including measured descendant-work skew, adaptive split depth, resource-wall pattern, exact survivor growth, artifact sizes, and concurrency/storage behavior, together with the audited residual literature mask, to answer one question:

> Can the current exact production architecture be turned into a finite, auditable execution plan that reaches the residual frozen `d<=176 / d<=192` numerical census under the repository's current execution policies?

The gate must produce a compact machine-readable certificate with:

- exact target population/window definition inherited from the audited Stage32-00 / Stage29 contract after source-locked hostile-audited literature reductions;
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
A conservative finite production plan exists under current policy, with no unresolved algorithmic wall hidden behind unsupported extrapolation. Proceed to the actual 32-01 residual production plan; do not return to d16 calibration by default.

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
POST_B16_LITERATURE_RECEIVER_AUDIT_COMPLETE=false
LITERATURE_REDUCED_WINDOW_MASK_AUDITED=false
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
