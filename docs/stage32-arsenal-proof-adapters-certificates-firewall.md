# Stage32 Arsenal provisional harvest — proof adapters, certificates, source locks, and numerical→theorem firewalls

```text
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage32
SOURCE_PR=1474
SOURCE_BRANCH=stage32-post1473-integral-picard-support-preflight
SOURCE_HEAD=77ede66e92a46b3365a4ee43a265728665a0b17a
ARSENAL_PR=1478
FORMAL_SELECTOR_CHANGED=false
STAGE32_MAINLINE_CHANGED=false
THEOREM_CREDIT=false
```

This is a targeted catch-up harvest. It was reverse-indexed from the current Stage32 controller and the directly named current wall/replay sources; it is not a sequential reread of Stage32 history. Scope is limited to proof adapters, certificates, source locks, numerical→theorem firewalls, and reusable exact-computation patterns not already captured in the first two Stage32 harvest passes.

## Disposition summary

| Classification | Candidate | Disposition |
|---|---|---|
| Arsenal candidate | `S32-PW05` exact finite-group orbit reconstruction of a bilinear pairing | **new provisional card** |
| Workflow candidate | `NUMERICAL_CANDIDATE_EXACT_REPLAY` | **new workflow candidate** |
| Workflow candidate | `SOURCE_LOCKED_ADAPTER_WALL` | **new workflow vocabulary; integrates existing research-credit firewall policy** |
| Workflow candidate | `SEMANTIC_PROMOTION_FIREWALL` | **workflow consolidation, not a mathematical card** |
| Duplicate / integrate | symbolic exact count, rank/unrank, HNF image reduction, finite-coset quadratic bound | already `S32-PW01..PW04`; no duplicate card |
| Duplicate / integrate | HNF prefix membership inside `aut_equivariant_pairing_adapter.py` | method-level overlap with `S32-PW03`; no duplicate card |
| Stage32-specific / non-promoted | fixed `g1-d186` support-47 witness, `K_c` pushforward test, concrete `sigma_c`/`E_pi` locks and numerical outputs | do not promote |

## 1. Arsenal candidate

### S32-PW05 — exact finite-group orbit reconstruction from seed pairing data

**Type:** `FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION`

Primary source lock:

```text
path=stages/stage32/residual-32-01-production/aut_equivariant_pairing_adapter.py
blob_sha=08a7c76c5607e6feafae1c88b2befa3f1ebf9c89
```

Supporting exact group/basis source:

```text
path=stages/stage32/residual-32-01-production/pairing_prefix_engine.py
blob_sha=c8e87c6598fa1cd7ba1675fc35fa83bea983c94b
```

The reusable mechanism is broader than the Stage32 Picard instance. Given:

1. an exact finite permutation group `G` on a finite labelled set;
2. an exact seed Gram/pairing matrix on a subset of labels;
3. a proof/source lock that every `g in G` preserves the pairing;
4. sufficient orbit coverage of ordered label pairs;

propagate each seed value by

```text
<a,b> = <g(a),g(b)>
```

and reconstruct the entire finite pairing table without separately evaluating every pair. The implementation fails closed if the group order regresses, an orbit assigns conflicting values, coverage is incomplete, symmetry fails, or the recovered basis submatrix differs from the seed Gram. It emits canonical digests for the reconstructed full pairing and its basis-column image.

Stage32 instance:

```text
label_count=140
seed_basis_rank=64
seed_pair_count=4096
exact_group_order=1536
required_covered_ordered_pairs=19600
coverage_complete=true
conflict_count=0
```

**Applicability.** Use when a large exact finite relation/pairing table is invariant under a source-locked finite group and a much smaller seed region meets every required orbit. This can turn an `O(n^2)` direct reconstruction problem into seed evaluation plus exact orbit propagation, while retaining a complete certificate.

**DO_NOT_USE_FOR.** Do not use if the group action is heuristic/approximate, if invariance of the target relation is not proved, if orbit coverage is incomplete, if labels are not locked across source and target coordinates, or if conflicting propagated values are ignored. Orbit propagation proves only the invariant finite table it reconstructs; it does not by itself identify geometric semantics or earn theorem/receiver/endpoint credit.

```text
ID=S32-PW05
STATUS=PROVISIONAL_ARSENAL_CANDIDATE
EXACT_FINITE_GROUP_REQUIRED=true
PAIRING_INVARIANCE_REQUIRED=true
COMPLETE_ORBIT_COVERAGE_REQUIRED=true
CONFLICTS_FAIL_CLOSED=true
BASIS_REGRESSION_REQUIRED=true
FORMAL_SELECTOR=false
THEOREM_CREDIT=false
```

