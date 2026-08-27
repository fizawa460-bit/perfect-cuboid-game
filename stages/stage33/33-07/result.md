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

## PR #1419 raw-order4 Bockstein normal form

The nine quotient-order-two directions that failed the raw order-two test in
PR #1414 have now been retained at their correct raw order four rather than
being forced into Kummer squareclasses. Exact mod-4 divisor checks on all 72
boundary P1 components produce deterministic order-four first-residue function
models for all nine directions. Together with the 17 retained raw-order-two
models, all 26 boundary first-residue directions are therefore materialized in
mixed order `17 x order2 + 9 x order4` form.

The nine nonzero doubles are independent in the 44-dimensional U44 kernel.
Taking those doubles as the first nine vectors of a new U44 basis gives the
exact raw extension normal form

```text
RAW_EXTENSION_GROUP=(Z/4)^9 direct_sum (Z/2)^52
RAW_EXTENSION_ORDER=2^70
RAW_ORDER2_FIRST_RESIDUE_DIRECTIONS=17
RAW_ORDER4_FIRST_RESIDUE_DIRECTIONS=9
BOCKSTEIN_IMAGE_RANK_F2=9
COMPLEX_CONJUGATION_ON_EACH_ORDER4_FACTOR=inversion
FULL_ORDER4_BOCKSTEIN_CERTIFICATE_SHA256=085ad52c1eb1cf8069fcac9a0814250428288cc5d517a036670ae529c36eb88a
COMPACT_ORDER4_BOCKSTEIN_CERTIFICATE_SHA256=30f2a4653619419a42d5513be26c8acf7505e042e4cbef279abd3476c34d1cfa
RAW_EXTENSION_NORMAL_FORM_CERTIFICATE_SHA256=3d5467d5af707780747134af734f53263eebb8aae1ac3f3ae33f55239a6241cd
QUOTIENT_TO_RAW_BOCKSTEIN_NORMAL_FORM_CLOSED=true
GLOBAL_GEOMETRIC_GERSTEN_LIFTS_MATERIALIZED=0/26
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

This closes the finite quotient-to-raw Bockstein structure itself. It does not
close the global residue-lift problem: the 17 order-two boundary packages and
the 9 order-four boundary packages all still need genuine global geometric
Gersten lifts before their Galois differences can be computed. The corrected
smallest exact kernel is therefore

```text
R33-BR2A-26-MIXED-ORDER-FIRST-RESIDUE-GLOBAL-GERSTEN-LIFT-GALOIS-DIFFERENCE-COCYCLE
```

No finite boundary calculation is promoted to a global Q-defined lift here.
<!-- STAGE33_07_ALL72_AMBIENT_BOUNDARY_PROGRESS -->
## All-72 ambient boundary-function milestone

The mixed-order first-residue packages now have explicit ambient rational-function lifts on **all 72 boundary components**.  The 24 physical side conics contribute 120 nontrivial source/component functions with 240 selected crossing factors (`2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d`); the 48 exceptional tangent conics contribute another 120 nontrivial functions with 240 factors (`a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397`).  The exceptional constructor reproduces all 48 frozen tangent-conic commitments before forming deterministic ambient projection pairs.

This does **not** promote any source to a global geometric Gersten/Brauer lift.  The remaining exact kernel is `R33-BR2A-26-AMBIENT-BOUNDARY-FUNCTION-PACKAGES-GLOBAL-GERSTEN-OFF-BOUNDARY-RESIDUES`: assemble the 26 ambient boundary packages and certify every off-boundary codimension-one residue (or an exact cancellation) before global-lift credit.

```text
ALL_72_BOUNDARY_COMPONENT_PACKAGES_AMBIENTIZED=true
GLOBAL_GEOMETRIC_GERSTEN_LIFTS_MATERIALIZED=0/26
OFF_BOUNDARY_CODIM1_RESIDUE_CERTIFICATES=0/26
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
```
<!-- STAGE33_07_GERSTEN_EXISTENCE_26_V11 -->
## Gersten lift existence 26/26; explicit representative choice still open

The mixed-order boundary tuples now pass the **full codimension-two localization/Gersten kernel check** over `L=Q(i,sqrt(2))`: all 17 order-two sources cancel at every crossing mod 2 with even infinity poles, and all 9 order-four sources cancel as `-r + r = 0 mod 4` with denominator exponent divisible by 4.  Extending each boundary tuple by zero on every other codimension-one divisor and applying the retained localization exact sequence certifies abstract global geometric open-Brauer/Gersten lift existence for all 26 sources (`c97cf3df4c69bc859765b6844dc12e1ad24bdf0da0457446f1e5e11846c6660a`).

This promotion is deliberately separated from a choice of explicit rational-symbol representatives.  No `cc`/`ct` difference cocycle in the proper 14-dimensional `Br(Sbar)[2]` basis has been materialized, so the finite localization connecting map remains the exact kernel.

```text
GLOBAL_GEOMETRIC_GERSTEN_LIFT_EXISTENCE_CERTIFIED=26/26
GLOBAL_GEOMETRIC_GERSTEN_EXPLICIT_REPRESENTATIVES_MATERIALIZED=0/26
FINITE_V4_H1_PROPER_BR2_DIMENSION_F2=16
LOCALIZATION_EXTENSION_CLASS_MATRIX_TARGET_SHAPE=16x26
LOCALIZATION_EXTENSION_CLASS_COLUMNS_MATERIALIZED=0/26
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

