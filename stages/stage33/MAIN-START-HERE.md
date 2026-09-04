# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

Stage33 is stricter than the repo-wide traversal rule. For ordinary research/navigation, follow exactly:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

- Start from `stages/stage33/controller.json` and the active roadmap named or implied by the current leaf. Do not enumerate repository contents to rediscover state already named there.
- For the current 33-12 microgoal, the active roadmap is `stages/stage33/ROADMAP-33-12-MICROGOALS.md`; keep the current leaf split into one tiny verifiable goal per commit.
- For reusable cross-Stage weapons, read `docs/arsenal/index.json`, select only matching IDs, then read only the needed card and exact source/certificate paths referenced by that card.
- Known paths are fetched directly. File/path discovery uses GitHub search. Term/content discovery uses GitHub code search.
- A recursive repository tree is not an ordinary Stage33 discovery tool. Use it only if the active research task explicitly requires enumeration of the full file set itself.
- A search miss never proves repository absence and must not be promoted to mathematical absence.

## V58 Arsenal-first repeatable bounded-search constitution

The exact mathematical frontier remains V25-V36 plus the branch-local e3 construction chain through V57. One J2-adapted Kummer column is materialized (`1/10`), original standard columns remain `0/10`. V58 changes operational discovery routing only and does not grant mathematical credit.

V58 (`stages/stage33/33-12/e3-search-routing-supersession-v58.json`) explicitly supersedes only the fixed one-search cap in main V41 routing. Until the compact controller/state projection is regenerated on this branch, V58 takes precedence over any inherited V41 field that says `one automatic bounded repository search` or budget `=1`.

For every unresolved evidence leaf:

1. Identify the exact missing object from the live Stage33 authority and active micro-roadmap.
2. Use **Arsenal first**: read `docs/arsenal/index.json`, select only matching IDs, and inspect only the needed cards/source locks.
3. If Arsenal has no suitable hit, run a bounded repository search tied to a concrete load-bearing subquestion and a narrow named scope.
4. Additional bounded searches are allowed with **no fixed per-object count cap** only when the next query follows a materially new mathematical signal, alias, map/producer name, exact source path, or independently implicated candidate family.
5. Stop when the bounded question is answered, the named candidate family is exhausted, the reusable asset is source-locked, or further search would require repository-wide enumeration, branch-history archaeology, unconstrained keyword expansion, or near-equivalent miss chasing.
6. A miss in Arsenal or any bounded search is **not repository absence** and is not mathematical nonexistence.
7. When the current leaf has enough exact information, construct/derive the missing object; search need not continue merely because more bounded queries are possible.
8. Before reusing any hit, recheck live Stage authority and its exact limitations.

The current construction target is e3 A2.4: `B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX`, a `14 x 4` exact matrix, followed by the membership solve `M*x = mask20`. Do not infer e3 by splitting `J2 = e2+e3`, do not split standard col2/col3 from the XOR relation, and do not guess any remaining Kummer column.

## Authority and release

Current-main Research OS structure remains inherited from Controller V62. V58 is the branch-local operational supersession for the fixed search-count cap; mathematical authority remains the exact certificate chain and the e3 branch certificates through V57. No closure, receiver, endpoint, theorem, or merge credit is granted by this routing change.

`MAIN-BATCH-HANDOFF.md` is retired and must not be recreated.

After writes, run at minimum:

- `python stages/stage33/33-12/verify_e3_search_routing_supersession_v58.py`
- `python stages/stage33/33-12/verify_e3_mask20_b1_gysin_image_gate_v57.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