### Dedup note for PW05

This is **not** a duplicate of `S32-PW03`. `S32-PW03` uses exact HNF to decide membership in the image of low-dimensional linear observables; `S32-PW05` reconstructs a whole invariant finite bilinear table from seed data and group orbits. The later HNF prefix-membership oracle in the same Python file is an `S32-PW03`-style subroutine and is not separately promoted.

It is also related to, but not a duplicate of, Stage33's `V4_EQUIVARIANT_TRANSPORT_AUDIT`: the Stage33 workflow checks source-target intertwining/relabeling compatibility, whereas `S32-PW05` uses a validated action to reconstruct missing invariant values by exhaustive orbit coverage.

## 2. Workflow candidates

### NUMERICAL_CANDIDATE_EXACT_REPLAY

Source lock:

```text
path=stages/stage32/residual-32-01-production/diagnose_stage32_post1473_integral_picard_support_milp_candidate_preflight.py
blob_sha=f249eaa0a1a03a301bae9e9f371713af5d57c41b
```

The numerical MILP backend is used only to propose an integer candidate. The candidate is then fixed coordinate-by-coordinate into the exact QF_LIA model, and `SAT` is accepted only after exact Z3 replay plus exact Picard reconstruction and all-140 pairing replay. Numerical infeasibility, timeout, or lack of a candidate is explicitly `UNKNOWN`, never `UNSAT`.

Reusable contract:

```text
fast/numerical/heuristic solver -> candidate only
candidate -> exact source-locked replay
exact replay SAT -> certificate may advance at the same semantic layer
numerical timeout/infeasible/no-candidate -> UNKNOWN
numerical backend alone -> never UNSAT/theorem credit
```

**Applicability.** Use when an exact discrete model is expensive to search but cheap enough to verify after fixing a candidate, including MILP→SMT, floating optimization→exact arithmetic replay, heuristic search→symbolic verification, or remote solver→local deterministic checker.

**DO_NOT_USE_FOR.** Do not accept rounded coordinates without exact replay; do not convert numerical infeasibility or timeout into a proof of emptiness; do not let successful replay at one model layer silently promote to a stronger geometric/theorem layer.

This is a Workflow candidate, not an Arsenal mathematical theorem/card, because its reusable content is proof engineering and evidence discipline rather than a domain-specific mathematical reduction.

### SOURCE_LOCKED_ADAPTER_WALL

Primary sources:

```text
path=stages/stage32/controller.json
blob_sha=fe38433e7a57dfc1b642505f6fdfb6f293ddd58c

path=stages/stage32/residual-32-01-production/post1473-specific-class-kc-adapter-wall.md
blob_sha=03f07ef74986ac7aede6fc5ab462b41b71435561
```

When a theorem or quotient construction exists abstractly but the exact source-to-target map needed for the current retained coordinates is missing, stop at an explicit adapter wall instead of treating conceptual equivalence as executable transfer. The Stage32 instance distinguishes geometric `S -> K_c`, discriminant-level `sigma_c`, and a full integral Picard64 action; it explicitly forbids substituting the finite Reynolds quotient for the geometric quotient.

Reusable contract:

```text
abstract theorem/quotient exists
+ current object is source-locked
- exact marked adapter is missing
=> BLOCKED_MISSING_EXACT_ADAPTER
not => exclusion
not => existence
not => theorem transfer
```

**Applicability.** Use whenever a proof crosses models, bases, quotients, coefficient systems, fields, coordinate conventions, or geometric/combinatorial representations and the transfer itself carries mathematical content.

**DO_NOT_USE_FOR.** Do not treat matching dimensions, ranks, fingerprints, group names, quotient names, or abstract isomorphism types as the missing adapter. Do not infer a result in the target model until the required marked map and its hypotheses are replayable.

This consolidates the repository's existing research-credit/promotion firewall discipline; it is not proposed as a new theorem card.

### SEMANTIC_PROMOTION_FIREWALL

Controller source lock:

```text
path=stages/stage32/controller.json
blob_sha=fe38433e7a57dfc1b642505f6fdfb6f293ddd58c
```

The current controller records a deliberately strict ladder:

