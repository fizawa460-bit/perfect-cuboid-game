# MB104 — 32-01 fibration-nef import preflight for 32-03 — 2026-09-19

Status: **CROSS-LANE MATHEMATICAL IMPORT PREFLIGHT / ZERO CREDIT / NO MERGE**

## Question

Can the post-TD02 32-01 fibration-nef / Picard64 machinery be imported into MB104 in a way that
moves the 32-03 multibranch goal forward?

This note treats 32-01 only as a source of shared cuboid-surface geometry and exact lattice tools.
It does **not** import 32-01 terminal-population semantics, pruning credit, or MAIN authority.

Source heads used:

```text
MB PR #1825 head:
93c38c87cb4288e5b978cb9e3113a6697273dd16

32-01-178 PR #1821 head:
fd8ffe03ff4b90f811e317a43e76a95f31c30464
```

## 1. What can and cannot be imported

### Importable shared geometry

The following 32-01 assets are surface/Picard facts rather than terminal-family facts:

```text
retained rank-64 Picard marking,
H^perp exact quadratic form,
Aut(S) action,
six recovered fibration base-locus cells,
the six isotropic divisor classes
F_j = H - sum_(i in B_j) E_i,
Picard image-lattice / HNF machinery.
```

For every cell `B_j`, `|B_j|=8`, so on the degree-16 cuboid resolution

```text
F_j^2 = 16 - 2*8 = 0,
H.F_j = 16.
```

The six cells partition the 48 exceptional curves.

### Not directly importable

The 32-01 post-TD02 objects

```text
static min-q tables,
qexc caps,
parity quotient,
weighted terminal counters,
x4 workunit semantics,
branch-and-bound terminal masses
```

depend on the 32-01 terminal family and cannot be applied to MB104 without a new semantic adapter.

They must not be treated as MB pruning predicates.

## 2. Exact six-cell model in MB node coordinates

Using the exact 48-node model already retained by Z33G, the six 32-01 fibration cells are the
nonempty intersections of one coordinate hyperplane among `b1,b2,b3` with one admissible
W-pair among `a1,a2,a3,c`:

```text
B0 = {b1=a2=a3=0} = nodes  0.. 7
B1 = {b2=a1=a3=0} = nodes  8..15
B2 = {b3=a1=a2=0} = nodes 16..23
B3 = {b1=a1=c =0} = nodes 24..31
B4 = {b2=a2=c =0} = nodes 32..39
B5 = {b3=a3=c =0} = nodes 40..47
```

This is the same six-cell support design recovered abstractly in 32-01.

No individual node-to-retained-label bijection is needed for the aggregate calculation below.

## 3. Surviving MB support signatures on the six fibrations

For a balanced support `Sigma`, let

```text
k_j = |Sigma intersect B_j|.
```

The four Z33G balanced support orbits have:

```text
0000770000ff : (8,0,0,6,0,0)
00007b0000ff : (8,0,0,6,0,0)

000707000f0f : (4,4,0,3,3,0)
00070b000f0f : (4,4,0,3,3,0)
```

Z33G already excludes `00070b000f0f`, so the surviving signatures are

```text
size48 pair:
  (8,0,0,6,0,0)

size768 orbit:
  (4,4,0,3,3,0).
```

Important negative result:

```text
the six-cell aggregate signature does not distinguish
0000770000ff from 00007b0000ff,

and before Z33G it also did not distinguish
000707000f0f from 00070b000f0f.
```

Therefore the six-cell aggregate alone cannot replace Z33G-type fine Pic^0 information.

## 4. Exact fibration degrees on the MB carrier

For the primitive balanced ray

```text
P = 7H - 4 sum_(i in Sigma) E_i,
P^2=336,
H.P=112,
```

and one fibration class

```text
F_j = H - sum_(i in B_j) E_i,
```

we have

```text
P.F_j = 7*16 - 8*k_j = 112 - 8*k_j.          (FIB-DEG)
```

Hence for a hypothetical carrier

```text
C in |lP|,
nu:E -> C,
g(E)=1,
```

the restriction of the fibration gives a map

```text
f_j:E -> P1
```

of degree

```text
deg(f_j)=l(112-8k_j).
```

### size48 support pair

For `(8,0,0,6,0,0)`:

```text
(P.F_0,...,P.F_5)
=
(48,112,112,64,112,112).
```

Thus the six elliptic-cover degrees are

```text
(48l,112l,112l,64l,112l,112l).
```

### size768 survivor

For `(4,4,0,3,3,0)`:

```text
(P.F_0,...,P.F_5)
=
(80,80,112,88,88,112).
```

Thus

```text
(80l,80l,112l,88l,88l,112l).
```

These are genuinely new exact MB observables imported from the 32-01 fibration geometry.

## 5. Direct Picard64/H^perp strictness test — NO-GO in its naive form

A tempting route was:

```text
32-01 H^perp Schur penalty
 -> strictify the old Z21 Hodge equality
 -> revive Z6/Z11/Z14/Z16/Z21.
```

The naive version fails for a structural reason.

The balanced ray `P` is already an explicit integral class of the retained Picard lattice.
Therefore checking

```text
P or lP is in the Picard image lattice
```

cannot exclude it.

Likewise, an H^perp norm computed only from the already-known divisor class `P` cannot create a
new contradiction: it merely recovers the exact norm of a class that already exists.

So:

