# Stage14-Work-bjX22 — fixed heavy prime, fixed Gaussian root, primitive-direction mass

## Status

`COMPLETE_FIXED_HEAVY_PRIME_ROOT_ORIENTATION_PRIMITIVE_DIRECTION_CONTRACTION`

Consumes merged `Stage14-Work-biX21`, merged `Stage14-4dw`, merged `Stage14-s7-63`, merged `Stage14-t103`, and latest main. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering global receiver

Merged Work-biX21 proves that on a square-root-saturating range-stable arithmetic subfamily one may freeze a single Gaussian mover prime

```text
ell_* = B^o(1)
```

carrying weighted state mass

```text
M(ell_*) = B^(1/2-o(1)).
```

Merged 4dw reconstructs every live plus-state from one primitive divisor pair

```text
r < s,
gcd_odd(r,s)=1,
r^2+s^2 = 2 ell_* x,
rs=y,
```

up to `B^o(1)` frozen gcd / endpoint decoration, and shows that the fixed Gaussian root condition is exactly

```text
r == + i_* s (mod ell_*)
```

or

```text
r == - i_* s (mod ell_*),
```

with exactly two root orientations.

Merged s7-63 proves that one proportional primitive direction carries only `B^o(1)` charged-once physical mass.

## 2. Square-root mass forces square-root many primitive directions

Write the primitive complementary direction of a state as

```text
dir(r,s) = (r0:s0),
```

where `(r,s)=g(r0,s0)`, `g=B^o(1)`, and `gcd(r0,s0)=1` under the fixed positive ordering convention.

Let `D_*` be the set of primitive directions represented among states attached to `ell_*`. By merged s7-63, for every direction `d`,

```text
mass(d) <= B^o(1).
```

Since

```text
sum_{d in D_*} mass(d) = M(ell_*) = B^(1/2-o(1)),
```

we obtain

```text
|D_*| >= M(ell_*) / B^o(1) = B^(1/2-o(1)).
```

Thus the heavy-prime obstruction cannot be explained by repeated scale copies of only subpolynomially many primitive directions.

```text
GLOBAL_PRIMITIVE_DIRECTION_COUNT_EXPONENT=1/2
GLOBAL_SQRT_MASS_REQUIRES_SQRT_MANY_PRIMITIVE_DIRECTIONS=true
SUBPOLYNOMIAL_DIRECTION_IMAGE_COMPATIBLE_WITH_SQRT_SATURATION=false
```

This is a counting contraction, not a new fixed-power saving.

## 3. One Gaussian root orientation can also be frozen

The two root orientations partition the fixed-prime state mass:

```text
M(ell_*) = M_+ + M_-.
```

Hence one sign `epsilon_* in {+1,-1}` satisfies

```text
M_{epsilon_*} >= M(ell_*)/2 = B^(1/2-o(1)).
```

Because each proportional primitive direction still carries only `B^o(1)` mass after this restriction, the selected orientation contains

```text
B^(1/2-o(1))
```

distinct primitive directions.

Therefore, without exponent loss, the global arithmetic survivor may be localized simultaneously to

```text
ell_* = B^o(1) fixed,
epsilon_* fixed,
r == epsilon_* i_* s (mod ell_*),
B^(1/2-o(1)) distinct primitive directions (r0:s0).
```

```text
GLOBAL_FIXED_GAUSSIAN_ROOT_ORIENTATION_PROVED=true
GLOBAL_FIXED_ROOT_ORIENTATION_STATE_MASS_EXPONENT=1/2
GLOBAL_FIXED_ROOT_ORIENTATION_DIRECTION_COUNT_EXPONENT=1/2
GLOBAL_PRIME_AND_ROOT_CAN_BE_FROZEN_SIMULTANEOUSLY=true
```

The fixed congruence modulo `ell_*` is already charged Gaussian mover structure and gives no fresh fixed-power loss because `ell_*=B^o(1)`.

## 4. Collision energy is now discharged as a localization device

Merged s7-62 forced exponent-one collision energy. Merged Work-biX21 used subpolynomial prime support to freeze `ell_*`. Merged 4dv showed that the fixed-prime pair-collision equation is tautological, and merged s7-63 showed that proportional collision classes cannot account for the forced energy while the nonproportional pair relation adds no fresh codimension.

