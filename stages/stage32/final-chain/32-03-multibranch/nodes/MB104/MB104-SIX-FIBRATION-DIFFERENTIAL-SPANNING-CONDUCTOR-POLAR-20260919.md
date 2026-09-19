# MB104 — six-fibration differential spanning and conductor-polar adapter — 2026-09-19

Status: **CROSS-LANE IMPORT RESEARCH / EXACT DIFFERENTIAL-SPANNING RESULT / POLAR ADAPTER SOURCE-GATED / ZERO CREDIT**

## Purpose

Continue the 32-01 -> 32-03 import from the previous fibration-nef preflight.

The goal is not to import 32-01 terminal pruning.  It is to use the six exact cuboid fibrations
recovered in 32-01 as a finite differential system on the smooth cuboid surface, then connect that
system to the Z48 conductor/different of a hypothetical MB104 genus-one carrier.

No MAIN, theorem, endpoint, or merge credit is changed.

## 1. The six fibrations are explicit conic maps

Use projective coordinates

```text
[a1:a2:a3:b1:b2:b3:c]
```

on the cuboid surface

```text
a1^2+a2^2-b3^2 = 0
a2^2+a3^2-b1^2 = 0
a1^2+a3^2-b2^2 = 0
a1^2+a2^2+a3^2-c^2 = 0.
```

The six 8-node base loci recovered by the 32-01 support design are exactly the base loci of the
following maps to smooth conics:

```text
f0 = [b1:a2:a3],   b1^2=a2^2+a3^2
f1 = [b2:a1:a3],   b2^2=a1^2+a3^2
f2 = [b3:a1:a2],   b3^2=a1^2+a2^2

f3 = [b1:a1:c],    c^2=a1^2+b1^2
f4 = [b2:a2:c],    c^2=a2^2+b2^2
f5 = [b3:a3:c],    c^2=a3^2+b3^2.
```

Each target conic is isomorphic to P1.

On the minimal resolution, write

```text
D_j = H - sum_(i in B_j) E_i.
```

Stoll--Testa Section 5 gives the crucial half-class relation

```text
2G_j = D_j,
```

where G_j is the actual genus-5 fiber class.  Hence

```text
G_j^2=0,
H.G_j=8.
```

The earlier draft conflated D_j with G_j; all degree bounds below use the corrected true fiber class.

The previous import preflight computed the restrictions to an MB balanced carrier
`C in |lP|`.

## 2. Exact combined-differential injectivity away from the 48 nodes

For one conic map represented by a nonzero coordinate triple

```text
T_j=(x,y,z),
```

a tangent vector `v` satisfies

```text
df_j(v)=0
```

iff its variation on that triple is projectively radial:

```text
(v_x,v_y,v_z)=lambda_j(x,y,z).
```

Use the six coordinate triples

```text
T0={b1,a2,a3}
T1={b2,a1,a3}
T2={b3,a1,a2}
T3={b1,a1,c}
T4={b2,a2,c}
T5={b3,a3,c}.
```

Build the overlap graph on `T0,...,T5`: join two triples when their shared coordinate is nonzero.

If the graph is connected, all `lambda_j` are equal, since any nonzero shared coordinate forces
the two projective scaling constants to agree.  Every ambient coordinate occurs in at least one
triple, so

```text
v=lambda*(a1,a2,a3,b1,b2,b3,c),
```

which is the projective radial direction and therefore zero in the tangent space of the projective
surface.

The only way the overlap graph can disconnect is for all three coordinates of one of the six
triples to vanish.  The six minimal disconnecting zero sets are exactly

```text
{b1,a2,a3}
{b2,a1,a3}
{b3,a1,a2}
{b1,a1,c}
{b2,a2,c}
{b3,a3,c}.
```

Each is one of the six 8-node fibration base loci.  On the original cuboid surface these are among
the 48 ordinary double points.

Therefore:

```text
combined map
  F=(f0,...,f5): S_smooth -> (P1)^6

has injective differential at every smooth point of the original surface.
```

Equivalently:

```text
for every nonzero tangent direction at every smooth non-node point,
at least one df_j is nonzero on that direction.
```

