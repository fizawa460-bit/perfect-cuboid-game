# Stage29-15 — ENDPOINT_ARSENAL_REMATCH + mandatory OPEN-receiver execution triage

```text
STAGE=Stage29
ITEM=29-15_ENDPOINT_ARSENAL_REMATCH
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
BASE_MAIN_SHA=469996b93fe93650423fb2b4d629f67b1a2998b9
ATTACK_ROUTE_COUNT_RETAINED=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=2
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=1
P_OVER_M3_SCALE_KNOWN=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Purpose

29-15 is not only a literature/Arsenal rematch. It now contains a mandatory anti-hollow-AMBER pass over every current named OPEN residual receiver and the literal terminal frontier.

Every such receiver is forced into exactly one execution class:

```text
1 EXECUTE_NOW_BOUNDED
2 CURRENT_TOOL_LIMIT_EXECUTED
3 NEW_THEOREM_REQUIRED
4 DORMANT_NONDECISIVE
```

Class 1 is transient. If a receiver is genuinely finite/bounded, tractable from current exact data, and endpoint-decisive or route-enabling, it must be executed **inside 29-15**. It may not be handed to 29-16 as `OPEN_BOUNDED`.

A finite task whose completion has no current endpoint-decision or route-enabling consequence is class 4, with a concrete reactivation trigger. A theoretically finite task already reduced to an infeasible current implementation/model/CAS wall is class 2 and must name that exact wall. Class 3 is reserved for genuinely uniform/infinite/global theorem input.

The authoritative submitted ledger is

```text
stages/stage29/29-15/open-receiver-triage.json
```

and the class-1 execution proofs are in

```text
stages/stage29/29-15/bounded-execution.md
stages/stage29/29-15/verify_bounded_execution.py.
```

Submitted classification:

```text
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED=2
CLASS1_EXECUTED=2
CLASS1_PENDING=0
CLASS2_CURRENT_TOOL_LIMIT_EXECUTED=16
CLASS3_NEW_THEOREM_REQUIRED=9
CLASS4_DORMANT_NONDECISIVE=17
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS=0
```

## 2. New bounded execution A — Beauville V4 kernel

Stage29-02d left

```text
R29-BEAU2A=SwapEquivarianceOfBeauvilleV4AlbaneseIsogenyKernel
```

as `OPEN_BOUNDED`.

For the cuboid Beauville tower

```text
C0 x C0 -> X_B=(C0 x C0)/Delta(Gamma) -> D x D,
Gamma ~= (Z/2)^2,
```

the deck group of the second map is

```text
(Gamma x Gamma)/Delta(Gamma) ~= Gamma,
[(g,h)] -> g h^{-1}.
```

Factor exchange sends this class to its inverse. Since every element of `Gamma` has order dividing two, inversion is the identity. Hence factor exchange acts trivially on the V4 deck group. By Albanese functoriality, the induced V4 isogeny kernel is swap-stable.

Therefore the Q(i)/Q swap descent preserves the kernel and the expected Weil-restriction target is legitimate:

```text
R29-BEAU2A=DISCHARGED_SWAP_EQUIVARIANT_V4_KERNEL
BEAUVILLE_V4_KERNEL_SWAP_STABLE=true
BEAUVILLE_V4_DECK_ACTION_UNDER_SWAP=TRIVIAL
DESCENDED_ALBANESE_Q_ISOGENY_TARGET=Res_{Q(i)/Q}(J_D,Q(i))
```

This closes an adapter, not the infinite twist problem. `R29-BEAU2` and `R29-BEAU3` remain theorem-level.

## 3. New bounded execution B — exact p=2 local density

Stage29-09/12 left

```text
R29-KUM-LOC2-2=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
```

for the seven forms

```text
x,y,z,x+y,x+z,y+z,x+y+z.
```

The exact state reduction is finite.

`P^2(F_2)` has seven equal primitive parity cylinders. Any pattern with two or three of `x,y,z` odd fails the common-squareclass condition because the sum of two odd same-squareclass units has odd 2-adic valuation. Exactly the three cylinders with a unique odd coordinate survive.

In one surviving chart, scale the odd coordinate to one and let `X,Z in 2Z_2` be the other two ratios. Simultaneous squarehood of `X` and `1+X` occurs exactly for

```text
v2(X)=2a, a>=2,
odd-unit(X)=1 mod 8,
```

with conditional state mass

```text
w_a=2^(-2a-2),
sum_{a>=2} w_a=1/48.
```

The same holds for `Z`. The correlated condition `X+Z` is a square exactly when the half-valuations differ by at least two. Equal half-valuations and adjacent half-valuations contribute respectively

```text
1/3840
1/7680.
```

Thus the success mass inside one surviving parity cylinder is

```text
1/2304 - 1/3840 - 1/7680 = 1/23040.
```

Multiplying by the three of seven surviving projective parity cylinders yields

```text
Delta_2=(3/7)*(1/23040)=1/53760.
```

Hence

```text
R29-KUM-LOC2-2=DISCHARGED_EXACT_TWO_ADIC_STATE_DENSITY
DELTA_2=1/53760
TWO_ADIC_LOCAL_OBSTRUCTION_EMPTY=false
```

This is local infrastructure only. `R29-KUM-LOC3` remains a class-3 global physical-height/measure transfer receiver.

## 4. Whole endpoint theorem rematch

The strongest certified whole-endpoint counting input remains the already-consumed Stage14 consequence

```text
P(B)<<_epsilon B^(1/2+epsilon).
```

It is sparsity, not emptiness.

A fresh high-level near-match is surface Chabauty. It is structurally inapplicable to the **full endpoint surface**: the smooth resolution has

```text
q(S)=h^1(S,O_S)=0,
Alb(S)=0.
```

Every morphism from a smooth projective variety to an abelian variety factors through its Albanese, so `S` cannot embed positively dimensionally in an abelian variety. Therefore the abelian-embedding hypothesis used by the Caro--Pasten surface Chabauty--Coleman method and the Balakrishnan--Caro refinement is unavailable:

```text
R29-ARS-SURFACE-CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO.
```

This does not apply to auxiliary irregular covers or curve-level Chabauty.

`R29-PI1-OPEN` remains class 3: no effective cuboid-open higher-dimensional/nonabelian Chabauty-Kim theorem is certified.

## 5. Low-genus and fibration arithmetic

Rank-zero quotient enumeration, classical/elliptic Chabauty, Mordell--Weil sieve and quadratic Chabauty remain valid tools once a concrete Q-defined curve and reconstruction map exist.

They are not uniform infinite-family theorems. The exact finite Picard program `R29-LG2/LG2-EFF/LG2-MB` has already been pushed to a mathematically finite rank-44 lattice search, but the Stage29-02c-LG2 feasibility audit records `bound^22` close-vector growth and no symmetry-reduced effectivity-aware production enumerator. These are class 2, not a fresh class-1 job silently deferred.

`R29-FIB1` is class 4: a finite field-of-definition ledger by itself does not cover or exclude endpoint rational points. `R29-FIB2` is class 3 because a uniform moving-family arithmetic/specialization theorem is still required.

## 6. K3, Campedelli, modular and Brauer routes

No current K3 Brauer theorem directly supplies an obstruction on the exact cuboid K3 physical-image locus. Explicit CM/Kummer Brauer tools remain adapter-ready, but potential-density/density results are nondecisive for emptiness.

The Campedelli geometric rational/Enriques dichotomy is already consumed. `R29-CAMP3` is class 4 until a concrete Q-arithmetic theorem makes the finite type assignment consequential. `R29-CAMP2` is class 3 because its H-torsor classes are infinite without a uniform ramification/Selmer support theorem.

The modular route already computes the eight K8 defect elements and ordinary `1,3,3,1` conjugacy split. `R29-MOD1C` and `R29-KUM5` are class 2: the exact remaining wall is the arithmetic sigma/action-cocycle model, not an unattempted generic S4 calculation. Cusp/boundary ledgers `MOD1D/MOD2B` are class 4 until an arithmetic defect class survives and needs them.

For the physical-open Brauer route, 29-02f already isolated the exact `UPic/Gersten/two-primary` targets and explained why finite V4 data alone do not close absolute-Galois hypercohomology. The individual finite/model computations are class 2 with explicit missing matrices/modules in the triage ledger. `R29-QWEB-CLIFFORD` remains class 3 because its missing input is genuinely a new applicable isotropy/Clifford theorem.

## 7. Local, parametric and population routes

Odd-prime local density and the new exact p=2 density are now complete local inputs, but they do not multiply into a global endpoint theorem without `R29-KUM-LOC3`; that receiver is class 3.

Master-Hit global Euler-brick coverage is already consumed. The universal exponent-one blocker remains conjectural:

```text
R29-PESCH-E1=NEW_THEOREM_REQUIRED.
```

Bounded Peschmann/fibration identification and finite MW searches are class 4 unless a theorem makes a finite computation exhaustive.

The 29-13 external inputs are also forced through the rule:

- Paper C: finite windows were actually audited; the all-multiples continuation cannot be obtained by extending a window, so `CURRENT_TOOL_LIMIT_EXECUTED` with the primitive-divisor theorem boundary recorded.
- Paper D: height structure is currently endpoint-nondecisive, so `DORMANT_NONDECISIVE`.
- Paper E: a real certification attempt was made in 29-13; the source lacks the rigorous integrality-preserving map/completeness certificate needed to turn its elliptic integral-point count into the claimed quartic closure, so it is class 2 rather than vague AMBER.

The sole GREEN parent route remains

```text
J12-POP-INTERACTION=GREEN.
```

No existing bound controls the literal endpoint survival

```text
P(B)/M3(B).
```

That terminal frontier is class 3. Density zero inside larger hosts is not a P/M3 theorem and is not emptiness.

## 8. 29-15 submission verdict

The Arsenal rematch found no new decisive whole-endpoint theorem, but the mandatory bounded-execution rule materially improves the submission:

```text
ARSENAL_REMATCH_COMPLETE=true
OPEN_RECEIVER_TRIAGE_COMPLETE=true
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED_COUNT=2
CLASS1_EXECUTED_COUNT=2
CLASS1_PENDING_COUNT=0
CLASS2_CURRENT_TOOL_LIMIT_EXECUTED_COUNT=16
CLASS3_NEW_THEOREM_REQUIRED_COUNT=9
CLASS4_DORMANT_NONDECISIVE_COUNT=17
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0

NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=2
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=1
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE=FULL_ENDPOINT_SURFACE_CHABAUTY_BY_ALBANESE_ZERO

ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

29-16 is therefore allowed to receive only classes 2, 3 and 4. If the 29-15 audit discovers any further receiver that should be class 1, it must be executed and audited on this same PR before advancement.
