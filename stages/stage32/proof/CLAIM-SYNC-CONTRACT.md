# Stage32 claim-DAG synchronization contract

Status: **ACTIVE OPERATIONAL HOOK — ON-DEMAND ONLY**

This contract connects ordinary Stage32 MAIN / EX research to the claim-management layer introduced by #1706. It does **not** change ordinary startup and must not be preloaded for scratch-only work.

## 1. Ordinary research remains unchanged

Ordinary `stage32main batch` and mapped `stage32exN-mainbatch` runs still use their existing startup sets and current-leaf working sets. The claim registry, active-frontier shard, lane adapters, proof path, and FINAL-CHECK are not ordinary startup files.

Scratch diagnostics, route probes, failed micro-techniques, and non-retained experiments remain outside the claim DAG. A scratch result cannot be used as a proof dependency or MAIN promotion input.

## 2. Synchronization triggers

Claim-DAG synchronization is mandatory when any of these events occurs:

- `RETAINED_CONSOLIDATION`: a successful leaf/result is retained into a shared or audit-ready checkpoint;
- `AUTHORITY_OR_AUDIT_TRANSITION`: a retained claim changes SCRATCH/PROVISIONAL/AUDITED/SUPERSEDED/REVOKED status, including hostile-audit PASS/FAIL/revocation consumption;
- `EX_TO_MAIN_PROMOTION`: an EX result is proposed for or actually connected to MAIN authority;
- `ACTIVE_FRONTIER_REMAP`: a lane begins attacking/consuming a materially different active claim, or a new Stage32 EX lane is enrolled;
- `FINAL_MILESTONE_TRANSITION`: a reserved Stage32 final-proof milestone is created, versioned, audited, revoked, or rewired.

Scratch-only work does not trigger claim-DAG writes.

Audit transitions are deliberately asymmetric before registry synchronization:

- hostile-audit **PASS**: downstream credit remains at the previous, lower pre-sync authority level until the exact PASS receipt and claim core are synchronized. A PASS receipt by itself does not silently mutate the claim registry;
- hostile-audit **FAIL** or explicit **revocation**: downstream consumption of the affected claim is blocked immediately when the invalidating result is known. The previous `AUDITED` level must not remain consumable merely because the registry downgrade/revocation has not yet been written;
- the registry's `SUPERSEDED` / `REVOKED` / downgraded authority metadata is then synchronized at the claim-sync checkpoint with the exact invalidating audit/revocation source lock.

Thus synchronization latency may delay an authority increase, but it may never delay an authority decrease or preserve invalidated downstream credit.

## 3. Trigger-time read set

At a synchronization trigger, open only:

1. this file;
2. `stages/stage32/STAGE32-PROOF-PATH.md`;
3. `stages/stage32/proof/LANE-ADAPTERS.json`;
4. the relevant claim shard(s): `CLAIM-REGISTRY.json` and/or `ACTIVE-FRONTIER.json` only as required;
5. `stages/stage32/FINAL-CHECK.json` only for a final-milestone transition;
6. the exact retained artifact/source lock/audit receipt needed for the changed claim.

Do not bulk-load Stage32 history merely because synchronization was triggered.

## 4. Synchronization procedure

For the triggering result:

1. identify the lane and exact existing claim ID(s) it attacks, consumes, or owns;
2. decide whether the result changes mathematical claim semantics or only evidence/authority metadata;
3. if statement, quantifier, population, model, field, scope, `PROVES`, `DOES_NOT_PROVE`, `requires`, `bridges`, source locks, or replay verifier changes, create a new versioned claim ID/core rather than mutating the old immutable core;
4. retain a mathematically relevant candidate as `PROVISIONAL` with exact source locks/replay path before any promotion use;
5. assign `AUDITED` only from an exact hostile-audit PASS receipt for the same claim core/evidence boundary; never self-assign audit credit;
6. if a hostile-audit FAIL or revocation is known for a previously consumable claim, block every downstream use of that claim immediately, then synchronize the downgrade/revocation and invalidating receipt before allowing any later consumption;
7. update lane `ATTACKS`/`CONSUMES`/`OWNER` references when the active frontier materially changes;
8. for EX -> MAIN, require the audited EX terminal claim plus an explicit current-target promotion adapter; a lane reference or PASS narrative is insufficient;
9. keep `MAIN-STATE.json` / EX `MAIN-STATE.json` as routing authority; claim-DAG synchronization does not replace or silently rewrite lane routing state;
10. preserve all existing credit firewalls and `DOES_NOT_PROVE` ceilings.

## 5. New EX lane enrollment

A new Stage32 EX lane may research on scratch/provisional footing before claim-DAG enrollment, but it cannot promote mathematical credit to MAIN until it is registered in `LANE-ADAPTERS.json` with:

- a stable lane name;
- exact `state_path`;
- exact `startup_path`;
- relevant registered `claim_refs`;
- exact `active_frontier_refs` for current `ATTACKS`/`CONSUMES` routing.

Its startup contract must contain the same on-demand synchronization hook as the currently mapped lanes. If it attacks a genuinely new mathematical obligation, add/version the corresponding active-frontier claim before promotion.

## 6. Required verification at a synchronization checkpoint

Before declaring the synchronization checkpoint complete, run:

```text
python stages/stage32/proof/verify_stage32_claim_dag.py --integrity
python stages/stage32/proof/verify_stage32_active_frontier.py
```

For a final-milestone transition, also run the real FINAL-CHECK path. `NOT_READY_STAGE32_FINAL_CHECK` remains the expected result until the complete reserved audited closure chain actually exists.

A verifier failure blocks promotion/authority consumption; it does not erase the underlying research artifact.

The active-frontier verifier includes a synthetic authority-transition regression: a known hostile-audit FAIL or revocation against a pre-sync `AUDITED` claim must evaluate as non-consumable downstream, while a PASS against a lower-authority claim must not increase its consumable authority before synchronization.

## 7. User-facing operating rule

The user may continue issuing ordinary commands such as `stage32main batch` and `stage32exN-mainbatch`. The agent is responsible for recognizing the trigger events above and performing claim-DAG synchronization only when required.

No synchronization event grants merge authorization, heavy-compute authorization, Stage32 closure, receiver/theorem credit, or Perfect Cuboid endpoint credit by itself.
