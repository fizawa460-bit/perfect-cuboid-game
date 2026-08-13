# Stage14-t82 refinement for tH23

Read `14-t80/th23-target.md` and `14-t81/th23-refinement.md`, but use this file as the newest refinement.

## New exact t82 input

Fix `U=R+iS`, `m=R^2+S^2`. On the t81 hard affine-degenerate branch,

```text
[U]=1 on alpha-tag primes  <=> p|S,
[U]=[i] on beta-tag primes <=> p|R.
```

For

```text
M_alpha=gcd(M,odd(alpha)),
M_beta=gcd(M,odd(beta)),
D_Ubeta=gcd(M_alpha,|S|)*gcd(M_beta,|R|),
```

t82 proves

```text
d_diag | D_Ubeta | |R*S|,
D_Ubeta <= m/2,
d_diag < ell/4 up to B^o(1),
# {d_diag for fixed U} <= tau(|R*S|)=B^o(1).
```

Also, if `M_nsel=M/gcd(M,D_Ubeta)`, then exactly

```text
M_nsel | (M/d)*d_frac.
```

Thus on the hard near-full / nonfractional branch

```text
M_nsel=B^o(1),
M=D_Ubeta*B^o(1).
```

Do not charge a moving modulus-family length. The modulus is a divisor-hosted fixed-U coefficient.

On `d_diag`, the fixed class cancels and the projective incidence is

```text
[pi]=sigma([V]) mod d_diag.
```

So audit only the remaining single-frequency incomplete canonical-prime/short-cover inverse-fraction sum with a fixed divisor modulus.

## Mandatory retained masks

```text
fixed U=R+iS,
d_diag|R*S,
d_diag<=m/2<ell/4 (up to B^o(1)),
primitive single frequency,
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
balanced primitive V=p+iq,
gcd(q-p,q+p) in {1,2},
q-p,q+p<sqrt(ell),
ell*odd(h)*odd(q-p)*odd(q+p)<2B,
h*ell*((q-p)^2+(q+p)^2)<=4B,
ell*delta<=Y_U,
fixed beta tag,
fixed reciprocal/inversion orientation.
```

## Do not reopen

```text
two independent frequencies,
Hecke conductor d^2,
moving modulus averaging,
fixed-power fractional support,
fixed-power affine mismatch support,
fixed-U projective coefficient on d_diag.
```

## Refined requested object

```text
FixedUCoordinateDivisorModulusSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve
```

Audit fixed-modulus incomplete Kloosterman/inverse-fraction estimates, DI/Kuznetsov/Bettin-Chandee style bounds, Poisson/spectral duality, and canonical-Gaussian-prime weighted variants under the exact lengths and masks above.

Required final fields should include

```text
T82_FIXED_U_SELECTOR_DIVISOR_RETAINED=...
MOVING_MODULUS_FAMILY_LENGTH_REOPENED=false
TWO_FREQUENCY_LENGTH_REOPENED=false
FIXED_DIVISOR_MODULUS_RANGE_RETAINED=...
PURE_PI_V_PROJECTIVE_RELATION_RETAINED=...
FULL_PHYSICAL_MASKS_RETAINED=...
OFF_THE_SHELF_FIXED_DIVISOR_SINGLE_FREQUENCY_POWER_SAVING_PROVED=...
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=...
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=...
STRICT_SUBSQRT_POWER_SAVING_PROVED=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
TH24_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<latest main>
NEXT=Stage14-t83
```

Record the complete tH23 specification/result in the repo so the chat-to-chat handoff can stay short.
