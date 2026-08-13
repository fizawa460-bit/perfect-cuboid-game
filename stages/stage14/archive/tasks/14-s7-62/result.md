# Stage14-s7-62 — range-stable mover peel and forced norm-ratio collision energy

## Status

`COMPLETE_RANGE_STABLE_SUBPOLYNOMIAL_MOVER_AND_FORCED_COLLISION_ENERGY_REDUCTION`

Consumes merged `Stage14-s7-61`, merged `Stage14-s7-60`, merged `Stage14-4ds`, merged `Stage14-4dt`, merged `Stage14-4du`, merged `Stage14-Work-bhX20`, and latest main.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged 4dt gives a divisor-many Gaussian mover-prime candidate list for each frozen cofactor state. Merged 4du then gives the global candidate-image / collision-energy dichotomy

```text
I^2 <= |Im(E)| * Energy.
```

Stage14-s7-62 adds a new s-specific scale peel: once the separately identified range/sector influence is removed, a genuinely arithmetic range-stable mover prime must satisfy `ell=B^o(1)`. This collapses the diffuse-image branch of 4du and forces large collision energy on any square-root-saturating arithmetic sequence.

## 1. Equal square-root scale of the complementary norm coordinates

On the theta-quarter saturation packet,

```text
X=C_*ST,
Y=u_*RJ.
```

Merged s7-46 gives

```text
log_B C_* = chi,
log_B(ST) = 1/2-chi,
log_B u_* = 1/4-chi,
log_B(RJ) = chi+1/4.
```

Hence

```text
boxed:
X=B^(1/2+o(1)),
Y=B^(1/2+o(1)).
```

## 2. Range-stable arithmetic movers have subpolynomial prime size

Merged s7-61 writes one candidate flip as

```text
state + : (X_+,Y_+)=(ell*x,y),
state - : (X_-,Y_-)=(x,ell*y).
```

The s7-59 physical filtration already isolates range/sector influence from the genuinely arithmetic balanced-allocation / reciprocal-completion influence.

Therefore, on the **pure arithmetic mover branch**, the flip must be range-stable: both local states remain in the same fixed-power interior norm scale before the two-square arithmetic selector is compared.

Thus

```text
X_+,X_-,Y_+,Y_-=B^(1/2+o(1)).
```

But exactly

```text
X_+/X_-=ell,
Y_-/Y_+=ell.
```

Therefore

```text
boxed:
ell=B^o(1).
```

If `ell=B^(lambda+o(1))` with fixed `lambda>0`, the flip is a fixed-power archimedean mover and belongs to the already-separated range/sector branch rather than the pure arithmetic branch.

```text
RANGE_STABLE_ARITHMETIC_MOVER_PRIME_SCALE=Bo0
FIXED_POWER_ELL_ARITHMETIC_MOVER_EMPTY=true
FIXED_POWER_ELL_CAN_ONLY_SURVIVE_AS_RANGE_MOVER=true
```

This does not bound the range-mover branch; it cleanly separates it from the arithmetic receiver.

## 3. Explicit low-degree divisor graphs

The merged 4dt finite candidate theorem can be sharpened algebraically.

For the plus state, if `Q(ell*x,y)=1`, write

```text
m=D+A,
n=D-A.
```

Then

```text
mn=y,
m^2+n^2=2ell*x,
```

so

```text
boxed:
ell=(m^2+n^2)/(2x),  mn=y.
```

For the minus state, if `Q(x,ell*y)=1`, then

```text
mn=ell*y,
m^2+n^2=2x.
```

Because `gcd(ell,y)=1` and `ell` is prime, after swapping factors if needed

```text
m=ell*a,
n=b,
ab=y,
```

hence

```text
boxed:
ell^2 a^2+b^2=2x,  ab=y,
```

or symmetrically

```text
a^2+ell^2 b^2=2x,  ab=y.
```

Thus the candidate boundary is a divisor graph of degree at most two in `ell`.

```text
LOW_DEGREE_DIVISOR_GRAPH_BOUNDARY_PROVED=true
BOUNDARY_DEGREE_IN_ELL_AT_MOST=2
```

Merged 4dt already proves the resulting frozen-state candidate count is `B^o(1)`. That theorem is imported and not double charged.

## 4. The range-stable candidate image is subpolynomial

On the pure arithmetic branch every candidate mover satisfies

```text
ell=B^o(1).
```

Hence the number of distinct candidate primes occurring across **all** range-stable arithmetic frozen states is itself

