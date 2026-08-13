# Stage14-4cr — two-thirds promotion and Cayley/Gaussian orientation factorization

## Status

`COMPLETE_TWO_THIRDS_PROMOTION_AND_CAYLEY_GAUSSIAN_ORIENTATION_FACTORIZATION`

Stage14-4cr consumes merged `14-s7-30`, merged `14-4cq`, and the exact Gaussian quotient/orientation dictionary of merged `14-X7`.

The decisive point is that s7-30 and 4cq give two **independent upper bounds for the same charged-once physical block**. They are not multiplied; taking their minimum is legal and introduces no double charge.

The combined envelope improves the whole-family bound from

```text
B^(11/16+o(1))
```

to

```text
boxed:
V(B) << B^(2/3+o(1)).
```

The unique remaining saturation block is

```text
theta=7/24,
phi=1/4,
c=1/3.
```

At the same time, the good common core of 4cq admits an exact two-way Cayley allocation. The two factors are precisely the same-Gaussian-orientation and opposite-Gaussian-orientation parts of the two reciprocal plus norms.

No external determinant method, genus-one theorem, large sieve, or H theorem is used.

---

## 1. Imported balanced strip and exact common-core scale

Use the merged common-core strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Merged s7-30 pins the common-core exponent exactly:

```text
C=B^(c+o(1)),
c=2*theta+2*phi-3/4.                            (1.1)
```

Write the residual exponents

```text
u_res <= B^(mu+o(1)),
v_res <= B^(nu+o(1)),
```

with

```text
mu <= 2*theta-2*phi,
nu <= 1/4+2*phi-2*theta.                         (1.2)
```

The first primitive xi-agreement pair satisfies

```text
U*V=B^(2*phi+o(1)),
gcd(U,V)=1,
```

and the common-core root-line count is

```text
#(U,V) <= B^(2*phi-c+o(1)).                      (1.3)
```

---

## 2. The s7-30 two-sided envelope

Merged s7-30 leaves `v_res` unfixed and counts the opposite signed quotient pair `(c_k^+,c_k^-)` on the same common-core quadratic root family.

Its charged-once exponent is

```text
boxed:
E_30(theta,phi)
 <= max(theta+phi+1/8, 1-2*theta).               (2.1)
```

This is a uniform whole-strip bound. In particular it implies `11/16`, but Stage14-4cr will not maximize it in isolation.

The second branch obeys

```text
1-2*theta <= 5/8                                  (2.2)
```

throughout the strip because `theta>=3/16`.

---

## 3. The 4cq dual-Cayley envelope after the scale pin

Merged 4cq proves the alternative charged-once estimate

```text
E_Cayley(theta,phi,c)
 <= 1/2+2*phi-c.                                  (3.1)
```

Substitute the exact scale pin (1.1):

```text
1/2+2*phi-(2*theta+2*phi-3/4)
 =5/4-2*theta.
```

Hence

```text
boxed:
E_Cayley(theta,phi)
 <= 5/4-2*theta.                                  (3.2)
```

This bound uses the legal quantifier order

```text
residual pair + root product XY
-> common core C by Cayley divisor data
-> first primitive common-core root pair
-> divisor-many physical reconstruction.
```

It is an alternative count of the same packet, not an extra multiplicative charge.

---

## 4. Exact 2/3 envelope

For every physical block,

```text
E(theta,phi)
 <= min(E_30(theta,phi),E_Cayley(theta,phi)).      (4.1)
```

Split at

```text
theta=7/24.                                       (4.2)
```

### 4.1. theta <= 7/24

Since `phi<=1/4`,

```text
theta+phi+1/8
 <= 7/24+1/4+1/8
 = 2/3.                                           (4.3)
```

Also (2.2) gives

```text
1-2*theta <=5/8<2/3.                              (4.4)
```

Therefore

```text
E_30<=2/3.                                        (4.5)
```

### 4.2. theta >= 7/24

By (3.2),

```text
E_Cayley
 <=5/4-2*(7/24)
 =2/3.                                            (4.6)
```

Thus on the whole strip

```text
boxed:
E(theta,phi)<=2/3.                                (4.7)
```

and therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=2/3.        (4.8)
```

Relative to merged s7-30,

```text
11/16-2/3=1/48.                                   (4.9)
```

Relative to the old 3/4 mainline,

```text
3/4-2/3=1/12.                                     (4.10)
```

---

## 5. Unique two-thirds saturation corner

Equality in Section 4 is possible only if both sides meet at the crossover.

If `theta<7/24`, then the first branch in (4.3) is strictly below `2/3`, while the second branch is at most `5/8`.

If `theta>7/24`, then (4.6) is strictly below `2/3`.

At `theta=7/24`, equality in (4.3) further requires `phi=1/4`.

Hence the unique possible saturation block is

```text
boxed:
theta=7/24,
phi=1/4.                                          (5.1)
```

The exact common-core scale is

```text
c=2*(7/24)+2*(1/4)-3/4
 =1/3.                                            (5.2)
