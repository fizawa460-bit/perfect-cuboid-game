# Stage14-s6-09 — fixed-direction squareclass-energy transfer and active-direction barrier

## Purpose

Merged Stage14-s6-08 leaves the exact residual condition

```text
ker(F)=ker(G)
```

for two coupled normalized difference-of-squares attached to the injective physical transfer

```text
physical ordered edge -> (F2,F3).
```

The intended next step was a new same-modulus dispersion theorem for this normalized collision.

Before building another analytic machine, Stage14-s6-09 compares the s6 half-angle quartic with the already-merged Stage14-t36 fixed-direction squareclass-energy theorem.

The comparison is exact and stronger than expected:

> the raw s6 cross-square quartic is exactly the t36 quartic, up to the fixed squareclass `-1`.

Consequently the **entire fixed-F2 squareclass fiber is already controlled** by the merged t36 genus-one collision theorem.  For each fixed primitive partner direction `F2`, only `B^o(1)` transferred primitive faces `F3` can lie in the physical target squareclass.

This closes the analytic same-kernel problem *inside one direction fiber*.

It does **not** improve the current full-family exponent `41/42`, because there may still be `B^{1+o(1)}` primitive partner directions `F2` up to height `B`.  In fact, once each physical direction has only subpolynomial degree, physical edge count and active-direction count are the same at power-exponent scale.

Thus the remaining s6 problem is no longer a fixed-fiber square sieve.  It is an **active-direction sparsity problem**:

```text
How many primitive F2 directions can admit even one physical transferred F3?
```

No external theorem is introduced here.  We reuse the merged t36 theorem exactly with its proved quantifiers.

---

## 1. Merged inputs

We use three merged statements.

### 1.1 s6-07 / s6-08 physical transfer

Every physical ordered edge is injectively encoded by primitive Pythagorean faces

```text
F2=(S2,X2,H2),
F3=(S3,X3,H3),
H2,H3<=B.
```

Write their half-angle coordinates as

```text
a=t_-(F2), b=t_+(F2),
c=t_-(F3), d=t_+(F3).
```

Then the exact physical compatibility is

```text
Delta0
=(a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c)
```

with

```text
Delta0 is a nonzero positive integer square.
```

Merged s6-08 further factors the odd-good gcd-matrix square from `Delta0` and identifies the normalized same-kernel receiver.  We retain that normalization, but first inspect the raw quartic before the automatic square is removed.

### 1.2 t36 fixed-direction squareclass theorem

Merged Stage14-t36 fixes `0<a<b` and defines

```text
F_ab(p,q)
=(b^2*p^2-a^2*q^2)
 (b^2*q^2-a^2*p^2),
```

or, with `x=p/q`,

```text
f_ab(x)
=(b^2*x^2-a^2)
 (b^2-a^2*x^2).
```

For a fixed squareclass, pairwise collisions lie on a genus-one twist with four rational branch points

```text
+-a/b, +-b/a,
```

and full rational `2`-torsion.  The merged t22 bounded-height mechanism gives, uniformly in the direction and twist,

```text
same-squareclass multiplicity <= B^o(1).
```

Equivalently, if `J_ab` is any admissible fixed-direction fiber, t36 proves

```text
E_ab <= J_ab * B^o(1)
```

for its squareclass collision energy.

### 1.3 4bl small-partner-leg sector

Merged Stage14-4bl proves

```text
X2<=B^(20/21)
=> # physical edges << B^(20/21+o(1)).
```

This sectoral improvement remains valid and is not changed by s6-09.

---

## 2. Exact identification with the t36 quartic

From the four-linear factorization define

```text
Fraw=a^2*d^2-b^2*c^2,
Graw=b^2*d^2-a^2*c^2.
```

Then

```text
Delta0=Fraw*Graw.
```

Now evaluate the t36 form at

```text
(p,q)=(c,d).
```

Directly,

```text
F_ab(c,d)
=(b^2*c^2-a^2*d^2)
 (b^2*d^2-a^2*c^2)
=(-Fraw)*Graw.
```

