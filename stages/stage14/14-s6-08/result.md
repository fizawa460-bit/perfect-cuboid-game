# Stage14-s6-08 — normalized cross-square resonance and kernel-collision receiver

## Purpose

Merged Stage14-s6-07 injectively re-encodes every physical ordered edge as a pair of primitive Pythagorean faces

```text
F2=(S2,X2,H2),
F3=(S3,X3,H3),
H2,H3<=B,
```

satisfying the exact necessary square condition

```text
(S3*X2)^2-(X3*S2)^2 = square.
```

It also decomposes the odd-good part of `X2` into a `2 x 2` half-angle gcd matrix between `F2` and `F3`.

Merged Stage14-4bl independently strengthens the physical denominator/cancellation ledger.  If the partner half-angle parameters are `s>t`, then the two compact torsion selectors give

```text
Q=D_+*D_-,
K=k_+*k_-,
Q*K=X2/kappa,
kappa in {1,2}.
```

The optimized physical split is

```text
X2 <= B^(20/21)
```

versus its complement.  The first sector is bounded directly by

```text
B^(20/21+o(1)),
```

while on the complement `Q` or `K` is at least the critical missing scale `B^(10/21)` up to an absolute constant.

The natural next attempt is therefore to combine a large half-angle gcd / dual selector with the cross-product square and claim an additional incidence saving.

Stage14-s6-08 audits that step before making such a claim.

The outcome is a structural resonance:

> every good gcd cell already enters the cross-product square as an **automatic square factor**.

Thus a large cell does not by itself make the raw square condition rarer.  This is the same type of quantifier/algebraic trap encountered earlier when exact witnesses made auxiliary quadratic characters identically `+1`.

After dividing out the complete gcd-matrix square factor, however, the remaining condition has a clean exact form: two normalized difference-of-squares have the same squarefree kernel.  That normalized kernel collision is the correct receiver for the next same-modulus dispersion step.

No external theorem is used in this stage.

---

## 1. Import the two exact predecessor structures

We use two merged inputs.

### 1.1 s6-07: physical edge -> pair of primitive faces

Every physical ordered edge gives an injective pair `(F2,F3)` with

```text
H2,H3<=B
```

and

```text
(S3*X2)^2-(X3*S2)^2 = Y^2 > 0.
```

No arbitrary globally soluble cover point is introduced.

### 1.2 4bl: dual physical selectors

For the primitive partner face write

```text
H2+S2=kappa*s^2,
H2-S2=kappa*t^2,
X2=kappa*s*t,
gcd(s,t)=1,
kappa in {1,2}.
```

The two exact compact selectors satisfy

```text
D_+*k_+=s,
D_-*k_-=t.
```

Hence

```text
Q:=D_+D_-,
K:=k_+k_-,
Q*K=X2/kappa.
```

The optimized physical split is

```text
X2<=B^(20/21):  O(B^(20/21+o(1))) physical edges,
X2>B^(20/21):   max(Q,K) >> B^(10/21).
```

This is a genuine physical-edge statement, not a coordinate-density estimate.

We retain all of it.

---

## 2. Half-angle coordinates for the transferred pair

For a primitive oriented Pythagorean face `F=(S,X,H)` define

```text
H-S = kappa*t_-^2,
H+S = kappa*t_+^2,
kappa in {1,2}.
```

For the two transferred faces put

```text
a=t2- = t_-(F2),
b=t2+ = t_+(F2),
c=t3- = t_-(F3),
d=t3+ = t_+(F3).
```

Then

```text
S2 = kappa2*(b^2-a^2)/2,
X2 = kappa2*a*b,
S3 = kappa3*(d^2-c^2)/2,
X3 = kappa3*c*d.
```

The parity encoded by `kappa2,kappa3` makes these integers.

Because each face is primitive,

```text
gcd(a,b)=1,
gcd(c,d)=1
```

at odd primes, with the usual finite 2-adic convention already absorbed by the two `kappa` values.

---

## 3. Exact four-bilinear factorization of the cross-product square

Define the unscaled cross product

```text
A0 = a*b*(d^2-c^2),
C0 = c*d*(b^2-a^2).
```

Then direct multiplication gives

```text
A0-C0 = (a*d-b*c)*(b*d+a*c),
A0+C0 = (a*d+b*c)*(b*d-a*c).
```

Therefore

```text
boxed:
Delta0
 = A0^2-C0^2
 = (a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c).
```

The geometric square from s6-07 is

```text
(S3*X2)^2-(X3*S2)^2
 = (kappa2*kappa3/2)^2 * Delta0.
```

For the allowed primitive parity types the factor `2/(kappa2*kappa3)` clears integrally, so every physical image has

```text
boxed: Delta0 is a nonzero integer square.
```

This is the exact half-angle form of the transferred physical square detector.

We record

```text
HALF_ANGLE_CROSS_SQUARE_FOUR_BILINEAR_FACTORIZATION=true.
```

---

## 4. Insert the s6-07 good gcd matrix

Let the four pairwise-coprime odd-good cells be