The legal conclusion is therefore the one-state primitive-direction mass statement above. The following are alternative descriptions of the same surviving incidence mass and may not be multiplied as independent savings:

```text
heavy-prime mass,
forced collision energy,
nonproportional collision energy,
primitive-direction count.
```

```text
COLLISION_ENERGY_DISCHARGED_AS_LOCALIZATION=true
NONPROPORTIONAL_ENERGY_NOT_AN_INDEPENDENT_SAVING=true
HEAVY_PRIME_DIRECTION_COUNT_DOUBLE_CHARGE_FORBIDDEN=true
```

## 5. Relation to fixed-U t103

Merged t103 independently proves that a `B^o(1)` packet-wide dictionary of SIGN/DIV/PROJ selector labels contains one common elementary boundary skeleton carrying exponent-zero prime-average incidence. This and the global root-orientation freeze share one abstract principle:

```text
exponent-zero / square-root mass
+ B^o(1) or O(1) label dictionary
=> one label may be frozen without fixed-power loss.
```

Accordingly

```text
COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_PROVED=true
```

at the combinatorial level.

But the arithmetic objects remain different:

- global: one fixed subpolynomial Gaussian prime, one fixed Gaussian root orientation, and a square-root-scale family of primitive divisor-pair directions with transported physical masks;
- fixed-U: one common selector skeleton across a subpolynomial generic-prime family, with prime-dependent Gaussian slope / residue / projective actions and two-level centering.

No finite-fiber arithmetic map identifies these receivers.

```text
COMMON_ARITHMETIC_MASK_ADAPTER_PROVED=false
GLOBAL_FIXED_U_SAVING_CROSS_PROMOTED=false
```

## 6. New canonical global arithmetic receiver

The range-stable arithmetic branch contracts to

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimeFixedRootPrimitiveDivisorDirectionPhysicalMaskMass.
```

For the plus branch:

```text
ell_* = B^o(1) fixed,
epsilon_* in {+1,-1} fixed,
r < s,
gcd_odd(r,s)=1,
r == epsilon_* i_* s (mod ell_*),
x=(r^2+s^2)/(2ell_*),
y=rs,
```

with `B^(1/2-o(1))` distinct primitive directions and every balanced/range/chart/orientation/reciprocal-completion mask transported from the original physical packet.

The next internal task is not another collision estimate. It is to transport the surviving physical masks explicitly into fixed-prime/fixed-root primitive divisor-pair coordinates and determine whether one of those masks has a genuine fixed-power density deficit.

```text
NEXT_INTERNAL_TARGET=FixedPrimeFixedRootPrimitiveDivisorPairPhysicalMaskTransportLemma
```

## 7. H decision

No new H is opened. The theorem shape has just contracted from collision energy to a one-state two-variable primitive family. External theorem matching is premature until the transported physical-mask geometry is explicit.

```text
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH28_NEEDED=false
```

## Boundary

```text
STAGE14_WORK_BJX22=COMPLETE_FIXED_HEAVY_PRIME_ROOT_ORIENTATION_PRIMITIVE_DIRECTION_CONTRACTION
GLOBAL_PRIMITIVE_DIRECTION_COUNT_EXPONENT=1/2
GLOBAL_SQRT_MASS_REQUIRES_SQRT_MANY_PRIMITIVE_DIRECTIONS=true
GLOBAL_FIXED_GAUSSIAN_ROOT_ORIENTATION_PROVED=true
GLOBAL_FIXED_ROOT_ORIENTATION_STATE_MASS_EXPONENT=1/2
GLOBAL_FIXED_ROOT_ORIENTATION_DIRECTION_COUNT_EXPONENT=1/2
GLOBAL_PRIME_AND_ROOT_CAN_BE_FROZEN_SIMULTANEOUSLY=true
COLLISION_ENERGY_DISCHARGED_AS_LOCALIZATION=true
NONPROPORTIONAL_ENERGY_NOT_AN_INDEPENDENT_SAVING=true
HEAVY_PRIME_DIRECTION_COUNT_DOUBLE_CHARGE_FORBIDDEN=true
COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_PROVED=true
COMMON_ARITHMETIC_MASK_ADAPTER_PROVED=false
GLOBAL_FIXED_U_SAVING_CROSS_PROMOTED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH28_NEEDED=false
NEXT_INTERNAL_TARGET=FixedPrimeFixedRootPrimitiveDivisorPairPhysicalMaskTransportLemma
```
