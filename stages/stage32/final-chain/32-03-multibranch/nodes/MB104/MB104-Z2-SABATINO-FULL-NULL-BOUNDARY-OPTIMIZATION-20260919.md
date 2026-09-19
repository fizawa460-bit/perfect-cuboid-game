# MB104 Z2 — Sabatino optimization over the complete null/exceptional boundary family — 2026-09-19

Status: **PARALLEL PRE-AUDIT SOURCE-VALID NATURAL-BOUNDARY NO-GO / NO CREDIT**

## Purpose

Z35 optimized Sabatino Theorem 1.1(i) over arbitrary subsets of the 48 exceptional curves.
After the Z3 complete-null-locus theorem, there is a stronger natural boundary family:

```text
any reduced SNC subset of
  {48 exceptional curves}
  union
  {zero-pairing elliptic quartics for the balanced support}.
```

This note optimizes the source-valid inequality over that entire finite family.

It does not claim to optimize over arbitrary unrelated curves on the surface.

## 1. Sabatino polynomial

Let

```text
C=lP,  P=7H-4 sum_(i in Sigma)E_i,  |Sigma|=14.
```

For a chosen reduced boundary D, write

```text
t = number of selected supported exceptional curves,
u = number of selected unsupported exceptional curves,
r = t+u,
q = number of selected zero elliptic quartics,
I = number of transverse intersection points among selected boundary components.
```

Every zero quartic and every unsupported exceptional is P-null, hence disjoint from an
irreducible C.  Each selected supported exceptional meets C in exactly 8l reduced normalization
points.

Therefore

```text
C^2 = 336l^2,
(K+D).C = (112+8t)l,
e(C\D) = -8tl.
```

The quadratic and linear parts of Sabatino Theorem 1.1(i) become exactly

```text
168l(l+1) alpha^2 - (224-8t)l alpha.
```

For the constant term, because the exceptional curves are rational, the zero quartics are
elliptic, and the retained boundary configurations are SNC,

```text
e(D)=2r-I,
K.D=4q,
D^2=-2r-4q+2I.
```

Hence

```text
G(D)
 = 3e(S\D) - (K+D)^2
 = 224 - 4r - 4q + I.
```

Thus the exact inequality to optimize is

```text
F_D(alpha)
 = 168l(l+1)alpha^2
   -(224-8t)l alpha
   +224-4r-4q+I
 >=0.
```

The vertex is always in [0,1] for the finite cases below, and

```text
F_D,min
 = G(D)
   - ((224-8t)^2/672) * l/(l+1).
```

## 2. Exact finite boundary replay

The complete null-locus incidence is already known.

### Size-48 supports

There are:

- 34 unsupported exceptionals;
- 14 supported exceptionals;
- four zero quartics;
- the quartics are pairwise disjoint;
- each quartic passes through seven supported nodes and one unsupported node;
- the four omitted-node incidences form two repeated pairs, so an unsupported exceptional may meet
  at most two selected zero quartics.

Exhausting all choices of the four quartics and fourteen supported exceptionals, while also allowing
every subset of the unsupported exceptionals, gives the global optimum:

```text
u=34,
t=0,
q=4,
I=4,
G=76.
```

Equivalently: select the complete P-null boundary and no supported exceptional.

Then

```text
F_min(l)
 = 76 - (224/3) l/(l+1)
 = 4(l+57)/(3(l+1))
 > 4/3.
```

So the inequality remains strictly satisfied for every l>=1.

The same optimum applies to both size-48 support orbits.

### Surviving size-768 support

There are:

- 34 unsupported exceptionals;
- 14 supported exceptionals;
- two zero quartics;
- the two quartics meet at two smooth non-box points;
- each quartic also meets its one omitted unsupported exceptional.

The exact finite replay gives

```text
u=34,
t=0,
q=2,
I=4,
G=84.
```

Again this is the complete P-null boundary and no supported exceptional.

Hence

```text
F_min(l)
 = 84 - (224/3) l/(l+1)
 = 28(l+9)/(3(l+1))
 > 28/3.
```

So this orbit is also strictly compatible for every l>=1.

## 3. Consequence

Adding the newly classified zero-quartic null boundary makes Sabatino substantially sharper than
the exceptional-only Z35 test, especially on the size-48 supports, but it still does not cross the
required sign.

The best asymptotic margins are

```text
size48:       4/3,
surviving768: 28/3.
```

Therefore the source-valid Sabatino open-surface route is exhausted on the complete natural
null/exceptional boundary family for the three balanced uniform survivors.

A future Z2 revival would need a genuinely different boundary component or a different
canonical-degree theorem, not another subset of the now-complete null configuration.

## Source locks

- Z35 direct Sabatino application / theorem-formula source;
- Z3 complete P-null-locus theorem;
- archived zero-quartic incidence data.

External source:
P. Sabatino, *An Explicit Bound for the Log-Canonical Degree of Curves on Open Surfaces*,
PRIMS 58 (2022), Theorem 1.1(i).

## Firewalls

```text
Sabatino_complete_null_boundary_closes=false
Sabatino_natural_boundary_family_exhausted=true
arbitrary_unrelated_boundary_curves_not_optimized=true
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
