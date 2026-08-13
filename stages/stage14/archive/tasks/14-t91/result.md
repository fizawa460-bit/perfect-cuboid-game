# Stage14-t91 — primitive Gaussian orientation hypercube and exceptional-support localization

## Status

`COMPLETE_PRIMITIVE_GAUSSIAN_ORIENTATION_HYPERCUBE_AND_EXCEPTIONAL_SUPPORT_LOCALIZATION`

Stage14-t91 consumes merged Stage14-t90.  The Stage14-tH26 request emitted by t90 is an immutable t90 snapshot under `stages/stage14/H-PROTOCOL.md`; t91 does not edit or refine `stages/stage14/14-t90/th26-target.md`.

The whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

---

## 1. Imported t90 kernel

Fix the packet

```text
(U,epsilon,k,h,kappa,beta),
eta in {1,2},
k0=eta*k,
```

and the reciprocal/inversion orientation.  Merged t90 gives

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
all odd p|Q => p==1 mod 4,
d=B^o(1).
```

The bounded physical weight is a `B^o(1)` linear combination of

```text
chi(pi_ell) * Sigma_U,chi(delta0),

Sigma_U,chi(delta0)
 = sum_{N(gamma)=delta0}^{primitive}
     c_U(gamma) chi(gamma).
```

No multiplicativity of `c_U` is assumed.

```text
MERGED_T90_IMPORTED=true
TH26_TARGET_REOPENED=false
TH26_REFINEMENT_REQUESTED=false
```

---

## 2. Primitive representations are primewise orientation choices

Write

```text
delta0 = 2^e2 * product_j p_j^{e_j},
```

where every odd `p_j` is `1 mod 4`.  Choose once and for all a Gaussian prime

```text
varpi_j * conjugate(varpi_j) = p_j.
```

Let `gamma=u+i v` satisfy

```text
N(gamma)=delta0,
gcd(u,v)=1.
```

For an odd `p_j`, if both `varpi_j` and `conjugate(varpi_j)` divide `gamma`, then their product `p_j` divides `gamma` as a rational Gaussian integer, hence `p_j|u` and `p_j|v`, contradicting primitivity.  Conversely, if the entire exponent `e_j` is placed on exactly one of the two conjugate factors, no rational `p_j` divides both coordinates.

Therefore, up to the finite unit and two-primary convention, every primitive representation is exactly

```text
gamma
 = unit * gamma_2 * product_j varpi_j^(e_j*epsilon_j)
                         conjugate(varpi_j)^(e_j*(1-epsilon_j)),

epsilon_j in {0,1}.
```

Thus the moving Gaussian representation fiber is not a two-dimensional lattice search.  It is the Boolean orientation cube on the distinct odd split-prime divisors of `delta0`.

```text
PRIMITIVE_GAUSSIAN_REPRESENTATION_ORIENTATION_HYPERCUBE_PROVED=true
PRIME_POWER_EXPONENT_SPLITTING_ALLOWED=false
EACH_ODD_SPLIT_PRIME_POWER_HAS_EXACTLY_TWO_PRIMITIVE_ORIENTATIONS=true
PRIMITIVE_REPRESENTATION_ORIENTATION_COUNT=2^omega_odd(delta0)*O(1)
```

Since `2^omega(n)<=tau(n)=B^o(1)` on polynomial-size physical variables, this recovers the t88/t90 `B^o(1)` fiber bound with a sharper exact parameterization.

---

## 3. Primitive-cover condition is automatic on the orientation cube

The defining hypercube consists only of primitive Gaussian representations.  Hence the separate primitive-cover indicator inside the t90 coefficient can be removed from the live orientation sum once the orientation cube is used as the parameter space.

Equivalently, the t90 Möbius expansion remains a valid audit identity, but it is no longer necessary as an analytic moving factor after conditioning on the primitive orientation cube.

```text
PRIMITIVE_COVER_MASK_AUTOMATIC_ON_ORIENTATION_HYPERCUBE=true
PRIMITIVE_MOBIUS_SUM_CHARGED_AS_MOVING_ANALYTIC_VARIABLE=false
```

This does not remove the remaining fixed physical selectors.

---

## 4. Fixed-packet exceptional prime support

The fixed packet contains only polynomial-size integers.  Define the fixed exceptional support

```text
E_U
 = rad_odd(2*k0*d*kappa*R*S*A0*B0),
