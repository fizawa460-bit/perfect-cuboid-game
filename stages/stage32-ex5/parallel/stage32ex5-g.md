# stage32ex5-g

Role: geometric exceptional-divisor -> blow-up-center/node reverse adapter for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only exact surface/blow-up/map/curve sources discovered search-first

Task: reconstruct the bridge from geometry rather than runtime enumeration. Starting from the exceptional divisors used by the Picard/runtime model, recover their blow-up centers or singular-node images through exact maps/equations/curve incidences. Match those centers to the 48 canonical projective singular nodes without relying on the incidental order returned by `Points(...)`.

Required deliverable: exact geometric source locators, explicit divisor-to-center/node rule, 48-count and bijection checks, scale/sign/equivalence conventions, ambiguity ledger, and verifier/replay procedure. If the geometric map loses labels, prove exactly where and how much information is lost.

Do not identify divisors merely by numeric slot unless independently justified. Do not edit authority/state/claim files. No FULL178 span replay.