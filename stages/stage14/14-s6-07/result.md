# Stage14-s6-07 — third-face transfer, dual half-angle gcd matrix, and root-sign no-go

## Purpose

Stage14-s6-06 replaced the abstract global-small-point denominator by the exact physical compact selector attached to

```text
Q0 = P_phys + (0,0)
```

and proved that its denominator is controlled by the `H2-S2` half-angle factor of the primitive partner face.  The next proposed step was to count the square-cancellation/root-sign pattern directly on physical edges.

This stage performs that audit before imposing a probabilistic or large-sieve model on the root signs.

The main structural discovery is that every physical ordered edge canonically produces a **third primitive Pythagorean face**

```text
F3 = primitive(H*S2, S*X2, G),
G = gcd(S,S2)*d,
```

with hypotenuse at most the original physical cutoff.  The original first face and the physical space diagonal are recoverable from `(F2,F3)`, so this is an injective re-encoding of the physical edge rather than an upper-majorant relaxation.

After introducing the second compact torsion translate

```text
Q1 = P_phys + (-X^2,0),
```

the two compact denominators are controlled by the complementary partner half-angle factors `H2-S2` and `H2+S2`.

For every odd prime power of `X2` not supported on the first hypotenuse `H`, the root sign is then exactly equivalent to membership in one cell of a **2 x 2 gcd matrix** between the minus/plus half-angle parameters of `F2` and `F3`.

Consequently the root signs are not independent Bernoulli data which may be assigned a `2^{-omega}` probability for free.  They are the deterministic divisor allocation in the factorization

```text
(G-H*S2)(G+H*S2)=S^2*X2^2.
```

The stage therefore closes a tempting but invalid root-sign-only power-saving route.  It replaces it by a concrete same-modulus incidence receiver: a large partner leg forces either a large cross-prime overlap with `H` or a large half-angle gcd cell between two primitive Pythagorean faces, while the pair `(F2,F3)` must also satisfy one exact cross-product square condition.

No external theorem is used.

---

## 1. Frozen physical ordered edge

Let

```text
F1=(S,X,H),
F2=(S2,X2,H2)
```

be primitive oriented Pythagorean faces forming an actual Stage14 physical edge with integer space diagonal `d<=B`.  Put

```text
g=gcd(S,S2),
G=g*d.
```

Merged s6-06 proves

```text
G^2=S^2*H2^2+X^2*S2^2
   =H^2*S2^2+S^2*X2^2.
```

Hence

```text
(H*S2)^2+(S*X2)^2=G^2.                 (7.1)
```

The two factors of the associated difference of squares are

```text
Uminus = G-H*S2,
Uplus  = G+H*S2,
```

and satisfy

```text
Uminus*Uplus=S^2*X2^2.                 (7.2)
```

All quantities in this stage refer to this exact physical ordered edge.

---

## 2. Exact third primitive Pythagorean face

Set

```text
c = gcd(H,X2).
```

Because both `F1` and `F2` are primitive,

```text
gcd(S,H)=1,
gcd(S2,X2)=1.
```

A prime-by-prime check therefore gives

```text
gcd(H*S2, S*X2)=g*c.                   (7.3)
```

Moreover `g` and `c` are coprime.  Since the left side of (7.3) divides the hypotenuse `G=g*d` of (7.1), one obtains

```text
c|d.
```

Define

```text
S3 = H*S2/(g*c),
X3 = S*X2/(g*c),
H3 = G/(g*c)=d/c.
```

Then

```text
S3^2+X3^2=H3^2,
gcd(S3,X3)=1,
H3<=d<=B.
```

Thus

```text
F3=(S3,X3,H3)
```

is a primitive oriented Pythagorean face inside the same physical cutoff.

We record

```text
THIRD_PRIMITIVE_PYTHAGOREAN_FACE_EXACT=true
THIRD_FACE_HYPOTENUSE_LE_B=true.
```

---

## 3. The transfer is injective and keeps the physical edge

The ratio of the first face is recovered from `F2,F3` by

```text
X3*S2 / (S3*X2) = S/H.                 (7.4)
```

Since `gcd(S,H)=1`, reducing the fraction on the left recovers the ordered pair `(S,H)` exactly.  Then

```text
X=sqrt(H^2-S^2)
```

is uniquely determined by positivity, and

