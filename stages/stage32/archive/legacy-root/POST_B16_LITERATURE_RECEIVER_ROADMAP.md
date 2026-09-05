# Stage32 post-b16 literature-receiver reduction roadmap

Status: PLANNED_HIGHEST_PRIORITY_AFTER_D16_B16_CALIBRATION_CLOSE

## Purpose

Before Stage32 commits to brute-force production across the frozen 183 unibranch `(genus, degree)` windows, convert the four identified literature routes into exact Stage32 receivers and hostile-audit their applicability.

The objective is not merely to collect references. The objective is to produce an exact **183-window theorem mask** answering:

- which windows are completely discharged by a published theorem/classification;
- which windows are only reduced to a strict special locus or subpopulation;
- which windows are covered only under an extra local hypothesis such as smoothness at a node;
- which windows remain untouched and still require exact enumeration;
- how many full rows and how much within-row population remain after all non-overlapping literature reductions are applied.

This audit is the highest-priority Stage32-main item immediately after the d16/b16 calibration route is closed and audited. It runs **before** the frozen-census feasibility gate and before arming a large 183-window production campaign.

## Four literature receiver families

The following are discovery targets, not pre-authorized theorem credit. Each must be independently source-locked to a stable paper/thesis locator and exact theorem/proposition statement before use.

### LIT32-FSM — Freitag--Salvati Manni box-variety low-genus bound

Target source family: `Parametrization of the box variety by theta functions` and the exact result underlying the inherited `d <= 176 / d <= 192` unibranch finite window.

Audit tasks:
- lock the exact theorem statement and hypotheses;
- identify the precise meaning of irreducible/integral curve, normalization, bijectivity/unibranch assumptions, degree and genus;
- recover exactly how the constants 176 and 192 arise;
- determine whether any hypothesis-sensitive refinement can reduce the frozen window rather than merely reproduce its existing boundary.

### LIT32-GF — García-Fritz / García-Fritz--Urzúa nodal-surface degree and symmetric-differential bounds

Target source family: the sharper low-genus degree bounds and local-node/symmetric-differential constraints discussed for the cuboid/box surface or the relevant nodal-surface framework.

Audit tasks:
- lock exact theorem statements and all local singularity hypotheses;
- distinguish `curve smooth at a surface node` from `unibranch but singular at that node`;
- translate node incidence, exceptional intersections and local multiplicities into the Stage32 Picard/intersection data;
- determine whether a bound such as the reported smooth-at-node `d <= 4g + 44` form is actually applicable to a certified Stage32 subpopulation;
- never delete an entire `(g,d)` row when only a proper local-hypothesis subpopulation is covered.

### LIT32-BTVA — Bruin--Thomas--Várilly-Alvarado symmetric-differential special-locus constraints

Target source: `Explicit computation of symmetric differentials and its application to quasihyperbolicity` and any source-locked companion material/code needed to reproduce the cuboid-surface statements.

Audit tasks:
- lock exact rational/genus-one node-incidence statements and their exceptional known-curve clauses;
- identify the explicit special locus cut out by the symmetric differentials, when available;
- map `number of nodes passed through`, exceptional-divisor intersections and known-curve exclusions to Stage32 candidate data;
- decide whether low-node candidates can be removed, classified, or reduced to a finite explicit locus before lattice enumeration.

### LIT32-TS — Testa--Stoll low-degree classification and K3/Aut compression

Target source family: `Curves on the surface of cuboids`, its verified computational data/code, and the Picard/K3 quotient classification machinery already upstream of Stage32.

Audit tasks:
- lock the exact degree range and classification statement;
- identify which degree/genus rows are already completely classified;
- recover the K3 quotient, Picard-lattice and automorphism-orbit compression used in the proof;
- determine which parts are theorem-level reusable adapters for degree above the published classification range, without extrapolating a bounded classification into an unproved general theorem.

## Required exact output

Create a machine-readable `STAGE32_POST_B16_LITERATURE_RECEIVER_AUDIT_V1` certificate with all 183 frozen rows represented explicitly.

For each row `(g,d)`, record one of:

- `FULLY_DISCHARGED_BY_SOURCE_LOCKED_THEOREM`
- `FULLY_CLASSIFIED_BY_SOURCE_LOCKED_RESULT`
- `REDUCED_TO_EXPLICIT_SPECIAL_LOCUS`
- `REDUCED_ONLY_FOR_CERTIFIED_SUBPOPULATION`
- `NO_APPLICABLE_LITERATURE_REDUCTION`
- `UNKNOWN_APPLICABILITY`

Each nontrivial reduction must include:
- source identifier and stable locator;
- theorem/proposition/lemma locator;
- exact hypotheses;
- Stage32 variable dictionary;
- proof that the Stage32 population satisfies those hypotheses;
- overlap accounting so the same restriction is not double-counted;
- residual population definition after the reduction.

The aggregate certificate must report:
- `initial_window_count = 183`;
- number of entire rows fully discharged/classified;
- number of rows partially reduced;
- number of unchanged rows;
- exact residual row list;
- any finer residual subpopulation masks;
- a revised production/feasibility target built from the residual population only.

## Ordering and stop rule

After d16/b16 calibration closes and its evidence is audited:

1. run this literature receiverization and exact applicability audit;
2. hostile-audit the 183-window theorem mask;
3. only then run the post-b16 feasibility gate against the **residual** frozen-census population;
4. only after a feasible residual plan exists may a large full-window production campaign be armed.

If the literature audit finds a credible theorem that could remove a large part of the target but whose applicability adapter is unresolved, stop and solve that bounded adapter before spending comparable resources on brute-force enumeration.

This priority does not block the independent `32-03` multibranch ledger from running in parallel when safe under the existing Stage32 dependency DAG.

## Firewalls

Planning, source discovery, or a plausible paper match alone grants no theorem/receiver/numerical credit. Until exact receiver audit passes:

```text
POST_B16_LITERATURE_RECEIVER_AUDIT_COMPLETE=false
LITERATURE_REDUCED_WINDOW_MASK_AUDITED=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
STAGE32_CLOSED=false
```
