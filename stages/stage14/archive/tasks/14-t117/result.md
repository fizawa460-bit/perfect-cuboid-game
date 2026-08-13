# Stage14-t117 — local-support / generic-orientation / selected-class depletion trichotomy

## Status

`COMPLETE_FIXED_U_THREE_MECHANISM_POWER_SAVING_TRICHOTOMY`

Consumes Stage14-t116 on the same batch branch and merged Stage14-t114.

Use the exact t115 norm-fiber tower and t116 coordinates `(n,e,epsilon)`.  Let the charged-once ambient principal mass be

```text
H
 = sum_{n,e,epsilon} A(n),
```

with the exact finite/O(1) representation multiplicities understood.  Define the exceptional-local admissible mass

```text
H_loc
 = sum_{n,e,epsilon} A(n) L_U(n;e),
```

and the full ell-independent physical-core mass

```text
M_core
 = sum_{n,e,epsilon}
     A(n) L_U(n;e) S_U(n;e,epsilon).
```

When the denominators are nonzero set

```text
lambda_loc := H_loc/H,

sigma_gen := M_core/H_loc.
```

Then the t114 weighted core density factors **exactly** as

```text
mu_core = M_core/H = lambda_loc * sigma_gen.
```

Thus the opaque Branch-A condition of t114 has become a product of two separately defined physical densities.

For each locally admissible `(n,e)` also center the generic orientation Boolean exactly:

```text
S_U(n;e,epsilon)
 = sigma_U(n;e) + S_U^circ(n;e,epsilon),

E_epsilon S_U^circ=0,
E_epsilon |S_U^circ|^2
 = sigma_U(n;e)(1-sigma_U(n;e)).
```

This is bookkeeping, not a saving theorem.  In particular a small centered discrepancy cannot be charged independently of the positive mean `sigma_U`; a generic-orientation fixed-power deficit means the **principal acceptance density itself** is power-small on the charged physical background.

Now suppose, as in t114, that one seeks

```text
T <= B^(-delta) H
```

for a fixed `delta>0`, where `T=M_core+D` includes the selected-projective-class discrepancy `D`.

Merged t114 gives the first dichotomy:

```text
mu_core <= B^(-delta/2)
```

or

```text
D <= -(1-B^(-delta/2)) M_core.
```

On the first branch, since

```text
mu_core=lambda_loc*sigma_gen,
```

one must have at least one of

```text
lambda_loc <= B^(-delta/4)
```

or

```text
sigma_gen <= B^(-delta/4).
```

Therefore every fixed-power improvement of the current fixed-U receiver must come from at least one of exactly three mechanisms:

```text
(A) ExceptionalLocalAdmissibleNormSupportWeightedDensityDeficit,
(B) GenericSplitPrimeOrientationPhysicalPrincipalDensityDeficit,
(C) PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

The thresholds `delta/4` are only a convenient symmetric split; any fixed partition of the exponent gives the same structural conclusion.

This is a material receiver change.  The earlier undifferentiated `PhysicalCofactorCoreWeightedDensity` branch is no longer minimal.

No one of (A)--(C) is proved here.  Existing merged tH26/tH28 negative certificates do not settle (A) or (B), and ordinary prime-class equidistribution is already known from t113 to point in the wrong direction for (C).  A new H audit would therefore be premature until one of the three mechanisms is opened into a theorem-compatible arithmetic object.

The next internal priority is (A): explicitly describe which scalar norms admit any exceptional-local label.  Only after that support is understood should the route decide whether the generic orientation mean requires a new Fourier/spin/dispersion audit.

```text
LOCAL_ADMISSIBLE_WEIGHTED_DENSITY_DEFINED=true
GENERIC_ORIENTATION_PRINCIPAL_DENSITY_DEFINED=true
WEIGHTED_CORE_DENSITY_FACTORIZATION_EXACT=true
GENERIC_ORIENTATION_PRINCIPAL_CENTERED_SPLIT_EXACT=true
CENTERED_ORIENTATION_TERM_RECHARGE_FORBIDDEN=true
FIXED_U_THREE_MECHANISM_SAVING_TRICHOTOMY_PROVED=true
RECEIVER_MATERIALLY_CHANGED=true
EXCEPTIONAL_LOCAL_NORM_SUPPORT_DEFICIT_PROVED=false
GENERIC_ORIENTATION_PRINCIPAL_DENSITY_DEFICIT_PROVED=false
SELECTED_CLASS_NEAR_TOTAL_DEPLETION_PROVED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=false
PREFERRED_RECEIVER=SharedUExceptionalLocalNormSupportDeficitOrGenericOrientationPrincipalDensityDeficitOrSelectedClassNearTotalDepletion
NEXT_INTERNAL_TARGET=ExceptionalSupportNormAdmissibilityArithmeticDecomposition
NEXT=Stage14-t118
```
