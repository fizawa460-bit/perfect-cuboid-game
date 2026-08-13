# Stage14-4ds — Gaussian split-prime two-square mover-density reduction

## Status

`COMPLETE_GAUSSIAN_SPLIT_PRIME_MOVER_DENSITY_REDUCTION_NO_THIN_RESIDUE_SAVING`

Consumes merged `Stage14-4dr`, merged `Stage14-s7-61`, merged `Stage14-Work-bhX20`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering single-prime receiver

Merged 4dr reduces the zero-mode arithmetic square-root obstruction to one active split-prime allocation bit `ell` acting on two candidate product states. With all other allocation bits and side masks frozen, physical arithmetic admissibility is

```text
Q(X,Y)
 = 1_{(X+Y)/2 square}
   1_{(X-Y)/2 square}.
```

The local influence is the symmetric difference of `Q` between the two `ell`-allocation states. Reciprocal completion has only `B^o(1)` multiplicity and is not an independent fixed-power coordinate.

## 2. Exact local congruence calculation from merged s7-61

Merged s7-61 writes the two states, after absorbing the frozen cofactor data into coprime positive integers `x,y`, as

```text
state + : (ell*x, y),
state - : (x, ell*y),
gcd(ell,2xy)=1.
```

If the plus state is admissible, then

```text
ell*x = D_+^2 + A_+^2,
y     = D_+^2 - A_+^2,
```

and therefore modulo `ell`

```text
D_+^2 + A_+^2 = 0.
```

On units this forces a square root of `-1` modulo `ell`, hence generic influential primes satisfy

```text
ell == 1 (mod 4).
```

This is exactly the already-charged Gaussian split-prime support. It is positive-density prime support and does not yield a growing-modulus residue restriction.

```text
GAUSSIAN_SPLIT_PRIME_SUPPORT_IMPORTED=true
FRESH_THIN_RESIDUE_SUPPORT_PROVED=false
LOCAL_CONGRUENCE_DOUBLE_CHARGE_ALLOWED=false
```

## 3. Stabilizer/mover interpretation

Merged Work-bhX20 supplies the common prime-action language. For the present global route, call `ell` a stabilizer on a frozen packet when the two allocation states have identical physical acceptance, and a mover when the acceptance changes.

Then

```text
Influence_ell
 = mass( Q(state 0) XOR Q(state 1) )
```

is exactly the mover density for that prime action. Stabilizers have zero contribution by definition. Since merged 4dr already localizes square-root saturation to exponent-zero single-prime influence, every square-root-saturating zero-mode arithmetic sequence must contain an active Gaussian split prime with exponent-zero mover density.

```text
GLOBAL_SINGLE_PRIME_MOVER_LANGUAGE_IMPORTED=true
SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_GAUSSIAN_MOVER_DENSITY=true
```

## 4. Why simultaneous two-state energy is not yet chargeable

If both allocation states were admissible simultaneously, the four square equations would create a stronger collision/energy packet. Such a packet may admit additional determinant, character, or finite-energy control.

But the influence event is XOR, not intersection. Exponent-zero mover density can in principle be carried by packets where exactly one state is admissible and the simultaneous-admissibility mass is negligible.

Therefore

```text
SIMULTANEOUS_TWO_STATE_COLLISION_STRONGER_THAN_MOVER_EVENT=true
EXPONENT_ZERO_MOVER_IMPLIES_COLLISION_DENSITY=false
COLLISION_ENERGY_SAVING_CHARGEABLE=false
```

No theorem-level saving may be imported from a collision subfamily without a new bridge.

## 5. Exhaustion of the ordinary residue route

The local residue calculation gives only Gaussian splitting. Thus the following route is now exhausted as a source of a new fixed power:

```text
single-prime influence
 -> local congruence modulo ell
 -> thin residue class for ell.
```

The remaining problem is statistical/energetic rather than congruence-thinness: how frequently does an already-eligible Gaussian split prime move the two-square physical boundary after all complementary allocation data and side masks are frozen?

The minimal mainline receiver is therefore

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
SingleGaussianSplitPrimeTwoSquarePhysicalMoverDensityOrEnergy.
```

This agrees with the integrated Work-bhX20 target `PrimeMoverDensityOrEnergyLemma`, but no fixed-U result is cross-promoted.

## 6. H decision

No new mainline H is opened at 4ds. The newly exposed object is an internal prime-action density/energy statistic. Before an external theorem audit, one still needs an exact representation of mover density as either

```text
(a) a short interval / boundary-length condition in ell,
(b) a chargeable two-state collision or second-moment energy,
(c) a low-degree polynomial/congruence boundary in frozen cofactor coordinates,
(d) a character/Hecke correlation with a genuine nonprincipal phase.
```

None is yet proved on merged main.

## Boundary

```text
STAGE14_4DS=COMPLETE_GAUSSIAN_SPLIT_PRIME_MOVER_DENSITY_REDUCTION_NO_THIN_RESIDUE_SAVING
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SINGLE_PRIME_TWO_SQUARE_INFLUENCE_IMPORTED=true
GAUSSIAN_SPLIT_PRIME_SUPPORT_IMPORTED=true
FRESH_THIN_RESIDUE_SUPPORT_PROVED=false
LOCAL_CONGRUENCE_ONLY_REPRODUCES_EXISTING_GAUSSIAN_SUPPORT=true
GLOBAL_SINGLE_PRIME_MOVER_LANGUAGE_IMPORTED=true
SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_GAUSSIAN_MOVER_DENSITY=true
SIMULTANEOUS_TWO_STATE_COLLISION_STRONGER_THAN_MOVER_EVENT=true
EXPONENT_ZERO_MOVER_IMPLIES_COLLISION_DENSITY=false
COLLISION_ENERGY_SAVING_CHARGEABLE=false
MAINLINE_MOVER_DENSITY_FIXED_POWER_DEFICIT_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanSingleGaussianSplitPrimeTwoSquarePhysicalMoverDensityOrEnergy
NEXT=Stage14-4dt
```
