# Stage29 — foundation synthesis, multi-route endpoint attack, and perfect-cuboid routing

```text
STAGE=Stage29
ROADMAP_REVISION=R2_POST_29_02_FOUNDATION_SCREEN
ROLE=FOUNDATION_SYNTHESIS_PLUS_MULTI_ROUTE_ENDPOINT_ATTACK_PLUS_ROUTING
NUMBERING=INCREMENTAL_01_02_03...
LEGACY_10_70_SEQUENCE_USED=false
PERFECT_CUBOID_ENDPOINT_ITSELF_DEFERRED=true
STAGE28_FINAL_STATUS=CLOSED_AUDITED_PASS_MERGED
STAGE29_02_STATUS=AUDITED_SCREENING_COMPLETE
```

Stage29 began as a search for materially different foundations beyond Stage16–28. That search produced substantially more global structure than the original roadmap assumed: the full endpoint surface, the joint V4 completion model, Beauville/modular/L-function/Brauer routes, the full seven-line degree-64 sign/Kummer cover, classical Campedelli quotients, and the non-Fano/Hirzebruch recognition adapter over `Q(i)` with an explicit `Q` twist.

Therefore the post-29-02 roadmap no longer assumes that 29-06/07 must discover the global or joint models from scratch. The remaining job is to place the population program and all audited endpoint models into one exact dependency map, attack several serious routes in parallel, and only compress/rank them when evidence justifies doing so.

## Core operating policy

### 1. Living roadmap

The roadmap is intentionally revisable.

```text
ROADMAP_IS_LIVING=true
MATERIAL_NEW_FOUNDATION_CAN_TRIGGER_ROADMAP_REVIEW=true
MATERIAL_NEW_EQUIVALENCE_CAN_TRIGGER_ROADMAP_REVIEW=true
MATERIAL_NEW_OBSTRUCTION_CAN_TRIGGER_ROADMAP_REVIEW=true
MATERIAL_BACKFLOW_CAN_TRIGGER_ROADMAP_REVIEW=true
COSMETIC_RESULT_DOES_NOT_TRIGGER_ROADMAP_REWRITE=true
```

A roadmap review is mandatory when a new result changes the identity of the main endpoint object, proves that previously separate routes are the same mechanism, opens a materially stronger obstruction/descent route, or makes a planned stage redundant. Small receiver closures do not by themselves trigger a rewrite.

All named gap scans double as formal roadmap-review checkpoints.

### 2. Multi-route attack, not premature single-route selection

Stage29 will not force an early choice of one primary route.

```text
PREMATURE_SINGLE_ROUTE_SELECTION=false
MULTI_ROUTE_ATTACK_ALLOWED=true
PARALLEL_ROUTE_PORTFOLIO_DEFAULT=true
ROUTE_PRUNING_REQUIRES_EVIDENCE=true
FINAL_COMPRESSION_AT_29_16=true
```

If several endpoint routes remain genuinely different and viable, Stage29 should attack all of them far enough to determine what each can and cannot prove. A route may be retired only for a mathematical reason: exact redundancy, insufficient coverage, a red theorem trigger, an impossible field-of-definition requirement, or a strictly dominated receiver.

### 3. Backflow and anti-loop rule

Old frozen gaps are not automatically reopened. Backflow to Stage16–28 is allowed only through a new exact receiver created by the audited Stage29 foundations.

```text
REPLAY_OLD_FROZEN_GATE_WITHOUT_NEW_INPUT=false
NEW_LENS_CAN_TRIGGER_BACKFLOW=true
BACKFLOW_ONLY_TO_RELEVANT_STAGE=true
SEQUENTIAL_STAGE16_TO_STAGE28_RERUN=false
BACKFLOW_RESULT_REIMPORTED_ONCE=true
```

### 4. Population-versus-cover firewall

The full degree-64 sign/Kummer cover is an exact global endpoint model, but the earlier population stages are not yet automatically certified as literal successive floors of that cover tower.

```text
FULL_ENDPOINT_IS_DEGREE64_SIGN_KUMMER_COVER=true
STAGE16_20_AS_LITERAL_SIGN_TOWER_LEVELS_PROVED=false
POPULATION_TRANSFER_TO_SIGN_TOWER_AUTOMATIC=false
HEIGHT_TRANSFER_AUTOMATIC=false
PRIMITIVITY_TRANSFER_AUTOMATIC=false
ASYMPTOTIC_TRANSFER_AUTOMATIC=false
```

Making that bridge exact is a central post-29-02 task, not an assumption.

## Audited foundation inventory entering 29-03

