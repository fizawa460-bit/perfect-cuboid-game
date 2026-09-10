# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary research surface for the current Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`. It is not a current V6, O210, or Q602 attack.

## Current Stage32 authority

As synchronized against Stage32 MAIN PR #1753:

- control mode: `FULL178_AND_FINAL_MILESTONE_CHAIN`;
- primary incomplete requirement: `32-01 FULL178`;
- current observed stop gate: `N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER`;
- downstream final milestones remain gated by the FULL178/finality chain;
- V6 / O210 / Q602 are frozen historical/formal prerequisite provenance, not current attack targets;
- `[73,97,235]` is the formal historical Q602 residue triple from the earlier proof path, not the current Stage32 survivor population.

The observed Stage32 MAIN authority head for this synchronization is `a2cacaeb9b61eca34399952a7daaf5288ff3b826`. Current repository `main` is `bf2890ec0b8168f70db803de876024aa6b6d1f6d`; later Stage32 MAIN movement must be rechecked before any EX5-to-MAIN promotion.

## What EX5 can contribute to 32-01 FULL178

The current EX5 BC2 line develops an exact interface/obstruction chain for FULL178 compressed terminal data:

`FULL178 indexed terminal / pairings`
`-> exact Picard64 completion constraints`
`-> integral Picard / 59D witness reconstruction when SAT`
`-> canonical 48-node support consumer through the retained runtime-node bridge`.

This gives two useful kinds of output:

1. **UNSAT obstruction:** an exact terminal or exact finite block has no integral Picard64 completion under the locked model, so that certified portion of the FULL178 geometric input can be pruned.
2. **SAT interface:** an exact Picard witness can be reconstructed and passed to the canonical node-support interface for downstream geometric/effectivity analysis.

Neither output automatically grants FULL178 completion, Stage32 MAIN credit, effectivity, actual-curve existence, production-leaf coverage, receiver credit, a final milestone, or a Perfect Cuboid endpoint claim.

The legacy EX5 synchronization used Stage32 MAIN node `32-01-178/N150` as its consumption boundary. Current Stage32 MAIN has advanced to N350's production-leaf certificate/producer-registration boundary. N350 is still pending fresh hostile audit and its producer registry is empty, so current EX5 work has zero N350/N104 production-coverage credit and cannot self-register. A later MAIN-consumable EX5 producer requires exact canonical old-rank mapping, a source-locked replay verifier, fresh hostile-audit PASS, and explicit MAIN-side registration.

## Current exact EX5 progress

For the local `(g1-d008,e=4)` indexed terminal stratum, retained exact Picard64 UNSAT blocks are:

- ranks `0..132`;
- ranks `133..265`;
- ranks `266..398`.

Thus ranks `0..398` are locally closed in this stratum. BC2-11 has additionally rederived ranks `399..531` exactly at the structural rank/unrank + source-terminal-predicate level, with outer exceptional rank `3` and base terminal `[0,1,0,0,0,0,1,0,0,0,1]`; it grants no Picard64 closure credit. The whole `(g1-d008,e=4)` stratum remains open, and FULL178 remains incomplete.

Latest exact-UNSAT checkpoint:

- `stages/stage32-ex5/breadth-cycle-2/bc2-10-outer-rank2-exact-unsat-checkpoint.json`;
- checkpoint canonical `1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b`;
- evidence canonical `06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531`.

Latest structural checkpoint:

- `stages/stage32-ex5/breadth-cycle-2/bc2-11-next-exceptional-terminal-block-preflight-checkpoint.json`;
- canonical `b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d`.

Current next unit: `BC2_12_OUTER_RANK3_SYMBOLIC_X4_PARENT_PREFLIGHT`, which applies the retained symbolic-x4 Picard64 parent formulation only to the exactly rederived ranks `399..531` and derives the exceptional-mass split from the actual BC2-11 signature.

## Historical/formal provenance firewall

Earlier EX5 artifacts were built while the Stage32 narrative prominently referenced V6/O210/Q602 and the formal Q602 triple `[73,97,235]`. Those retained artifacts and their canonical evidence remain valid at their original scopes and are not rewritten.

Current-facing EX5 documents must not present those objects as the live Stage32 target or current survivor set. Old `no O210/Q602 credit` language is interpreted as a **historical-credit firewall**: EX5 does not mutate, recompute, or claim new credit for the frozen V6/O210/Q602 line unless current Stage32 MAIN explicitly reopens it.

## Operating files

- startup: `MAIN-START-HERE.md`
- current routing/state: `MAIN-STATE.json`
- current roadmap and claim boundaries: `CURRENT-ROADMAP.md`
- current hostile audit: `CURRENT-AUDIT-CONTRACT.md`
- historical source-locked Cycle1 roadmap: `stage32-ex5.md`
- historical source-locked Cycle1 audit contract: `AUDIT-CONTRACT.md`
- current state verifier: `verify_main_state.py`

`stage32-ex5.md` and `AUDIT-CONTRACT.md` are retained because historical Cycle1 evidence source-locks those exact blobs. Current terminology changes belong in `README.md`, `CURRENT-ROADMAP.md`, `CURRENT-AUDIT-CONTRACT.md`, `MAIN-STATE.json`, and startup/routing projections instead.

Exact evidence/checkpoint files are proof records, not prose state, and must not be rewritten merely to synchronize terminology.

## Intermediate audit boundary

Predecessor PR #1742 passed the required 100-commit intermediate hostile audit on exact head `a5e59bab3f7fe5a31e356c5a78edcbd741b093a6`, review `5161068590`, and was then merged to `main` at `bf2890ec0b8168f70db803de876024aa6b6d1f6d`. The freeze is therefore released for the current continuation; the audit scope/credit firewalls remain in force.

Current continuation is Draft PR #1762 on `impl/stage32ex5-bc2-11-continuation`. Merge remains forbidden without explicit user authorization.
