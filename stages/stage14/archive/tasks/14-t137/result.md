# Stage14-t137 — split long-headroom fixed-residue occupancy by modulus scale and exceptional-character risk

## Status

`COMPLETE_LONG_HEADROOM_MITSUI_SAFE_VERSUS_LARGE_SUBPOLYNOMIAL_MODULUS_SPLIT`

Consumes merged `Stage14-t136`, completed merged `Stage14-tH30`, merged `Stage14-t90` for the exact endpoint-modulus provenance, and merged `Stage14-Work-buX33` as the latest integration boundary.

The live fixed-U receiver is

```text
EndpointShortFixedGaussianResiduePrimeOccupancyDeficit
OR
LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

This stage opens only the long-headroom branch.

Fix the same ordinary Gaussian prime residue

```text
beta_* mod d,
```

and the explicit primitive cofactor set from t135.  For each long-headroom cofactor `z`, put

```text
L_B := 2*sqrt(B),
y_z := X_U/N(z),
y_z >= L_B*B^theta
```

for one fixed small `theta>0`.  The endpoint modulus satisfies, from merged t90,

```text
d | D_{U,beta} | |R_U*S_U|,
gcd(d,ell*k0*N(z))=1,
d=B^o(1).
```

The modulus is fixed across the whole frozen packet, so a modulus-scale split is a packet split, not another inner sum.

## 1. Natural modulus ideal scale over Q(i)

The ordinary congruence condition is modulo the Gaussian ideal

```text
q=(d) subset Z[i],
N(q)=d^2.
```

For prime norm endpoint `y_z`, the ambient Euclidean radius is `X_z=sqrt(y_z)`.  Since on the long branch

```text
log X_z = (1/2+Omega_theta(1))*log B + O(1)
```

at exponent level, any modulus condition of the form

```text
N(q) <= exp(c*sqrt(log X_z))
```

is equivalent, after shrinking a fixed constant, to

```text
d <= exp(c_safe*sqrt(log B))
```

for a fixed sufficiently small `c_safe=c_safe(theta)>0`.

Define the exact packet alternatives

```text
SAFE_MITSUI:
  d <= exp(c_safe*sqrt(log B)),

LARGE_SUBPOLY:
  exp(c_safe*sqrt(log B)) < d = B^o(1).
```

The second range is nonempty at theorem level: `B^o(1)` is strictly broader than `exp(O(sqrt(log B)))`.

```text
LONG_MODULUS_PACKET_SPLIT_EXACT=true
MITSUI_SAFE_MODULUS_THRESHOLD=exp(c_safe*sqrt(logB))
GENUINELY_LARGER_SUBPOLYNOMIAL_MODULUS_RANGE_REMAINS=true
```

## 2. Why the SAFE_MITSUI branch is materially cleaner

On this branch every prime interval has two simultaneous properties:

```text
fixed-power headroom: y_z/L_B >= B^theta,
Gaussian modulus ideal norm: N((d))=d^2 <= exp(O(sqrt(log y_z))).
```

The prime element itself is already in one fixed D4/canonical open sector and one ordinary residue `beta_* mod d`.  Thus the target matches the structural input of Mitsui-type prime-element theorems with congruence and angular/convex restrictions, including modern formulations which retain a possible Siegel secondary term.

There is no longer any cofactor coefficient or moving projective class to adapt.

A theorem audit is still required before charging this as solved, because the possible real exceptional character must be compared quantitatively with the fixed-power-depletion threshold and because the theorem's pseudopolynomial modulus constant must be chosen inside its stated range.

## 3. Exceptional-character risk has one fixed residue sign

For a fixed modulus `(d)`, the relevant prime-element explicit formula may contain at most one real exceptional Hecke character in the classical near-1 zero region.  If such a character exists, its value on the frozen residue/sector class is a fixed sign

```text
sigma_exc in {+1,-1}.
```

The secondary term has the standard schematic sign

```text
principal - sigma_exc * exceptional_term.
```

Hence only `sigma_exc=+1` can suppress the principal term; `sigma_exc=-1` is favorable for lower occupancy.  This is only a sign classification here.  No asymptotic or lower bound is charged until the independent audit.

```text
EXCEPTIONAL_CHARACTER_RESIDUE_SIGN_FIXED=true
EXCEPTIONAL_SIGN_MINUS_IS_DEPLETION_THREAT=false
EXCEPTIONAL_SIGN_PLUS_MAY_SUPPRESS_PRINCIPAL=true
```

## 4. Large subpolynomial range remains genuinely outside this split

For

```text
d > exp(c_safe*sqrt(log B)),
d=B^o(1),
```

the tH30 obstruction is not removed by naming `d=B^o(1)`: the modulus can exceed the pseudopolynomial conductor range of Mitsui/Hecke prime-element PNT technology while still being subpolynomial in `B`.

No modulus average is available, and the packet has one fixed residue.  This branch therefore remains

```text
LongHeadroomLargeSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

## 5. Receiver and H decision

This stage refines but does not yet discharge the long branch.  The next stage should freeze the SAFE_MITSUI theorem target exactly and dispatch a clean-room audit.  The endpoint branch is untouched.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH31_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointShortFixedGaussianResiduePrimeOccupancyDeficitOrLongHeadroomMitsuiSafeFixedResiduePrimeOccupancyOrLongHeadroomLargeSubpolynomialModulusFixedResiduePrimeOccupancyBias
NEXT_INTERNAL_TARGET=MitsuiSafeLongHeadroomFixedGaussianResiduePrimeOccupancyTargetFreeze
NEXT=Stage14-t138
```