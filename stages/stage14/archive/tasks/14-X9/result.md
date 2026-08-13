# Stage14-X9 — five-eighths promotion, superseded common-gcd receiver, and exact boundary split

## Status

`COMPLETE_FIVE_EIGHTHS_PROMOTION_AND_UPPER_CORE_LOWER_CORELESS_BOUNDARY_SPLIT`

Stage14-X9 consumes merged `X8`, merged `s7-31`, merged `4cr`, and the Gaussian quotient / cross-resultant dictionary of merged `X7`.

The current whole-family exponent is no longer the `2/3` value recorded by X8/4cr.  Merged s7-31 strengthens the same charged-once common-core packet to

```text
V(B) << B^(5/8+o(1)).
```

by proving that the common gcd of the opposite signed quotient pair is not a free square-root parameter: its odd part squared divides the already-fixed outer quantity `C*u_res`.

X9 performs three cross-route tasks.

1. It promotes the merged `5/8` theorem into the X ledger and explicitly supersedes the old X8/4cr `2/3` barrier.
2. It checks that the `TwoThirdsCayleyGaussianCommonGcdRootProductIncidence` receiver of 4cr is no longer minimal: the common-gcd loss is already eliminated by s7-31 on the whole strip.
3. It separates the two exact `5/8` saturation mechanisms.  The upper boundary has a fixed-power common core and is saturated before the opposite quotient pair contributes any power; the lower boundary has `C=B^o(1)` and is saturated by a genuinely coreless reciprocal two-pair count.

No additional power saving below `5/8` is proved in X9.

---

## 1. Imported balanced strip and the new current theorem

Keep

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Merged s7-31 gives the exact block envelope

```text
boxed:
E_31(theta,phi)
 <= max(2*theta,1-2*theta).                         (1.1)
```

Consequently

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8.         (1.2)
```

The improvement over X8 is

```text
2/3-5/8=1/24.                                       (1.3)
```

The current gap to square-root scale is

```text
5/8-1/2=1/8.                                        (1.4)
```

The former X8 corner

```text
theta=7/24,
phi=1/4
```

is now strictly subcritical:

```text
E_31=max(7/12,5/12)=7/12.                           (1.5)
```

Thus

```text
X8_TWO_THIRDS_SATURATION_SUPERSEDED=true.            (1.6)
```

---

## 2. Why the 4cr common-gcd receiver is superseded

4cr was written before merged s7-31.  At its `2/3` corner it retained

```text
h=gcd(c_k^+,c_k^-),
oddpart(h)|X*Y
```

as a fixed-power boundary and defined

```text
TwoThirdsCayleyGaussianCommonGcdRootProductIncidence.
```

Merged s7-31 proves the stronger outer-data statement

```text
oddpart(h)^2 | C*u_res.                             (2.1)
```

The pair `(C,u_res)` is fixed before the opposite signed quotient pair is counted.  Hence

```text
fixed (C,u_res)
=> #h <= B^o(1),                                   (2.2)
```

and the nonprimitive second-root-pair count sharpens from

```text
B^o(1)*(M^(1/2)+M/C)
```

to

```text
boxed:
B^o(1)*(1+M/C).                                    (2.3)
```

Therefore the common gcd contributes no fixed power anywhere on the merged strip.

```text
FOUR_CR_COMMON_GCD_FIXED_POWER_BOUNDARY_SURVIVES=false
TWO_THIRDS_CAYLEY_GAUSSIAN_COMMON_GCD_ROOT_PRODUCT_RECEIVER_MINIMAL=false.  (2.4)
```

The exact Cayley/Gaussian orientation split of 4cr remains valid structure; only its old minimal receiver is superseded.

---

## 3. Exact five-eighths saturation set

Equation (1.1) reaches `5/8` in exactly two ways.

### 3.1 Upper edge

```text
2*theta=5/8
```

forces

```text
boxed:
theta=5/16.                                        (3.1)
```

The strip then gives

```text
boxed:
3/16 <= phi <= 1/4.                                (3.2)
```

### 3.2 Lower corner

```text
1-2*theta=5/8
```

forces

```text
theta=3/16.
```

The strip conditions `phi<=theta` and `theta+phi>=3/8` then force

```text
boxed:
theta=phi=3/16.                                    (3.3)
```

There are no other `5/8` saturation blocks.

---

## 4. Upper edge ledger: the second quotient pair is already divisor-many

On

```text
theta=5/16,
3/16<=phi<=1/4,
```

use the s7-31 scale variables

```text
chi = 2*theta+2*phi-3/4,
mu  <= 2*theta-2*phi,
nu  <= 1/4+2*phi-2*theta.                          (4.1)
```

Substitution gives

```text
boxed:
chi = 2*phi-1/8,                                   (4.2)
mu  <= 5/8-2*phi,                                  (4.3)
nu  <= 2*phi-3/8.                                  (4.4)
```

The first primitive xi-agreement pair count has exponent

```text
2*phi-chi = 1/8.                                   (4.5)
```

The sharpened opposite signed quotient exponent is

```text
max(0,nu-chi)
 <= max(0,(2phi-3/8)-(2phi-1/8))
 =0.                                                (4.6)
