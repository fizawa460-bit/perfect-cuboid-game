# Stage32 MB104 — F1-P5 six-branch Hurwitz passport

Status: **RETAINED FINITE GLOBAL REDUCTION / INFINITE l-FAMILY REDUCED TO SIX INTEGER NODE-SPLITS / NO CLOSURE / MB104 INCOMPLETE / NO CREDIT**

## Inputs

Assume an actual integral normalization-genus-one carrier realizes the explicit retained uniform F1-P5 packet.  The preceding full-deck leaf forces a connected `G`-stable curve

```text
Z subset C8 x C8,
G ~= (Z/2)^3,
g(Z)=224l+1,
```

whose two projections to the genus-five curve `C8` are etale of degree

```text
n=56l,
```

and whose quotient

```text
E=Z/G
```

is the original genus-one normalization.

## 1. The factor quotient has six simple branch values

The three singular node-stabilizer involutions `s1,s2,s3` each account for exactly `16` box nodes.  If `f_j` is the number of fixed points of `s_j` on `C8`, then the diagonal fixed locus in `C8 x C8` has `f_j^2` points.  No point can be fixed by two distinct outside involutions because their product is a nontrivial element of the free subgroup `G0`.  Hence every diagonal fixed-point orbit has size `|G|/2=4`, and

```text
f_j^2/4 = 16,
f_j=8.
```

The three nontrivial elements of `G0` are fixed-point-free.  Apply Riemann--Hurwitz to

```text
C8 -> Q:=C8/G.
```

With `genus(C8)=5`,

```text
8 = 8(2g(Q)-2) + sum_(1!=s in G) #Fix(s).
```

The three singular stabilizers already contribute `3*8=24`.  The remaining outside involution cannot contribute positively without forcing negative genus.  Therefore

```text
Q ~= P^1,
```

and the remaining outside involution is fixed-point-free.

For each `s_j`, its eight fixed points split into two `G`-orbits of four points.  Thus

```text
C8 -> P^1
```

has exactly six branch values, two for each singular stabilizer type, and all inertia indices are `2`.

## 2. Quotient the etale correspondence

The first etale projection `Z->C8` is `G`-equivariant, so quotienting gives a degree-`n=56l` map

```text
phi: E=Z/G -> Q=C8/G ~= P^1.
```

It is unramified away from the six branch values of `C8->Q`.

Fix one such branch value `q`, with inertia involution `s`.  For a point `z in Z` over a fixed point `x in C8`, etaleness of `Z->C8` gives

```text
G_z subset G_x=<s>.
```

Comparing local quotient degrees in the commutative square shows

```text
ramification_index(phi at [z]) = |G_x|/|G_z|.
```

Hence every point over `q` is of exactly one of two kinds:

```text
G_z=<s>:  phi is unramified there;
G_z=1:    phi has simple ramification index 2.
```

Let

```text
u_q = number of unramified points over q,
r_q = number of ramified points over q.
```

Then

```text
u_q + 2 r_q = n = 56l.                   (H1)
```

## 3. Riemann--Hurwitz fixes the total unramified capacity

Since `E` has genus one and `Q=P^1`,

```text
sum_q r_q = 2n = 112l.                   (H2)
```

Summing `(H1)` over the six branch values gives

```text
sum_q u_q + 2 sum_q r_q = 6n.
```

Using `(H2)`,

```text
sum_q u_q = 2n = 112l.                   (H3)
```

But the retained uniform packet has exactly

```text
R8=r_odd=112l
```

distinct normalization branches through its fourteen supported box nodes.

Each such branch gives a distinct point of `E`.  At the corresponding box node the same singular stabilizer fixes both coordinates of every lift in `Z`, so the point of `E` is **unramified** for `phi` and lies over one of the six branch values.

Thus the `112l` supported odd branches inject into a set whose total cardinality is exactly `112l`.  Therefore they exhaust it:

```text
all unramified points of phi over the six branch values
= the supported odd/minimal branches.
```

There are no additional unramified points over those six values.

## 4. Exact pair totals from the `(5,5,4)` support

The support uses the three stabilizer types in node counts

```text
5,5,4.
```

Each supported node carries `8l` normalization branches.  Therefore, for the two branch values associated to each stabilizer type, the sums of `u_q` are exactly

```text
40l,
40l,
32l.                                      (H4)
```

Using `(H1)` on each pair, the corresponding pair sums of simple ramification points are

```text
36l,
36l,
40l.                                      (H5)
```

## 5. Finite six-integer passport

A fixed supported box node has a fixed first-factor `G`-orbit, hence contributes all of its `8l` branches to one of the six branch values.  Write

```text
u_q = 8l m_q.
```

Then the infinite family is reduced to six nonnegative integers

```text
m1,...,m6
```

with pair constraints

```text
m1+m2=5,
m3+m4=5,
m5+m6=4.                                (H6)
```

For each branch value,

```text
r_q = (56l-u_q)/2
    = (28-4m_q)l.                         (H7)
```

Thus the local monodromy permutation around `q` has cycle shape

```text
2^((28-4m_q)l) 1^(8m_q l).
```

Up to swapping the two branch values inside each stabilizer pair, only finitely many integer passport shapes remain, independent of `l` except for the common scaling factor.

## Consequence

The global realization problem for this explicit F1-P5 uniform ray has moved from arbitrary high-degree singular curves to a finite Hurwitz/Nielsen-class question:

```text
Does there exist, for some l>=1,
a connected degree-56l genus-one cover of P^1
with six involutory branch permutations,
pairwise fixed-point totals governed by (H6),
which lifts to the required G-equivariant etale correspondence Z->C8?
```

This leaf does not answer that final existence question.

## Firewalls

- Conditional on actual realization of the explicit uniform F1-P5 packet.
- No Hurwitz passport is asserted to exist.
- No Nielsen-class nonexistence theorem is claimed.
- No surviving support orbit is closed yet.
- Whole span5, unequal Picard coefficients, P6 sectors, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
