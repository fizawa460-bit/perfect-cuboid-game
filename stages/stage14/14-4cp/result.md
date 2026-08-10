# Stage14-4cp — promote the common-core primitive root-line bound to the mainline

## Status

`COMPLETE_THREE_QUARTER_PROMOTION_SINGULAR_ELIMINATION_AND_QUARTER_PHI_ROOTLINE_REDUCTION`

Stage14-4cp consumes merged `14-4co`, merged `14-s7-29`, and merged `14-X6`.

The decisive change is that the old `7/8` top-edge receiver is no longer the current mainline obstruction.  Merged s7-29 proves an unconditional charged-once bound

```text
V(B) << B^(3/4+o(1)),
```

while merged X6 proves that the only singular reciprocal-Edwards specialization `lambda=4` is asymptotically empty on the top-theta physical packet.

Thus Stage14-4cp promotes `3/4` to the mainline exponent and freezes the unique new saturation edge.

---

## 1. Imported primitive agreement coordinates

Use the merged s7-28/s7-29 primitive xi-agreement pair

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,

D+A=aU,
D-A=bV,
```

where the full signed quotient decoration `(a,b,...)` is divisor-many once residual/root data are fixed.

Then

```text
H_k^+=(a^2 U^2+b^2 V^2)/2.
```

Merged 4cg/s7-29 give the common-core divisibility

```text
C | a^2 U^2+b^2 V^2,
gcd(C,UV)=1
```

after peeling only a `B^o(1)` bad coefficient factor.  For the good part `C_0=C/B^o(1)`, every prime power `p^e||C_0` imposes

```text
(a_0 U/(b_0 V))^2 == -1 (mod p^e).
```

Hence all good common-core primes are `1 mod 4`, with two roots per prime power and only

```text
2^omega(C_0)=B^o(1)
```

CRT root lines.

---

## 2. Primitive determinant spacing

Fix one CRT root line

```text
U == rho V (mod C_0).
```

For two distinct primitive points `(U_1,V_1),(U_2,V_2)` on the same root line,

```text
U_1 V_2-U_2 V_1
```

is a nonzero multiple of `C_0`.  The standard slope-spacing argument therefore gives, in a dyadic box,

```text
# {(U,V)} <= 1 + 6 U_0 V_0/C_0.
```

Since

```text
UV=oddpart(RJ)=B^(2 phi+o(1)),
C=B^(c+o(1)),
```

we obtain

```text
# {(U,V) : fixed residual/quotient data}
 <= B^(2 phi-c+o(1)).                         (2.1)
```

This is a charged-once primitive-pair count; `S*T` is reconstructed later and is not charged independently.

---

## 3. Exact cancellation of the common-core exponent

Merged 4cg gives

```text
u_res v_res <= B^(1/4+o(1)).
```

For `C~B^c`, the residual/common-core support contributes

```text
B^(c+1/4+o(1)).
```

Multiplying by (2.1), the exponent `c` cancels exactly:

```text
B^(c+1/4) B^(2 phi-c)
 = B^(2 phi+1/4+o(1)).                      (3.1)
```

As `phi<=1/4`, every physical block satisfies

```text
boxed:
V(B) << B^(3/4+o(1)).                       (3.2)
```

Therefore

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4
IMPROVEMENT_OVER_PREVIOUS_7_8=1/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

This promotion is unconditional within the merged Stage14 theorem chain; no genus-one H theorem is used.

---

## 4. The new saturation edge is only phi=1/4

Equation (3.1) is sharper away from the quarter-phi edge.  If

```text
phi <= 1/4-eta,
```

then

```text
2 phi+1/4 <= 3/4-2 eta.
```

Hence a block can saturate the new `3/4` bound only when

```text
boxed:
theta=5/16,
phi=1/4.                                      (4.1)
```

The previous interval

```text
theta=5/16,
3/16<=phi<=1/4
```

is no longer a barrier interval; only its right endpoint survives.

```text
THREE_QUARTER_SATURATION_REQUIRES_PHI=1/4=true.
```

---

## 5. The lambda=4 singular branch is physically empty

Merged X6 returns the singular relation from 4cn/4co to the common-core plus identity and proves exactly

```text
(g1*g2)(beta*gamma)(D+A)^2 = 4(S*T)Q^2,
(g1*g2)(beta*gamma)(D-A)^2 = 4(S*T)P^2.
```

The factors `g1*g2` and `4` are 2-primary, while the odd squarefree kernels of `beta*gamma` and `S*T` are coprime.  Odd valuation parity forces

```text
oddpart(beta*gamma)=1,
oddpart(S*T)=1.
```

But on the top-theta packet

```text
beta*gamma=B^(3/8+o(1)),
S*T>=B^(1/4-o(1)).
```

Thus

```text
boxed:
TOP_THETA_LAMBDA4_SINGULAR_BRANCH_EMPTY=true.       (5.1)
```

The squareclass locks proved in 4co remain valid necessary identities for the formal singular specialization, but no asymptotic physical top-edge packet reaches that specialization.  Consequently the singular receiver is removed rather than carried into the new `3/4` barrier.

---

## 6. Four-root quadratic-value masks on the surviving smooth packet

Merged X6 also gives, for the same primitive pair,

```text
F_- = a^2 U^2-b^2 V^2
    = 4 r s epsilon_k * oddpart(alpha*delta),

