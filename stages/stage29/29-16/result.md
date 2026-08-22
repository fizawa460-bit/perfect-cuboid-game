# Stage29-16 — residual receiver compression and route portfolio

```text
STAGE=Stage29
ITEM=29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
BASE_MAIN_SHA=a58d3a1580ef4f0086ff448bbad8fe7a5686bf3a
SOURCE_RECEIVER_OR_TERMINAL_FRONTIER_COUNT=46
SOURCE_CLASS1_CLOSED_COUNT=6
SOURCE_CLASS2_ACTIVE_COUNT=13
SOURCE_CLASS3_ACTIVE_COUNT=11
SOURCE_CLASS4_DORMANT_COUNT=16
ACTIVE_SOURCE_ENTRY_COUNT=24
COMPRESSED_ACTIVE_KERNEL_COUNT=13
COMPRESSED_CLASS2_KERNEL_COUNT=4
COMPRESSED_CLASS3_KERNEL_COUNT=9
ATTACK_ROUTE_COUNT_RETAINED=11
INDEPENDENT_EXECUTION_OWNER_ROUTE_COUNT=9
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Purpose

29-15 forced every residual receiver into one of four execution classes and executed every Class-1 task that was actually tractable with current exact data. The post-Work re-audit finished with

```text
46 total receiver/frontier entries
  6 class 1 discharged
 13 class 2 current-tool-limit executed
 11 class 3 new-theorem required
 16 class 4 dormant/nondecisive.
```

29-16 does not reopen those proofs. Its job is to remove bookkeeping duplication from the surviving frontier.

The 24 active Class-2/Class-3 entries are grouped by identical execution wall, dependency chain and endpoint consequence. No kernel mixes Class 2 and Class 3.

The exact result is

```text
13 Class-2 entries -> 4 computational kernels
11 Class-3 entries -> 9 theorem kernels
24 active entries   -> 13 execution kernels.
```

The authoritative mapping is `active-kernel-ledger.json`.

## 2. Four computational kernels

### K16-C2-LOWGENUS-PICARD-PRODUCTION

Compresses

```text
R29-LG2
R29-LG2-EFF
R29-LG2-MB.
```

The remaining wall is one production-quality, symmetry-reduced, effectivity-aware and multibranch Picard-lattice program to the audited `d<=176/192` bounds.

Completion remains nondecisive by itself: no theorem covers every physical endpoint rational point by a rational or elliptic curve.

### K16-C2-MODULAR-S4-ACTION

Compresses the sole active modular implementation receiver

```text
R29-KUM5.
```

`MOD1C` and `MOD1D` are already discharged. The live task is the action/cocycle-level identification between the arrangement and modular residual `S4` data. Completing it maps the eight exact marked defects; it does not automatically eliminate any defect.

### K16-C2-BRAUER-EXPLICIT-CHAIN

Compresses the exact finite/model chain

```text
R29-CAMP4
R29-K3-RULED2
R29-BR0A
R29-BR0B
R29-BR0G
R29-BR2A
R29-BR2B
R29-NF-PHYS2.
```

This is the largest computational kernel but it is one dependency chain, not eight independent research directions.

Already discharged inputs include:

```text
72-component physical boundary
Ford seven-line complement Br[2] precursor of dimension 9
K_c Q-defined ruled (4,4) double-cover model
simple branch hypotheses
geometric dim_F2 Br(K_c_Qbar)[2]=2
boundary_module_probe.m extraction preflight.
```

The remaining wall is explicit integral/Galois arithmetic: materialize the boundary-to-Picard matrices and saturation, compute the full `UPic/Gersten` data, finish the Creutz--Viray relation/symbol basis and Q-action, construct surviving two-primary classes, and evaluate them locally on the physical/lift locus.

This kernel is endpoint-decision-capable: an empty certified physical Brauer/etale-Brauer set would prove endpoint emptiness. Completing the matrices alone may instead produce a nonempty set and therefore does not guarantee a solution.

### K16-C2-EXT-E-INTEGRAL-CERTIFICATION

The remaining Paper-E certification is kept separate because it is a thin-family computation and is not a prerequisite for the global Brauer chain.

Even a successful closure would exclude only that special family.

## 3. Nine theorem kernels

### K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT

`R29-PI1-OPEN`: an effective cuboid-specific rational-point theorem on the physical endpoint open. This is the broad full-surface theorem frontier.

### K16-C3-CAMPEDELLI-UNIFORM-TORSOR

`R29-CAMP2`: uniform finite ramification/Selmer-style control or a replacement arithmetic theorem for an audited Q-defined Campedelli quotient. Since every endpoint Q-point pushes to every audited Q-defined quotient, emptiness of one such quotient is decisive.

### K16-C3-BEAUVILLE-ONE-STEP-DESCENT

Compresses

```text
R29-BEAU1C
R29-BEAU2
R29-BEAU3.
```

The exact squareclass function is already known. Cao--Demarche--Xu and Cao show that ordinary descent equals etale-Brauer on the smooth physical open and that iterated descent is not stronger. Therefore the remaining Beauville work is one one-step problem:

```text
make the physically occurring open twists finite,
or uniformly control every locally soluble twist strongly enough to compute the one-step descent/etale-Brauer set.
```

No second-descent route survives independently.

### K16-C3-QWEB-CLIFFORD-OBSTRUCTION

`R29-QWEB-CLIFFORD`: a new rank-seven Clifford/isotropy theorem strong enough for the exact endpoint web, with the exact physical adapter.

### K16-C3-M3-LOCAL-TO-GLOBAL

`R29-KUM-LOC3`: transfer the complete local squareclass information to the exact primitive canonical Euler-cuboid measure under `R<=B`.

Ambient `P2` or toric equidistribution is insufficient because conditioning on `M3` is the whole missing theorem.

### K16-C3-PESCH-EXPONENT-ONE

`R29-PESCH-E1`: prove the universal exponent-one blocker or an exact replacement.

This is the narrowest currently named theorem-shaped target whose audited coverage already gives

```text
IF PROVED -> PERFECT CUBOID NONEXISTENCE.
```

The implication is audited; the blocker itself remains conjectural.

### K16-C3-MOVING-FIBER-ARITHMETIC

`R29-FIB2`: a uniform moving-family theorem or globally exhaustive finite reduction with exact reconstruction. Individual fiber Chabauty/Mordell--Weil calculations cannot replace the uniform quantifier.

### K16-C3-EXT-C-PRIMITIVE-DIVISOR

`R29-EXT-CHANG-C`: the finite windows are exhausted. The residual all-multiples step really is a new odd-multiplicity primitive-divisor theorem. It remains a thin/special family rather than global coverage.

### K16-C3-TERMINAL-P-OVER-M3

The literal final survival frontier remains

```text
P(B)/M3(B).
```

No certified nontrivial global scale is known. A proof that this tends to zero would close the final population-ratio question but would still not prove `P(B)=0`.

## 4. Route compression

The eleven historical attack-route labels remain useful as provenance, but they are no longer eleven independent execution owners.

Two routes have no unique current execution kernel:

```text
G10-K3-SIGN
  -> current live K3 arithmetic is executed inside K16-C2-BRAUER-EXPLICIT-CHAIN.

