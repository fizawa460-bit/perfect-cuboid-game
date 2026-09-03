# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## V39 locator-first construction constitution

The exact mathematical frontier remains V25-V36: one J2-adapted Kummer column is materialized (`1/10`), original standard columns remain `0/10`, and V36 remains the exact record that the bounded #1498 scan found no registered positive asset directly supplying another standalone genuine full-surface H2(mu2) lift.

V39 supersedes only V36's operational STOP. It does **not** change V25-V36 mathematics or grant any mathematical credit.

For every unresolved evidence leaf:

1. Identify the exact missing object from `MAIN-STATE.json`.
2. Query #1498 first with `python3 -B docs/evidence-locator/query_evidence.py <terms>`.
3. If there is a suitable candidate, inspect only that bounded candidate and recheck the live Stage authority before use.
4. If there is no suitable candidate, record only `LOCATOR_MISS_NOT_REPO_ABSENCE` and proceed to construct/derive the missing exact object. Do **not** fall back to broad repository/history/origin search.
5. After a newly constructed object is exactly verified and reusable, register it in the locator with its exact provenance and limitations.

Anti-loop applies to repeated broad origin/history searches, repeated deep inspection of already-rejected candidates without a new signal, unsupported standard-column splitting, and guessed remaining columns. Anti-loop does **not** prohibit re-querying #1498 as the routing step and does **not** prohibit new mathematical construction after a locator miss.

The current construction priority is `e3, e1, e4, e5, e6, e7, e8, e9, e10`. The next ordinary action is: query #1498 for a standalone genuine full-surface H2(mu2) lift for `e3`; if no suitable hit exists, construct the `e3` lift from current exact source data.

Do not infer `e3` by splitting `J2 = e2+e3`, do not split standard col2/col3 from the XOR relation, and do not guess any remaining Kummer column.

## Authority and release

Controller V60 and `sync_main_state.py` generate `MAIN-STATE.json` V17. Mathematical authority remains the V25-V36 exact certificate chain; V39 is operational routing authority only. V38 remains the historical synchronization receipt. Dedicated current routing CI is `.github/workflows/stage33-v39-routing.yml`.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

After writes, run:

- `python stages/stage33/33-12/verify_j2_post_v38_locator_first_construction_policy_v39.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