Next exact kernel: `R33-BR2A-26-GERSTEN-LIFT-CHOICE-GALOIS-EXTENSION-CLASS-IN-PROPER-BR2`.
Next leaf: `L33-07-COMPUTE-GALOIS-EXTENSION-CLASS-OF-26-GERSTEN-LIFT-TORSOR-WITHOUT-REQUIRING-RATIONAL-SYMBOL-REPRESENTATIVES`.

<!-- STAGE33_07_POST_PURITY_GERSTEN_TORSOR_V12 -->
## Post-purity Gersten torsor ambiguity remains 416 bits

Actions run `33073824503` independently reproduced the 26/26 abstract
Gersten-existence prefix and all 416 elementary endpoint-compatible V4
extensions, then locked their exact information boundary in `3e9f189a2d94a7a3640e7e44504e60a8c2199b30d9e395651abf243d02af3a32`.
Purity proves every lift fibre is nonempty, but supplies neither a chosen
representative nor a Galois-equivariant section or `cc`/`ct` lift-difference
cocycle.  Therefore the retained inputs determine none of the `16 x 26`
connecting-matrix entries.  This is an information-boundary result; it does
**not** claim that all `2^416` abstract endpoint-compatible extensions are
geometrically realised.

```text
GLOBAL_GEOMETRIC_GERSTEN_LIFT_EXISTENCE_CERTIFIED=26/26
GLOBAL_GEOMETRIC_GERSTEN_EXPLICIT_REPRESENTATIVES_MATERIALIZED=0/26
ENDPOINT_COMPATIBLE_EXTENSION_AMBIGUITY_DIMENSION_F2=416
CONNECTING_MATRIX_TARGET_SHAPE=16x26
CONNECTING_MATRIX_COLUMNS_MATERIALIZED=0/26
GEOMETRIC_REALIZABILITY_OF_ALL_ABSTRACT_EXTENSIONS_CLAIMED=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

Actions evidence: workflow `Stage33-07 post-purity Gersten torsor ambiguity`,
run `33073824503`, artifact `9647000457`, digest
`sha256:21841cffd1ee3d36a1086c5a5e956cc2f6ffa5fa8d2e778de6b7266410b303f6`.

Next exact kernel: `R33-BR2A-GENUINE-GALOIS-EQUIVARIANT-GERSTEN-MIDDLE-MODULE-OR-26-LIFT-DIFFERENCE-COCYCLES`.
Next leaf: `L33-07-MATERIALIZE-GALOIS-EQUIVARIANT-GERSTEN-MIDDLE-MODULE-OR-26-CC-CT-LIFT-DIFFERENCES`.

<!-- STAGE33_07_BOUNDARY_SOURCE_V4_ACTION_V13 -->
## Boundary-source V4 action closed; middle extension still open

Actions run `33075304812` reconstructed complex conjugation on every chosen
raw boundary representative.  All 17 raw-order-two sources are fixed; the
nine raw-order-four sources are inverted with defect equal to their locked
U44 double/Bockstein class.  After passage to `A[2] ~= F2^26`, both `cc` and
`ct` act trivially.  Thus the source action is no longer missing.  This does
not choose or act on any genuine middle Gersten lift, and the `16 x 26`
connecting matrix remains wholly unmaterialized.

```text
RAW_SOURCE_ACTION=17_CC_FIXED_ORDER2_PLUS_9_CC_INVERTED_ORDER4
QUOTIENT_A2_DIMENSION_F2=26
QUOTIENT_A2_CC_ACTION=TRIVIAL
QUOTIENT_A2_CT_ACTION=TRIVIAL
SOURCE_SIDE_V4_ACTION_FULLY_MATERIALIZED=true
MIDDLE_GERSTEN_MODULE_ACTION_MATERIALIZED=false
CONNECTING_MATRIX_COLUMNS_MATERIALIZED=0/26
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

