# Stage36 — Campedelli uniform H-torsor arithmetic

```text
STAGE=36
ROOT_KERNEL=K16-C3-CAMPEDELLI-UNIFORM-TORSOR
SOURCE_RECEIVER=R29-CAMP2
PARENT_ROUTE=Q11-CAMPEDELLI
SOURCE_EXECUTION_CLASS=3
INITIAL_STATUS=PLANNED_NOT_STARTED
INITIAL_CLASSIFICATION=CLASS3_ACTIVE
R29_CAMP2_CLOSED=false
Q11_CAMPEDELLI_CLOSED=false
ENDPOINT_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage36 is the dedicated post-Stage29 attack on `K16-C3-CAMPEDELLI-UNIFORM-TORSOR`.
It does not reopen Stage29. It attacks only the audited Campedelli receiver
`R29-CAMP2=ArithmeticHTorsorDescentForThreeCertifiedQSymmetryRepresentatives`.

The ten audited Q-defined Campedelli kernels are reduced only by the certified
Q-liftable symmetry decomposition `6+2+2`, so the arithmetic execution frontier
contains exactly three certified Q-symmetry representatives. The geometric
`Q(i)` decomposition `8+2` is not a Q-arithmetic classification.

For every physical endpoint Q-point, the audited quotient maps give

```text
U_endpoint(Q) -> C_H(Q)
```

for every admissible Q-defined Campedelli kernel `H`. Hence proving
`C_H(Q)=empty` for one audited quotient is sufficient to kill physical endpoint
Q-points. The converse is false: a rational quotient point need not lift
rationally upstairs.

## Audited source frontier

Stage36 consumes, rather than rediscovers, these Stage29 facts:

```text
- ten admissible rank-3 Campedelli kernels;
- every kernel and quotient is Q-defined;
- Sbar -> Cbar_H has degree 8;
- S -> C_H is etale of degree 8 on the resolved level;
- H ~= (Z/2)^3;
- certified Q-symmetry decomposition is 6+2+2;
- three Q-symmetry representatives suffice for R29-CAMP2;
- endpoint Q-points push to every audited C_H;
- quotient Q-points do not automatically lift;
- point fibers define H-torsor classes in H^1(Q,H);
- H^1(Q,H) is infinite before ramification/Selmer restriction.
```

Primary retained authorities:

```text
stages/stage29/29-16/active-kernel-ledger.json
stages/stage29/29-06/endpoint-hub-graph.json
stages/stage29/29-06/source-crosswalk.md
stages/stage29/29-02hb/route-contract.json
stages/stage29/29-02hb/arithmetic-routing.md
stages/stage29/29-02hb/campedelli-quotient-adapter.md
stages/stage29/29-02hb/source-lock.md
```

Stage29 history beyond those interfaces is not routine Stage36 startup input.

## Formal Arsenal routing

Stage36 follows the canonical Research Arsenal route:

```text
docs/arsenal/index.json
-> only the relevant generated/formal card
-> revalidate against current Stage36 source locks.
```

Do not preload the full Arsenal. Pre-registered candidate methods are:

```text
S34-WF01 CLASS3_RECEIVER_REPLACEMENT_THEOREM_PIPELINE
  exact replacement theorem may discharge R29-CAMP2 if its quantifiers match.

S30-W02 SEMILINEAR_GALOIS_DESCENT_ADAPTER
  use only if an external Campedelli/torsor model needs an explicit Q-form adapter.

S30-WF02 IMMUTABLE_LAYERED_CERTIFICATE_REPLAY
  source-lock external arithmetic computations and expensive finite certificates.

S30-WF03 ADAPTER_CREDIT_LAYER_FIREWALL
  keep Q-form, torsor, finite-twist, local, quotient, receiver and endpoint credit separate.

S34-W01 SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT
  use only if exact torsor equations yield a finite exhaustive squareclass family.

S34-W03 RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION
  use if the exact physical-image plus one torsor/branch can be proved empty.

S34-W02 GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION
  locked until a globally exhaustive finite reduction gives certified auxiliary curves
  with full Mordell-Weil group and all torsion data.
