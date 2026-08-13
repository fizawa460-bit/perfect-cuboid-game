# Stage14-4dy — primitive-slope physical-acceptance principal density

## Status

`COMPLETE_PROJECTIVE_SLOPE_SCALE_OCCUPANCY_TO_FIXED_BOOLEAN_PRINCIPAL_DENSITY`

Consumes merged `Stage14-4dx`, merged `Stage14-s7-64`, merged `Stage14-Work-bkX23`, merged `Stage14-t104`, and latest main. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering receiver

Merged `4dx` transported the fixed-heavy-prime/fixed-root primitive divisor-pair survivor to projective slope/scale coordinates and left the joint occupancy of slope/scale windows with chart/orientation/reciprocal-completion masks as the live receiver.

Merged `s7-64` now resolves the apparent two-coordinate geometry more sharply. Write

```text
r=g a,
s=g b,
gcd(a,b)=1,
0<a<b,
u=a/b.
```

On the surviving primitive-direction family,

```text
g=B^o(1).
```

Hence the reduced rational slope `u=a/b` determines the primitive pair `(a,b)` uniquely; there is no independent polynomial scale coordinate after primitive reduction.

```text
INDEPENDENT_POLYNOMIAL_SCALE_AFTER_PRIMITIVE_REDUCTION=false
RESIDUAL_COMMON_SCALE_MULTIPLICITY=Bo1
```

The `q=s` coordinate of `4dx` is therefore bookkeeping for slope height plus the already-subpolynomial common factor, not a second source of square-root support.

## 2. Archimedean masks become one-variable slope/height windows

For fixed heavy Gaussian mover prime `ell_*` and fixed Gaussian root orientation,

```text
x = g^2(a^2+b^2)/(2 ell_*),
y = g^2 ab,
```

so

```text
x/y = (u+u^(-1))/(2 ell_*),
A/D = (1-u)/(1+u).
```

Thus norm-ratio, angle, balanced/interior, and range masks are transported to `O(1)` positive-width conditions on the reduced rational slope and its height. They do not individually supply a fixed-power deficit on the square-root-scale ambient family.

```text
ARCHIMEDEAN_MASKS_TRANSPORT_TO_PRIMITIVE_SLOPE=true
FIXED_WIDTH_SLOPE_WINDOWS_FIXED_POWER_SPARSE=false
```

The fixed Gaussian root line

```text
a == epsilon_* i_* b (mod ell_*),
ell_*=B^o(1),
```

is likewise already-charged localization and gives no fresh fixed-power loss.

## 3. Chart and orientation labels are finite-fiber localization

The atomic source/target placement for the active plus/minus allocation flip has only `O(1)` core labels and a `B^o(1)` full decoration dictionary. By merged `s7-64` / `Work-bjX22`, one complete mover-chart label may be frozen without fixed-power loss.

The Gaussian root orientation is already frozen as one of two labels.

Hence

```text
ATOMIC_CHART_VARIATION_DISCHARGED_AS_LOCALIZATION=true
ROOT_ORIENTATION_VARIATION_DISCHARGED_AS_LOCALIZATION=true
CHART_OR_ORIENTATION_FIXED_POWER_SAVING_RECHARGE_ALLOWED=false
```

There is therefore no remaining genuine chart/slope coupling at polynomial-support level.

## 4. Reciprocal completion does not factor, but becomes one Boolean acceptance predicate

After fixing

```text
ell_*, root orientation, atomic chart, primitive slope (a:b),
```

the reconstructed cofactor values are fixed up to `B^o(1)` decorations. Balanced six-block allocation has divisor-many `B^o(1)` witnesses when it exists, and reciprocal/post-column completion has `B^o(1)` multiplicity per allocation.

This does **not** imply density saving. Instead define

```text
A_phys(a,b)=1
```

iff at least one allowed subpolynomial decoration, balanced allocation witness, and reciprocal/post-column completion exists for the transported physical point.

Then