```text
c=gcd(H,X2),
d=c*H3.
```

Therefore two physical ordered edges with the same `(F2,F3)` are identical.

```text
PHYSICAL_EDGE_TO_F2_F3_INJECTIVE=true.
```

No graph-degree multiplicity or arbitrary global representative is introduced by this transfer.

---

## 4. Exact compatibility square for `(F2,F3)`

Equation (7.4) also gives an intrinsic necessary condition on a pair of primitive faces.

Put

```text
A=S3*X2,
C=X3*S2.
```

For a physical image,

```text
C/A=S/H,
```

so

```text
A^2-C^2
 = (X*S2*X2/(g*c))^2.                 (7.5)
```

Hence

```text
boxed:
(S3*X2)^2-(X3*S2)^2 is a nonzero integer square.
```

Conversely, within the actual image, the square root and the reduced ratio recover the first face exactly as above.  We do not claim that an arbitrary pair of primitive faces satisfying only (7.5) automatically satisfies every Stage14 orientation/gluing condition.

This gives the next counting problem a concrete ambient equation:

```text
F2 primitive Pythagorean,
F3 primitive Pythagorean,
H2,H3<=B,
(S3*X2)^2-(X3*S2)^2=square.            (7.6)
```

We record

```text
F2_F3_CROSS_PRODUCT_SQUARE_NECESSARY=true.
```

---

## 5. Uniform minus/plus half-angle coordinates

For any primitive oriented Pythagorean face

```text
F=(A,B,C),
A^2+B^2=C^2,
```

define `kappa(F) in {1,2}` and positive integers

```text
t_-(F), t_+(F)
```

by

```text
C-A = kappa(F)*t_-(F)^2,
C+A = kappa(F)*t_+(F)^2.                (7.7)
```

Explicitly, for Euclid parameters `m>n`,

- if `A=2mn`, then `kappa=1`, `t_-=m-n`, `t_+=m+n`;
- if `A=m^2-n^2`, then `kappa=2`, `t_-=n`, `t_+=m`.

At odd primes,

```text
gcd(t_-(F),t_+(F))=1.                  (7.8)
```

Write

```text
t2-=t_-(F2),  t2+=t_+(F2),
t3-=t_-(F3),  t3+=t_+(F3).
```

For odd primes, the full prime power of `X2` lies in exactly one of `t2-` or `t2+`.

---

## 6. Two exact compact torsion selectors

### 6.1 The `T0=(0,0)` selector

Merged s6-06 gives

```text
N0 = H*G-S^2*H2-X^2*S2,
R- = H2-S2,
Z0 = -N0/R-.
```

If `D0` is the reduced square denominator of `Z0`, then

```text
D0^2=R-/gcd(N0,R-),
D0|t2-.                                      (7.9)
```

### 6.2 The `T1=(-X^2,0)` selector

The second nonidentity real 2-torsion point gives

```text
Z1=-X^2*(ZP-S^2)/(ZP+X^2).
```

Using the exact s6-06 physical coordinate and

```text
(H*H2-G)(H*H2+G)=X^2*X2^2,
```

one obtains

```text
Z1=-(G+H*S2)*(H*H2-G)/X2^2.
```

The numerator product has the exact factorization

```text
(G+H*S2)*(H*H2-G)
 =(H2-S2)*(H*G-S^2*H2+X^2*S2).
```

Therefore, putting

```text
N1 = H*G-S^2*H2+X^2*S2,
R+ = H2+S2,
```

we have

```text
boxed:
Z1=-N1/R+.                                  (7.10)
```

If `D1` is its reduced square denominator, then

```text
D1^2=R+/gcd(N1,R+),
D1|t2+.                                      (7.11)
```

Both points lie on the compact real component, are nonzero modulo `2E(Q)`, preserve canonical height, and are invertible back to the same physical point.

Thus the physical edge carries complementary compact selectors attached to **both** partner half-angle columns.

```text
DUAL_COMPACT_HALF_ANGLE_SELECTORS_EXACT=true.
```

---

## 7. Good partner-leg primes become a 2 x 2 gcd matrix

Let

```text
p^e || X2
```

with `p` odd and `p` not dividing `H`.

Because `p|X2`, primitivity gives `p not dividing S2`; because `p not dividing H`, the two factors in (7.2) cannot both be divisible by `p`:

```text
gcd(G-H*S2,G+H*S2) | 2*H*S2.
```

The full `p`-valuation of the right side of (7.2) is therefore carried by exactly one factor.

Also `p` does not divide the third-face scale `g*c`: `p not dividing g` since `g|S2`, and `p not dividing c` by definition of `c=gcd(H,X2)`.  Since

```text
G-H*S2 = g*c*(H3-S3),
G+H*S2 = g*c*(H3+S3),
```

we obtain the exact dichotomy

```text
G == +H*S2 mod p^(2e)
  <=> p^e | t3-,

G == -H*S2 mod p^(2e)
  <=> p^e | t3+.                            (7.12)
```

(The third half-angle may contain a higher power when `p|S`; the gcd with the partner half-angle still contains exactly `p^e`.)

Now define the four odd-good gcd cells

```text
q-- = gcd(t2-,t3-) on p not dividing 2H,
q-+ = gcd(t2-,t3+) on p not dividing 2H,
q+- = gcd(t2+,t3-) on p not dividing 2H,
q++ = gcd(t2+,t3+) on p not dividing 2H.
```

More formally these are the corresponding gcds restricted to the prime powers of `X2` coprime to `2H`.

Then every odd good prime power `p^e||X2` occurs in exactly one cell, with its full exponent `e`.  Hence the four cells are pairwise coprime and

```text
boxed:
q--*q-+*q+-*q++ = X2_good,                 (7.13)
```

where

```text
X2_good = product_{p^e||X2, p odd, p not dividing H} p^e.
```

This is the exact root-sign state space.

```text
GOOD_ODD_ROOT_SIGN_GCD_MATRIX_EXACT=true
GOOD_PART_X2_FOUR_GCD_CELL_PRODUCT=true.
```

---

## 8. The compact denominators are two of the four gcd cells

The root-sign laws of s6-06 and Section 6 translate directly into the matrix.

For the good odd part:

```text
D0_good          = q-+,
(t2-/D0)_good    = q--,
D1_good          = q+-,
(t2+/D1)_good    = q++.                    (7.14)
```

Thus:

- `q-+` is the good denominator part of the `(0,0)` compact selector;
- `q+-` is the good denominator part of the `(-X^2,0)` compact selector;
- `q--` and `q++` are the corresponding square-cancellation cofactors.

The four objects are not separate random phenomena.  They are one deterministic 2 x 2 factorization table.

---

## 9. Why independent root-sign probability is not available

For a fixed partner face, one might be tempted to say that each good prime has two square roots and therefore costs a factor about `1/2` when a specified root sign is required.

Equation (7.12) shows why this is not a theorem.

Once the physical third face is present, the sign at `p` is already determined by whether `p^e` lies in `t3-` or `t3+`.  Across all good primes the sign pattern is simply a divisor allocation between the two coprime third half-angle parameters.  The number of formal allocations is at most

```text
2^omega(X2_good)=B^o(1),
```

but there is no justified density factor

```text
2^(-omega(X2_good))
```

on the physical set.

Equivalently, the character/root-sign condition is a re-expression of the exact factorization (7.2), not an independent sieve condition imposed after physicality.

Therefore

```text
ROOT_SIGN_INDEPENDENT_BERNOULLI_MODEL_JUSTIFIED=false
ROOT_SIGN_ONLY_POWER_SAVING_PROVED=false.
```

This is analogous to the exact-witness character resonance isolated in s6-04: once the physical relation is imposed, one must count the resulting shared-factor incidence rather than assign independent probability to it.

---

## 10. A deterministic five-factor large-incidence dichotomy

Let

```text
X2_cross = X2/X2_good.
```

This contains the 2-primary part and the full prime powers of `X2` whose primes divide `H`.

Combining (7.13),

```text
boxed:
X2 = X2_cross*q--*q-+*q+-*q++.             (7.15)
```

Hence every physical ordered edge satisfies

```text
max(X2_cross,q--,q-+,q+-,q++) >= X2^(1/5). (7.16)
```

This is a genuine deterministic replacement for a root-sign probability heuristic.

There are only five possible receivers:

1. a large cross-prime overlap between the first hypotenuse `H` and partner leg `X2`;
2. one of four large shared half-angle gcd cells between `F2` and `F3`.

