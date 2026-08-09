# Stage14-num-α1 — exact diagonal-first dictionary

> STATUS: `STAGE14_NUM_ALPHA1=COMPLETE_EXACT_DIAGONAL_FIRST_DICTIONARY`
>
> CLASSIFICATION: exact finite-enumeration specification only; no performance or asymptotic claim.

## 1. Frozen Stage14 population

The ordinary Stage14 numerical contract is

```text
0 < a < b < c,
gcd(a,b,c)=1,
a^2+b^2+c^2=d^2,
d <= B,
at least two of a^2+b^2, a^2+c^2, b^2+c^2 are squares.
```

Thus `B` is already the **space-diagonal cutoff**. A diagonal-first search over exactly `d<=B` uses the same physical finite region as ordinary num; there is no height-envelope conversion to prove.

This is a major compatibility advantage of the α architecture.

## 2. Opposite-edge representations

Write the three face diagonals as

```text
x^2 = a^2+b^2
y^2 = a^2+c^2
z^2 = b^2+c^2.
```

Every integral face diagonal gives one ordered representation of the same square `d^2`:

```text
(a,z), (b,y), (c,x),
```

because

```text
d^2 = a^2+z^2 = b^2+y^2 = c^2+x^2.
```

The role is ordered: first coordinate = edge, second coordinate = opposite face diagonal.

A sum-of-two-squares generator normally returns an unordered pair `{u,v}` (or a sorted pair `u<=v`). For Stage14 both role orientations must be considered:

```text
(u,v)
(v,u).
```

No universal inequality says the edge must be the smaller component.

## 3. Exact two-representation collision theorem

Take two distinct ordered representations

```text
d^2 = a^2 + F_a^2 = b^2 + F_b^2.
```

Then

```text
F_a^2 - b^2 = F_b^2 - a^2.
```

Define

```text
c^2 := d^2-a^2-b^2
     = F_a^2-b^2
     = F_b^2-a^2.
```

If this is a positive perfect square, then

```text
F_a^2 = b^2+c^2,
F_b^2 = a^2+c^2,
d^2   = a^2+b^2+c^2.
```

Therefore `(a,b,c)` is an integer cuboid with integer space diagonal and at least two integral face diagonals.

Conversely, any Stage14 object with at least two integral face diagonals supplies the two corresponding ordered opposite-edge representations, and their cross-difference is exactly the remaining edge square.

Hence, before primitive/canonical filtering,

```text
TWO_FACE_OR_MORE
<=>
two distinct ordered representations of d^2
have positive-square residual d^2-a^2-b^2.
```

This is exact, not heuristic.

## 4. Exactly two versus three faces

After reconstructing `(a,b,c)`, test all three face squares directly.

For the two witness faces integrality is automatic. The remaining test is

```text
a^2+b^2 = square ?
```

in the displayed orientation; after canonical sorting simply recompute all three masks.

- exactly two integral faces -> Stage14 `N2` object;
- all three integral faces -> Stage14 `T` object / perfect-cuboid candidate.

An all-three-face object has three active opposite-edge representations, hence three representation-pair witnesses. The α engine must deduplicate these to one physical object.

## 5. Canonicalization

The reference α enumerator must favor completeness over clever orientation pruning.

For every successful collision:

1. reconstruct positive integer `(a,b,c,d)`;
2. sort `(a,b,c)` into ordinary Stage14 order;
3. require `gcd(a,b,c)=1`;
4. recompute all three face-square tests exactly;
5. require at least two active faces;
6. emit the ordinary canonical object key and face mask;
7. deduplicate by canonical object key.

Harmless generation multiplicities include:

```text
representation-pair order,
within-representation role reversal,
edge permutation,
three pair witnesses of an all-three-face object.
```

They are removed only after exact reconstruction.

## 6. Primitive semantics

The Stage14 primitive rule is exactly

```text
gcd(a,b,c)=1.
```