This is the first exact surface-wide differential-spanning statement obtained from the 32-01
fibration package.

For Z48 this is enough, because the intrinsic conductor scheme is supported in the smooth interior
and avoids the exceptional curves.

## 3. Consequence on the normalization of a hypothetical MB carrier

Let

```text
nu:E -> C subset S
```

be the normalization of a hypothetical integral carrier, with

```text
g(E)=1.
```

For each j define

```text
g_j = f_j o nu : E -> P1.
```

At a point q in E write `m_q` for the multiplicity of the corresponding analytic branch of C.
In local smooth surface coordinates, `m_q` is the minimum order of a local parameter function
along the branch.

Because `df_0,...,df_5` span the cotangent directions at `nu(q)`, at least one fibration
coordinate has exact branch order `m_q`.  Therefore

```text
min_j ord_q(d g_j) = m_q-1.                    (RAM-MIN)
```

Let `R_j` be the ramification divisor of `g_j).  Then the common ramification divisor

```text
A = gcd(R_0,...,R_5)
```

has exact coefficient

```text
ord_q(A)=m_q-1.
```

Thus A measures the failure of the normalization map itself to be immersive.

In particular smooth branches contribute zero to A even when several distinct smooth branches
collide at the same singular point of C.

## 4. Global linear bound on intrinsic branch multiplicity defect

Riemann--Hurwitz on the elliptic normalization gives

```text
deg R_j = 2 deg g_j = 2l(P.G_j).
```

The previous import preflight computed:

### size48 supports

```text
P.G_j = (24,56,56,32,56,56),
```

so

```text
deg A <= min_j deg R_j = 48l.
```

### surviving size768 support

```text
P.G_j = (40,40,56,44,44,56),
```

so

```text
deg A <= 80l.
```

Hence:

```text
sum_(normalization branches q) (m_q-1)
<= 48l   for the two size48 orbits,

sum_(normalization branches q) (m_q-1)
<= 80l   for the surviving size768 orbit.       (BRANCH-DEFECT)
```

This is a genuine new MB constraint imported from 32-01 geometry.

It is linear in l, whereas the Z48 different has degree

```text
deg Delta = 336l^2+112l.
```

## 5. Conductor-polar identity: exact theorem shape, external source gate

For a local reduced plane-curve germ `g=0` and its normalization parameterization, Piene's
Jacobian/conductor formula expresses each partial derivative of g on the normalization as

```text
conductor_generator * Jacobian_minor.
```

In the present surface setting, after choosing one fibration coordinate as a local projection,
the corresponding local relative polar has normalization divisor of the form

```text
Delta + R_j,
```

where `Delta` is the conductor different and `R_j` is the ramification divisor of
`g_j=f_j o nu`.

The degree check is exact:

```text
deg Delta + deg R_j
=
(336l^2+112l) + 2l(P.G_j)
=
C.(C+K_S+2G_j).
```

Thus the line-bundle degree is precisely the relative-polar degree.

Important:

```text
this equality is NOT a contradiction.
```

It is the expected adjunction/polar identity.  A one-fibration degree argument therefore cannot
close MB104.

The local Piene theorem is externally source-supported, but its exact global surface adapter is
not promoted here without a dedicated source/hypothesis audit.

## 6. What six fibrations add beyond one polar

The six-fibration spanning result gives more than six copies of the same degree formula.

At q in E:

```text
gcd_j(R_j) has coefficient m_q-1.
```

Therefore, if the local conductor-polar formula is globalized correctly, the common normalization
divisor of the six polar systems is

```text
Delta + A,
```

with

```text
deg A = O(l).
```

So the six-polar system separates the quadratic conductor contribution from the purely intrinsic
branch-multiplicity defect.

This is a useful structural split:

```text
quadratic part:
  conductor different Delta = Theta(l^2)

linear common residual:
  A = sum_q (m_q-1) q = O(l).
