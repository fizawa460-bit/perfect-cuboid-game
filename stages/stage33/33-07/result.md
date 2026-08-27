# Stage33-07 — BR2A integration — REOPENED / BLOCKED_NEW_KERNEL

Stage33-08 hostile audit #1375 found a theorem-scope regression in the global-Q residue-lift step used by the original Stage33-07 closure.

Current effective state:

```text
STAGE33_UNIT=33-07
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR2A=BLOCKED_NEW_KERNEL
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```

Historical audit verdict
`PASS_AFTER_J2_PROPER_TRANSCENDENTAL_ENDPOINT_SURVIVAL_AND_EXACT_BR0B_BR0G_GLOBAL_INTEGRATION`
is retained as provenance, but its global BR0G Q-lift/inventory credit is superseded by the Stage33-08 hostile re-audit.

## What remains exact

The regression does **not** affect:

```text
BR0B all-primary inventory and full boundary injection
J2 Q-defined exact order 2
J2 endpoint pullback nonzero
J2 proper/unramified/transcendental
J2 Q2 evaluation nonconstant with values 0 and 1/2
seven-line endpoint contribution = 0
Stage33-04 BR0G boundary-residue presentation
```

The Stage33-04 finite ramified object

```text
(Z/2)^49 direct_sum (Z/4)^12
```

remains an exact **boundary residue module**.

## What is no longer promoted

Panin--Zainoulline Theorem 1.1 is semi-local and does not by itself prove global surjectivity of compatible residues on the whole projective surface. Therefore the following Stage33-07 claims are pending repair:

```text
complete Q-defined global BR0G class inventory
Q-defined global lifts of the constant-character complement
Q-defined global lifts of the R17/O12 finite residue directions
noncanonical finite Gersten splitting over Q
global direct-sum presentation of those lifts
full duplicate quotient involving the unknown global lifts
```

The cuboid minimal resolution is simply connected, so the global geometric residue-lift obstruction over Qbar vanishes. The remaining kernel is arithmetic descent to Q, where the proper geometric Brauer module is nonzero (transcendental l-adic rank 14).

## Closure accounting

The Stage33-07 contract requires a complete relevant Q-defined class list. That gate is currently false, so the unit is not CLOSED. A conservative current count retains only the clearly unaffected closure gates:

```text
CLOSURE_CRITERIA_TOTAL=14
CLOSURE_CRITERIA_SATISFIED_CONSERVATIVE=4
```

The exact repair target is

```text
L33-07-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS
```

No Brauer--Manin emptiness, endpoint emptiness, or Perfect Cuboid existence/nonexistence conclusion follows from this reopened state.

## Retained exact non-elementary geometric prefix (PR #1409)

The firewalled K1 pure-geometric seven-sign fixed filtration completed exactly
without rerunning any timed-out mathematical shard. Existing `14 x 32` non-P7
and `P7 x 128` evidence was recovered through paginated artifact enumeration and
verified as one disjoint mixed partition.

```text
K1_TYPE=Z/4 direct_sum (Z/2)^7
K1_SUPPORT_SKELETON_COUNT=20487593
K1_WEIGHTED_H_CHECKED=1311205952
K1_REPRESENTATIVE_SURVIVORS=0
K1_WEIGHTED_SURVIVORS=0
K1_EXACTLY_REJECTED=true
K1_CERTIFICATE_SHA256=7ac64a76b8132e044b145d009e331476f55e04a78001a127bce6fe3034c206fa
```

Together with the retained K2 and K3 exact prefixes, the next K2 pure-geometric
leaf was recovered from six byte-identical successful artifacts and reproduced
exactly from the locked inputs without launching a new Actions run. The existing
64-shard geometric-sign census was then independently reaggregated from its
manifest and all shard certificates. It rejects the remaining K2 prefix exactly:

```text
K1=REJECTED
K2_FULL_Q4_SURVIVORS=867_ORBITS_AND_517873664_WEIGHTED_H
K2_Q2_AFFINE_SURVIVORS=867_ORBIT_FAMILIES
K2_Q2_AFFINE_REPRESENTATIVE_SECTIONS=2183168
K2_Q2_AFFINE_WEIGHTED_H=129468416
K2_Q2_AFFINE_SURVIVAL_RATIO=1/4_IN_EVERY_ORBIT_FAMILY
K2_Q2_AFFINE_CERTIFICATE_SHA256=f9dd684e2813acdbec07fc59575d9d487828c97f6fa8f111983fec5a6fe6b9b0
K2_SIGN_CENSUS_REPRESENTATIVE_SECTIONS_CHECKED=2183168
K2_SIGN_CENSUS_WEIGHTED_H_CHECKED=129468416
K2_SIGN_CENSUS_REPRESENTATIVE_SURVIVORS=0
K2_SIGN_CENSUS_WEIGHTED_SURVIVORS=0
K2_SIGN_CENSUS_CERTIFICATE_SHA256=44390c7bd74b8be73f74ccc305e1b4229a73433b20f1ce9f1d02a63e0526558b
K2=REJECTED
K3=REJECTED
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
```