Hence

```text
boxed:
F_ab(c,d)=-Delta0.
```

There is no approximation, dyadic loss, local completion, or change of variables beyond the half-angle coordinates already present in s6-08.

Since physical images satisfy

```text
Delta0=Y^2>0,
```

we have

```text
boxed:
F_ab(c,d)=-Y^2.
```

Thus every physical transferred face `F3` belongs to the **fixed rational squareclass `[-1]`** in the t36 direction fiber determined by `F2`.

We record

```text
S6_RAW_CROSS_SQUARE_IS_T36_QUARTIC_EXACT=true
PHYSICAL_F3_TARGET_SQUARECLASS=-1.
```

---

## 3. Height compatibility with t36

The t36 collision theorem requires polynomially bounded direction and point heights.

For a primitive Pythagorean face written in half-angle coordinates,

```text
H-S=kappa*t_-^2,
H+S=kappa*t_+^2,
kappa in {1,2}.
```

Therefore

```text
t_-^2 <= 2H,
t_+^2 <= 2H.
```

Since `H2,H3<=B`, all four half-angle variables satisfy

```text
1<=a,b,c,d<=sqrt(2B).
```

The rational slope

```text
x=c/d
```

therefore has height `B^{1/2+o(1)}`.  The direction coefficients `a,b` have the same scale.

Physical nondegeneracy `Delta0!=0` implies

```text
x != +-a/b,
x != +-b/a,
```

so no branch point of the t36 genus-one collision curve is encountered.

Hence the s6 transferred fibers satisfy the merged t36 hypotheses with room to spare.

---

## 4. Fixed-F2 physical multiplicity is subpolynomial

Fix one primitive partner face `F2`, hence fix its half-angle direction `(a,b)`.

Suppose at least one physical transferred face `F3'` occurs, with slope

```text
x'=c'/d'.
```

By Section 2,

```text
f_ab(x') in -Q^{*2}.
```

Any other physical transferred face `F3` in the same direction has

```text
f_ab(x) in -Q^{*2}.
```

Therefore

```text
f_ab(x)*f_ab(x') in Q^{*2}.
```

This is exactly a same-squareclass collision counted by merged t36.  Its genus-one twist is

```text
Y^2=f_ab(x')
    (b^2*X^2-a^2)
    (b^2-a^2*X^2),
```

with four rational branch points and full rational `2`-torsion.

The merged t36 uniform bounded-height theorem therefore gives

```text
# {physical F3 for fixed F2}
<= B^o(1).
```

A reduced positive half-angle slope determines only boundedly many primitive oriented-face lifts (the finite `kappa` choice), so no polynomial multiplicity is lost when passing from rational slope back to `F3`.

Thus

```text
boxed:
DEG_phys(F2) <= B^o(1)
```

uniformly in the primitive partner direction.

We record

```text
FIXED_F2_PHYSICAL_F3_MULTIPLICITY=B^o(1).
```

This is the direct s6 receiver of the t36 theorem.

---

## 5. Collision-energy formulation inside one s6 fiber

Let `H(F2)` be any finite ambient family of primitive transferred faces `F3` of polynomial height, with fixed `F2` direction.

For each rational squareclass `r`, put

```text
m_F2(r)
= # {F3 in H(F2): [F_ab(c,d)]=r}.
```

Then the squareclass collision energy is

```text
E(F2)=sum_r m_F2(r)^2.
```

Merged t36 applies to every fixed member of the fiber and yields

```text
boxed:
E(F2) <= |H(F2)| * B^o(1).
```

The physical target occupies the single class

```text
r=[-1].
```

Consequently both statements hold:

```text
m_F2(-1) <= B^o(1),
```

and, by the energy inequality,

```text
m_F2(-1) <= |H(F2)|^(1/2) B^o(1).
```

The direct `B^o(1)` multiplicity is the stronger statement for the exact s6 target class; the square-root energy form remains useful when later weights or enlarged target classes are introduced.

We record