```text
q-- = gcd(a,c) on p not dividing 2H,
q-+ = gcd(a,d) on p not dividing 2H,
q+- = gcd(b,c) on p not dividing 2H,
q++ = gcd(b,d) on p not dividing 2H.
```

Merged s6-07 proves

```text
q--*q-+*q+-*q++ = X2_good.
```

For compact notation write

```text
q11=q--,
q12=q-+,
q21=q+-,
q22=q++.
```

Because the cells are pairwise coprime, there are integers `a0,b0,c0,d0` such that

```text
a = q11*q12*a0,
b = q21*q22*b0,
c = q11*q21*c0,
d = q12*q22*d0.
```

No coprimality assertion is made for the residual variables beyond what follows from the original primitive pairs; cross primes and the finite bad set remain there.

---

## 5. The entire good gcd matrix is an automatic square factor

Substitute the previous decomposition into the four bilinear factors.

First,

```text
a*d +/- b*c
 = q11*q22
   * (q12^2*a0*d0 +/- q21^2*b0*c0).
```

Second,

```text
b*d +/- a*c
 = q12*q21
   * (q22^2*b0*d0 +/- q11^2*a0*c0).
```

Therefore

```text
Delta0
 = (q11*q12*q21*q22)^2 * Delta_norm,
```

where

```text
boxed:
Delta_norm
 = (q12^2*a0*d0-q21^2*b0*c0)
   (q12^2*a0*d0+q21^2*b0*c0)
   (q22^2*b0*d0-q11^2*a0*c0)
   (q22^2*b0*d0+q11^2*a0*c0).
```

Since

```text
q11*q12*q21*q22=X2_good,
```

we obtain the exact identity

```text
boxed:
Delta0 = X2_good^2 * Delta_norm.
```

Thus every odd-good prime power allocated by the root-sign/gcd matrix contributes to the raw cross-square detector with **even valuation automatically**.

Because `Delta0` itself is a square on the physical image,

```text
boxed: Delta_norm is also an integer square.
```

This is the central s6-08 structural result.

```text
GOOD_GCD_MATRIX_SQUARE_FACTOR_EXACT=true
GOOD_GCD_PRODUCT_SQUARE_DIVIDES_CROSS_SQUARE_AUTOMATICALLY=true
NORMALIZED_CROSS_SQUARE_IS_SQUARE=true.
```

---

## 6. Consequence: large gcd-cell occupancy is not a raw square-sieve saving

Merged s6-07 forces a positive-power large incidence factor after the small-`X2` sector is removed.  Merged 4bl strengthens the dual physical product to the full critical scale `10/21` after the optimized `X2=B^(20/21)` split.

Those facts remain true.

However the identity of Section 5 shows that one may not argue

```text
large q cell
=> square condition has an additional modulus q
=> gain 1/q.
```

The raw square condition already contains `q^2` for algebraic reasons.  The large cell is part of the square, not an independent congruence imposed on it.

Equivalently, the root-sign allocation determines which bilinear pair receives the automatic square factor; it does not create a Bernoulli or independent square-sieve event.

Therefore

```text
LARGE_GCD_CELL_RAW_SQUARE_DETECTOR_SAVING_JUSTIFIED=false.
```

This does **not** say the large cell is useless.  It says the cell must remain inside the normalized coefficients when one proves cancellation/dispersion; its mere divisibility cannot be charged again as a new saving.

---

## 7. Exact normalized two-factor form

Group the normalized four factors into two difference-of-squares:

```text
F = (q12^2*a0*d0)^2 - (q21^2*b0*c0)^2,
G = (q22^2*b0*d0)^2 - (q11^2*a0*c0)^2.
```

Then

```text
boxed: Delta_norm = F*G.
```

On every physical image

```text
F != 0,
G != 0,
F*G > 0,
F*G is a square.
```

Let

```text
ker(n) = product of primes occurring to odd valuation in |n|.
```

Then for nonzero same-sign integers `F,G`,

```text
F*G is a square
<=>
ker(F)=ker(G).
```

Hence the physical image satisfies the exact collision

```text
boxed:
ker((q12^2*a0*d0)^2-(q21^2*b0*c0)^2)
 =
ker((q22^2*b0*d0)^2-(q11^2*a0*c0)^2).
```

This is the correct residual square detector after the deterministic gcd allocation has been removed.

We call it the **normalized biquadratic kernel collision**.

```text
NORMALIZED_BIQUADRATIC_KERNEL_COLLISION_EXACT=true.
```

---

## 8. A useful algebraic coupling between the two normalized factors

Before gcd normalization, put

```text
Fraw = a^2*d^2-b^2*c^2,
Graw = b^2*d^2-a^2*c^2.
```

Then

```text
Delta0=Fraw*Graw.
```

Two exact linear-combination identities are

```text
a^2*Fraw-b^2*Graw = d^2*(a^4-b^4),
b^2*Fraw-a^2*Graw = c^2*(a^4-b^4).
```

Thus once the common squarefree kernel of `Fraw,Graw` is fixed, the two square parts are not independent: they satisfy a pair of coupled difference-of-squares equations whose right sides share the same factor `a^4-b^4`.

