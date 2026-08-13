# Stage14-tH24 — primitive binary norm / super-square-root LPF applicability audit

## Status

```text
STAGE14_TH24=COMPLETE_T84_SNAPSHOT_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_VERTICAL_DIVISOR_SIEVE_APPLICABILITY_AUDIT
H_STAGE=Stage14-tH24
AUDITED_THROUGH=Stage14-t84
SOURCE_SNAPSHOT_SHA=fa93c79084e05a2f1aa39eeb80b48f2e82f82113
TARGET_FILE=stages/stage14/14-t84/th24-target.md
REQUESTED_OBJECT=FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve
TARGET_FROZEN=true
H_SOURCE_SNAPSHOT_FROZEN=true
```

This is an immutable Stage14-t84 snapshot audit under `stages/stage14/H-PROTOCOL.md`. Later t85+ work is not imported into the mathematical question.

The final applicability verdict is negative: no located off-the-shelf theorem, and no one-standard-step adapter located in the audited literature, gives a uniform fixed `B`-power saving for the full t84 receiver with all physical masks retained.

```text
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

---

## 1. Frozen t84 arithmetic receiver

Fix

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
```

and the reciprocal/inversion orientation. The live point is one primitive pair

```text
(T,D),
gcd(T,D)=1,
N=T^2+D^2,
D=d*j,
d|D_Ubeta|R*S,
# {d for fixed U}=B^o(1).
```

Merged t84 proves that the canonical direction prime is intrinsic to `N`:

```text
ell=LPF(N)=LPF_odd(N),
v_ell(N)=1,
ell^2>2N,
n=N/ell=k*delta,
n<ell/2,
n<sqrt(B/h),
h*N<=2B,
ell*delta<=Y_U.
```

The determinant quotient remains

```text
0<|D|=d*|j|<=sqrt(2B/h),
min(d,|j|)<=(2B/h)^(1/4),
gcd(T,d)=gcd(T,j)=1.
```

Every odd prime factor of `N` is `1 mod 4`, and `v_2(N)<=1`.

The canonical representation `ell=x^2+y^2` and fixed orientation reconstruct the original cover uniquely:

```text
p=(x*T+y*D)/ell,
q=sigma*(y*T-x*D)/ell.
```

Therefore

```text
T84_PRIMITIVE_BINARY_NORM_RETAINED=true
T84_CANONICAL_ELL_AS_LPF_RETAINED=true
T84_SUPER_SQRT_LPF_GAP_RETAINED=true
T84_SHORT_COFACTOR_RETAINED=true
T84_FIXED_U_VERTICAL_DIVISOR_RETAINED=true
T84_PI_V_RECONSTRUCTION_RETAINED=true
CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
NO_SEPARATE_ELL_SUM=true
```

---

## 2. The super-square-root LPF condition is not by itself a power-sparse event

The inequality

```text
ell^2>2N
```

makes `ell` unique and makes the cofactor short. It does not create an additional independent density factor after `ell=LPF(N)` has been substituted.

In particular, the receiver contains the prime-norm subcase

```text
N=ell,
n=1
```

whenever the fixed packet permits `k=1` and the remaining physical masks. More generally, for fixed admissible cofactor `n`, the arithmetic shape `N=ell*n` still has one large split prime variable. Thus the LPF condition alone cannot be charged as a second prime choice or as a factor `ell^{-1}`.

```text
SUPER_SQRT_LPF_UNIQUENESS_RETAINED=true
SUPER_SQRT_LPF_DENSITY_DOUBLE_CHARGE_FORBIDDEN=true
AUTOMATIC_LPF_FIXED_POWER_SAVING=false
```

A sieve saving must come from interaction with the vertical divisor/progression, the cofactor, or the reconstructed physical masks.

---

## 3. Half-dimensional / beta-sieve audit

The primitive sum-of-two-squares support is naturally half-dimensional: odd prime divisors are restricted to split primes `1 mod 4`, and standard half-dimensional sieve ideas are relevant for upper bounds and almost-prime decompositions.

However the t84 target is not merely

```text
P^-(T^2+D^2)>z
```

or primality of a binary quadratic form. It requires simultaneously

```text
LPF(N)=ell,
ell^2>2N,
n=N/ell=k*delta,
D=d*j with d|R*S,
ell*delta<=Y_U,
```

plus reconstructed balanced-cover, four-cell, short-ellipse and sharp-hyperbola masks.

A classical upper-bound beta-sieve can organize small-prime exclusions and gives logarithmic-density factors, but no located theorem turns those factors into a uniform fixed `B^{-delta}` gain for this weighted two-dimensional receiver.

```text
HALF_DIMENSIONAL_SIEVE_FORMALLY_RELEVANT=true
HALF_DIMENSIONAL_SIEVE_APPLICABLE=false
HALF_DIMENSIONAL_SIEVE_FIXED_POWER_GAIN_PROVED=false
```

---

## 4. Buchstab / Harman decomposition audit

Because `ell` is the unique prime above `sqrt(2N)`, a Buchstab decomposition can isolate the factorization

```text
N=ell*n,
n<ell/2.
```

