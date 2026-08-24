# Stage33 — BRAUER-EXPLICIT-DAG execution roadmap

```text
STAGE33_ROADMAP_VERSION=3
STAGE33_STATUS=ROADMAP_CREATED_NOT_EXECUTED
PRIMARY_KERNEL=K16-C2-BRAUER-EXPLICIT-CHAIN
PRIMARY_PROGRAM=BRAUER-EXPLICIT-DAG
BRAUER_SCOPE=FROZEN_STAGE29_PHYSICAL_OPEN_BRAUER_KERNEL
SOURCE_FRONTIER=STAGE29
STAGE32_COMPLETION_REQUIRED=false
STAGE33_CAN_RUN_CONCURRENTLY_WITH_STAGE32=true
BIG_TASK_COUNT=11
PERFECT_CUBOID_PROBLEM_STATUS=OPEN
```

## 0. Purpose and execution policy

Stage33 is the execution program for the frozen Stage29 Brauer frontier. It is a separate research line from Stage32 low-genus Picard production. Stage32 infrastructure may be reused when technically convenient, but Stage33 does not wait for the Stage32 183-row census and receives no mathematical credit from Stage32 unless an exact adapter is explicitly proved.

The frozen starting kernel is

```text
K16-C2-BRAUER-EXPLICIT-CHAIN
```

whose audited internal shape is a dependency DAG rather than a literal chain.

Stage29's Brauer frontier is not purely two-primary. The proper odd-primary transcendental contribution was closed, but `BR0B` explicitly retained possible odd-primary open-algebraic unit/character terms. Therefore the Stage33 scope is the full frozen Stage29 physical-open Brauer kernel:

```text
BR0B = open algebraic / absolute-Galois contribution, all primary torsion retained until computed
BR0G = physical-boundary residue contribution
BR2A/BR2B = two-primary geometric/transcendental relation, representative, and evaluation contribution
```

No later unit may silently drop an odd-primary class surviving `BR0B` merely because the BR2 branch is two-primary.

This roadmap supersedes the `GO / STOP` language in `INTRODUCTION.md` as an execution policy. `BRAUER-PROSPECT-SCAN` remains useful, but only as reconnaissance and ordering information. A pessimistic scan is **not** by itself a reason to abandon Stage33.

Stage33 continues until the current Brauer mechanism is mathematically exhausted as far as the available theorem/CAS stack permits.

Allowed bounded stop/checkpoint reasons are only:

```text
A. EXACT_BRANCH_CLOSURE
   The relevant branch is proved vacuous, trivial, impossible, or completely evaluated.

B. NEW_KERNEL_EXPOSED
   A genuinely new theorem / arithmetic / effectivity dependency is isolated and cannot
   be discharged by the current source-locked theorem and exact-computation stack.

C. HOSTILE_AUDIT_REQUIRED
   A promotion boundary has been reached and no further theorem/receiver credit is allowed
   before independent audit.

D. EXECUTION_RESOURCE_WALL
   A finite exact computation is specified but the current backend cannot complete it.
   This is not negative mathematical evidence; replace/compress the backend before credit.
```

The following are **not** valid stop reasons:

```text
LOW_PROSPECT_SCORE
NO_EARLY_OBSTRUCTION
LOCAL_EVALUATIONS_LOOK_TRIVIAL
BRAUER_MANIN_SET_APPEARS_NONEMPTY_NUMERICALLY
EXTERNAL_AI_PESSIMISM
```

If the Brauer mechanism is eventually proved non-obstructive, record that exact negative result for the declared Stage33 scope and close the mechanism honestly. If a new unknown theorem is required, freeze the exact new kernel instead of pretending the route failed.

## 1. Frozen dependency shape

From Stage29:

```text
BR0A -> BR0B
BR0A + boundary incidence -> BR0G
K3-RULED2 + BR0G/physical-boundary data -> BR2A
BR2A + explicit representatives -> BR2B
BR0G/BR2A -> NF-PHYS2 when invoked
BR2A/BR2B -> CAMP4 when invoked
```

Already-audited inputs include:

```text
physical boundary components = 72
Div_D -> Pic extraction preflight exists
proper odd-primary transcendental Brauer = absent
open algebraic odd-primary contribution = NOT CLOSED at Stage29
seven-line base-complement geometric Br[2] dimension = 9
K_c has explicit ruled (4,4) double-cover model over P1 x P1
ruled-double-cover branch hypotheses discharged
dim_F2 Br(K_c_Qbar)[2] = 2
```

These are inputs only. They do not imply Q-defined endpoint classes, nonconstant local evaluation, or a Brauer--Manin obstruction.

## 2. Big-task plan

