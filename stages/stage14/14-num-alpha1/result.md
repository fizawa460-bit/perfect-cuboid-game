# Stage14-num-α1 — exact diagonal-first dictionary

> STATUS: `STAGE14_NUM_ALPHA1=COMPLETE_EXACT_DIAGONAL_FIRST_DICTIONARY`
>
> CLASSIFICATION: exact finite-enumeration specification only; no performance or asymptotic claim.

## 1. Starting identities

For a cuboid with positive integer edges `(a,b,c)`, face diagonals `(x,y,z)` and integer space diagonal `d`, use

```text
x^2 = a^2+b^2
y^2 = a^2+c^2
z^2 = b^2+c^2
d^2 = a^2+b^2+c^2.
```

Hence every active face produces one ordered **opposite-edge representation** of the same square `d^2`:

```text
(a,z), (b,y), (c,x),
```

because

```text
d^2 = a^2+z^2 = b^2+y^2 = c^2+x^2.
```

The ordered role matters: the first coordinate is an edge, the second is the face diagonal opposite that edge. An unordered sum-of-two-squares representation `{u,v}` therefore supplies up to two role orientations `(u,v)` and `(v,u)` before geometric filtering.

## 2. Exact two-representation collision theorem

Take two distinct ordered representations of the same `d^2`,

```text
d^2 = a^2+F_a^2 = b^2+F_b^2.
```

Then automatically

```text
F_a^2-b^2 = F_b^2-a^2.
```

Define

```text
c^2 := F_a^2-b^2.
```

If `c^2>0` is a perfect square, then

```text
F_a^2=b^2+c^2,
F_b^2=a^2+c^2,
d^2=a^2+b^2+c^2.
```

Therefore `(a,b,c)` is an integer cuboid with integer space diagonal and at least the two face diagonals `F_a,F_b` integral. Conversely, every cuboid with integer space diagonal and at least two integer face diagonals yields such a pair of ordered representations by choosing the two edges opposite those active faces.

Thus:

```text
TWO_FACE_OR_MORE
<=>
there exist two distinct ordered representations of d^2
whose cross-difference is a positive square.
```

No probabilistic or heuristic step is involved.

## 3. Exactly two versus all three faces

After reconstructing `(a,b,c)`, compute the remaining face square

```text
R^2 = a^2+b^2.
```

If `R^2` is not a square, the reconstructed object has exactly the two active faces used in the collision. If it is a square, all three face diagonals are integral and the object is a perfect-cuboid candidate.

A three-face object produces three active ordered representations and therefore three pair collisions. The α engine must canonicalize the edge triple and merge these three collision witnesses into one physical object with the all-three face mask. It must not count them as three cuboids.

An exactly-two object produces one unordered pair of active-face representations, modulo exchanging the two witnesses.

## 4. Canonicalization and duplicate symmetries

The collision layer is allowed to generate all role orientations. After a positive-square cross-difference is found:

1. form `(a,b,c)`;
2. reject zero/negative coordinates;
3. sort the edge triple into the ordinary Stage14 canonical order;
4. compute all three face-square tests from the sorted triple;
5. compute `gcd(a,b,c)` and apply the ordinary primitive rule;
6. emit the same canonical object key and face mask as main num;
7. deduplicate by canonical object key, not by representation-pair identity.

The following search symmetries are therefore harmless if canonicalized:

```text
representation pair order: (R1,R2) <-> (R2,R1)
within-representation role trial: (u,v) versus (v,u)
edge permutation after reconstruction
three pair witnesses of one all-three-face object
```

No orientation may be discarded merely because one component of `{u,v}` is larger: for the third opposite-edge representation `(c,x)`, the ordering of `c` and `x=sqrt(a^2+b^2)` is not fixed in general.

## 5. What one representation can and cannot enumerate

A single representation

```text
d^2 = a^2+F^2
```

only says that `a` is an edge and `F` is the opposite face diagonal. It does **not** determine the two edges spanning `F`.

To enumerate the full one-active-face population from a diagonal-first engine one needs a nested decomposition

```text
F^2 = b^2+c^2.
```

Then `(a,b,c)` has integer space diagonal `d` and at least that one active face; the other two faces are tested afterward.

Consequently there are two distinct α workloads:

```text
PAIR_COLLISION_MODE:
    complete enumeration of two-face-or-more objects from collisions inside Rep(d^2)

NESTED_SINGLE_FACE_MODE:
    complete enumeration of the full one-face population by Rep(d^2) followed by Rep(F^2)
```