```

The corresponding endpoint exponents are

```text
mu <= 1/12,
nu <= 1/6,
2*phi-c = 1/6.                                    (5.3)
```

Thus the live corner has the scales

```text
C       ~ B^(1/3),
XY      ~ B^(1/4),
UV      ~ B^(1/2),
alpha*delta ~ B^(7/12),
u_res  <= B^(1/12),
v_res  <= B^(1/6).                                (5.4)
```

The s7-30 second quotient square-root loss is

```text
B^(nu/2)=B^(1/12),                                (5.5)
```

and its common gcd

```text
h=gcd(c_k^+,c_k^-)
```

still satisfies

```text
oddpart(h)|X*Y.                                   (5.6)
```

This common-gcd/root-product incidence remains genuinely live.

---

## 6. Exact Cayley +/- allocation of the good common core

Use the 4cq notation after the two coordinate gcd-square peels:

```text
C_* = C/C_bad,
C_bad | (r*s*X*Y)^2.                              (6.1)
```

The two normalized Cayley ratios satisfy

```text
x^2 == y^2 == -1 (mod C_*),                       (6.2)
```

and the reciprocal equation gives

```text
lambda*x*y == 4 (mod C_*).                        (6.3)
```

Put

```text
M := 4*r*s*X*Y*epsilon_x*epsilon_k,
N := a*b*c*d.                                     (6.4)
```

Then

```text
lambda=4*M/N.                                     (6.5)
```

Section 4 of merged 4cq makes `N` a unit modulo `C_*`; (6.3) makes `lambda` a unit, hence `M` is also a unit modulo `C_*`. Therefore

```text
gcd(C_*,M*N)=1.                                   (6.6)
```

Merged 4cq proves

```text
C_* | (M-N)(M+N).                                 (6.7)
```

Define

```text
C_- := gcd(C_*,M-N),
C_+ := gcd(C_*,M+N).                               (6.8)
```

Because `C_*` is odd and

```text
gcd(M-N,M+N) | 2*M,
gcd(M-N,M+N) | 2*N,
```

(6.6) gives

```text
boxed:
gcd(C_-,C_+)=1,
C_-*C_+=C_*.                                      (6.9)
```

Thus the good common core has an exact two-way Cayley sign allocation. There is no third branch and no allocation multiplicity beyond divisor-many primewise orientation.

---

## 7. Cayley signs are Gaussian relative orientations

Let an odd prime power `p^e` divide `C_*`. By (6.2), both normalized plus hosts define square roots of `-1`.

### 7.1. The `C_-` branch

If

```text
p^e | C_-,
```

then

```text
M == N (mod p^e),
lambda == 4 (mod p^e).                            (7.1)
```

Equation (6.3) gives

```text
x*y == 1 (mod p^e).
```

Since `x^2=-1`, `x^{-1}=-x`, hence

```text
boxed:
y == -x (mod p^e).                                (7.2)
```

So `C_-` is the **opposite Gaussian orientation** support.

### 7.2. The `C_+` branch

If

```text
p^e | C_+,
```

then

```text
M == -N (mod p^e),
lambda == -4 (mod p^e).                           (7.3)
```

Equation (6.3) gives

```text
x*y == -1 (mod p^e),
```

so

```text
boxed:
y == x (mod p^e).                                 (7.4)
```

Thus `C_+` is the **same Gaussian orientation** support.

This is the exact local meaning of the two Cayley divisors.

---

## 8. Gaussian divisor factorization

Write the normalized Gaussian plus-host coordinates

```text
Z_k  := D_0+i*A_0,
Z_xi := Q_0+i*P_0,                                 (8.1)
```

where the gcd-square peels of 4cq make both coordinate pairs primitive modulo `C_*`.

Every prime of `C_*` is `1 mod 4`. Fix the Gaussian prime orientation corresponding to the root `x` on `Z_k`.

By Section 7 there exist coprime Gaussian integers `Pi_+,Pi_-`, unique up to units after the CRT orientation is fixed, with

```text
N(Pi_+)=C_+,
N(Pi_-)=C_-,                                      (8.2)
```

such that

```text
boxed:
Pi_+*Pi_-       | Z_k,
Pi_+*conj(Pi_-) | Z_xi.                           (8.3)
```

Equivalently:

- `Pi_+` is common with the same Gaussian orientation;
- `Pi_-` is common only after conjugating the second plus host.

This is compatible with merged X7: the twisted four-root data are Gaussian quotient norms after the common-core divisor is removed. Stage14-4cr uses only the exact orientation dictionary; it does not import X7's generated primes as a second spacing modulus.

```text
CAYLEY_SIGN_ALLOCATION_EQUALS_GAUSSIAN_RELATIVE_ORIENTATION=true. (8.4)
```

---

## 9. Why the Gaussian split does not yet improve below 2/3

The factorization (8.3) is structural. It does **not** by itself supply an additional independent determinant modulus.

The same common core `C_*` has merely been partitioned between same/opposite Gaussian orientations. Multiplying `C_+` and `C_-` again into the s7-30 root-line modulus would recharge the same common-core divisibility.

Likewise, merged X7 proves that the real/twisted generated primes are post-root-line factorization data, not independent outer spacing moduli.

Therefore

```text
CAYLEY_GAUSSIAN_ORIENTATION_SPLIT_ALONE_GIVES_EXTRA_SAVING=false. (9.1)
```

The next gain must couple the orientation split to the s7-30 boundary variable

```text
h=gcd(c_k^+,c_k^-),
oddpart(h)|X*Y,                                    (9.2)
```

or to a genuinely shared Gaussian quotient/resultant support across surviving packets.

---

## 10. New minimal receiver

At the unique `2/3` corner, both legal ledgers saturate simultaneously:

- the s7-30 route pays the square-root common-gcd term for the opposite quotient pair;
- the 4cq route pays the outer `XY` support while recovering `C` by Cayley divisor data;
- the good common core is split into `C_+` and `C_-` Gaussian relative orientations.

The minimal remaining mainline receiver is

```text
TwoThirdsCayleyGaussianCommonGcdRootProductIncidence.
```

It counts the corner packets satisfying simultaneously

```text
theta=7/24,
phi=1/4,
c=1/3,
oddpart(h)|X*Y,
C_+*C_-=C_*,
gcd(C_+,C_-)=1,
Pi_+Pi_- | Z_k,
Pi_+conj(Pi_-) | Z_xi,
```

with all original squarefree-cell, reciprocal reconstruction, dyadic, orientation, and charged-once masks retained.

A next step should split according to the size of `h`, `C_bad`, and the two Cayley orientation factors, and determine whether a large component forces a primitive/resultant spacing gain while the small component is divisor-reconstructible.

---

## 11. H / tH decision

No new mainline H is needed at this stage.

The new `2/3` promotion is obtained entirely by combining two already-proved elementary charged-once ledgers. The remaining receiver still has unexhausted exact gcd/divisor/Gaussian-factor structure.

The completed reciprocal-Edwards genus-one H audit remains nonminimal. The fixed-U `tH18/t69` route is a different coefficient space and is not cross-promoted.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false
T69_CROSS_PROMOTED_TO_MAINLINE=false.             (11.1)
```

