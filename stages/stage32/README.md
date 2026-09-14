# Stage32

This README is a layout map only. It is **not** a startup/read-order contract and is not current mathematical routing authority. `stage32mainbatch` resolves through `COMMANDS.md` to the single MAIN startup contract `MAIN-START-HERE.md`; mutable routing/credit comes from `MAIN-STATE.json`, and operational cross-lane dependencies come from `proof/CROSS-LANE-DEMANDS.json`.

The retained final-chain architecture is `32-01 FULL178 -> 32-02 effectivity -> 32-03 multibranch -> 32-04 synthesis -> 32-05 hostile audit`; which step is currently active must be read from `MAIN-STATE.json`, not inferred from this README.

## Layout

- `32-01-178/` — FULL178 specialist surface. Ordinary startup is `32-01-178/MAIN-START-HERE.md`; `MISSION.json` and Generation-1 child-lane history are on-demand evidence, not a competing startup contract.
- `integrated-ex/` — integrated historical/user-facing view of former EX1-EX4 subresearch.
- `residual-32-01-production/` — retained FULL178 production evidence/code consumed through current routing.
- `proof/` — claim/frontier registries, adapters, demand coordination, and FINAL-CHECK support.
- `management/` — routing/checkpoint records.
- `archive/` — historical root documents and cleanup manifests.
- `scratch/`, `scouts/`, `runkeys/`, `audits/` — bounded operational support.

EX5 remains a separate specialist surface and is consumed only through current source-locked interfaces and the required audit/promotion gates.

Old numbered Stage32 paths are retained because verifiers/source locks may depend on them. Their presence does not make them ordinary startup authority. New loose root files should be limited to true startup/authority interfaces; put orchestration, management, proof, and historical material in their designated subdirectories.