```text
FIVE_FACTOR_LARGE_INCIDENCE_DICHOTOMY=true.
```

---

## 11. Remove a small-partner-leg sector at square-root scale

Independently of open parallel work, primitive Euclid parameterization gives

```text
#{primitive oriented F2: H2<=B, X2<=Y} << Y*log(2B).
```

Merged Stage14-4ag gives maximum physical graph degree `B^o(1)`.  Thus physical edges with

```text
X2<=Y
```

are

```text
<< Y*B^o(1).                                (7.17)
```

Choose the same harmless margin

```text
Y=B^(41/84).
```

Then

```text
41/84 < 1/2,
```

so this whole sector is already below the square-root scale.

Every square-root-relevant residual edge therefore has

```text
X2>B^(41/84).
```

By (7.16), at least one of the five exact incidence factors satisfies

```text
boxed:
factor > B^(41/420).                        (7.18)
```

We record

```text
SMALL_X2_SECTOR_SQRT_CONTROLLED=true
FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420.
```

This does not by itself count the large-cell sector; it isolates a fixed positive-power modulus/gcd on every residual physical edge.

---

## 12. Exact receiver for Stage14-s6-08

The next stage no longer needs to discuss an abstract least denominator or a probabilistic root sign.

Every residual physical edge injects into a pair `(F2,F3)` of primitive Pythagorean faces with `H2,H3<=B` satisfying

```text
(S3*X2)^2-(X3*S2)^2 = square,               (7.19)
```

and carrying at least one large incidence object:

```text
X2_cross > B^(41/420)
```

or

```text
q_{ij} > B^(41/420)
```

for one of four half-angle gcd cells.

For a half-angle cell `q`, the same modulus divides one Euclid half-angle coordinate of `F2` and one of `F3`.  This is precisely a **same-modulus collision**, not two independent local conditions.

The correct next problem is therefore:

> count compatible pairs `(F2,F3)` satisfying (7.19) when one shared half-angle gcd or the cross-prime overlap is at least a fixed positive power of `B`.

This is structurally aligned with the same-modulus/shared-prime dispersion receiver independently isolated by the Stage14-t route, but s6-07 does not import any unproved t-route power saving.

---

## 13. Quantitative status

The unconditional physical upper bound remains

```text
V(B) <<_epsilon B^(41/42+epsilon).
```

No full post-local exponent is claimed in this stage.

What is new is that the unresolved physical family has been transformed from

```text
root-sign distribution on one abstract witness
```

to

```text
injective pair of primitive Pythagorean faces
+ exact cross-product square
+ forced positive-power shared-gcd/cross-prime incidence.
```

This is a strictly sharper counting target, while avoiding both previous quantifier gaps:

- no coordinate-density estimate is multiplied into an unweighted packet count;
- no independent probability is assigned to a sign already forced by the physical factorization.

---

## 14. Boundary

```text
STAGE14_S6_07=COMPLETE_THIRD_FACE_TRANSFER_DUAL_HALF_ANGLE_GCD_MATRIX_AND_ROOT_SIGN_NOGO
THIRD_PRIMITIVE_PYTHAGOREAN_FACE_EXACT=true
THIRD_FACE_HYPOTENUSE_LE_B=true
PHYSICAL_EDGE_TO_F2_F3_INJECTIVE=true
F2_F3_CROSS_PRODUCT_SQUARE_NECESSARY=true
DUAL_COMPACT_HALF_ANGLE_SELECTORS_EXACT=true
GOOD_ODD_ROOT_SIGN_GCD_MATRIX_EXACT=true
GOOD_PART_X2_FOUR_GCD_CELL_PRODUCT=true
DUAL_SELECTOR_DENOMINATOR_GCD_CELLS_IDENTIFIED=true
ROOT_SIGN_INDEPENDENT_BERNOULLI_MODEL_JUSTIFIED=false
ROOT_SIGN_ONLY_POWER_SAVING_PROVED=false
FIVE_FACTOR_LARGE_INCIDENCE_DICHOTOMY=true
SMALL_X2_SECTOR_SQRT_CONTROLLED=true
FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
SAME_MODULUS_COLLISION_RECEIVER_DEFINED=true
ABSTRACT_EXISTENCE_COORDINATE_MULTIPLICATION_REQUIRED=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s6-08
```