The intended Stage33 scale is **11 big tasks**. Individual tasks may require bounded child PRs, but child PR count must not be confused with roadmap size.

### Stage33-01 — BRAUER-PROSPECT-SCAN and source reconstruction

Objective: reconstruct the strongest current Stage29 Brauer state and cheaply measure where arithmetic information survives before launching the expensive exact layers.

Required probes:

```text
P0: reconstruct BR0B all-primary open-algebraic scope and confirm that no odd-primary survivor is dropped
P1: K3 geometric Br[2] dimension 2 -> provisional Q(i)/Q survival picture
P2: seven-line geometric dimension 9 -> provisional endpoint/boundary/Galois survival picture
P3: for any explicit surviving candidate class, bounded high-information local-evaluation tests
```

Outputs:

```text
SOURCE_LOCK_MANIFEST
DEPENDENCY_DAG_RECONSTRUCTED=true|false
BR0B_ALL_PRIMARY_SCOPE_RECONCILED=true|false
K3_SURVIVAL_PREVIEW
LINE9_ENDPOINT_SURVIVAL_PREVIEW
LOCAL_EVALUATION_PREVIEW
NEXT_PRIORITY_ORDER
```

Credit rule: previews are reconnaissance only. They do not close BR0A/BR0B/BR0G/BR2A/BR2B unless the exact full hypotheses for that receiver are independently met.

Continuation rule: regardless of optimistic or pessimistic preview, proceed to exact DAG work unless the scan itself already gives an exact branch-closure certificate or exposes a new kernel.

### Stage33-02 — BR0A integral Picard / saturation production

Objective: replace the preflight with an explicit, source-locked integral Picard computation strong enough for the endpoint divisor/boundary arithmetic.

Required work:

```text
- exact divisor lattice and generators used by the Brauer computation;
- integral saturation / index certificate;
- intersection and restriction maps needed downstream;
- reproducible CAS/checker manifests;
- no rational-rank-only substitute where integral saturation is required.
```

Gate:

```text
BR0A=DISCHARGED
```

only after an independently checkable integral certificate.

### Stage33-03 — BR0B absolute-Galois UPic / Gersten layer

Objective: compute the arithmetic/Galois module data that converts the geometric Picard/divisor information into the exact open-algebraic Brauer classes needed downstream, retaining all primary torsion allowed by the Stage29 receiver.

Required work:

```text
- explicit Galois action on the relevant integral modules;
- UPic/Gersten boundary maps at the required level;
- kernels/cokernels and torsion tracked exactly, without assuming 2-primary;
- unit-kernel / absolute-Galois inflation and character terms accounted for exactly;
- Qbar -> Q inference made only through explicit descent/cohomology adapters;
- complete Q-defined open-algebraic class inventory, including any odd-primary survivors,
  or an exact certificate that the relevant open-algebraic quotient is empty/trivial.
```

Gate:

```text
BR0B=DISCHARGED
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
```

or a named smaller exact residual kernel.

### Stage33-04 — BR0G physical-boundary residue adapter

Objective: carry the divisor/residue machinery through the actual physical open, including all 72 frozen boundary components and exceptional/boundary incidence data.

Required work:

```text
- complete 72-component inventory with stable IDs;
- exact residue matrix / incidence adapter;
- multiquadratic pullback and exceptional-divisor residue accounting;
- proof that no physical boundary component is silently omitted;
- exact kernel of classes unramified on the physical open.
```

Gate:

```text
BR0G=DISCHARGED
```

or exact residual.

### Stage33-05 — K3 two-primary Q(i)/Q action and descent

Objective: turn the audited geometric fact

```text
dim_F2 Br(K_c_Qbar)[2] = 2
```

into exact arithmetic information over Q.

Required work:

```text
- explicit Q(i)/Q action matrix on the two-primary geometric space;
- invariant / descended subspace calculation;
- obstruction to descent, if any;
- explicit arithmetic symbol representatives for every surviving relevant class,
  or an exact certificate that none survives.
```

Outputs must distinguish:

```text
GEOMETRIC_DIM=2
Q_RELEVANT_SURVIVING_DIM=0|1|2
```

with no inference from the first number to the second.

### Stage33-06 — seven-line endpoint survival and multiquadratic pullback

Objective: turn the audited base-complement result

```text
Br(P2_Qbar-D)[2] ~= (Z/2)^9
```

into exact endpoint data.

Required work:

```text
- explicit nine-dimensional source basis / relation matrix;
- exact pullback through the endpoint multiquadratic cover;
- physical-boundary residue survival;
- Q-Galois survival;
- duplicate/trivial symbol elimination;
- exact endpoint-relevant surviving subspace or exact zero certificate.
```

No credit from dimension 9 alone.

