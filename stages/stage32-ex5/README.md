# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary research surface for the current Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`. It is not a current V6, O210, or Q602 attack.

## Current Stage32 authority

As synchronized against Stage32 MAIN PR #1753:

- control mode: `FULL178_AND_FINAL_MILESTONE_CHAIN`;
- primary incomplete requirement: `32-01 FULL178`;
- downstream final milestones remain gated by the FULL178/finality chain;
- V6 / O210 / Q602 are frozen historical/formal prerequisite provenance, not current attack targets;
- `[73,97,235]` is the formal historical Q602 residue triple from the earlier proof path, not the current Stage32 survivor population.

The observed Stage32 MAIN authority head for this synchronization is `6327346d336028c910410da9bd430e117ecc024d`. Current repository `main` was `e2da76d90a0994af5038023613c6c4084c4c507e`; later Stage32 MAIN movement must be rechecked before any EX5-to-MAIN promotion.

## What EX5 can contribute to 32-01 FULL178

The current EX5 BC2 line develops an exact interface/obstruction chain for FULL178 compressed terminal data:

`FULL178 indexed terminal / pairings`
`-> exact Picard64 completion constraints`
`-> integral Picard / 59D witness reconstruction when SAT`
`-> canonical 48-node support consumer through the retained runtime-node bridge`.

This gives two useful kinds of output:

1. **UNSAT obstruction:** an exact terminal or exact finite block has no integral Picard64 completion under the locked model, so that certified portion of the FULL178 geometric input can be pruned.
2. **SAT interface:** an exact Picard witness can be reconstructed and passed to the canonical node-support interface for downstream geometric/effectivity analysis.

Neither output automatically grants FULL178 completion, Stage32 MAIN credit, effectivity, actual-curve existence, receiver credit, a final milestone, or a Perfect Cuboid endpoint claim.

Stage32 MAIN node `32-01-178/N150` is the intended consumption gate: MAIN may consume EX5 only after a retained/audited FULL178-target-compatible producer/result and an explicit adapter to the 32-01 numerical-census semantics exist. EX5 progress newer than the current N150 snapshot is therefore retained locally until MAIN explicitly consumes it.

## Current exact EX5 progress

For the local `(g1-d008,e=4)` indexed terminal stratum, retained exact Picard64 UNSAT blocks are:

- ranks `0..132`;
- ranks `133..265`;
- ranks `266..398`.

Thus ranks `0..398` are locally closed in this stratum. The whole `(g1-d008,e=4)` stratum remains open, and FULL178 remains incomplete.

Latest retained checkpoint:

- `stages/stage32-ex5/breadth-cycle-2/bc2-10-outer-rank2-exact-unsat-checkpoint.json`;
- checkpoint canonical `1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b`;
- evidence canonical `06e4e0e8fbbe1bb64fc757be58f272fec0e85bea1e3bd7a9f21f8bf0dbda1531`.

Current next unit: `BC2_11_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`, which rederives the next 133-rank outer exceptional block after rank 398 before any further Picard64 solver credit.

## Historical/formal provenance firewall

Earlier EX5 artifacts were built while the Stage32 narrative prominently referenced V6/O210/Q602 and the formal Q602 triple `[73,97,235]`. Those retained artifacts and their canonical evidence remain valid at their original scopes and are not rewritten.

Current-facing EX5 documents must not present those objects as the live Stage32 target or current survivor set. Old `no O210/Q602 credit` language is interpreted as a **historical-credit firewall**: EX5 does not mutate, recompute, or claim new credit for the frozen V6/O210/Q602 line unless current Stage32 MAIN explicitly reopens it.

## Operating files

- startup: `MAIN-START-HERE.md`
- current routing/state: `MAIN-STATE.json`
- current roadmap and claim boundaries: `CURRENT-ROADMAP.md`
- historical source-locked Cycle1 roadmap: `stage32-ex5.md`
- hostile audit: `AUDIT-CONTRACT.md`
- current state verifier: `verify_main_state.py`

`stage32-ex5.md` is retained because historical Cycle1 evidence source-locks that exact blob. Current terminology changes belong in `README.md`, `CURRENT-ROADMAP.md`, `MAIN-STATE.json`, and the audit/startup contracts instead.

Exact evidence/checkpoint files are proof records, not prose state, and must not be rewritten merely to synchronize terminology.

Merge remains forbidden without explicit user authorization.