Reconsider an auxiliary H only after the `h / C_bad / C_+ / C_-` size decomposition has been exhausted.

---

## Stage boundary

```text
STAGE14_4CR=COMPLETE_TWO_THIRDS_PROMOTION_AND_CAYLEY_GAUSSIAN_ORIENTATION_FACTORIZATION
MERGED_S7_30_IMPORTED=true
MERGED_4CQ_IMPORTED=true
MERGED_X7_GAUSSIAN_ORIENTATION_IMPORTED=true
COMMON_CORE_SCALE_PINNED=true
S7_30_BLOCK_ENVELOPE=max(theta+phi+1/8,1-2theta)
DUAL_CAYLEY_BLOCK_ENVELOPE=5/4-2theta
COMBINED_BLOCK_ENVELOPE_LE_2_3=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=2/3
IMPROVEMENT_OVER_11_16=1/48
IMPROVEMENT_OVER_3_4=1/12
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
TWO_THIRDS_SATURATION_THETA=7/24
TWO_THIRDS_SATURATION_PHI=1/4
TWO_THIRDS_SATURATION_COMMON_CORE_EXPONENT=1/3
TWO_THIRDS_SATURATION_URES_EXPONENT_MAX=1/12
TWO_THIRDS_SATURATION_VRES_EXPONENT_MAX=1/6
CAYLEY_GOOD_CORE_SIGN_ALLOCATION_PROVED=true
CAYLEY_C_MINUS_OPPOSITE_GAUSSIAN_ORIENTATION=true
CAYLEY_C_PLUS_SAME_GAUSSIAN_ORIENTATION=true
CAYLEY_GAUSSIAN_DIVISOR_FACTORIZATION_PROVED=true
CAYLEY_GAUSSIAN_ORIENTATION_SPLIT_ALONE_GIVES_EXTRA_SAVING=false
REMAINING_RECEIVER=TwoThirdsCayleyGaussianCommonGcdRootProductIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false
T69_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cs
```
