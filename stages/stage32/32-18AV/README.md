# Stage32-18AV — d16 b16 remaining-wall frontier cost scout

## Purpose
Measure the same cut39 lower-frontier cost shape used on `p436/s5` for the other five unresolved b16 walls, in parallel, without granting numerical or theorem credit.

Targets:
- `p436/s362`
- `p503/s118`
- `p503/s665`
- `p922/s13`
- `p922/s38`

Each job reconstructs the exact upper cut39 frontier from the locked source artifact, then probes every frontier state with an exact local lower-search budget of 2,048 nodes. The output is a compact cost histogram plus capped-heavy frontier IDs. This is workload reconnaissance only; it is not production and does not change mathematical credit.

## Safety / resource contract
- Locked exact source artifact: `9574308138`, ZIP SHA256 `0671a8a8637641f5cc4da36b99700b1511c923d03e5ea446317d17b35bd88fc4`.
- Five heavy jobs, `max-parallel: 5`.
- With the already-running single-job 18AT planner, planned Stage32 effective heavy concurrency is at most 6, below the repo-wide cap 18.
- Persist only compact per-wall planner outputs; raw exhaustive state stays runner-local.
- Frontier cap is 50,000 states per wall. This is a safety envelope, not a mathematical claim.
- Intermediate artifacts use 7-day retention. Based on the prior p436/s5 planner artifact (~30 KB), even a large safety-factor projection remains far below the 500 MB operating budget.
- A dedicated runkey and dedicated ARM commit are required. Controller/docs edits cannot authorize rerun.

## Firewalls
`D16_B16_NUMERICAL_CREDIT=false`, `GLOBAL_B16_AGGREGATION_COMPLETE=false`, `FULL_D16_G0_ROW_COMPLETE=false`, `THEOREM_CREDIT=false`, `RECEIVER_CREDIT=false`.
