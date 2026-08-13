# Stage14-4bo — normalized-core compression and moving-good-product receiver

## Purpose

Merged Stage14-4bn identifies physical ordered edges exactly with B-admissible positive cross-square pairs `(F2,F3)`, and merged Stage14-s6-10 closes the old fixed-fiber s6 method at the active-direction barrier.

Merged Stage14-4bm has already removed two sectors:

```text
X2 <= B^(20/21)              -> B^(20/21+o(1)),
X2_cross >= B^(4/21)         -> B^(61/63+o(1)).
```

Thus the only unresolved main-track edges satisfy

```text
X2 > B^(20/21),
X2_cross < B^(4/21),
```

and carry the four pairwise-coprime good gcd cells from merged s6-07/s6-08.

This stage does not reopen the closed s6 fixed-direction analysis.  Instead it compresses the remaining active-edge arithmetic into:

1. a small normalized core `(a0,b0,c0,d0)` of total counting exponent at most `3/7`; and
2. one moving scalar
   `Q = q-- q-+ q+- q++ = X2_good`,
   with only subpolynomially many four-cell allocations for each fixed `Q`.

The result is an exact new receiver for the main track: all remaining fixed-power difficulty is the average occupancy of the one-dimensional moving-`Q` fibers over the small normalized cores.

No external theorem is used.

---

## 1. Merged inputs

We use only merged results.

### 1.1 Exact physical pair model from 4bn

A physical ordered edge is equivalent to a B-admissible pair of primitive Pythagorean faces

```text
F2=(S2,X2,H2),
F3=(S3,X3,H3)
```

with positive cross square

```text
(S3*X2)^2-(X3*S2)^2 = square > 0
```

and exact reconstructed cutoff

```text
gcd(H,X2)*H3 <= B.
```

In particular `H2,H3<=B`, hence `X2,X3<=B`.

### 1.2 Half-angle variables and the good gcd matrix

Write

```text
H2-S2 = kappa2*a^2,
H2+S2 = kappa2*b^2,
X2     = kappa2*a*b,

H3-S3 = kappa3*c^2,
H3+S3 = kappa3*d^2,
X3     = kappa3*c*d,
```

with `kappa2,kappa3 in {1,2}`.

Merged s6-07 gives four pairwise-coprime good cells

```text
q11=q--,
q12=q-+,
q21=q+-,
q22=q++
```

such that

```text
Q := q11*q12*q21*q22 = X2_good,
X2 = X2_cross * Q.
```

Merged s6-08 gives the exact decomposition

```text
a = q11*q12*a0,
b = q21*q22*b0,
c = q11*q21*c0,
d = q12*q22*d0.
```

---

## 2. The F2 normalized core is exactly the cross part

Multiply the first two decompositions:

```text
a*b = Q*a0*b0.
```

Since `X2=kappa2*a*b` and `X2=X2_cross*Q`, cancellation of `Q` gives the exact identity

```text
boxed:
kappa2*a0*b0 = X2_cross.                     (BO.1)
```

Therefore every unresolved 4bm edge satisfies

```text
boxed:
a0*b0 < B^(4/21).                            (BO.2)
```

This is stronger than a generic size estimate: the normalized F2 core product is exactly the old cross-prime/2-primary factor up to the fixed `kappa2`.

We record

```text
F2_NORMALIZED_CORE_PRODUCT_EXACT=X2_cross/kappa2
F2_NORMALIZED_CORE_PRODUCT_EXPONENT_LT=4/21.
```

---

## 3. The F3 normalized core has exponent at most 5/21

Likewise

```text
c*d = Q*c0*d0.
```

Since `X3=kappa3*c*d`,

```text
boxed:
kappa3*c0*d0 = X3/Q.                         (BO.3)
```

On the unresolved family,

```text
X2 > B^(20/21),
X2_cross < B^(4/21),
```

so

```text
Q=X2/X2_cross > B^(16/21).                    (BO.4)
```

Because `X3<=B`, (BO.3) and (BO.4) imply

