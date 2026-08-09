# Stage14-4bn — exact physical-pair converse and active-direction reduction

## Purpose

Merged Stage14-4bm leaves the only unresolved main-track sector in the form

```text
X2 > B^(20/21),
X2_cross < B^(4/21),
q_ij >> B^(4/21) for one good half-angle gcd cell,
normalized squareclass/kernel compatibility.
```

The planned next move was a new signed reduced-quartic dispersion theorem.  Before building another analytic machine, this stage compares the physical `(F2,F3)` transfer with the already-merged Stage14-t36 fixed-direction squareclass theorem and audits the converse direction of the s6-07 transfer.

Two stronger structural facts result.

1. The s6-07 cross-product-square condition is not merely necessary.  After adding the exact reconstructed cutoff, it is **sufficient**, and gives an inverse to the physical-edge transfer.
2. The fixed-direction target is exactly the t36 squareclass `[-1]`, with a universal rational anchor `(p,q)=(0,1)`.  Hence every fixed primitive partner direction has only `B^o(1)` admissible physical partners.  No new fixed-fiber dispersion theorem is needed.

Thus the unresolved count is exactly an **active-direction count**: how many primitive `F2` directions admit at least one admissible positive cross-square partner `F3` inside the physical cutoff?

No result from open Stage14-s6-09 is used as a theorem input; the fixed-fiber transfer is rederived from merged s6-08 and merged t36.

---

## 1. Merged inputs

We use only merged results.

### 1.1 Merged s6-07 / s6-08

Every physical ordered edge gives primitive oriented Pythagorean faces

```text
F2=(S2,X2,H2),
F3=(S3,X3,H3)
```

with

```text
(S3*X2)^2-(X3*S2)^2 = square > 0.
```

In half-angle coordinates

```text
a=t_-(F2), b=t_+(F2),
c=t_-(F3), d=t_+(F3),
```

the raw square detector is

```text
Delta0=(a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c).
```

Merged s6-08 extracts the automatic good-gcd square and identifies the normalized same-kernel collision.

### 1.2 Merged t36

For a fixed direction `0<a<b`, define

```text
F_ab(p,q)
=(b^2*p^2-a^2*q^2)
 (b^2*q^2-a^2*p^2).
```

Merged t36 proves uniform `B^o(1)` multiplicity for a fixed rational squareclass in a polynomial-height direction fiber, by the associated genus-one collision curve and the merged t22 bounded-height mechanism.

### 1.3 Merged 4bm

The small-partner-leg and cross-prime branches already satisfy

```text
X2 <= B^(20/21)                 -> O(B^(20/21+o(1))),
X2_cross >= B^(4/21)            -> O(B^(61/63+o(1))).
```

The unresolved family has a large good gcd cell `q_ij >> B^(4/21)` and the normalized s6-08 kernel collision.

---

## 2. Define admissible primitive-face pairs

Let

```text
F2=(S2,X2,H2),
F3=(S3,X3,H3)
```

be primitive oriented Pythagorean faces.

Put

```text
A = S3*X2,
C = X3*S2.
```

Call `(F2,F3)` a **positive cross-square pair** if

```text
A>C>0,
A^2-C^2=Y^2
```

for an integer `Y>0`.

Let

```text
h0 = gcd(A,C),
H  = A/h0,
S  = C/h0,
X  = Y/h0.
```

Since `h0^2 | Y^2`, one has `h0|Y`, and therefore

```text
S^2+X^2=H^2,
gcd(S,H)=1,
```

hence also `gcd(S,X)=1`.  Thus

```text
F1=(S,X,H)
```

is a primitive oriented Pythagorean face.

Define

```text
g = gcd(S,S2),
c0 = gcd(H,X2).
```

The reconstructed space diagonal is

```text
d_rec = c0*H3.
```

For the physical cutoff `B`, call the pair **B-admissible** when additionally

```text
d_rec<=B.
```

The `d_rec` condition is essential: `H3<=B` alone is only an upper-majorant condition because `c0` may exceed `1`.

---

## 3. Exact scale lemma

For a positive cross-square pair, the ratio identity

```text
C/A=S/H
```

is equivalent to

```text
H*X3*S2 = S*S3*X2.
```

Because both `F1` and `F2` are primitive,

```text
gcd(S,H)=1,
gcd(S2,X2)=1.
```

A prime-by-prime calculation gives

```text
boxed:
gcd(H*S2,S*X2)=g*c0,
```

and also

```text
gcd(g,c0)=1.
```

Since `(S3,X3)=1` and

```text
(H*S2)/(S*X2)=S3/X3,
```

we therefore obtain the exact scale identities

```text
boxed:
H*S2 = g*c0*S3,
S*X2 = g*c0*X3.
```

Taking hypotenuses gives

