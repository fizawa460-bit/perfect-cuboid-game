# Stage33 rules

Stage33 inherits `AGENTS.md` and `docs/research-os/`. Stage-local rules may
strengthen but never weaken repo-wide Actions/storage, research-credit,
promotion, cycle-safety, or claim firewalls.

## Authority

Use current material in this order:

1. repo-wide policy (`AGENTS.md`, triggered Research OS policy);
2. this file for stable Stage33 scope/release rules;
3. `MAIN-STATE.json` for ordinary MAIN routing and compact current state;
4. `controller.json`, active unit state, and exact certificates for detailed
   machine/mathematical authority;
5. `HISTORY.md`, roadmaps, and Git for provenance and history.

Historical status never overrides current exact authority. Certificate credit is
limited to the certificate's declared interface and scope.

## Frozen scope and release

Stage33 executes the frozen Stage29 physical-open Brauer kernel
`K16-C2-BRAUER-EXPLICIT-CHAIN` / `BRAUER-EXPLICIT-DAG`.
Detailed acceptance criteria remain in `33-00/unit-closure-contract.md`.

Stage33 has 11 big tasks. Repair children do not increment that denominator.
Downstream work releases only when the required exact state and hostile
recertification are complete. Preview, numerical, blocked, or audit-pending
states do not count as closed.

## Stop and anti-loop rules

A Stage33 mathematical line may stop only as:

- `EXACT_BRANCH_CLOSURE`
- `NEW_KERNEL_EXPOSED`
- `HOSTILE_AUDIT_REQUIRED`
- `EXECUTION_RESOURCE_WALL`

A durable operational checkpoint does not itself authorize stopping.

Respect `MAIN-STATE.resolved_investigations`,
`MAIN-STATE.anti_loop_policy`, and any active `work_checkpoint`.
Do not repeat a closed investigation under the same effective premises.
Reopen only for a listed condition or a materially changed exact interface.

If two consecutive MAIN batches leave the same effective receiver/missing
interface and candidate information unchanged, with no independent observation,
no candidate or materially distinct route removed, and no missing interface
constructed, a third same-route continuation requires a breadth/route audit
first. Bookkeeping, controller edits, verifier wiring, CI status, source-lock
restatement, renaming, or an equivalent reformulation do not count as new exact
information by themselves.

## Ordinary MAIN routing

`MAIN-START-HERE.md` is the short routine routing contract. Ordinary startup is
bounded to `AGENTS.md`, `MAIN-STATE.json`, and its `current_leaf_working_set`.
The full controller, this RULES file, history, old repair state, and cold
evidence are not routine startup inputs.

`MAIN-STATE.json` has two roles:

- all fields except `work_checkpoint` are generated compact projection;
- `work_checkpoint` is the single durable operational scratch field.

`work_checkpoint` must have authority `OPERATIONAL_ONLY_NOT_PROOF`. It may record
only useful unpromoted narrowing, anti-repeat information, and the immediate
current action. It must never select a mathematical source, grant proof credit, or
override certificates/controller.

When unpromoted work materially changes the current action or anti-repeat boundary,
commit `work_checkpoint` promptly before broader exploration. `sync_main_state.py`
must preserve it. Clear it only after exact promotion subsumes it, or replace it
with the corrected narrow blocker.

`MAIN-BATCH-HANDOFF.md` is retired. No workflow, promotion helper, or MAIN batch
may recreate or reset a separate handoff file.

## File roles

- `MAIN-START-HERE.md`: short routine routing only.
- `MAIN-STATE.json`: compact startup projection plus the one operational checkpoint.
- `controller.json`: detailed current mathematical/release machine state.
- active unit state/certificates/verifiers: exact mathematics and evidence.
- `CURRENT.md`: compatibility pointer only; it must not duplicate mutable state.
- `HISTORY.md` and roadmaps: non-routine provenance/planning.

Do not duplicate mutable current state across additional operational documents.
