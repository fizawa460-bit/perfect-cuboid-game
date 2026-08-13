# Stage14-tH33 — super-Kai individual Gaussian-residue long-interval audit

## Status

`COMPLETE_NEGATIVE_UNRESOLVED_SUPER_KAI_INDIVIDUAL_RESIDUE_GATE_AUDIT`

This is a clean-room audit of the frozen `Stage14-t157` target only.

```text
AUDITED_THROUGH=Stage14-t157
SOURCE_SNAPSHOT_SHA=4c46731e68b7d76291a37bc6f10638467c006c93
TARGET_FILE=stages/stage14/14-t157/th33-target.md
TARGET_FROZEN=true
REQUESTED_OBJECT=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
```

No later t-stage conclusion is used.

## 1. Frozen object and exact burden

Work in `K=Q(i)`.  The target fixes one odd squarefree ordinary modulus `d=B^o(1)`, one invertible Gaussian residue `beta_* mod d`, one strict canonical D4 sector, and one actual long interval

```text
L_B=2*sqrt(B),
X=L_B*R,
R>=B^theta,
theta>0 fixed.
```

The packet is explicitly outside the completed tH31/Kai envelope at the actual upper scale:

```text
d^2 > exp(sqrt(log X)/C_K).
```

The required conclusion is not mere existence of a prime.  It is the pointwise lower ratio

```text
T(X;d,beta_*) >= B^(-o(1))*M(X;d),
```

where `M` is the unrestricted sector prime count divided by the exact ordinary Gaussian residue-group order

```text
q_d=|(Z[i]/d Z[i])^x|=d^2*B^o(1).
```

Thus a Linnik-style least-prime theorem, a product-of-primes ray-class representation theorem, or an average-over-moduli theorem is insufficient without an additional chargeable adapter.

## 2. Kai/Mitsui remains the sharpest directly certified individual-modulus PNT interface

Wataru Kai, *Notes on Mitsui's Prime Number Theorem with Siegel zeros*, arXiv:2209.11816v2, refines Mitsui's prime-element theorem for fixed number fields and retains a possible Hecke Siegel zero.  The theorem permits the modulus norm to grow pseudopolynomially with the archimedean scale.

For the already-audited `K=Q(i)` interface, completed tH31 records the usable native condition as

```text
N((d))=d^2 <= exp(sqrt(log X)/C_K)
```

for a fixed field/theorem constant `C_K>0`.

Inside this envelope, the fixed sector and one ordinary Gaussian residue are directly compatible and the long-interval subtraction is valid.  The frozen tH33 packet assumes the strict opposite inequality.  No statement in Kai's theorem extends the individual-residue asymptotic past that envelope merely because `d=B^o(1)`.

```text
KAI_MITSUI_EXACT_GEOMETRY_MATCHES=true
KAI_MITSUI_NATIVE_RANGE_RETAINED=true
KAI_MITSUI_SUPER_RANGE_EXTENSION_FOUND=false
BEST_CERTIFIED_INDIVIDUAL_MODULUS_RANGE=d^2_LE_exp_sqrtlogX_over_CK
```

## 3. Fixed-power headroom helps subtraction, not modulus admissibility

The target has

```text
X/L_B=R>=B^theta.
```

Hence, if a cumulative individual-residue prime-element theorem is already available at scale `X`, the contribution below `L_B` is smaller by a fixed power and can be subtracted exactly as in tH31.  This is a genuine simplification: no short-interval theorem is needed on the long branch.

However, tH155 already evaluates Kai/Mitsui at the actual upper scale `X`; there is no further hidden scale gain.  Once

```text
d^2 > exp(sqrt(log X)/C_K),
```

the fixed-power ratio `X/L_B` does not enlarge Kai's individual modulus hypothesis.

```text
FIXED_POWER_HEADROOM_USED=true
FIXED_POWER_HEADROOM_REMOVES_SHORT_INTERVAL_ISSUE=true
FIXED_POWER_HEADROOM_ENLARGES_INDIVIDUAL_MODULUS_RANGE=false
```

## 4. Log-free zero density and Deuring-Heilbronn do not supply the required pointwise density theorem