```text
PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1
FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true
BOOLEAN_ACCEPTANCE_FACTORIZATION_INTO_INDEPENDENT_SLOPE_AND_SCALE_MASKS_PROVED=false
```

Thus the genuinely coupled remnant is not a two-variable geometric occupancy; it is the arithmetic existence condition encoded by `A_phys` on primitive slopes.

## 5. Principal-density formulation

Let `Omega_G(B)` be the frozen ambient family of primitive slopes in the retained slope/height windows, on the fixed Gaussian root line and fixed chart. Merged `s7-64` / `Work-bkX23` give

```text
|Omega_G(B)| = B^(1/2+o(1)).
```

Define

```text
mu_G := E_{Omega_G} A_phys,
A_phys^circ := A_phys - mu_G.
```

Exactly,

```text
E A_phys^circ = 0,
E |A_phys^circ|^2 = mu_G(1-mu_G).
```

On any square-root-saturating arithmetic subsequence,

```text
#accepted = B^(1/2-o(1)),
```

so necessarily

```text
mu_G = B^(-o(1))
```

in the exponent-zero lower-bound sense.

Therefore the mainline arithmetic branch would close if one proved any fixed `delta>0` with

```text
mu_G <= B^(-delta+o(1)).
```

No such estimate is presently merged.

```text
GLOBAL_ACCEPTANCE_PRINCIPAL_DENSITY_RECEIVER=true
GLOBAL_ACCEPTANCE_DENSITY_EXPONENT_ZERO_ON_SATURATING_SEQUENCE=true
GLOBAL_FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false
```

## 6. What is and is not left

The following are now discharged as independent polynomial supports on this branch:

```text
heavy mover-prime label,
Gaussian root orientation,
collision energy,
proportional scale copies,
projective scale coordinate,
atomic mover-chart label,
reciprocal-completion multiplicity.
```

They remain valid localization/fiber statements but cannot be recharged as independent savings.

The only live mainline arithmetic object is the density of the Boolean physical acceptance predicate on the fixed primitive-slope background family.

New canonical receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChart
PrimitiveRationalSlopeBalancedReciprocalExistencePrincipalDensity.
```

## 7. Next internal split

Before any new H task, the Boolean witness condition must be expanded internally into the actual arithmetic witnesses:

```text
(a) balanced divisor-in-window existence,
(b) disjoint smooth/rough prime-allocation compatibility,
(c) genuinely coupled reciprocal/post-column completion acceptance.
```

The next question is whether one component already has a fixed-power density deficit, or whether exponent-zero acceptance forces one further structured witness family.

## 8. H decision

No new H is opened at `4dy`. The current receiver is explicit enough for one more internal witness decomposition, and no external theorem shape has yet been isolated without losing physical masks.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DY=COMPLETE_PROJECTIVE_SLOPE_SCALE_OCCUPANCY_TO_FIXED_BOOLEAN_PRINCIPAL_DENSITY
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
INDEPENDENT_POLYNOMIAL_SCALE_AFTER_PRIMITIVE_REDUCTION=false
ARCHIMEDEAN_MASKS_TRANSPORT_TO_PRIMITIVE_SLOPE=true
ATOMIC_CHART_VARIATION_DISCHARGED_AS_LOCALIZATION=true
ROOT_ORIENTATION_VARIATION_DISCHARGED_AS_LOCALIZATION=true
PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1
FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true
BOOLEAN_ACCEPTANCE_FACTORIZATION_INTO_INDEPENDENT_SLOPE_AND_SCALE_MASKS_PROVED=false
GLOBAL_ACCEPTANCE_PRINCIPAL_DENSITY_RECEIVER=true
GLOBAL_ACCEPTANCE_DENSITY_EXPONENT_ZERO_ON_SATURATING_SEQUENCE=true
GLOBAL_FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false
SQRT_OBSTRUCTION_REDUCED_TO_PRIMITIVE_SLOPE_PHYSICAL_ACCEPTANCE_PRINCIPAL_DENSITY=true
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4dz`.
