# Stage14-t79 — principal ray density, active-support deficit, and endpoint-small external squareclass split

## Status

`COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION`

Stage14-t79 consumes merged t77 and t78.  It does **not** require the still-unmerged tH22 branch.  The strongest merged whole-family theorem on the starting main is

```text
V(B) << B^(23/44+o(1)).
```

No additional whole-family power saving is claimed here.

The t77/t78 ray-active packet has

```text
K=oddpart(kappa),
K_ext=K/gcd(K,k),
M=K/gcd(K,g*k)=K_ext/gcd(K_ext,g),
G(M)=(Z[i]/MZ[i])^x/(Z/MZ)^x,
|G(M)|=prod_{p|M}(p-chi_4(p)).
```

After fixed beta and reciprocal orientation, the exact ray-class condition is expanded as

```text
1_{[pi]=[U]^-1 I_beta sigma([V])}
 = 1/|G(M)| sum_{chi in G(M)^}
   C_chi(U,beta) chi(pi) conjugate((chi o sigma)(V)).
```

Stage14-t79 separates the principal density term and then stratifies every nonprincipal character by the set of rational primes of `M` on which its local component is nonprincipal.

---

## 1. Exact active-support decomposition

For each odd prime `p|M`, write

```text
g_p := |G(p)| = p-chi_4(p).
```

The local dual group has one principal character and `g_p-1` nonprincipal characters.

For a character `chi in G(M)^`, define its active rational support

```text
d(chi) := product_{p|M, chi_p nonprincipal} p.
```

Because `M` is squarefree, `d(chi)|M`.  For a fixed divisor `d|M`, the number of characters with exact active support `d` is

```text
N_M(d)=prod_{p|d}(g_p-1).
```

Therefore

```text
sum_{d|M} N_M(d)=prod_{p|M} g_p=|G(M)|.
```

This is a purely finite-group identity and does not use Hecke conductor theory.

```text
PROJECTIVE_CHARACTER_ACTIVE_SUPPORT_DECOMPOSITION_PROVED=true
EXACT_SUPPORT_CHARACTER_COUNT=prod_{p|d}(g_p-1)
```

---

## 2. Principal character is exactly the expected projective density

The principal character has

```text
d=1,
N_M(1)=1.
```

Its normalized coefficient is exactly

```text
1/|G(M)|.
```

Since

```text
|G(M)|=prod_{p|M}(p-chi_4(p))=M*B^o(1),
```

this is

```text
M^(-1) B^o(1).
```

The principal character carries no Gaussian-prime or cover oscillation.  It is therefore not part of the nonprincipal large-sieve contract: it is precisely the expected projective root-line density already visible in t76/t77.

This statement does not by itself close the whole physical count; it says that the principal term requires no external character theorem and must be charged only once as the density term.

```text
PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY=true
PRINCIPAL_RAY_CHARACTER_NORMALIZED_WEIGHT=1/|G(M)|
PRINCIPAL_RAY_CHARACTER_REQUIRES_LARGE_SIEVE=false
PRINCIPAL_DENSITY_DOUBLE_CHARGE_FORBIDDEN=true
```

---

## 3. Support-deficit suppression

Let

```text
e=M/d.
```

Call `e` the inactive-support deficit.  From the exact support count,

```text
N_M(d)/|G(M)|
 = prod_{p|d}(g_p-1)/g_p
   * prod_{p|e} 1/g_p
 <= 1/|G(e)|.
```

For squarefree odd `e`,

```text
|G(e)|=prod_{p|e}(p-chi_4(p)) >= phi(e)=e*B^(-o(1)).
```

Hence

```text
boxed:
N_M(d)/|G(M)| <= B^o(1)/e.
```

There are only `tau(M)=B^o(1)` support divisors.  Consequently, for every threshold `E`, the total normalized coefficient mass of all characters with

```text
M/d(chi) >= E
```

is

```text
boxed:
<= E^(-1) B^o(1).
```

This suppression is obtained before estimating either the Gaussian-prime sum or the cover sum.  After the t78 Möbius tensorization, taking absolute values costs only another `B^o(1)` divisor multiplicity.

Thus every character missing a fixed-power portion of the ray modulus is automatically power-suppressed.  The genuinely hard family can be restricted to

```text
d(chi)=M/B^o(1),
```

that is, near-full active support.

```text
FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED=true
SUPPORT_DEFICIT_NORMALIZED_MASS_BOUND=E^-1*Bo1
HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT=true
```

---

## 4. Relation with tH22 conductor language

The active-support argument above is independent of tH22 and is valid on merged main.

