# MB104 Z33G — null-union Pic^0 gluing holonomy gate — 2026-09-19

Status: **PRE-AUDIT EXACT ONE-ORBIT ELIMINATION / NO CREDIT**

## Target

Z33E proves that every individual zero-pairing elliptic quartic `Q` satisfies

```text
O_Q(P) ~= O_Q.
```

Z33F shows that numerical lattice/discriminant data cannot add an embedding obstruction because

```text
P = 7H - 4 sum_(i in Sigma) E_i
```

is already an integral class in `Pic(S)`.

The remaining possibility is genuinely nonnumerical: on a reducible null union, a line bundle can be trivial on every irreducible component but still carry nontrivial multiplicative gluing around a cycle in the dual graph.

Z33G computes that gluing exactly for the four balanced incidence-16 support orbits.

## 1. Exact zero-quartic incidence

Using the exact 48-node model and the 12 Stoll--Testa `C2` elliptic quartics, the four canonical supports have:

```text
0000770000ff:
  Q0,Q1,Q2,Q3
  omitted nodes: 31,31,27,27

00007b0000ff:
  Q0,Q1,Q2,Q3
  omitted nodes: 31,31,26,26

000707000f0f:
  QA=Q3, QB=Q5
  omitted nodes: 27,35

00070b000f0f:
  QA=Q3, QB=Q5
  omitted nodes: 26,35
```

The two size-48 representatives use four quartics from the same `b1=0` family. Their proper transforms are pairwise disjoint. The repeated omitted exceptional curves join them only as two tree components

```text
Q -- E_omit -- Q.
```

There is no graph cycle, so componentwise triviality already implies triviality on the whole retained null union. The size-48 orbits survive this gate.

The size-768 representatives are different.

## 2. The two zero quartics on the size-768 supports

The common two zero quartics are

```text
QA:
  b1=0,
  i*a2-a3=0,
  a1-c=0

QB:
  b2=0,
  i*a3+a1=0,
  a2-c=0.
```

Their intersection is obtained exactly from the combined linear equations:

```text
a1=a2=c,
a3=i*c,
b1=b2=0,
b3^2=2*c^2.
```

Projectively `c!=0`, so they meet in exactly two points

```text
r_+ = (1,1,i,0,0,+sqrt(2),1),
r_- = (1,1,i,0,0,-sqrt(2),1).
```

These are smooth points of the cuboid surface and are not box nodes.

Thus the reduced union

```text
U = QA union QB
```

has two components joined at two distinct points. Its dual multigraph has first Betti number one, so a componentwise-trivial line bundle has one multiplicative gluing invariant.

The omitted exceptional curves at nodes `27/26` and `35` are leaves and do not change this cycle invariant.

## 3. A common rational section of O(P)

Use the global hyperplane section `c=0` and the canonical exceptional divisors. A rational section `sigma` of `O_S(P)` can be chosen with divisor

```text
div(sigma)=7(c=0)-4 sum_(i in Sigma) E_i.
```

On `QA`, its eight box-node points are the two hyperplane sections

```text
(c=0) + (a2=0).
```

If `pA` is the unique omitted node of `QA`, Z33E's hyperflex identity gives a linear form `LA` with

```text
div_QA(LA)=4 pA.
```

Therefore

```text
fA = c^3 * LA / a2^4
```

has exactly the same divisor as `sigma|QA`.

Similarly the eight nodes of `QB` split as

```text
(c=0) + (a3=0),
```

and for omitted node `pB=35`

```text
fB = c^3 * LB / a3^4
```

has divisor `div(sigma|QB)`.

Hence

```text
tau_A=sigma/fA,
tau_B=sigma/fB
```

are nowhere-zero trivializations on the two components. At a common point the transition is

```text
g(r)=tau_A/tau_B=fB(r)/fA(r).
```

The cycle holonomy is

```text
h = g(r_+)/g(r_-).
```

The restriction `O_U(P)` is trivial iff `h=1`. For `lP`, the holonomy is `h^l`.

## 4. Orbit 000707000f0f: holonomy is trivial

Here `pA=27`, `pB=35`.

Exact hyperflex forms are

```text
LA27 = b3 + i*b2 - 2*a2,
LB35 = -b1 + i*b3 - 2*a3.
```

At `r_+` and `r_-`,

```text
LA27(r_pm)= +/-sqrt(2)-2,
LB35(r_pm)= i*(+/-sqrt(2)-2).
```

Also

```text
c=1, a2=1, a3=i,
a2^4=a3^4=1.
```

Therefore

```text
g(r_+)=g(r_-)=i,
h=1.
```

No gluing obstruction is obtained for this orbit.

