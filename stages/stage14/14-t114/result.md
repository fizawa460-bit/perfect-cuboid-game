# Stage14-t114 — weighted cofactor-core density versus selected-class depletion dichotomy

## Status

`COMPLETE_COFACTOR_CORE_DENSITY_OR_PRINCIPAL_SCALE_CLASS_DEPLETION_DICHOTOMY`

Consumes Stage14-t113 on the same batch branch and keeps the charged-once fixed-U packet/physical masks unchanged.

Let `Omega` be one frozen dyadic primitive Gaussian cofactor background block before the ell-independent physical core is imposed.  For each `(a,gamma) in Omega`, retain the t112 principal prime weight

```text
A_gamma=|P_gamma|/|G(d)| >= 0.
```

Define the ambient principal baseline and the physical-core principal mass

```text
H_Omega
 := sum_{(a,gamma) in Omega} A_gamma,

M_Omega
 := sum_{(a,gamma) in Omega}
      C_U(a,gamma) A_gamma.
```

When `H_Omega>0`, define the exact weighted cofactor-core density

```text
mu_core(Omega):=M_Omega/H_Omega in [0,1].
```

The full selected-class count remains

```text
T_Omega=M_Omega+D_Omega.
```

Fix any `delta>0`.  Suppose one seeks a fixed-power bound relative to this charged-once ambient principal baseline,

```text
T_Omega <= B^(-delta) H_Omega.
```

Then there is an exact dichotomy.

### Branch A — physical cofactor core is already power sparse

If

```text
mu_core(Omega) <= B^(-delta/2),
```

then

```text
M_Omega <= B^(-delta/2) H_Omega.
```

The saving source is the ell-independent primitive physical cofactor core `C_U`; projective prime distribution need not be charged.

### Branch B — selected classes must be almost maximally depleted

If instead

```text
mu_core(Omega) > B^(-delta/2),
```

then `M_Omega>0` and

```text
D_Omega
 = T_Omega-M_Omega
 <= B^(-delta)H_Omega-M_Omega
 <= -(1-B^(-delta/2))M_Omega.
```

Thus the selected projective classes must carry a negative discrepancy whose magnitude is asymptotically the entire principal mass.  This is much stronger than ordinary equidistribution or square-root cancellation around the uniform class mean.

Therefore any fixed-power improvement on the fixed-U receiver must prove at least one of

```text
PhysicalCofactorCoreWeightedDensityDeficit
```

or

```text
PhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion.
```

This is a material receiver change from the undifferentiated joint cofactor/projective-prime correlation of t111.  The two branches demand different next steps:

- Branch A: open `C_U(a,gamma)=P_prim*P_tag*P_cell*P_sign` and identify a theorem-compatible or deterministic density deficit;
- Branch B: first expose a structural reason the physical map `(a,gamma)->c(a,gamma)` selects systematically prime-poor classes.  Generic Hecke/projective equidistribution is in the wrong direction and tH26 already gives the relevant negative applicability boundary.

No new tH is opened.  The next internal task is Branch A first, because `C_U` is still an exact merged arithmetic predicate whose components have not yet been jointly decomposed at the polynomial cofactor scale.

```text
WEIGHTED_PHYSICAL_COFACTOR_CORE_DENSITY_DEFINED=true
FIXED_POWER_SAVING_DICHOTOMY_EXACT=true
COFACTOR_CORE_POWER_DEFICIT_BRANCH_EXPOSED=true
SELECTED_CLASS_NEAR_TOTAL_DEPLETION_BRANCH_EXPOSED=true
ORDINARY_EQUIDISTRIBUTION_CANNOT_DISCHARGE_DEPLETION_BRANCH=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUPhysicalCofactorCoreWeightedDensityOrSelectedProjectiveClassNearTotalPrimeDepletion
NEXT_INTERNAL_TARGET=PrimitiveGaussianCofactorPhysicalCoreArithmeticDecomposition
NEXT=Stage14-t115
```
