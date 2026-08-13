# Stage14-4dv — fixed-prime collision tautology and single-state divisor-graph mass

## Status

`COMPLETE_FIXED_PRIME_COLLISION_TAUTOLOGY_REDUCTION`

Consumes merged `Stage14-4du`, merged `Stage14-s7-62`, merged `Stage14-Work-biX21`, merged `Stage14-t102`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering heavy-prime receiver

Merged s7-62 removes the diffuse candidate-image branch on the pure range-stable arithmetic receiver:

```text
ell=B^o(1),
|Im(E_arith)|=B^o(1),
Energy>=B^(1-o(1)).
```

Merged Work-biX21 then extracts one heavy Gaussian mover prime

```text
ell_*=B^o(1)
```

carrying

```text
m(ell_*)=B^(1/2-o(1))
```

weighted frozen-state mass.

Thus the mainline arithmetic obstruction can be studied after freezing one prime `ell_*`.

## 2. Plus-state fixed-prime divisor graph

For every plus-state incidence carrying `ell_*`, merged s7-62 gives divisors `r,s` with

```text
rs=y,
r^2+s^2=2 ell_* x.
```

Equivalently

```text
Q(ell_* x,y)=1.
```

Hence the fixed-heavy-prime state set lies on the single-state divisor graph

```text
rs=y,
r^2+s^2=2 ell_* x,
```

with all balanced/range/chart/primitive/reciprocal side masks retained.

The minus-state graph is analogously

```text
ab=y,
ell_*^2 a^2+b^2=2x
```

or its symmetric variant.

```text
FIXED_HEAVY_PRIME_SINGLE_STATE_DIVISOR_GRAPH_EXPLICIT=true
BOUNDARY_DEGREE_IN_FIXED_PRIME_AT_MOST=2
```

## 3. The apparent pair-collision equation becomes tautological

Merged 4du records the plus/plus equal-candidate collision equation

```text
x_2(r_1^2+s_1^2)=x_1(r_2^2+s_2^2).
```

After Work-biX21 freezes the common candidate prime `ell_*`, each participating state already satisfies

```text
r_i^2+s_i^2=2 ell_* x_i.
```

Substitution gives exactly

```text
x_2(2 ell_* x_1)=x_1(2 ell_* x_2),
```

which is an identity.

Therefore the pair-collision equation supplies no fresh determinant, modulus, transversality, or independent incidence condition once the heavy prime has been frozen.

```text
FIXED_PRIME_PLUS_PLUS_COLLISION_EQUATION_TAUTOLOGICAL=true
FRESH_PAIRWISE_DETERMINANT_FROM_COLLISION=false
COLLISION_ENERGY_DOUBLE_CHARGE_ALLOWED=false
```

The same warning applies to any energy argument whose only pair relation is equality of the already-frozen candidate prime: energy concentration localizes the obstruction to one fiber but does not create a second arithmetic equation inside that fiber.

## 4. What the energy gain really proves

The valid content of s7-62 / Work-biX21 is concentration:

```text
square-root arithmetic saturation
=> one ell_*=B^o(1)
=> B^(1/2-o(1)) weighted states satisfy the fixed-prime mover graph.
```

It does **not** imply a new pairwise saving after `ell_*` is fixed.

Thus the collision-energy language is now discharged as a localization device. The live count is the one-fiber state mass itself.

```text
COLLISION_ENERGY_USED_ONLY_FOR_HEAVY_FIBER_EXTRACTION=true
FIXED_PRIME_COLLISION_ENERGY_IS_NOT_FRESH_SAVING_SOURCE=true
```

## 5. New minimal receiver

The range-stable zero-mode arithmetic obstruction contracts to

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianMoverPrimeDivisorGraphStateMass.
```

For the plus branch, estimate uniformly for one fixed

```text
ell_*=B^o(1), ell_* == 1 (mod 4)
```

the weighted physical state mass satisfying

```text
rs=y,
r^2+s^2=2 ell_* x,
```

under every retained physical mask. The minus degree-two divisor graph is included in the same receiver.

A strict sub-square-root saving now requires a fixed-power deficit for this fixed-prime one-state divisor-graph family, or a further decomposition of its proportional/common-factor structure that yields a genuinely new independent condition.

## 6. H decision

No new H is opened at 4dv. The previous proposal to seek a determinant theorem directly for the fixed-prime collision equation is premature because that pair equation is tautological after the heavy-prime freeze.

The next step is internal: parameterize the fixed-`ell_*` divisor graph itself and determine whether its apparent square-root state mass is already divisor-many/fiberwise finite or whether one genuinely two-dimensional physical parameter remains.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DV=COMPLETE_FIXED_PRIME_COLLISION_TAUTOLOGY_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MERGED_S7_62_DIFFUSE_BRANCH_REMOVAL_IMPORTED=true
MERGED_WORK_BIX21_HEAVY_PRIME_IMPORTED=true
GLOBAL_HEAVY_MOVER_PRIME_SCALE=Bo0
GLOBAL_HEAVY_MOVER_STATE_MASS_EXPONENT=1/2
FIXED_HEAVY_PRIME_SINGLE_STATE_DIVISOR_GRAPH_EXPLICIT=true
FIXED_PRIME_PLUS_PLUS_COLLISION_EQUATION_TAUTOLOGICAL=true
FRESH_PAIRWISE_DETERMINANT_FROM_COLLISION=false
COLLISION_ENERGY_USED_ONLY_FOR_HEAVY_FIBER_EXTRACTION=true
SQRT_OBSTRUCTION_REDUCED_TO_FIXED_PRIME_DIVISOR_GRAPH_STATE_MASS=true
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4dw`.
