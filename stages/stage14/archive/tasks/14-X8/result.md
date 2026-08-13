# Stage14-X8 — two-sided / dual-Cayley minimax and the 2/3 bound

## Status

`COMPLETE_TWO_SIDED_DUAL_CAYLEY_MINIMAX_AND_TWO_THIRDS_PROMOTION`

Stage14-X8 consumes merged `X7`, merged `s7-30` (PR #517), and merged `4cq` on the same balanced common-core physical packet.

The key point is that `s7-30` and `4cq` provide two different legal charged-once upper bounds for every dyadic block of the same physical family.  Therefore their minimum may be taken blockwise.  The exact common-core scale pin proved in `s7-30` converts the `4cq` alternative ledger into a one-variable affine bound.  The two estimates cross at one new interior endpoint:

```text
theta = 7/24,
phi   = 1/4,
c     = 1/3.
```

This yields the unconditional whole-family improvement

```text
boxed:
V(B) << B^(2/3+o(1)).
```

No external determinant method, genus-one theorem, large sieve, or H/tH theorem is used.

---

## 1. Imported balanced strip

Keep the merged balanced common-core coordinates

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

The cells have exponent scales

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
R,J         = B^(phi+o(1)),
S,T         = B^(3/8-phi+o(1)).
```

Write

```text
C=B^(c+o(1)).
```

Merged `s7-30` proves the exact scale pin

```text
boxed:
c = 2*theta+2*phi-3/4.                       (1.1)
```

This identity is valid on the whole balanced strip, not merely on a previous saturation face.

---

## 2. First legal bound: merged s7-30

Merged `s7-30` replaces the raw second residual support by a nonprimitive quadratic root-pair count against the already-fixed common core.  Its exact block exponent is

```text
boxed:
E_s(theta,phi)
 <= max(theta+phi+1/8, 1-2*theta).             (2.1)
```

The proof keeps the charged-once order

```text
C,u_res
-> first primitive xi-agreement pair (U,V)
-> reconstruct opposite agreement product
-> count moving opposite signed quotient pair against C
-> reconstruct v_res, X*Y and the remaining cells.
```

It gives the merged whole-family bound `11/16`, with its own isolated saturation at `theta=5/16,phi=1/4` before any use of the alternative 4cq ledger.

---

## 3. Second legal bound: merged 4cq

Merged `4cq` uses the two common-core plus hosts simultaneously.  After its gcd-square peel, fixing the residual/quotient data and `X*Y` makes the common core divisor-many.  Its alternative block ledger is

```text
boxed:
E_d(theta,phi,c)
 <= 1/2+2*phi-c.                                (3.1)
```

This is a different quantifier order from s7-30:

```text
residual pair
-> X*Y
-> recover C by dual-Cayley divisor data
-> count primitive (U,V) on the common-core root line
-> physical reconstruction.
```

The two ledgers do not charge the same moving datum twice.  They are independent upper bounds on the same physical block, so

```text
boxed:
E_X8(theta,phi,c)
 <= min(E_s(theta,phi),E_d(theta,phi,c)).        (3.2)
```

is legitimate.

---

## 4. Insert the exact common-core scale pin into the dual ledger

Substitute (1.1) into (3.1):

```text
E_d
 <= 1/2+2*phi-(2*theta+2*phi-3/4)
 = 5/4-2*theta.                                  (4.1)
```

Thus the phi and common-core exponents cancel completely in the alternative ledger:

```text
boxed:
E_d(theta) <= 5/4-2*theta.                       (4.2)
```

This sharpening was unavailable inside the original 4cq branch because 4cq was written before merged s7-30 supplied the global scale pin.

Accordingly the current blockwise estimate is

```text
boxed:
E_X8(theta,phi)
 <= min(
      max(theta+phi+1/8,1-2*theta),
      5/4-2*theta
    ).                                           (4.3)
```

---

## 5. Exact minimax bound: 2/3

We split only at

```text
theta_0 = 7/24.                                  (5.1)
```

### 5.1 theta <= 7/24

Since `phi<=1/4`,

```text
theta+phi+1/8
 <= 7/24+1/4+1/8
 = 7/24+6/24+3/24
 = 16/24
 = 2/3.                                          (5.2)
```

Also `theta>=3/16`, so

```text
1-2*theta
 <= 1-3/8
 = 5/8
 < 2/3.                                          (5.3)
```

Hence the s7-30 branch alone gives

```text
E_s(theta,phi) <= 2/3.                            (5.4)
```

### 5.2 theta >= 7/24

The dual-Cayley branch gives

```text
E_d(theta)
 <= 5/4-2*(7/24)
 = 15/12-7/12
 = 8/12
 = 2/3.                                          (5.5)
```

Therefore every balanced block satisfies

```text
boxed:
E_X8(theta,phi) <= 2/3.                           (5.6)
```

There are only `B^o(1)` dyadic refinements, so

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=2/3.       (5.7)
```

The improvement over merged s7-30 is

```text
11/16-2/3 = 33/48-32/48 = 1/48.                  (5.8)
```

The remaining gap to the square-root scale is

```text
2/3-1/2 = 1/6.                                    (5.9)
```

---

## 6. Unique 2/3 saturation point

If `theta<7/24`, then both terms in the s7-30 maximum are strictly below `2/3`:

```text
theta+phi+1/8 < 2/3,
1-2theta <= 5/8.
```

If `theta>7/24`, then

```text
5/4-2theta < 2/3.
```

Thus equality can occur only at

```text
theta=7/24.                                      (6.1)
```

At that value

```text
1-2theta = 5/12,
```

while

```text
theta+phi+1/8
 = 7/24+phi+3/24
 = 10/24+phi.                                    (6.2)
```

To reach `2/3=16/24`, we must have

```text
boxed:
phi=1/4.                                         (6.3)
```

Using (1.1),

```text
boxed:
c=2*(7/24)+2*(1/4)-3/4=1/3.                    (6.4)
```

Hence the unique possible 2/3 saturation is

```text
boxed:
theta=7/24,
phi=1/4,
c=1/3.                                         (6.5)
```

This supersedes both earlier obstruction tags:

- the `s7-30` top corner `theta=5/16,phi=1/4` is bounded by the dual ledger at `5/8`;
- the `4cq` symmetric corner `theta=phi=1/4` is bounded by the two-sided s7-30 ledger at `5/8`.

Neither is a current whole-family barrier.

---

## 7. Exact scale ledger at the new corner

At

```text
theta=7/24,
phi=1/4,
c=1/3,
```

the physical cells have scales

```text
alpha,delta = B^(7/24+o(1)),
beta,gamma  = B^(5/24+o(1)),
R,J         = B^(1/4+o(1)),
S,T         = B^(1/8+o(1)).                     (7.1)
```

The two reduced residual exponents obey

```text
mu <= 2theta-2phi = 1/12,
nu <= 1/4+2phi-2theta = 1/6.                    (7.2)
```

The first primitive common-core root pair contributes

```text
2phi-c = 1/6.                                    (7.3)
```

The second nonprimitive quotient lemma is in its pure square-root branch:

```text
nu/2 = 1/12,
nu-c = -1/6.                                     (7.4)
```

So the `M/C` contribution is negligible and the active s-side boundary is precisely the common-gcd square-root term

```text
h=gcd(c_k^+,c_k^-),
oddpart(h)|X*Y.                                  (7.5)
```

The s7-30 charged-once exponent is therefore

```text
c + mu + (2phi-c) + nu/2
 = 1/3+1/12+1/6+1/12
 = 2/3.                                          (7.6)
```

The dual-Cayley ledger simultaneously gives

```text
1/2+2phi-c
 = 1/2+1/2-1/3
 = 2/3.                                          (7.7)
```

Thus the new barrier is a genuine balance between the opposite-quotient common-gcd boundary and the fixed-`X*Y` dual-Cayley reconstruction route.

---

## 8. X7 four-root / Gaussian quotient structure at the new corner

Merged X7 remains compatible but does not by itself improve the exponent.  It proves

```text
aU-bV=2r*alpha,
aU+bV=2s*delta,
```

and, after the fixed common-core Gaussian divisor is removed, the twisted four-root support is the norm factorization of one Gaussian quotient.

At the X8 corner,

```text
H_k^+=B^(2theta+o(1))=B^(7/12+o(1)),
C=B^(1/3+o(1)).
```

Therefore the post-common-core Gaussian quotient norm has scale

```text
N(W)=B^(7/12-1/3+o(1))
    =B^(1/4+o(1)),                               (8.1)
```

matching the xi-switch product scale

```text
S*T=B^(1/4+o(1)).                                 (8.2)
```

X7's cross-resultant dictionary remains available for the next step, but its generated primes are self-generated values and cannot be recharged as an independent spacing modulus.

---

## 9. New minimal receiver

The previous X7 receiver

```text
QuarterPhiCommonCoreLinearGaussianQuotientCrossResultantEnergy
```

is now localized to the unique minimax corner and must be combined with the active common-gcd/root-product constraint and the dual-Cayley fixed-`X*Y` reconstruction.

Define

```text
Theta7Over24QuarterPhiCommonGcdCayleyGaussianQuotientEnergy.
```

Its frozen scale data are

```text
theta=7/24,
phi=1/4,
c=1/3,
UV=B^(1/2+o(1)),
C=B^(1/3+o(1)),
X*Y=B^(1/4+o(1)),
u_res<=B^(1/12+o(1)),
opposite quotient product<=B^(1/6+o(1)),
opposite quotient gcd<=B^(1/12+o(1)),
Gaussian quotient norm=B^(1/4+o(1)).
```

The next exact attack should separate:

1. common-gcd primes of the opposite signed quotient pair that are supported on reconstructed `X*Y`;
2. dual-Cayley common-core divisor allocations after `X*Y` is fixed;
3. X7 same-role/cross-role resultant transfer versus mutually private Gaussian quotient primes.

No one of these may be independently multiplied into the already charged common-core spacing modulus.

---

## 10. H / tH decision

No X8 auxiliary H theorem is needed.

The `2/3` improvement is obtained solely by combining two already merged elementary charged-once estimates with the exact common-core scale pin.  The remaining receiver still has unexhausted gcd/divisor/Gaussian-factorization structure.

```text
X8_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_X8=false.
```

An X-specific H should be reconsidered only if X9 exhausts the exact common-gcd, dual-Cayley divisor, and cross-resultant decompositions and leaves a genuine average theorem.

---

## Stage boundary

```text
STAGE14_X8=COMPLETE_TWO_SIDED_DUAL_CAYLEY_MINIMAX_AND_TWO_THIRDS_PROMOTION
MERGED_X7_IMPORTED=true
MERGED_S7_30_IMPORTED=true
MERGED_4CQ_IMPORTED=true
S7_30_BLOCK_EXPONENT=max(theta+phi+1/8,1-2theta)
S7_30_COMMON_CORE_SCALE_PIN=c=2theta+2phi-3/4
DUAL_CAYLEY_BLOCK_EXPONENT=1/2+2phi-c
DUAL_CAYLEY_BLOCK_EXPONENT_AFTER_SCALE_PIN=5/4-2theta
COMBINED_BLOCK_EXPONENT=min(max(theta+phi+1/8,1-2theta),5/4-2theta)
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=2/3
IMPROVEMENT_OVER_11_16=1/48
CURRENT_GAP_TO_SQRT=1/6
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
TWO_THIRDS_SATURATION_REQUIRES_THETA=7/24
TWO_THIRDS_SATURATION_REQUIRES_PHI=1/4
TWO_THIRDS_SATURATION_COMMON_CORE_EXPONENT=1/3
TWO_THIRDS_SATURATION_URES_EXPONENT=1/12
TWO_THIRDS_SATURATION_VRES_EXPONENT_MAX=1/6
TWO_THIRDS_SATURATION_FIRST_PRIMITIVE_PAIR_EXPONENT=1/6
TWO_THIRDS_SATURATION_OPPOSITE_QUOTIENT_SQRT_EXPONENT=1/12
TWO_THIRDS_SATURATION_GAUSSIAN_QUOTIENT_NORM_EXPONENT=1/4
S7_30_THETA_5_16_BARRIER_SUPERSEDED=true
FOUR_CQ_SYMMETRIC_QUARTER_QUARTER_BARRIER_SUPERSEDED=true
X7_SELF_GENERATED_SPACING_GUARD_RETAINED=true
REMAINING_RECEIVER=Theta7Over24QuarterPhiCommonGcdCayleyGaussianQuotientEnergy
X8_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_X8=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT_RECOMMENDED=Stage14-X9
```
