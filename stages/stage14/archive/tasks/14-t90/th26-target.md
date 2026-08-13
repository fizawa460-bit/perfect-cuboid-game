# Stage14-tH26 immutable snapshot target emitted by Stage14-t90

## Snapshot source

```text
PARENT_STAGE=Stage14-t90
PARENT_RECEIVER=SharedUCanonicalLPFPrimitiveGaussianCofactorRepresentationCharacterWeightedPhysicalSieve
H_NUMBER=26
H_TARGET_FROZEN_AT_PARENT_DISPATCH=true
```

Do not mutate this target after tH26 is dispatched.  Later t91+ work must use a new H number if it produces a materially different receiver.

## Fixed packet

Fix

```text
(U,epsilon,k,h,kappa,beta),
eta in {1,2},
k0=eta*k,
```

with reciprocal/inversion orientation fixed.  The scalar variable is

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
delta0=Q/ell,
```

subject to

```text
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
all odd p|Q => p==1 mod 4.
```

The endpoint selector conductor satisfies

```text
d=B^o(1),
gcd(d,ell*k0*delta0)=1.
```

## Gaussian representation weight

For each endpoint projective character `chi` of

```text
G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x,
```

t90 reduces the physical completion weight to

```text
chi(pi_ell) * Sum_U,chi(delta0),
```

where

```text
N(pi_ell)=ell
```

is the canonical Gaussian prime orientation and

```text
Sum_U,chi(delta0)
 = sum_{N(gamma)=delta0}^{primitive}
     c_U(gamma) chi(gamma).
```

The coefficient `c_U(gamma)` retains the exact physical selectors:

```text
fixed kappa/beta denominator tag,
primitive-cover Mobius condition,
angular-gcd/four-cell divisibility allocation,
reciprocal/inversion and positivity orientation,
endpoint-small projective/ring-class condition.
```

The projective character family has size `B^o(1)`.  The full coefficient is not assumed multiplicative.

## Exact audit object

Audit sums of the shape

```text
S(X)=sum_{Q~X}
  1_{ell=LPF(Q),v_ell(Q)=1}
  1_{ell^2>4B}
  1_{ell^2>2*h*k0*Q}
  1_{h*k0*Q<=2B}
  1_{all odd p|Q => p==1 mod 4}
  chi(pi_ell)
  Sum_U,chi(Q/ell).
```

Both the principal endpoint character and all nonprincipal endpoint characters must be audited.  The principal term is positive and cannot be removed by cancellation arguments intended only for nonprincipal characters.

## Questions tH26 must answer

1. Is there an existing theorem giving, uniformly in every fixed physical packet and endpoint-small `d`,

```text
S(X) << X*B^(-delta+o(1))
```

for some absolute/fixed positive `delta` on every physical dyadic range?

2. If not, does existing literature give a power saving after a valid decomposition of `c_U(gamma)` into finitely many multiplicative, Hecke-character, spin, trace-function, or bilinear pieces while retaining all physical masks?

3. Does the principal Gaussian representation term admit any fixed-power density deficit beyond the merely logarithmic sparsity of integers supported on split primes?

4. Can the canonical largest-prime condition `ell=LPF(Q)`, `v_ell(Q)=1`, together with the strong gap `ell^2>2*h*k0*Q`, be combined with Gaussian spin/Hecke estimates without losing uniformity in the short cofactor `delta0`?

5. Are Bombieri--Vinogradov/Barban--Davenport--Halberstam, Gaussian prime, Hecke large-sieve, bilinear Gaussian spin, dispersion, or friable-largest-prime theorems directly applicable to this exact coefficient system?  State precisely which hypotheses fail if not.

6. Give a certified fixed-power exponent only if the theorem applies to the full frozen object above.  Logarithmic gains must not be reported as a positive `B`-power exponent.

## Required verdict fields

```text
STAGE14_TH26=...
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=true|false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=...
PRINCIPAL_REPRESENTATION_TERM_POWER_SPARSE=true|false
NONPRINCIPAL_GAUSSIAN_CHARACTER_SAVING_AVAILABLE=true|false
FULL_PHYSICAL_COEFFICIENT_DECOMPOSITION_THEOREM_READY=true|false
CANONICAL_LPF_SHORT_COFACTOR_UNIFORMITY_CONTROLLED=true|false
PREFERRED_NEXT_INTERNAL_REDUCTION=...
NEXT_H_NEEDED=true|false
```
