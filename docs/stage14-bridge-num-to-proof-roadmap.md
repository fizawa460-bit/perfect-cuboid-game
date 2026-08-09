# Stage14-bridge — Numerical-to-proof translation roadmap

## Purpose

`Stage14-bridge` is the numerical-to-proof translation track for Stage14.

Its job is **not** to extend the numerical cutoff and **not** to prove a new asymptotic theorem from finite data. Its job is to consume already-frozen `Stage14-num` diagnostics, identify reproducible arithmetic structure, convert that structure into an exact algebraic/local/family statement, and hand the smallest useful lemma or falsifiable transfer test to an active proof route.

In one line:

```text
exact numerical anomaly
-> reproduce / control
-> algebraize
-> match to a live Stage14 proof object
-> hand off a concrete lemma/test
```

The receiving route, not `bridge`, owns any eventual theorem-level proof.

---

## Non-goals and safety locks

`Stage14-bridge` must never:

- infer perfect-cuboid nonexistence from `T(B)=0` at a finite cutoff;
- treat a p-value or finite shell fluctuation as an asymptotic theorem;
- open a new numerical census merely because a pattern is unclear;
- duplicate a lemma already assigned to `14-4`, `s`, `t`, or `q`;
- replace Stage13 or Stage14 theorem contracts with an empirically fitted law;
- promote a visually attractive ratio to a conjectural limit without a named mechanism;
- claim independence/IID for arithmetic objects without proof.

If an observation cannot be matched to a concrete proof-side object, archive it as a finite diagnostic and stop.

```text
FINITE_DATA_IS_THEOREM=false
T_EQ_0_FINITE_NONEXISTENCE=false
BRIDGE_MAY_CHANGE_STAGE14_THEOREM=false
BRIDGE_MAY_START_NEW_CENSUS=false
```

---

## Evidence ladder

Every candidate signal is assigned one level.

```text
L0  visual / anecdotal pattern
L1  exact reproducible finite pattern
L2  survives predeclared controls / alternative weighting / shell checks
L3  exact algebraic, local-congruence, graph, squareclass, or parameter reformulation
L4  explicit dictionary to a live 14-4 / s / t proof object
L5  smallest falsifiable receiving-stage lemma or transfer test written down
L6  theorem-level proof in receiving route
```

Rules:

- `bridge` may work on `L1` through `L5`.
- Normal handoff requires at least `L4`.
- `L6` belongs to the receiving proof route.
- `L0/L1` patterns with no mechanism are not enough to create a proof handoff.

---

## Source contract

Bridge reads only merged/frozen numerical sources unless the task is explicitly a pre-merge design review.

For each run record:

```text
SOURCE_NUM_STAGE=
SOURCE_NUM_PR=
SOURCE_NUM_MERGE_SHA=
SOURCE_DATA_HASH_OR_FROZEN_ARTIFACT=
OBSERVABLE=
CONTROL_SET=
EVIDENCE_LEVEL_BEFORE=
EVIDENCE_LEVEL_AFTER=
```

If the source numerical PR is still open, the bridge worker may inspect it for planning but must not freeze a bridge theorem/handoff that depends on its unmerged values.

---

## Routing table

After algebraization, route by native mathematical object rather than by where the observation was discovered.

| Observed structure | Primary receiver | Typical bridge output |
|---|---|---|
| residue-class / prime-divisibility / local QR bias | `s`, then `14-4` | exact local-state identity, Fourier coefficient, conditional density question |
| reciprocal/Jacobi/character correlation | `s` / `14-4` | explicit character sum or discrepancy kernel |
| squareclass / Gaussian allocation / elliptic-cover pattern | `t` | explicit cover, kernel class, incidence-count target |
| new proof obstruction with no owned method | `q` | exact obstruction statement and literature-search trigger |
| graph/family clustering | receiver determined by parameterization | exact family invariant or collision identity |
| pure finite instability with no mechanism | none | finite diagnostic only; no proof handoff |
| new exact census requirement | `num` | tightly specified requested observable; bridge itself does not scan |

Anti-duplication rule:

```text
if receiver already owns the exact obstruction:
    append a numerical diagnostic only if it changes the receiver's smallest test;
    otherwise NO_NEW_HANDOFF
```

