# Stage32 arsenal promotion — provisional harvest

```text
REGISTRY=STAGE32-ARSENAL-PROVISIONAL-R02
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage32
SOURCE_PR=1474
SOURCE_BRANCH=stage32-post1473-integral-picard-support-preflight
BASE_HARVEST_SOURCE_HEAD=305da21597a8d61f64cd221b7efc8ca39833e3a8
PROOF_ADAPTER_SUPPLEMENT_SOURCE_HEAD=77ede66e92a46b3365a4ee43a265728665a0b17a
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file harvests reusable Stage32 interfaces before Stage32 closes. These cards are valid for candidate discovery and exact-source lookup, but they are **not** active theorem selectors. Revalidate the named source locks and applicability conditions before reuse. At Stage32 close, rerun promotion review and either activate, revise, or retire each card.

Targeted proof-adapter/certificate/firewall catch-up supplement: [`stage32-arsenal-proof-adapters-certificates-firewall.md`](stage32-arsenal-proof-adapters-certificates-firewall.md). It adds only `S32-PW05` as a new provisional mathematical card; numerical-candidate→exact-replay and source-locked adapter-wall patterns remain Workflow candidates rather than selectors/theorems.

## Current production-algorithm harvest disposition

The four locked source paths were revalidated at exact Stage32 source head `305da21597a8d61f64cd221b7efc8ca39833e3a8`; their blob SHAs below are unchanged at that head. This batch deliberately distinguishes reusable production algorithms from the Picard-side mathematical adapters that happened to live in the same production directory.

```text
PRODUCTION_ALGORITHM_BATCH=S32-PW01,S32-PW02
PARKED_OUTSIDE_THIS_ALGORITHM_BATCH=S32-PW03,S32-PW04
ALL_FOUR_BASE_CARDS_REMAIN_PROVISIONAL=true
PROOF_ADAPTER_SUPPLEMENT=S32-PW05
STAGE32_SELECTOR_OR_CONTROLLER_CHANGED=false
```

`S32-PW01/PW02` are retained as the current production-algorithm harvest because they implement exact symbolic compression and exact random access to the same certified finite terminal predicate. `S32-PW03/PW04` remain useful provisional Arsenal candidates, but are parked outside this narrower algorithm batch because they are Picard-lattice/finite-coset adapters tied to the current mathematical closure interface. Parking them here is not retirement or revocation. `S32-PW05` is a separate exact finite-group equivariant reconstruction card from the later proof-adapter catch-up pass.

## S32-PW01 — exact symbolic terminal-family compression

**Type:** `EXACT_ENUMERATION_COMPRESSION`

Source lock:

```text
path=stages/stage32/residual-32-01-production/compressed_terminal_family.py
blob_sha=90ff82ed312dcc0cb32cf207935945f550e29170
certified_e_range=0..729
```

The Stage32 terminal predicate on the 11 pairing-prefix values can be counted by exact symbolic convolution instead of visiting every DFS terminal. The current source preserves the exact filters

```text
x0 <= x1
x0=x1 => (x5,x6) <=lex (x8,x9)
x1+x8+x9+x10 = 0 mod 2
sum(exceptional xi) <= e
0 <= x4 <= 19*d-5*e
```

and computes

```text
stratum_terminal_count=(19*d-5*e+1)*exceptional_terminal_count(e).
```

Use when a later search has the **same combinatorial predicate** and exhaustive materialization is the bottleneck.

```text
ID=S32-PW01
CURRENT_BATCH_DISPOSITION=PROVISIONAL_PRODUCTION_ALGORITHM_CANDIDATE
REQUIRES_EXACT_PREDICATE_MATCH=true
REPLACES_DFS_MATERIALIZATION_WITH_EXACT_COUNT=true
CHANGING_VARIABLE_ORDER_OR_FILTERS_REQUIRES_NEW_PROOF=true
FINITE_COUNT_IS_NOT_THEOREM_CREDIT=true
```

## S32-PW02 — exact rank/unrank random access to a compressed family

**Type:** `EXACT_INDEXER`

Source lock:

```text
path=stages/stage32/residual-32-01-production/compressed_terminal_indexer.py
blob_sha=4fb0a8dd34909494bd62646373e42877ed7a3c9e
```

`CompressedTerminalIndexer` gives exact count/rank/unrank access to the same terminal set as `S32-PW01`, with a source-controlled compressed ordering. It explicitly does **not** preserve the legacy DFS stream order.

This is reusable when a mathematically exact finite family is too large to enumerate but downstream work needs deterministic random access, partitioning, sharding, or reproducible sampling by global index.

```text
ID=S32-PW02
CURRENT_BATCH_DISPOSITION=PROVISIONAL_PRODUCTION_ALGORITHM_CANDIDATE
SET_EQUAL_TO_TERMINAL_PREDICATE=true
LEGACY_DFS_ORDER_PRESERVED=false
EXACT_RANDOM_ACCESS=true
REQUIRES_S32_PW01_STYLE_COUNT_DECOMPOSITION=true
```

## S32-PW03 — Picard lattice slice -> exact low-dimensional image bridge

**Type:** `LATTICE_ADAPTER`

Source lock:

```text
path=stages/stage32/residual-32-01-production/direct_picard_slice_bridge.py
blob_sha=be48bd94304d0217727c5c3368761d347cb22eaa
picard_rank=64
known_curve_count=140
```

The retained Picard marking is converted into three exact integral functionals: degree, exceptional mass, and first normal-half mass. The map

```text
phi: Z^64 -> Z^3
```

has rank 3 and kernel rank 61. Its image is computed by column HNF, so the historical `tar in Image(phi)` gate becomes fixed congruence tests before any closest-vector or terminal-family materialization. The exact identity

```text
normal_total + 5*exceptional_total = 19*degree
```

is verified on the full retained Picard lattice.

Use when a high-rank integral lattice search has a small set of exact linear observables and the target-image test can be pushed ahead of expensive enumeration.

```text
ID=S32-PW03
CURRENT_BATCH_DISPOSITION=PARKED_OUTSIDE_PRODUCTION_ALGORITHM_BATCH
EXACT_HNF_IMAGE_GATE=true
TARGET_PARTITION_WITHOUT_TERMINAL_MATERIALIZATION=true
REQUIRES_RETAINED_MARKING_AND_GRAM_MATCH=true
NUMERICAL_ROW_COMPLETE=false
THEOREM_CREDIT=false
```

## S32-PW04 — finite coset compression of integral quadratic loss

**Type:** `FINITE_LATTICE_QUOTIENT_BOUND`

Source lock:

```text
path=stages/stage32/residual-32-01-production/direct_picard_integral_coset_bound.py
blob_sha=9276a75e00970851f1d27b043492257ca5c1d3f1
smith_diagonal=[1,2,2]
generator_orders=[20,20,40]
reachable_class_count=640
```

After the `S32-PW03` slice reduction, the integral shift only depends on 640 reachable fractional classes. Exact Smith decomposition and coordinate Cauchy--Schwarz bounds give a rigorous classwise lower bound on integrality loss without running a closest-vector search. In the locked Stage32 instance, 2,018,569 prior slices factor through these 640 classes.

Use when a family of affine lattice optimization problems shares one quadratic kernel and only finitely many fractional shift classes.

```text
ID=S32-PW04
CURRENT_BATCH_DISPOSITION=PARKED_OUTSIDE_PRODUCTION_ALGORITHM_BATCH
FINITE_COSET_REDUCTION=true
CLOSEST_VECTOR_SEARCH_REQUIRED=false
BOUND_IS_SAFE_LOWER_BOUND_NOT_EXACT_CVP=true
REQUIRES_SAME_QUADRATIC_KERNEL_AND_SHIFT_LATTICE=true
FINITE_PRUNE_IS_NOT_GLOBAL_THEOREM=true
```

## S32-PW05 — exact finite-group orbit reconstruction from seed pairing data

**Type:** `FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION`

The full contract, source locks, applicability, dedup boundary, and `DO_NOT_USE_FOR` rules are in [`stage32-arsenal-proof-adapters-certificates-firewall.md`](stage32-arsenal-proof-adapters-certificates-firewall.md).

```text
path=stages/stage32/residual-32-01-production/aut_equivariant_pairing_adapter.py
blob_sha=08a7c76c5607e6feafae1c88b2befa3f1ebf9c89
supporting_path=stages/stage32/residual-32-01-production/pairing_prefix_engine.py
supporting_blob_sha=c8e87c6598fa1cd7ba1675fc35fa83bea983c94b
```

A source-locked exact finite group transports a small seed Gram/pairing table across all ordered-pair orbits. Conflicts, incomplete coverage, group-order regression, symmetry failure, or basis regression fail closed. This is a whole-table equivariant reconstruction method, not the HNF image-membership method of `S32-PW03`.

## Promotion firewalls

- These are **provisional cards from an active Stage**. They are not in `docs/arsenal/index.json.selectors`.
- Reuse requires source-lock and hypothesis matching; matching only the broad topic is insufficient.
- `S32-PW01/PW02` preserve a specific finite predicate, not arbitrary DFS searches.
- `S32-PW03/PW04` are exact only for a matching retained lattice/marking interface or an explicitly proved adapter.
- `S32-PW05` requires a proved exact finite action, invariance, complete orbit coverage, and fail-closed conflict/regression checks.
- Numerical candidate search never earns `UNSAT`; candidate success must be replayed exactly before even same-layer certificate promotion.
- Computational success at one semantic layer does not silently promote through Picard/effectivity/irreducibility/geometric/theorem layers.
- `PARKED_OUTSIDE_PRODUCTION_ALGORITHM_BATCH` is only a batch-scope classification; it is not retirement, revocation, or theorem-status change.
- No bounded count, SAT/UNSAT result, finite quotient, representative row, or reconstructed finite table earns theorem/receiver/endpoint credit by itself.
- Stage32 closure may revise or retire these cards.

```text
PROVISIONAL_WEAPONS=S32-PW01,S32-PW02,S32-PW03,S32-PW04,S32-PW05
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```