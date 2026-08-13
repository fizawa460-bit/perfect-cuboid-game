# Stage14-bridge — Numerical-to-proof translation roadmap

## Purpose

`Stage14-bridge` is the numerical-to-proof translation track for Stage14.

Its job is **not** to extend the numerical cutoff and **not** to prove an asymptotic theorem from finite data. It consumes already-frozen `Stage14-num` diagnostics, identifies reproducible arithmetic structure, converts that structure into an exact algebraic/local/family statement, and hands the smallest useful lemma or falsifiable transfer test to an active proof route.

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

- infer perfect-cuboid nonexistence from finite `T(B)=0`;
- promote a p-value or shell fluctuation to an asymptotic theorem;
- start a new numerical census merely because a mechanism is unclear;
- duplicate a lemma already owned by `14-4`, `s`, `t`, or `q`;
- replace Stage13/Stage14 theorem contracts with fitted empirical laws;
- promote an attractive ratio to a conjectural limit without a named mechanism;
- assume IID/independence for arithmetic objects without proof.

If an observation cannot be matched to a concrete proof-side object, keep it as a finite diagnostic and stop.

```text
FINITE_DATA_IS_THEOREM=false
T_EQ_0_FINITE_NONEXISTENCE=false
BRIDGE_MAY_CHANGE_STAGE14_THEOREM=false
BRIDGE_MAY_START_NEW_CENSUS=false
```

---

## Evidence ladder

```text
L0  visual / anecdotal pattern
L1  exact reproducible finite pattern
L2  survives predeclared controls / alternative weighting / shell checks
L3  exact algebraic, local-congruence, graph, squareclass, or parameter reformulation
L4  explicit dictionary to a live 14-4 / s / t proof object
L5  smallest falsifiable receiving-stage lemma or transfer test
L6  theorem-level proof in receiving route
```

Rules:

- `bridge` works on `L1` through `L5`.
- Normal handoff requires at least `L4`.
- `L6` belongs to the receiving proof route.
- `L0/L1` with no mechanism is not a proof handoff.

---

## Source contract

Bridge normally reads only merged/frozen numerical sources.

Each run records:

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

An open numerical PR may be inspected for planning, but no bridge handoff may freeze its values as authoritative before merge.

---

## Routing table

| Observed structure | Primary receiver | Bridge output |
|---|---|---|
| residue-class / prime-divisibility / local QR bias | `s`, then `14-4` | local-state identity, Fourier coefficient, conditional density question |
| reciprocal/Jacobi/character correlation | `s` / `14-4` | explicit character sum or discrepancy kernel |
| squareclass / Gaussian allocation / elliptic-cover pattern | `t` | explicit cover, kernel class, incidence-count target |
| new stable obstruction with no owned method | `q` | exact obstruction and literature-search trigger |
| graph/family clustering | object-dependent | exact family invariant or collision identity |
| pure finite instability with no mechanism | none | finite diagnostic only |
| new exact census requirement | `num` | tightly specified observable; bridge itself does not scan |

Anti-duplication:

```text
if receiver already owns the exact obstruction:
    add a numerical diagnostic only if it changes the smallest receiving test;
    otherwise NO_NEW_HANDOFF
```

---

## Promotion gates

### Gate A — exact reproducibility

- source rows/artifact frozen or deterministically regenerated;
- canonicalization and primitive conditions unchanged;
- signal survives independent recomputation or exact identity check.

### Gate B — finite-control audit

Use the relevant controls before promoting a signal:

- cumulative vs shell-local behavior;
- equal-space-diagonal weighting;
- graph-component weighting;
- arithmetic-class conditioning;
- multiple cutoffs;
- multiplicity correction;
- multiple-testing correction when a statistical calibration is used.

### Gate C — algebraization

Rewrite the signal as at least one exact object:

```text
local residue predicate
finite-field identity
Jacobi/Legendre character
squareclass condition
Gaussian ideal allocation
elliptic-cover/Kummer class
graph collision relation
Euclid-parameter family
exact endpoint/survival identity
```

### Gate D — receiver dictionary

State exactly:

```text
NUM observable <-> proof variable / local row / edge / cover / family
```

and identify the receiving Stage14 stage/file/current obstruction.

### Gate E — smallest falsifiable test

Every handoff ends with a bounded task:

```text
1. freeze one actual local state / monomial / family;
2. derive the predicted exact sign/density/identity;
3. prove or disprove it with owned tools;
4. only then insert it into the full proof assembly.
```

---

## Initial roadmap

### Stage14-bridge1 — Conditional second-face survival mechanism

Authoritative trigger sources are now merged:

