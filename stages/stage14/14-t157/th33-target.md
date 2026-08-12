# Stage14-tH33 frozen target — super-Kai individual Gaussian residue long-interval occupancy

```text
TARGET_FROZEN=true
FROZEN_BY=Stage14-t157
REQUESTED_OBJECT=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
```

## Frozen arithmetic object

Work over `K=Q(i)`.  Retain all merged fixed-U packet labels, the strict canonical D4 sector, and the exact ordinary Gaussian prime residue

```text
pi == beta_* (mod d),
```

where `d` is odd, squarefree, `d=B^o(1)`, and `beta_*` is invertible modulo `d`.

Put

```text
L_B=2*sqrt(B),
X=L_B*R,
R>=B^theta,
theta>0 fixed.
```

The packet is required to be outside the completed tH31 Kai/Mitsui envelope at its actual upper scale:

```text
d^2 > exp(sqrt(log X)/C_K),
```

where `C_K` denotes exactly the field constant in the already-consumed tH31 theorem interface.  No numerical value is to be invented.

Stage14-t156 additionally proves on every principal survivor

```text
log d >= c_{K,theta} sqrt(log B).
```

For the sparse localization one may also retain

```text
d^3 <= B^(1/2+o(1)),
```

and for an area principal shell

```text
d^5 <= B^(1/2+o(1)).
```

These upper caps are compatibility data, not assumptions that may be weakened or replaced by a polynomial-modulus average.

## Count and benchmark

Define

```text
T(X;d,beta_*)
 = #{canonical split Gaussian primes pi:
      pi==beta_* (mod d),
      pi in the fixed strict D4 sector,
      L_B < N(pi) <= X},
```

and

```text
M(X;d)
 = 1/q_d
   * #{canonical split Gaussian primes pi:
       pi in the same fixed strict D4 sector,
       L_B < N(pi) <= X},

q_d=|(Z[i]/dZ[i])^x|.
```

The desired fixed-power-scale conclusion is the uniform lower ratio

```text
T(X;d,beta_*) >= B^(-o(1)) M(X;d)
```

for every frozen physical packet in the target range.

A theorem that only gives an average over moduli, residues, interval locations, sectors, or fixed-U packets is not directly applicable unless it includes a rigorously chargeable exceptional-set bound compatible with the already-frozen Stage14 measure.

## Required audit questions

1. Does an unconditional existing theorem give the above individual-residue long-interval lower ratio beyond the Kai/Mitsui pseudopolynomial envelope?
2. Can Linnik-type least-prime, log-free zero-density, Deuring-Heilbronn, Gallagher, Bombieri-Vinogradov/Barban-Davenport-Halberstam, or Hecke large-sieve technology be converted to this exact fixed packet without averaging away the charged residue?
3. Does fixed-power headroom `X/L_B>=B^theta` materially enlarge the admissible individual modulus range beyond tH31 once the lower endpoint is already polynomially large?
4. Retain a possible real Hecke/Siegel zero.  State explicitly whether it is harmless, suppressing only by `B^-o(1)`, or becomes a genuine obstruction in the super-Kai range.
5. If no direct theorem applies, identify the sharpest certified individual-modulus range and the exact missing adapter/theorem species.
6. Do not use GRH or unproved equidistribution.

## Relationship to earlier audits

- tH31 positively covers the same prime geometry only inside the Kai/Mitsui actual-scale pseudopolynomial envelope.
- tH30 audited a broader cofactor/prime reciprocal hyperbola with individual `d=B^o(1)` and isolated the individual-residue modulus bias as a blocker.
- tH33 is materially narrower: one actual upper endpoint, fixed-power headroom, one exact ordinary Gaussian residue, and the explicit actual-scale Kai-inadmissible modulus window produced by t156.

## Required output fields

```text
STAGE14_TH33=...
DIRECT_THEOREM_APPLICABLE=...
SUPER_KAI_INDIVIDUAL_RESIDUE_LONG_INTERVAL_COVERED=...
BEST_CERTIFIED_INDIVIDUAL_MODULUS_RANGE=...
FIXED_POWER_HEADROOM_USED=...
POSSIBLE_SIEGEL_ZERO_RETAINED=...
AVERAGING_REQUIRED=...
SUPER_KAI_LONG_FIXED_POWER_DEPLETION_RULED_OUT=...
NEXT_H_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
