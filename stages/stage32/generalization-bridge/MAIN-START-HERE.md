# Stage32 BRIDGE startup

This file is the authoritative startup/read-order contract for ordinary `stage32bridge-mainbatch`.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from live Stage32 MAIN authority;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. `stages/stage32/generalization-bridge/MISSION.json`;
6. `stages/stage32/generalization-bridge/STATE.json`, focusing on the current node, active leaf, next obligation, source-lane boundary, target-population boundary, and credit firewall;
7. only the exact source/evidence/interface paths required by the active leaf.

Do not preload MB history, FULL178 history, EX5 history, or unrelated Stage32 assets. Repository discovery remains search-first under root `AGENTS.md`.

Current `stages/stage32/MAIN-STATE.json` remains mathematical routing authority. `CROSS-LANE-DEMANDS.json` controls operational priority only. BRIDGE never self-promotes a source-lane result or a bridge result to MAIN credit.

## Mission

BRIDGE tests whether an exact retained structural result from another Stage32 lane can be transported into a **population-wide necessary condition** on the current authoritative FULL178/Picard64 population.

The initial seed is the MB104 line of ideas that exposes residual-character/Fourier and square-energy structure. The seed is not authority merely because it exists on an unmerged or unaudited sibling branch. Before using any source result, BRIDGE must freeze its exact identity, audit/retained status, hypotheses, semantic scope, and the exact implication it proposes to transport.

BRIDGE is specifically allowed to answer **NO GENERALIZATION**. A clean no-go result is preferred over silently weakening hypotheses or inventing a cross-lane identification.

## Ownership

BRIDGE owns only:

- source-locked semantic adapters from an exact retained source-lane statement to the current FULL178/Picard64 objects;
- proof that a proposed invariant/character/energy is well-defined for every target object in the claimed scope;
- minimization over hidden/free completion coordinates needed to turn a source-lane quantity into a target-visible lower bound or necessary condition;
- bounded diagnostics that estimate whether a proved target condition is materially useful before any scaleout;
- exact no-go certificates showing that source-specific hypotheses, free completions, or semantic mismatch destroy the proposed population-wide cut.

BRIDGE does **not** own:

- new 32-03 MB mathematics, conductor calculations, branch classification, or MB authority;
- construction/repair of EX5 Picard64 producer interfaces;
- 178 terminal enumeration, prefix/maxcut/block transport, or ordinary numerical-census research;
- CUT direct completion infeasibility;
- MAIN authority promotion, current-authority subtraction, claim-DAG mutation, final integration, or merge.

If the active bridge needs missing mathematics owned by MB, EX5, 178, CUT, or MAIN, stop at an exact blocker or create/use a proper cross-lane demand. Do not rebuild producer-owned mathematics inside BRIDGE.

## Initial route

The initial route is deliberately top-down and must not fall back to terminal-by-terminal research merely because a global adapter is difficult:

1. **BR101 — source/target semantic freeze.** Freeze the exact source-lane theorem/candidate and the exact current FULL178 target semantics. Identify which hypotheses are source-specific and which quantities are intrinsic enough to transport.
2. **BR102 — general character/invariant definition.** Determine whether the MB-style residual-character/Picard direction, or an equivalent invariant, is definable on general target Picard64 completions. If it is only meaningful on the `000707`, genus-one, span-five, balanced16, `e=2`, multibranch packet, record `NO_GENERALIZATION` for that formulation rather than erasing those hypotheses.
3. **BR103 — free-completion minimization.** Using the exact terminal-to-Picard64 interface, minimize the proposed character/energy over every allowed hidden/free completion coordinate and congruence. If the free coordinates can cancel the quantity completely on every terminal, freeze that as a no-go result. If a nontrivial lower bound survives, prove it with exact arithmetic.
4. **BR104 — bounded population diagnostic.** Apply only the proved target condition to a bounded representative FULL178 slice. Measure strict gain against the current audited baseline on identical population semantics. Bounded evidence remains noncredit and is not a theorem outside its certified scope.
5. **BR105 — full-population adapter candidate or no-go.** Only after BR102/BR103 prove a genuine target-wide condition may BRIDGE formulate a FULL178 adapter candidate. Scaleout is separate and must preserve current authority, overlap, and no-double-charge firewalls.
6. **BR190 — retained handoff.** Freeze either a useful exact generalization candidate, a precise no-go theorem for the attempted transport, or a source-lane blocker for hostile audit and later MAIN decision.

## Anti-loop / top-down rule

Do not respond to failure of BR102 or BR103 by descending into isolated terminal/block exclusions. BRIDGE exists to find or refute broad transferable structure. Local examples are permitted only to falsify a proposed universal adapter or to validate exact semantics.

Do not multiply a BRIDGE saving with HPADJ/CUT/EX5/178 savings until exact overlap/double-charge accounting is proved by the owning MAIN integration surface.

## Cross-lane routing

Inspect only demands involving lane `BRIDGE`. A higher-priority OPEN demand where BRIDGE is producer preempts lower-priority local work. If BRIDGE is consumer of an OPEN demand, wait rather than duplicate producer mathematics. For SATISFIED re-entry, validate exact artifact identity, source locks, and target-population semantics before use.

Demand status grants no mathematical credit. Source-lane PASS grants no BRIDGE transfer credit without the semantic adapter. BRIDGE hostile-audit PASS grants no MAIN pruning credit without explicit MAIN consumption.

## Execution and audit

Ordinary startup does not authorize heavy compute or artifact-producing scaleout. Any later heavy workflow must obey repository storage/runkey/resume rules and requires its own explicit authorization gate.

`stage32bridge-audit` is audit-only for a frozen exact retained BRIDGE boundary. It must verify source identity, target semantics, universal quantifiers, free-completion minimization, no-recharge, and all credit firewalls. It does not merge or self-promote.

Do not merge without explicit user authorization.