- `Stage14-num-alpha11-diag7` (PR #320);
- `Stage14-num-alpha11-diag8` (PR #324), extending matched raw-face denominators through `B=1,000,000`.

Exact bridge identity:

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

Merged diag8 shows the directional second-face survival effect persists at every listed checkpoint through `B=1m`, with `S_ab` lower than `S_ac,S_bc`. This remains finite evidence; the empirical profile is not monotone toward the hypothetical profile implied by a `2:2:1` pair law.

Bridge question:

> Why is conditional acquisition of a second integral face direction-dependent, and can that bias be written in the same local/character variables already owned by `s` / `14-4`?

Required work:

1. keep the exact endpoint identity separate from any proposed limiting pair law;
2. decompose `S_ab,S_ac,S_bc` by already-frozen arithmetic/local classes rather than fit a smooth trend;
3. test whether stable components correspond to an existing Stage14 local-state row, Fourier coefficient, reciprocal character, or Euclid-state condition;
4. write the exact receiver dictionary if one exists;
5. otherwise freeze `NO_MECHANISM_YET` and stop.

Locks:

```text
PAIR_2_2_1_IS_ASSUMPTION_FOR_BRIDGE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_PROVED_BY_BRIDGE1=false
BRIDGE1_TRIGGER_READY=true
```

Expected receiver: `s` and/or `14-4`.

### Stage14-bridge2 — p=7 local-signature translator

Trigger:

A merged numerical source confirms that the `p=7` shared-edge / related divisibility signature survives relevant multiplicity/family controls.

Task:

1. write the exact `F_7` conditional universe used by the diagnostic;
2. distinguish two-face + space-diagonal conditioning from Stage13 one-face -> additional-face `lambda_7`;
3. identify whether `7 | shared edge` selects a specific local 2-descent/Fourier state in `s5*` / `14-4*`;
4. compute the exact local coefficient/density prediction if possible;
5. hand off only if a proof-side state variable is identified.

A finite association alone is insufficient.

Expected receiver: `s`, `14-4`.

### Stage14-bridge3 — Residual direction-drift mechanism

Trigger:

A merged num diagnostic still shows reproducible direction movement after known dependency explanations are removed.

Controls to reuse before inventing a mechanism:

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

Then search for an exact parameter/family invariant correlated with the residual. Do not request finer shells merely to create more fluctuations.

Possible receiver:

- `t` for squareclass/elliptic/family invariants;
- `s`/`14-4` for local-character invariants;
- `q` if a new stable obstruction is isolated with no owned method.

### Stage14-bridge4+ — Trigger-driven only

Do not manufacture an endless bridge sequence.

Open a new bridge stage only for a merged num result containing one of:

```text
NEW_EXACT_IDENTITY
REPRODUCIBLE_LOCAL_SIGNATURE
REPRODUCIBLE_FAMILY_OR_SQUARECLASS_SIGNATURE
CONTROL_SURVIVING_DIRECTIONAL_ANOMALY
NEW_THEOREM_LEVEL_QUESTION_FROM_FINITE_DATA
```

Each stage starts with:

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
3. freeze canonical tuple, primitive status, all squared-distance checks, and full hashes;
4. open an explicit emergency review artifact;
5. do not reinterpret the result before independent reproduction.

```text
T_GT_0_EMERGENCY_OVERRIDES_BRIDGE_ROADMAP=true
```

---

## Handoff format

Every successful bridge PR contains:

```text
SOURCE_NUM_STAGE=
SOURCE_NUM_PR=
SOURCE_NUM_MERGE_SHA=
OBSERVABLE=
FINITE_SCOPE=
CONTROLS_PASSED=
EXACT_REFORMULATION=
RECEIVER_ROUTE=
RECEIVER_STAGE_OR_FILE=
VARIABLE_DICTIONARY=
HANDOFF_TEST=
ASYMPTOTIC_CLAIM=false
FINITE_ZERO_NONEXISTENCE_CLAIM=false
```

If `RECEIVER_ROUTE` cannot be named, the result remains diagnostic.

---

## Monitoring/autopilot activation contract

This roadmap does **not** itself add a fourth automation lane. Activation is a separate change to `stages/stage14/AUTOPILOT.md` after user approval.

When activated, the bridge lane should:

1. watch only newly merged `Stage14-num*` work;
2. never freeze an unmerged num result;
3. process at most one anomaly/handoff per run;
4. prefer an exact mechanism over another statistical decomposition;
5. create a Draft PR only for a concrete `L4/L5` handoff or a scientifically useful durable `NO_MECHANISM_YET` closure;
6. never merge mathematical work automatically.

---

## Current starting point

Both required denominator sources are now merged, so the first bridge task is immediately available.

```text
STAGE14_BRIDGE_ROADMAP=DEFINED
BRIDGE_ROLE=NUMERICAL_TO_PROOF_TRANSLATOR
BRIDGE_FIRST_TASK=Stage14-bridge1 conditional second-face survival mechanism
BRIDGE1_SOURCE_DIAG7_MERGED=true
BRIDGE1_SOURCE_DIAG8_MERGED=true
BRIDGE1_TRIGGER_READY=true
BRIDGE1_PRIMARY_RECEIVER=s_or_14_4
BRIDGE_AUTOPILOT_ACTIVE=false
NEXT=Stage14-bridge1
```
