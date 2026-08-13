# Stage14-t130 — real projective characters are blind to generic Gaussian orientation

## Status

`COMPLETE_REAL_PROJECTIVE_CHARACTER_ORIENTATION_BLINDNESS_AND_SCALARIZATION`

Consumes Stage14-t129 on the same batch branch together with merged `Stage14-t125/t127`, merged `Stage14-t91/t118`, and completed merged `Stage14-tH29` as a negative theorem boundary.

Fix one long-headroom branch from t128 and one nontrivial real/order-two character

```text
chi in G(d)^,
chi^2=1,
G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x.
```

For every invertible Gaussian residue class `z`, the projective quotient gives

```text
[z]*[conj(z)]=[N(z)]=1,
```

because `N(z)` is rational. Hence

```text
[conj(z)]=[z]^(-1).
```

Applying a real character,

```text
chi([conj(z)])
 = chi([z])^(-1)
 = chi([z]),
```

since `chi([z]) in {+1,-1}`.

## 1. Generic orientation bits disappear from a real character

Freeze the t118 exceptional multiplier/orientation label and write

```text
gamma=gamma_E*gamma_G,
N(gamma_G)=n_G=prod_p p^(e_p),
```

where every generic odd prime `p` is split and coprime to the exceptional support. For a chosen Gaussian prime `varpi_p|p`, a primitive generic representation chooses either

```text
varpi_p^(e_p)
```

or

```text
conj(varpi_p)^(e_p).
```

For real `chi`, the two choices have exactly the same character value. Therefore

```text
chi([gamma_G])
```

depends only on the scalar generic norm `n_G`, not on any generic orientation bit.

Define the well-defined scalar phase

```text
xi_chi(n_G)
 := prod_{p^e || n_G} chi([varpi_p])^e
 in {+1,-1}.
```

Changing the chosen `varpi_p` to its conjugate does not change this definition. On the split-prime semigroup coprime to the frozen exceptional support, `xi_chi` is completely multiplicative.

Thus, for the fixed exceptional label,

```text
chi([gamma])
 = chi([gamma_E]) * xi_chi(n_G).
```

```text
REAL_PROJECTIVE_CHARACTER_CONJUGATION_INVARIANT=true
REAL_PROJECTIVE_CHARACTER_GENERIC_ORIENTATION_BLIND=true
REAL_PROJECTIVE_CHARACTER_SCALAR_NORM_PHASE_DEFINED=true
REAL_PROJECTIVE_SCALAR_PHASE_COMPLETELY_MULTIPLICATIVE_ON_GENERIC_SPLIT_SUPPORT=true
```

## 2. Exact scalarized long-headroom coefficient

Let

```text
W_phys(n)
 := #{gamma in Omega_nb,long : N(gamma)=n}
```

inside the already frozen exceptional packet. Merged fixed-norm/orientation bounds give

```text
0<=W_phys(n)<=B^o(1).
```

Because the real character is constant across every generic orientation above the same scalar norm,

```text
sum_{gamma in Omega_nb,long, N(gamma)=n} chi([gamma])
 = W_phys(n)
   * chi([gamma_E])
   * xi_chi(n_G).
```

Define the prime-side cumulative real Hecke sum

```text
P_chi(y)
 := sum_{
      pi_ell canonical split,
      L_B<ell<=y
    }
    chi([pi_ell]).
```

Then the exact t127 real-character hyperbola contribution is

```text
D_chi,long
 = chi([a]) chi([gamma_E])
   * sum_n
       W_phys(n) xi_chi(n_G)
       P_chi(X_U/n),
```

with the t128 long-headroom restriction retained on `n`.

Therefore branch (B) is not a Gaussian orientation-correlation problem. Its only cofactor dependence is a scalar norm weight

```text
W_phys(n) xi_chi(n_G),
```

against a real projective-Hecke prime cumulative sum.

## 3. What this does and does not solve

This scalarization removes one possible obstruction but does not prove cancellation:

- `W_phys(n)` is only bounded by `B^o(1)` and is not proved multiplicative;
- `xi_chi(n_G)` is multiplicative but can correlate with `W_phys(n)`;
- tH29 does not uniformly exclude an exceptional real Hecke zero for the allowed `d=B^o(1)` family;
- a principal-scale bias may therefore still survive on the long-headroom branch.

So the real branch is sharpened to

```text
LongHeadroomRealProjectiveHeckePrimeBiasAgainstScalarPhysicalNormWeight.
```

No new literature audit is justified: the same possible exceptional real Hecke bias was already part of the frozen tH29 negative verdict, while the newly exposed scalar weight still requires internal arithmetic opening before a fresh theorem target would differ materially.

```text
REAL_BRANCH_GAUSSIAN_ORIENTATION_CORRELATION_REMAINS=false
REAL_BRANCH_SCALAR_PHYSICAL_NORM_WEIGHT_REMAINS=true
REAL_EXCEPTIONAL_ZERO_BOUNDARY_RETAINED=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH30_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointCornerWedgeProjectivePrimeDepletionOrLongHeadroomRealHeckePrimeBiasAgainstScalarPhysicalNormWeightOrLongHeadroomNonrealProjectiveCofactorBilinearCorrelation
NEXT_INTERNAL_TARGET=NonrealProjectiveCharacterNormFiberOrientationCoefficientOpening
NEXT=Stage14-t131