### Stage33-07 — BR2A Creutz--Viray relation/symbol integration and full class inventory

Objective: integrate the BR0B open-algebraic all-primary inventory with the line-arrangement, K3, physical-boundary and two-primary descent data into one complete relevant Q-defined class list for the frozen Stage33 Brauer scope.

Required work:

```text
- import every surviving BR0B Q-defined class, including odd-primary survivors;
- explicit two-primary relation matrix;
- explicit two-primary symbol matrix;
- source-lock exact theorem hypotheses and variable dictionary;
- quotient by trivial/algebraic/duplicate classes exactly without deleting BR0B classes by type;
- invoke NF-PHYS2 and/or CAMP4 only when their exact hypotheses are met;
- produce the complete relevant Q-defined class list for the declared Stage33 Brauer scope,
  with primary order and provenance recorded for every class, or an exact empty list.
```

Gate:

```text
BR2A=DISCHARGED
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
```

or named residual.

### Stage33-08 — BR2B explicit endpoint Brauer representatives

Objective: construct representatives that can actually be evaluated locally on the physical open for every class in the complete Stage33-07 inventory, regardless of primary order.

For every surviving class record:

```text
CLASS_ID
PRIMARY_ORDER
PROVENANCE=BR0B|BR0G|BR2|MERGED
FIELD_OF_DEFINITION=Q
SYMBOL_OR_ALGEBRA_REPRESENTATIVE
RAMIFICATION_SUPPORT
DENOMINATOR_SUPPORT
EQUIVALENCE/INDEPENDENCE_CERTIFICATE
PHYSICAL_OPEN_DOMAIN
```

Gate:

```text
BR2B=DISCHARGED
```

only when every relevant class from Stage33-07 has an evaluable exact representative or an exact proof that no representative/class survives.

### Stage33-09 — complete relevant-place and physical-local-locus certification

Objective: determine exactly where local evaluation can matter and certify the physical local-point loci needed for evaluation.

Required work:

```text
- derive the finite relevant-place set from the actual representatives, bad reduction,
  denominators and residue support;
- include the real place when relevant;
- never hard-code Q_2 or any prime without representative-based justification;
- include odd-primary places forced by any BR0B survivor;
- certify physical local loci/components with exact witnesses or exact local descriptions;
- prove constancy outside the finite relevant-place set when that reduction is used.
```

This task is the bridge from symbolic Brauer classes to a finite exact local computation.

### Stage33-10 — exact local evaluation production

Objective: evaluate every relevant Brauer class on every required physical local locus.

Per class/place output:

```text
CLASS_ID
PRIMARY_ORDER
PLACE
PHYSICAL_LOCAL_LOCUS_CERTIFIED=true
EVALUATION_IMAGE
COMPONENT_OR_CELL_DECOMPOSITION
WITNESS_POINTS_WHEN_NEEDED
CONSTANCY/NONCONSTANCY_CERTIFICATE
SOURCE_LOCK
```

Numerical sampling is reconnaissance only. Promotion requires exact evaluation images or an exact residual kernel.

### Stage33-11 — physical adelic compatibility, final Brauer verdict, and hostile audit

Objective: combine all exact local images under global reciprocity and determine the physical-open orthogonality status for the complete frozen Stage29 Brauer kernel executed by Stage33.

Required final alternatives:

```text
A. PHYSICAL_STAGE33_BRAUER_SCOPE_SET_EMPTY_CERTIFIED
   -> the physical adelic set orthogonal to the complete Stage33 class inventory is empty
   -> no physical endpoint Q-point
   -> perfect-cuboid nonexistence, subject to hostile audit of every endpoint adapter.

B. PHYSICAL_STAGE33_BRAUER_SCOPE_SET_NONEMPTY_CERTIFIED
   -> this completed Stage33 Brauer mechanism does not prove endpoint emptiness;
   -> record the exact surviving adelic restrictions and close this mechanism negatively;
   -> this does NOT by itself certify nonemptiness of the full Brauer--Manin set unless
      FULL_RELEVANT_BRAUER_GROUP_COVERAGE_CERTIFIED=true is separately audited.

C. RELEVANT_STAGE33_BRAUER_SCOPE_TRIVIAL_OR_EVALUATIONS_VACUOUS_CERTIFIED
   -> close this Stage33 Brauer mechanism negatively with an exact certificate;
   -> no claim is made about any Brauer class outside the declared frozen Stage33 scope.

D. NEW_KERNEL_EXPOSED
   -> freeze the smallest exact unresolved theorem/computation dependency;
   -> no nonexistence or negative-route claim beyond the proved prefix.
```

