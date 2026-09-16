# Stage32 BRIDGE startup

This file is the authoritative startup/read-order contract for ordinary `stage32bridge-mainbatch`.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from live Stage32 MAIN authority;
4. current Issue `#1817` body and comments, treating them as research evidence only;
5. `stages/stage32/generalization-bridge/BR200-ISSUE1817-INTEGRATION-CHARTER-RESET.json`;
6. `stages/stage32/generalization-bridge/MISSION.json`;
7. `stages/stage32/generalization-bridge/STATE.json`, focusing on the current node, active leaf, next obligation, source locks, target-population boundary, and credit firewall;
8. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json` only if the active leaf explicitly needs a cross-lane dependency;
9. only the exact source/evidence/interface paths required by the active leaf.

Do not preload MB history, EX5 history, CUT history, old BR101-BR190 history, or unrelated Stage32 assets. Historical retained Picard64/HNF/59D assets may be opened only when the current active leaf source-locks them as inputs. Repository discovery remains search-first under root `AGENTS.md`.

Current `stages/stage32/MAIN-STATE.json` remains mathematical routing authority. Issue #1817 is a zero-credit research queue, not authority. BRIDGE never self-promotes an Issue comment, scratch result, sibling result, or bridge result to MAIN credit.

When Issue #1817 contains apparently conflicting research notes, use the strongest result that is logically established by the source-locked derivation, not merely the latest timestamp. In particular, the established **16-state Picard free-exceptional syndrome with `mu <= 8`** supersedes rougher exploratory notes that use `mu <= 133` or leave the syndrome image size unresolved.

## V2 mission

BRIDGE no longer performs open-ended cross-lane generalization search.

Its sole active mission is to integrate the converged Issue #1817 route into one compact, replayable, same-population FULL178 upper-bound producer:

```text
exact (b,c,t) population
  -> support + exact completion character r
  -> low-qBC tiers, K=8 first
  -> full qA histogram
  -> 16-state Picard residual-mass mu syndrome
  -> FULL178 compact b-sharded scaleout
  -> full qBC histogram only if material slack remains
  -> existing 59D solver only on late survivors
