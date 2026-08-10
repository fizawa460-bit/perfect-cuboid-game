# Stage14-4ct — top-corner residual-host gcd peel and primitive Gaussian common-core lift

## Status

`COMPLETE_TOP_CORNER_RESIDUAL_HOST_GCD_PEEL_AND_PRIMITIVE_GAUSSIAN_COMMON_CORE_LIFT`

Stage14-4ct consumes merged `14-4cs` and merged `14-s7-32` on the same physical collision family.

Merged `s7-32` keeps the unconditional whole-family estimate

```text
V(B) << B^(5/8+o(1))
```

but proves that equality can occur only at the unique dyadic corner

```text
theta=5/16,
phi=1/4.
```

Thus the lower `theta=phi=3/16` receiver of 4cs is superseded.  The purpose of 4ct is to analyze the remaining xi-switched Gaussian residual host at this unique top corner.

No exponent below `5/8` is promoted in this stage.  The new theorem proves that every fixed-power coordinate gcd of the residual host already gives a fixed-power saving.  Therefore the only possible `5/8` saturation branch is the branch where the residual host is primitive up to `B^o(1)` and essentially the whole common core lifts as a canonical Gaussian divisor of the residual host.

---

## 1. Unique top-corner data

At the only surviving `5/8` corner,

```text
theta=5/16,
phi=1/4,
```

merged `s7-30/31/32` give

```text
C = B^(3/8+o(1)),
u_res <= B^(1/8+o(1)),
v_res <= B^(1/8+o(1)),
q_xi = C*v_res <= B^(1/2+o(1)).
```

Use the xi-switched Gaussian descent

```text
Z_S = lambda_S^2 W_S,
N(lambda_S)=oddpart(S)=B^(1/8+o(1)),
N(W_S)=q_xi * O_2(1).
```

Fix the finite 2-primary convention once and take odd parts.  Put

```text
v := oddpart(v_res),
W_S=A+iB,
g := oddpart(gcd(A,B)).
```

Then exactly

```text
oddpart(N(W_S)) = C*v.                              (1.1)
```

The xi one-host reconstruction theorem of merged `s7-32` says that fixed `(W_S,lambda_S)` together with the finite endpoint/orientation decoration has only `B^o(1)` physical lifts.  Hence it is legal to count the canonical factorization of `W_S` directly.

---

## 2. Canonical common-core gcd peel

Write

```text
W_S = g W_0,
```

where the integer coordinates of `W_0` have odd gcd one.  Define

```text
C_bad  := gcd(C,g^2),
C_good := C/C_bad,
d       := g^2/C_bad.                              (2.1)
```

Both `C_bad` and `d` are positive odd integers, with

```text
C_bad | g^2,
d | g^2.                                           (2.2)
```

Taking odd norms in (1.1) gives

```text
C*v = g^2 * oddpart(N(W_0)).                       (2.3)
```

Prime-by-prime, after removing the common coordinate gcd, the remaining exponent of every prime-power of `C` is still present in `N(W_0)`.  Equivalently,

```text
boxed:
C_good | oddpart(N(W_0)).                          (2.4)
```

Substitute

```text
C=C_bad*C_good,
g^2=C_bad*d
```

into (2.3), then cancel `C_bad`.  Using (2.4) yields the exact factorization

```text
boxed:
d | v,                                             (2.5)

oddpart(N(W_0))/C_good = v/d.                      (2.6)
```

Thus the coordinate gcd does not introduce a new free parameter.  Its excess square factor

```text
d=g^2/C_bad
```

is a divisor of the already-small reduced residual `v`.

---

## 3. Primitive Gaussian lift of the good common core

Because `W_0` has odd-coprime coordinates, an odd prime `p == 3 (mod 4)` cannot divide `N(W_0)`.  Therefore every odd prime dividing `C_good` satisfies

```text
p == 1 (mod 4).                                    (3.1)
```

Let `p^e || C_good` and write `p=pi*bar(pi)` in `Z[i]`.  Since the coordinates of `W_0` are not both divisible by `p`, exactly one of `pi^e` and `bar(pi)^e` divides `W_0`.  Multiplying these forced local orientations gives a Gaussian integer `Pi_C`, unique up to a Gaussian unit, such that

```text
boxed:
N(Pi_C)=C_good,
Pi_C | W_0.                                        (3.2)
```

Hence there is a canonical residual Gaussian quotient `T_C` with

```text
boxed:
W_S = g * Pi_C * T_C,                              (3.3)

oddpart(N(T_C)) = v/d.                             (3.4)
```

This is an integral Gaussian factorization, not a density statement.

The previous top-corner receiver treated `C|N(W_S)` only at norm level.  Stage14-4ct upgrades the good part of `C` to an actual oriented Gaussian divisor of the residual host.

---

## 4. Charged-once gcd-stratified host count

Dyadically write

```text
g      = B^(rho+o(1)),
d      = B^(sigma+o(1)),
C_good = B^(delta+o(1)).
```

Since `C=B^(3/8+o(1))` and `C_bad=g^2/d`,

```text
delta = 3/8 - 2*rho + sigma.                      (4.1)
```

Also `d|v` and `v<=B^(1/8+o(1))`, so

```text
0 <= sigma <= 1/8.                                 (4.2)
```

For fixed `g`, the integer `d` is a divisor of `g^2`, hence there are only `B^o(1)` possibilities for `d`.  Once `g,d,C_good` are fixed, the Gaussian orientation `Pi_C` has only `B^o(1)` possibilities.  By (3.4), the remaining Gaussian quotient has odd norm at most

