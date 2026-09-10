# Stage32 Harvest 4 registration planning

Status: **PLAN COMPLETE / REGISTRATION NOT PERFORMED**.

This file plans the stable-ID layout and registration sequence after `stage32-harvest4-hostile-dedup.{json,md}`. It does not edit `docs/arsenal/index.json`, generated cards, or Stage32 mathematical authority.

## Planned ID layout

Existing Stage32 active weapons are `S32-PW01`, `S32-PW03`, `S32-PW04`, `S32-PW05`, `S32-PW06`. `S32-PW02` is retired into `S32-PW01` and is permanently unavailable for reuse. Stage32 currently has no stable `S32-WFxx` IDs.

| Harvest 4 unit | Planned ID | Role | Plan state |
|---|---|---|---|
| `ABS-S32-H4-01` | `S32-PW07` | `SUPPORT_MASS_CAP_NECESSARY_PRUNER` | ready after exact source-lock revalidation |
| `ABS-S32-H4-08` | `S32-PW08` | `FINITE_STABILIZER_CAPACITY_PARITY_ELIMINATOR` | ready after exact source-lock revalidation |
| `ABS-S32-H4-09` | `S32-PW09` | `NORMALIZATION_CONDUCTOR_EVEN_CORRECTION_COUPLER` | ready after exact source-lock revalidation |
| `ABS-S32-H4-10` | `S32-PW10` | `CELLULAR_SMITH_COKERNEL_ASSEMBLY_OBSTRUCTION` | ready after exact source-lock revalidation |
| `ABS-S32-H4-13` | `S32-PW11` | `WEIGHTED_LOCAL_DEBT_AND_FACTORWISE_RAMIFICATION_SPLIT` | provisional-ready after source-lock revalidation |
| `ABS-S32-H4-CF21` | `S32-PW12` | `SOURCE_BOUND_ORBIT_CHARACTER_WITH_ABSOLUTE_MARKING_FIREWALL` | ready; hostile PASS 5123545511 must remain pinned |
| `ABS-S32-H4-18` | `S32-PW13` | `VALUATION_SEPARATED_SECTION_LOWER_BOUND_CERTIFIER` | **HOLD / not active** until source retention + hostile audit |
| `ABS-S32-H4-07` | `S32-WF01` | `SYMBOLIC_FREE_AXIS_EXACT_UNSAT_BLOCK_PARTITION` | ready after exact source-lock revalidation |
| `ABS-S32-H4-15` | `S32-WF02` | `CANONICAL_GEOMETRIC_IDENTITY_RECONSTRUCTION_STACK` | ready after exact source-lock revalidation |

The `PW12/PW13` ordering is deliberate: the audited source-bound orbit-character interface is in the first registration wave, while the closed-unmerged section-lower-bound source is held behind `PW13`. This avoids activating a gap only because one candidate still lacks registration-grade provenance.

Planned IDs are not stable assignments until they are actually inserted into the canonical machine registry.

## Existing-card extensions

`ABS-S32-H4-02 -> S32-PW01` is ready after source-lock revalidation. It adds survivor-space rank/unrank while preserving the original canonical completeness rank and reversible bridge.

`ABS-S32-H4-06 -> S32-PW03` is **held** until the required N260/N280 audit dependencies are satisfied. Its retained content is the exact functional-augmentation/dependence ladder around the existing HNF image gate.

`ABS-S32-H4-12 -> S30-W01 / S30-WF01` is **held** until the mixed audited/scratch source is revalidated. If later accepted, Stage32 records only a provisional extension/relation. The closed Stage30 formal source contract must not be rewritten by an active Stage32 harvest.

## First registration wave

If all per-unit source locks revalidate at the frozen source boundary, the first implementation wave may activate:

```text
weapons:
S32-PW01
S32-PW03
S32-PW04
S32-PW05
S32-PW06
S32-PW07
S32-PW08
S32-PW09
S32-PW10
S32-PW11
S32-PW12

workflows:
S32-WF01
S32-WF02

retired:
S32-PW02 -> S32-PW01
```

That yields **11 active Stage32 weapons + 2 active Stage32 workflows = 13 active Stage32 Arsenal entries**. `S32-PW13` remains absent from `active_cards` until its hold is independently cleared. If it is later activated, Stage32 reaches 12 weapons + 2 workflows = 14 active entries.

## Registration implementation order

1. Re-fetch PR #1755 and verify the Harvest 4 frozen range has not expanded.
2. Revalidate each ready candidate against its exact frozen head, source path/blob, and hostile-audit receipt where one is claimed. Do not manufacture missing source paths from names.
3. Append Harvest 4 sections to `docs/stage32-arsenal-promotion.md`. Every new active ID needs exactly one matching heading so the generator can snapshot the exact source contract.
4. Put the H4-02 extension inside the existing `S32-PW01` source section; do not create a duplicate `## S32-PW01` heading.
5. Leave H4-06 and H4-12 as held registration-plan metadata until their gates clear.
6. Update only the Stage32 provisional-harvest registry entry and related relation/provenance metadata in `docs/arsenal/index.json`.
7. Preserve `S32-PW02 -> S32-PW01` exactly.
8. Run `docs/arsenal/sync_arsenal_catalog.py` to regenerate `catalog.md` and individual cards. Generated files are never hand-edited.
9. Run the generator in check mode and hostile-audit registry/source/generated consistency before any merge decision.

## Hostile registration checks

Registration must fail closed if any new card lacks exact source identity, if a held unit appears in `active_cards`, if a generated card widens the hostile-dedup quantifiers, if `S32-PW02` is reused, or if Stage32 provisional material mutates closed Stage30 formal semantics.

The card-level outputs remain exactly bounded: finite necessary pruning is not theorem credit; finite stabilizer forcing is not global existence; conductor/ramification coupling is necessary only; Smith cokernel classification is finite assembly credit only; weighted debt accounting does not create a second no-recharge theorem; source-bound orbit character does not choose an absolute W-line; symbolic free-axis UNSAT remains local unless adapted; canonical identity reconstruction is infrastructure only.

## Held / nonregistered units

- `ABS-S32-H4-18 / planned S32-PW13`: source is `PROVISIONAL_CLOSED_UNMERGED`; retain and hostile-audit before activation.
- `ABS-S32-H4-CF20`: genuinely new but still blocked by missing hostile re-audit receipt; no ID is reserved for it.
- H4 duplicates `03,04,05,11,14,16,17,19`: remain nonregistered.

## Boundary

```text
REGISTRATION_PLAN_COMPLETE=true
INDEX_JSON_MODIFIED=false
GENERATED_CARDS_MODIFIED=false
STABLE_IDS_ASSIGNED=false
STAGE32_MATHEMATICAL_CREDIT_CHANGE=0
MERGE_AUTHORIZED=false
NEXT_PHASE=STAGE32_HARVEST4_REGISTRATION_IMPLEMENTATION_READY_WAVE
```