Thorner--Zaman, *Explicit results on the distribution of zeros of Hecke L-functions*, arXiv:1510.08086, proves log-free zero-density estimates and explicit Deuring--Heilbronn zero repulsion for Hecke L-functions.  Their subsequent Chebotarev/least-prime work, including arXiv:1604.01750, uses these tools to obtain explicit least-prime bounds.

Those results are powerful enough for existence/Linnik-type conclusions and for controlling families of Hecke zeros, but the audited statements do not give, for every one frozen ordinary Gaussian residue with super-Kai `d=B^o(1)`, the lower-density estimate

```text
T >= B^(-o(1))*M.
```

The distinction is fixed-power significant: one prime, or even a bounded number of primes, is far below a principal benchmark of size `B^(1/2-o(1))` on the surviving Stage14 packets.

```text
LOG_FREE_ZERO_DENSITY_AVAILABLE=true
DEURING_HEILBRONN_AVAILABLE=true
LEAST_PRIME_STYLE_EXISTENCE_SUFFICIENT=false
POINTWISE_SUPER_KAI_DENSITY_FROM_ZERO_DENSITY_CERTIFIED=false
```

## 5. Averaged distribution theorems are not directly chargeable

Bombieri--Vinogradov / Barban--Davenport--Halberstam technology can reach modulus ranges much larger than the individual Siegel--Walfisz/Kai envelope by averaging over moduli and/or residue classes.

For number fields with sector restrictions, Khale--O'Kuhn--Panidapu--Sun--Zhang, arXiv:2008.09677, proves a Bombieri--Vinogradov theorem for primes in short intervals and small sectors.  Smith's number-field BDH results, arXiv:1210.3862 and 1210.3863, are likewise mean-square/average statements.  These do not yield a theorem for the one charged fixed-U modulus and one charged residue in the frozen target without a separate exceptional-set-to-Stage14-measure adapter.

Likewise, large-sieve/zero-density estimates over character or modulus families do not permit us to discard the frozen packet merely because it is exceptional in an averaged theorem.

```text
AVERAGED_LARGE_MODULUS_RESULTS_EXIST=true
AVERAGING_REQUIRED_FOR_KNOWN_BEYOND_KAI_DISTRIBUTION_RESULTS=true
FROZEN_FIXED_PACKET_EXCEPTIONAL_SET_ADAPTER_PROVED=false
AVERAGED_RESULTS_DIRECTLY_APPLICABLE=false
```

## 6. Gaussian-sector results do not restore the growing ordinary residue

Joshua Stucky, *Gaussian Primes in Narrow Sectors*, arXiv:2008.11325, gives strong norm/angle localization for Gaussian primes, but its Hecke family is the angular/conductor-one geometry already used as a comparator in tH32.  It does not provide the present pointwise theorem for one growing ordinary residue modulo super-Kai `d`.

Thus dropping the ordinary residue condition would change the frozen theorem object and is not legal.

```text
GAUSSIAN_SECTOR_THEOREMS_AVAILABLE=true
GROWING_ORDINARY_RESIDUE_RESTORED_BY_SECTOR_THEOREM=false
```

## 7. Recent ray-class product results are existence/combinatorial substitutes, not the required single-prime density

Recent work of Xie, *Products of prime ideals in ray class groups*, arXiv:2606.30567, proves small products of prime ideals representing ray classes.  Earlier Deshouillers--Gun--Ramare--Sivaraman, arXiv:2210.11051, similarly represents ray classes by products of a bounded number of small prime ideals and proves Brun--Titchmarsh-type upper bounds.

These are not lower asymptotics for the number of single prime ideals in every frozen class up to `X`, and therefore do not imply the target lower ratio.

```text
RAY_CLASS_PRODUCT_REPRESENTATION_RESULTS_AVAILABLE=true
RAY_CLASS_PRODUCT_RESULTS_IMPLY_SINGLE_PRIME_DENSITY=false
```

## 8. Possible real Hecke/Siegel zero

A possible real exceptional character must remain in the theorem contract.  It is not a new fixed-power obstruction by itself.

Because the Stage14 target retains

```text
d=B^o(1),
q_d=B^o(1),
```

