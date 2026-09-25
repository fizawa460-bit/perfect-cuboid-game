# Stage32 canonical command surface

Stage32 now has one ordinary operator entrypoint.

## Operator-facing commands

- `stage32mainbatch` — follow `stages/stage32/ROADMAP.md`, read `MAIN-STATE.json`, select the current incomplete formal unit, and coordinate only the execution surface needed for that unit. Startup: `stages/stage32/MAIN-START-HERE.md`.
- `stage32audit` — hostile audit of a frozen exact MAIN/final-chain boundary. PASS is not merge authorization.

For normal work, these are the only commands the operator needs.

## Internal / on-demand execution commands

These commands remain valid because they preserve isolated heavy-run, resume, and audit boundaries. They are not competing Stage32 controllers and are not all preloaded by `stage32mainbatch`.

- `stage32ex5-mainbatch`, `stage32ex5-audit` — 32-02 Picard64/affine exact-certificate backend. Startup is `stages/stage32-ex5/MAIN-STATE.json`.
- `stage32mb-mainbatch`, `stage32mb-audit` — 32-03 multibranch execution surface.
- `stage32mb-fib`, `stage32mb-fib-audit` — MB-local auxiliary fibration/Picard64 heavy surface; not a separate claim-DAG lane.
- `stage32-01-178-mainbatch`, `stage32-01-178-audit` — retained 32-01 specialist; **parked/on-demand because the required numerical census is audited complete**.
- `stage32cut-mainbatch`, `stage32cut-audit` — retained direct-obstruction specialist; no ordinary open successor.
- `stage32bridge-mainbatch`, `stage32bridge-audit` — retained experimental FULL178 bridge; parked after 32-01 completion unless MAIN explicitly reopens it.

Historical child commands such as `stage32-01-178-a..f`, `stage32ex5-a..h`, and checkpoint-specific commands are history only unless an explicit current assignment re-enables them.

## Routing authority

Ordinary routing is:

`ROADMAP current incomplete unit` -> `MAIN-STATE current routing` -> `selected unit state` -> exact retained evidence.

`stages/stage32/proof/LANE-ADAPTERS.json` remains the machine registry for claim-lane adapters. Stage32EX5 is intentionally collapsed to `stages/stage32-ex5/MAIN-STATE.json`. MB-FIB remains outside the claim-lane adapter registry.

`CROSS-LANE-DEMANDS.json` is consulted when a real producer/consumer dependency exists; it is not a mandatory every-start preload. This file is a command registry, not a second startup contract and grants no mathematical credit or merge authorization.