```text
FIXED_F2_SQUARECLASS_COLLISION_ENERGY=J_F2*B^o(1)
NORMALIZED_KERNEL_FIBER_ANALYSIS_CLOSED=true.
```

---

## 6. Relation to the s6-08 normalized kernel collision

Merged s6-08 removes the automatic odd-good gcd-matrix square and writes

```text
Delta0=X2_good^2*Delta_norm,
Delta_norm=F*G,
ker(F)=ker(G).
```

The identity of Section 2 shows that this normalized collision is not a new independent analytic family: it is what remains after dividing a deterministic square from a member of the already-controlled t36 squareclass fiber.

Thus there is no need to prove a second fixed-direction large-sieve theorem merely to control multiplicity in one `F2` fiber.

The good gcd cells still matter for **cross-direction organization** and for canonical shared-modulus decompositions.  What is closed is only the fixed-direction squareclass multiplicity problem.

Accordingly

```text
SAME_MODULUS_NORMALIZED_KERNEL_RECEIVER_NEEDED_FOR_FIXED_FIBER=false.
```

A common-modulus dispersion may still be useful after summing over many directions, but it is no longer the missing theorem inside one direction.

---

## 7. Why this does not yet improve the global 41/42 exponent

Primitive Pythagorean faces with hypotenuse at most `B` are parameterized by coprime opposite-parity Euclid pairs in a disk of radius `B^{1/2}`.  Therefore the total number of possible primitive oriented partner directions is

```text
O(B).
```

Combining only this elementary direction count with Section 4 gives

```text
# physical edges
<= B^(1+o(1)).
```

This is weaker than the already-proved s5/s5u global physical bound

```text
B^(41/42+epsilon).
```

Numerically,

```text
1-41/42=1/42.
```

Thus fixed-direction squareclass sparsity, even at the very strong `B^o(1)` multiplicity level, does not by itself produce a new global exponent.

The merged 4bl small-partner-leg estimate remains

```text
X2<=B^(20/21)
=> B^(20/21+o(1)),
```

but on the complementary large-`X2` direction family the elementary number of possible `F2` directions is still `B^{1+o(1)}`.

Therefore

```text
T36_FIXED_FIBER_SAVING_IMPROVES_GLOBAL_41_42=false.
```

---

## 8. Active directions are the true remaining counting object

Define

```text
A_phys(B)
= # {primitive oriented F2, H2<=B:
     at least one physical transferred F3 exists}.
```

Every active direction contributes at least one physical ordered edge.  Section 4 shows it contributes at most `B^o(1)` such edges.  Therefore

```text
boxed:
A_phys(B)
<= E_phys(B)
<= A_phys(B)*B^o(1).
```

Hence **active-direction count and physical-edge count have the same power exponent**.

This is a decisive quantifier simplification.

The current global bound

```text
E_phys(B) << B^(41/42+epsilon)
```

is therefore equivalent at exponent scale to

```text
A_phys(B) << B^(41/42+epsilon).
```

Any strict global improvement now requires an active-direction theorem of the form

```text
A_phys(B)
<< B^(41/42-delta+epsilon)
```

for some fixed `delta>0`.

To reach a square-root upper bound by this route one would need

```text
A_phys(B) << B^(1/2+o(1)).
```

The missing `10/21` from `41/42` to `1/2` has therefore been transferred completely from **point multiplicity inside one elliptic/squareclass fiber** to **sparsity of the set of directions that possess any physical point at all**.

We record

```text
PHYSICAL_EDGE_ACTIVE_DIRECTION_EXPONENT_EQUIVALENCE=true
ACTIVE_DIRECTION_POWER_SAVING_REQUIRED=true.
```

---

## 9. Large gcd cells do not automatically solve active-direction sparsity

The s6-07 / s6-08 gcd matrix remains useful, but its role must be stated correctly.

A large good cell says that one half-angle coordinate of `F2` and one half-angle coordinate of some witnessing `F3` share a large divisor.  Since the witness `F3` is now known to be one of only `B^o(1)` possibilities for fixed `F2`, this is a sharply defined edge label.

