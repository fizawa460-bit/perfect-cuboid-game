# Stage33 — BRAUER-EXPLICIT-DAG roadmap

```text
STAGE33_ROADMAP_VERSION=4
STAGE33_ROADMAP_ROLE=PLANNING_ONLY
PRIMARY_KERNEL=K16-C2-BRAUER-EXPLICIT-CHAIN
PRIMARY_PROGRAM=BRAUER-EXPLICIT-DAG
BRAUER_SCOPE=FROZEN_STAGE29_PHYSICAL_OPEN_BRAUER_KERNEL
SOURCE_FRONTIER=STAGE29
BIG_TASK_COUNT=11
PERFECT_CUBOID_PROBLEM_STATUS=OPEN
```

This file is the **plan**, not the live status or policy authority.

Use:

```text
stable Stage33 rules     -> stages/stage33/RULES.md
human current state      -> stages/stage33/CURRENT.md
machine current state    -> stages/stage33/controller.json
history/evidence index   -> stages/stage33/HISTORY.md
unit closure details     -> stages/stage33/33-00/unit-closure-contract.md
active J2 repair plan    -> stages/stage33/ROADMAP-33-05-J2-REPRESENTATIVE-REPAIR.md
33-07 repair-band plan   -> stages/stage33/ROADMAP-33-07-REPAIR-BAND.md
```

Do not add mutable `STAGE33_STATUS`, current receiver, live-route ledger, or batch progress here. Those belong in CURRENT/controller/active state. Historical route decisions belong in HISTORY/results/Git history.

## Purpose

Stage33 executes the frozen Stage29 physical-open Brauer frontier. It is separate from Stage32 low-genus production; infrastructure may be reused, but mathematical credit transfers only through explicit adapters.

The frozen scope contains the Stage29-retained open-algebraic contribution, physical-boundary residue contribution, and two-primary geometric/transcendental contribution. The exact scope and release laws are governed by `RULES.md` and the unit-closure contract.

## Frozen dependency shape

```text
BR0A -> BR0B
BR0A + boundary incidence -> BR0G
K3-RULED2 + BR0G/physical-boundary data -> BR2A
BR2A + explicit representatives -> BR2B
BR0G/BR2A -> NF-PHYS2 when invoked
BR2A/BR2B -> CAMP4 when invoked
```

This dependency sketch is planning structure only; the current reopened/repair state is read from CURRENT/controller.

## Eleven big tasks

The Stage33 progress denominator is the eleven big tasks below. Repair children are addressed separately and do not independently increment the denominator.

### Stage33-01 — BRAUER-PROSPECT-SCAN / source reconstruction

Reconstruct the Stage29 Brauer inputs and dependency DAG, reconcile the all-primary BR0B scope, and produce reconnaissance that orders later exact work without promoting previews into theorem credit.

### Stage33-02 — BR0A integral Picard / saturation

Produce the explicit integral divisor/Picard lattice, saturation/index evidence, and exact intersection/restriction maps required downstream.

### Stage33-03 — BR0B absolute-Galois UPic / Gersten

Compute the arithmetic/Galois module layer, including all primary torsion permitted by Stage29, exact kernels/cokernels, descent adapters, and the Q-defined open-algebraic class inventory or exact zero result.

### Stage33-04 — BR0G physical-boundary residue adapter

Account exactly for the frozen physical boundary, residue/incidence maps, multiquadratic pullback, exceptional divisors, and the unramified physical-open kernel.

### Stage33-05 — K3 two-primary Q(i)/Q action and descent

Start from the geometric two-dimensional Br[2] space and determine the exact Q-relevant arithmetic survival/descent data. Every surviving class needs an explicit arithmetic representative or an exact zero-survival certificate.

The present J2 representative repair is a repair of this task; its live R5e/R5f/R5g state is deliberately not repeated here.

### Stage33-06 — seven-line endpoint survival / multiquadratic pullback

Transport the geometric nine-dimensional line-complement Br[2] source through endpoint pullback, physical-boundary survival, Q-Galois survival, and exact duplicate/trivial-symbol quotienting.

### Stage33-07 — BR2A relation/symbol integration / complete class inventory

Integrate BR0B, BR0G, K3, line-arrangement, relation, symbol, and descent data into one complete relevant Q-defined Stage33 class inventory, with order and provenance for every class.

If hostile review reopens this task, repair children are governed by `ROADMAP-33-07-REPAIR-BAND.md`; the roadmap does not duplicate their current status.

### Stage33-08 — BR2B explicit endpoint representatives

Construct exact locally evaluable representatives for every surviving class, with field of definition, ramification/denominator support, equivalence/independence evidence, and physical-open domain.

### Stage33-40 — relevant places / physical local loci

Determine the complete finite relevant-place set from actual representatives and certify the physical local loci/components needed for evaluation, including any odd-primary places forced by BR0B survivors.

### Stage33-41 — exact local evaluations

Evaluate every relevant class on every required physical local locus with exact evaluation images and constancy/nonconstancy certificates; numerical sampling is reconnaissance only.

### Stage33-42 — adelic compatibility / final Brauer disposition

Assemble all exact local images under reciprocity and determine the exact disposition of the complete frozen Stage33 Brauer scope, followed by the required hostile audit and endpoint-promotion checks.

Possible mathematical outcomes are represented by the unit-closure contract; this roadmap does not itself grant endpoint or perfect-cuboid credit.

## Repair address space

`33-09..33-39` is repair address space rather than additional denominator tasks. Which repair children are active, closed, blocked, or released is a **current-state** matter and must be read from controller/CURRENT and the repair-band roadmap/state.

Repair-child completion never changes the Stage33 numerator by itself. It may enable hostile recertification and closure of a reopened parent big task according to the unit-closure contract.

## Stage32 separation

Stage32 and Stage33 may run concurrently. Progress in one does not imply mathematical progress in the other. Cross-stage mathematical reuse requires an explicit adapter; generic infrastructure reuse is allowed.

## Detailed acceptance criteria

This roadmap intentionally does not duplicate exact closure booleans, state-machine definitions, audit requirements, anti-loop policy, claim firewalls, or current status.

Those live in:

- `RULES.md` for stable Stage33 policy;
- `33-00/unit-closure-contract.md` for exact unit acceptance/release gates;
- Research OS for repo-wide evidence/credit/Actions rules;
- CURRENT/controller/active unit state for live execution state.

The pre-migration detailed roadmap and its old `ROADMAP_CREATED_NOT_EXECUTED` header remain recoverable in Git history and are indexed conceptually by `HISTORY.md`.
