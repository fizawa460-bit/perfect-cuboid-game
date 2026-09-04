# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

Stage33 is stricter than the repo-wide traversal rule. For ordinary research/navigation, follow exactly:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

- Start from `stages/stage33/controller.json` and the active roadmap named or implied by the current leaf. Do not enumerate repository contents to rediscover state already named there.
- For reusable cross-Stage weapons, read `docs/arsenal/index.json`, select only matching IDs, then read only the needed card and exact source/certificate paths referenced by that card.
- Known paths are fetched directly. File/path discovery uses GitHub search. Term/content discovery uses GitHub code search.
- A recursive repository tree is not an ordinary Stage33 discovery tool. Use it only if the active research task explicitly requires enumeration of the full file set itself.
- A search miss never proves repository absence and must not be promoted to mathematical absence.

## V41 Arsenal-first bounded-search constitution

The exact mathematical frontier remains V25-V36: one J2-adapted Kummer column is materialized (`1/10`), original standard columns remain `0/10`, and the historical bounded reuse scan did not materialize another standalone genuine full-surface H2(mu2) lift. V41 changes operational discovery routing only. It does **not** change V25-V36 mathematics or grant mathematical credit.

For every unresolved evidence leaf:

1. Identify the exact missing object from `MAIN-STATE.json`.
2. Open `docs/research-os/policies/repository-asset-discovery.md` and use **Arsenal first** for an already-existing cross-Stage weapon: read `docs/arsenal/index.json`, select only matching IDs, and inspect only the needed cards/source locks.
3. If Arsenal has no suitable hit, **one automatic bounded repository search is authorized** for that missing object. Keep it narrow: canonical Stage `FINAL.md` handoffs (Stage16+), canonical final HTML handoffs (Stages12-15), directly implicated report/directory paths, and exact missing-object terms.
4. A miss in Arsenal or that bounded search is **not repository absence**.
5. Any broader repository/history/origin archaeology, repeated bounded search, or expansion beyond that one-search budget requires **explicit user authorization**.
6. If there is still no suitable hit and no broader search is authorized, proceed to construct/derive the missing exact object from current exact source data.
7. Before reusing any hit, recheck live Stage authority and its exact limitations.

The current construction/search priority remains `e3, e1, e4, e5, e6, e7, e8, e9, e10`.

Do not infer `e3` by splitting `J2 = e2+e3`, do not split standard col2/col3 from the XOR relation, and do not guess any remaining Kummer column.

## Authority and release

Controller V62 and `sync_main_state.py` generate the compact MAIN projection. Mathematical authority remains the V25-V36 exact certificate chain. V41 is operational routing authority only.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

After writes, run:

- `python stages/stage33/33-12/verify_j2_post_v39_arsenal_first_bounded_search_policy_v41.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
