# Stage32 MB104 — explicit F1-P5 support forces full deck stabilizer

Status: **RETAINED GLOBAL NECESSARY GEOMETRY / PRODUCT PULLBACK CONNECTED / e=4 FORCED / NO CLOSURE / MB104 INCOMPLETE / NO CREDIT**

## Inputs

Assume an actual integral normalization-genus-one carrier realizes the retained uniform F1-P5 packet

```text
D_l = 7lH - 4l sum_(p in Sigma) E_p,
|Sigma|=14,
d=r_odd=112l,
```

with the explicit retained support `Sigma`.

The previous equality-rigidity leaf gives, for a connected component `Z` of the pullback to

```text
P=C8 x C8,
```

an etale degree

```text
e=deg(Z->Y) in {1,2,4}
```

and two etale product projections of degree `14el`.

Let

```text
G = Gamma[4]/Gamma[8] ~= (Z/2)^3,
G0 = Gamma'[4]/Gamma[8] ~= (Z/2)^2.
```

Then `P/G0=X`, `P/G=B`, and `G0` acts freely on `C8`.

## The explicit support uses all three singular stabilizer types

The node-stabilizer adapter identifies the three singular types by the unique zero among

```text
b1=Z1, b2=Z2, b3=Z3.
```

The explicit F1-P5 support has type counts

```text
(5,5,4).
```

So every one of the three distinct singular stabilizer involutions

```text
s1,s2,s3 in G\G0
```

occurs at a supported box node, and every supported normalization branch is odd/minimal.

## Branch fibers force every component to be stable under each occurring involution

Let `E` be the normalization of the hypothetical downstairs carrier and

```text
Y -> E
```

the connected Beauville double cover.  A normalization point `y in Y` above an odd branch through a box node is a branch point of `Y->E`, hence is fixed by the Beauville involution.

Choose a lift `p in P` of the corresponding fixed point in `X`.  If the box node has stabilizer `s_j`, then

```text
s_j(p)=p.
```

Because `G` is abelian, for every `h in G0`,

```text
s_j(hp)=h s_j(p)=hp.
```

Thus `s_j` fixes **all four points** in the `P->X` fiber over that branch point.

Now pull `Y` back along the degree-four etale cover `P->X`.  Every connected component maps surjectively to `Y`, so over `y` it contains at least one point of that four-point fiber.  Since `s_j` fixes that point, it cannot send the connected component to a distinct component: the connected components of the etale pullback are disjoint.  Therefore `s_j` stabilizes every connected component.

This argument applies to `s1,s2,s3` because all three node types occur in the explicit support.

## Three outside involutions generate the full deck group

The three `s_j` are distinct elements of the same coset `G\G0`.  In the vector space `G ~= F_2^3` with the index-two subspace `G0 ~= F_2^2`, any three distinct elements of one nonzero coset generate all of `G`: subtracting one from the other two gives two distinct nonzero elements of `G0`, hence a basis of `G0`, together with one outside element.

Therefore the stabilizer of every connected component contains all of `G`.

Hence there can be only one connected component in the degree-four pullback to `P`, and

```text
e=4.
```

The product pullback `Z` is connected and `G`-stable.

## Sharpened equality geometry

Substituting `e=4` into the previous equality-rigidity result gives

```text
2g(Z)-2 = 4d = 448l,
g(Z)=224l+1,
```

and both product projections are etale of exact degree

```text
Z -> C8 : 56l,
Z -> C8 : 56l.
```

Moreover

```text
Z/G ~= E,
```

so the original genus-one normalization is the full `(Z/2)^3` quotient of this connected equal-bidegree etale correspondence.

## Consequence

The cases `e=1` and `e=2` are excluded for the explicit uniform F1-P5 support.  Any actual realization must have the much more rigid form

```text
connected G-stable etale correspondence
Z subset C8 x C8
of bidegree (56l,56l),
with quotient Z/G of genus one.
```

This is a strict strengthening of the earlier Beauville lower-bound wall and of the first equality-rigidity leaf.

It is not yet a contradiction.  The next finite problem is to classify the induced degree-`56l` map

```text
E=Z/G -> C8/G = X(4) ~= P^1
```

together with the six fixed branch values of `C8->X(4)` and the required branch-type totals coming from the `(5,5,4)` supported-node distribution.

## Firewalls

- Conditional on actual realization of the explicit uniform F1-P5 packet.
- No etale correspondence is constructed.
- No surviving balanced support orbit is yet closed.
- No claim is made yet that the resulting six-point Hurwitz passport is impossible.
- Whole span5, unequal Picard coefficients, P6 sectors, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
