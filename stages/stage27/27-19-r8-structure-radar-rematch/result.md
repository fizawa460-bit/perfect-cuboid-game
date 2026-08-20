# Stage27-19 — StructureRadar rematch to r8 lower construction receivers

```text
TASK_ID=Stage27-19-r8-StructureRadar-lower-rematch
CHECKPOINT=40
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The audited r8 lower route has two exact nonduplicate receivers:

1. `LOW_HEIGHT_CROSS_CANCELLATION`: construct a physical rational curve with `2d_x+2d_y-g<=7`, where useful `g>0` comes from a genuine polynomial cross-divisibility identity between the two toric Pythagorean parameter pairs;
2. `THICK_MOVING_PHYSICAL_FAMILY`: construct a physical moving family with source-count exponent `rho` and physical height degree `h` such that `rho/h>1/4`.

The full StructureRadar classification was rematched against these receivers.

## Strongest matches

### SR-STR-002 — AMBER_STRONG for THICK_MOVING_PHYSICAL_FAMILY

The generalized Saunderson construction is a genuine two-parameter parametric Diophantine family and already demonstrates the exact type of source-dimension mechanism needed for a thick lower family. Its recorded lower exponent is for primitive canonical Euler cuboids without the space-diagonal condition. Therefore it does not directly lower-bound Stage19/N2, but it is the closest construction blueprint in the radar corpus.

Exact missing adapter:

```text
SAUNDERSON_TO_STAGE19_SPACE_DIAGONAL_ADAPTER:
Find a positive-dimensional subfamily/cover of the generalized Saunderson parameter space on which the space diagonal is rational/integral, retain primitive/canonical/exactly-two masks, and prove source-count exponent rho and physical height h with rho/h>1/4 and finite-to-subpower multiplicity.
```

This is a real construction target rather than an analytic counting theorem. If such a subfamily has one additional independent equation but still source exponent near three at height eight, the aspirational exponent is near 3/8.

### SR-STR-163 — GREEN_STRUCTURAL / AMBER_WEAK

Generalized-Jacobian/Prym and rational-2-torsion descent is a legal way to encode branched square/space-diagonal conditions on a candidate family. It can be used as an adapter once a candidate moving family is proposed, but it does not itself construct a low-height or thick family and supplies no lower exponent.

### SR-STR-162 — AMBER_WEAK

The moving first-small-point/2-descent pipeline supplies a way to control rational points across a moving Pythagorean/elliptic family after a candidate construction exists. It is primarily a family-uniformity/height tool, not a source of a new family. It may become useful for proving multiplicity/height control of a Saunderson-derived or other candidate subfamily.

### SR-STR-223 — RED_AS_CONSTRUCTION / GREEN_GEOMETRIC_CONTEXT

The moving genus-five/fiber-product card explains the geometry of compatible Stage14/Stage19 lifts but is an upper/counting obstruction receiver, not a constructive parametrization theorem. Fixed-fiber quotient decompositions and finite rank/torsion data do not furnish the required moving rational surface/curve with controlled height.

## Other corpus verdicts

- K3/thin-cover cards such as SR-STR-003 are primarily upper/thin-set tools and do not construct a Stage19 lower family.
- Squareclass/sieve/large-sieve/determinant cards are wrong-direction for a lower construction unless a candidate family first produces an explicit cover or divisibility identity.
- Existing R501/R502 quarter-power families remain calibration data, not new receivers.

## Route decision

No `GREEN_DIRECT` lower breakthrough is already present in StructureRadar. However the lower rematch is not empty: SR-STR-002 gives a concrete next construction program, with SR-STR-163/162 as downstream adapters for the extra space-diagonal condition and moving-family arithmetic control.

The preferred next route is therefore not a blind polynomial ansatz. It is:

```text
NEXT_ROUTE=Stage27-19-r9
NEXT_KIND=SAUNDERSON_SPACE_DIAGONAL_SUBFAMILY_PREFLIGHT
PRIMARY_CARD=SR-STR-002
SECONDARY_ADAPTERS=SR-STR-163,SR-STR-162
TARGET=positive-dimensional generalized-Saunderson subfamily with integral space diagonal and rho/h>1/4
BROAD_EXTERNAL_SEARCH_REQUIRED_BEFORE_R9=false
```

A first preflight should derive the space-diagonal square condition explicitly on the generalized Saunderson parameter space, determine its dimension/genus after obvious scaling symmetries, and compute the height ledger before attempting a full parametrization. If it collapses to a high-genus/finitely-many problem or to the known R501/R502 curves, freeze this route and only then request a new external construction search.

```text
DIRECT_GREEN_LOWER_BREAKTHROUGH_FOUND=false
SR002_STATUS=AMBER_STRONG
SR163_STATUS=GREEN_STRUCTURAL_AMBER_WEAK
SR162_STATUS=AMBER_WEAK
SR223_STATUS=RED_AS_CONSTRUCTION
R8_REMAINING_STATUS=OPEN_WITH_CONCRETE_CONSTRUCTION_PROGRAM
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
ADVANCE_TO_CHECKPOINT50=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-19-r8-StructureRadar-rematch-audit
```
