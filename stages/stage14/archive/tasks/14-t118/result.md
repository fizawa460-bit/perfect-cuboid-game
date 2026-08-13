# Stage14-t118 — exceptional-support norm admissibility as multiplier cylinders

## Status

`COMPLETE_EXCEPTIONAL_LOCAL_NORM_SUPPORT_MULTIPLIER_CYLINDER_DECOMPOSITION`

Consumes merged `Stage14-t117`, merged `Stage14-t91`, and merged `Stage14-Work-boX27` from latest main. The Work result is used only for its charged-once support-relocation principle; no global saving is imported into the fixed-U route.

Fix one live fixed-U packet and its merged exceptional support

```text
E_U=rad_odd(2*k0*d*kappa*R*S*A0*B0).
```

For every scalar cofactor norm `n=N(gamma)` write exactly

```text
n=m_E*n_G,
m_E=gcd(n,E_U^infinity),
gcd(n_G,E_U)=1.
```

All odd primes of a primitive Gaussian norm are split, so every odd prime divisor of `n_G` is `1 mod 4`.

Merged t91 proves that every genuinely nontrivial local interaction of a cofactor prime with the frozen packet is supported on `E_U`. Therefore, after the finite two-primary/unit convention is included in the exceptional label, the t116 local predicate can be rewritten as

```text
L_U(n;e)=L_U^E(m_E;e).
```

In particular, changing the generic coprime split-supported factor `n_G` while keeping `m_E` and the exceptional label fixed cannot change the exceptional-local admissibility decision.

Define the admissible exceptional multiplier set

```text
M_U(B)
 := {m_E:
      p|m_E => p|E_U,
      m_E is in the physical scalar-norm range,
      exists e with L_U^E(m_E;e)=1}.
```

Then the locally admissible scalar norms are exactly the union of multiplier cylinders

```text
S_loc(U;B)
 = union_{m in M_U(B)}
     {m*n_G:
       gcd(n_G,E_U)=1,
       every odd p|n_G satisfies p==1 mod 4,
       m*n_G lies in the fixed-U physical norm range}.
```

This is an exact support identity. The full physical norm support is the sub-support obtained by additionally requiring at least one generic orientation to survive the global Boolean predicate `S_U`.

The prime-side principal weight from t115/t117 remains

```text
A(n)=|P_n|/|G(d)|,
```

so the cylinders are weighted by `A(m*n_G)`; no multiplicative separation of this weight is asserted.

The point of this stage is only to remove a false dependence: exceptional-local admissibility is a condition on the exceptional multiplier `m_E`, not a new condition independently resampled along the generic norm coordinate.

```text
EXCEPTIONAL_NORM_FACTOR_DEFINED_AS_EU_SMOOTH_MULTIPLIER=true
GENERIC_NORM_FACTOR_COPRIME_TO_EU=true
EXCEPTIONAL_LOCAL_PREDICATE_DEPENDS_ONLY_ON_EXCEPTIONAL_MULTIPLIER=true
LOCAL_ADMISSIBLE_NORM_SUPPORT_IS_EXACT_MULTIPLIER_CYLINDER_UNION=true
GENERIC_SPLIT_PRIME_NORM_COORDINATE_REMAINS_POLYNOMIAL=true
PRIME_PRINCIPAL_WEIGHT_SEPARATION_PROVED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=false
PREFERRED_RECEIVER=SharedUExceptionalMultiplierCylinderPhysicalNormSupportOrSelectedProjectiveClassNearTotalDepletion
NEXT_INTERNAL_TARGET=ExceptionalMultiplierFamilyComplexityAndScaleFreezing
NEXT=Stage14-t119
```
