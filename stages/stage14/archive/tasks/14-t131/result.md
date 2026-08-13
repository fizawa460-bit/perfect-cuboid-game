# Stage14-t131 — compress the nonreal projective branch to a scalar norm-fiber orientation coefficient

## Status

`COMPLETE_NONREAL_PROJECTIVE_NORM_FIBER_ORIENTATION_COEFFICIENT_COMPRESSION`

Consumes Stage14-t130 on the same batch branch together with merged `Stage14-t91/t116/t125/t127` and completed merged `Stage14-tH29` as a negative theorem boundary.

Fix one long-headroom nonreal character

```text
chi in G(d)^,
chi^2!=1.
```

The exact t127 contribution is

```text
D_chi,long
 = chi([a])
   * sum_{
       gamma in Omega_nb,long,
       pi_ell canonical split,
       ell>L_B,
       N(gamma)*ell<=X_U
     }
     chi([gamma]) chi([pi_ell]).
```

## 1. Norm-fiber compression is exact

For each scalar cofactor norm `n`, define

```text
Omega_n
 := {gamma in Omega_nb,long : N(gamma)=n},

W_phys(n):=|Omega_n|,

A_chi(n)
 := sum_{gamma in Omega_n} chi([gamma]).
```

Merged fixed-norm and orientation-fiber bounds give uniformly

```text
0<=W_phys(n)<=B^o(1),
|A_chi(n)|<=W_phys(n)<=B^o(1).
```

Define again the prime-side cumulative character sum

```text
P_chi(y)
 := sum_{
      pi_ell canonical split,
      L_B<ell<=y
    }
    chi([pi_ell]).
```

Then regrouping by `n=N(gamma)` gives the exact scalar outer sum

```text
D_chi,long
 = chi([a])
   * sum_n A_chi(n) P_chi(X_U/n),
```

with the long-headroom restriction retained on `n`.

No absolute value and no approximation is used.

```text
NONREAL_COFACTOR_NORM_FIBER_COEFFICIENT_DEFINED=true
NONREAL_HYPERBOLA_SCALAR_NORM_COMPRESSION_EXACT=true
NONREAL_NORM_FIBER_COEFFICIENT_SUPNORM=Bo1
```

## 2. Exact orientation-phase form inside one norm fiber

Freeze the exceptional Gaussian label and write

```text
gamma=gamma_E*gamma_G,
N(gamma_G)=n_G=prod_p p^(e_p).
```

Choose one base primitive generic orientation

```text
gamma_0=gamma_E*prod_p varpi_p^(e_p).
```

Flipping the orientation at one split prime `p` changes the projective cofactor class by

```text
[conj(varpi_p)/varpi_p]^(e_p)
 = [varpi_p]^(-2e_p).
```

Hence its character phase changes by

```text
r_{p,chi}
 := chi([varpi_p])^(-2e_p),
|r_{p,chi}|=1.
```

Let `E_phys(n)` be the exact finite set of generic orientation labels which, after the already frozen exceptional/unit/canonical bookkeeping, represent the actual nonboundary physical cofactors in `Omega_n`. Then

```text
A_chi(n)
 = chi([gamma_0])
   * sum_{epsilon in E_phys(n)}
       prod_p r_{p,chi}^(epsilon_p).
```

This is an exact finite subset-product Fourier coefficient on the generic split-prime orientation cube. For nonreal `chi`, the local phases need not equal `1` or `-1`, so unlike t130 the orientation dependence does not disappear.

No product formula for the restricted sum over `E_phys(n)` is asserted. In particular, the canonical/unit representative selection must not be replaced by the full Boolean cube without proof.

```text
NONREAL_ORIENTATION_PHASE_PRODUCT_EXACT=true
NONREAL_ORIENTATION_DEPENDENCE_SURVIVES=true
FULL_ORIENTATION_CUBE_PRODUCT_FORMULA_ASSUMED=false
PHYSICAL_CANONICAL_ORIENTATION_SUBSET_RETAINED=true
```

## 3. The polynomial outer variable is now scalar norm, not Gaussian representation

The inner Gaussian representation/orientation fiber has size only `B^o(1)`. Therefore any principal-scale nonreal obstruction must persist after compression to the polynomial scalar norm family through the bounded coefficients

```text
A_chi(n).
```

The branch is sharpened to

```text
LongHeadroomNonrealProjectiveHeckePrimeCorrelationAgainstPhysicalNormFiberOrientationCoefficient.
```

This does not itself prove a saving. A `B^o(1)` sup norm is bookkeeping, not cancellation; the coefficient may be coherent across polynomially many scalar norms.

The completed tH29 negative verdict remains applicable: no theorem-ready Type-I/Type-II, spin, or multiplicative structure has been proved for the exact sequence `A_chi(n)`. A fresh tH would therefore only re-audit the same missing adapter.

## 4. Material receiver change after t129--t131

All three t128 mechanisms have now been opened to their minimal scalar outer coordinates:

```text
(A) Endpoint reciprocal-hyperbola corner wedge
    0<u<=v<theta
    with projective-prime depletion;

(B) long-headroom real character
    W_phys(n) xi_chi(n_G)
    against the real Hecke prime cumulative sum;

(C) long-headroom nonreal character
    A_chi(n)
    against the nonreal Hecke prime cumulative sum.
```

Thus the live fixed-U obstruction is no longer an opaque Gaussian cofactor/prime bilinear incidence. Its polynomial outer coordinate is explicitly the scalar cofactor norm `n` in every branch; only the arithmetic weight attached to `n` differs.

This is a material receiver change and matches the `t131` revisit point named by merged Work-brX30.

```text
FIXED_U_ALL_LIVE_BRANCHES_SCALAR_NORM_OUTER_COORDINATE=true
ENDPOINT_BRANCH_EXACT_CORNER_WEDGE=true
REAL_BRANCH_GENERIC_ORIENTATION_ELIMINATED=true
NONREAL_BRANCH_INNER_ORIENTATION_COMPRESSED_TO_BO1_COEFFICIENT=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH30_NEEDED=false
PREFERRED_RECEIVER=SharedUScalarNormOuterEndpointCornerWedgeProjectivePrimeDepletionOrLongRealHeckeBiasAgainstPhysicalNormWeightOrLongNonrealHeckeCorrelationAgainstNormFiberOrientationCoefficient
NEXT_INTERNAL_TARGET=ScalarNormPhysicalWeightCommonDecompositionAcrossProjectiveCharacterBranches
NEXT=Stage14-t132
