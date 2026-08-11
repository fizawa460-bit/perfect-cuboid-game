# Stage14-t125 — freeze the nonboundary cofactor-to-projective-class map and nested prime interval

## Status

`COMPLETE_NONBOUNDARY_PROJECTIVE_CLASS_MAP_AND_NESTED_PRIME_INTERVAL_FREEZE`

Consumes merged `Stage14-t124`, merged `Stage14-t109/t112`, and merged `Stage14-Work-bqX29` from latest merged main.

Fix one live fixed-`U` packet

```text
(U,epsilon,k,h,kappa,beta,eta),
k0=eta*k,
```

one allowed norm-`k0` Gaussian factor `a`, one admissible exceptional packet from t118--t124, and one canonical nonboundary physical primitive cofactor

```text
gamma in Z[i],
n=N(gamma),
gcd(Re gamma,Im gamma)=1.
```

All finite/unit/exceptional labels are already charged once.  By t124, the only live fixed-`U` saving mechanism is selected projective-class near-total prime depletion.

The endpoint modulus and selected class are exactly

```text
d=B^o(1),
G=G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x,

c(gamma)=([gamma][a])^(-1) in G.
```

The dominant split prime `ell` is accepted exactly when

```text
[pi_ell]=c(gamma)
```

and its rational norm lies in the t109 physical interval

```text
I_B(n)=
(max(2*sqrt(B),2*h*k0*n), 2B/(h*k0*n)].
```

### Nonempty intervals have a common lower endpoint

If `I_B(n)` is nonempty, then necessarily

```text
2*h*k0*n < 2B/(h*k0*n),
```

hence

```text
(h*k0*n)^2 < B,
h*k0*n < sqrt(B).
```

Therefore on every live nonempty interval

```text
2*h*k0*n < 2*sqrt(B),
```

and the max in the lower endpoint collapses exactly:

```text
I_B(n)=
(2*sqrt(B), 2B/(h*k0*n)].
```

Put

```text
X_U := 2B/(h*k0).
```

Then the moving prime interval is simply

```text
I_B(n)=(2*sqrt(B), X_U/n].
```

Thus all live intervals are nested, have one common lower endpoint, and vary only through the reciprocal upper cutoff `X_U/n`.

### Exact generic-orientation class map

After freezing the exceptional Gaussian factor `gamma_E`, write

```text
gamma=gamma_E*gamma_G.
```

Then

```text
c(gamma)
 = c_E * [gamma_G]^(-1),

c_E:=([gamma_E][a])^(-1).
```

If the generic norm is

```text
g=N(gamma_G)=prod_p p^(e_p)
```

with every odd `p` split and coprime to the fixed exceptional support, choose one canonical Gaussian prime `varpi_p|p`.  A primitive generic orientation chooses, for each `p`, either `varpi_p^(e_p)` or its conjugate.  Since

```text
[conj(varpi_p)]=[varpi_p]^(-1) in G
```

(the rational norm `p` is trivial in the projective quotient), flipping one orientation bit multiplies the **cofactor class** `[gamma_G]` by `[varpi_p]^(-2*e_p)`.  Because the selected class uses the inverse cofactor class, the selected class itself is multiplied by

```text
r_p=[varpi_p]^(2*e_p).
```

Hence, after choosing one base orientation,

```text
c(gamma)
 = c_base * prod_p r_p^(epsilon_p),
epsilon_p in {0,1}.
```

This is an exact finite-group subset-product description of the moving cofactor-to-class map.  No distribution or independence of the orientation bits is asserted.

The prime interval depends only on the scalar norm `n`, while the selected projective class depends on the actual Gaussian cofactor orientation modulo `d`.  These are now frozen as separate exact coordinates.

This stage is an exact coordinate freeze of the t124 receiver; it does not remove or add a saving mechanism, so it is not a material receiver change.

```text
NONBOUNDARY_SELECTED_CLASS_MAP_FROZEN=true
SELECTED_CLASS_EQUALS_INVERSE_COFACTOR_CLASS=true
GENERIC_ORIENTATION_SELECTED_CLASS_SUBSET_PRODUCT_EXACT=true
LIVE_PRIME_INTERVAL_COMMON_LOWER_ENDPOINT=2sqrtB
LIVE_PRIME_INTERVAL_UPPER_ENDPOINT=XU_over_n
LIVE_PRIME_INTERVALS_NESTED=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion
NEXT_INTERNAL_TARGET=SelectedClassNestedPrimeIntervalHyperbolaTransposition
NEXT=Stage14-t126
```
