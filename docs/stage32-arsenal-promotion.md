# Stage32 arsenal promotion — provisional consolidated harvest

```text
REGISTRY=STAGE32-ARSENAL-PROVISIONAL-R03-CONSOLIDATED
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage32
SOURCE_PR=1474
SOURCE_BRANCH=stage32-post1473-integral-picard-support-preflight
SOURCE_HEAD=77ede66e92a46b3365a4ee43a265728665a0b17a
BASE_HARVEST_SOURCE_HEAD=305da21597a8d61f64cd221b7efc8ca39833e3a8
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file is the consolidated Stage32 provisional Arsenal record. It supersedes the earlier split production-algorithm and proof-adapter sidecar layout. All cards remain candidate-discovery/source-routing aids only; active Stage32 source locks and controller state override them.

## Consolidation result

One same-object split was removed:

```text
S32-PW02 exact rank/unrank random access
  -> MERGED_INTO S32-PW01 exact compressed terminal-family interface
S32-PW02_RETIRED_ID=true
ID_REUSE_ALLOWED=false
```

Reason: the former PW01 exact symbolic count and PW02 rank/unrank/index access describe one certified terminal set, one predicate, and one compressed decomposition. The indexer is not an independent mathematical reduction without the PW01 count decomposition.

The remaining cards have different mathematical inputs/outputs and stay separate:

| Active card | Unique role |
|---|---|
| `S32-PW01` | exact symbolic terminal-family compression **plus** exact count/rank/unrank/random access |
| `S32-PW03` | high-rank lattice -> low-dimensional exact image/HNF gate |
| `S32-PW04` | affine lattice family -> finite fractional classes + safe exact quadratic lower bound |
| `S32-PW05` | exact finite-group orbit reconstruction of an invariant pairing/relation table |

```text
CARD_COUNT_BEFORE_CONSOLIDATION=5
CARD_COUNT_AFTER_CONSOLIDATION=4
MERGED_CARD_IDS=S32-PW02->S32-PW01
FORMAL_SELECTOR_CHANGES=0
STAGE32_MAINLINE_CHANGES=0
```

## S32-PW01 — exact compressed finite-family count and indexed access

**Type:** `EXACT_ENUMERATION_COMPRESSION_AND_INDEXER`

Source locks:

```text
count_path=stages/stage32/residual-32-01-production/compressed_terminal_family.py
count_blob_sha=90ff82ed312dcc0cb32cf207935945f550e29170
indexer_path=stages/stage32/residual-32-01-production/compressed_terminal_indexer.py
indexer_blob_sha=4fb0a8dd34909494bd62646373e42877ed7a3c9e
certified_e_range=0..729
```

The terminal predicate is counted by exact symbolic convolution instead of materializing the DFS leaves, and the same decomposition supplies deterministic global indexing with exact `rank`/`unrank` random access. The compressed ordering is source-controlled and need not preserve the legacy DFS stream order.

The locked Stage32 predicate includes

```text
x0 <= x1
x0=x1 => (x5,x6) <=lex (x8,x9)
x1+x8+x9+x10 = 0 mod 2
sum(exceptional xi) <= e
0 <= x4 <= 19*d-5*e
```

with exact stratum count

```text
stratum_terminal_count=(19*d-5*e+1)*exceptional_terminal_count(e).
```

Use when a finite structured family is too large to enumerate but admits a proved exact count decomposition and downstream work needs exact cardinality, deterministic random access, shard boundaries, or reproducible sampling by global index.

```text
HYPOTHESES=exact predicate match; proved count decomposition; rank/unrank set equality
APPLICABILITY=large exact finite families whose materialization is the bottleneck
DO_NOT_USE_FOR=changed filters/order semantics without a new proof; assuming legacy DFS order; sampled roundtrips as a substitute for global set-equality proof; theorem credit from finite count alone
```

## S32-PW03 — Picard lattice slice -> exact low-dimensional image bridge

**Type:** `LATTICE_ADAPTER`

```text
path=stages/stage32/residual-32-01-production/direct_picard_slice_bridge.py
blob_sha=be48bd94304d0217727c5c3368761d347cb22eaa
picard_rank=64
known_curve_count=140
```

Exact integral observables compress a high-rank lattice problem to a low-dimensional image. Column HNF turns target-image membership into fixed congruence tests before closest-vector work or terminal-family materialization.

```text
HYPOTHESES=exact integral observables; source-locked marking/Gram; exact image computation
APPLICABILITY=high-rank lattice searches with a small exact observable map whose image gate can be applied early
DO_NOT_USE_FOR=changed marking without an adapter; numerical row completion; theorem credit from image membership alone
```

The HNF prefix-membership subroutine inside `aut_equivariant_pairing_adapter.py` belongs here and is not another card.

## S32-PW04 — finite coset compression of integral quadratic loss

**Type:** `FINITE_LATTICE_QUOTIENT_BOUND`

```text
path=stages/stage32/residual-32-01-production/direct_picard_integral_coset_bound.py
blob_sha=9276a75e00970851f1d27b043492257ca5c1d3f1
smith_diagonal=[1,2,2]
generator_orders=[20,20,40]
reachable_class_count=640
```

After the exact slice reduction, affine integral optimization factors through finitely many reachable fractional shift classes. Exact Smith reduction and coordinate Cauchy--Schwarz bounds provide a rigorous classwise lower bound without a closest-vector search.

```text
HYPOTHESES=same exact quadratic kernel; same shift lattice; exact finite quotient/class reachability
APPLICABILITY=large affine lattice families sharing one quadratic kernel and finitely many fractional shift classes
DO_NOT_USE_FOR=treating the lower bound as an exact CVP solution; indefinite/wrong-sign quadratic forms; floating-only bounds; global theorem credit from finite pruning
```

## S32-PW05 — exact finite-group orbit reconstruction from seed data

**Type:** `FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION`

```text
path=stages/stage32/residual-32-01-production/aut_equivariant_pairing_adapter.py
blob_sha=08a7c76c5607e6feafae1c88b2befa3f1ebf9c89
supporting_path=stages/stage32/residual-32-01-production/pairing_prefix_engine.py
supporting_blob_sha=c8e87c6598fa1cd7ba1675fc35fa83bea983c94b
```

Given an exact finite action, an invariant pairing/relation, and seed values meeting every required ordered-pair orbit, propagate

```text
<a,b> = <g(a),g(b)>
```

and reconstruct the full finite table. The implementation fails closed on group-order regression, conflicting propagated values, incomplete orbit coverage, symmetry failure, or disagreement with the seed basis Gram.

Stage32's locked instance uses 140 labels, a rank-64 seed basis, group order 1536, and complete coverage of 19,600 ordered pairs; these numbers are provenance, not reusable constants.

```text
HYPOTHESES=proved exact finite action; proved invariance; complete required orbit coverage; locked labels; conflict/regression checks
APPLICABILITY=large exact finite relation tables generated from a much smaller seed region by symmetry
DO_NOT_USE_FOR=approximate symmetry; unverified action; incomplete orbit coverage; ignored conflicts; semantic/geometric identification merely from reconstructed algebra; theorem credit from table reconstruction alone
```

This is not PW03: PW03 decides image membership through HNF; PW05 reconstructs missing invariant values by orbit propagation.

## Workflow candidates retained after consolidation

### NUMERICAL_CANDIDATE_EXACT_REPLAY

```text
path=stages/stage32/residual-32-01-production/diagnose_stage32_post1473_integral_picard_support_milp_candidate_preflight.py
blob_sha=f249eaa0a1a03a301bae9e9f371713af5d57c41b
```

Reusable contract:

```text
numerical/heuristic solver -> candidate only
candidate -> exact source-locked replay
exact replay SAT -> same-layer certificate may advance
numerical timeout/infeasible/no-candidate -> UNKNOWN, never UNSAT
```

Do not accept rounded coordinates without exact replay and do not let same-layer exact replay silently become a stronger geometric/theorem claim.

### SOURCE_LOCKED_ADAPTER_WALL

```text
controller_path=stages/stage32/controller.json
controller_blob_sha=fe38433e7a57dfc1b642505f6fdfb6f293ddd58c
wall_path=stages/stage32/residual-32-01-production/post1473-specific-class-kc-adapter-wall.md
wall_blob_sha=03f07ef74986ac7aede6fc5ab462b41b71435561
```

Reusable contract:

```text
abstract theorem/quotient/equivalence exists
+ current source object is locked
- exact marked source->target adapter is materialized
=> BLOCKED_MISSING_EXACT_ADAPTER
```

Matching ranks, dimensions, fingerprints, group names, quotient names, or abstract isomorphism types do not substitute for the missing marked adapter.

### SEMANTIC_PROMOTION_FIREWALL / CANONICAL_EVIDENCE_CHAIN

The controller keeps distinct layers such as

```text
integral class
!= effective divisor
!= integral irreducible low-genus carrier
!= family closure
!= route/receiver/theorem/endpoint credit
```

and the replay pipeline pins semantic dependencies, rejects digest/schema regressions, performs exact replay, emits a canonical certificate, then keeps higher credit flags false until the next bridge is separately proved.

These are workflow/evidence patterns, not mathematical Arsenal cards.

## Duplicate check and non-promotion boundary

Checked overlaps after consolidation:

- former `PW02` duplicated the same exact terminal-family interface as `PW01` and is merged;
- PW03 HNF image reduction is not PW04 finite-coset quadratic reduction;
- PW03 HNF membership is not PW05 orbit reconstruction;
- PW04 finite quotient/bound is not PW05 group-orbit reconstruction;
- Stage32 PW05 is related to Stage33 equivariance auditing but reconstructs invariant values rather than testing a source-target intertwiner, so it is not a cross-stage duplicate.

Stage32-specific data remain non-promoted: the fixed `g1-d186` class, support-47 witness, concrete `K_c` pushforward test, `sigma_c`/`E_pi` locks, pending `P^2/2`, run/artifact IDs, witness hashes, and one-row production conclusions.

## Final provisional boundary

```text
PROVISIONAL_WEAPONS=S32-PW01,S32-PW03,S32-PW04,S32-PW05
RETIRED_MERGED_IDS=S32-PW02->S32-PW01
WORKFLOW_CANDIDATES=NUMERICAL_CANDIDATE_EXACT_REPLAY,SOURCE_LOCKED_ADAPTER_WALL,SEMANTIC_PROMOTION_FIREWALL,CANONICAL_EVIDENCE_CHAIN
STAGE32_SPECIFIC_DATA_PROMOTED=false
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
FINAL_PROMOTION_REVIEW_REQUIRED_AT_STAGE32_CLOSE=true
PERFECT_CUBOID_CONCLUSION=NONE
```
