# Stage14-4dj — conditional principal-density localization

## Status

`COMPLETE_FULL_CONDUCTOR_PRINCIPAL_DENSITY_DEFICIT_LOCALIZATION`

Consumes merged `Stage14-4di`, merged frozen `Stage14-4diH`, merged `Stage14-sH50`, and merged `Stage14-X15`.

The entering whole-family bound is

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The 4diH/sH50 audits show that the remaining obstruction is not conductor loss but the positive conditional principal density together with the X15 pairwise/triple covariance terms.

## 1. Conditional root cells

Fix a full-conductor physical cell

```text
c=(C_*,rho,orientation,balanced-squarefree decorations),
rho^2=-1 mod C_*,
C_*=B^(chi+o(1)), 1/6<=chi<=1/4.
```

Let `M(c)` be the exact number of physical packets in this cell after retaining all plus/minus/k-agreement masks. Let `M_max(c)` be the charged-once complete-coordinate majorant supplied by the merged `(C_*,S,T)` finite-fiber parameterization. Define

```text
omega(c)=M(c)/M_max(c),
0<=omega(c)<=1.
```

No new arithmetic weight is introduced: this is only a partition of the exact positive principal mass.

## 2. Deficit strata

For `delta>=0`, stratify cells by

```text
omega(c)=B^(-delta+o(1)).
```

Since the charged-once principal majorant over all cells is `B^(1/2+o(1))`, every fixed-power deficit stratum satisfies

```text
sum M(c) << B^(1/2-delta+o(1)).
```

Hence

```text
PRINCIPAL_DENSITY_DEFICIT_STRATUM_EXPONENT=1/2-delta.
```

Every `delta>0` stratum is strict sub-square-root. Any sequence saturating the current square-root bound must therefore lie in cells with

```text
omega(c)=B^(-o(1)).
```

Equivalently, the physical principal occupancy is near-maximal at fixed-power scale.

## 3. Covariance bookkeeping

The X15 exact triple-centering identity is retained. The localization above does not allow cancellation between the positive principal term and centered covariance terms to be double charged. A strict whole-family theorem on the surviving high-occupancy cells still requires either

```text
(a) a fixed-power deficit inside those cells,
(b) a main-term-scale signed anti-correlation controlling principal plus all covariance terms,
(c) a fresh exact reduction of the high-occupancy cells before absolute values.
```

## 4. Boundary

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PRINCIPAL_DENSITY_DEFICIT_LOCALIZATION_PROVED=true
PRINCIPAL_DENSITY_DEFICIT_STRATUM_EXPONENT=1/2-delta
SQRT_SATURATION_REQUIRES_NEAR_MAXIMAL_CONDITIONAL_OCCUPANCY=true
SATURATING_CELL_OCCUPANCY=B^(-o(1))
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

New receiver:

```text
FullConductorNearMaximalConditionalPrincipalOccupancyJointThreeProjectionSignedCovariance
```

Next: `Stage14-4dk`.

## Stage boundary

```text
STAGE14_4DJ=COMPLETE_FULL_CONDUCTOR_PRINCIPAL_DENSITY_DEFICIT_LOCALIZATION
NEXT=Stage14-4dk
```