```

where `R,S` are the fixed coordinates of `U` and `A0,B0` denote the fixed odd direction columns used by the merged four-cell decomposition.  Any equivalent fixed packet product containing the same local bad primes is admissible; only its prime support matters.

The number of divisors and local orientation patterns on `E_U` is

```text
B^o(1).
```

For a split prime `p|delta0` with `p∤E_U`:

- `p` does not change the fixed `(kappa,beta)` denominator tag;
- `p` is absent from the endpoint conductor `d`;
- `p` is absent from the fixed direction-side four-cell support;
- the reciprocal/inversion choice is already fixed globally;
- primitivity is already encoded by the orientation bit.

Thus every genuinely nontrivial local selector interaction of a cofactor prime with fixed packet data is supported on `gcd(delta0,E_U)`.

```text
FIXED_PACKET_EXCEPTIONAL_SUPPORT_DEFINED=true
EXCEPTIONAL_SUPPORT_DIVISOR_COMPLEXITY=Bo1
NONTRIVIAL_FIXED_PACKET_LOCAL_SELECTOR_PRIMES_SUBSET_OF_EU=true
```

No claim is made that the complete coefficient is multiplicative at the good primes: the reconstructed sign/positivity and global canonical orientation may still correlate several orientation bits.

```text
FULL_GOOD_PRIME_COEFFICIENT_MULTIPLICATIVITY_PROVED=false
```

---

## 5. Exceptional/generic orientation split

Factor

```text
delta_E = gcd(delta0,E_U^infinity),
delta_G = delta0/delta_E.
```

Because only the prime support matters and `E_U` is fixed packet data,

```text
# admissible orientation labels on delta_E = B^o(1).
```

After fixing one exceptional orientation label, the remaining sum is over the Boolean cube

```text
{epsilon_p : p|delta_G}.
```

Hence

```text
Sigma_U,chi(delta0)
 = B^o(1)-sum over exceptional labels of
     sum_{epsilon in {0,1}^{omega(delta_G)}}
       C_U(exceptional,epsilon)
       chi(gamma_exceptional * gamma_epsilon),
```

with `|C_U|<=B^o(1)` and all fixed-packet congruence allocations frozen.

This is an exact structural reduction, not an estimate.

```text
EXCEPTIONAL_ORIENTATION_BITS_COST=Bo1
GENERIC_COFACTOR_PARAMETER_IS_SPLIT_PRIME_ORIENTATION_CUBE=true
```

---

## 6. What remains genuinely global

The t91 reduction eliminates coordinate multiplicity and fixed-support local entropy.  The remaining possible obstruction is a global Boolean function on the generic split-prime orientation bits, induced by the reconstructed physical sign/positivity and any residual cross-prime condition not localized on `E_U`.

Therefore the smallest current internal receiver is

```text
SharedUCanonicalLPFGenericSplitPrimeOrientationCubePhysicalCorrelation
```

with outer scalar conditions

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
```

and inner primitive cofactor variable represented by the orientation cube of `delta_G`.

The next internal task is to test whether the remaining Boolean coefficient factors, has bounded Fourier degree, or admits a low-complexity character expansion.  Until that is proved, a fixed-power saving cannot be inferred from the orientation count alone.

```text
T91_FIXED_U_PACKET_POWER_SAVING_PROVED=false
```

---

## 7. H decision

`tH26` remains the immutable t90 snapshot audit.  Stage14-t91 neither reopens nor refines it.

```text
TH26_NEEDED=true
TH26_TARGET_REOPENED=false
TH26_REFINEMENT_REQUESTED=false
TH27_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH26=false
```

If tH26 returns while t91+ continues, its verdict is merged as a t90-snapshot result.  A materially new theorem audit for a later receiver must use tH27.

---

## 8. Global ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T91_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t92
```

---

## Locked boundary

```text
STAGE14_T91=COMPLETE_PRIMITIVE_GAUSSIAN_ORIENTATION_HYPERCUBE_AND_EXCEPTIONAL_SUPPORT_LOCALIZATION
MERGED_T90_IMPORTED=true
PRIMITIVE_GAUSSIAN_REPRESENTATION_ORIENTATION_HYPERCUBE_PROVED=true
PRIME_POWER_EXPONENT_SPLITTING_ALLOWED=false
EACH_ODD_SPLIT_PRIME_POWER_HAS_EXACTLY_TWO_PRIMITIVE_ORIENTATIONS=true
PRIMITIVE_REPRESENTATION_ORIENTATION_COUNT=2^omega_odd(delta0)*O(1)
PRIMITIVE_COVER_MASK_AUTOMATIC_ON_ORIENTATION_HYPERCUBE=true
PRIMITIVE_MOBIUS_SUM_CHARGED_AS_MOVING_ANALYTIC_VARIABLE=false
FIXED_PACKET_EXCEPTIONAL_SUPPORT_DEFINED=true
EXCEPTIONAL_SUPPORT_DIVISOR_COMPLEXITY=Bo1
NONTRIVIAL_FIXED_PACKET_LOCAL_SELECTOR_PRIMES_SUBSET_OF_EU=true
FULL_GOOD_PRIME_COEFFICIENT_MULTIPLICATIVITY_PROVED=false
EXCEPTIONAL_ORIENTATION_BITS_COST=Bo1
GENERIC_COFACTOR_PARAMETER_IS_SPLIT_PRIME_ORIENTATION_CUBE=true
T91_FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH26_NEEDED=true
TH26_TARGET_REOPENED=false
TH26_REFINEMENT_REQUESTED=false
TH27_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH26=false
PREFERRED_RECEIVER=SharedUCanonicalLPFGenericSplitPrimeOrientationCubePhysicalCorrelation
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-t92
```
