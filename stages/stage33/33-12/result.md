# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_FULL_GEOMETRIC_LERAY_SHA_COCYCLE_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The marked Brauer functional is still one of the three nonzero functionals.

## IMPORTANT revocation: constant d=2 is not the named J2 torsor

The previous promotion

```text
partial norm squareclass = 2
=> named Leray/Sha squareclass d=2
```

is invalid. J2 is already certified geometrically nontrivial in `Br(Kc_bar)[2]`. But `2` is a square after base change to `Qbar`, so a 2-isogeny covering with constant squareclass `d=2` becomes trivial over `Qbar(t)`. It therefore cannot represent the geometric J2 torsor.

Exact rejection certificate:

```text
j2-d2-geometric-nontriviality-rejection.json
canonical SHA256 = 8e128315159812ec709c79840bd46e213df3cb22512056478294c8f4fa637d78
```

Thus

```text
J2_2ISOGENY_SQUARECLASS_SELECTED=false
J2_2ISOGENY_KERNEL_MEMBERSHIP_CERTIFIED=false
J2_TORSOR_EQUATION_MATERIALIZED=false
PARTIAL_NORM_SQUARECLASS_2=ARITHMETIC_DESCENT_DATUM_ONLY
```

The old `d=2` fiber/lattice computation is retained only as a computation for that generic candidate; it has no named-J2 credit.

## NEW exact geometric half-divisor pushforward

On the branch normalization

```text
C: z^2=t^4-6*t^2+1,
E_J2=2*infinity_minus-P_plus-P_minus,
P_plus: t=1+sqrt(2),
P_minus: t=1-sqrt(2).
```

For `pi:C->P1_t`, exact pushforward gives

```text
pi_*(E_J2)=2*infinity-r_plus-r_minus.
```

Since

```text
Dplus=t^2-2*t-1,
div(Dplus)=r_plus+r_minus-2*infinity,
```

we obtain the exact identity

```text
pi_*(E_J2) = -div(Dplus).
```

Therefore `Dplus` is the unique geometrically nonconstant squareclass with the finite odd-valuation support forced by the named J2 half-divisor, up to constants (which are squares over `Qbar`). In particular, unlike constant `2`, `Dplus` remains nonsquare over `Qbar(t)`.

Certificate:

```text
j2-geometric-halfdivisor-base-squareclass.json
canonical SHA256 = 876734d9c1263150666d120c55c2d836fac74b2fb04168197c0845854a6f142d
```

This does **not yet** promote `Dplus` to the full Leray/Ogg-Shafarevich torsor coordinate. The remaining adapter is now precise:

```text
PROVE_THE_LERAY_OGG_SHA_EDGE_MAP_IDENTIFIES
THE_HALFDIVISOR_PUSHFORWARD_SQUARECLASS_DPLUS
WITH_THE_NAMED_CLASS_XI_J2.
```

If that adapter is exact, the geometric torsor coordinate is forced to `Dplus` and only then should arithmetic descent back to `Q(t)` be performed.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
J2 2-isogeny squareclass selected = false
J2 torsor equation materialized = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