The immediate performance experiment should prioritize `PAIR_COLLISION_MODE`, because Stage14-num6 currently freezes the two-face population `N2` and `T` and this mode is closest to the historical high-range perfect-cuboid search architecture.

## 6. Primitive semantics

Primitive normalization is a property of the reconstructed physical edge triple:

```text
gcd(a,b,c)=1.
```

It must be checked after reconstruction/canonicalization. A restriction on `d` or on a single sum-of-two-squares representation is not by itself a substitute for the Stage14 primitive contract.

Scaled copies share the same representation geometry after scaling and must be removed exactly as in ordinary num.

## 7. Physical cutoff semantics

For every physical cuboid,

```text
max(a,b,c) < d.
```

Therefore a search bounded by space diagonal `d<=D` is not automatically identical to an edge-height search `max(a,b,c)<=B`: it is a different finite region.

For α1 the conversion is deliberately not guessed. The α2 reference enumerator must support both filters on each reconstructed object:

```text
DIAGONAL_CUTOFF: d<=D
ORDINARY_STAGE14_CUTOFF: existing main-num physical B predicate
```

Exact overlap with main num is judged only using the latter predicate. α5 will formalize the optimal diagonal envelope needed to cover a given ordinary `B` cutoff without omission.

## 8. Relation to the Belogourov search architecture

Belogourov's diagonal-first search fixes the body diagonal `g`, factors/sieves it, generates Girard sum-of-two-squares representations of `g^2`, and combines representations to test cuboid compatibility. The author's earlier/full version retained several almost-perfect classes; later speed-oriented versions intentionally skipped most almost-perfect checks.

Stage14-num-α adopts only the **enumeration architecture**:

```text
fix d -> generate Rep(d^2) -> collide compatible representations.
```

It does not import historical almost-perfect counts as a census, and it may not copy any optimization that discards exactly-two objects.

Primary/authoritative descriptions checked for α1:

- Alexander Belogourov, *Distributed search for a perfect cuboid* (2022 author manuscript / distributed-search report).
- Belogourov's earlier project description of the same diagonal-decomposition search architecture.

## 9. Exact α2 interface

The α2 reference implementation should expose the following auditable primitives:

```text
representations_of_square(d) -> unordered positive pairs {u,v} with u^2+v^2=d^2
ordered_roles({u,v}) -> (u,v),(v,u)
collide((a,Fa),(b,Fb)) -> c or NONE
canonicalize(a,b,c) -> ordinary Stage14 object key
face_mask(a,b,c) -> ordinary Stage14 three-face mask
primitive(a,b,c) -> gcd(a,b,c)==1
```

For every tested ordinary cutoff, α2 must compare exact key sets rather than only counts.

Required α2 locks:

```text
ALPHA_PAIR_COLLISION_N2_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_FACE_MASKS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_T_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_RAW_EDGE_KEYS_EQUAL_MAIN=true
```

If α2 also implements nested one-face mode, that comparison is additional and must use the corresponding main-num one-face source contract; it is not required to validate the pair-collision accelerator first.

## 10. α1 decision

The diagonal-first idea is mathematically compatible with the exact Stage14 two-face census.

```text
PAIR_COLLISION_ENUMERATION_COMPLETE_FOR_TWO_FACE_OR_MORE=true
ALL_THREE_REQUIRES_CANONICAL_DEDUP_OF_THREE_WITNESSES=true
UNORDERED_REPRESENTATION_WITHOUT_ROLE_TRIAL_INCOMPLETE=true
FULL_ONE_FACE_FROM_PAIR_COLLISIONS_ALONE=false
FULL_ONE_FACE_REQUIRES_NESTED_FACE_DECOMPOSITION=true
PRIMITIVE_FILTER_MUST_USE_RECONSTRUCTED_EDGE_TRIPLE=true
PHYSICAL_B_TO_DIAGONAL_ENVELOPE_NOT_YET_LOCKED=true
MEANINGFUL_SPEEDUP_PROVED=false
```

The important outcome is that the fast historical idea can be tested **without weakening `N2/T` completeness**. The first implementation does not need to reproduce the entire one-face family before we know whether the diagonal collision engine is worthwhile.

## Next

`Stage14-num-α2`: build a deliberately simple reference implementation of the ordered-representation collision theorem and compare its canonical two-face object keys, face masks, raw-edge keys and `T` exactly against ordinary num on small frozen cutoffs.
