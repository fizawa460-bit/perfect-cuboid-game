# Stage14-tH29 — independent nonboundary Gaussian cofactor/prime projective-hyperbola theorem audit

## Status

`COMPLETE_NONBOUNDARY_PROJECTIVE_HYPERBOLA_DISPERSION_APPLICABILITY_AUDIT`

This is a clean-room audit of the frozen Stage14-t127 target only.

```text
AUDITED_THROUGH=Stage14-t127
SOURCE_SNAPSHOT_SHA=38ac82435315979d3d0493090d153b4b36163be1
TARGET_FILE=stages/stage14/14-t127/th29-target.md
TARGET_FROZEN=true
REQUESTED_OBJECT=FixedPacketNonboundaryPrimitiveGaussianCofactorPrimeProjectiveHyperbolaDispersion
```

No later Stage14-t conclusion is used.

## 1. Frozen analytic object

The target is the centered nonprincipal contribution

```text
D
 = 1/g * sum_{chi != 1 in G(d)^}
       chi([a])
       sum_{
         gamma in Omega_nb,
         pi_ell canonical split,
         ell>2*sqrt(B),
         N(gamma)*ell<=X_U
       }
       chi([gamma]) chi([pi_ell]),

g=|G(d)|=B^o(1),
d=B^o(1),
X_U=2B/(h*k0).
```

The bad event to be ruled out would be

```text
D <= -(1-B^(-delta)) M
```

for some fixed `delta>0`, where `M` is the exact principal class baseline.

## 2. The nested interval has no uniform headroom

For one cofactor norm `n`, the prime range is exactly

```text
(2*sqrt(B), X_U/n].
```

The target gives only

```text
X_U/n > 2*sqrt(B),
```

with no fixed-power or even logarithmic lower bound on the interval width or on the multiplicative headroom

```text
R(n):=X_U/(2*sqrt(B)*n)=sqrt(B)/(h*k0*n)>1.
```

Hence the family contains an endpoint regime with `R(n)` arbitrarily close to `1` at theorem level.  Prime-ideal or Gaussian-prime distribution theorems in long/short norm intervals do not automatically provide a uniform asymptotic in such unrestricted edge intervals.

Joshua Stucky, arXiv:2008.11325, proves Gaussian-prime counting with simultaneous short norm and angular restrictions, but this does not state a uniform theorem for the present arbitrary moving endpoint, projective ray class modulo `d=B^o(1)`, and correlated physical cofactor weight.

```text
UNIFORM_PRIME_INTERVAL_HEADROOM_PROVED=false
ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true
GAUSSIAN_NARROW_SECTOR_THEOREM_DIRECTLY_APPLICABLE=false
```

## 3. Hecke/ray-class zero-density theory does not remove the uniform individual-class obstruction

The projective characters are finite-order Hecke/ray-class type characters over `Q(i)`.  Thorner--Zaman, arXiv:1510.08086, prove log-free zero-density and Deuring--Heilbronn results for Hecke `L`-functions and explicitly retain the possibility of an exceptional real character/real zero.  Zaman, arXiv:1506.01635, gives least-prime-ideal results in the presence of Siegel zeros; those results concern existence/least prime ideals in ray classes, not a uniform lower asymptotic for every moving interval in this target.

The frozen hypotheses say only

```text
d=B^o(1),
```

not `d` fixed independently of `B` and not `d<=log^A B`.  They also contain no no-exceptional-character hypothesis for the projective quotient.  Consequently the standard Hecke PNT/zero-density package does not directly imply

```text
D=o(M)
```

uniformly over all frozen packets and all endpoint intervals.

```text
HECKE_ZERO_DENSITY_AVAILABLE=true
REAL_EXCEPTIONAL_CHARACTER_UNIFORMLY_EXCLUDED=false
INDIVIDUAL_PROJECTIVE_CLASS_PNT_FOR_D_EQUALS_BO1_AND_ALL_TARGET_INTERVALS_PROVED=false
LEAST_PRIME_IDEAL_RESULTS_SUFFICIENT_FOR_TARGET=false
```

## 4. Large-sieve/Bombieri--Vinogradov technology

Baier--Bansal, arXiv:1811.07300, prove large-sieve inequalities for sparse sets of Gaussian moduli, including Gaussian-prime moduli.  This is valuable mean-value technology but the frozen target has one endpoint modulus `d=B^o(1)` and only `B^o(1)` projective characters; it does not average over a polynomially large modulus family.

Likewise Bombieri--Vinogradov/BDH-type results average prime-distribution errors over moduli/classes or substantially cleaner coefficients.  They do not directly furnish a lower bound against principal-scale negative correlation for this exact fixed-modulus cofactor/prime hyperbola with `Omega_nb` retained.