However the existence of a large divisor of one coordinate of `F2` is not itself a power-sparse property of primitive directions: an integer of size `B^{1/2}` may trivially possess a large divisor (including itself).  The saving must come from the **simultaneous existence of a compatible second direction `F3`**, not from the divisor size alone.

Therefore the next stage must count active directions using a two-sided incidence/collision theorem.  Recharging the same gcd cell as a raw `1/q` density factor would repeat the resonance error already closed in s6-08.

---

## 10. New route boundary

Stage14-s6 started from an abstract global-small-point problem.  By s6-09 the hierarchy is now:

```text
physical hit
 -> exact compact global point
 -> exact second-face denominator
 -> exact half-angle divisor/root-sign data
 -> injective (F2,F3) transfer
 -> exact cross-square / normalized kernel collision
 -> fixed-F2 squareclass multiplicity B^o(1)
 -> ACTIVE F2 DIRECTIONS remain.
```

The remaining obstruction is no longer:

- Sha/global-solubility relaxation;
- arbitrary global representative choice;
- coordinate-density versus packet-existence transfer;
- root-sign independence;
- large-gcd raw square-sieve density;
- independent two-factor tensorization;
- fixed-direction same-squareclass energy.

It is specifically:

```text
cross-direction incidence strong enough to show
only a power-sparse subset of primitive F2 directions
admits any compatible physical F3.
```

This is the correct receiver for Stage14-s6-10.

---

## 11. What is and is not proved

### Proved / imported with exact applicability

1. `F_ab(c,d)=-Delta0` exactly;
2. every physical transferred `F3` lies in fixed squareclass `[-1]` for fixed `F2`;
3. merged t36 applies uniformly to these s6 fibers;
4. fixed `F2` physical multiplicity is `B^o(1)`;
5. fixed-direction squareclass collision energy is `J_F2*B^o(1)`;
6. physical-edge count and active-direction count have the same power exponent;
7. merged 4bl `B^(20/21+o(1))` small-partner-leg sector remains valid.

### Not proved

- no new full-family exponent below `41/42`;
- no active-direction power saving beyond the existing physical upper bound;
- no square-root upper bound;
- no square-root asymptotic;
- no perfect-cuboid nonexistence theorem.

The global exponent remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42.
```

---

## 12. Boundary

```text
STAGE14_S6_09=COMPLETE_FIXED_DIRECTION_SQUARECLASS_ENERGY_TRANSFER_AND_ACTIVE_DIRECTION_BARRIER
MERGED_S6_08_NORMALIZED_KERNEL_RECEIVER_IMPORTED=true
MERGED_T36_FIXED_DIRECTION_ENERGY_IMPORTED=true
MERGED_4BL_SMALL_PARTNER_LEG_BOUND_RETAINED=true
S6_RAW_CROSS_SQUARE_IS_T36_QUARTIC_EXACT=true
PHYSICAL_F3_TARGET_SQUARECLASS=-1
FIXED_F2_PHYSICAL_F3_MULTIPLICITY=B^o(1)
FIXED_F2_SQUARECLASS_COLLISION_ENERGY=J_F2*B^o(1)
NORMALIZED_KERNEL_FIBER_ANALYSIS_CLOSED=true
SAME_MODULUS_NORMALIZED_KERNEL_RECEIVER_NEEDED_FOR_FIXED_FIBER=false
PHYSICAL_EDGE_ACTIVE_DIRECTION_EXPONENT_EQUIVALENCE=true
T36_FIXED_FIBER_SAVING_IMPROVES_GLOBAL_41_42=false
ACTIVE_DIRECTION_POWER_SAVING_REQUIRED=true
CURRENT_ACTIVE_DIRECTION_UPPER_BOUND_EXPONENT=41/42
REQUIRED_ACTIVE_DIRECTION_EXPONENT_FOR_SQRT=1/2
SMALL_PARTNER_LEG_PACKET_BOUND=B^(20/21+o(1))
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s6-10
```