```

The remaining quadratic complexity is therefore not explainable merely by simultaneous
ramification of the six imported fibrations.

## 7. Why this does not yet close Z25

For a reduced singularity with branches `B_alpha`,

```text
delta_p
=
sum_alpha delta(B_alpha)
+
sum_(alpha<beta) I(B_alpha,B_beta).
```

The new bound on `sum(m_q-1)` does not by itself bound the intrinsic
`delta(B_alpha)`.

For example, a single plane branch may have fixed small multiplicity and arbitrarily large
delta through high characteristic exponents.

Likewise two smooth branches can have arbitrarily high pairwise tangency while contributing zero
to A.

Therefore the following naive implication is invalid:

```text
deg A=O(l)
=> delta=O(l).
```

This pass explicitly closes that false route.

## 8. Refined Z25 target

The import nevertheless sharpens Z25 considerably.

A useful next theorem must exploit not only the common ramification gcd A, but the **six separate
ramification divisors** and/or the finite cuboid coordinate relations.

Two exact success shapes remain plausible.

### Z25-FIB-A — intrinsic branch semigroup bound

For every irreducible branch B, use the six orders

```text
ord_q(g_j-g_j(q))
```

and the cuboid quadratic relations to bound its conductor exponent / delta by a function of the
six ramification orders.

The global sum of those ramification orders is bounded by

```text
sum_j deg R_j = O(l).
```

A sufficiently strong local inequality could then rule out `deg Delta=Theta(l^2)`.

A generic two-coordinate semigroup bound is too weak; the cuboid relations must be used.

### Z25-FIB-B — pairwise branch collision via multi-projection jets

For two distinct smooth branches through the same point, high contact means the jets of **every**
local function agree to high order.  Since the six fibration coordinates generate cotangent
directions, high branch contact forces high simultaneous jet coincidence in the six projections.

The missing global theorem is a sharp bound on the total such six-projection jet coincidence that
beats the coefficient 168 in

```text
delta(C)=168l^2+56l.
```

A crude pair-of-projections coincidence count has coefficient thousands and is useless.  Any
successful argument must use the special six-map dependence/cuboid equations, not a generic
Bezout bound in P1 x P1.

## 9. Picard64/H^perp re-entry point

The 32-01 H^perp machinery should not be applied to P itself.

A legitimate re-entry point would be an auxiliary divisor/residual vector extracted from either:

```text
- branch-semigroup defect left after factoring Delta+A, or
- six-projection collision/polar residual data.
```

Only then is there genuinely new unknown data on which a positive Schur penalty might provide
strictness.

## 10. Updated route verdict

### PROVED / exact internal geometry

```text
six explicit conic fibrations;
combined differential injective on S_smooth away from the 48 nodes;
min_j ramification order on a branch = branch multiplicity - 1;
deg common ramification gcd <=48l (size48) or <=80l (size768).
```

### SOURCE-GATED but well-supported

```text
global relative-polar pullback divisor = Delta + R_j.
```

### CLOSED AS TOO WEAK

```text
single-fibration polar degree comparison;
direct Picard membership of P;
crude two-projection coincidence Bezout.
```

### BEST NEXT DEEP ROUTE

```text
use the six exact cuboid projection orders simultaneously
to control branch semigroups / characteristic exponents
or simultaneous pairwise jet coincidence.
```

That is now the narrowest serious 32-01 -> 32-03 route.

## Firewalls

```text
32_01_terminal_credit_imported=false
main_credit_changed=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
MB104_complete=false
merge_authorized=false
```


## 11. Extension beyond the six rank-3 fibrations

The continuation pass checked Stoll--Testa Section 5 and the public verification log.

The cuboid surface carries

```text
6 rank-3 genus-5 fibrations
+
22 rank-4 genus-5 fibrations
=
28 total.
```

Each of the eleven rank-4 quadrics yields two complementary fiber classes whose sum is H.
Therefore the six-map differential result above is only the first layer of the available
fibration arsenal.

The next exact import task is to materialize the 22 rank-4 fiber classes in the retained Picard64
basis and compute `P.G` for each of the three surviving balanced support orbits.  A rank-4
fiber with `P.G<24` on a size48 support or `P.G<40` on the size768 support would strictly
improve every ramification/polar budget above.
