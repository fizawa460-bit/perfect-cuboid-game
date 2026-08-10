# Stage14-t81 refinement for tH23

The original t80 target

```text
NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve
```

is sharpened by t81 before any external theorem adapter is applied.

## Do not reopen

The following are already closed internally:

```text
principal ray character,
fixed-power inactive character support,
fixed-power additive zero-frequency support,
Hecke conductor d^2 versus rational additive modulus d,
local projective-character Fourier transform,
two-frequency independence.
```

## Exact t81 graph kernel

Fix the t80 packet and support `d=M/B^o(1)`.  Primewise the fixed t77 class relation is

```text
x_pi=tau_{c_p,s_p}(x_V),

tau_{c,s}(y)=(c+s*y)/(1-s*c*y),
```

or `tau_{infty,s}(y)=-s/y`.

After resumming the local nonprincipal character family, the normalized Fourier kernel is the Fourier transform of this one Mobius graph.

For primitive local frequencies:

```text
c_p != 0 or infinity
  => genuine Kloosterman graph
  => normalized size <= p^(-3/2)*B^o(1),

c_p = 0
  => tau(y)=s_p*y.
```

At affine primes:

```text
p == 3 mod4 and b != s_p*a mod p
  => kernel = 0,

p == 1 mod4 and b != s_p*a mod p
  => extra p^-1 gain relative to matched scale.
```

Define

```text
d_frac = product_{p|d : C_p != identity} p,
d_mis  = product_{p|d/d_frac : b != s_p*a mod p} p.
```

Then

```text
|K_d(a,b)|
 <= d^-1*d_frac^-1/2*d_mis^-1*B^o(1).
```

Therefore fixed-power `d_frac` or `d_mis` is already saved locally.  The hard branch satisfies

```text
d_frac=B^o(1),
d_mis=B^o(1),
d_diag=d/B^o(1),
b=s_d*a mod d_diag,
s_d^2=1 mod d_diag.
```

For fixed primitive `a`, only `B^o(1)` values of `b` remain.

The affine-degenerate support has exact arithmetic meaning

```text
C_p=[U]^-1 I_beta,p = identity
<=> [U]=I_beta,p.
```

Hence it is beta-selected fixed-`U` coordinate support, not a new moving modulus.

## Refined tH23 object

```text
AffineDegenerateAlmostDiagonalSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve
```

Please audit only the remaining matched single-frequency physical sum.  In particular, do not charge a second independent additive-frequency length and do not use ambient Hecke conductor norm `d^2` after t80/t81.

The theorem adapter must retain

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
small angular-g four-cell weights,
balanced primitive cover,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell*odd(h)*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
fixed beta sign rule,
fixed reciprocal/inversion orientation,
d_diag=d/B^o(1),
primitive single frequency a,
b=s_d*a mod d_diag.
```

Candidate technologies to audit now include fixed-modulus incomplete Kloosterman/inverse-fraction large sieve, Deshouillers-Iwaniec style spectral estimates, bilinear forms with Kloosterman fractions, Bettin-Chandee type bounds, Poisson/Kuznetsov after the frequency collapse, and canonical-Gaussian-prime weighted variants.

Do not mark a theorem applicable unless its variable lengths, rational modulus `d_diag`, frequency range, prime weight, cover coefficient sequence, and all sharp physical hyperbolas match.

Expected tH23 final fields should include

```text
T81_GRAPH_RESUMMATION_RETAINED=...
TWO_FREQUENCY_LENGTH_REOPENED=false
HECKE_CONDUCTOR_D2_REOPENED=false
FRACTIONAL_FIXED_POWER_SUPPORT_REOPENED=false
AFFINE_MISMATCH_SUPPORT_REOPENED=false
SINGLE_FREQUENCY_MATCHED_LINE_RETAINED=...
CANONICAL_PRIME_MASK_RETAINED=...
SHORT_COVER_MASK_RETAINED=...
FULL_PHYSICAL_MASKS_RETAINED=...
OFF_THE_SHELF_SINGLE_FREQUENCY_POWER_SAVING_PROVED=...
CERTIFIED_SINGLE_FREQUENCY_B_POWER_SAVING_EXPONENT=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
TH24_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=...
NEXT=Stage14-t82
```