```text
Picard64 membership on P itself = no new obstruction.
```

A useful H^perp import would have to act on **new unknown data** attached to the carrier
(distribution, auxiliary divisor, polar, residual class, or singularity package), not on P alone.

## 6. Conductor + fibration polar adapter — promising new route

Z48 gives the exact intrinsic conductor scheme and different:

```text
length(Z_cond)=delta(C)=168l^2+56l,

deg Delta
= 2 delta(C)
= 336l^2+112l.
```

Moreover the conductor lies in the smooth interior of the surface.

For a local plane-curve singularity, the Piene conductor/Jacobian identity for a normalization
parameterization has the form

```text
partial(g)/partial(y_i) o nu
=
(conductor generator) * Jacobian minor.
```

For a map to a one-dimensional base this is the local mechanism behind the relation

```text
polar divisor on E
=
conductor different Delta
+
ramification divisor of the chosen projection/fibration.
```

For the imported fibration `f_j:E->P1`, Riemann--Hurwitz on the elliptic normalization gives

```text
deg R_j = 2 deg(f_j) = 2l(P.F_j).
```

Therefore the candidate exact global relation has degree

```text
deg(Polar_j|E)
=
336l^2+112l + 2l(P.F_j).                       (POLAR-DEG)
```

The smallest ramification budgets are:

```text
size48:
  min_j deg R_j = 96l;

size768:
  min_j deg R_j = 160l.
```

This is a qualitatively new asymptotic separation:

```text
conductor different mass = Theta(l^2),
fibration ramification budget = Theta(l).
```

No contradiction follows from this degree comparison alone, because the conductor is a fixed
factor of the polar divisor.  But it isolates where a contradiction must come from:

```text
any remaining quadratic singularity mass cannot be explained by
ordinary ramification of the normalization maps to P1.
```

## 7. Why this may revive Z25

For a reduced plane-curve singularity with branches C_a,

```text
delta
=
sum_a delta(C_a)
+
sum_(a<b) I(C_a,C_b).
```

The first term measures intrinsic singularity of individual branches; the second term is
branch collision/tangency.

For one branch of multiplicity m_a, a generic ambient projection contributes at least
`m_a-1` to ramification on the normalization.  Thus the imported fibration ramification budget
is naturally suited to bounding the **individual-branch singularity defect**.

What it does not automatically see is high intersection multiplicity between distinct smooth
branches.  Two smooth tangent branches may carry arbitrarily large delta while both remain
unramified for a generic projection.

Therefore the 32-01 import points directly at the old Z25 missing theorem species:

```text
quadratic delta/conductor mass
must be forced into pairwise branch collision/tangency,
then control that tangency using the finite cuboid fibration/polar system.
```

This is substantially sharper than the old generic statement "need a stronger collision theorem."

## 8. Six-fibration strengthening target

The next promising MB theorem target is not a single fibration but the full six-map differential
system.

At a smooth interior point of S, test whether the differentials

```text
df_0,...,df_5
```

span the cotangent space with a source-complete finite exceptional locus.

If yes, then for every singular branch of C one obtains a controlled collection of local
ramification orders across the six maps.  The total budgets are explicit from (FIB-DEG).

The remaining conductor contribution would then be forced into collisions of distinct smooth
branches.  A second exact step would need to show that sufficiently high tangency between two
branches forces simultaneous special behavior in at least one or two of the six fibrations.

Legal success shapes are:

```text
A. prove a global inequality
   delta(C) <= linear_fibration_budget + bounded_pairwise_collision_budget
   with leading coefficient <168;

B. prove the six-fibration system separates tangent directions strongly enough that
   pairwise contact order is bounded by a sum of fibration coincidence/ramification orders;

C. derive an exact finite collision signature and feed it to the retained Picard64/H^perp
   machinery as a genuinely new unknown residual vector.
```

Any of A/B/C would be a real 32-01 -> 32-03 mathematical import.

## 9. Route ranking after the preflight

### HIGH

```text
six fibration classes F_j
+
Z48 conductor/different
+
local polar/Jacobian-conductor identity
+
branch-tangency decomposition of delta.
```

This is the best import route found in this pass.

### MEDIUM

```text
Picard64/H^perp machinery applied to a new auxiliary residual class
coming from polar/collision data.
```

Potentially strong after the new residual is defined.

### LOW / NO-GO

```text
apply 32-01 terminal static-minq tables directly to MB;
apply Picard membership directly to P;
expect six-cell counts alone to separate the two size48 support orbits.
```

These do not move MB104.

## 10. Immediate next research gate

The most valuable next exact question is:

```text
For the six recovered cuboid fibrations F_j, do their differentials span T^*_S
on the smooth interior outside an explicitly controlled divisor/finite set,
and can pairwise branch tangency of an integral lP carrier be bounded
by the six induced projection/polar contact orders?
```

This should be attacked before spending more time on arbitrary Picard64 Schur strictness.

If the differential-spanning/polar inequality works, it gives a route that uses:

```text
32-01 fibration geometry
+ Z33 support equality
+ Z40B boundary control
+ Z48 quadratic conductor mass
```

in one MB-native argument.

## Firewalls

```text
cross_lane_import_credit=false
32_01_terminal_predicate_imported=false
main_credit_changed=false
theorem_credit_changed=false
endpoint_credit_changed=false
MB104_complete=false
merge_authorized=false
```