---

## Promotion gates

A finite signal is promoted from diagnostic to proof handoff only if all applicable gates pass.

### Gate A — exact reproducibility

- source rows/artifact are frozen or deterministically regenerated;
- canonicalization and primitive conditions are unchanged;
- the observation survives an independent recomputation or an exact identity check.

### Gate B — finite-control audit

Use controls appropriate to the claim, for example:

- cumulative versus shell-local behavior;
- equal-space-diagonal weighting;
- graph-component weighting;
- arithmetic-class conditioning;
- multiple cutoffs;
- multiplicity correction;
- predeclared multiple-testing correction where statistical calibration is used.

Failure does not mean the observation is false; it means it remains below handoff level.

### Gate C — algebraization

Rewrite the observation as at least one exact object, for example:

```text
local residue predicate
finite-field identity
Jacobi/Legendre character
squareclass condition
Gaussian ideal allocation
elliptic-cover/Kummer class
graph collision relation
Euclid-parameter family condition
exact endpoint/survival identity
```

### Gate D — receiver dictionary

State the exact correspondence:

```text
NUM observable <-> proof variable / local row / edge / cover / family
```

and cite the receiving Stage14 file/stage/lemma or its current `NEXT` obstruction.

### Gate E — smallest falsifiable test

The handoff must end with a bounded receiving task, not a vague suggestion.

Example shape:

```text
TEST:
1. freeze one actual local state / monomial / family;
2. derive the predicted sign or density identity;
3. prove/disprove it exactly or with the already-owned analytic estimate;
4. only if it passes, insert it into the full assembly.
```

---

## Initial roadmap

### Stage14-bridge1 — Conditional second-face survival mechanism

Trigger sources:

- merged `Stage14-num-alpha11-diag7`;
- the first later merged denominator extension that reproduces the same raw-face / endpoint identity over a materially larger matched range.

Frozen exact bridge identity from diag7:

```text
a = ab&ac
b = ab&bc
c = ac&bc

E_ab = a+b
E_ac = a+c
E_bc = b+c

A_q - N1_q = E_q
S_q = E_q / A_q
```

Bridge question:

> Why is the conditional probability of acquiring a second integral face direction-dependent, and can that directional survival bias be written in the same local/character variables already averaged by the `s` / `14-4` routes?

Required work:

1. separate the exact endpoint identity from any proposed limiting pair law;
2. decompose `S_ab,S_ac,S_bc` by already-frozen arithmetic/local classes rather than fitting a smooth trend;
3. test whether the strongest stable classes correspond to an existing Stage14 local-state row or reciprocal character;
4. produce a receiver dictionary if one exists;
5. otherwise freeze `NO_MECHANISM_YET` and stop.

Important lock:

```text
PAIR_2_2_1_IS_ASSUMPTION_FOR_BRIDGE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_PROVED_BY_BRIDGE1=false
```

Expected receivers: `s` and/or `14-4`.

### Stage14-bridge2 — p=7 local-signature translator

Trigger:

A merged numerical source confirms that the previously observed `p=7` shared-edge or related local divisibility signature survives the relevant multiplicity/family controls.

Task:

1. write the exact `F_7` conditional universe used by the numerical diagnostic;
2. distinguish the two-face + space-diagonal conditioning from Stage13's one-face -> additional-face `lambda_7` problem;
3. identify whether `7 | shared edge` selects a specific local 2-descent/Fourier state already present in `s5*` / `14-4*`;
4. compute the exact local coefficient/density prediction if possible;
5. hand off only if a proof-side state variable is identified.

A finite association alone is not enough.

Expected receivers: `s`, `14-4`.

### Stage14-bridge3 — Residual direction-drift mechanism

Trigger:

After known dependency explanations are removed, a merged num diagnostic still shows reproducible direction movement across disjoint shells or matched arithmetic classes.

Known controls to reuse before inventing a new mechanism:

- same-space-diagonal multiplicity;
- primitive-face graph components;
- largest-component removal;
- known small-prime arithmetic partitions;
- shell-size/multinomial calibration.

Task:

```text
raw direction shift
- explained local/arithmetic mixtures
- known cluster/family effects
= residual structured shift
```