```text
B^(1/8-sigma+o(1)),
```

so the total number of `T_C` in that norm range is at most

```text
B^(1/8-sigma+o(1)).                                (4.3)
```

The switched square divisor `lambda_S` costs `B^(1/8+o(1))`.  Therefore the xi one-host reconstruction gives the alternative physical block count

```text
E_host(rho,sigma)
 <= 1/8 + rho + delta + (1/8-sigma)
 = 5/8-rho.                                        (4.4)
```

All remaining physical reconstruction is `B^o(1)` by merged `s7-32`.

Hence

```text
boxed:
rho>0
=> E <= 5/8-rho.                                  (4.5)
```

Every fixed-power coordinate gcd of `W_S` is therefore strictly subcritical.

---

## 5. Exact localization of the surviving 5/8 branch

Combine (4.4) with the merged global `5/8` upper bound.  Equality at exponent `5/8` can survive only when

```text
boxed:
g=B^o(1).                                          (5.1)
```

Then automatically

```text
C_bad=B^o(1),
C_good=C/B^o(1)=B^(3/8+o(1)).                      (5.2)
```

Thus essentially the entire physical common core is represented by the canonical Gaussian divisor `Pi_C` in (3.2):

```text
boxed:
N(Pi_C)=B^(3/8+o(1)),
Pi_C | W_0,
oddpart(N(T_C))<=B^(1/8+o(1)).                     (5.3)
```

The old lower-corner factorization receiver is gone, and the old upper-edge continuum has already collapsed by s7-32.  The only remaining fixed-power obstruction is now the simultaneous compatibility of

```text
Z_S=lambda_S^2 * Pi_C * T_C,
N(lambda_S)=B^(1/8+o(1)),
N(Pi_C)=B^(3/8+o(1)),
N(T_C)<=B^(1/8+o(1)),
```

with the primitive xi-agreement root line modulo the same common core `C` and the full reciprocal reconstruction.

Define the new minimal receiver

```text
TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence.   (5.4)
```

This receiver is strictly narrower than the s7-32 receiver because it discards every fixed-power nonprimitive residual-host branch.

---

## 6. Relation to 4cr/4cs and t71

Merged `4cr/4cs` split the physical common core through Cayley same/opposite Gaussian orientations and identify the quotient common gcd with the physical root gcd.  Those results remain compatible with (3.2), but Stage14-4ct does not assert that the Cayley orientation divisor and `Pi_C` are already identical prime-by-prime.  That comparison is the next exact task.

Merged `t71` works in a fixed-`U` Cayley coefficient space.  Its squareclass four-cell transfer is not cross-promoted here because no exact variable/quantifier adapter to the moving top-corner `W_S` factorization has yet been proved.

```text
T71_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 7. H / tH decision

No auxiliary H theorem is needed in 4ct.  The stage is closed by elementary integer gcd decomposition, the two-squares prime theorem, unique Gaussian orientation for a primitive host, and merged one-host reconstruction.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false.
```

If the next exact comparison fails to collapse the receiver, the only appropriate new H target would be a theorem specifically for

```text
TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence,
```

namely an averaged incidence between a large canonical Gaussian divisor `Pi_C` of norm `B^(3/8)`, a square divisor `lambda_S^2` of norm `B^(1/4)`, and the primitive xi-agreement root line modulo the same `C`.  The generic reciprocal genus-one H must not be revived.

---

## Stage boundary

```text
STAGE14_4CT=COMPLETE_TOP_CORNER_RESIDUAL_HOST_GCD_PEEL_AND_PRIMITIVE_GAUSSIAN_COMMON_CORE_LIFT
MERGED_4CS_IMPORTED=true
MERGED_S7_32_IMPORTED=true
UNIQUE_FIVE_EIGHTHS_SATURATION_THETA=5/16
UNIQUE_FIVE_EIGHTHS_SATURATION_PHI=1/4
LOWER_FIVE_EIGHTHS_RECEIVER_SURVIVES=false
RESIDUAL_HOST_ODD_COORDINATE_GCD_DEFINED=true
COMMON_CORE_HOST_BAD_PART=C_bad=gcd(C,g^2)
COMMON_CORE_HOST_GOOD_PART=C_good=C/C_bad
RESIDUAL_HOST_EXCESS_SQUARE_FACTOR=d=g^2/C_bad
RESIDUAL_HOST_EXCESS_SQUARE_DIVIDES_VRES=true
GOOD_COMMON_CORE_PRIMES_SPLIT_IN_GAUSSIANS=true
CANONICAL_GOOD_COMMON_CORE_GAUSSIAN_DIVISOR_EXISTS=true
CANONICAL_GOOD_COMMON_CORE_GAUSSIAN_DIVISOR_NORM=C_good
RESIDUAL_HOST_CANONICAL_FACTORIZATION=W_S=g*Pi_C*T_C
RESIDUAL_GAUSSIAN_QUOTIENT_ODD_NORM=v_res_odd/d
GCD_STRATIFIED_XI_HOST_BLOCK_EXPONENT=5/8-rho
FIXED_POWER_RESIDUAL_HOST_COORDINATE_GCD_BRANCH_SAVED=true
FIVE_EIGHTHS_SATURATION_REQUIRES_RESIDUAL_HOST_GCD=Bo1
FIVE_EIGHTHS_SATURATION_GOOD_COMMON_CORE_EXPONENT=3/8
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8
NEW_WHOLE_FAMILY_POWER_SAVING_BELOW_5_8_PROVED=false
REMAINING_RECEIVER=TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence
T71_CROSS_PROMOTED_TO_MAINLINE=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cu
```