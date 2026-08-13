# Stage14-4eg — common-core scale stratification and root-line principal/centered split

## Status

`COMPLETE_COMMON_CORE_SCALE_STRATIFICATION_AND_PRINCIPAL_CENTERED_ROOT_DECOMPOSITION`

Consumes merged `Stage14-4ef`, merged `Stage14-sH71`, merged `Stage14-s7-71`, merged `Stage14-4ec/4ed`, and latest main `eb93b1c3ca28637c2d3dd3ffead4271cb3e56478`. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Consume the negative sH71 verdict

Merged sH71 proves no surveyed theorem directly gives a fixed-power conditional saving for

```text
C0 | X0^2+Y0^2,
gcd(X0,Y0)=1,
gcd(C0,X0Y0)=1,
```

on the canonical-allocation-conditioned candidate family. It explicitly recommends stratifying by the actual common-core scale and separating principal root-line density from centered discrepancy.

Write on one dyadic common-core block

```text
C0 = B^(kappa+o(1)),
0 <= kappa <= O(1).
```

The squarefree split-supported physical packet has

```text
R(C0) := {i mod C0 : i^2 == -1 mod C0},
|R(C0)| = 2^omega(C0) = B^o(1).
```

Among unit ratios modulo `C0`, the exact model principal density is

```text
rho(C0) = |R(C0)|/phi(C0).
```

Using the standard subpolynomial loss in `C0/phi(C0)` and `2^omega(C0)`, one has

```text
rho(C0)=C0^(-1+o(1))=B^(-kappa+o(1)).
```

Thus:

```text
kappa=0:
  rho(C0)=B^(-o(1));

kappa>0 fixed:
  rho(C0)=B^(-kappa+o(1)).
```

```text
COMMON_CORE_SCALE_PARAMETER_KAPPA_DEFINED=true
ROOT_LINE_PRINCIPAL_DENSITY=rho_C0
POLYNOMIAL_C0_PRINCIPAL_DENSITY_HAS_POWER_LOSS=true
SUBPOLYNOMIAL_C0_PRINCIPAL_DENSITY_HAS_FIXED_POWER_LOSS=false
```

## 2. Exact centered decomposition before absolute values

Let `z=(omega,C0,X0,Y0)` range over the charged-once reciprocal candidate incidence above one canonical allocation-bearing slope. Candidate multiplicity per slope remains `B^o(1)`.

Define

```text
R_root(z)=1_{C0 | X0^2+Y0^2},
Delta_root(z)=R_root(z)-rho(C0).
```

Then exactly

```text
R_root(z)=rho(C0)+Delta_root(z).
```

Summing over any fixed `kappa` block gives

```text
accepted incidence mass
 = principal mass + centered discrepancy mass.
```

No equidistribution is assumed: this is an algebraic decomposition of the exact indicator. The existential slope count is exponent-equivalent to candidate incidence mass because the candidate fiber is `B^o(1)`.

```text
ROOT_INDICATOR_PRINCIPAL_PLUS_CENTERED_DECOMPOSITION_EXACT=true
CANONICAL_BACKGROUND_EQUIDISTRIBUTION_ASSUMED=false
CANDIDATE_INCIDENCE_AND_SLOPE_ACCEPTANCE_EXPONENT_EQUIVALENT=true
```

## 3. Consequence on polynomial common-core blocks

Fix any `epsilon>0`. On a block with

```text
kappa>=epsilon,
```

the principal contribution is at most

```text
B^(-epsilon+o(1))
```

relative to the candidate background. Hence an exponent-zero reciprocal acceptance density on such a block cannot be carried by the principal term alone. It requires exponent-zero positive centered discrepancy.

```text
POLYNOMIAL_COMMON_CORE_SATURATION_REQUIRES_CENTERED_DISCREPANCY=true
PRINCIPAL_TERM_ALONE_CANNOT_SATURATE_FOR_KAPPA_POSITIVE=true
```

This is not yet a discrepancy theorem.

## 4. Consequence on the subpolynomial block

When

```text
C0=B^o(1),
```

the principal root-line density itself is only `B^(-o(1))`. Therefore root spacing alone cannot close the square-root branch on this block, exactly as certified by sH71.

```text
SUBPOLYNOMIAL_COMMON_CORE_ROOT_SPACING_CANNOT_GIVE_FIXED_POWER=true
```

## Boundary

```text
STAGE14_4EG=COMPLETE_COMMON_CORE_SCALE_STRATIFICATION_AND_PRINCIPAL_CENTERED_ROOT_DECOMPOSITION
COMMON_CORE_SCALE_PARAMETER_KAPPA_DEFINED=true
ROOT_INDICATOR_PRINCIPAL_PLUS_CENTERED_DECOMPOSITION_EXACT=true
POLYNOMIAL_COMMON_CORE_SATURATION_REQUIRES_CENTERED_DISCREPANCY=true
SUBPOLYNOMIAL_COMMON_CORE_ROOT_SPACING_CANNOT_GIVE_FIXED_POWER=true
RECIPROCAL_ROOT_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4eh
```