```text
boxed:
sqrt(H^2*S2^2+S^2*X2^2)=g*c0*H3=g*d_rec.
```

This is precisely the forward `G=g*d` identity of merged s6-07, now derived in the converse direction.

---

## 4. Reconstruct the primitive raw cuboid

Define raw edges

```text
Araw = S*S2/g,
Braw = X*S2/g,
Craw = X2*S/g.
```

Then the first two face diagonals are automatically integral:

```text
Araw^2+Braw^2 = (H*S2/g)^2,
Araw^2+Craw^2 = (H2*S/g)^2.
```

The space diagonal satisfies

```text
Araw^2+Braw^2+Craw^2
 = (H^2*S2^2+S^2*X2^2)/g^2
 = (g*d_rec)^2/g^2
 = d_rec^2.
```

Thus every positive cross-square pair reconstructs an integer-space-diagonal cuboid with the two prescribed integer face diagonals.

It is primitive.  Write

```text
S=g*s,
S2=g*t,
gcd(s,t)=1.
```

Then

```text
Araw=g*s*t,
Braw=X*t,
Craw=X2*s.
```

A common prime divisor cannot lie in `s` or `t` because of the primitive-face coprimalities, and a prime dividing `g` cannot divide both `X` and `X2`.  Hence

```text
boxed:
gcd(Araw,Braw,Craw)=1.
```

The reduced first and second faces are exactly `F1` and `F2`.

---

## 5. The transfer is a bijection after the exact cutoff is retained

Starting from a physical ordered edge, merged s6-07 constructs

```text
F3=primitive(H*S2,S*X2,g*d),
```

with scale `g*c0`, so

```text
H3=d/c0.
```

Applying the converse construction of Sections 2--4 returns the same `F1`, the same raw primitive cuboid, and

```text
d_rec=c0*H3=d.
```

Conversely, start from a B-admissible positive cross-square pair.  The raw cuboid constructed in Section 4 is primitive, has two integer face diagonals and integer space diagonal `d_rec<=B`.  Applying the merged s6-07 third-face construction divides

```text
(H*S2,S*X2,g*d_rec)
```

by the exact scale `g*c0`, and therefore returns exactly the original `F3`.

Hence:

```text
boxed:
physical ordered edges with d<=B
<->
B-admissible positive cross-square pairs (F2,F3).
```

This upgrades the former one-way transfer to an exact counting equivalence.

```text
PHYSICAL_EDGE_TO_CROSS_SQUARE_PAIR_BIJECTION=true.
```

---

## 6. Exact identification with the merged t36 target class

Write the two primitive faces in half-angle coordinates

```text
a=t_-(F2), b=t_+(F2),
c=t_-(F3), d=t_+(F3).
```

Merged s6-08 gives

```text
Delta0
=(a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c)
```

and every physical / admissible pair has

```text
Delta0=square > 0.
```

But

```text
F_ab(c,d)
=(b^2*c^2-a^2*d^2)
 (b^2*d^2-a^2*c^2)
=-Delta0.
```

Therefore every admissible partner lies in the fixed t36 squareclass

```text
boxed: [-1].
```

There is a universal anchor in that class for every direction:

```text
F_ab(0,1)=(-a^2)*(b^2)=-(ab)^2.
```

Thus the t36 collision theorem may be applied using `(0,1)` as a fixed reference point.  It is not necessary to first choose one physical partner in the fiber.

Since `H2,H3<=B` implies

```text
a,b,c,d <= sqrt(2B),
```

the merged t36 polynomial-height hypotheses hold uniformly.

Consequently

```text
boxed:
# {B-admissible physical partners F3 for fixed F2}
<= B^o(1).
```

The exact cutoff `d_rec<=B` only removes points, so it cannot worsen this bound.

This closes the planned fixed-fiber signed-dispersion task without a new large-sieve theorem.

---

## 7. A symmetric reverse-fiber bound

The same quartic is symmetric in the two directions:

```text
F_cd(a,b)=Delta0.
```

The target squareclass for fixed `F3` is therefore `[+1]`.  A universal rational anchor is

```text
(p,q)=(1,1),
F_cd(1,1)=(d^2-c^2)^2.
```

Merged t36 thus also gives

```text
boxed:
# {admissible F2 for fixed F3}
<= B^o(1).
```

Hence the exact admissible cross-square graph has subpolynomial degree on **both** vertex classes.

This does not by itself make the active vertex set power-sparse: a large matching can have degree one on both sides.

---

## 8. Exact active-direction counting object

Define

```text
A_phys(B)
= # {primitive oriented F2:
     there exists a B-admissible positive cross-square partner F3}.
```

By the bijection and fixed-F2 bound,

```text
boxed:
A_phys(B)
<= E_phys^ord(B)
<= A_phys(B)*B^o(1).
```

Thus ordered physical-edge count and active-direction count have exactly the same power exponent.

