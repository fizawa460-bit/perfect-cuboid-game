# Stage14-t123 — generic norm-support deficit forces near-total weight on the finite D4 boundary

## Status

`COMPLETE_GENERIC_NORM_SUPPORT_DEFICIT_TO_FINITE_BOUNDARY_WEIGHT_CONCENTRATION`

Consumes Stage14-t122 on the same batch branch and the weighted t120 receiver.

Fix the t120 exceptional packet `(m,e_loc)` and write the ambient generic-norm principal weight as

```text
A_m(g)>=0.
```

Let `G_amb` be the generic split-prime norm set in the frozen physical block and `G_phys` the subset admitting at least one ell-independent physical orientation.

Stage14-t122 proves the pointwise inclusion

```text
G_amb \ G_phys
  subset
B_bd(m),

B_bd(m):={g in G_amb : k0*m*g in {1,2}}.
```

Thus

```text
|B_bd(m)|<=2.
```

No density estimate is needed for this statement.

Define the charged principal masses

```text
H_g := sum_{g in G_amb} A_m(g),
M_g := sum_{g in G_phys} A_m(g).
```

Since every nonboundary generic norm is physically supported,

```text
H_g-M_g
 <= sum_{g in B_bd(m)} A_m(g).
```

Therefore if the t120 generic-support mechanism supplies a fixed-power deficit

```text
M_g <= B^(-delta) H_g,
```

then necessarily

```text
sum_{g in B_bd(m)} A_m(g)
 >= (1-B^(-delta)) H_g.
```

So the old support-deficit branch is no longer a diffuse polynomial support problem.  It can occur only when essentially the entire ambient prime-principal weight is concentrated on at most two exact boundary norms whose primitive Gaussian product lies on an axis or diagonal.

Equivalently, the t120 branch

```text
ExceptionalMultiplierConditionedGenericSplitPrimePhysicalNormSupportDeficit
```

is sharpened to

```text
FiniteD4BoundaryGenericNormNearTotalPrimePrincipalWeightConcentration.
```

This is a material receiver change.  The other t120 branch remains unchanged:

```text
PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

The two mechanisms now have the same extreme-correlation character: one requires near-total concentration of the principal weight on a finite rejected scalar-norm boundary, while the other requires near-total depletion of the physically selected projective prime class relative to its principal mass.

No new tH is opened yet.  Merged tH28 explicitly warns that fixed cofactor prime spines need not be power sparse, so the finite-boundary branch must first be audited internally with the exact physical prime interval and the exact values allowed by `k0*m*g in {1,2}`.  The selected-class branch likewise still needs the exact cofactor-to-class map frozen before another external theorem audit.

```text
GENERIC_NORM_SUPPORT_COMPLEMENT_SUBSET_FINITE_D4_BOUNDARY=true
FINITE_D4_BOUNDARY_GENERIC_NORM_COUNT_LE_2=true
GENERIC_SUPPORT_POWER_DEFICIT_FORCES_NEAR_TOTAL_BOUNDARY_WEIGHT_CONCENTRATION=true
GENERIC_DIFFUSE_NORM_SUPPORT_DEFICIT_RECEIVER_SUPERSEDED=true
FINITE_BOUNDARY_PRIME_SPINE_CONCENTRATION_REMAINS=true
SELECTED_CLASS_NEAR_TOTAL_DEPLETION_BRANCH_RETAINED=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=false
PREFERRED_RECEIVER=SharedUFiniteD4BoundaryGenericNormNearTotalPrimePrincipalWeightConcentrationOrSelectedProjectiveClassNearTotalPrimeDepletion
NEXT_INTERNAL_TARGET=FiniteBoundaryGenericNormPrimeSpineConcentrationAudit
NEXT=Stage14-t124
```
