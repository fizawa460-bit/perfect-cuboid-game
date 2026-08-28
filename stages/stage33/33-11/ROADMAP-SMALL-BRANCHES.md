# Stage33-11 small-branch roadmap

Status: roadmap-only planning document. This file does not promote exact credit, change controller state, close Stage33-11, release Stage33-08/33-12, or make theorem/endpoint claims.

## Goal

Finish Stage33-11 = `ARITHMETIC-LOCALIZATION-CONNECTING-MAP` without continuing to grow one oversized PR/workflow. The target is unchanged: materialize and hostile-audit the genuine arithmetic localization connecting map on all 26 source directions, with exact accounting and no working-convention pins left in the promoted proof path.

Final Stage33-11 exit target:

- genuine connecting columns: exact/audited `26/26`;
- every promoted column supported by actual height-one-prime residue data and verified Galois transport;
- no unresolved `Q-defined/V4-compatible` purity pin used as proof;
- arithmetic localization connecting map declared computed only after hostile audit;
- Stage33-07/33-08/theorem/endpoint firewalls remain closed until their own downstream exit conditions are independently met;
- Stage33-12 remains reserved for its existing summary/connection role and is not consumed by this continuation.

## Starting boundary

The active PR #1449 remains the current MAIN evidence boundary. Its final workflow result and audit verdict determine the exact handoff into the branches below. This roadmap intentionally does not assume that pending workflow output passes or that any working column is promotable before audit.

Known MAIN structure to preserve if confirmed by the handoff:

- 26/26 MAIN-working map exists but is non-authoritative;
- 14 working generators cover the cyclic source blocks/orbits;
- exceptional-local valuation evidence has been materialized for those generators;
- strict-transform work has been reduced to a finite normalized carrier inventory;
- geometric symmetry/orbit reduction should be used before individual carrier factorization;
- exact Stage33-11 progress remains whatever the hostile audit explicitly certifies, not whatever MAIN working state suggests.

## Continuation branches

### 33-11d — CARRIER-PRIME-REFINEMENT

Purpose: replace carrier-level purity conventions with actual height-one-prime data.

Work:

1. consume the audited #1449 handoff only;
2. partition unresolved normalized carriers by already certified `cc/ct` and geometric symmetry;
3. factor/refine one representative per required orbit on the Testa–Stoll surface;
4. record reduced supports and scheme-theoretic multiplicities separately;
5. transport factorizations only through exact certified automorphisms;
6. leave any irreducibility/primary-decomposition uncertainty explicit rather than promoting it by convention.

Exit condition:

- every carrier used by the 14 working generators has an exact height-one-prime refinement, or the remaining unresolved set is finite and explicitly named;
- if unresolved primes remain, 33-11d does not close and the obstruction is carried forward without exact promotion.

Preferred PR size: one coherent prime-refinement PR. Split only if the factorization computation itself produces a genuinely separate mathematical obstruction.

### 33-11e — PRIME-LEVEL-GALOIS-TRANSPORT

Purpose: prove that the carrier-level Galois cancellation survives after refinement to actual height-one primes.

Work:

1. rebuild each relevant divisor package in the refined prime basis;
2. verify exact `cc` and `ct` action on each prime, including nontrivial splitting/permutation;
3. verify the certified geometric swaps/sign actions where they are used for transport;
4. compute `g(D)-D` at prime level for each of the 14 working generators;
5. remove every remaining `Q-defined/V4-compatible pending audit` pin from the proof path.

Exit condition:

- exact prime-level Galois transport is known for all working-generator divisor packages;
- each generator has an exact zero difference or an explicit nonzero/residual obstruction;
- no carrier-only equality is treated as a substitute for prime-level equality.

### 33-11f — 26-COLUMN-EXACT-CLOSURE

Purpose: turn the generator/orbit result into the genuine connecting map on all 26 named source directions.

Work:

1. transport exact generator results through the already certified cyclic source blocks/orbits;
2. materialize all 26 named connecting columns explicitly;
3. preserve the exact Stage33-10 absolute-H1 receiver and its inflation/restriction semantics;
4. compare every transported column against the named source basis and target coordinates;
5. generate a compact deterministic `26/26` certificate with source locks and per-column provenance;
6. distinguish `ZERO`, `NONZERO`, and `UNRESOLVED` exactly; never coerce unresolved columns to zero.

Exit condition:

- all 26 named columns are exact and explicit;
- `UNRESOLVED = 0`;
- the complete connecting matrix/map is reproducible from locked inputs;
- MAIN working and exact/audited counts are no longer conflated.

### 33-11g — HOSTILE-AUDIT-AND-STAGE33-11-EXIT

Purpose: close Stage33-11 itself, not merely finish MAIN implementation.

Work:

1. independently replay source locks and representative/orbit transport;
2. independently verify the prime refinements used by 33-11d;
3. independently verify prime-level `cc/ct` transport from 33-11e;
4. independently regenerate/check all 26 columns from 33-11f;
5. verify that no discarded working pin or stale carrier-level shortcut entered the exact path;
6. verify exact/audited progress and all firewalls before controller promotion.

Stage33-11 closes only if all of the following hold:

- `connecting_columns_exact_audited = 26/26`;
- `unresolved_connecting_columns = 0`;
- every promoted column has prime-level provenance;
- hostile audit verdict = PASS;
- arithmetic-localization connecting map = computed exact;
- no theorem/endpoint credit is inferred merely from this closure;
- Stage33-07 closure and Stage33-08 release are evaluated only by their own downstream conditions;
- Stage33-12 is still available for its original summary/connection task.

If audit fails, repair stays inside the smallest responsible 33-11d/e/f branch rather than reopening the whole chain.

## Branching rule

The labels `33-11d` through `33-11g` are logical small branches, not a command to create all PRs immediately. Create the next PR only after the previous branch has a stable audited handoff. A branch may collapse into its neighbor if the work is trivial, or split once if it develops a genuinely independent obstruction. Do not manufacture extra suffixes merely to hit a predetermined count.

## Workflow rule

Each continuation PR should trigger only its own narrow Stage33-11 path. Avoid broad `stages/stage33/**` triggers where possible. Controller-only/doc-only writes must not authorize expensive reruns. Heavy computation, if needed, gets a dedicated runkey/path gate. Audit PRs should replay only the evidence needed for that branch rather than rebuilding unrelated Stage33-07/09/10 history.

## Promotion firewall

Throughout 33-11d/e/f MAIN:

- exact/audited progress and MAIN working progress remain separate;
- Stage33-12 release = false;
- Stage33-08 release = false;
- Stage33-07 closed = false unless independently proven later;
- theorem credit = false;
- endpoint credit = false;
- perfect-cuboid existence/nonexistence claim = false.

Only 33-11g hostile audit may promote Stage33-11 to exact closure, and only from exact evidence produced by the preceding branches.
