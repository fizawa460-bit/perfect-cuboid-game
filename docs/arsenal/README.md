# Research arsenal

Status: **CURRENT ROUTER AFTER STAGE29 CLOSE**.

This is the compact entry point for reusable mathematical weapons. The weapon files themselves intentionally keep their long-standing paths in `docs/` so historical Stage links do not break. Historical progress/status documents are archived separately.

For the large historical corpora, use [`deep-source-index.md`](deep-source-index.md) instead of browsing Stage14 or StructureRadar blindly. It routes by task to the exact Arsenal, Toolbox, numerical, literature, external-gate, failed-route and promotion sources.

## When to consult Arsenal

Do **not** load the full Arsenal during ordinary Stage startup. First identify the active leaf's exact object and the kind of missing weapon: theorem, obstruction, adapter, finite reduction, exact-search compression, certificate pattern, or warning.

Before starting a fresh literature search or inventing a new mathematical route, query this router/index for that weapon shape and open only the matching card/source locks. A topic match is not enough: population/object, field, cutoff, canonicalization, multiplicity, measure, quantifiers and adapter hypotheses must match. If no card applies after that check, proceed to external literature/new-theorem work. If a new reusable weapon is proved and audited, feed it back through Arsenal promotion.

Machine-readable routing summary: [`index.json`](index.json).

## Current strongest selectors

Use a selector only after population, cutoff, canonicalization, multiplicity, measure and quantifier matching.

| Role | Current reusable source |
|---|---|
| `N2` whole-family upper | `AR-006`: `N2(B) << B^(1/2+o(1))` in [`../stage14-arsenal.md`](../stage14-arsenal.md) |
| `N2` lower construction | `S25-W01`: global/directional `N2,j(B) >>_j B^(1/4)` in [`../stage25-arsenal-promotion.md`](../stage25-arsenal-promotion.md) |
| `M3` lower | Stage28 final exact `liminf M3(B)/B^(1/3) >= 27/(40*pi^2)` |
| `M3` upper | `S26-W03`: `M3(B) <<_eta B(log B)^(5-eta)` for fixed `eta<1/46` |
| Stage19/20 common-host bridge | `S28-W01` |
| normalized interaction threshold | `S28-W02` |
| branch-profile differential | `S28-W03` |
| common-polarization fixed-curve differential | `S28-W04` |

## Provisional active-stage harvests

These are deliberately **not** current strongest selectors. They expose reusable candidates from still-open stages so later work can avoid re-inventing them, while forcing source revalidation before credit.

- [`../stage32-arsenal-promotion.md`](../stage32-arsenal-promotion.md) — provisional Stage32 exact-enumeration compression, rank/unrank, Picard slice/image, and finite integral-coset reduction cards.
- [`../stage33-arsenal-promotion.md`](../stage33-arsenal-promotion.md) — provisional Stage33 arithmetic-HS, finite-module/Bockstein, Picard-adjoint, source-target compatibility, and descent-warning cards.

Rules:

```text
PROVISIONAL_CARD_CAN_TRIGGER_SOURCE_LOOKUP=true
PROVISIONAL_CARD_IS_FORMAL_SELECTOR=false
PROVISIONAL_CARD_EARNS_THEOREM_CREDIT=false
ACTIVE_STAGE_SOURCE_LOCK_MUST_BE_REVALIDATED=true
FINAL_PROMOTION_REVIEW_REQUIRED_AT_STAGE_CLOSE=true
```

## Weapon sets kept at stable paths

- [`../stage14-arsenal.md`](../stage14-arsenal.md)
- [`../stage14-arsenal-index.md`](../stage14-arsenal-index.md)
- [`../stage14-num-reuse-index.md`](../stage14-num-reuse-index.md)
- [`../stage14-toolbox/`](../stage14-toolbox/)
- [`../structure-radar/`](../structure-radar/)
- [`../stage20-arsenal.md`](../stage20-arsenal.md)
- [`../stage21-arsenal.md`](../stage21-arsenal.md)
- [`../stage22-arsenal-promotion.md`](../stage22-arsenal-promotion.md)
- [`../stage23-arsenal-promotion.md`](../stage23-arsenal-promotion.md)
- [`../stage24-arsenal-promotion.md`](../stage24-arsenal-promotion.md)
- [`../stage25-arsenal-promotion.md`](../stage25-arsenal-promotion.md)
- [`../stage26-arsenal-promotion.md`](../stage26-arsenal-promotion.md)
- [`../stage28-arsenal-promotion.md`](../stage28-arsenal-promotion.md)

The Stage14/15 bound-attack ledger/map/coverage/queues are also retained as Arsenal provenance because they are useful for duplication and failed-route checks. Use [`deep-source-index.md`](deep-source-index.md) for the recommended lookup order.

## Stage29 endpoint frontier

Stage29 closed the synthesis phase and compressed remaining work to 13 active kernels. These are research receivers/frontier, not automatically theorem weapons.

- [`../../stages/stage29/29-17/final-handoff.json`](../../stages/stage29/29-17/final-handoff.json)
- [`../../stages/stage29/29-17/result.md`](../../stages/stage29/29-17/result.md)

Future endpoint work should choose one of these kernels and descend its dependency DAG rather than replaying the old 46-entry triage.

## Superseded compiled indexes

The former `research-arsenal-index.md/json` stopped at Stage26 and are archived under `../archive/arsenal-index-history/`. They are provenance only; this file is the current router.

The Stage27 promotion candidate is also archived because its file header remained `PENDING_STAGE27_70_AUDIT`; later stages consumed the audited Stage27 results, so that stale header must not masquerade as current weapon state.

## Firewalls

- Alternative proofs of the same completion condition are not independent probabilities.
- Do not multiply sieve, thin-cover, squareclass and global bounds merely because they use different coordinates.
- A family closure does not close the endpoint.
- A finite census does not prove global nonexistence.
- Historical Stage29 `GREEN` means certified route-level progress, not a solved endpoint.
- Provisional Stage32/33 cards are discovery aids until final promotion review; they never override their active Stage controllers/source locks.