Actions evidence: workflow `Stage33-07 boundary source V4 action adapter`,
run `33075304812`, artifact `9647609431`, digest
`sha256:3f252012ea0c71487e4d2750936289d3953794b4fbf9be1fc11544b0658bd44f`.

Next exact kernel: `R33-BR2A-GENUINE-GALOIS-EQUIVARIANT-MIDDLE-GERSTEN-EXTENSION-CLASS-WITH-SOURCE-AND-KERNEL-ACTIONS-FIXED`.
Next leaf: `L33-07-MATERIALIZE-MIDDLE-GERSTEN-CC-CT-ACTIONS-OR-26-CHOSEN-LIFT-DIFFERENCE-COCYCLES`.

<!-- STAGE33_07_FINITE_SWAP_NONZERO_WITNESS_V14 -->
## Finite swap envelope cannot force the localization class to zero

The retained finite conditions on the two coordinate swaps do not determine
the actual integral Picard actions, and they are not strong enough to force
the unknown finite localization map to vanish.  An exact Boolean certificate
materialized one admissible finite swap pair satisfying the `cc`/`ct`
centralizer conditions, all seven sign-conjugacy equations, the retained
two-torsion quadratic form, both involution equations, and the `S3` braid
relation.  For this candidate, the seven-sign plus two-swap naturality system
has rank `386` in the ambient `26 x 16 = 416` matrix space, leaving dimension
`30`, together with an explicit nonzero kernel vector.

This candidate is deliberately **not** identified with the actual integral
Picard swap pair.  Its role is only to refute the proposed universal statement
that every admissible finite candidate forces zero.  Therefore no value of the
actual connecting map is inferred and no column is materialized.

