# Stage27-19-r9b — Saunderson lower viability verdict

The space-diagonal locus is the genus-3 curve

y^2=t^8+68t^6-122t^4+68t^2+1.

This destroys the r8 thick-family mechanism: the original Euclid parameter count T^2 comes from primitive homogeneous pairs (r,s) representing points of bounded height on P^1. Requiring a rational point on the genus-3 double cover is not a free positive-dimensional thickening of that P^1 parameter space.

A fixed genus-3 curve has only finitely many rational points by Faltings. Therefore the Saunderson space-diagonal subfamily cannot itself supply a polynomially growing Stage19 lower family unless the model degenerates or a different positive-dimensional family parameter is introduced. The polynomial is squarefree, so no such degeneration occurs here.

Consequently SR-STR-002 is RED for the current THICK_MOVING_PHYSICAL_FAMILY receiver after exact preflight. SR-STR-163/162 remain useful only if a different candidate moving family is found; they do not rescue this fixed genus-3 locus.

This does not rule out isolated perfect-cuboid points on the curve and is not a perfect-cuboid nonexistence statement.

```text
SR_STR_002_R9_STATUS=RED_CURRENT
SAUNDERSON_THICK_FAMILY_ROUTE=NO_GO
FALTINGS_FINITE_FIXED_GENUS3_RATIONAL_POINTS=true
ISOLATED_POINTS_NOT_EXCLUDED=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEW_LOWER_EXPONENT_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r9c
```