This abstract-type reduction does not identify the actual endpoint glue and
does not repair the arithmetic Hochschild--Serre descent kernel. The formal
Stage33-07 state therefore remains `BLOCKED_NEW_KERNEL`, with Stage33-08
unreleased. With the retained K1, K2, and K3 geometric branches rejected, the
next active exact target returns to the formal repair kernel:

```text
Stage33-07_REPAIR_GLOBAL_RESIDUE_LIFT_ARITHMETIC_HS_DESCENT
```

## Arithmetic HS repair reduction retained from BR2A regression

The existing successful workflow `Stage33-07 BR2A integration regression`
(run `33026712371`) was recovered without rerunning a heavy mathematical workload.
Its 22,238-byte compact artifact was source-locked and the relevant
certificates were reproduced locally with identical canonical hashes.

The repair problem now has the following exact, firewalled reduction:

```text
FINITE_RAMIFIED_BOUNDARY_MODULE=(Z/2)^49 direct_sum (Z/4)^12
KNOWN_GLOBAL_U44=(Z/2)^44
BOUNDARY_QUOTIENT_AFTER_U44=(Z/2)^23 direct_sum (Z/4)^3
BOUNDARY_QUOTIENT_PRESENTATION_INPUT_GENERATORS=29
BOUNDARY_QUOTIENT_MINIMAL_INVARIANT_FACTOR_GENERATORS=26
PROPER_GEOMETRIC_BRAUER_ODD_GQ_INVARIANTS=0
REPAIR_REDUCED_TO_TWO_PRIMARY=true
PROPER_GEOMETRIC_BR2_DIMENSION_F2=14
PROPER_GEOMETRIC_BR2_V4_FIXED_DIMENSION_F2=10
FINITE_V4_H1_PROPER_BR2_DIMENSION_F2=16
ABSOLUTE_H1_IDENTIFIED_WITH_FINITE_V4_H1=false
```

An explicit unimodular Smith decomposition of the retained 29-by-29 row
relation matrix has also been certified.  It supplies mutually inverse integer
coordinate maps between `R01..R17,O01..O12` and the 23 order-two plus 3
order-four invariant-factor generators.  This removes a coordinate ambiguity
from the next localization calculation, but it does not compute
`delta_loc`, the Hochschild--Serre `d2`, or a Q-defined lift.

```text
TWO_PRIMARY_RESIDUE_INVARIANT_BASIS_SHA256=f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939
ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=false
BOUNDARY_RESIDUAL_PROMOTED_TO_GLOBAL_Q_CLASSES=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
```

The next exact leaf is therefore the order-two localization extension class in
this explicit invariant basis.  The two-primary constant-character cokernel
and the order-four continuation remain in scope after that leaf.

## PR #1414 absolute-localization correction and constructive restart

The finite `V4` receiver is not the whole absolute obstruction.  The exact
coefficient action factors through

```text
L=Q(i,sqrt(2)), Gal(L/Q)=V4,
```

but inflation--restriction leaves a genuine `G_L` restriction term.  The
correct decision order is now certified as

```text
Stage A: F2^26 -> ((L*/L*2) tensor_F2 Br(Sbar)[2])^V4
Stage B: ker(Stage A) -> H^1(V4,Br(Sbar)[2]) = F2^16.
```

Stage A is exactly a `14 x 26` tensor of `L`-squareclasses, hence 364
project-specific entries.  Neither the endpoint modules nor their dimensions
determine it: all `2^416` finite `16 x 26` extension matrices occur for some
abstract endpoint-compatible extension.  Real geometric lift data are
necessary.

A focused literature recheck found no theorem that supplies this cuboid-
specific tensor.  Creutz--Viray supplies the proper `Br[2]` coefficient module,
Ford supplies the algebraically closed graph/localization layer, and the
root-stack residue theorem maps a given Brauer class to its residue rather than
constructing the inverse global arithmetic lift.  The exact verdict ledger is
`order2-localization-literature-recheck.md`.

The constructive route has therefore started from the pinned Testa--Stoll
equations.  All 24 physical side conics now have exact Pythagorean `P1`
parametrizations, and all 144 side--exceptional crossings are matched to

```text
t = 0, infinity, 1, -1, i, -i.
```

