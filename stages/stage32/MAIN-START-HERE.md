# Stage32 MAIN startup

Ordinary `Stage32-main-batch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/MAIN-START-HERE.md`;
3. `stages/stage32/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. It does not contain the mutable Stage32 frontier, current target, survivor set, next route, current firewall values, or cleanup progress. Read all such current values only from `MAIN-STATE.json`.

Do not preload the Stage32 root directory, historical roadmaps, controller history, production state, runkeys, audits, or Research OS unless `MAIN-STATE.json`, `AGENTS.md`, or the active task explicitly requires them.

## Authority split

`MAIN-STATE.json` is the current mutable ordinary startup projection. It is not a proof certificate and does not rewrite historical evidence.

Exact mathematical claims remain grounded in the hostile-audited certificates and source locks referenced by `MAIN-STATE.json`. Historical controller, production-state, runkey, roadmap, audit, and history files remain evidence or operational history; they are not ordinary current-leaf startup authority merely because they exist.

If historical material conflicts with `MAIN-STATE.json` about current routing, use `MAIN-STATE.json` for ordinary routing and use the exact referenced certificate chain for mathematical claims. Do not infer new mathematical credit from the compact state itself.

## Search and Arsenal routing

Repository discovery is search-first; never request a recursive/full repository tree. For an existing weapon or evidence lookup, follow the repository discovery policy referenced by `AGENTS.md`, then `docs/arsenal/index.json`, then only the relevant card(s) and exact referenced assets.

A search miss is not repository-wide absence and is not mathematical nonexistence.

## On-demand history

Historical Stage32 files may be opened only when the current state or active task requires their exact semantics, provenance, heavy-workflow history, source lock, audit record, or cleanup-reference analysis. Their presence does not authorize heavy compute or change current credit.

## Write and merge discipline

Before writes, follow the current gate and firewalls in `MAIN-STATE.json`. Proof/source-locked assets must not be deleted or relocated without an explicit reference audit authorized by the current state.

Do not merge without explicit user authorization.
