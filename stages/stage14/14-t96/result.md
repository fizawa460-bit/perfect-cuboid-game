# Stage14-t96 — orientation-bit influence localization on the antipodal quotient

## Status

`COMPLETE_ANTIPODAL_QUOTIENT_INFLUENCE_LOCALIZATION`

Stage14-t96 consumes merged Stage14-t95 and the completed frozen Stage14-tH26 snapshot. No H target is reopened.

The whole-family ledger remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Imported t95 quotient occupancy kernel

On the antipodal quotient `Omega={+-1}^r/{+-1}`, let `f:Omega->{0,1}` be normalized physical occupancy with mean `mu=E f`. Merged t95 proves

```text
sum_{chi!=1}|fhat(chi)|^2 = Var(f) = mu*(1-mu).
```

All odd Walsh modes were already removed in t93/t94.

## 2. Coordinate influences

Choose any Boolean chart of the quotient by fixing one orientation bit as gauge. For each remaining generic split-prime bit `p`, define

```text
Inf_p(f)=P_x[f(x)!=f(x^p)].
```

For Boolean `f`, the discrete Poincare/Efron-Stein inequality gives

```text
Var(f) <= (1/4) sum_p Inf_p(f),
```

hence

```text
sum_p Inf_p(f) >= 4*mu*(1-mu).
```

## 3. Consequence for the t95 survivor

The t95 square-root-saturating survivor has

```text
mu=B^(-o(1)),
1-mu=B^(-o(1)).
```

Therefore `Var(f)=B^(-o(1))` and `sum_p Inf_p(f)=B^(-o(1))`. Since `r=omega(delta_G)<=B^o(1)`, at least one generic split prime satisfies

```text
Inf_p(f)>=B^(-o(1)).
```

Thus a saturating sequence cannot have every generic orientation bit asymptotically invisible.

```text
ALL_GENERIC_ORIENTATION_BITS_ALMOST_INVISIBLE_AT_SATURATION=false
SATURATION_FORCES_A_NONNEGLIGIBLE_GENERIC_ORIENTATION_INFLUENCE=true
```

## 4. Arithmetic meaning

Flipping the `p` bit replaces the full Gaussian prime-power factor `varpi_p^e` by its conjugate while all exceptional data and all other generic bits stay fixed. Hence non-negligible influence means this one local conjugation changes physical acceptance on a `B^{-o(1)}` fraction of quotient fibers. Because t91 already localized fixed packet tags away from generic primes, the surviving effect must be genuinely global: reconstructed sign/positivity, canonical orientation, or another residual cross-prime selector.

Current receiver:

```text
SharedUCanonicalLPF
ExponentZeroIntermediateOccupancy
SingleGenericSplitPrimeInfluenceBoundary
```

## 5. Limits

No fixed-power lower bound for an influence is proved, hence no fixed-power packet saving. KKL/Friedgut is not charged as a power-saving theorem.

```text
FIXED_POWER_INFLUENCE_LOWER_BOUND_PROVED=false
FIXED_POWER_PACKET_SAVING_PROVED=false
```

## 6. H decision

```text
TH26_COMPLETE_CONSUMED=true
TH26_TARGET_REOPENED=false
TH27_NEEDED=false
```

A new H is deferred until the influential-bit event becomes a concrete arithmetic congruence/interval or theorem-compatible influence/noise estimate retaining all physical masks.

## Frozen boundary

```text
STAGE14_T96=COMPLETE_ANTIPODAL_QUOTIENT_INFLUENCE_LOCALIZATION
T95_VARIANCE_IDENTITY_RETAINED=true
ANTIPODAL_QUOTIENT_RETAINED=true
ODD_WALSH_SECTOR_REOPENED=false
POINCARE_EFRON_STEIN_APPLIED=true
SUM_GENERIC_INFLUENCE_LOWER_BOUND=4*mu*(1-mu)
SATURATION_FORCES_A_NONNEGLIGIBLE_GENERIC_ORIENTATION_INFLUENCE=true
ALL_GENERIC_ORIENTATION_BITS_ALMOST_INVISIBLE_AT_SATURATION=false
FIXED_POWER_INFLUENCE_LOWER_BOUND_PROVED=false
FIXED_POWER_PACKET_SAVING_PROVED=false
TH27_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-t97
```
