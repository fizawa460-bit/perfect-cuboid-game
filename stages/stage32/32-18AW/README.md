# Stage32-18AW — D16/B16 remaining-wall tier2 cost planner

Purpose: extend the successful 18AS selective tier2 measurement from p436/s5 to the five other unresolved B16 walls, using the exact 18AV heavy frontier IDs only.

Locked inputs:
- exact source artifact: 9574308138
- 18AV run: 33143519365
- walls: p436/s362, p503/s118, p503/s665, p922/s13, p922/s38
- cut: 39
- tier1 probe budget: 2048 nodes
- tier2 probe budget: 32768 nodes
- max heavy concurrency: 5 (plus the independent 18AT planner gives effective Stage32 heavy concurrency <= 6)

Execution contract:
- download and digest-check the compact 18AV artifact for each wall;
- extract only that wall's `heavy_frontier_ids`;
- reconstruct the exact same cut39 frontier and selectively probe only those IDs at 32768 nodes;
- persist compact cost certificates only; raw dump/cost CSV remain runner-local and are deleted before upload;
- no finer split and no production claim.

This is workload-shape reconnaissance only. It grants no D16/B16 numerical, theorem, receiver, or endpoint credit.
