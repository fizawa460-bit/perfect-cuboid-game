# MB104 — full 28-fibration intersection audit on the balanced hard core — 2026-09-19

Status: **EXACT KNOWN-FIBRATION INTERSECTION AUDIT / ZERO CREDIT / NO MERGE**

## Purpose

After correcting the rank-3 half-fiber class, test the full Stoll--Testa genus-5 fibration
inventory against the three surviving MB balanced support orbits.

External source inventory:

```text
6 rank-3 quadrics -> 6 genus-5 fibrations;
11 rank-4 quadrics -> 2 complementary genus-5 fibrations each;
total = 28.
```

For rank-3 quadrics, if B is the 8-node base locus,

```text
2G = H - sum_(i in B) E_i.
```

For each rank-4 quadric the two fiber classes are complementary:

```text
G + G' = H.
```

The public Stoll verification log gives representatives of all four automorphism-orbit types:
one rank-3 type and three rank-4 types.

## 1. Correct rank-3 intersections

For

```text
P=7H-4 sum_(i in Sigma) E_i
```

and an 8-node rank-3 base cell B, put

```text
k=|Sigma intersect B|.
```

Since

```text
2G=H-sum_B E_i,
```

we have

```text
P.G = (112-8k)/2 = 56-4k.
```

Using the six-cell support profiles:

### size48 pair

```text
k=(8,0,0,6,0,0)

P.G=(24,56,56,32,56,56).
```

Thus

```text
min_rank3(P.G)=24.
```

### surviving size768 orbit

```text
k=(4,4,0,3,3,0)

P.G=(40,40,56,44,44,56).
```

Thus

```text
min_rank3(P.G)=40.
```

## 2. Rank-4 isotrivial pair: intersection is always 56

Stoll--Testa state that the first rank-4 quadric gives two isotrivial fibrations whose six bad
fibers are a genus-1 quartic from G2 taken twice.

A G2 elliptic quartic Q has

```text
H.Q=4,
Q passes through exactly 8 surface nodes.
```

On the resolution, the total fiber over such a doubled quartic has class

```text
G = 2Q + sum_(i in supp(Q)) E_i.
```

Let

```text
s=|Sigma intersect supp(Q)|.
```

Then

```text
P.Q = 7*4 - 4s = 28-4s,
P.E_i = 8 for i in Sigma,
P.E_i = 0 otherwise.
```

Therefore

```text
P.G
=2(28-4s)+8s
=56.
```

The support dependence cancels exactly.

Hence both fibrations in the first rank-4 pair have

```text
P.G=56.
```

## 3. The next six rank-4 quadrics: intersection is always 56

For the next rank-4 orbit, Stoll--Testa describe bad fibers consisting of two G3 elliptic
quartics joined by four exceptional curves.

The public cuboid equations show:

```text
each G3 quartic has degree 4 and passes through 4 nodes;
the paired G3 components in a split fiber pass through the same 4 nodes.
```

For example, in the representative fibration

```text
[a1+a2 : b1+b2],
```

the t=0 fiber contains the two G3 curves

```text
a1+a2=0,
b1-b2=0,
sqrt(2)a1 +/- b3=0,
```

and these two curves have the same four-node support.

Thus on the resolution one split fiber has

```text
G = Q_+ + Q_- + sum_(i in T) E_i,
|T|=4,
supp(Q_+)=supp(Q_-)=T.
```

If

```text
s=|Sigma intersect T|,
```

then

```text
P.G
=(28-4s)+(28-4s)+8s
=56.
```

So one ruling has P-intersection 56.  Since the complementary ruling satisfies

```text
G+G'=H
```

and

```text
P.H=112,
```

the complementary ruling also has

```text
P.G'=56.
```

Hence all twelve fibrations from these six rank-4 quadrics have P-intersection 56.

The alternative bad-fiber description with doubled conics gives the same fiber class and is not
needed for this intersection computation.

## 4. The last four rank-4 quadrics: intersection is always 56

Stoll--Testa state that the fibrations from the last four rank-4 quadrics also have split fibers
consisting of two G3 quartics joined by four exceptional curves, of the same type as above.

Therefore the same cancellation gives

```text
P.G=56
```

for one ruling of each quadric, and complementary-class symmetry gives 56 for the other ruling.

Hence all eight fibrations from the last four rank-4 quadrics have P-intersection 56.

## 5. Full 28-fibration profile

Thus every known rank-4 genus-5 fibration has

```text
P.G=56
```

on every balanced support under consideration.

The complete minimum over the 28 known fibrations is therefore:

### size48

```text
rank3 degrees:
(24,56,56,32,56,56)

rank4 degrees:
56 repeated 22 times

global minimum:
24.
```

### size768

```text
rank3 degrees:
(40,40,56,44,44,56)

rank4 degrees:
56 repeated 22 times

global minimum:
40.
```

So the rank-3 fibrations already realize the smallest degree among all 28 known genus-5
fibrations.

## 6. Corrected ramification budgets

For the elliptic normalization E of C in |lP|,

```text
deg R_g = 2l(P.G).
```

Therefore the best known fibration gives

```text
size48:
  min deg R = 48l;

size768:
  min deg R = 80l.
```

The previous 96l/160l values were the result of using the doubled rank-3 aggregate class instead
of the true fiber class and are superseded.

## 7. Research consequence

The search for a stronger MB route by merely enlarging

```text
6 rank-3 fibrations -> all 28 known genus-5 fibrations
```

does **not** lower the best projection degree.

Thus the useful information from the full 28-fibration system is not a smaller Riemann--Hurwitz
budget.

What remains potentially useful is higher directional diversity:

```text
more independent polar directions,
more jet-separation tests,
more possible residual/collision observables.
```

But any such gain must use the simultaneous geometry of the maps.  It cannot come from the
minimum degree alone.

## 8. Updated next gate

The next route is now sharply separated:

```text
CLOSED:
  search the known 28 genus-5 fibrations for P.G <24 (size48)
  or P.G <40 (size768).

OPEN:
  use simultaneous projection/polar jets from the 28-map system,
  or construct a genuinely new isotropic nef class outside the known 28 fibrations.

OPEN and likely cheaper:
  use the corrected six rank-3 maps with the exact 48l/80l common-ramification bound
  to derive a new residual invariant and only then feed that invariant to Picard64/H^perp.
```

No claim is made that the 28 Stoll--Testa fibrations exhaust all possible isotropic nef classes in
Pic(S).  The result only closes the **known fibration inventory** route.

## Sources

- Stoll--Testa, Section 5: 28 genus-5 fibrations; rank-3 half-class relation; rank-4 complementary
  fiber classes and bad-fiber decompositions.
- Michael Stoll public Verification repository, Cuboids/cuboids.magma and
  Cuboids/Section5_fibrations.log: exact cuboid curve equations and representative fibration maps.

## Firewalls

```text
known_28_fibration_inventory_audited=true
all_isotropic_nef_classes_classified=false
main_credit_changed=false
theorem_credit=false
endpoint_credit=false
MB104_complete=false
merge_authorized=false
```