```

Thus the opposite signed quotient pair contributes only `B^o(1)` on the entire upper edge.

The whole `5/8` exponent is exactly

```text
chi + mu + 1/8
 <= (2phi-1/8)+(5/8-2phi)+1/8
 =5/8.                                              (4.7)
```

Moreover

```text
boxed:
chi+mu=1/2.                                         (4.8)
```

Equivalently, the outer residual norm

```text
q_k=C*u_res
```

has exponent `1/2` all along the upper edge.

This is the first exact X9 boundary mechanism:

```text
upper edge = outer common-residual mass B^(1/2)
             x first primitive root-line fiber B^(1/8)
             x B^o(1) completion.                  (4.9)
```

Define

```text
UpperFiveEighthsCommonResidualPrimitiveRootLineEnergy. (4.10)
```

---

## 5. 4cr Cayley/Gaussian split on the upper edge

Merged 4cr decomposes the good common core

```text
C_*=C/C_bad
```

as

```text
C_+*C_-=C_*,
gcd(C_+,C_-)=1,                                    (5.1)
```

where

- `C_+` is the same-Gaussian-orientation support;
- `C_-` is the opposite-Gaussian-orientation support.

For Gaussian divisors

```text
N(Pi_+)=C_+,
N(Pi_-)=C_-,
```

4cr gives

```text
Pi_+*Pi_-       | Z_k,
Pi_+*conj(Pi_-) | Z_xi.                            (5.2)
```

At least one sign component satisfies

```text
max(C_+,C_-) >= C_*^(1/2).                         (5.3)
```

On the upper edge the common-core exponent ranges

```text
1/4 <= chi <= 3/8,                                 (5.4)
```

so the dominant Gaussian orientation component has exponent at least

```text
chi/2 in [1/8,3/16]                                (5.5)
```

up to the already-controlled bad peel.

This is useful structure for the next stage, but it is not an additional determinant modulus.  `C_+` and `C_-` partition the same common core already charged in (4.7).

```text
UPPER_EDGE_CAYLEY_ORIENTATION_SPLIT_AVAILABLE=true
UPPER_EDGE_CAYLEY_SPLIT_GIVES_EXTRA_SPACING_BY_ITSELF=false.    (5.6)
```

Hence the upper receiver should retain the large same/opposite Gaussian orientation tag, but no power saving is claimed from the tag alone.

A sharpened upper receiver is

```text
UpperFiveEighthsCayleyGaussianCommonResidualPrimitiveRootLineEnergy. (5.7)
```

---

## 6. Lower corner ledger: the common core disappears

At

```text
theta=phi=3/16,
```

the same scale formulas give

```text
boxed:
chi=0,
mu=0,
nu=1/4.                                            (6.1)
```

Therefore

```text
C=B^o(1),
u_res=B^o(1),                            (6.2)
```

and the first primitive pair has exponent

```text
2*phi-chi=3/8.                                     (6.3)
```

The second quotient pair contributes

```text
max(0,nu-chi)=1/4.                                 (6.4)
```

Hence

```text
3/8+1/4=5/8.                                       (6.5)
```

The common-gcd square-divisibility is especially strong here:

```text
oddpart(h)^2 | C*u_res=B^o(1),                     (6.6)
```

so not only the number of possible `h`, but the size of its odd part is `B^o(1)`.

Thus the lower saturation has nothing to do with a large common gcd or a large common core.

```text
LOWER_CORNER_COMMON_CORE_FIXED_POWER=false
LOWER_CORNER_COMMON_GCD_FIXED_POWER=false.          (6.7)
```

The lower `5/8` loss is exactly a coreless reciprocal two-pair density:

```text
first primitive pair:      B^(3/8)
opposite quotient pair:    B^(1/4)
remaining completion:      B^o(1).                 (6.8)
```

Define

```text
LowerFiveEighthsCorelessReciprocalPrimitivePairEnergy. (6.9)
```

---

## 7. Lower corner four-root balance

Merged X6/X7 provide

```text
F_- = a^2 U^2-b^2 V^2,
F_+ = a^2 U^2+b^2 V^2,
```

with the real and Gaussian/twisted prime allocations interpreted as self-generated value factorizations rather than outer spacing moduli.

At the lower corner

```text
alpha*delta = B^(2theta+o(1)) = B^(3/8+o(1)),
S*T         = B^(3/4-2phi+o(1)) = B^(3/8+o(1)),
U*V         = B^(2phi+o(1)) = B^(3/8+o(1)).        (7.1)
```

Since `C=B^o(1)`, the good part of the plus value has the same exponent scale as the switched xi kernel:

```text
oddpart(F_+) = B^(3/8+o(1)).                       (7.2)
```

Likewise the agreement part of `F_-` is `B^(3/8+o(1))` after endpoint-small factors.

Thus the lower receiver contains a balanced triad

```text
U*V,
real difference-value kernel,
Gaussian plus-value kernel
```

all at exponent `3/8`.

This structure is genuine, but X7 already proves that these generated kernels cannot simply be multiplied into a new deterministic spacing modulus.

```text
LOWER_CORNER_BALANCED_REAL_GAUSSIAN_VALUE_TRIAD=true
LOWER_CORNER_SELF_GENERATED_MODULI_RECHARGED=false.  (7.3)
```

A more descriptive lower receiver is

```text
LowerFiveEighthsCorelessReciprocalFourRootPairEnergy. (7.4)
```

---

## 8. X7 cross-resultants and why they do not close X9 automatically

For two primitive first-pair points X7 defines

```text
R_12=U_1^2 V_2^2-U_2^2 V_1^2,
K_12=U_1^2 V_2^2+U_2^2 V_1^2.                     (8.1)
```

A generated prime transfers between the two points exactly through the corresponding same-role or cross-role resultant.

This remains relevant to both X9 receivers.  However X7 also proves that a generated prime which is private to one point does not force cross spacing.  Therefore no unconditional saving follows merely from the existence of the balanced real/Gaussian kernels on the lower corner or from the Cayley orientation split on the upper edge.

```text
X7_CROSS_RESULTANT_DICTIONARY_RETAINED=true
PRIVATE_GENERATED_PRIME_AUTOMATIC_CROSS_SPACING=false. (8.2)
```

The next X stage must therefore work with pair energy / shared-resultant structure, not a second pointwise CRT charge.

---

## 9. Current minimal X receivers

The merged `5/8` theorem has two inequivalent saturation mechanisms and should no longer be represented by one homogeneous receiver.

### Upper receiver

```text
UpperFiveEighthsCayleyGaussianCommonResidualPrimitiveRootLineEnergy
```

with

```text
theta=5/16,
3/16<=phi<=1/4,
C=B^(2phi-1/8+o(1)),
u_res=B^(5/8-2phi+o(1)),
C*u_res=B^(1/2+o(1)),
# first primitive pair=B^(1/8+o(1)),
# opposite quotient pair=B^o(1),
C_+C_-=C_*,
max(C_+,C_-)>=C_*^(1/2),
```

plus all original reconstruction and X7 cross-resultant masks.

### Lower receiver

```text
LowerFiveEighthsCorelessReciprocalFourRootPairEnergy
```

with

```text
theta=phi=3/16,
C=B^o(1),
u_res=B^o(1),
# first primitive pair=B^(3/8+o(1)),
# opposite quotient pair=B^(1/4+o(1)),
U*V~agreement kernel~Gaussian plus kernel~B^(3/8+o(1)),
```

again retaining the physical reciprocal reconstruction and X7 shared-resultant/private-prime distinction.

The umbrella receiver is

```text
FiveEighthsSeparatedUpperCayleyLowerCorelessReciprocalEnergy.   (9.1)
```

---

## 10. H / tH decision

X9 introduces no external theorem and no new average estimate.  It only imports merged s7-31, removes the stale 4cr common-gcd receiver, and separates the two exact boundary mechanisms.

The upper edge still contains unused exact Cayley/Gaussian divisor structure.  The lower corner still contains an exact balanced real/Gaussian value decomposition and reciprocal reconstruction.  Those internal structures should be exhausted before requesting an X-specific average theorem.

The fixed-U t/tH line remains a different coefficient space and is not cross-promoted.

```text
X9_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
TH19_CROSS_PROMOTED_TO_X9=false.                    (10.1)
```

If X10 reduces either boundary to a genuine pair-energy theorem, the H target should be named separately for the upper or lower receiver rather than returning to a generic genus-one object.

---

## Stage boundary

```text
STAGE14_X9=COMPLETE_FIVE_EIGHTHS_PROMOTION_AND_UPPER_CORE_LOWER_CORELESS_BOUNDARY_SPLIT
MERGED_X8_IMPORTED=true
MERGED_S7_31_IMPORTED=true
MERGED_4CR_IMPORTED=true
MERGED_X7_CROSS_RESULTANT_IMPORTED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
IMPROVEMENT_OVER_X8_TWO_THIRDS=1/24
CURRENT_GAP_TO_SQRT=1/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
X9_PROVES_ADDITIONAL_SAVING_BELOW_MERGED_5_8=false
X8_TWO_THIRDS_SATURATION_SUPERSEDED=true
X8_FORMER_CORNER_EXPONENT_UNDER_S7_31=7/12
FOUR_CR_COMMON_GCD_FIXED_POWER_BOUNDARY_SURVIVES=false
TWO_THIRDS_CAYLEY_GAUSSIAN_COMMON_GCD_ROOT_PRODUCT_RECEIVER_MINIMAL=false
FIVE_EIGHTHS_UPPER_EDGE_THETA=5/16
FIVE_EIGHTHS_UPPER_EDGE_PHI_RANGE=[3/16,1/4]
FIVE_EIGHTHS_LOWER_CORNER=(theta,phi)=(3/16,3/16)
UPPER_EDGE_COMMON_CORE_EXPONENT=2phi-1/8
UPPER_EDGE_URES_EXPONENT=5/8-2phi
UPPER_EDGE_C_URES_EXPONENT=1/2
UPPER_EDGE_FIRST_PRIMITIVE_PAIR_EXPONENT=1/8
UPPER_EDGE_OPPOSITE_QUOTIENT_PAIR_EXPONENT=0
UPPER_EDGE_CAYLEY_ORIENTATION_SPLIT_AVAILABLE=true
UPPER_EDGE_CAYLEY_SPLIT_GIVES_EXTRA_SPACING_BY_ITSELF=false
LOWER_CORNER_COMMON_CORE_EXPONENT=0
LOWER_CORNER_URES_EXPONENT=0
LOWER_CORNER_FIRST_PRIMITIVE_PAIR_EXPONENT=3/8
LOWER_CORNER_OPPOSITE_QUOTIENT_PAIR_EXPONENT=1/4
LOWER_CORNER_COMMON_GCD_FIXED_POWER=false
LOWER_CORNER_BALANCED_REAL_GAUSSIAN_VALUE_TRIAD=true
LOWER_CORNER_SELF_GENERATED_MODULI_RECHARGED=false
UPPER_RECEIVER=UpperFiveEighthsCayleyGaussianCommonResidualPrimitiveRootLineEnergy
LOWER_RECEIVER=LowerFiveEighthsCorelessReciprocalFourRootPairEnergy
REMAINING_RECEIVER=FiveEighthsSeparatedUpperCayleyLowerCorelessReciprocalEnergy
X9_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT_RECOMMENDED=Stage14-X10
```