The current merged whole-family bound

```text
E_phys(B) << B^(41/42+epsilon)
```

therefore already implies

```text
A_phys(B) << B^(41/42+epsilon).
```

The remaining quantitative problem is not point multiplicity inside a direction fiber.  It is the sparsity of directions that admit even one nonboundary partner satisfying the exact reconstructed cutoff.

---

## 9. Import the merged 4bm residual localization

The exact active-direction set can be decomposed using merged 4bm.

### 9.1 Small partner leg

Directions occurring through an edge with

```text
X2<=B^(20/21)
```

contribute at most

```text
B^(20/21+o(1))
```

ordered edges, hence no more active directions.

### 9.2 Cross-prime branch

Directions occurring through an edge with

```text
X2_cross>=B^(4/21)
```

contribute at most

```text
B^(61/63+o(1)).
```

### 9.3 Unique unresolved active-direction family

Every remaining active direction has at least one admissible partner satisfying

```text
X2>B^(20/21),
X2_cross<B^(4/21),
q_ij >> B^(4/21)
```

for one good half-angle gcd cell, together with

```text
F_ab(c,d) in -Q^{*2}
```

(or equivalently the merged s6-08 normalized kernel collision) and the sharp reconstructed cutoff

```text
gcd(H,X2)*H3<=B.
```

Call this set `A_res(B)`.

Then

```text
boxed:
E_phys(B)
<< B^(20/21+o(1))
 + B^(61/63+o(1))
 + A_res(B)*B^o(1).
```

This is now the main-track counting ledger.

Any fixed saving

```text
A_res(B) << B^(41/42-delta+epsilon), delta>0,
```

gives the first whole-family post-local improvement.  If `delta>=1/126`, the already-proved cross branch `61/63` becomes the next exponent ceiling and must then be sharpened as well.

No square-root claim follows merely from controlling `A_res`; the `20/21` and `61/63` sectoral bounds are themselves still above `1/2`.

---

## 10. What route is closed

The planned Stage14-4bn task was

```text
new signed same-modulus dispersion inside a fixed large-gcd fiber.
```

Merged t36 plus the exact identity

```text
F_ab(c,d)=-Delta0
```

shows that this would duplicate an already-closed fixed-direction theorem.

Accordingly the following are no longer the missing main-track theorem:

- fixed-direction normalized-kernel multiplicity;
- fixed-direction signed squareclass cancellation;
- arbitrary packet-existence transfer;
- raw `1/q` density from the large gcd cell.

The remaining theorem is two-sided / cross-direction:

> prove that only a power-sparse subset of primitive `F2` directions admits any B-admissible target-class partner `F3`, retaining the large good gcd-cell and the sharp product cutoff.

---

## Boundary

```text
STAGE14_4BN=EXACT_PHYSICAL_PAIR_BIJECTION_AND_ACTIVE_DIRECTION_REDUCTION
MERGED_4BM_IMPORTED=true
MERGED_S6_08_IMPORTED=true
MERGED_T36_IMPORTED=true
OPEN_S6_09_USED_AS_THEOREM_INPUT=false
POSITIVE_CROSS_SQUARE_CONVERSE_PROVED=true
RECONSTRUCTED_FIRST_FACE_PRIMITIVE=true
RECONSTRUCTED_RAW_CUBOID_PRIMITIVE=true
RECONSTRUCTED_SPACE_DIAGONAL=d_rec=gcd(H,X2)*H3
EXACT_RECONSTRUCTED_CUTOFF_REQUIRED=true
PHYSICAL_EDGE_TO_CROSS_SQUARE_PAIR_BIJECTION=true
T36_TARGET_SQUARECLASS=-1
UNIVERSAL_MINUS_SQUARECLASS_ANCHOR=(0,1)
FIXED_F2_ADMISSIBLE_PARTNER_MULTIPLICITY=B^o(1)
FIXED_F3_ADMISSIBLE_PARTNER_MULTIPLICITY=B^o(1)
FIXED_FIBER_SIGNED_DISPERSION_NEW_THEOREM_REQUIRED=false
PHYSICAL_EDGE_ACTIVE_DIRECTION_EXPONENT_EQUIVALENCE=true
SMALL_PARTNER_LEG_SECTOR_BOUND=B^(20/21+o(1))
CROSS_PRIME_SECTOR_BOUND=B^(61/63+o(1))
UNRESOLVED_ACTIVE_DIRECTION_GCD_CELL_SCALE=4/21
CURRENT_ACTIVE_DIRECTION_UPPER_BOUND_EXPONENT=41/42
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bo count residual active F2 directions admitting a B-admissible target-class F3, using the exact cross-square bijection, large good gcd-cell q_ij>>B^(4/21), and sharp cutoff gcd(H,X2)*H3<=B
```
