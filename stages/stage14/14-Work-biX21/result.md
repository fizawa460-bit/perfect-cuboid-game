# Stage14-Work-biX21 — subpolynomial prime-support concentration and heavy-mover extraction

## Status

`COMPLETE_SUBPOLYNOMIAL_PRIME_SUPPORT_CONCENTRATION_ENERGY_UNIFICATION`

Consumes only merged Stage14 sources on latest main: `Stage14-Work-bhX20`, `Stage14-4du`, `Stage14-s7-62`, `Stage14-t102`, and the completed frozen `Stage14-tH27` boundary through t102. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Common combinatorial concentration lemma

Let a physical mover incidence be distributed over a prime-index set `P`, with nonnegative masses

```text
m(p) >= 0,
I = sum_{p in P} m(p),
K = |P|,
Energy = sum_{p in P} m(p)^2.
```

Then exactly

```text
max_p m(p) >= I/K,
I^2 <= K * Energy.
```

Hence whenever

```text
K=B^o(1),
I=B^(alpha-o(1)),
```

one has

```text
max_p m(p)=B^(alpha-o(1))
```

in the lower-bound exponent sense, and

```text
Energy >= B^(2 alpha-o(1)).
```

This is a charged-once concentration statement. The heavy-prime and energy conclusions are two consequences of the same incidence mass and may not be multiplied as independent savings.

```text
COMMON_SUBPOLYNOMIAL_PRIME_SUPPORT_CONCENTRATION_LEMMA_PROVED=true
HEAVY_PRIME_AND_ENERGY_DOUBLE_CHARGE_FORBIDDEN=true
```

## 2. Global range-stable arithmetic branch: one heavy mover prime

Merged s7-62 proves on the pure arithmetic range-stable mover branch

```text
|Im(E_arith)|=B^o(1).
```

It also proves that square-root saturation of that arithmetic incidence has

```text
I_arith=B^(1/2-o(1)).
```

Therefore the lemma above gives a prime `ell_*` in the range-stable Gaussian mover image with

```text
m(ell_*) >= I_arith / |Im(E_arith)|
          = B^(1/2-o(1)).
```

Thus any square-root-saturating range-stable arithmetic sequence contains one subpolynomial-size Gaussian split prime

```text
ell_*=B^o(1)
```

which is a physical two-square mover candidate for `B^(1/2-o(1))` weighted frozen states.

This is stronger than merely knowing that the total collision energy is `B^(1-o(1))`: the obstruction can be localized to one heavy candidate prime before any external incidence theorem is invoked.

```text
GLOBAL_RANGE_STABLE_HEAVY_MOVER_PRIME_PROVED=true
GLOBAL_HEAVY_MOVER_PRIME_SCALE=Bo0
GLOBAL_HEAVY_MOVER_STATE_MASS_EXPONENT=1/2
```

## 3. Fixed-prime global collision equation

Merged 4du gives, for two plus-state divisor representations sharing the same mover prime,

```text
y_i=r_i s_i,
ell=(r_i^2+s_i^2)/(2x_i),
```

and collision is exactly

```text
x_2 (r_1^2+s_1^2)
=
x_1 (r_2^2+s_2^2).
```

After the heavy-prime extraction this equation is no longer only an aggregate collision relation over a moving prime image. On the heavy subfamily one may freeze

```text
ell=ell_*
```

and study a single fixed-prime norm-ratio incidence packet carrying square-root-scale state mass.

The minus and mixed candidate descriptions remain analogous degree-at-most-two divisor graphs from merged s7-62.

No fixed-power upper bound for this fixed-`ell_*` collision packet is proved here.

```text
GLOBAL_COLLISION_PRIME_CAN_BE_FROZEN_ON_SATURATING_ARITHMETIC_SUBFAMILY=true
FIXED_HEAVY_PRIME_NORM_RATIO_COLLISION_SAVING_PROVED=false
```

## 4. Fixed-U side: the same concentration skeleton, different normalization

Merged t102 proves on every live square-root-saturating fixed-U packet

```text
r=omega(delta_G)=B^o(1),
I_bar=(1/r) sum_p Inf_p(f)=B^(-o(1)),
E_move=(1/r) sum_p Inf_p(f)^2=B^(-o(1))
```

in lower-bound/exponent-zero sense, and an exponent-zero density of mover-prime bits.

Applying the same finite-support concentration principle yields a prime `p_*` with

```text
Inf_{p_*}(f)=B^(-o(1)),
```

which is consistent with the earlier t96 single-influential-prime localization. Thus t102 realizes the same abstract principle:

```text
subpolynomial prime support
+
non-negligible total mover mass
=>
heavy prime action / non-negligible mover energy.
```

However the normalization is different. Global `m(ell)` counts cross-state physical incidences at square-root scale, whereas fixed-U `Inf_p(f)` is a normalized edge-boundary density inside one Boolean packet.

```text
COMMON_PRIME_SUPPORT_ENERGY_SKELETON_PROVED=true
GLOBAL_AND_FIXED_U_MOVER_MASS_NORMALIZATIONS_IDENTIFIED=false
```

## 5. Why this is not yet a cross-route arithmetic adapter

The global heavy-prime packet is governed by complementary-square / divisor-graph arithmetic:

```text
Q(ell*x,y) XOR Q(x,ell*y),
Q(X,Y)=1_{(X+Y)/2 square} 1_{(X-Y)/2 square}.
```

The fixed-U packet is governed by Gaussian orientation conjugation and one of the t100/t101 elementary mover boundaries:

```text
SIGN / DIV / PROJ,
principal density + centered discrepancy.
```

Merged t102 further proves only that one broad boundary class has exponent-zero prime average; it does not produce one common elementary modulus, sign cone, or projective acceptance set across primes.

Therefore no finite-fiber map currently identifies the global fixed-`ell_*` norm-ratio collision packet with a fixed-U elementary mover-energy packet.

```text
COMMON_ARITHMETIC_COLLISION_ADAPTER_PROVED=false
FIXED_U_SAVING_CROSS_PROMOTED=false
GLOBAL_SAVING_CROSS_PROMOTED=false
```

## 6. New integrated receiver

On the range-stable global arithmetic branch the receiver contracts from

```text
GaussianMoverCandidateImageOrNormRatioCollisionEnergy
```

to

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianMoverPrimeNormRatioCollisionMass.
```

The remaining global alternatives outside this arithmetic branch remain charged exactly as before:

```text
range/sector mover branch,
masked full-conductor inverse-fraction covariance,
positive connected third cumulant,
principal occupancy.
```

The fixed-U receiver remains

```text
SharedUCanonicalLPFExponentZeroGenericPrimeMoverDensityEnergy
PlusPrincipalCenteredBoundaryIncidence.
```

## 7. Next internal target

The most useful next integrated target is:

```text
Fixed-Prime Norm-Ratio Collision Proportionality Lemma.
```

For the heavy global prime `ell_*`, split the square-root-scale collision mass into

```text
(a) proportional/common-factor collisions,
(b) genuinely nonproportional norm-ratio incidences,
```

under all physical masks. Either show the proportional branch is finite-fiber / already charged, or expose a fresh determinant/incidence receiver on the nonproportional branch.

On the fixed-U side, the analogous requirement is to compress the varying SIGN/DIV/PROJ mover incidences to one common arithmetic boundary before any cross-route theorem transfer is legal.

## 8. H decision

No new H is opened by Work-biX21.

The new gain is exact and internal: heavy-prime extraction from merged subpolynomial image support. The next global step is still proportional/nonproportional collision algebra. tH27 remains complete and consumed on the fixed-U side; `tH28` remains unnecessary until a common theorem-shaped boundary family is exposed.

```text
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH28_NEEDED=false
```

## Boundary

```text
STAGE14_WORK_BIX21=COMPLETE_SUBPOLYNOMIAL_PRIME_SUPPORT_CONCENTRATION_ENERGY_UNIFICATION
MERGED_BHX20_CONSUMED=true
MERGED_4DU_CONSUMED=true
MERGED_S7_62_CONSUMED=true
MERGED_T102_CONSUMED=true
COMMON_SUBPOLYNOMIAL_PRIME_SUPPORT_CONCENTRATION_LEMMA_PROVED=true
COMMON_PRIME_SUPPORT_ENERGY_SKELETON_PROVED=true
GLOBAL_RANGE_STABLE_HEAVY_MOVER_PRIME_PROVED=true
GLOBAL_HEAVY_MOVER_PRIME_SCALE=Bo0
GLOBAL_HEAVY_MOVER_STATE_MASS_EXPONENT=1/2
GLOBAL_COLLISION_PRIME_CAN_BE_FROZEN_ON_SATURATING_ARITHMETIC_SUBFAMILY=true
HEAVY_PRIME_AND_ENERGY_DOUBLE_CHARGE_FORBIDDEN=true
COMMON_ARITHMETIC_COLLISION_ADAPTER_PROVED=false
FIXED_HEAVY_PRIME_NORM_RATIO_COLLISION_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH28_NEEDED=false
NEXT_INTEGRATED_TARGET=FixedPrimeNormRatioCollisionProportionalityLemma
```