## 5. Orbit 00070b000f0f: non-torsion holonomy

Here `pA=26`, while `pB=35` remains unchanged.

The `QA` hyperflex form becomes

```text
LA26 = -b3 + i*b2 - 2*a2.
```

Thus

```text
LA26(r_+) = -sqrt(2)-2,
LA26(r_-) =  sqrt(2)-2,

LB35(r_+) = i*( sqrt(2)-2),
LB35(r_-) = i*(-sqrt(2)-2).
```

Consequently

```text
g(r_+) = i*(3-2sqrt(2)),
g(r_-) = i*(3+2sqrt(2)),
```

and the cycle holonomy is

```text
h
 = (3-2sqrt(2))/(3+2sqrt(2))
 = (3-2sqrt(2))^2
 = 17-12sqrt(2).
```

This lies in the real quadratic field `Q(sqrt(2))` and is not `+/-1`. A real quadratic field has only the roots of unity `+/-1`, so `h` has infinite multiplicative order. Equivalently under the standard real embedding,

```text
0 < 17-12sqrt(2) < 1.
```

Hence

```text
h^l != 1
```

for every `l>=1`.

Therefore

```text
O_U(lP)
```

is nontrivial for every positive `l`.

## 6. Elimination

If an irreducible effective carrier

```text
C in |lP|
```

existed on this support, then `C.QA=C.QB=0`. Since `C` is distinct from the degree-four quartics, positivity of local intersection on the smooth resolution forces `C` to be disjoint from both.

The defining section of `O_S(lP)` would then restrict to a nowhere-zero section on

```text
U=QA union QB,
```

which would trivialize `O_U(lP)`.

But the computed holonomy is `h^l!=1`. Contradiction.

Thus the complete Aut(S) orbit

```text
00070b000f0f   orbit size 768
```

is excluded from the displayed uniform genus-one P5 ray.

By automorphism transport, nontriviality of the restriction line bundle is invariant across the orbit.

## 7. Updated finite hard core

Before Z33G:

```text
4 orbits / 1632 supports.
```

After Z33G:

```text
0000770000ff    48   survives
00007b0000ff    48   survives
000707000f0f   768   survives
00070b000f0f   768   EXCLUDED
```

Remaining:

```text
3 orbits / 864 supports.
```

This is a support-specific elimination only. It does not close arbitrary unequal Picard classes or the full MB104 population.

## 8. Degree-eight known-curve preflight

The immutable Stoll--Testa source also gives 32 explicit degree-eight hyperelliptic genus-three curves (`C4s`) and 16 further displayed genus-three curves (`C5s`).

A bounded node-incidence replay on the four canonical balanced supports finds the displayed `C4s` meet at most four supported box nodes, far below the zero-pairing threshold `14`; the displayed `C5s` contain no box nodes in this model. They therefore do not add a competing degree-eight null component to this gate.

## Next route

The strongest next finite-first target is the surviving size-768 orbit, whose same two-quartic cycle has trivial holonomy:

```text
MB104-Z33H-SURVIVING-768-SECOND-GLUING-INVARIANT-PREFLIGHT
```

Target: look for a second exact global gluing datum on `000707000f0f`--for example another null divisor/component, a higher-order restriction along the two intersection points, or a source-complete first-normal-neighborhood restriction. Stop if the available data only reproduce the trivial line-bundle holonomy.

In parallel, the two size-48 tree orbits should not be revisited by ordinary Pic^0 gluing unless a new null component creates a cycle.

## Source locks

Historical archive head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- balanced quotient note blob `1dfafccb9559c98ccf71cc4b98449d784941d48f`;
- balanced quotient certificate blob `f63d08b9005762a02935a727f35e6581ae52aaab`;
- balanced quotient verifier blob `fe55e8a7bcd5b790f8d65419a9a88ba59106ba54`.

Immutable Stoll--Testa computational source:

```text
MichaelStollBayreuth/Verification
commit 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
Cuboids/cuboids.magma
blob 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

Current source adapter:

- `MB104-P6B-STOLL-TESTA-KNOWN-CURVE-KC-SOURCE-NOTE-20260919.md`
  blob `dc58a0a7d57dff5286e7b6739d4ac02f9266fa87`.

Current null restriction:

- Z33E note blob `57fa113b33ed827fd8b5d619b232ec16cdf85a8c`;
- Z33E certificate blob `be722c44f006394b753edab17eb1fc9146ed7d22`.

## Firewalls

```text
excluded_support_orbit=00070b000f0f
excluded_support_count=768
remaining_balanced_support_count=864
whole_uniform_ray_closed=false
arbitrary_unequal_picard_classes_closed=false
finite_degree_window_proved_population_wide=false
MB104_complete=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
