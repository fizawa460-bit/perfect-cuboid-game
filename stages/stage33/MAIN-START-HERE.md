# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then `stages/stage33/ROADMAP-33-12-MICROGOALS.md`, then only the files required by the first eligible unfinished micro-goal and the live `current_leaf_working_set`. The micro-roadmap is planning/execution structure only; controller/MAIN-STATE remain live authority.

Every MAIN batch works in atomic commits: select the first micro-goal whose prerequisites are satisfied, produce its exact object or narrowly stated exact obstruction, run its verifier, commit it, and only then advance to the next micro-goal. Do not use a broad batch target such as "construct the remaining lift" when the roadmap provides a smaller acceptance-tested item.

## V58 bounded-search routing supersession

For the active Stage33 branch, `stages/stage33/33-12/e3-search-routing-supersession-v58.json` supersedes the fixed one-search budget and any historical wording that treats one bounded-search miss as exhaustion of the search allowance. This is an operational routing change only; V57 and all prior mathematical certificates remain unchanged.

Current discovery order is:

1. Identify the exact missing object from the active micro-goal.
2. Consult `docs/arsenal/index.json` first and inspect only matching cards.
3. Run bounded repository searches as needed. There is **no fixed per-object query-count cap**.
4. Every additional search must answer a concrete load-bearing subquestion, remain within a named narrow scope, and be justified by a new mathematical alias, candidate family, implicated path, producer, source/certificate path, or other materially new signal.
5. Stop when the bounded question is answered, the identified candidate family is exhausted, the asset is source-locked, or the next move would become repository-wide enumeration, branch-history archaeology, unconstrained keyword expansion, or near-equivalent miss-chasing.
6. A search miss proves neither repository absence nor mathematical nonexistence. Construction may begin whenever the current leaf has enough information; it is not gated by an arbitrary search count.

Research OS still forbids unlimited/open-ended discovery. Recursive repository-wide enumeration, automatic branch-history/origin archaeology, unconstrained keyword expansion, and repeated near-equivalent searches solely to chase a negative result remain prohibited.

The V39 locator-first section below is retained for historical compatibility with the branch's pre-main-sync controller. Where its locator ordering or single-miss construction wording conflicts with V58, V58 governs current Stage33 MAIN execution. The forthcoming current-main controller synchronization must preserve V58 semantics rather than restore a one-search budget.

## V39 locator-first construction constitution

The exact mathematical frontier remains V25-V36: one J2-adapted Kummer column is materialized (`1/10`), original standard columns remain `0/10`, and V36 remains the exact record that the bounded #1498 scan found no registered positive asset directly supplying another standalone genuine full-surface H2(mu2) lift.

V39 supersedes only V36's operational STOP. It does **not** change V25-V36 mathematics or grant any mathematical credit.

For every unresolved evidence leaf:

1. Identify the exact missing object from `MAIN-STATE.json` and the active micro-roadmap.
2. Query #1498 first with `python3 -B docs/evidence-locator/query_evidence.py <terms>` when the micro-goal calls for an existing reusable asset.
3. If there is a suitable candidate, inspect only that bounded candidate and recheck the live Stage authority before use.
4. If there is no suitable candidate, record only `LOCATOR_MISS_NOT_REPO_ABSENCE` and proceed to construct/derive the missing exact object. Do **not** fall back to broad repository/history/origin search.
5. After a newly constructed object is exactly verified and reusable, register it in the locator with its exact provenance and limitations.

Anti-loop applies to repeated broad origin/history searches, repeated deep inspection of already-rejected candidates without a new signal, unsupported standard-column splitting, and guessed remaining columns. Anti-loop does **not** prohibit re-querying #1498 as the routing step and does **not** prohibit new mathematical construction after a locator miss.

The current construction priority is `e3, e1, e4, e5, e6, e7, e8, e9, e10`. Within each source, use the active micro-roadmap sequence rather than treating an entire lift/column as one batch.

Do not infer `e3` by splitting `J2 = e2+e3`, do not split standard col2/col3 from the XOR relation, and do not guess any remaining Kummer column.

## Authority and release

Controller V61 and `sync_main_state.py` generate `MAIN-STATE.json` V18. Mathematical authority remains the V25-V36 exact certificate chain; V39/V40 is operational routing authority only. V38 remains the historical synchronization receipt. Dedicated current routing CI is `.github/workflows/stage33-v39-routing.yml`.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

After writes, run the verifier for the selected micro-goal, then:

- `python stages/stage33/33-12/verify_e3_search_routing_supersession_v58.py`
- `python stages/stage33/33-12/verify_j2_post_v38_locator_first_construction_policy_v39.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.

## Hostile-audit multi-registry repair

Current-main locator routing means `index.json`, `stage32-post1498.json`, and `stage33.json` are all searched before construction when the selected micro-goal requires locator routing. A nonempty candidate list is not a suitable-hit verdict: inspect only the bounded candidate limitations. The current Stage33 Gersten 26-column candidate is relevant but explicitly does not itself identify a standalone genuine remaining retained10 H2(mu2) lift, so construction is authorized only after that bounded classification.

The one-shot hostile-audit synchronization runner and repair script were removed after their successful transition. Ordinary Stage33 routing now uses only the retained V39/V40 verifier, controller/generator state, current multi-registry locator, and the active micro-roadmap for execution granularity.
