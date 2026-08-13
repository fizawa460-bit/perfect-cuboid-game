# Stage14-tH30 — independent fixed-residue Gaussian cofactor/prime hyperbola theorem audit

## Status

`COMPLETE_FIXED_RESIDUE_GAUSSIAN_COFACTOR_PRIME_HYPERBOLA_APPLICABILITY_AUDIT`

This is an independent audit of the frozen Stage14-t135 target.

```text
AUDITED_THROUGH=Stage14-t135
SOURCE_SNAPSHOT_SHA=14ca52cf310b1bb51f51878cb9d5c76cfb768923
TARGET_FILE=stages/stage14/14-t135/th30-target.md
TARGET_FROZEN=true
REQUESTED_OBJECT=FixedPacketFixedGaussianResiduePrimitiveSectorCofactorPrimeReciprocalHyperbolaOccupancy
```

No later t-stage conclusion is used.

## 1. Frozen target

The target is the nonnegative fixed-residue incidence

```text
T_*
 = # {(z,pi_ell):
      z primitive in one fixed open Gaussian sector S,
      z == rho_* (mod d),
      z satisfies one frozen exceptional local packet,
      pi_ell canonical split prime,
      pi_ell == beta_* (mod d),
      ell>2*sqrt(B),
      N(z)*ell<=X_U},
```

with

```text
d=B^o(1),
X_U=2B/(h*k0),
```

and principal ordinary-residue baseline

```text
M_*
 = 1/|(Z[i]/dZ[i])^x|
   * sum_z #{canonical split pi_ell:
             2*sqrt(B)<ell<=X_U/N(z)}.
```

The audit asks whether known results uniformly rule out

```text
T_* <= B^(-delta) M_*
```

for fixed `delta>0` while retaining the whole target.

## 2. The previous opaque-cofactor obstruction is removed

Unlike the tH29 target, the cofactor coefficient is no longer an unnamed nonmultiplicative physical sequence.  It is the indicator of an explicit primitive Gaussian lattice set in

- one fixed broad sector;
- one fixed ordinary Gaussian residue class modulo `d`;
- one frozen finite/local exceptional packet.

Thus the old failure

```text
PHYSICAL_COFACTOR_CHARACTER_TYPE_I_II_ADAPTER_PROVED=false
```

is no longer the decisive obstruction for this target.  The cofactor side is theorem-compatible lattice/ray-class data in the ordinary sense; no separate Gaussian-spin identification is needed merely to state it.

```text
OPAQUE_PHYSICAL_COFACTOR_COEFFICIENT_REMAINS=false
COFACTOR_LATTICE_RESIDUE_SECTOR_STRUCTURE_EXPLICIT=true
TH29_COFACTOR_TYPE_II_ADAPTER_OBSTRUCTION_REMOVED=true
```

This is genuine progress relative to tH29.

## 3. Endpoint-short prime intervals still prevent a uniform lower theorem

For fixed `z`, the prime interval is

```text
(2*sqrt(B), X_U/N(z)].
```

The frozen hypotheses require only that its upper endpoint exceed the lower endpoint.  There is no uniform additive or multiplicative headroom.  Hence the target includes intervals whose length is arbitrarily small at theorem level.

Even for ordinary rational primes, unconditional short-interval results require a positive power-scale interval.  Runbo Li, arXiv:2308.04458, proves primes in intervals of length `x^0.52`; this is far stronger headroom than the frozen target guarantees.  Grenie--Molteni--Perelli, arXiv:1602.02906, obtain uniform prime/prime-ideal short-interval results under the relevant Riemann Hypothesis, not unconditionally.

Joshua Stucky, arXiv:2008.11325, counts Gaussian primes with simultaneous short norm and angular restrictions, but does not give an unconditional lower asymptotic for an arbitrarily thin moving interval in one growing ordinary residue class modulo the present `d`.

Therefore the reciprocal hyperbola cannot by itself manufacture a uniform prime lower bound at the endpoint.

```text
ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true
UNCONDITIONAL_ENDPOINT_PRIME_LOWER_BOUND_FOR_ALL_TARGET_INTERVALS=false
GAUSSIAN_SHORT_INTERVAL_SECTOR_RESULTS_DIRECTLY_CLOSE_TARGET=false
```

## 4. Growing individual modulus and exceptional real zeros remain

The prime condition is now one ordinary Gaussian residue class modulo `d`, which is cleaner than a moving projective class.  Nevertheless the target only assumes

```text
d=B^o(1),
```

with no fixed `A` such that `d<=log^A B` and no no-exceptional-zero hypothesis.

Thorner--Zaman, arXiv:1510.08086, prove log-free zero-density and Deuring--Heilbronn estimates for Hecke `L`-functions while retaining the possible exceptional real character/zero.  Zaman, arXiv:1506.01635, explicitly treats least prime ideals in ray classes in the presence of a Siegel zero; existence/least-prime bounds do not yield the required uniform lower asymptotic in every reciprocal interval.

