# Stage14-4du — candidate-image / collision-energy dichotomy

## Status

`COMPLETE_MOVER_CANDIDATE_IMAGE_ENERGY_DICHOTOMY_NO_FORCED_COLLISION`

Consumes merged `Stage14-4dt`, merged `Stage14-4ds`, merged `Stage14-s7-61`, and merged `Stage14-Work-bhX20` on latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering finite-candidate map

Merged 4dt proves that for every frozen cofactor state `s=(x,y,...)`, the set of Gaussian split-prime mover candidates has cardinality

```text
#Cand(s)=B^o(1).
```

For a plus-state factorization `y=rs`, with

```text
D=(r+s)/2,
A=(s-r)/2,
```

the candidate is

```text
ell = (D^2+A^2)/x
    = (r^2+s^2)/(2x).
```

The minus-state representation gives an analogous finite representation map. All physical side masks remain retained.

Let `E` be the charged-once incidence set of pairs `(s,ell)` for which `ell` is an actual physical mover candidate of state `s`.

## 2. First and second moments

Write

```text
m(ell)=#{s : (s,ell) in E}
```

with the physical packet weights absorbed into the state multiplicity convention. Then

```text
I := |E| = sum_ell m(ell),
Energy := sum_ell m(ell)^2.
```

Since each state contributes only `B^o(1)` candidates, square-root saturation is compatible with

```text
I = B^(1/2-o(1)).
```

Cauchy gives the exact general inequality

```text
I^2 <= |Im(E)| * Energy,
```

where `|Im(E)|` is the number of distinct candidate primes occurring across the frozen states.

Thus large total incidence forces either a large candidate-prime image or large collision energy, but not collision energy alone.

```text
CANDIDATE_FIRST_SECOND_MOMENT_DICHOTOMY_PROVED=true
SATURATION_FORCES_COLLISION_ENERGY_ALONE=false
```

## 3. Explicit collision equation

For two plus-state factorizations

```text
y_i=r_i s_i,
ell=(r_i^2+s_i^2)/(2x_i),
```

collision at the same candidate prime is equivalent to

```text
x_2 (r_1^2+s_1^2) = x_1 (r_2^2+s_2^2).
```

Therefore the collision branch is a norm-ratio incidence problem between two frozen divisor states. This equation is fresh as a cross-state equality, but it is not yet known to have fixed-power sparse solution count under the retained physical masks.

The same conclusion holds for mixed plus/minus candidate descriptions after writing the corresponding sum-of-two-squares representation data.

```text
PLUS_CANDIDATE_COLLISION_EQUATION_EXPLICIT=true
COLLISION_EQUATION_FIXED_POWER_SAVING_PROVED=false
```

## 4. Diffuse branch is genuinely live

There is no merged theorem forcing many different frozen states to reuse the same `ell`. A configuration with

```text
m(ell)=O(B^o(1))
```

for every candidate prime and

```text
|Im(E)|=B^(1/2-o(1))
```

is consistent with all current reductions. In such a diffuse regime

```text
Energy=B^(1/2+o(1)),
```

so a collision estimate by itself need not improve the whole-family exponent.

Hence any next saving theorem must control at least one of the two branches:

```text
DIFFUSE IMAGE:
  bound the number/weighted mass of distinct divisor-generated Gaussian mover primes;

COLLISION ENERGY:
  bound repeated candidate values via the norm-ratio collision equation.
```

Neither branch may be discarded by pigeonhole without an additional bound on `|Im(E)|` or `Energy`.

```text
DIFFUSE_CANDIDATE_IMAGE_BRANCH_RETAINED=true
COLLISION_ENERGY_BRANCH_RETAINED=true
FORCED_HIGH_MULTIPLICITY_CANDIDATE_PRIME=false
```

## 5. New minimal receiver

The weighted concentration obstruction from 4dt is therefore sharpened to

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
GaussianMoverCandidateImageOrNormRatioCollisionEnergy.
```

This is a true dichotomy, not two independent savings. A future proof may close either branch and then re-optimize the other, but cannot multiply bounds from alternative descriptions of the same incidence mass.

## 6. H decision

No new H is opened at 4du. The collision equation and diffuse image map are now explicit enough for one more internal arithmetic audit: determine whether the image map has a growing-modulus constraint or whether the collision equation reduces to a known determinant/energy form already present in Stage14. External literature should be invoked only after that identification.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DU=COMPLETE_MOVER_CANDIDATE_IMAGE_ENERGY_DICHOTOMY_NO_FORCED_COLLISION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FIXED_FROZEN_STATE_MOVER_PRIME_CANDIDATE_COUNT=Bo1
CANDIDATE_FIRST_SECOND_MOMENT_DICHOTOMY_PROVED=true
PLUS_CANDIDATE_COLLISION_EQUATION_EXPLICIT=true
SATURATION_FORCES_COLLISION_ENERGY_ALONE=false
DIFFUSE_CANDIDATE_IMAGE_BRANCH_RETAINED=true
COLLISION_ENERGY_BRANCH_RETAINED=true
FORCED_HIGH_MULTIPLICITY_CANDIDATE_PRIME=false
SQRT_OBSTRUCTION_REDUCED_TO_CANDIDATE_IMAGE_OR_COLLISION_ENERGY=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4dv`.