```

Provisional Stage33 cards are discovery/routing only and never override Stage36
live authority or formal Arsenal contracts.

## Stage36 proof firewall

The following implications are forbidden unless separately proved:

```text
GEOMETRIC_QI_8_PLUS_2 != Q_ARITHMETIC_CLASSIFICATION
CERTIFIED_Q_SYMMETRY_6_PLUS_2_PLUS_2 != EXACT_Q_ISOMORPHISM_CLASSIFICATION
GEOMETRICALLY_RATIONAL != Q_RATIONAL
GEOMETRIC_ENRIQUES_CLASSIFICATION != EXPLICIT_Q_MODEL
H1_Q_H_WRITTEN_DOWN != FINITE_TWIST_FAMILY
BOUNDED_TWIST_SEARCH != SELMER_EXHAUSTIVENESS
LOCAL_SOLUBILITY_OF_SELECTED_TWISTS != GLOBAL_QUOTIENT_POINT_CLASSIFICATION
CAMPEDELLI_BRAUER_STRUCTURE != CAMP2_TORSOR_CLOSURE
QUOTIENT_Q_POINT != ENDPOINT_Q_POINT
```

Population-stage contracts do not transfer through the quotient:

```text
PRIMITIVITY_TRANSFER=false
CANONICAL_ORDER_TRANSFER=false
HEIGHT_TRANSFER=false
POPULATION_ASYMPTOTIC_TRANSFER=false
```

Stage36 is an endpoint rational-point attack only.

# Executable roadmap

## 36-01 — SOURCE_AUTHORITY_LOCK

Freeze the exact Stage29 kernel/receiver/quotient authority imported by Stage36.

Required output:

```text
ROOT_KERNEL exact identity
R29-CAMP2 exact identity
Q11-CAMPEDELLI parent identity
ten-kernel count
degree-8 H quotient
H=(Z/2)^3
certified Q orbit split 6+2+2
one-way endpoint -> quotient rational-point map
all source paths and immutable hashes
```

No new Campedelli literature search is allowed here.

Pass condition:

```text
STAGE36_SOURCE_FRONTIER_LOCKED=true
NEW_THEOREM_CREDIT=false
```

## 36-02 — THREE_Q_REPRESENTATIVE_INVENTORY

Materialize one exact kernel `H` and one exact quotient `C_H` for each certified
Q-symmetry orbit `6+2+2`.

For each representative record:

```text
exact kernel generators/labels
exact Q-defined quotient
canonical versus resolved model
quotient equations or exact retained model locator
Q-action/symmetry provenance
relation to the other kernels in its certified orbit
```

Do not collapse the three representatives to two from geometric `8+2`.

Pass condition:

```text
THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT=true
EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM=false
```

## 36-03 — PHYSICAL_OPEN_PUSH_AND_BOUNDARY

Replay the exact physical endpoint -> `C_H` map and identify every
deleted/exceptional locus relevant to arithmetic descent.

Required chain:

```text
U_endpoint -> S / Sbar -> C_H / Cbar_H
```

Explicitly treat:

```text
free-action locus
six A1 quotient points
canonical/resolution distinction
branch/deleted boundary
points where the torsor model changes or degenerates
```

Pass condition:

```text
ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT=true
CONVERSE_LIFT_CLAIM=false
```

## 36-04 — EXPLICIT_H_TORSOR_AND_LIFT_CLASS

Turn the abstract `H`-torsor fiber into an explicit arithmetic object.
For rational quotient point `P`, construct the exact class

```text
delta_H(P) in H^1(Q,H)
```

and an exact criterion for the endpoint fiber to have a Q-point.

Required payload:

```text
explicit degree-8 torsor/cover equations or equivalent cocycle
three independent Z/2 characters
exact twist parameters
zero/pole/degenerate cases
exact rational lifting iff-condition
```

Pass condition:

```text
POINTWISE_H_TORSOR_CLASS_EXPLICIT=true
FINITE_TWIST_FAMILY_PROVED=false
```

Writing down `H^1(Q,H)` alone does not prove finiteness.

## 36-05 — UNIFORM_RAMIFICATION_SUPPORT

This is the first main Class-3 wall.

Prove that every physically relevant H-torsor class is unramified outside one
explicitly controlled finite set `S`, or isolate the exact reason such a uniform
`S` is not currently proved.

Analyze at least:

```text
boundary divisors
bad reduction
prime 2
infinity/sign
discriminants
numerator/denominator support introduced by quotient coordinates
exceptional loci from 36-03
```

Legal outcomes:

```text
PASS_UNIFORM_FINITE_RAMIFICATION_SUPPORT
BLOCKED_MOVING_RAMIFICATION_SUPPORT
BLOCKED_MISSING_QFORM_OR_BOUNDARY_ADAPTER
```

A bounded prime experiment does not prove finite support.

## 36-06 — FINITE_SELMER_STYLE_TWIST_FAMILY

Entry condition: 36-05 proves sufficient uniform ramification control.

Replace the infinite `H^1(Q,H)` lifting problem by one exact finite exhaustive
twist family.

Required:

```text
exact Selmer-style ambient group
all unit/sign/2-adic components
completeness proof
duplicate/twist-equivalence handling
certified exhaustive finite list or exact finite parameter space
```

Pass condition:

```text
FINITE_EXHAUSTIVE_H_TWIST_FAMILY=true
```

If finiteness cannot be proved, do not enumerate arbitrary search bounds.

## 36-07 — EXHAUSTIVE_LOCAL_SOLUBILITY_FILTER

Apply exact local conditions to every certified twist from 36-06.
At minimum inspect all mathematically required places:

```text
R
2
all ramified/bad primes
all additional primes required by the exact torsor model
```

Every eliminated twist must carry a concrete local witness.

Legal outcomes:

```text
ALL_TWISTS_LOCALLY_ELIMINATED
FINITE_LOCALLY_SOLUBLE_SURVIVORS_CERTIFIED
```

No conclusion about `C_H(Q)` follows merely because most twists fail locally.

## 36-08 — SURVIVOR_GLOBAL_CLOSURE

If 36-07 leaves survivors, classify exactly the remaining arithmetic object.
Possible exact forms include:

```text
genus-one curves
higher-genus curves
finite covers
explicit Brauer/etale-Brauer obstruction
another proof-capable finite auxiliary object
```

Only now may Stage36 invoke a downstream Arsenal method that matches the exact
object.

`R29-CAMP4` / `K16-C2-BRAUER-EXPLICIT-CHAIN` may be consulted as an asset
provider if exact Campedelli Brauer compatibility is needed, but it remains a
sibling kernel and is not silently merged into Stage36 authority.

Pass condition:

```text
EVERY_LOCALLY_SOLUBLE_SURVIVOR_GLOBALLY_CLOSED=true
```

or isolate a sharper remaining Class-3 theorem.

## 36-09 — RECEIVER-MATCHED REPLACEMENT / BREADTH GATE

If the direct H-torsor/Selmer route remains blocked, do not immediately broaden
into arbitrary Campedelli literature.

First:

```text
1. state the exact surviving receiver;
2. state the exact missing theorem quantifiers;
3. consult docs/arsenal/index.json;
4. apply S34-WF01 if an exact replacement theorem species exists.
```

If materially distinct routes repeatedly block, invoke the repository Cycle
Exploration Safety Protocol before parking or inventing another route.

Required cycle behavior is the same as Stage35/35EX:

```text
EXHAUSTIVE_VIEW_AUDIT
+
BLIND_REDISCOVERY
```

Use the exact machine-readable enum contracts from the current policy. Do not
silently revive dominated/frozen routes.

## 36-10 — DECISION_CERTIFICATE_OR_PARK

Possible final Stage36 classifications:

```text
R29_CAMP2_CLOSED_BY_QUOTIENT_EMPTINESS
R29_CAMP2_CLOSED_BY_RECEIVER_MATCHED_REPLACEMENT
CLASS3_RETAINED_WITH_SHARPER_CAMPEDELLI_THEOREM
SPLIT_TRIGGERED_DISTINCT_OBSTRUCTIONS
```

To claim quotient emptiness Stage36 must certify:

```text
exact audited Q-defined quotient
exact endpoint push map
complete torsor/descent or replacement theorem
every ramification/boundary/exceptional case
no surviving rational quotient point
```

Even after `C_H(Q)=empty` is proved, Stage36 must separately record
`R29_CAMP2_CLOSED=true` before any parent promotion.

Do not automatically set:

```text
Q11_CAMPEDELLI_CLOSED=true
ENDPOINT_CLOSED=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=true
```

without a separately audited dependency/promotion implication.

# Operating rules — same model as Stage35

Ordinary startup is bounded. After confirming current branch/PR/head, read only:

```text
1. AGENTS.md
2. stages/stage36/MAIN-START-HERE.md
3. stages/stage36/MAIN-STATE.json
4. stages/stage36/MAIN-BATCH-HANDOFF.md
5. files named by current_leaf_working_set
```

`ROADMAP.md` is planning provenance, not routine startup input.

Repository asset discovery is search-first:

```text
known path -> direct fetch
known symbol/file -> targeted search
explicit source-lock -> follow exact locator
recursive tree traversal -> only for an explicitly exhaustive need
```

A search miss is not evidence of absence.

Each leaf should be kept small enough to audit independently. Prefer:

```text
one mathematical claim/interface
-> one certificate
-> one verifier
-> one small commit or tightly bounded PR unit
```

Before fresh literature search:

```text
exact missing object/theorem type
-> Arsenal router
-> relevant card only
-> external literature only if no matching applicable retained weapon exists
```

Before heavy compute use the repo-wide Actions evidence/safety policy. Before
receiver/theorem/endpoint promotion use the research-credit firewall. Before
parking after repeated blocked reformulations use the Cycle Exploration Safety
Protocol.

At every hostile-audit boundary:

```text
exact current head
current-main freshness
immutable source locks
exact-head CI
no stale controller/state authority
explicit no-credit firewall
no merge until hostile audit PASS
```

At batch end, promote exact authority only into `MAIN-STATE.json`; keep temporary
narrative only in `MAIN-BATCH-HANDOFF.md`.

# Anti-loop rules

Do not:

```text
enumerate arbitrary H^1(Q,H) twists without a finite-support proof
search more primes merely because a bounded local search found no points
replace Q arithmetic by the geometric Q(i) 8+2 orbit split
assume geometric rationality gives a Q-parametrization
treat CAMP4 Brauer data as automatic CAMP2 closure
redo all ten kernels when the certified 6+2+2 symmetry reduction applies
repeat literature searches without a changed exact theorem target
promote a quotient rational point to an endpoint rational point
promote finite computation without exhaustive provenance
```

Reopen a parked Stage36 route only on material new input:

```text
new uniform ramification theorem
exact finite Selmer/twist reduction
new Q-form/torsor adapter
proof-capable Campedelli Brauer obstruction matching the receiver
exact receiver-matched replacement theorem
audited contradiction to the current quotient/torsor model
```
