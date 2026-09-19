# MB104 Z3 — Birkar semiampleness / exact null contraction gate — 2026-09-19

Status: **PARALLEL PRE-AUDIT SEMIAMPLENESS REDUCTION / NO RECEIVER CREDIT**

## Purpose

Finish the original Z3 effective-cone/contraction direction for the three surviving balanced
incidence-16 uniform rays.

Retained exact inputs now give:

```text
P = 7H - 4 sum_(i in Sigma) E_i,
P^2 = 336,
P nef,
Null(P) completely classified,
O(P) formally trivial along the retained zero-quartic cores.
```

The remaining issue is whether characteristic-zero nilpotent thickening can obstruct semiampleness.

Birkar's semiampleness criterion is exactly designed for this point.

## 1. External theorem

C. Birkar,
*The augmented base locus of real divisors over arbitrary fields*,
Math. Ann. 368 (2017), 905--921,
arXiv:1312.0239,
Theorem 1.4:

For a nef Q-Cartier divisor L on a projective scheme X over a field, there exists a closed
subscheme Z whose reduction is the exceptional/null locus E(L), such that

```text
L is semiample  <=>  L|Z is semiample.
```

In characteristic zero one cannot in general replace Z by the reduced null locus.  Thus the
finite-formal-neighborhood work is load-bearing rather than cosmetic.

## 2. Complete null locus

The support-hyperplane bypass proves that, for each of

```text
0000770000ff,
00007b0000ff,
000707000f0f,
```

the complete irreducible P-null locus consists exactly of

```text
34 unsupported exceptional (-2)-curves
+
the zero-pairing elliptic quartics in the support hyperplane section.
```

There is no hidden positive-degree null curve.

Because P^2>0, this curve union is precisely Birkar's positive-dimensional exceptional locus.

## 3. Formal triviality on isolated unsupported exceptionals

If an unsupported exceptional curve E is not attached to a zero quartic, then

```text
E ~= P1,
E^2=-2,
P.E=0,
O_E(P) ~= O_E.
```

For every n>=1,

```text
I_E^n/I_E^(n+1) ~= O_E(-nE) ~= O_P1(2n),
H^1(E,O_E(2n))=0.
```

Hence triviality extends uniquely through every finite infinitesimal neighborhood of E.

## 4. Size-48 connected null components

For each size-48 support, the nontrivial connected components of the null locus are two trees

```text
Q_1 -- E -- Q_2
```

with Q_j elliptic (-4) quartics and E an unsupported exceptional (-2)-curve.

The retained size-48 formal-null calculation proves directly

```text
H^1(U,O_U(-nU))=0
```

for every n>=1 and therefore

```text
O_{nU}(P) ~= O_{nU}
```

for every finite n.

Thus the full null locus is formally trivial in the two size-48 support orbits.

## 5. Surviving size-768 full connected null component

For support `000707000f0f`, write

```text
U=A union B
```

for the two zero elliptic quartics.  They meet transversely at two smooth points r_+,r_-.

The full connected null component is obtained by attaching the two omitted unsupported
exceptional curves as one-edge leaves, one to A and one to B.

The dual graph has exactly one cycle: the two parallel A--B edges.  The exceptional leaves create
no new graph cycle.

### Component cohomology

Let N be this full reduced connected null divisor.  Its component intersections give

```text
N.A=N.B=-1,
N.E_A=N.E_B=-1.
```

Hence for every n>=1,

```text
deg O_A(-nN)=deg O_B(-nN)=n >0,
deg O_E(-nN)=n >0.
```

Therefore componentwise H^1 vanishes on every irreducible component.

For the normalization sequence, any obstruction class is consequently represented entirely by
edge-gluing data on the dual graph.  Tree-edge data on the two exceptional leaves are
coboundaries.  The only possible cohomology class is the A--B cycle discrepancy.

### The cycle is already zero to every order

Near r_+ and r_- the leaf exceptionals do not meet the surface germ, so locally

```text
I_N = I_U.
```

Therefore the n-th infinitesimal cycle transition for N is exactly the n-th cycle transition for
the two-quartic core U.

Z37 computes the first-normal cycle class exactly and obtains zero.  Z38 then proves

```text
O_{nU}(P) ~= O_{nU}
```

for every finite n.

Hence every A--B cycle obstruction for N is zero.  Since there is no other graph cycle and all
component H^1 groups vanish,

```text
O_{nN}(P) ~= O_{nN}
```

for every finite n>=1.

Thus P is formally trivial along the complete size-768 null component as well.

## 6. Birkar subscheme Z

Let `Z_B` be the closed subscheme supplied by Birkar Theorem 1.4.

Its reduction is Null(P).  Since the surface is Noetherian and `Z_B` is a finite closed
thickening supported on Null(P), there exists n such that

```text
I_N^n subset I_{Z_B}.
```

Therefore `Z_B` is a closed subscheme of the n-th formal neighborhood nN.

The formal triviality above implies

```text
O(P)|Z_B ~= O_ZB.
```

In particular P|Z_B is semiample.

Birkar Theorem 1.4 now gives

```text
P is semiample.
```

## 7. Exact contraction consequence

Because P is big and semiample, a sufficiently divisible multiple defines a birational morphism

```text
phi_P : S -> Y
```

with

```text
mP = phi_P^* A
```

for an ample divisor A on Y.

An irreducible curve R is contracted iff

```text
P.R=0.
```

Hence the exceptional locus of phi_P is exactly the already-classified null configuration:

- 34 unsupported exceptional curves;
- four zero elliptic quartics in each size-48 orbit;
- two zero elliptic quartics in the surviving size-768 orbit.

No hidden curve is contracted.

## 8. Scope

This is a positive structural result for Z3, not an exclusion of the three surviving supports.

Semiampleness shows that the null geometry is compatible with an algebraic contraction.  The next
useful question is whether the descended ample class on Y plus the resulting singularity package
gives a stronger Z12/Z2 obstruction to a genus-one member.

Do not reinterpret semiampleness as existence of an irreducible carrier in |lP|.

## Source locks

Current compact branch:
- complete-null-locus bypass certificate;
- Z3 size-48 formal-null certificate;
- Z37 first-normal exact transition certificate;
- Z38 all-higher formal Picard certificate.

External theorem:
- Birkar, arXiv:1312.0239, Theorem 1.4,
  published Math. Ann. 368 (2017), 905--921.

## Firewalls

```text
P_semiample_pre_audit=true
exact_null_contraction_pre_audit=true
three_surviving_orbits_excluded=false
irreducible_carrier_exists=false
whole_uniform_ray_closed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
