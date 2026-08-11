# Stage14-t115 — exact norm-fiber tower for the weighted physical cofactor core

## Status

`COMPLETE_WEIGHTED_COFACTOR_CORE_NORM_FIBER_TOWER`

Consumes merged `Stage14-t114`, merged `Stage14-t91`, and latest merged main.  No unmerged route output is used as theorem source.

Fix one live fixed-`U` packet and one frozen norm-`k0` Gaussian factor / exceptional finite label permitted by the merged t-route.  On one dyadic primitive cofactor background block `Omega`, Stage14-t114 defines

```text
A_gamma=|P_gamma|/|G(d)|,
H_Omega=sum_{gamma in Omega} A_gamma,
M_Omega=sum_{gamma in Omega} C_U(gamma) A_gamma,
mu_core=M_Omega/H_Omega.
```

Here

```text
C_U(gamma)=P_prim*P_tag*P_cell*P_sign in {0,1}.
```

For fixed packet data the principal prime pool entering `A_gamma` depends on the cofactor only through

```text
n=N(gamma)
```

because its interval is

```text
I_B(n)=
(max(2*sqrt(B),2*h*k0*n), 2B/(h*k0*n)]
```

and `|G(d)|` is packet-fixed.  Thus write this common weight as `A(n)`.

For every represented norm `n` in the dyadic block define

```text
R_n := # {gamma in Omega : N(gamma)=n},
C_n := # {gamma in Omega : N(gamma)=n, C_U(gamma)=1},
rho_core(n):=C_n/R_n     (R_n>0).
```

Then the t114 weighted density has the exact tower identity

```text
H_Omega = sum_n A(n) R_n,
M_Omega = sum_n A(n) C_n
        = sum_n A(n) R_n rho_core(n),

mu_core(Omega)
 = [sum_n A(n)R_n rho_core(n)]/[sum_n A(n)R_n].
```

Therefore the prime principal weight does not create an additional orientation variable inside a fixed norm fiber.  Any power-small `mu_core` must be visible as a power-small weighted average of the exact norm-fiber physical acceptance densities `rho_core(n)`.

This does **not** assert that scalar norms with small `rho_core(n)` are themselves uniformly distributed, nor that the outer weights `A(n)R_n` are regular.  It only separates the scalar norm coordinate from the internal Gaussian orientation fiber without changing the physical measure.

Merged t91 gives

```text
R_n=2^omega_odd(n)*O(1)=B^o(1)
```

for each primitive split-supported norm after finite unit/two-primary conventions.  Thus the individual norm fiber remains subpolynomial, but the set of norms is the polynomial-scale coordinate and must not be discarded.

```text
COFACTOR_PRINCIPAL_WEIGHT_DEPENDS_ONLY_ON_NORM=true
WEIGHTED_COFACTOR_CORE_NORM_FIBER_TOWER_EXACT=true
NORM_FIBER_ORIENTATION_MULTIPLICITY=Bo1
NORM_FIBER_MULTIPLICITY_RECHARGE_FORBIDDEN=true
OUTER_NORM_COORDINATE_REMAINS_POLYNOMIAL_SCALE=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUWeightedPrimitiveNormFiberPhysicalCoreDensity
NEXT_INTERNAL_TARGET=ExceptionalGenericOrientationPhysicalCoreSplit
NEXT=Stage14-t116
```
