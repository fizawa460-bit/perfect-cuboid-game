# stage32ex5-f

Role: Picard-slot / intersection-signature reverse lookup for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only exact Picard/intersection/pairing artifacts discovered search-first

Task: work backwards from the runtime exceptional slots, especially the `92+k` convention and retained Picard/intersection/pairing matrices, to construct an order-independent signature for each exceptional divisor. Determine whether those signatures can be matched exactly and injectively to the 48 source singular nodes using incidence with retained curves or other exact geometric data.

Required deliverable: exact artifact/source locators, definition of the signature, 48-count/uniqueness table, collision ledger, exact node-matching rule if successful, and verifier/replay procedure. If signatures are insufficient, identify the smallest missing datum rather than falling back to guessed runtime order.

Do not assume matrix row/column labels without proving their provenance. Do not edit authority/state/claim files. No FULL178 span replay.

## Lane-F checkpoint

Status: `PASS_HANDOFF_READY` (scratch only; mainbatch consolidation/audit still required).

The exact Hperp adapter exposes a 140 x 64 pairing matrix whose rows preserve the locked Stoll `Cs cat pts` class order and whose columns are the retained primitive Picard-basis labels. Restricting those columns to the 26 labels `<=92` removes every exceptional-basis coordinate and leaves only fixed source curve labels

`[1,33,12,16,7,90,87,92,51,40,77,44,20,55,19,56,73,79,75,24,26,52,18,11,3,6]`.

For each runtime exceptional slot `k`, use the 26 entries of row `92+k` as its Picard incidence signature. Independently reconstruct the 48 source singular nodes and the 92 Stoll curves, then evaluate node membership in those same 26 labelled curves. The 48 candidate signatures are all distinct, so exact signature equality gives a 48/48 bijection. This rule does not consume `Points(SingularSubscheme(S))` traversal order and does not use any exceptional-basis column. The full 92-curve sanity check is stronger: all 48 node signatures are distinct and every node is incident to exactly 10 known curves.

Artifacts:
- `lane-f/bc2-01b-exceptional-pairing-canonical.json` — 48-row map, source locks, collision ledger, selected26 rule, replay expectations.
- `lane-f/verify_bc2_01b_exceptional_pairing.py` — fail-closed rederivation from retained Picard/Hperp data and locked Stoll equations.
- `lane-f/VERIFY-DAG.txt` — compact proof/replay DAG.

Replay:
`python3 stages/stage32-ex5/parallel/lane-f/verify_bc2_01b_exceptional_pairing.py`

The verifier additionally checks candidate/slot traversal permutations and projective rescaling by `2`, `-3`, and `i`; these do not change the signature match. `mapping_sha256 = 2c3cdbf40a1c896a1ab2bfeded21d89798ef425150ae6ebc3c4d63491aee2fc1`.

Firewalls remain unchanged: scratch result only; no FULL178 span replay, no Stage32/Q602/O210/endpoint credit, no merge.
