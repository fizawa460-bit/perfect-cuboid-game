# Stage32 arsenal promotion — provisional harvest

```text
REGISTRY=STAGE32-ARSENAL-PROVISIONAL-R01
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage32
SOURCE_PR=1474
SOURCE_BRANCH=stage32-post1473-integral-picard-support-preflight
SOURCE_HEAD=0de6dc6f5314f45dcebe1df46c022cfb08721360
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file harvests reusable Stage32 interfaces before Stage32 closes. These cards are valid for candidate discovery and exact-source lookup, but they are **not** active theorem selectors. Revalidate the named source locks and applicability conditions before reuse. At Stage32 close, rerun promotion review and either activate, revise, or retire each card.

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
FINITE_COSET_REDUCTION=true
CLOSEST_VECTOR_SEARCH_REQUIRED=false
BOUND_IS_SAFE_LOWER_BOUND_NOT_EXACT_CVP=true
REQUIRES_SAME_QUADRATIC_KERNEL_AND_SHIFT_LATTICE=true
FINITE_PRUNE_IS_NOT_GLOBAL_THEOREM=true
```

## Promotion firewalls

- These are **provisional cards from an active Stage**. They are not in `docs/arsenal/index.json.selectors`.
- Reuse requires source-lock and hypothesis matching; matching only the broad topic is insufficient.
- `S32-PW01/PW02` preserve a specific finite predicate, not arbitrary DFS searches.
- `S32-PW03/PW04` are exact only for a matching retained lattice/marking interface or an explicitly proved adapter.
- No bounded count, SAT/UNSAT result, finite quotient, or representative row earns theorem/receiver/endpoint credit by itself.
- Stage32 closure may revise or retire these cards.

```text
PROVISIONAL_WEAPONS=S32-PW01,S32-PW02,S32-PW03,S32-PW04
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```