```text
boxed:
c0*d0 < B^(5/21).                            (BO.5)
```

Thus both normalized half-angle pairs are genuinely small even though the original directions may have height `B`.

```text
GOOD_PRODUCT_EXPONENT_GT=16/21
F3_NORMALIZED_CORE_PRODUCT_EXPONENT_LT=5/21.
```

---

## 4. The normalized core family has exponent at most 3/7

Let

```text
C=(a0,b0,c0,d0).
```

The elementary divisor-hyperbola estimate

```text
#{(u,v) in Z_{>0}^2: u*v<=Y} << Y*log(2Y)
```

gives

```text
#{(a0,b0): a0*b0 < B^(4/21)}
  << B^(4/21+o(1)),

#{(c0,d0): c0*d0 < B^(5/21)}
  << B^(5/21+o(1)).
```

Hence the number of possible normalized cores is

```text
boxed:
#C(B) << B^(9/21+o(1)) = B^(3/7+o(1)).       (BO.6)
```

Since

```text
3/7 = 1/2 - 1/14,
```

the normalized core itself already lies strictly below square-root scale.

This does **not** prove a square-root bound for physical edges: the moving good product `Q` remains.

```text
NORMALIZED_CORE_COUNT_EXPONENT=3/7
NORMALIZED_CORE_BELOW_SQRT_BY=1/14.
```

---

## 5. For fixed Q, the four-cell allocation costs only B^o(1)

Every good prime power of `Q` belongs to exactly one of the four pairwise-coprime cells `q11,q12,q21,q22`.

Therefore, for fixed `Q`, the number of possible cell allocations is at most

```text
4^omega(Q).
```

By the divisor bound,

```text
4^omega(Q) <= tau(Q)^2 = Q^o(1) = B^o(1).
```

After fixing

```text
(C,Q,cell allocation,kappa2,kappa3),
```

the four original half-angle variables `a,b,c,d`, hence the pair `(F2,F3)`, are determined.  Physical cross-square and the sharp 4bn cutoff are then predicates, not additional multiplicities.

Thus at power scale the four large gcd cells do not form four independent moving dimensions.  They form one moving scalar `Q` plus subpolynomial divisor-allocation data.

```text
FIXED_Q_GOOD_CELL_ALLOCATION_MULTIPLICITY=B^o(1)
FOUR_GCD_CELLS_POWER_SCALE_DIMENSION=ONE_MOVING_Q.
```

---

## 6. Exact normalized square receiver over (C,Q)

Merged s6-08 gives, after extracting the automatic `Q^2` square factor,

```text
F=(q12^2*a0*d0)^2-(q21^2*b0*c0)^2,
G=(q22^2*b0*d0)^2-(q11^2*a0*c0)^2,
ker(F)=ker(G).
```

For fixed `(C,Q)`, only `B^o(1)` allocations of the prime powers of `Q` into the four coefficients are possible.  Therefore the remaining active-edge problem is exactly a moving-`Q` squareclass/kernel occupancy problem over a `B^(3/7+o(1))` family of small cores.

Define

```text
M_C(B)
 = # {Q:
      some four-cell allocation of Q
      gives a B-admissible physical pair
      with normalized core C}.
```

Then

```text
boxed:
E_res(B)
 << B^o(1) * sum_C M_C(B).                  (BO.7)
```

No coordinate-density-to-existence multiplication occurs: `(C,Q,allocation)` reconstructs the actual physical pair.

---

## 7. Exponent transfer ledger for the moving-Q fibers

A convenient sufficient form is a uniform average-scale estimate

```text
M_C(B) << B^(mu+o(1))
```

for every admissible core `C`.  Combining with (BO.6)-(BO.7) gives

```text
E_res(B) << B^(3/7 + mu + o(1)).            (BO.8)
```

Therefore:

### Any new whole-family improvement

To beat the current `41/42`, it is enough to prove

```text
mu < 41/42 - 3/7 = 23/42.                  (BO.9)
```

### Reach the already-closed cross-sector ceiling