This is another formulation of the same-modulus correlation.  Treating the two normalized square detectors independently would lose this coupling and reproduces the tensor barrier already seen on the t route.

Accordingly the next analytic input must preserve a common modulus/kernel across the two factors.

---

## 9. Compatibility with the merged 4bl exponent ledger

The merged 4bl result gives, without any use of the new normalized kernel collision,

```text
# {physical edges: X2<=B^(20/21)}
  << B^(20/21+o(1)).
```

Since

```text
41/42 - 20/21 = 1/42,
```

this is a genuine sectoral physical-edge improvement over the current global `41/42` exponent.

On the residual family

```text
X2>B^(20/21),
```

one has

```text
max(Q,K) >> B^(10/21).
```

s6-08 shows why this critical-scale product cannot simply be multiplied into the raw cross-square detector as an independent `B^(-10/21)` gain: its good-prime portion is part of the automatic square prefactor.

The correct residual problem is now:

```text
large physical dual product Q or K
+ exact normalized biquadratic kernel collision
+ coupled same-modulus structure
+ physical injective (F2,F3) parameterization.
```

No arbitrary packet selector remains.

---

## 10. Relation to the t35 shared-prime dispersion result

Merged Stage14-t35 proves that using the **same** auxiliary modulus in both coordinates recovers the polynomial loss caused by naive tensorization, but generic positive Cauchy/duality still does not produce a fixed power saving.  It leaves signed fixed-fiber cancellation as the missing analytic step.

s6-08 reaches the analogous conclusion from the physical half-angle side:

- independent treatment of the two difference-of-squares factors is structurally wasteful;
- raw gcd occupancy is resonant and cannot be charged as a second saving;
- the exact target is a same-kernel / same-modulus correlation between `F` and `G`.

We do not formally import an unproved t36 statement and do not claim that t35 by itself closes the s6 residual family.

The two routes now have a common receiver rather than merely similar vocabulary.

---

## 11. What is proved and what is not

### Proved here

1. exact four-bilinear half-angle factorization of the transferred cross square;
2. exact extraction of the complete odd-good gcd-matrix product as a square prefactor;
3. exact normalized cross-square equation;
4. exact equality of squarefree kernels of the two normalized difference-of-squares;
5. exact algebraic coupling showing why the two factors should not be tensorized independently;
6. compatibility with the merged 4bl `20/21` / `10/21` exponent ledger.

### Not proved here

- no `1/q` saving from a large raw gcd cell;
- no independent root-sign probability;
- no global bound better than `B^(41/42+epsilon)` yet;
- no square-root upper bound;
- no square-root asymptotic;
- no perfect-cuboid nonexistence theorem.

Thus

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

The `B^(20/21+o(1))` statement is a genuine bound for the small-partner-leg sector only, not the full family.

---

## 12. Next target

Stage14-s6-09 should attack the normalized collision directly.

A useful dyadic formulation is:

1. freeze dyadic sizes of `a0,b0,c0,d0` and the four pairwise-coprime cells `qij`;
2. retain a single common squarefree kernel `r` with

```text
F=r*x^2,
G=r*y^2;
```

3. use the two coupling identities rather than two independent square sieves;
4. prove a same-modulus collision/dispersion estimate which gains a fixed power on the residual `X2>B^(20/21)` family;
5. only after that combine with the direct `B^(20/21+o(1))` small-leg sector.

Any successful bound of the form

```text
# residual physical edges << B^(41/42-delta+epsilon)
```

for some fixed `delta>0` gives the first full-family post-local improvement on the s6 route.

Reaching

```text
delta>=10/21
```

would reach the square-root upper-bound scale, but s6-09 should first establish whether **any** fixed `delta>0` is available from the normalized same-kernel collision.

---

## Boundary

```text
STAGE14_S6_08=COMPLETE_NORMALIZED_CROSS_SQUARE_RESONANCE_AND_KERNEL_COLLISION_RECEIVER
MERGED_S6_07_PHYSICAL_F2_F3_TRANSFER_IMPORTED=true
MERGED_4BL_DUAL_CRITICAL_SCALE_IMPORTED=true
HALF_ANGLE_CROSS_SQUARE_FOUR_BILINEAR_FACTORIZATION=true
GOOD_GCD_MATRIX_SQUARE_FACTOR_EXACT=true
GOOD_GCD_PRODUCT_SQUARE_DIVIDES_CROSS_SQUARE_AUTOMATICALLY=true
NORMALIZED_CROSS_SQUARE_IS_SQUARE=true
LARGE_GCD_CELL_RAW_SQUARE_DETECTOR_SAVING_JUSTIFIED=false
NORMALIZED_BIQUADRATIC_KERNEL_COLLISION_EXACT=true
INDEPENDENT_TWO_FACTOR_TENSORIZATION_IS_CORRECT_NEXT_MODEL=false
SAME_MODULUS_NORMALIZED_KERNEL_RECEIVER_DEFINED=true
SMALL_PARTNER_LEG_PACKET_BOUND=B^(20/21+o(1))
SMALL_PARTNER_LEG_SAVING_VS_41_42=1/42
CRITICAL_DUAL_PRODUCT_SCALE=10/21
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s6-09
```
