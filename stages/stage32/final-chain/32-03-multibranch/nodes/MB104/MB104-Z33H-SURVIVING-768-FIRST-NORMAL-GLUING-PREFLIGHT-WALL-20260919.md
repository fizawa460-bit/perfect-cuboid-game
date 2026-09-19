# MB104 Z33H — surviving-768 first-normal-neighborhood gluing preflight wall — 2026-09-19

Status: **PRE-AUDIT FIRST-ORDER INTERFACE WALL / NO CREDIT**

## Input

After Z33G the surviving size-768 canonical support is

```text
000707000f0f.
```

Its two zero-pairing elliptic quartics `A,B` meet in exactly two smooth points and the ordinary reducible-union Picard holonomy of `O(P)` is

```text
h=1.
```

Thus

```text
O_{A union B}(P) ~= O_{A union B}.
```

The ordinary `Pic^0` obstruction is exhausted on this support.

## First infinitesimal neighborhood

Put

```text
U=A union B.
```

For the first infinitesimal neighborhood `2U`, the standard units sequence has kernel

```text
I_U/I_U^2 ~= O_U(-U),
```

so after fixing the trivial restriction on `U`, a possible first-order obstruction lies in

```text
H^1(U,O_U(-U)).
```

The exact intersection numbers are

```text
A^2=B^2=-4,
A.B=2.
```

Hence

```text
deg O_A(-U)=deg O_B(-U)=2.
```

Both components are elliptic, so

```text
H^1(A,O_A(-U))=H^1(B,O_B(-U))=0.
```

Therefore any first-order obstruction is purely a two-intersection-cycle gluing phenomenon; there is no independent componentwise first-order obstruction.

Equivalently, the normalization exact sequence shows that the remaining obstruction space is controlled entirely by the comparison of normal-direction transition data at the two common points. It is at most the single cycle contribution.

## Why Z33G data are insufficient for this class

Z33G computes the ordinary transition using

```text
g(r)=f_B(r)/f_A(r)
```

and compares only the two values

```text
g(r_+), g(r_-).
```

For the surviving support those values agree.

A first-neighborhood class requires one order more: after ordinary gluing has been normalized, one must compute the transition in

```text
1 + I_U/I_U^2,
```

i.e. the normal-direction coefficient of the ambient transition at each intersection point, with the two coefficients compared in the globally normalized conormal line bundle.

No retained Stage32 source currently identifies that coefficient or supplies the required normalization of the two normal directions across the elliptic components. Repository search found no first-neighborhood / formal-Picard adapter for the retained `C2` quartics.

The explicit Stoll--Testa equations make such a new calculation conceivable, but it is no longer a shallow reuse of retained data.

## Disposition

```text
ordinary null-union Pic0 holonomy = trivial,
componentwise first-order H1       = zero,
possible cycle first-order class   = not source-locked,
size-768 orbit excluded here       = false.
```

Z33H is parked rather than guessing a derivative normalization.

## Routing

The finite null-locus route has now produced one genuine orbit elimination and reached a first-normal-neighborhood interface on the remaining size-768 orbit.

Following the current Z1--Z30 re-audit, rotate to the other directly executable Tier-1 route:

```text
MB104-Z34-Z12-BTVA-GENERAL-M-SUPPORT-HILBERT-PREFLIGHT
```

Target: recover the published perfect-cuboid BTVA ancillary/general-`m` implementation surface and determine whether support-specific graded growth at `N=14` can be computed after quotienting the known support-hyperplane-generated submodule.

## Firewalls

```text
first_normal_obstruction_computed=false
surviving_768_excluded=false
remaining_balanced_support_count=864
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