This is formally exact and is a legitimate reorganization of the receiver.

The difficulty is the resulting bilinear Gaussian factorization

```text
T+iD = pi*W,
N(pi)=ell,
N(W)=n,
```

with the vertical condition on the imaginary coordinate and all reconstructed-cover masks. The t84 contract explicitly forbids treating `pi` and the cover as a newly independent multiplicity. A Harman/Buchstab theorem adapter therefore must estimate the coupled factorization with coefficient norms and ranges already respecting that uniqueness.

No located theorem supplies that full adapter in one standard step.

```text
BUCHSTAB_DECOMPOSITION_FORMALLY_AVAILABLE=true
GAUSSIAN_FACTORIZATION_FORMALLY_AVAILABLE=true
HARMAN_BUCHSTAB_APPLICABLE=false
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
```

---

## 5. Binary quadratic prime / large-prime-factor results

Prime-value theorems for positive definite binary quadratic forms, including Fouvry--Iwaniec type results and later thin-variable generalizations, establish strong distribution for the special subcase in which the form value itself is prime.

That is not an upper bound for the t84 set, which contains all short cofactors

```text
1<=n<sqrt(B/h),
n=k*delta.
```

Likewise, largest-prime-factor results for one-variable polynomial values do not provide a uniform two-variable weighted estimate with `D=d*j`, primitive gcd, and reconstructed-cover filters.

```text
BINARY_QUADRATIC_PRIME_VALUE_THEOREM_DIRECT_ADAPTER=false
BINARY_QUADRATIC_LARGE_PRIME_FACTOR_THEOREM_APPLICABLE=false
```

---

## 6. Gaussian prime BV/BDH and sector distribution

Gaussian-prime distribution in sectors and Bombieri--Vinogradov type results give genuine averaging for a prime ideal / Gaussian prime variable in short norm and angular ranges, sometimes also over arithmetic progressions.

The t84 quantifier order is different. `pi` is not free: it is the unique Gaussian prime above the rational prime

```text
ell=LPF(T^2+D^2).
```

After factoring `T+iD=pi*W`, the congruence

```text
Im(pi*W)=D=d*j
```

couples the prime and cofactor coordinates. The same `ell` also enters `ell*delta<=Y_U` and the reconstructed balanced-cover/hyperbola masks. No located Gaussian BV/BDH theorem retains this vertical product constraint and all physical weights while producing a fixed-power saving.

Moreover, for fixed `U` there are only `B^o(1)` possible `d`; a broad modulus average is neither available nor needed.

```text
GAUSSIAN_BV_BDH_APPLICABLE=false
GAUSSIAN_SECTOR_PRIME_THEOREM_APPLICABLE=false
MOVING_MODULUS_FAMILY_REOPENED=false
```

---

## 7. Vertical divisor dispersion and quarter-scale switching

The exact determinant quotient gives

```text
D=d*j,
min(d,|j|)<=(2B/h)^(1/4).
```

This is useful internal structure. It guarantees that one of the fixed-U divisor host `d` and complementary vertical quotient `j` is quarter-scale short.

But it is only a size dichotomy. It does not by itself provide distribution of primitive binary norm values with a prescribed large prime factor in the vertical progression. If one switches from `d` to `j`, the other factor and the reconstructed physical masks remain coupled through `D`.

No located dispersion theorem controls the resulting weighted primitive lattice points uniformly through the transition region where both `d` and `|j|` can be near the quarter scale.

```text
QUARTER_SCALE_DIVISOR_SWITCH_FORMALLY_AVAILABLE=true
VERTICAL_DIVISOR_DISPERSION_APPLICABLE=false
VERTICAL_SWITCH_UNIFORM_FIXED_POWER_GAIN_PROVED=false
```

---

## 8. Cofactor sieve

The cofactor satisfies

```text
n=k*delta<sqrt(B/h),
```

and every odd prime factor of `n` is `1 mod 4`. This is a useful half-dimensional semigroup restriction.

For fixed `k`, an upper-bound sieve on `delta` supplies standard logarithmic savings in appropriate unweighted models. The target explicitly requires a fixed `B`-power saving, and a logarithmic gain does not qualify.

The additional condition

```text
ell*delta<=Y_U
```

couples the cofactor range back to the largest prime. No located cofactor sieve theorem simultaneously preserves the vertical divisor and reconstructed-cover masks with fixed-power gain.

```text
SHORT_COFACTOR_SIEVE_FORMALLY_AVAILABLE=true
SHORT_COFACTOR_SIEVE_FIXED_POWER_GAIN_PROVED=false
```

---

## 9. Coefficient and physical-mask audit

Merged t78/tH23 already permits four-cell Möbius tensorization at only `B^o(1)` coefficient loss. That bookkeeping remains usable here.

```text
FOUR_CELL_COEFFICIENT_L2_THEOREM_READY=true
FOUR_CELL_COEFFICIENT_L2_LOSS=Bo1
```

The theorem adapter must nevertheless retain the filters on the reconstructed `V`:

```text
balanced primitive V,
small angular-g four-cell weights,
short ellipse,
sharp ell*odd(h)*odd(r)*odd(t) hyperbola,
ell*delta<=Y_U,
fixed beta tag,
fixed reciprocal/inversion orientation,
canonical Gaussian direction convention.
```

No audited candidate theorem admits this complete coefficient system with a certified fixed `B`-power gain.

```text
FULL_PHYSICAL_MASKS_RETAINED=true
APPLICABLE_THEOREM_ADAPTER_RETAINS_FULL_MASKS=false
```

---

## 10. Range ledger

The frozen t84 inequalities imply the following admissible scale ledger:

```text
N=T^2+D^2 <= 2B/h,
|T|,|D| <= sqrt(2B/h),
d*|j|=|D|,
min(d,|j|)<=(2B/h)^(1/4),
ell>sqrt(2N),
n=N/ell<sqrt(N/2)<sqrt(B/h),
n=k*delta,
ell*delta<=Y_U.
```

The range contains both `d`-short and `j`-short cells and does not force a uniform separation between the surviving lattice-coordinate length, cofactor length, and the moduli produced after Gaussian factorization. Therefore none of the candidate distribution theorems has a uniform range adapter across the full packet.

```text
N_SCALE_EXPLICIT=true
T_RANGE_EXPLICIT=true
D_RANGE_EXPLICIT=true
D_RANGE_VERTICAL_FACTORIZATION_RETAINED=true
COFACTOR_RANGE_EXPLICIT=true
PRIME_RANGE_EXPLICIT=true
PRIMITIVE_GCD_CONDITION_RETAINED=true
QUANTIFIER_ORDER_RETAINED=true
```

---

## 11. Strict applicability verdict

Questions A--D from the target have answers:

```text
A_OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING=false
B_ONE_STANDARD_STEP_COMPLETE_ADAPTER=false
C_FIXED_U_PACKET_POWER_SAVING_CERTIFIED=false
D_FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
```

Equivalently,

```text
HALF_DIMENSIONAL_SIEVE_APPLICABLE=false
HARMAN_BUCHSTAB_APPLICABLE=false
GAUSSIAN_BV_BDH_APPLICABLE=false
BINARY_QUADRATIC_LARGE_PRIME_FACTOR_THEOREM_APPLICABLE=false
VERTICAL_DIVISOR_DISPERSION_APPLICABLE=false
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

The minimal remaining obstruction is

```text
MINIMAL_REMAINING_OBSTRUCTION=FixedUVerticalDivisorPrimitiveBinaryNormShortCofactorBuchstabDispersionWithReconstructedCoverMasks
```

The preferred internal receiver is

```text
PREFERRED_RECEIVER=SharedUFixedSelectorDivisorPrimitiveBinaryNormSuperSqrtLPFShortCofactorVerticalBuchstabEnergy
```

The exact feature for t85+ to attack internally is the quarter-scale vertical factorization `D=d*j` inside the primitive Gaussian product after the largest prime has already been made intrinsic.

No new external theorem object has been isolated by this negative audit, so

```text
NEXT_H_NEEDED=false
```

---

## 12. Global ledger context

The immutable mathematical audit stops at t84. Current main may contain later bookkeeping, but the latest canonical whole-family theorem visible at dispatch remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

No fixed-U theorem was proved, so there is no legal whole-family exponent update.

---

## Locked boundary

```text
STAGE14_TH24=COMPLETE_T84_SNAPSHOT_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_VERTICAL_DIVISOR_SIEVE_APPLICABILITY_AUDIT
AUDITED_THROUGH=Stage14-t84
SOURCE_SNAPSHOT_SHA=fa93c79084e05a2f1aa39eeb80b48f2e82f82113
TARGET_FROZEN=true
T84_PRIMITIVE_BINARY_NORM_RETAINED=true
T84_CANONICAL_ELL_AS_LPF_RETAINED=true
T84_SUPER_SQRT_LPF_GAP_RETAINED=true
T84_SHORT_COFACTOR_RETAINED=true
T84_FIXED_U_VERTICAL_DIVISOR_RETAINED=true
T84_PI_V_RECONSTRUCTION_RETAINED=true
CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
NO_SEPARATE_ELL_SUM=true
FULL_PHYSICAL_MASKS_RETAINED=true
HALF_DIMENSIONAL_SIEVE_APPLICABLE=false
HARMAN_BUCHSTAB_APPLICABLE=false
GAUSSIAN_BV_BDH_APPLICABLE=false
BINARY_QUADRATIC_LARGE_PRIME_FACTOR_THEOREM_APPLICABLE=false
VERTICAL_DIVISOR_DISPERSION_APPLICABLE=false
FOUR_CELL_COEFFICIENT_L2_THEOREM_READY=true
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MINIMAL_REMAINING_OBSTRUCTION=FixedUVerticalDivisorPrimitiveBinaryNormShortCofactorBuchstabDispersionWithReconstructedCoverMasks
PREFERRED_RECEIVER=SharedUFixedSelectorDivisorPrimitiveBinaryNormSuperSqrtLPFShortCofactorVerticalBuchstabEnergy
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
```