Then search for an exact parameter/family invariant correlated with that residual. Do **not** request finer shells merely to create more fluctuations.

Possible receivers:

- `t` if the invariant is squareclass/elliptic/family based;
- `s`/`14-4` if it is local-character based;
- `q` if a new stable obstruction is isolated but no owned technique matches it.

### Stage14-bridge4+ — Trigger-driven only

Do not manufacture an endless fixed bridge sequence.

Open a new bridge stage only when a merged num result contains one of:

```text
NEW_EXACT_IDENTITY
REPRODUCIBLE_LOCAL_SIGNATURE
REPRODUCIBLE_FAMILY_OR_SQUARECLASS_SIGNATURE
CONTROL_SURVIVING_DIRECTIONAL_ANOMALY
NEW_THEOREM_LEVEL_QUESTION_FROM_FINITE_DATA
```

Each `bridge4+` stage must begin with:

```text
TRIGGER_NUM_STAGE=
EXACT_NUM_OBSERVATION=
CONTROLS_ALREADY_PASSED=
WHY_PREVIOUS_BRIDGE_DOES_NOT_EXPLAIN_IT=
CANDIDATE_RECEIVER=
SMALLEST_ALGEBRAIZATION_TEST=
```

---

## Perfect-cuboid emergency rule

If any exact numerical census ever finds `T>0`:

1. stop normal bridge progression;
2. independently reproduce the object from raw integer identities;
3. freeze canonical tuple, primitive status, all six squared-distance checks, and full hashes;
4. open an explicit emergency review artifact;
5. do not let a bridge worker reinterpret or simplify the finding before reproduction.

```text
T_GT_0_EMERGENCY_OVERRIDES_BRIDGE_ROADMAP=true
```

This rule is about validation discipline, not an expectation that such an object will be found.

---

## Handoff format

Every successful bridge PR must contain:

```text
## Numerical source
SOURCE_NUM_STAGE=
SOURCE_NUM_PR=
SOURCE_NUM_MERGE_SHA=

## Exact observation
OBSERVABLE=
FINITE_SCOPE=

## Controls
CONTROLS_PASSED=
CONTROLS_FAILED_OR_NOT_APPLICABLE=

## Algebraization
EXACT_REFORMULATION=

## Receiver dictionary
RECEIVER_ROUTE=
RECEIVER_STAGE_OR_FILE=
VARIABLE_DICTIONARY=

## Smallest falsifiable receiving task
HANDOFF_TEST=

## Claim boundary
ASYMPTOTIC_CLAIM=false
FINITE_ZERO_NONEXISTENCE_CLAIM=false
```

If `RECEIVER_ROUTE` cannot be named, the result remains diagnostic and must not be presented as a proof advance.

---

## Monitoring/autopilot activation contract

This roadmap does **not** by itself add a fourth active automation lane. Activation should be a separate change to `stages/stage14/AUTOPILOT.md` after the user chooses to turn the bridge worker on.

When activated, the bridge lane should:

1. watch only newly merged `Stage14-num*` work since its last accepted bridge source;
2. never start while the relevant num source is still open/unmerged;
3. process at most one anomaly/handoff per run;
4. prefer an exact mechanism over another statistical decomposition;
5. create a Draft PR only when it reaches a concrete `L4/L5` handoff or when a durable `NO_MECHANISM_YET` closure is scientifically useful;
6. never merge proof work automatically.

---

## Current starting point

At roadmap creation, the most useful first bridge topic is the Stage13 -> Stage14 **conditional second-face survival** phenomenon exposed by merged `Stage14-num-alpha11-diag7`. A larger raw-denominator extension exists in an open numerical PR and must be treated as provisional until merged.

```text
STAGE14_BRIDGE_ROADMAP=DEFINED
BRIDGE_ROLE=NUMERICAL_TO_PROOF_TRANSLATOR
BRIDGE_FIRST_TASK=Stage14-bridge1 conditional second-face survival mechanism
BRIDGE1_PRIMARY_RECEIVER=s_or_14_4
BRIDGE_AUTOPILOT_ACTIVE=false
NEXT=Stage14-bridge1 after the next relevant denominator source is merged, or immediately from merged diag7 if explicitly requested
```