```text
GAUSSIAN_SPARSE_MODULI_LARGE_SIEVE_DIRECTLY_APPLICABLE=false
GAUSSIAN_BV_BDH_FIXED_PACKET_PROJECTIVE_HYPERBOLA_DIRECTLY_APPLICABLE=false
POLYNOMIAL_CHARACTER_OR_MODULUS_FAMILY_AVAILABLE=false
```

## 5. Bilinear/spin technology

Friedlander--Iwaniec--Mazur--Rubin, arXiv:1110.6331, obtain prime spin distribution by bilinear-form technology for a specifically defined spin invariant.  The t127 coefficient is an exact projective character incidence on the physical cofactor family `Omega_nb`; the frozen target does not identify this coefficient with a spin symbol or with a finite theorem-compatible Type-I/Type-II decomposition.

The t91--t124 reductions remove much of the old opaque selector from tH26, but they do not prove that the remaining physical cofactor indicator has multiplicative, spin, trace-function, or separated bilinear structure sufficient for those theorems.

```text
GAUSSIAN_SPIN_THEOREM_DIRECTLY_APPLICABLE=false
PHYSICAL_COFACTOR_CHARACTER_TYPE_I_II_ADAPTER_PROVED=false
```

## 6. Recent ray-class product results do not solve one-prime occupancy

Likun Xie, arXiv:2606.30567, proves that every narrow ray class in a fixed number field is represented by a product of three prime ideals of controlled norm, and a positive proportion by products of two prime ideals.  This does not imply that one canonical split prime occupies the packet-selected projective class in every moving interval, nor does it estimate the class-matched cofactor/prime hyperbola relative to its principal baseline.

```text
RAY_CLASS_PRODUCT_OF_PRIMES_RESULT_DIRECTLY_APPLICABLE=false
ONE_PRIME_MOVING_INTERVAL_OCCUPANCY_FROM_PRODUCT_THEOREM=false
```

## 7. Certified verdict

No audited theorem proves, uniformly for the frozen target,

```text
D=o(M)
```

or otherwise rules out

```text
D <= -(1-B^(-delta))M
```

with a fixed `delta>0`, while retaining all target conditions.

The decisive unresolved inputs are not generic projective density.  They are:

```text
A. endpoint-short prime intervals with no uniform headroom;
B. possible individual real projective-Hecke exceptional-character bias for d=B^o(1);
C. absence of a theorem-ready Type-I/Type-II or spin decomposition for the retained physical cofactor character sum.
```

These are separate mechanisms and should be split internally before another literature audit.

```text
DIRECT_THEOREM_APPLICABLE=false
UNIFORM_PROJECTIVE_HYPERBOLA_D_O_M_PROVED=false
UNIFORM_FIXED_POWER_SELECTED_CLASS_DEPLETION_RULED_OUT=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_NEXT_INTERNAL_REDUCTION=PrimeIntervalHeadroomExceptionalCharacterAndCofactorTypeIITriSplit
NEXT_H_NEEDED=false
```

## Primary sources checked

```text
Thorner--Zaman, Explicit results on the distribution of zeros of Hecke L-functions,
  arXiv:1510.08086.
Zaman, On the least prime ideal and Siegel zeros,
  arXiv:1506.01635.
Baier--Bansal, Large sieve with sparse sets of moduli for Z[i],
  arXiv:1811.07300.
Stucky, Gaussian Primes in Narrow Sectors,
  arXiv:2008.11325.
Friedlander--Iwaniec--Mazur--Rubin, The spin of prime ideals,
  arXiv:1110.6331.
Xie, Products of prime ideals in ray class groups,
  arXiv:2606.30567.
```

## Frozen boundary

```text
STAGE14_TH29=COMPLETE_NONBOUNDARY_PROJECTIVE_HYPERBOLA_DISPERSION_APPLICABILITY_AUDIT
AUDITED_THROUGH=Stage14-t127
SOURCE_SNAPSHOT_SHA=38ac82435315979d3d0493090d153b4b36163be1
TARGET_FROZEN=true
DIRECT_THEOREM_APPLICABLE=false
ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true
REAL_EXCEPTIONAL_CHARACTER_UNIFORMLY_EXCLUDED=false
PHYSICAL_COFACTOR_CHARACTER_TYPE_I_II_ADAPTER_PROVED=false
UNIFORM_PROJECTIVE_HYPERBOLA_D_O_M_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
PREFERRED_NEXT_INTERNAL_REDUCTION=PrimeIntervalHeadroomExceptionalCharacterAndCofactorTypeIITriSplit
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
