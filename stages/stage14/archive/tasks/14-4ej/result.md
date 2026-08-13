# Stage14-4ej — exact multiplicative-character expansion of the centered Gaussian root line

## Status

`COMPLETE_CENTERED_ROOT_DISCREPANCY_TO_VARIABLE_MODULUS_CHARACTER_CORRELATION`

Consumes batch-local `Stage14-4eh/4ei` and merged `Stage14-sH71`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Work on the primitive unit-ratio group

For every live candidate on the polynomial common-core branch,

```text
gcd(C0,X0Y0)=1.
```

Hence the ratio

```text
t = X0 * Y0^(-1) mod C0
```

lies in the finite abelian group

```text
G_C=(Z/C0Z)^x.
```

Let

```text
I_C={i in G_C : i^2 == -1 mod C0}.
```

On the squarefree split-supported physical modulus,

```text
|I_C|=2^omega(C0)=B^o(1).
```

The root selector is exactly

```text
1_{C0|X0^2+Y0^2}=1_{t in I_C}.
```

## 2. Exact character Fourier expansion

For a multiplicative character `chi` of `G_C`, define

```text
hat_I_C(chi)=sum_{i in I_C} conjugate(chi(i)).
```

Finite-group Fourier inversion gives exactly

```text
1_{t in I_C}
 = |I_C|/phi(C0)
 + (1/phi(C0))
   sum_{chi != 1} hat_I_C(chi) chi(t).
```

Therefore the centered term from Stage14-4eg is

```text
Delta_root(C0,X0,Y0)
 = (1/phi(C0))
   sum_{chi != 1}
     hat_I_C(chi) chi(X0) conjugate(chi(Y0)).
```

The principal term is exactly the sH71 density

```text
rho(C0)=|I_C|/phi(C0).
```

No approximation and no equidistribution assumption enters this identity.

```text
CENTERED_ROOT_LINE_HAS_EXACT_MULTIPLICATIVE_CHARACTER_EXPANSION=true
PRINCIPAL_CHARACTER_TERM_EQUALS_RHO_C0=true
```

Parseval also gives the exact coefficient identity

```text
sum_chi |hat_I_C(chi)|^2 = phi(C0)*|I_C|.
```

```text
ROOT_SET_CHARACTER_COEFFICIENT_L2_IDENTITY_EXACT=true
```

## 3. Insert the canonical physical candidate weights

On one polynomial common-core dyadic block let `w(z)` be the charged-once nonnegative weight of a physical reciprocal candidate; all canonical-allocation, primitive, dyadic/range/angular, squarefree/coprime, chart and endpoint masks remain inside `w`.

For each exact modulus `C` define

```text
A_C(chi)
 := sum_{z: C0(z)=C}
      w(z) chi(X0(z)) conjugate(chi(Y0(z))).
```

Then the total centered discrepancy is exactly

```text
D_kappa
 = sum_{C in dyadic block}
     (1/phi(C))
     sum_{chi != 1}
       hat_I_C(chi) A_C(chi).
```

Thus polynomial-core square-root saturation forces a large positive **variable-modulus nonprincipal character correlation** of the canonical physical candidate sequence.

```text
POLYNOMIAL_CORE_DISCREPANCY_IS_VARIABLE_MODULUS_CHARACTER_CORRELATION=true
ALL_PHYSICAL_MASKS_RETAINED_IN_CHARACTER_WEIGHT=true
C0_CANDIDATE_CORRELATION_RETAINED=true
```

## 4. Why this is not yet an off-the-shelf character-sum theorem

The modulus `C` is not an independent averaging variable: it is reconstructed from the same canonical allocation witness as `(X0,Y0)`. Moreover the exact physical weight has not been factored into separated coefficient sequences.

Therefore the character identity does not by itself supply cancellation, and the negative sH71 applicability verdict remains respected.

```text
CHARACTER_EXPANSION_ITSELF_GIVES_POWER_SAVING=false
VARIABLE_MODULUS_WEIGHT_SEPARATION_PROVED=false
```

## 5. Next internal step

Before opening a new discrepancy H, square the exact character receiver and inspect what its second moment actually counts. Orthogonality should distinguish repeated/heavy exact moduli from a diffuse correlated-modulus graph; treating those as one collision family would be unsafe.

```text
NEW_H_TRIGGERED_BY_4EJ=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4EJ=COMPLETE_CENTERED_ROOT_DISCREPANCY_TO_VARIABLE_MODULUS_CHARACTER_CORRELATION
CENTERED_ROOT_LINE_HAS_EXACT_MULTIPLICATIVE_CHARACTER_EXPANSION=true
ROOT_SET_CHARACTER_COEFFICIENT_L2_IDENTITY_EXACT=true
POLYNOMIAL_CORE_DISCREPANCY_IS_VARIABLE_MODULUS_CHARACTER_CORRELATION=true
ALL_PHYSICAL_MASKS_RETAINED_IN_CHARACTER_WEIGHT=true
C0_CANDIDATE_CORRELATION_RETAINED=true
CHARACTER_EXPANSION_ITSELF_GIVES_POWER_SAVING=false
VARIABLE_MODULUS_WEIGHT_SEPARATION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ek
```
