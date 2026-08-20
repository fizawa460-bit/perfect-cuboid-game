# Stage27-19-r8d — lower construction route arbitration

```text
TASK_ID=Stage27-19-r8d
PARENT_ROUTE=Stage27-19-r8c
ROUTE_KIND=LOWER_ROUTE_ARBITRATION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
```

The r8 sweep turns the lower reopen condition into two precise nonduplicate receivers:

1. `LOW_HEIGHT_CROSS_CANCELLATION`: construct a physical rational curve with `2d_x+2d_y-g<=7`, where any useful `g>0` comes from a polynomial cross-divisibility identity between the two toric Pythagorean parameter pairs;
2. `THICK_MOVING_PHYSICAL_FAMILY`: construct a family with source-count exponent `rho>2` and controlled height `h` satisfying `rho/h>1/4`.

No repository-internal identity currently supplies either object. The previous section/affine-bisection search is already closed, and r8a-c show exactly what genuinely new structure must appear before another symbolic ansatz sweep is justified.

Accordingly the lower lane remains mathematically open but is now **construction-gated**, not merely “try a higher degree ansatz.” The next useful work is an external/structural search specifically for rational parametrized subvarieties of the two-face/space-diagonal host exhibiting either cross-divisibility cancellation or a positive-dimensional moving family with controlled height and multiplicity.

This is a natural audit boundary. Do not create r8e by generic polynomial coefficient solving without one of these structural leads.

```text
R8_STRUCTURAL_SWEEP_COMPLETED=true
LOWER_ROUTE_STATUS=OPEN_BUT_CONSTRUCTION_GATED
LOW_HEIGHT_RECEIVER=2dx+2dy-g<=7
THICK_FAMILY_RECEIVER=rho/h>1/4
NEW_LOWER_EXPONENT_PROVED=false
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
ADVANCE_TO_CHECKPOINT50=false
R8E_BLIND_ANSATZ_FORBIDDEN=true
RECOMMENDED_NEXT_ACTION=STRUCTURE_RADAR_LOWER_CONSTRUCTION_REMATCH_OR_NEW_EXTERNAL_SEARCH
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-19-r8-audit
```