Thorner--Zaman, arXiv:2108.10878, show how sufficiently uniform zero-density technology yields Siegel--Walfisz and Hoheisel-type conclusions for rational arithmetic progressions, but the frozen target does not impose the corresponding safe modulus/interval hypotheses, and it is over `Q(i)` with a specific canonical Gaussian-prime residue.

Hence a standard fixed/polylog-conductor Hecke PNT heuristic is not a theorem for every allowed packet here.

```text
SUBPOLYNOMIAL_MODULUS_STRONGER_THAN_POLYLOG_POSSIBLE=true
REAL_EXCEPTIONAL_CHARACTER_UNIFORMLY_EXCLUDED=false
UNIFORM_INDIVIDUAL_FIXED_RESIDUE_PNT_FOR_D_EQUALS_BO1_PROVED=false
LEAST_PRIME_RAY_CLASS_RESULTS_SUFFICIENT=false
```

## 5. Mean-value and ray-class product results do not repair the individual endpoint target

Baier--Bansal, arXiv:1811.07300, give Gaussian large-sieve estimates over sparse modulus families.  The frozen target has one individual modulus/residue packet and no polynomial modulus average to spend.

Likun Xie, arXiv:2606.30567, proves representation of ray classes by products of a bounded number of prime ideals and positive-proportion two-prime representation results.  This does not imply one-prime occupancy in every fixed residue and every moving reciprocal interval.

The hyperbola does average over cofactors, but the frozen hypotheses do not prevent the principal cofactor mass from concentrating on the endpoint norm layer.  Therefore one cannot discard the endpoint regime by averaging without a separate internal mass argument.

```text
GAUSSIAN_LARGE_SIEVE_INDIVIDUAL_PACKET_LOWER_BOUND=false
RAY_CLASS_PRODUCT_RESULTS_ONE_PRIME_INTERVAL_LOWER_BOUND=false
HYPERBOLA_AVERAGING_FORCES_LONG_HEADROOM=false
```

## 6. Certified verdict

No audited unconditional theorem covers the complete frozen target and uniformly rules out a fixed-power depletion.

However the obstruction set is strictly smaller than at tH29.  The cofactor Type-I/II opacity is gone.  The remaining minimal obstructions are

```text
A. endpoint-short fixed-residue prime intervals with no uniform headroom;
B. long/interior fixed-residue prime distribution for an individual modulus allowed to be as large as B^o(1), including possible real exceptional-character bias.
```

A fresh literature audit is not useful until the parent route splits endpoint mass from long-headroom mass and separates a safe modulus range (for example fixed/polylogarithmic conductor) from the genuinely larger subpolynomial-modulus range.

```text
DIRECT_THEOREM_APPLICABLE=false
UNIFORM_FIXED_RESIDUE_HYPERBOLA_DEPLETION_RULED_OUT=false
TH29_COFACTOR_ADAPTER_OBSTRUCTION_REMOVED=true
ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true
SUBPOLYNOMIAL_INDIVIDUAL_MODULUS_OBSTRUCTION_REMAINS=true
REAL_EXCEPTIONAL_CHARACTER_UNIFORMLY_EXCLUDED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_NEXT_INTERNAL_REDUCTION=EndpointMassVersusLongHeadroomSafeModulusAndExceptionalRayClassSplit
NEXT_H_NEEDED=false
```

## Primary sources checked

```text
Thorner--Zaman, Explicit results on the distribution of zeros of Hecke L-functions,
  arXiv:1510.08086.
Zaman, On the least prime ideal and Siegel zeros,
  arXiv:1506.01635.
Thorner--Zaman, Refinements to the prime number theorem for arithmetic progressions,
  arXiv:2108.10878.
Grenie--Molteni--Perelli, Primes and prime ideals in short intervals,
  arXiv:1602.02906.
Stucky, Gaussian Primes in Narrow Sectors,
  arXiv:2008.11325.
Baier--Bansal, Large sieve with sparse sets of moduli for Z[i],
  arXiv:1811.07300.
Li, The number of primes in short intervals and numerical calculations for Harman's sieve,
  arXiv:2308.04458.
Xie, Products of prime ideals in ray class groups,
  arXiv:2606.30567.
```

## Frozen boundary

```text
STAGE14_TH30=COMPLETE_FIXED_RESIDUE_GAUSSIAN_COFACTOR_PRIME_HYPERBOLA_APPLICABILITY_AUDIT
AUDITED_THROUGH=Stage14-t135
SOURCE_SNAPSHOT_SHA=14ca52cf310b1bb51f51878cb9d5c76cfb768923
TARGET_FROZEN=true
DIRECT_THEOREM_APPLICABLE=false
TH29_COFACTOR_ADAPTER_OBSTRUCTION_REMOVED=true
ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true
SUBPOLYNOMIAL_INDIVIDUAL_MODULUS_OBSTRUCTION_REMAINS=true
REAL_EXCEPTIONAL_CHARACTER_UNIFORMLY_EXCLUDED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
PREFERRED_NEXT_INTERNAL_REDUCTION=EndpointMassVersusLongHeadroomSafeModulusAndExceptionalRayClassSplit
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