```text
EXPLICIT_ADMISSIBLE_FINITE_COUNTEREXAMPLES=1
AMBIENT_CONNECTING_MAP_DIMENSION_F2=416
COUNTEREXAMPLE_CONSTRAINT_RANK_F2=386
COUNTEREXAMPLE_REMAINING_DIMENSION_F2=30
ROBUST_ZERO_OVER_ALL_ADMISSIBLE_FINITE_CANDIDATES=false
ACTUAL_INTEGRAL_PICARD_SWAP_IDENTIFIED=false
MIDDLE_GERSTEN_MODULE_ACTION_MATERIALIZED=false
CONNECTING_MATRIX_COLUMNS_MATERIALIZED=0/26
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

Actions evidence: workflow `Stage33-07 finite swap naturality nonzero witness`,
run `33120565761`, certificate
`2db42b3f5cc7a166d891efe4850e1008c92622dfd4b5ef83f9ab9b2ce386943b`,
artifact `9666283654`, digest
`sha256:5474ade2beb8cbd64b457534b2361e9bd8aed1c2a6dfa90c2c9f916c9f5f8832`.

The repeated public-Magma swap workflows remain available only as manual
diagnostics; their PR-synchronization triggers are disabled after repeated
HTTP 500 failures.  The next exact leaf is
`L33-07-MATERIALIZE-MIDDLE-GERSTEN-EXTENSION-DATA-OR-AN-INTEGRAL-SWAP-DISTINGUISHER`.

<!-- STAGE33_07_INTEGRAL_PICARD_SWAP_LINEAR_ENVELOPE_V15 -->
## Exact retained-Picard swap linear envelope

`certify_integral_picard_swap_linear_envelope.py` uses the nonexpiring exact
64-dimensional Picard Gram, cc/ct actions, and all seven integral coordinate-sign
actions.  It makes no remote CAS request.  The nine commuting involutions split
`Pic(S)_Q` into 40 exact joint-character blocks with multiplicity histogram
`1:21, 2:18, 7:1`; distinct blocks are pairwise Gram-orthogonal and
nondegenerate.

For each desired coordinate swap, the required cc/ct commutation and sign-label
conjugacy leave a 142-dimensional rational linear intertwiner space.  This is a
necessary-condition envelope only: the unknown swaps have not been required to
be integral Gram isometries, involutions, or an S3 pair.  Therefore this leaf
does not identify either actual geometric Picard swap.  It instead isolates the
missing input as an exact integral curve-class/ample-cone marking (or equivalent
Picard quotient transport), unless genuine middle-Gersten lift data is supplied
directly.

```text
JOINT_CHARACTER_COUNT=40
JOINT_CHARACTER_MULTIPLICITIES=1:21,2:18,7:1
SWAP12_RATIONAL_LINEAR_INTERTWINER_DIMENSION=142
SWAP13_RATIONAL_LINEAR_INTERTWINER_DIMENSION=142
ACTUAL_INTEGRAL_PICARD_SWAP_IDENTIFIED=false
CONNECTING_MATRIX_COLUMNS_MATERIALIZED=0/26
MIDDLE_GERSTEN_MODULE_ACTION_MATERIALIZED=false
PROJECT_14x26_L_SQUARECLASS_TENSOR_MATERIALIZED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
```

Actions evidence: workflow `Stage33-07 integral Picard swap linear envelope`,
run `33121552448`, certificate
`571559b47c3cb54a950b0551d615672bb5373d0fd1a34eb4ace5b90e95d708b2`,
artifact `9666647588` (`1663` bytes), digest
`sha256:23554096cbd266a2cf8ed145abab1ac238b32b1b2243bc3b0f3439795ef33d77`.

Next leaf:
`L33-07-MATERIALIZE-INTEGRAL-CURVE-CLASS-OR-AMPLE-CONE-SWAP-DISTINGUISHER-OR-GENUINE-MIDDLE-GERSTEN-LIFT-DATA`.

<!-- STAGE33_07_RETAINED_STAGE32_PICARD_MARKING_V16 -->
## Stage32 Picard marking recovered before storage expiry

The still-live immutable Stage32 prepared artifact `9588229672` was downloaded
with its locked zip digest and reduced to the two exact inputs needed by this
Stage33 route: the saturated rank-63 `H^perp` packet and the nine geometric
140-class permutations.  The compact nonexpiring retained bundle has canonical
SHA256 `e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c`.

An independent local rational reconstruction from this packet reproduced the
historical `picard-core.json` canonical SHA256
`de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870`
literally.  It also checked all 140 known classes and the hyperplane were
integral in the selected 64-class basis, the Gram determinant was `-2^28`, and
`H^2=16`.  This recovers the missing integral marking input without using the
currently failing public Magma service.

The subsequent actual-swap/H1 naturality certificate was not completed in this
run and is not claimed here.

```text
RETAINED_STAGE32_PICARD_MARKING=true
HISTORICAL_PICARD_CORE_CANONICAL_SHA_REPRODUCED=true
KNOWN_CLASSES_RECOVERED=140
PICARD_RANK=64
PICARD_GRAM_DETERMINANT=-268435456
HYPERPLANE_SQUARE=16
ACTUAL_INTEGRAL_PICARD_SWAP_IDENTIFIED=false
CONNECTING_MATRIX_COLUMNS_MATERIALIZED=0/26
MIDDLE_GERSTEN_MODULE_ACTION_MATERIALIZED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ACTUAL_INDEX512_GLUE_IDENTIFIED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

Next leaf:
`L33-07-DERIVE-ACTUAL-SWAP-AND-V4-H1-ACTIONS-FROM-RETAINED-STAGE32-PICARD-MARKING`.