```

The primary objective is **compression and exact composition**, not discovery of a new unrelated obstruction.

## Historical BR190 boundary

The old `BR190-C3-RETAINED-AUDIT-HANDOFF.json` remains frozen, unaudited, unconsumed, and zero-credit. The V2 mission does not rely on its population-wide claim and does not convert it into authority.

A future use of that exact BR190 result still requires its own hostile audit. Reusing source-locked historical Picard64/HNF/59D code or mathematics does not reactivate BR190 or any historical specialist lane.

## Ownership

BRIDGE V2 owns only:

- exact source-locking of the Issue #1817 P1/P2 integration semantics;
- compact `(b,c,t,support,r)` state production and exact multiplicities;
- low-`qBC` tier production, beginning with K=8;
- full `qA` histogram convolution;
- exact 16-state Picard `mu` syndrome integration with `R=e-a-b-c`;
- bounded exact regression against retained direct/enumerated fixtures;
- FULL178 scaleout through the established eight `b` shards;
- compact deterministic certificates, source locks, population-conservation checks, shard coverage/disjointness, and predecessor comparison;
- a late-survivor handoff boundary to the already-retained 59D machinery.

BRIDGE V2 does **not** own:

- new MB mathematics or conductor/branch classification;
- reactivation of EX5 as a research lane or repair of obsolete EX5 population claims;
- ordinary 178 terminal-by-terminal enumeration, prefix/block pruning, or CUT work;
- generic GRF06/GRF07 mod-3/5/7 probing without a new source-locked odd-primary cokernel adapter;
- a global terminal-by-terminal 59D sweep;
- MAIN authority promotion/subtraction, claim-DAG mutation, theorem/effectivity/receiver/endpoint credit, final integration, or merge.

If a missing mathematical fact belongs to another active specialist lane, stop at an exact blocker or use a proper cross-lane demand. Do not silently rebuild producer-owned mathematics inside BRIDGE.

## Active route

1. **BR200 — charter reset.** Seal BR190 as historical/unconsumed and adopt Issue #1817 as the V2 research queue.
2. **BR201 — source-lock + compact-producer regression.** Freeze the current production-family/TD02/GRF04/Picard semantics. Reproduce the exact population identities required for `(b,c,t,support,r)`, low-qBC tiers and full qA. Small-H/bounded direct enumeration is allowed only as regression evidence.
3. **BR202 — P1 K=8 + full qA integration.** Construct the compact same-population capacity producer. Preserve support, exact `r`, K=8 `qBC` tiers and the full A-side `qA` histogram.
4. **BR203 — 16-state Picard `mu`.** Source-lock the 16-state syndrome/Cayley table, factor A/BC syndrome contributions, and apply `mu[sigma] <= e-a-b-c` inside the same producer.
5. **BR204 — FULL178 b-sharded scaleout.** Evaluate the integrated producer over exactly eight established `b` shards. Retain compact totals/certificates and deterministic stream hashes; discard raw state streams.
6. **BR205 — optional qBC escalation.** Increase tier depth or use a full qBC histogram only if BR204 quantifies material remaining slack. Do not pay the histogram cost merely because it exists.
7. **BR206 — late 59D handoff.** Use the existing 59D solver only on a source-locked late-survivor boundary if the remaining population is small enough to justify it.
8. **BR290 — retained hostile-audit handoff.** Freeze the exact candidate or blocker. Grant no MAIN credit.

## Transition, dominance, and salvage gates

Before every node transition after BR201, refresh the live MAIN authority and Issue #1817. Every retained candidate must record the live predecessor identity actually compared against, the exact same-population semantic adapter, and whether the candidate is a strict upper-bound improvement, equal, dominated, or semantically incomparable. Hard-coded Issue/charter numbers are regression anchors only and never substitute for the live predecessor.

If MAIN advances while BRIDGE is working, do not continue an expensive downstream step merely because an older scratch percentage looked attractive. Re-evaluate the candidate against the new live predecessor first. If the bridge candidate is dominated or the population semantics no longer match exactly, stop and record that status before further scaleout.

Valid intermediate work is salvageable. A BR202, BR203, or BR204 candidate may be frozen and handed to BR290 even when a deeper optional step blocks. Failure of Picard integration, qBC escalation, or the 59D handoff does not invalidate an already source-locked earlier same-population candidate.

BR203 has an explicit compactness gate. Before joining Picard `mu` into the P1 producer, measure the exact image cardinalities of the A-side and BC-side syndrome maps and the deduplicated free-exceptional syndrome/`mu` table used by the target tier. Testing whether `mu` factors through coarse group sums is useful but not required: failure of group-sum invariance is not a kill condition when the syndrome factors exactly across the existing A/BC split. Advance only if the syndrome join remains a finite compact-state augmentation and does not require terminal-identity materialization. If it causes genuine state explosion, freeze the BR202 candidate and stop/park BR203 with the measured blocker.

BR205's `material slack` gate is evidence-based, not discretionary. Escalation beyond K=8 is allowed only when BR204 retains exact slack attribution showing that qBC tier truncation is an active limiting relaxation on nonzero retained mass **and** a bounded same-population deeper-tier pilot gives strict improvement. Otherwise skip BR205.

BR206's `late survivors` gate is also evidence-based. The 59D solver may be invoked only after BRIDGE has an exact compact survivor boundary, an exact source-locked adapter from that boundary into the retained 59D model, a deduplicated survivor/work-item count, and a repository-policy-compliant workload/storage preflight. If any of those are missing, do not invoke 59D; freeze the best compact candidate instead.

## Compression / scale rules

The H=96 routing surface already has about 4.1M `(b,c,support,t,r)` states. This is moderate for streaming but is **not** permission to persist a 4.1M-row JSON artifact.

Use the established shard ranges:

```text
b=0..11
b=12..23
b=24..35
b=36..47
b=48..59
b=60..71
b=72..83
b=84..96
```

For each shard, stream exact states, evaluate/aggregate the bound, retain compact row/cell totals plus deterministic hashes/source locks, then discard the raw state stream. Final union verification must prove exact shard coverage, disjointness, and population conservation.

## Mathematical firewalls

- Same-population refinements are replacements/MIN bounds unless an exact disjoint incremental rejected identity set is produced.
- Never multiply savings or assume independence.
- Bounded/sample ratios must not be extrapolated into FULL178 authority.
- Issue #1817 scratch values are regression/research targets, not authority.
- The completion bit `r` is a state refinement, not a factor-two claim; predecessor TD02 already used a parity-max fallback.
- The Picard `mu` condition must be composed inside the same population producer, not applied as a raw-population percentage.
- Historical retained assets may be reused only with exact source locks and current semantic adapters.
- No MAIN/theorem/effectivity/receiver/endpoint/Perfect-Cuboid credit is granted by BRIDGE.

## Execution and audit

Ordinary startup authorizes light research/regression only. It does not authorize a new heavy or artifact-producing workflow. Any heavy FULL178 scaleout must obey repository storage/runkey/resume rules and its explicit authorization gate.

`stage32bridge-audit` is audit-only for a frozen exact retained BRIDGE boundary. It must verify exact source identities, population semantics, shard coverage/disjointness, deterministic replay, same-population replacement accounting, no double charging, and all credit firewalls. Audit PASS still grants no MAIN pruning credit without explicit MAIN consumption.

Do not merge without explicit user authorization.
