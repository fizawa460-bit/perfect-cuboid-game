# MB104 — minimum fibration degree and degree-8 exhaustiveness — 2026-09-19

Status: **SOURCE-COMPLETE LOW-DEGREE FIBRATION BOUND / ZERO CREDIT / NO MERGE**

## Purpose

Close the possibility that the 32-01 -> 32-03 import can be strengthened merely by finding an
unknown genus-(g) fibration on the cuboid surface with hyperplane degree smaller than the known
genus-5 fibrations.

Let (S) be the minimal desingularization of the cuboid surface and (H=K_S) the hyperplane
class.  Let (F) denote the class of a smooth general fiber of a fibration
(S	o B).

Then

```text
F^2=0
```

and adjunction gives

```text
2g(F)-2 = (K_S+F).F = H.F.
```

Thus the hyperplane degree of an integral general fiber is even.

## 1. No fiber degree below 8

The 2026 Stoll--Testa low-degree classification gives:

- all integral curves of degree at most six are classified;
- there are no integral curves of degree six;
- the degree-two curves are the known conics;
- the degree-four curves in the relevant low-dimensional spans are the known genus-one quartics.

The known degree-two and degree-four curves have negative self-intersection (in particular the
conics and elliptic quartics have self-intersection (-4)), so none can be a general fiber with
(F^2=0).

Odd degrees do not occur on the cuboid surface.

Therefore any fibration with integral general fiber satisfies

```text
H.F >= 8.
```

Equivalently the general-fiber genus satisfies

```text
g(F) >= 5.
```

So there is no hidden genus-2, genus-3, or genus-4 fibration that could beat the degree-eight
rank-3 fibrations.

## 2. Every degree-8 fibration is one of the known 28

Assume now

```text
H.F=8.
```

Adjunction gives

```text
g(F)=5.
```

For a smooth general fiber, the restriction of the surface hyperplane bundle is

```text
H|F = K_F
```

because (F|F) is trivial.

The surface embedding therefore realizes the general fiber by its canonical series.  Since the
fiber is already embedded in projective space, it is non-hyperelliptic and its canonical image is
a genus-five canonical curve spanning a (mathbf P^4).

Stoll--Testa Theorem 16(3) classifies every integral curve on the cuboid surface spanning a
(mathbf P^4):

```text
it has degree 8 and is a fiber of one of the 28 fibrations from Section 5.
```

Consequently:

```text
every fibration with H.F=8 is one of the known 28 genus-five fibrations.
```

This upgrades the previous full-28 audit from

```text
"the 28 known fibrations have no better degree"
```

to the source-complete statement

```text
"there is no other degree-eight fibration outside the known 28."
```

## 3. Combined with the balanced P-intersection audit

The previous MB104 full-28 audit gives:

### two size48 support orbits

```text
rank-3 P.G:
(24,56,56,32,56,56)

rank-4 P.G:
56 repeated 22 times.

minimum P.G = 24.
```

### surviving size768 support orbit

```text
rank-3 P.G:
(40,40,56,44,44,56)

rank-4 P.G:
56 repeated 22 times.

minimum P.G = 40.
```

Since every degree-eight fibration is among these 28, these are the exact minima among **all**
degree-eight fibrations:

```text
min_{H.F=8} P.F = 24  on the size48 pair,
min_{H.F=8} P.F = 40  on the size768 survivor.
```

The corresponding best elliptic-normalization ramification budgets remain

```text
48l  (size48),
80l  (size768).
```

## 4. What remains open

This does not classify fibrations with

```text
H.F >= 10.
```

A higher-degree isotropic nef class could in principle have smaller (P.F) if it has sufficiently
large incidence with the balanced support.

Therefore the next lattice question is no longer

```text
"are there unknown lower-degree fibrations?"
```

That route is closed.

The exact remaining question is:

```text
Does there exist a primitive nef isotropic class F with
H.F >= 10
but
P.F < 24  (size48)
or
P.F < 40  (size768)?
```

This is now a bounded-by-objective Picard64 search problem rather than an unstructured search for
new fibrations.

A successful negative answer would prove that the rank-3 fibrations used in the conductor/polar
adapter are globally optimal for the balanced hard core.

## Sources

- M. Stoll and D. Testa, *Curves on the surface of cuboids*, Math. Comp. (2026),
  especially Theorems 16 and 17 and the complete classification of integral curves of degree at
  most six.
- Stoll--Testa, *The surface parametrizing cuboids*, Section 5, for the 28 genus-five fibrations.

## Firewalls

```text
all_degree8_fibrations_exhausted=true
all_higher_degree_fibrations_classified=false
global_min_P_dot_fiber_proved=false
main_credit_changed=false
theorem_credit=false
endpoint_credit=false
MB104_complete=false
merge_authorized=false
```