J12-JOINT-V4
  -> its exact V4 cell structure is retained, but its bounded ADE child is dormant;
     the remaining literal final interaction is represented by K16-C3-TERMINAL-P-OVER-M3 unless a genuinely new joint theorem appears.
```

Thus

```text
LEGACY_ATTACK_ROUTE_COUNT=11
INDEPENDENT_EXECUTION_OWNER_ROUTE_COUNT=9
MERGED_SUPPORT_ROUTE_COUNT=2.
```

This is execution compression, not a color change and not route deletion.

```text
G10-FULL-ENDPOINT       = AMBER
G10-LOWGENUS-PICARD     = AMBER
G10-K3-SIGN             = AMBER
Q11-CAMPEDELLI          = AMBER
Q11-BEAUVILLE           = AMBER
Q11-MODULAR             = AMBER
Q11-BRAUER              = AMBER
J12-JOINT-V4            = AMBER
J12-LOCAL-SQUARECLASS   = AMBER
J12-PARAMETRIC          = AMBER
J12-POP-INTERACTION     = GREEN
```

## 5. Closed and dormant work

The six discharged Class-1 receivers are archived and removed from active scheduling.

The sixteen Class-4 receivers remain dormant with explicit reactivation triggers in `inactive-inventory.json`. They are not failed routes and are not deleted. They simply have no current endpoint-decision or route-enabling consequence.

No Class-4 work is promoted merely because it is finite.

## 6. What 29-16 says about the remaining difficulty

The frontier is now cleanly separated:

```text
4 computational kernels = concrete model/CAS/algorithm work
9 theorem kernels       = genuinely new uniform/global mathematical statements
16 dormant receivers    = do not spend effort until a trigger appears.
```

This does not imply the four computational kernels are easy. For example the low-genus Picard search is finite but combinatorially severe, and the physical-open Brauer chain requires large exact integral/Galois computations.

Likewise the nine theorem kernels vary drastically in scope. `PESCH-E1` and `EXT-C` are narrow problem-specific theorem targets; `P/M3`, M3 local-to-global and full endpoint effective rational-point theory are broad frontiers.

The separate scope/decision classification is in `decision-frontier.md`.

## 7. Submission verdict

```text
RESIDUAL_RECEIVER_COMPRESSION_COMPLETE=true
SOURCE_RECEIVER_OR_TERMINAL_FRONTIER_COUNT=46
SOURCE_CLASS1_CLOSED_COUNT=6
SOURCE_CLASS2_ACTIVE_COUNT=13
SOURCE_CLASS3_ACTIVE_COUNT=11
SOURCE_CLASS4_DORMANT_COUNT=16
ACTIVE_SOURCE_ENTRY_COUNT=24
COMPRESSED_ACTIVE_KERNEL_COUNT=13
COMPRESSED_CLASS2_KERNEL_COUNT=4
COMPRESSED_CLASS3_KERNEL_COUNT=9
ALL_ACTIVE_SOURCE_ENTRIES_MAPPED_EXACTLY_ONCE=true
MIXED_EXECUTION_CLASS_KERNEL_COUNT=0
DORMANT_RECEIVER_COUNT=16
DORMANT_REACTIVATION_TRIGGER_MISSING_COUNT=0

ATTACK_ROUTE_COUNT=11
INDEPENDENT_EXECUTION_OWNER_ROUTE_COUNT=9
MERGED_SUPPORT_ROUTE_COUNT=2
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
NEW_ATTACK_ROUTE_CREATED=false
P_OVER_M3_SCALE_KNOWN=false

AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM_AFTER_AUDIT_PASS=GAP_SCAN_FINAL
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
