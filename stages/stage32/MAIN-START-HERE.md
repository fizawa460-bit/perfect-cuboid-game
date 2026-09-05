# Stage32 MAIN startup

Ordinary `Stage32-main-batch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/MAIN-START-HERE.md`;
3. `stages/stage32/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This is the ordinary startup contract. Do not preload the Stage32 root directory, historical roadmaps, controller history, production state, runkeys, audits, or Research OS beyond an explicit trigger below.

## Authority split

`MAIN-STATE.json` is the current mutable **ordinary startup projection**. It is not a proof certificate and does not rewrite historical evidence.

Exact mathematical claims remain grounded in hostile-audited certificates/source locks. Historical files such as `controller.json`, `residual-32-01-production/state.json`, old FULL178 runkeys, and old roadmaps remain retained evidence/operational history but are not current-leaf startup authority.

If a historical file conflicts with `MAIN-STATE.json` about the current leaf or next route, use `MAIN-STATE.json` for ordinary routing and use the exact referenced certificate chain for mathematical claims. Do not infer new credit from the compact state.

## Current Stage32 frontier

The fixed target remains `g1-d186`, `O=210`, `qprime=4`, `Q=602`, with surviving residues `73,97,235`.

The #1577 ambient-symmetry / orbit-sum / parity detector lane is closed. #1588 obtained a genuine direct mod-2 fiber-divisor identity, but its mod-2 class is supported entirely in the exceptional span and maps to zero in the quotient by that span.

Therefore the next admissible constructive input is either:

- a direct mod-2 divisor/correspondence class with a proved nonexceptional component; or
- an independent primitive/odd commutator invariant.

Do not repeat the closed symmetry/parity detector without materially new input.

## Search and Arsenal routing

Repository discovery is search-first; never request a recursive/full tree. For an existing weapon/evidence lookup, read `docs/research-os/policies/repository-asset-discovery.md`, then `docs/arsenal/index.json`, then only the relevant card(s) and exact referenced assets.

A search miss is not repository-wide absence and is not mathematical nonexistence.

## On-demand files, not ordinary startup

Open these only when the active task requires them:

- inherited finite target / receiver semantics: `ROADMAP.md`, `GOAL_AND_STOP_CONTRACT.md`;
- heavy workflow design/rerun/diagnosis: `HEAVY_WORKFLOW_POLICY.md` plus the Actions-safety policy triggered by `AGENTS.md`;
- historical FULL178 execution: `residual-32-01-production/state.json`, `runkeys/residual32-01-full178-production.json`, `ROADMAP-32-19-21-REANCHOR.md`;
- historical detailed controller chronology: `controller.json` and its exact archives;
- history/old planning: only when explicitly needed for provenance or cleanup-reference audit.

None of these historical files authorizes heavy compute merely by being present.

## Firewalls

At startup: `Q602_excluded=false`, `O210_excluded=false`, `O212+` advance is unauthorized, and no controller/receiver/route/theorem/endpoint/perfect-cuboid credit is granted.

Do not merge without explicit user authorization.

## Root-cleanup sequencing

Do not delete or relocate Stage32 proof/source-locked assets merely because they are not in ordinary startup. First hostile-audit this startup authority split. Then perform a bounded root reference inventory and classify each direct-root item as startup-required, proof/source-locked, archive-candidate, or delete-candidate before any cleanup deletion.