```text
integral Picard class
!= effective divisor
!= integral irreducible low-genus curve
!= full-family geometric closure
!= route/receiver/theorem/endpoint credit
```

The same controller separately enforces:

```text
UNKNOWN != UNSAT
representative sample != FULL178 numerical credit
fixed-projection SAT != curve existence
missing K_c adapter != specific-class exclusion
```

The reusable idea is to make every semantic promotion an explicit edge with its own certificate/adapter, rather than allowing computational success to climb multiple layers implicitly.

**Applicability.** Any computation-heavy proof pipeline in which solver objects, algebraic classes, effective objects, geometric carriers, and final theorems are distinct semantic levels.

**DO_NOT_USE_FOR.** This firewall does not prove any bridge; it only prevents unsupported promotion. Each allowed edge still needs its own theorem, adapter, or exact replay.

## 3. Existing Arsenal overlap / no new card

The earlier Stage32 harvest already captures the requested large-computation reductions:

```text
S32-PW01  symbolic exact terminal-family count/compression
S32-PW02  exact rank/unrank/random access/sharding
S32-PW03  exact HNF image-membership / low-dimensional lattice reduction
S32-PW04  Smith/finite-coset compression + safe exact quadratic lower bound
```

No duplicate card is added for these. In particular:

- symbolic compression / exact count -> `S32-PW01`;
- rank / unrank / deterministic random access / shardability -> `S32-PW02`;
- enumeration reduction via exact linear observables/HNF -> `S32-PW03`;
- large-family affine lattice compression to finitely many fractional classes -> `S32-PW04`;
- the HNF prefix-membership portion of `aut_equivariant_pairing_adapter.py` -> integrate under `S32-PW03`, not `PW05`;
- canonical SHA/source pinning by itself -> workflow/evidence infrastructure, not a new mathematical weapon.

## 4. Stage32-specific, therefore non-promoted

The following are intentionally retained only as provenance/current-stage evidence:

- fixed target `g1-d186`, `(d,e,a,u,v)=(186,266,592,-44,32)`, `z=(-15,62,-44,26,32)`;
- the concrete support-47 witness, unique zero exceptional index, `C^2=758`, `K.C=186`, `h^0(O(C))>=294`, and arithmetic genus `473`;
- the specific Testa–Stoll `K_c` pushforward test for this class;
- the concrete seventh-sign `sigma_c` identification and Stage32 basis replay requirement;
- extraction of the concrete contracted exceptional set `E_pi` from retained node coordinates;
- the current `P^2/2` pending computation and all current Stage32 route statuses;
- concrete run IDs, artifact IDs, witness hashes, and one-row support conclusions except as source-lock provenance.

Reason: these are either tied to the cuboid-surface marking/current class or are unfinished proof obligations. They are not reusable mathematics at the abstraction level required for an Arsenal card.

## 5. Source-lock / certificate pattern retained as workflow evidence

The V6 replay script pins upstream manifest, preflight, Picard-adapter, node-audit, affine-constraint-row, reduced-matrix, unimodular-transform, and source-lock digests before accepting a result; its output is then canonically hashed. This is a strong deterministic certificate-chain pattern, but it overlaps the repository-wide evidence/source-lock policy and is therefore not assigned another Arsenal card.

Use the pattern as:

```text
pin all semantic dependencies
-> reject any digest/schema regression
-> run candidate computation
-> exact replay
-> emit canonical machine-readable certificate
-> keep theorem-credit flags false unless the next semantic bridge is separately proved
```

## 6. Final provisional boundary

```text
NEW_ARSENAL_CANDIDATES=S32-PW05
NEW_WORKFLOW_CANDIDATES=NUMERICAL_CANDIDATE_EXACT_REPLAY,SOURCE_LOCKED_ADAPTER_WALL
WORKFLOW_CONSOLIDATION=SEMANTIC_PROMOTION_FIREWALL,CANONICAL_EVIDENCE_CHAIN
DUPLICATE_OR_INTEGRATE=S32-PW01,S32-PW02,S32-PW03,S32-PW04
STAGE32_SPECIFIC_DATA_PROMOTED=false
FORMAL_SELECTOR_CHANGED=false
STAGE32_MAINLINE_CHANGED=false
FINAL_PROMOTION_REVIEW_REQUIRED_AT_STAGE32_CLOSE=true
```

Nothing in this harvest proves existence or nonexistence of a perfect cuboid, closes Stage32, authorizes FULL178 heavy production, or overrides the active Stage32 controller/source locks.