```text
boxed:
|Im(E_arith)|=B^o(1).
```

Indeed the set of positive integers, hence primes, up to `B^o(1)` has subpolynomial cardinality.

This is stronger than the per-state finite candidate list of 4dt.

```text
RANGE_STABLE_CANDIDATE_PRIME_IMAGE_SIZE=Bo1
DIFFUSE_B_HALF_CANDIDATE_IMAGE_POSSIBLE=false
```

## 5. 4du Cauchy dichotomy collapses to forced collision energy

Merged 4du defines

```text
m(ell)=#{frozen states s : (s,ell) in E},
I=sum_ell m(ell),
Energy=sum_ell m(ell)^2,
```

and proves

```text
I^2 <= |Im(E)| * Energy.
```

If the range-stable arithmetic mover incidence itself saturates at square-root scale,

```text
I=B^(1/2-o(1)),
```

then s7-62 gives

```text
|Im(E_arith)|=B^o(1).
```

Therefore

```text
boxed:
Energy >= I^2/|Im(E_arith)| = B^(1-o(1)).
```

So the diffuse-image alternative retained in general 4du is impossible on the pure arithmetic s branch.

```text
RANGE_STABLE_ARITHMETIC_SATURATION_FORCES_COLLISION_ENERGY=true
FORCED_COLLISION_ENERGY_EXPONENT=1
DIFFUSE_IMAGE_BRANCH_REMOVED_ON_RANGE_STABLE_ARITHMETIC_RECEIVER=true
```

This is an actual structural gain, but not yet a fixed-power whole-family saving: large energy identifies the obstruction; it does not by itself upper-bound it.

## 6. Explicit forced collision equation

Merged 4du gives the plus/plus collision equation. For two divisor states

```text
y_i=r_i s_i,
ell=(r_i^2+s_i^2)/(2x_i),
```

collision at the same mover prime is exactly

```text
boxed:
x_2(r_1^2+s_1^2)=x_1(r_2^2+s_2^2).
```

The minus and mixed branches admit analogous equations after the degree-two representation above.

Thus square-root saturation on the range-stable arithmetic branch now forces near-maximal weighted concentration on a concrete norm-ratio collision variety.

## 7. Remaining receiver

The previous 4du receiver

```text
GaussianMoverCandidateImageOrNormRatioCollisionEnergy
```

contracts on the s arithmetic branch to the single collision receiver

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
RangeStableSubpolynomialGaussianMoverNormRatioCollisionEnergy.
```

The next internal task is to analyze the multiplicity of

```text
x_2(r_1^2+s_1^2)=x_1(r_2^2+s_2^2),
r_i s_i=y_i,
```

under all retained physical masks, and determine whether common factors / proportional solutions account for the forced `B^(1-o(1))` energy or whether the nonproportional part admits a determinant/incidence saving.

## 8. H decision

No new auxiliary H is opened at s7-62.

Reason: merged 4du plus the new range-stable scale peel now force a specific norm-ratio collision equation. The next step is still exact/internal: separate proportional/common-factor collisions from genuinely nonproportional incidences before asking for an external determinant/energy theorem.

```text
S7_62_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_62=COMPLETE_RANGE_STABLE_SUBPOLYNOMIAL_MOVER_AND_FORCED_COLLISION_ENERGY_REDUCTION
MERGED_S7_61_IMPORTED=true
MERGED_4DT_FINITE_CANDIDATE_SUPPORT_IMPORTED=true
MERGED_4DU_IMAGE_ENERGY_DICHOTOMY_IMPORTED=true
RANGE_STABLE_ARITHMETIC_MOVER_PRIME_SCALE=Bo0
FIXED_POWER_ELL_ARITHMETIC_MOVER_EMPTY=true
LOW_DEGREE_DIVISOR_GRAPH_BOUNDARY_PROVED=true
BOUNDARY_DEGREE_IN_ELL_AT_MOST=2
RANGE_STABLE_CANDIDATE_PRIME_IMAGE_SIZE=Bo1
DIFFUSE_B_HALF_CANDIDATE_IMAGE_POSSIBLE=false
RANGE_STABLE_ARITHMETIC_SATURATION_FORCES_COLLISION_ENERGY=true
FORCED_COLLISION_ENERGY_EXPONENT=1
DIFFUSE_IMAGE_BRANCH_REMOVED_ON_RANGE_STABLE_ARITHMETIC_RECEIVER=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_62_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanRangeStableSubpolynomialGaussianMoverNormRatioCollisionEnergy
NEXT=Stage14-s7-63
```