F_+ = a^2 U^2+b^2 V^2
    = 2 H_k^+,
```

and

```text
gcd(F_-,F_+) | 2 a^2 b^2.
```

Outside the fixed bad support `2abrsC`, moving odd kernels are disjoint.  Primewise:

```text
good k-agreement prime p:
  U/V == +/- b/a (mod p),
  v_p(F_-)=1,

good xi-switch prime q:
  U/V == +/- i b/a (mod q),
  q == 1 (mod 4).
```

So the surviving quarter-phi packets carry four local root orientations: two real roots for the difference value and two Gaussian/twisted roots for the plus value.

---

## 7. Quantifier guard: self-generated moduli cannot be charged as new spacing

The agreement product `alpha*delta` is reconstructed from `F_-`; the switch product `S*T` is reconstructed from the plus/common-core host.  Therefore their good-prime root congruences are **self-generated quadratic-value masks** of `(U,V)`.

They are not independent ambient moduli that may be multiplied with `C_0` to claim a stronger determinant spacing.  Doing so would count the same quadratic value twice.

The common-core modulus `C_0` is different: it belongs to the residual/common-core outer data and is fixed before the primitive pair is counted.  That is precisely why the s7-29 spacing argument is legal.

Thus

```text
SELF_GENERATED_FOUR_ROOT_MODULI_CHARGED_AS_INDEPENDENT_SPACING=false
ADDITIONAL_POWER_SAVING_FROM_FOUR_ROOT_CRT_ALONE=false.
```

The four-root masks may still reduce the average number of primitive points on a common-core root line, but that requires a genuine distribution argument rather than a second deterministic modulus charge.

---

## 8. New minimal receiver after the 3/4 promotion

Only the quarter-phi corner (4.1) can saturate.  The minimal mainline receiver is therefore

```text
QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy.
```

It counts primitive pairs `(U,V)` with

```text
UV=B^(1/2+o(1)),
U == rho V (mod C_0),
```

where `rho` is one of divisor-many square roots of `-1` after coefficient normalization, subject simultaneously to

- the real two-root squarefree factorization of `F_-` into the legal k-agreement cells;
- the twisted/Gaussian two-root squarefree factorization of the good part of `F_+` into the legal xi-switch cells and common-core support;
- original dyadic, coprimality, reconstruction, orientation and charged-once masks.

The current `3/4` proof ignores most of these self-generated masks.  Any improvement below `3/4` must exploit their distribution along the fixed common-core primitive root lines without double charging.

---

## 9. H / tH decision

The completed `PhysicalReciprocalEdwardsGenusOneAverageIncidence` H audit is no longer the mainline target, and X6 independently shows the singular specialization is empty.

The new barrier is an arithmetic primitive-root-line energy, not a generic genus-one point count.  No additional mainline H request is justified before exact prime-allocation/spacing analysis of the quarter-phi receiver.

The fixed-U t/tH18 route remains a different coefficient space and is not cross-promoted.

```text
MAINLINE_H_AUDIT_COMPLETE=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## Stage boundary

```text
STAGE14_4CP=COMPLETE_THREE_QUARTER_PROMOTION_SINGULAR_ELIMINATION_AND_QUARTER_PHI_ROOTLINE_REDUCTION
MERGED_4CO_IMPORTED=true
MERGED_S7_29_IMPORTED=true
MERGED_X6_IMPORTED=true
COMMON_CORE_GAUSSIAN_ROOT_LINE_REDUCTION_PROVED=true
PRIMITIVE_ROOT_LINE_DETERMINANT_SPACING_PROVED=true
FIXED_C_RESIDUAL_SUPPORT_EXPONENT=c+1/4
FIXED_C_PRIMITIVE_PAIR_EXPONENT=2phi-c
BLOCK_EXPONENT_AFTER_COMMON_CORE_CANCELLATION=2phi+1/4
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4
IMPROVEMENT_OVER_PREVIOUS_7_8=1/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
THREE_QUARTER_SATURATION_REQUIRES_THETA=5/16
THREE_QUARTER_SATURATION_REQUIRES_PHI=1/4
TOP_THETA_LAMBDA4_SINGULAR_BRANCH_EMPTY=true
TOP_THETA_CAYLEY_SINGULAR_RECEIVER_REMOVED=true
PRIMITIVE_FOUR_ROOT_QUADRATIC_VALUE_MASKS_PROVED=true
SELF_GENERATED_FOUR_ROOT_MODULI_CHARGED_AS_INDEPENDENT_SPACING=false
ADDITIONAL_POWER_SAVING_FROM_FOUR_ROOT_CRT_ALONE=false
REMAINING_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy
QUARTER_PHI_COMMON_CORE_PRIMITIVE_FOUR_ROOT_QUADRATIC_VALUE_ENERGY_PROVED=false
PHYSICAL_RECIPROCAL_EDWARDS_GENUS_ONE_H_AUDIT=COMPLETE
GENERIC_GENUS_ONE_RECEIVER_IS_MINIMAL=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cq
```