Magma independently checks every point against the fixed 48 singular points,
exhausts the six crossings on every side, and recomputes the `cc/ct` action.
The exceptional incidence histogram is exactly `24 x degree 2 + 24 x degree
4`.  This closes only the side-coordinate prerequisite; exceptional tangent
coordinates, the 26 first-residue functions, the global Gersten lifts, and the
`14 x 26` squareclass tensor remain open.

```text
SIDE_P1_MODELS=24/24
SIDE_EXCEPTIONAL_CROSSINGS=144/144
EXCEPTIONAL_INCIDENCE_HISTOGRAM={2:24,4:24}
SIDE_P1_CERTIFICATE_SHA256=ae58f55d54fd00ba3b79b7bb51a6e668450643a11e60fd67f4f89475e4b6ad04
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

## Exact exceptional tangent-conic coordinates

The next constructive coordinate leaf has now been materialized over exact
Gaussian rationals.  Starting from the retained 24-side coordinate artifact,
the certifier reconstructs every one of the 48 ordinary double points, checks
Jacobian rank three, forms its three-dimensional projective tangent quotient,
and extracts the unique nonsingular quadratic tangent-cone relation.  Exact
differentiation places all 144 physical side branches on the claimed conics.
A deterministic projection from a certified tangent point then gives a `P1`
coordinate on each exceptional curve.

The calculation is pure local `Q(i)` linear algebra.  It does not use a
numerical solver, does not rerun the retained side-coordinate Magma job, and
does not construct any global Gersten lift or `L`-squareclass entry.  Omitted
large internal coordinate matrices remain bound by per-exceptional canonical
SHA256 commitments in the compact certificate.

```text
EXCEPTIONAL_P1_MODELS=48/48
EXCEPTIONAL_PHYSICAL_TANGENT_CROSSINGS=144/144
EXCEPTIONAL_INCIDENCE_HISTOGRAM={2:24,4:24}
EXCEPTIONAL_P1_TANGENT_CERTIFICATE_SHA256=beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636
EXCEPTIONAL_P1_TANGENT_WORKFLOW_RUN=33048533111
EXCEPTIONAL_P1_TANGENT_ARTIFACT_ID=9636618898
EXCEPTIONAL_P1_TANGENT_ARTIFACT_ZIP_SHA256=ca204a1d4d5e70c50608a8942f37a57048389e5a006519779eb0f07e1e99e8f8
ORDER2_SOURCE_FIRST_RESIDUE_FUNCTIONS_MATERIALIZED=false
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

The next exact leaf is to construct the 26 first-residue functions on the 72
boundary `P1` models with a deterministic normalization compatible with the
crossing involutions.  Only after those functions and their genuine global
lifts exist can the `14 x 26` `L`-squareclass restriction tensor be evaluated.

## Quotient-to-raw order-two liftability correction

Reconstructing the historical `U44/R17/O12` residue presentation from the
retained compact inputs exposes a further exact extension wall.  The group
`A[2] = (Z/2)^26` is the order-two subgroup of the quotient by the known
`U44` unit-symbol image; it is not the same as the image of the raw
order-two crossing-residue subgroup.

Exactly 17 Smith basis vectors have raw residues of order at most two.  Their
componentwise even divisors give deterministic Kummer functions on all 72
boundary `P1` models.  The other 9 basis vectors necessarily retain odd
order-four crossing entries.  Doubling each produces a nonzero `U44`
unit-symbol residue, and the resulting obstruction map has rank 9.  Therefore
those nine quotient-order-two directions cannot be encoded as squareclass
functions without first resolving the quotient-to-raw extension/Bockstein.

```text
QUOTIENT_A2_DIMENSION_F2=26
RAW_ORDER2_FIRST_RESIDUE_FUNCTION_LIFTABLE=17
QUOTIENT_ONLY_ORDER2_WITH_RAW_ORDER4_RESIDUE=9
QUOTIENT_TO_RAW_DOUBLE_OBSTRUCTION_RANK_F2=9
ORDER2_FIRST_RESIDUE_LIFTABILITY_CERTIFICATE_SHA256=85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312
ORDER2_FIRST_RESIDUE_LIFTABILITY_WORKFLOW_RUN=33049545470
ORDER2_FIRST_RESIDUE_LIFTABILITY_ARTIFACT_ID=9637010913
ORDER2_FIRST_RESIDUE_LIFTABILITY_ARTIFACT_ZIP_SHA256=e44d2f554e299abdb163f34b65258e95ed0a9b74c7f06d933123f702b483e865
ALL_26_FIRST_RESIDUE_FUNCTIONS_MATERIALIZED=false
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

The next exact leaf is no longer a blind 26-column squareclass construction.
It is the nine-dimensional `U44` double-obstruction extension problem.  The 17
raw-order-two directions remain retained and reusable.