It is applied to the reconstructed edge triple. No representation-level shortcut may replace this gate unless separately proved equivalent.

The historical source also checks gcds involving the space diagonal. For a genuine reconstructed cuboid this does not strengthen the primitive edge condition: a common divisor of all three edges automatically divides `d`, so the canonical Stage14 check remains the authoritative normalization.

## 7. Safe diagonal sieve inherited from the mathematics

Some diagonal-first pruning is valid for the **complete primitive Stage14 population**, not merely for perfect cuboids.

Suppose a primitive cuboid has integer space diagonal `d` and even one integral face diagonal `F` opposite edge `a`:

```text
d^2 = a^2 + F^2,
F^2 = b^2 + c^2.
```

### 7.1 `d` is odd

If `d` were even, `d^2 ≡ 0 (mod 4)`. Since a square is `0` or `1 mod 4`, `a^2+F^2 ≡0` forces `a,F` even. Then `F^2=b^2+c^2 ≡0 mod4` forces `b,c` even, contradicting `gcd(a,b,c)=1`.

Thus

```text
d is odd.
```

### 7.2 no prime `p ≡ 3 (mod 4)` divides `d`

If such a prime `p|d`, then from

```text
a^2 + F^2 ≡ 0 (mod p)
```

and the fact that `-1` is not a quadratic residue modulo `p`, we get `p|a` and `p|F`. Applying the same argument to

```text
b^2+c^2 = F^2 ≡0 (mod p)
```

gives `p|b,c`, again contradicting primitivity.

Therefore every prime divisor of `d` is `1 mod4`, and in particular

```text
d ≡ 1 (mod 4).
```

So the historical outer-loop ideas

```text
scan d = 1 mod 4
reject d having a 3 mod 4 prime factor
```

are safe for the complete Stage14 primitive population.

## 8. Historical optimizations that are NOT safe for Stage14 N2

The Belogourov source code v3.05 contains a fast `search_perfect` path. It generates Girard representations of `G^2`, then performs representation-pair collision tests. But that fast path also uses modular requirements such as the existence of an edge divisible by `11` and by `19` before accepting a candidate branch.

Those restrictions are Euler-brick/perfect-cuboid necessities; they rely on all three face diagonals being integral. They are not valid filters for an exactly-two-face Stage14 object.

This matches the author's distributed-search report: after the first full almost-perfect batch, the accelerated version became more than four times faster by deliberately abandoning most almost-perfect checks, and the later reported Face-cuboid samples are explicitly not complete.

Therefore α may import:

```text
SAFE:
  diagonal-first organization
  factorization of d
  Girard/Gaussian generation of Rep(d^2)
  d odd / d=1 mod4 primitive sieve
  no p=3 mod4 divisor of d
  exact representation collision identity
  exact square tests

UNSAFE UNTIL REPROVED FOR N2:
  perfect/Euler-brick-specific 11,19 or similar edge divisibility cuts
  geometric loop cuts whose proof assumes the missing third face is integral
  any optimization introduced by dropping almost-perfect checks
  historical Face-cuboid lists as if they were complete
```

α2 starts with **none of the unsafe cuts**.

## 9. What pair collisions do not enumerate

A single representation

```text
d^2 = a^2+F^2
```

does not determine the two edges inside `F`.

To enumerate the entire population having merely one integral face requires a nested decomposition

```text
F^2 = b^2+c^2.
```

So there are conceptually two diagonal-first modes:

```text
PAIR_COLLISION_MODE
  complete for the frozen Stage14 >=2-face population (N2 and T)

NESTED_SINGLE_FACE_MODE
  required only for a full census of all one-face objects
```

The ordinary Stage14-num3 contract already starts at **at least two faces**, so `PAIR_COLLISION_MODE` is sufficient to reproduce the current num population exactly. The ordinary `active faces` ledger is derived from those retained N2/T objects; α does not need a separate full one-face census to match it.