The live tH22 audit reports, on its own branch, that the finite Hecke conductor of a projective character with active support `d` is `(d)` and has norm `d^2`.  Stage14-t79 does not import that unmerged result as a predecessor.  If tH22 is merged, its conductor variable is exactly the active-support variable used here.

Therefore t79 predicts that the only Hecke-conductor regime which could still require a hybrid theorem is the near-maximal regime

```text
d=M/B^o(1),
N f_fin(chi)=M^2 B^o(1).
```

No conductor theorem is needed for the t79 finite-group suppression itself.

```text
TH22_HARD_PREDECESSOR_REQUIRED=false
TH22_ACTIVE_SUPPORT_COMPATIBILITY=true
```

---

## 5. Endpoint-small external squareclass branch

Merged t78 gives

```text
M=K_ext/gcd(K_ext,g).
```

Hence

```text
K_ext=B^o(1) => M=B^o(1).
```

In this endpoint-small ray-modulus regime,

```text
|G(M)|=B^o(1).
```

Therefore the complete ray-character expansion has only `B^o(1)` terms.  No ray-character large sieve is required merely to impose the projective class condition: one may expand all characters at endpoint-small cost.

This does **not** prove a new power saving for the underlying balanced physical cover.  It removes the ray-family/conductor obstruction and leaves a separate character-finite physical receiver:

```text
SharedUEndpointSmallExternalKappaBalancedPhysicalCoverEnergy.
```

The exact radial-only case `M=1` is its principal-only endpoint.  Fixed-power `K_ext` radial-only packets remain subsumed by t75 large-`g`, as proved in t78.

```text
ENDPOINT_SMALL_EXTERNAL_KAPPA_IMPLIES_ENDPOINT_SMALL_RAY_GROUP=true
ENDPOINT_SMALL_RAY_GROUP_CHARACTER_ENUMERATION_COST=Bo1
ENDPOINT_SMALL_EXTERNAL_KAPPA_PHYSICAL_ENERGY_PROVED=false
```

---

## 6. Refined ray-active receiver

For fixed-power `M`, t79 removes:

1. the principal density term;
2. every nonprincipal character with fixed-power inactive-support deficit;
3. the endpoint-small `M` character-family issue.

The remaining analytic ray receiver is therefore

```text
SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy.
```

Equivalently, any future hybrid theorem only needs to address nonprincipal characters satisfying

```text
M=B^(positive power+o(1)),
d(chi)=M/B^o(1),
```

with the t78 four-cell Möbius coefficients and the physical masks

```text
ell canonical,
ell^2>4B,
ell*H*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
balanced primitive cover,
fixed beta/inversion orientation.
```

```text
RAY_ACTIVE_NEAR_FULL_SUPPORT_HYBRID_ENERGY_PROVED=false
```

---

## 7. tH decision

`tH22` has already performed the broad projective ray-character applicability audit and found no off-the-shelf full-mask power saving.  Stage14-t79 only narrows that same kernel to near-full active support; it does not yet produce a new transform or theorem adapter.

Therefore do **not** open tH23 yet.  Stage14-t80 should first exploit the near-full-support condition locally — for example by primitive projective Gauss sums / conductor-exact dualization — and only request tH23 if that produces a genuinely new standard analytic object.

```text
TH22_NEEDED=true
TH22_PR_MERGED_AT_T79_START=false
TH23_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH22=false
NEXT=Stage14-t80
```

---

## 8. Current shared exponent

The strongest merged whole-family theorem remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
CURRENT_GAP_TO_SQRT=1/44
```

Stage14-t79 proves no additional whole-family saving.

---

## Locked boundary

```text
STAGE14_T79=COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION
MERGED_T78_IMPORTED=true
MERGED_T77_IMPORTED=true
PROJECTIVE_CHARACTER_ACTIVE_SUPPORT_DECOMPOSITION_PROVED=true
PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY=true
PRINCIPAL_RAY_CHARACTER_REQUIRES_LARGE_SIEVE=false
FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED=true
SUPPORT_DEFICIT_NORMALIZED_MASS_BOUND=E^-1*Bo1
HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT=true
ENDPOINT_SMALL_EXTERNAL_KAPPA_IMPLIES_ENDPOINT_SMALL_RAY_GROUP=true
ENDPOINT_SMALL_RAY_GROUP_CHARACTER_ENUMERATION_COST=Bo1
ENDPOINT_SMALL_EXTERNAL_KAPPA_PHYSICAL_ENERGY_PROVED=false
RAY_ACTIVE_NEAR_FULL_SUPPORT_HYBRID_ENERGY_PROVED=false
PREFERRED_RECEIVER=SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy
TH22_NEEDED=true
TH22_PR_MERGED_AT_T79_START=false
TH23_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH22=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
T79_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t80
```