A final hostile audit must independently verify source locks, BR0B all-primary completeness, descent, boundary coverage, complete class inventory within the declared Stage33 scope, representative completeness, local-place completeness, evaluation images, reciprocity assembly and the endpoint implication.

## 3. Stage32 separation firewall

Stage33 and Stage32 may run concurrently.

```text
STAGE32_LOWGENUS_ROW_PROGRESS_IMPLIES_STAGE33_PROGRESS=false
STAGE33_BRAUER_PROGRESS_IMPLIES_STAGE32_LG2_PROGRESS=false
STAGE32_COMPLETION_REQUIRED_FOR_STAGE33=false
```

Reuse is allowed only for generic infrastructure such as exact integer/lattice code, CI patterns, manifests, checkpointing, source-lock helpers and hostile-audit machinery. Any mathematical cross-stage adapter must be stated and proved explicitly.

## 4. Anti-overclaim firewalls

```text
GEOMETRIC_BR2_NONZERO_IMPLIES_Q_BRAUER_NONZERO=false
Q_BRAUER_NONZERO_IMPLIES_NONCONSTANT_EVALUATION=false
NONCONSTANT_EVALUATION_IMPLIES_BM_EMPTY=false
BASE_COMPLEMENT_BR2_DIM9_IMPLIES_ENDPOINT_BR2_DIM9=false
K3_QBAR_BR2_DIM2_IMPLIES_TWO_Q_OBSTRUCTIONS=false
VISIBLE_V4_GALOIS_ACTION_IMPLIES_OPEN_ALGEBRAIC_2_PRIMARY_ONLY=false
BR2_TWO_PRIMARY_SCOPE_IMPLIES_WHOLE_STAGE33_BRAUER_SCOPE_2_PRIMARY=false
DAG_COMPLETION_IMPLIES_BM_EMPTY=false
DAG_COMPLETION_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=false
PROSPECT_SCAN_NEGATIVE_IMPLIES_ROUTE_IMPOSSIBLE=false
NUMERICAL_LOCAL_SAMPLING_IMPLIES_EXACT_EVALUATION_IMAGE=false
EXTERNAL_AI_REVIEW_COUNTS_AS_THEOREM_EVIDENCE=false
STAGE33_SCOPE_NONEMPTY_IMPLIES_FULL_BM_NONEMPTY_WITHOUT_FULL_COVERAGE_CERT=false
STAGE33_SCOPE_EMPTY_IMPLIES_NO_RATIONAL_ENDPOINT=true
```

## 5. Controller / handoff contract

The exact unit state machine and release law are defined by `stages/stage33/33-00/unit-closure-contract.md`. Every big task must use exactly one of:

```text
OPEN
RUNNING
AUDIT_REQUIRED
CLOSED
BLOCKED_NEW_KERNEL
BLOCKED_RESOURCE
```

Every big-task handoff must contain at least:

```text
STAGE33_UNIT=
UNIT_STATUS=OPEN|RUNNING|AUDIT_REQUIRED|CLOSED|BLOCKED_NEW_KERNEL|BLOCKED_RESOURCE
UNIT_CLOSED=true|false
DOWNSTREAM_RELEASED=true|false
PREREQUISITE_UNITS=[]
PREREQUISITES_ALL_CLOSED=true|false
CLOSURE_CRITERIA_TOTAL=
CLOSURE_CRITERIA_SATISFIED=
UNRESOLVED_UNKNOWN_IN_SCOPE=
RECEIVERS_DISCHARGED=[]
RECEIVERS_OPEN=[]
NEW_KERNEL_ID=NONE|<stable-id>
THEOREM_CREDIT=true|false
ENDPOINT_CREDIT=true|false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=true|false
SOURCE_LOCKS=[]
ARTIFACT_HASHES=[]
AUDIT_VERDICT=
NEXT_RELEASED_UNITS=[]
```

Release law:

```text
DOWNSTREAM_RELEASED=true iff UNIT_STATUS=CLOSED
```

Partial or inconclusive work remains `RUNNING` or takes the appropriate `BLOCKED_*`/`AUDIT_REQUIRED` state; it never receives a synthetic `PASS`/`PARTIAL` unit status and never releases downstream work. Progress is the number of hostile-audited `CLOSED` units out of 11.

## 6. First execution command

After this roadmap and its unit-closure contract pass hostile re-audit and PR #1355 is merged, the first execution unit is:

```text
Stage33-01
NAME=BRAUER-PROSPECT-SCAN
ROLE=RECONNAISSANCE_NOT_GO_STOP_GATE
CONTINUE_AFTER_PESSIMISTIC_SCAN=true
```

Stage33-01 should reconstruct the source state from the Stage29 frontier before trusting the frozen introduction, because later literature or repository work may have strengthened individual adapters.