the standard ineffective Siegel lower bound on `1-beta_exc` remains only subpolynomially small in `B`.  Consequently the suppressing exceptional secondary factor, when evaluated over a fixed-power long interval, can cost `B^(-o(1))` but not a fixed `B^-delta` solely from the exceptional zero.

The unresolved issue is instead that beyond the Kai envelope the known unconditional individual-residue theorem does not control the aggregate nonexceptional zero/error contribution tightly enough relative to the residue main term.

```text
POSSIBLE_SIEGEL_ZERO_RETAINED=true
SIEGEL_ZERO_ALONE_FIXED_POWER_DEPLETION_CERTIFIED=false
SIEGEL_SUPPRESSION_SCALE=BoMinusO1
SUPER_KAI_NONEXCEPTIONAL_ERROR_CONTROL_MISSING=true
```

## 9. Certified verdict

No audited unconditional existing theorem gives the frozen super-Kai pointwise lower ratio for every physical fixed-U packet.

The sharpest directly certified individual-modulus range remains the completed tH31/Kai envelope

```text
d^2 <= exp(sqrt(log X)/C_K).
```

Beyond it, available tools split into:

- least-prime / Chebotarev existence results, too weak for principal density;
- log-free zero-density / Deuring--Heilbronn ingredients, without the required every-residue lower-ratio theorem;
- BV/BDH/large-sieve results requiring averaging not chargeable to the frozen packet;
- Gaussian sector results without the growing ordinary residue;
- ray-class product representations rather than single-prime density.

Therefore the exact unresolved external theorem species is

```text
SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
```

for `K=Q(i)`, one strict fixed sector, one ordinary residue modulo odd squarefree `d=B^o(1)`, fixed-power multiplicative headroom, and the actual-scale Kai-inadmissible window.

```text
STAGE14_TH33=COMPLETE_NEGATIVE_UNRESOLVED_SUPER_KAI_INDIVIDUAL_RESIDUE_GATE_AUDIT
DIRECT_THEOREM_APPLICABLE=false
SUPER_KAI_INDIVIDUAL_RESIDUE_LONG_INTERVAL_COVERED=false
BEST_CERTIFIED_INDIVIDUAL_MODULUS_RANGE=d^2_LE_exp_sqrtlogX_over_CK
FIXED_POWER_HEADROOM_USED=true
POSSIBLE_SIEGEL_ZERO_RETAINED=true
AVERAGING_REQUIRED=true
SUPER_KAI_LONG_FIXED_POWER_DEPLETION_RULED_OUT=false
NEXT_H_NEEDED=false
FIXED_U_H_NEEDED=false
FIXED_U_H_COMPLETED=true
FIXED_U_BLOCKED_BY_H=true
UNRESOLVED_EXTERNAL_GATE=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=UNRESOLVED_EXTERNAL_GATE:SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
```

## Primary sources audited

```text
Wataru Kai,
Notes on Mitsui's Prime Number Theorem with Siegel zeros,
arXiv:2209.11816v2.

Jesse Thorner and Asif Zaman,
Explicit results on the distribution of zeros of Hecke L-functions,
arXiv:1510.08086.

Jesse Thorner and Asif Zaman,
An explicit bound for the least prime ideal in the Chebotarev density theorem,
arXiv:1604.01750.

Tanmay Khale, Cooper O'Kuhn, Apoorva Panidapu, Alec Sun, Shengtong Zhang,
A Bombieri-Vinogradov Theorem for primes in short intervals and small sectors,
arXiv:2008.09677.

Ethan Smith,
A generalization of the Barban-Davenport-Halberstam Theorem to number fields,
arXiv:1210.3862;
A Barban-Davenport-Halberstam asymptotic for number fields,
arXiv:1210.3863.

Joshua Stucky,
Gaussian Primes in Narrow Sectors,
arXiv:2008.11325.

Likun Xie,
Products of prime ideals in ray class groups,
arXiv:2606.30567.

J.-M. Deshouillers, S. Gun, O. Ramare, J. Sivaraman,
Representing ideal classes of ray class groups by product of prime ideals of small size,
arXiv:2210.11051.
```