The roadmap now treats the following as existing audited infrastructure rather than future discoveries:

- `F1`: full perfect-cuboid surface / global endpoint geometry;
- `F2`: joint space-completion × third-face-completion V4 cover over the common two-face base;
- `F3`: parametrization/coverage viewpoint;
- `F4`: joint local-arithmetic viewpoint;
- `F5`: modular `M(4,8)` / 8-congruence / Weil-restriction route;
- `F6`: endpoint L-function, K3-character, and arithmetic-cohomology route;
- `F7`: full seven-line degree-64 `(Z/2)^6` sign/Kummer cover of `P2`;
- `F8`: classical Campedelli quotient compression.

Additional audited adapters include the Beauville irregular cover and the non-Fano/Hirzebruch recognition of F7 over `Q(i)` with explicit constant-sign `Q` twist. The latter is a named theorem ecosystem for F7, not an independent foundation.

The broad 29-02hd pass found no certified ninth foundation in that pass, but unresolved adapter/independence candidates remain and the `29-02h*` namespace may reopen if genuinely new mathematics appears.

## Revised incremental roadmap

### 29-01 — GLOBAL_CERTIFIED_MAP_LOCK — COMPLETE

Freeze the certified Stage16–28 population/transition map, Stage28 closure, and finite endpoint census under common physical conventions.

### 29-02 — NEW_FOUNDATION_SCREENING — COMPLETE AFTER AUDITED SUFFIX EXTENSIONS

Screen old and new theorem ecosystems, import the high-value global endpoint foundations, and perform the broad independent-foundation stop pass. The practical screening stop does not claim literature exhaustiveness.

### 29-03 — FOUNDATION_BACKFLOW_AND_ROADMAP_RATIFICATION

Decide which audited 29-02 receivers justify targeted reentry into Stage16–28 and ratify this R2 roadmap against the actual foundation inventory.

Priority decisions include:

```text
R29-KUM3A = TwoFaceSignSubcoverToStage28ToricYBirationalAdapter
R29-KUM3B = JointV4AsResidualTwoSquareRootsOfFullSignTower
R29-KUM4  = Stage16To20PopulationMaskAsSignSubcoverLattice
R29-PESCH1 = EuclidPairToStage28TwoFaceHostAndJointV4ExactCrosswalk
```

For each receiver decide exactly one of:

```text
TARGETED_BACKFLOW_REQUIRED
STAGE29_INTERNAL_ADAPTER_ONLY
DEFER_WITH_REASON
REDUNDANT_WITH_AUDITED_ROUTE
```

No sequential Stage16→28 rerun is allowed.

### GAP_SCAN_A / ROADMAP_REVIEW_A

Check both for missed foundations and for whether the post-29-02 roadmap itself needs revision. `NONE_FOUND / ROADMAP_STILL_VALID` is acceptable.

### 29-04 — POPULATION_PREDICATE_AND_CONDITION_COST_MATRIX

Rebuild the old condition-cost ledger in the language of exact predicates.

For every population transition record:

- which square/norm/completion predicate is being imposed;
- exact YES/NO population partition at that predicate level;
- known asymptotic or power corridor;
- finite survival ratio under the common physical cutoff where meaningful;
- local obstruction law;
- geometric cover/quotient corresponding to the predicate when proved;
- whether the transition is already represented inside F2/F7 or still lacks an exact adapter.

The goal is not to call all Stage16–20 populations literal sheets of the 64-cover. The goal is to determine exactly which predicate masks correspond to which subcovers and which do not.

### 29-05 — DEPENDENCY_EQUIVALENCE_AND_DOUBLE_CHARGE_LEDGER

Determine which mechanisms are genuinely independent and which are the same condition in different mathematical languages.

Audit at least:

```text
squareclass
Gaussian norm
Pythagorean parametrization
local parity/blocker laws
thin covers
K3 quotients
joint V4
seven-line sign/Kummer characters
Campedelli quotients
Beauville descent
modular 8-congruence
L-function pieces
Brauer/cohomology receivers
```

No proof gain may be multiplied merely because the same predicate has several descriptions.

### 29-06 — GLOBAL_FOUNDATION_SYNTHESIS

Replace the old `GLOBAL_ENDPOINT_GEOMETRY` discovery task with an exact synthesis task.

Build one auditable global diagram containing, with fields of definition and map degrees:

```text
full endpoint surface
<-> degree-64 seven-line sign/Kummer model
-> seven K3 quotient directions
-> ten Campedelli kernels / Q-symmetry orbit structure
-> Beauville irregular cover
-> joint V4 / marginal K3 covers
-> modular M(4,8) / residual S4 quotient
-> L-function / character decomposition
-> non-Fano/Hirzebruch recognition over Q(i) with Q twist
```