## 10. Relation to Belogourov's implementation

The checked public source (`renyxadarox/pcuboid`, C version 3.05) implements the same backbone:

```text
fix body diagonal G
-> factor G
-> synthesize all Girard representations G^2=A^2+F^2
-> combine representation pairs
-> test a difference/residual for being a square
-> test the remaining face square
```

In the fast path, with two sorted representations

```text
G^2=A^2+F^2=B^2+E^2,
```

the code tests

```text
C^2 = B^2-A^2,
D^2 = A^2+B^2.
```

When `C` is integral, `(A,B,C)` automatically has two integral opposite face diagonals `E,F` and space diagonal `G`; `D` distinguishes Perfect from Face. This is one canonical orientation of the general ordered-role theorem above.

The source's Girard synthesis recursively combines prime `1 mod4` sum-of-two-squares representations via the Brahmagupta-Fibonacci/Girard product identity and deduplicates the resulting pairs.

α1 imports the mathematical architecture, not its perfect-only pruning policy.

## 11. Exact α2 interface

The α2 reference implementation should expose auditable primitives:

```text
representations_of_square(d)
  -> unordered positive pairs {u,v} with u^2+v^2=d^2

ordered_roles({u,v})
  -> (u,v),(v,u)

collide((a,Fa),(b,Fb))
  -> c if d^2-a^2-b^2 is a positive square, else NONE

canonicalize(a,b,c,d)
  -> ordinary Stage14 object key

face_mask(a,b,c)
  -> exact ordinary Stage14 mask

primitive(a,b,c)
  -> gcd(a,b,c)==1
```

For a frozen cutoff `B`, α2 searches exactly

```text
d <= B
```

and compares **sets of canonical keys**, not merely counts.

Required locks:

```text
ALPHA_PAIR_COLLISION_N2_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_FACE_MASKS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_T_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_RAW_EDGE_KEYS_EQUAL_MAIN=true
ALPHA_ACTIVE_FACE_KEYS_EQUAL_MAIN=true
```

## 12. α1 decision

```text
STAGE14_NUM_ALPHA1=COMPLETE_EXACT_DIAGONAL_FIRST_DICTIONARY
PAIR_COLLISION_ENUMERATION_COMPLETE_FOR_STAGE14_NUM_POPULATION=true
PAIR_COLLISION_ENUMERATION_COMPLETE_FOR_TWO_FACE_OR_MORE=true
ALL_THREE_REQUIRES_CANONICAL_DEDUP_OF_THREE_WITNESSES=true
UNORDERED_REPRESENTATION_WITHOUT_ROLE_TRIAL_INCOMPLETE=true
FULL_ONE_FACE_FROM_PAIR_COLLISIONS_ALONE=false
FULL_ONE_FACE_REQUIRES_NESTED_FACE_DECOMPOSITION=true
PRIMITIVE_FILTER_MUST_USE_RECONSTRUCTED_EDGE_TRIPLE=true
STAGE14_PHYSICAL_CUTOFF_IS_SPACE_DIAGONAL=true
ALPHA_DIAGONAL_RANGE_EQUALS_MAIN_NUM_RANGE=true
D_ODD_AND_ONLY_1MOD4_PRIME_SUPPORT_SAFE=true
PERFECT_SPECIFIC_11_19_PRUNING_SAFE_FOR_N2=false
HISTORICAL_FAST_FACE_LIST_COMPLETE=false
MEANINGFUL_SPEEDUP_PROVED=false
```

The strongest α1 outcome is not yet speed. It is that the historical diagonal-first architecture can be tested against Stage14 **without any cutoff translation and without weakening the exact N2/T census contract**.

## Next

`Stage14-num-α2`: build the simplest standard-library ordered-role collision enumerator, use only the proven-safe diagonal sieve, and compare canonical N2/T object keys, face masks, active-face keys and raw-edge keys exactly against ordinary num on small frozen cutoffs before adding any performance optimization.
