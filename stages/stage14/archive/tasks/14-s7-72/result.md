# Stage14-s7-72 — common-core scale stratification of the reciprocal root selector

## Status

`COMPLETE_COMMON_CORE_SCALE_STRATIFICATION_OF_CANONICAL_RECIPROCAL_ROOT_SELECTOR`

Consumes merged `Stage14-s7-71`, merged `Stage14-sH71`, merged `Stage14-4ef`, and latest main at batch start.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged sH71 certifies that no audited off-the-shelf root-equidistribution / large-sieve / bilinear / norm-form theorem gives a uniform fixed-power saving for the conditional root event

```text
C0 | X0^2+Y0^2,
gcd(X0,Y0)=1,
gcd(C0,X0Y0)=1,
```

on the canonical allocation background. Its prescribed next internal reduction is to stratify the actual scale of `C0`.

## 1. Dyadic exponent cells for C0

Freeze one canonical allocation type and one reciprocal candidate fiber as in s7-71. Write

```text
C0 = B^(kappa+o(1)),
kappa >= 0.
```

The physical range bounds imply only finitely many fixed-power `kappa` cells plus the subpolynomial cell `kappa=0` on the Stage14 exponent scale.

Define

```text
Omega_kappa
 = {canonical-allocation slopes carrying a charged-once candidate
    with C0=B^(kappa+o(1))}.
```

The `B^o(1)` candidate multiplicity per slope allows one `kappa` cell and one candidate label to be frozen without changing any polynomial exponent.

```text
COMMON_CORE_SCALE_CELL_DEFINED=true
COMMON_CORE_SCALE_FREEZING_COST=Bo1
```

## 2. Exact local root density model

For squarefree odd split-supported `C0`, every prime factor is `1 mod 4` and the frozen orientation selects one of the local roots of `-1`. If all unit pairs modulo `C0` were sampled uniformly, the fixed oriented line

```text
X0 == i_C Y0 (mod C0)
```

would have density

```text
rho_or(C0)=1/phi(C0)
```

up to the already-frozen finite orientation convention; allowing both roots gives `2^omega(C0)/phi(C0)`. Since the physical support is squarefree and `2^omega(C0)=B^o(1)`, both conventions have exponent

```text
rho_root(C0)=C0^(-1+o(1))=B^(-kappa+o(1)).
```

This is a model principal density, not yet a theorem for the correlated physical sequence.

```text
ROOT_LINE_MODEL_PRINCIPAL_EXPONENT=kappa
ROOT_LINE_MODEL_DENSITY=B^(-kappa+o(1))
```

## 3. Subpolynomial versus polynomial common core

Two regimes are forced.

### Small common core

If

```text
kappa=0,
C0=B^o(1),
```

then even the idealized root-line principal density is only

```text
B^(-o(1)).
```

Therefore root spacing or principal local density alone cannot produce a fixed-power saving.

### Polynomial common core

If

```text
kappa>0,
```

then the idealized principal density has a genuine `B^-kappa` factor. A legal power saving would follow if the correlated canonical-allocation candidate sequence were shown to have discrepancy smaller than the ambient count by a compatible fixed power.

```text
SUBPOLYNOMIAL_C0_PRINCIPAL_POWER_SAVING_AVAILABLE=false
POLYNOMIAL_C0_PRINCIPAL_POWER_SAVING_POTENTIALLY_AVAILABLE=true
```

## 4. No theorem claim from the model density

Merged sH71 proves that the canonical allocation background is correlated with `C0,X0,Y0`; no pseudorandomness adapter is available. Hence the model factor `B^-kappa` cannot be charged pointwise or after conditioning without first separating principal mass from centered discrepancy.

Accordingly s7-72 makes no saving claim and does not reuse local Gaussian splitting/orientation.

```text
MODEL_ROOT_DENSITY_CHARGED_AS_THEOREM=false
GAUSSIAN_SPLITTING_RECHARGE_ALLOWED=false
ROOT_ORIENTATION_RECHARGE_ALLOWED=false
```

## 5. Next internal step

For each fixed `kappa` cell, write the root indicator exactly as

```text
1_root = rho_root(C0) + Delta_C0(X0,Y0),
```

with `Delta_C0` centered over primitive unit residue pairs modulo `C0`. Then sum this identity over the actual correlated canonical-allocation sequence before applying absolute values.

This is precisely the sH71 recommended principal-plus-centered decomposition.

## H decision

No new H is opened at s7-72. The merged sH71 audit explicitly requests this internal centered decomposition first.

```text
S7_72_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
RECEIVER_MATERIALLY_CHANGED=false
```

## Boundary

```text
STAGE14_S7_72=COMPLETE_COMMON_CORE_SCALE_STRATIFICATION_OF_CANONICAL_RECIPROCAL_ROOT_SELECTOR
MERGED_SH71_IMPORTED=true
COMMON_CORE_SCALE_CELL_DEFINED=true
ROOT_LINE_MODEL_PRINCIPAL_EXPONENT=kappa
SUBPOLYNOMIAL_C0_PRINCIPAL_POWER_SAVING_AVAILABLE=false
POLYNOMIAL_C0_PRINCIPAL_POWER_SAVING_POTENTIALLY_AVAILABLE=true
MODEL_ROOT_DENSITY_CHARGED_AS_THEOREM=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_72_NEW_AUXILIARY_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
REMAINING_RECEIVER=CommonCoreScaleStratifiedCanonicalAllocationRootLinePrincipalDensityPlusCenteredDiscrepancy
NEXT=Stage14-s7-73
```