To reduce the active residual to at most the 4bm cross bound `61/63`, it is enough to prove

```text
mu <= 61/63 - 3/7 = 34/63.                 (BO.10)
```

The gap between the two thresholds is exactly

```text
23/42 - 34/63 = 1/126,
```

matching the s6-10 active-direction saving needed to reach the cross-sector ceiling.

### Reach square-root scale on this residual

For the residual family itself to be `B^(1/2+o(1))`, it would suffice to prove the much stronger

```text
mu <= 1/2 - 3/7 = 1/14.                    (BO.11)
```

No bound of (BO.9), (BO.10), or (BO.11) is proved here.  These are exact transfer thresholds for the newly isolated scalar fiber.

---

## 8. Relation to s6-10 and t37

Merged s6-10 correctly closes the old fixed-direction method: once one fixes `F2`, partner multiplicity is already `B^o(1)`, so improving that fiber cannot make inactive directions appear.

Stage14-4bo does not reopen that method.  It changes coordinates on the **moving active family** and shows that the edge-relative good gcd matrix has only one power-scale moving quantity after normalization.

Merged t37 independently proves a fixed-canonical-prime power saving and leaves a moving-prime summation problem.  This is methodologically suggestive, but 4bo does **not** identify t37's canonical Gaussian prime with the largest prime factor of the present `Q`.  That identification would require a separate exact transfer and is not assumed.

The safe next step is to factor the moving `Q` by a canonical largest rational prime/power and derive the exact physical congruence or spin packet before importing any t-route estimate.

---

## 9. Quantitative status

The current unconditional whole-family bound remains

```text
V(B) << B^(41/42+epsilon).
```

Already-proved sectoral bounds remain

```text
X2<=B^(20/21)      -> B^(20/21+o(1)),
X2_cross>=B^(4/21) -> B^(61/63+o(1)).
```

For the only unresolved sector, 4bo proves the exact compression

```text
normalized core count <= B^(3/7+o(1)),
fixed-Q cell allocations = B^o(1),
remaining power-scale variable = moving Q=X2_good.
```

This is a structural reduction, not yet a new full-family exponent.

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false.
```

---

## Boundary

```text
STAGE14_4BO=NORMALIZED_CORE_COMPRESSION_AND_MOVING_GOOD_PRODUCT_RECEIVER
MERGED_4BN_PHYSICAL_PAIR_BIJECTION_IMPORTED=true
MERGED_S6_10_METHOD_CLOSURE_RESPECTED=true
MERGED_4BM_RESIDUAL_IMPORTED=true
F2_NORMALIZED_CORE_PRODUCT_EXACT=X2_cross/kappa2
F2_NORMALIZED_CORE_PRODUCT_EXPONENT_LT=4/21
GOOD_PRODUCT_EXPONENT_GT=16/21
F3_NORMALIZED_CORE_PRODUCT_EXPONENT_LT=5/21
NORMALIZED_CORE_COUNT_EXPONENT=3/7
NORMALIZED_CORE_BELOW_SQRT_BY=1/14
FIXED_Q_GOOD_CELL_ALLOCATION_MULTIPLICITY=B^o(1)
FOUR_GCD_CELLS_POWER_SCALE_DIMENSION=ONE_MOVING_Q
MOVING_Q_FIBER_RECEIVER_DEFINED=true
MOVING_Q_EXPONENT_FOR_ANY_WHOLE_FAMILY_IMPROVEMENT=23/42
MOVING_Q_EXPONENT_TO_REACH_CROSS_CEILING=34/63
MOVING_Q_EXPONENT_FOR_SQRT_RESIDUAL=1/14
T37_CANONICAL_PRIME_IDENTIFIED_WITH_Q_LARGEST_PRIME=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
NEXT=Stage14-4bp
```

## Next

`Stage14-4bp`: canonical-largest-prime decomposition of the moving good product `Q`, with exact congruence/spin transfer on the normalized core.  The goal is to prove a genuine average bound for `M_C(B)` rather than another fixed-direction point-count theorem.