Every arrow must be classified as exact finite map, quotient, birational map, generic map only, field extension, or still-open adapter. The synthesis must preserve the `Q` versus `Q(i)` firewalls discovered in audit.

### 29-07 — SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE

This is the main exact-bridge stage.

Attempt to prove or refute the expected placement of the Stage28 common two-face host and joint V4 inside the degree-64 sign tower. Resolve `R29-KUM3A/B` as far as possible.

Then test `R29-KUM4`: whether the Stage16–20 predicate populations can be represented as exact masks/subcovers/quotients of the same seven-squareclass architecture after preserving physical height, primitive normalization, canonical ordering, and multiplicity.

Possible outcomes are explicitly allowed:

```text
FULL_EXACT_TOWER_BRIDGE
PARTIAL_PREDICATE_BRIDGE
GEOMETRIC_ONLY_BRIDGE_NO_POPULATION_TRANSFER
NO_CLEAN_BRIDGE
```

A partial or negative result is acceptable and must not be repaired by analogy.

### 29-08 — PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS

Place all major construction/family routes into the synthesized endpoint map.

At minimum include Saunderson, StageA2 families, Meskhishvili-style families, Peschmann-style Euclid-pair/genus-3 constructions, low-degree curves, elliptic fibrations, and any repository-native parametrizations.

Record exact image dimension, generic degree/fiber, height distortion, coverage status, exceptional locus, field of definition, and whether each family lands in a curve, divisor, quotient, fibration fiber, or a dominant part of an endpoint model.

Family-specific exclusions remain family-specific unless coverage is proved.

### 29-09 — FULL_ENDPOINT_LOCAL_ARITHMETIC

Upgrade the old joint-local stage from two marginal completion predicates to the full endpoint predicate architecture.

Priority receivers include:

```text
R29-KUM-LOC1 = SevenLinearFormCommonSquareclassLocalDensity
R29-KUM-LOC2 = BranchValuationTransitionLedger
```

Also compare these with the exact Stage14–20 local blocker laws and the joint V4 finite-field correlation structure.

Determine whether the local system produces a genuinely new global sieve, character, Frobenius/monodromy restriction, Brauer-compatible obstruction, or only local sparsity without a global theorem.

### GAP_SCAN_B / ROADMAP_REVIEW_B

Review both missing mathematics and roadmap validity. Targeted backflow is allowed only for a newly sharpened exact receiver. A material new foundation may reopen `29-02h*` and trigger a roadmap revision.

## Multi-route endpoint attack block

The next three stages are deliberately a portfolio. They do not select a single winner in advance.

### 29-10 — GLOBAL_AND_K3_ATTACK_PORTFOLIO

Attack the endpoint through the full surface / degree-64 cover and its K3/low-genus geometry.

Include as applicable:

- low-degree curve exclusions and the degree-8+ frontier;
- finite Picard-lattice reductions and unresolved multibranch/effectivity cases;
- seven K3 quotient directions and their rational/elliptic fibrations;
- Terasoma/four-quadric specialization adapters where exact;
- exact natural slices with coverage labels;
- any valid determinant/incidence or rational-point technology attached to these models.

Do not require this route to dominate the others before proceeding.

### 29-11 — QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO

Attack all serious smaller-quotient/descent routes in parallel.

Include:

```text
Campedelli Q-form / H-torsor descent across the certified 6+2+2 Q-symmetry representatives
Campedelli involution quotients and Brauer/two-primary compatibility
Beauville Q-descent / twist / Albanese route
modular M(4,8), torsion-defect, residual S4, and Q-descent route
open/proper Brauer receivers where exact
```

A rational-point obstruction on any Q-defined quotient that receives every endpoint Q-point is potentially decisive; converses must not be assumed without lift/descent control.

### 29-12 — JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO

Attack routes whose strength comes from simultaneous completion, local arithmetic, or explicit parametrized/fibered models.

Include:

- joint V4 direct endpoint arithmetic;
- Stage19-side + third-face and Stage20-side + space-diagonal entrances as exact marginal charts, not automatically separate universes;
- seven-linear-form common-squareclass local/global receivers;
- Peschmann exact crosswalk if it survives `R29-PESCH1`;
- branch-sensitive interaction thresholds;
- height/multiplicity-safe counting or sieve routes;
- exact finite computations only as regression/negative control, not as global proof.

The purpose is to learn which interaction route produces a theorem unavailable from the pure geometric quotients.

