# Stage14-tH24 target — primitive binary norm with unique super-square-root largest prime

## Snapshot protocol

This target is prepared by Stage14-t84 under `stages/stage14/H-PROTOCOL.md`.

```text
H_STAGE=Stage14-tH24
SOURCE_STAGE=Stage14-t84
TARGET_FILE=stages/stage14/14-t84/th24-target.md
TARGET_FREEZES_AT_DISPATCH=true
RUNNING_TH24_MAY_CHASE_T85_PLUS=false
TH24_DISPATCHED_BY_T84=false
```

When tH24 is actually dispatched, audit the merged t84 snapshot only. Later t85+ reductions do not modify this request; a materially different later receiver uses tH25.

## Requested object

```text
FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve
```

## Exact input from t84

Fix

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
```

and the fixed reciprocal/inversion orientation. The remaining physical point is encoded by one primitive integer pair `(T,D)` satisfying

```text
N=T^2+D^2,
gcd(T,D)=1,
D=d*j,
d|D_Ubeta|R*S,
# {d for fixed U}=B^o(1).
```

The canonical direction prime is no longer an independent variable:

```text
ell=LPF(N)=LPF_odd(N),
v_ell(N)=1,
ell^2>2N.
```

Put

```text
n=N/ell=k*delta.
```

Then

```text
n<ell/2,
n^2<N/2,
n<sqrt(B/h),
delta<sqrt(B/h)/k,
h*N<=2B,
ell*delta<=Y_U.
```

The determinant quotient retains

```text
0<d*|j|=|D|<=sqrt(2B/h),
min(d,|j|)<=(2B/h)^(1/4),
gcd(T,d)=gcd(T,j)=1.
```

Every odd prime divisor of `N` is `1 mod 4`; `v_2(N)<=1`.

For the canonical representation `ell=x^2+y^2` and fixed orientation sigma, the original primitive cover is reconstructed exactly by

```text
p=(x*T+y*D)/ell,
q=sigma*(y*T-x*D)/ell.
```

Hence the canonical-prime/cover bilinear multiplicity has already been eliminated. Do not reopen it.

## Mandatory physical filters

The theorem adapter must retain, either directly in the counted set or as coefficient/mask restrictions with only `B^o(1)` loss:

```text
fixed U, epsilon, k, h, kappa, beta,
fixed reciprocal/inversion orientation,
d|D_Ubeta|R*S,
#d=B^o(1),
primitive (T,D),
D=d*j,
unique super-square-root LPF ell,
v_ell(N)=1,
n=N/ell=k*delta,
n<sqrt(B/h),
ell*delta<=Y_U,
canonical Gaussian direction convention,
reconstructed V primitive and balanced,
small angular-g four-cell weights,
short ellipse,
sharp ell*odd(h)*odd(r)*odd(t) hyperbola,
fixed beta-tag rules.
```

The t78 four-cell Möbius tensorization may be used; its divisor/L2 loss is only `B^o(1)` as already certified by tH23.

## Closed branches — do not reopen

```text
TH23_TARGET_REOPENED=false
MOVING_MODULUS_FAMILY_REOPENED=false
TWO_FREQUENCY_LENGTH_REOPENED=false
HECKE_CONDUCTOR_D2_REOPENED=false
CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
FIXED_POWER_INACTIVE_CHARACTER_SUPPORT_REOPENED=false
FRACTIONAL_PROJECTIVE_SUPPORT_REOPENED=false
AFFINE_MISMATCH_SUPPORT_REOPENED=false
```

Do not charge a separate sum over `ell`: in the t84 receiver `ell=LPF(T^2+D^2)`.

## Techniques to audit

Compare, with explicit variable/range adapters where relevant:

1. large-prime-factor results for primitive values of the binary quadratic form `T^2+D^2`;
2. half-dimensional sieve / beta-sieve for sums of two squares with a prescribed large prime factor;
3. Buchstab or Harman decompositions isolating a prime factor `ell>sqrt(2N)`;
4. Gaussian-integer prime-factor distribution in sectors/progressions;
5. Bombieri--Vinogradov / Barban--Davenport--Halberstam type results over `Z[i]` if they can retain the vertical divisor `d|D`;
6. bilinear forms obtained after writing `T+iD=pi*W` but **without** reintroducing an independent `pi,V` multiplicity already eliminated by t84;
7. dispersion for primitive lattice points with `D` restricted to a fixed divisor-hosted progression;
8. upper-bound sieve for the short cofactor `n=N/ell<sqrt(B/h)` with fixed factor `k`;
9. largest-prime-factor distribution for quadratic-form values in thin/weighted regions;
10. divisor switching using the quarter-scale dichotomy `min(d,|j|)<=B^(1/4+o(1))`;
11. any Gaussian prime theorem that uses the uniqueness of the prime factor above `sqrt(2N)`;
12. hybrid estimates that preserve the reconstructed balanced-cover and `ell*delta` / `ell*HRT` masks.

## Range ledger that must be explicit

Any `APPLICABLE=true` verdict must identify:

```text
N-scale,
T-range,
D-range,
d-range,
j-range,
cofactor n-range,
prime ell-range,
fixed k,h,U dependence,
primitive gcd condition,
vertical progression/divisor condition,
coefficient L2 norm,
sector/angular restriction if used,
level of distribution,
exceptional-character loss,
Buchstab/sieve remainder,
physical hyperbola losses,
quantifier order.
```

A logarithmic saving is not a certified fixed `B`-power saving.

## Main questions

A. Does an off-the-shelf theorem give a uniform fixed-power saving for this exact primitive binary-norm receiver?

B. If not directly, is there a complete theorem adapter after one standard Buchstab / divisor-switch / Gaussian factorization step while preserving all masks?

C. Can one certify, for a fixed U packet,

```text
packet contribution <= B^(-delta0) * current trivial packet scale
```

with an explicit `delta0>0`?

D. If a fixed-U saving exists, is there a legal uniform summation bridge that cross-promotes it to the whole-family square-root saturation ledger?

Do not update the global exponent unless D is proved.

## Required boundary

At minimum emit

```text
STAGE14_TH24=COMPLETE_...
AUDITED_THROUGH=Stage14-t84
TARGET_FROZEN=true
T84_PRIMITIVE_BINARY_NORM_RETAINED=true
T84_CANONICAL_ELL_AS_LPF_RETAINED=true
T84_SUPER_SQRT_LPF_GAP_RETAINED=true
T84_SHORT_COFACTOR_RETAINED=true
T84_FIXED_U_VERTICAL_DIVISOR_RETAINED=true
T84_PI_V_RECONSTRUCTION_RETAINED=true
CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
FULL_PHYSICAL_MASKS_RETAINED=...
HALF_DIMENSIONAL_SIEVE_APPLICABLE=...
HARMAN_BUCHSTAB_APPLICABLE=...
GAUSSIAN_BV_BDH_APPLICABLE=...
BINARY_QUADRATIC_LARGE_PRIME_FACTOR_THEOREM_APPLICABLE=...
VERTICAL_DIVISOR_DISPERSION_APPLICABLE=...
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=...
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=...
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=...
STRICT_SUBSQRT_POWER_SAVING_PROVED=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
NEXT_H_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=[latest main, but do not alter snapshot target]
```

If negative, isolate one exact minimal obstruction that t85+ can attack internally.

## GitHub deliverables

Record tH24 under

```text
stages/stage14/14-tH24/
```

with at least

```text
result.md
literature/applicability note
deterministic range/adapter audit
frozen boundary
dedicated CI workflow
```

Create branch, commits, Draft PR, run dedicated CI, and mark Ready when the tH24 snapshot result is internally consistent. The H result should merge as a scoped Stage14-t84 snapshot certificate even if t85+ has advanced in parallel, unless Stage14-t84 itself is substantively invalidated.
