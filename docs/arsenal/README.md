# Research Arsenal

Reusable mathematical weapons and proof workflows live at stable historical paths; this directory is their canonical router. Do not load the whole Arsenal during ordinary Stage startup.

## Choose one entry point

| Need | Open |
|---|---|
| Find a current card by ID, role, maturity, or Stage | [`catalog.md`](catalog.md) |
| Read the machine-readable registry | [`index.json`](index.json) |
| Search Stage14, Toolbox, StructureRadar, or old route history | [`deep-source-index.md`](deep-source-index.md) |
| Check or regenerate the catalog after an edit | [`sync_arsenal_catalog.py`](sync_arsenal_catalog.py) |

`index.json` is the sole machine-readable Arsenal registry. `catalog.md` is generated from it. Stage promotion files remain at their existing paths so old certificates and handoffs keep working; they are source/provenance documents, not competing indexes.

## Maturity labels

- **FORMAL** — audited reusable result from a closed Stage. Its exact hypotheses and exclusions still apply.
- **PROVISIONAL** — discovery/source-routing aid only. Revalidate the current Stage controller and source locks before use.
- **WORKFLOW** — reusable proof or audit procedure, not a theorem/population selector.
- **HISTORICAL** — provenance and duplication/failure lookup, not current authority.
- **RETIRED** — old ID kept only as a route to its successor; never reuse the ID.

Authority order is: active Stage controller/source locks, formal audited card contract, provisional snapshot, historical navigation. In particular, the Stage32 and Stage33 promotion files are frozen provisional snapshots and never override live Stage state.

## Lookup rule

Identify the active leaf's exact missing object first. Then search the catalog and open only the matching card and its source locks. A match requires compatible object/population, field, cutoff, canonicalization, multiplicity, measure, quantifiers, and adapter hypotheses.

If no card matches, proceed to literature or new-theorem work. A finite certificate, adapter, family closure, or reproducibility PASS never grants receiver, theorem, route, or endpoint credit without the separately required audited implication. The repository-wide promotion policy remains authoritative: [`../research-os/policies/research-credit-and-promotion-firewalls.md`](../research-os/policies/research-credit-and-promotion-firewalls.md).

## Path policy

The large Stage14 Arsenal, stage-specific promotion files, Toolbox, and StructureRadar are intentionally not moved. New navigation belongs here; proof sources stay at their stable paths. Superseded compiled indexes remain under [`../archive/arsenal-index-history/`](../archive/arsenal-index-history/).