### GAP_SCAN_C / ROADMAP_REVIEW_C

Compare what survived 29-10/11/12. Do not force one route to win. Instead classify each route as:

```text
GREEN = concrete theorem path with exact receiver
AMBER = meaningful but missing one identifiable theorem/adapter
RED = structurally blocked or dominated
MERGED = proved equivalent to another route
```

A material discovery may revise the remaining roadmap.

### 29-13 — A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES

Use StageA2 as a method source across every surviving natural quotient/slice/fibration, not as a privileged family.

Transfer only methods that preserve exact coverage labels: parameter reduction, quotient decomposition, low-genus models, Jacobian rank/torsion, descent, and rational-point closure.

```text
A2_FAMILY_SPECIFIC_EXCLUSION_NE_GLOBAL_EXCLUSION=true
```

### 29-14 — NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST

Attempt exact rational-point closure on the most structurally natural slices/quotients generated by the global map: K3 fibrations, Campedelli/Beauville/modular quotients, Peschmann-type fibers if adapted, and other high-relevance loci.

The output must separate:

```text
SLICE_CLOSED
SLICE_COVERAGE_FRACTION_OR_GEOMETRIC_ROLE
GLOBAL_COVERAGE_PROVED_OR_FALSE
WHAT_REMAINS_OUTSIDE_SLICE
```

Arbitrary thin families do not count as endpoint progress unless their coverage role is explicit.

### 29-15 — ENDPOINT_ARSENAL_REMATCH

Perform a concentrated rematch of StructureRadar, Arsenal, Stage14–28 weapons, A2 methods, new 29-02 theorem ecosystems, geometry, sieve, determinant/incidence, character sums, modularity, Brauer/descent, and rational-point technology against every GREEN/AMBER receiver still alive.

This is a rematch against exact receivers, not a generic literature search.

### 29-16 — RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO

Only here is route compression mandatory.

Compress unresolved endpoint work to a small portfolio of precise receivers. There may be more than one primary route if they remain genuinely independent.

For each surviving receiver state:

```text
exact population/variety
field of definition
map/coverage relation to endpoint
measure/height
quantifiers
multiplicity
required theorem strength
near-misses already ruled out
what perfect-cuboid consequence follows
status GREEN/AMBER
```

Also record RED/MERGED routes so they are not needlessly replayed later.

### GAP_SCAN_FINAL / ROADMAP_REVIEW_FINAL

Final check for unused repo-native weapons, missing symmetry/height/Q-form adapters, overlooked endpoint models, or unjustified coverage assumptions. If a genuinely new foundation appears even here, Stage29 may reopen the relevant earlier work rather than pretending the roadmap is immutable.

### 29-17 — PERFECT_CUBOID_ATTACK_HANDOFF

Freeze the final **portfolio**, not necessarily a single route.

The handoff must include:

- the exact global endpoint diagram;
- the certified relation, if any, between Stage16–20 populations and the sign/joint-cover architecture;
- all surviving GREEN and AMBER attacks;
- the strongest quotient/descent/local/global routes;
- coverage firewalls;
- finite numerical baseline;
- the minimum next theorem/computation required for each receiver.

A later direct perfect-cuboid attack stage may run several independent routes in parallel until one dominates or closes the endpoint.

### 29-close

Close Stage29 after fresh audit. Stage29 succeeds if it converts the Stage16–29 knowledge into an exact global map plus a sharply defined multi-route endpoint attack portfolio. It need not solve the perfect-cuboid problem.

## Gap-scan / roadmap-review rule

Every named gap scan returns both a mathematical gap result and a roadmap verdict.

```text
GAP_SCAN_RESULT = NONE_FOUND | FOUND_NEW_FOUNDATION_INTERNAL_ANALYSIS_REQUIRED | FOUND_TARGETED_BACKFLOW_REQUIRED | FOUND_EXTERNAL_INPUT_REQUIRED
ROADMAP_REVIEW = STILL_VALID | LOCAL_REORDER_REQUIRED | MATERIAL_REVISION_REQUIRED
```

A new suffix or roadmap rewrite is justified only by materially new mathematics, an exact new adapter, a new obstruction, a new coverage theorem, or a proved equivalence that makes planned work redundant. Cosmetic subdivision and renamed old gates are forbidden.

## Stage28 synchronization

Stage28 is closed/audited/merged through checkpoint70 / PR #1284 and imported into Stage29. Any future Stage28 work must be a narrow targeted backflow justified by a Stage29 receiver.

```text
STAGE28_FINAL_IMPORTED=true
STAGE28_REFRESH_PENDING=false
```
