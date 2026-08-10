# Stage14-X10 — top-corner root-gcd dichotomy and dominant Cayley short cofactor

## Status

`COMPLETE_TOP_CORNER_ROOT_GCD_DICHOTOMY_AND_DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION`

Stage14-X10 consumes merged `X9`, merged `s7-32`, merged `4cs`, and the Cayley/Gaussian orientation factorization of merged `4cr`.

The current whole-family theorem remains

```text
V(B) << B^(5/8+o(1)).
```

Merged `s7-32` sharply improves the saturation geometry recorded by X9: the lower coreless corner and every upper-edge point with `phi<1/4` are already power-saved.  The only block that can still saturate `5/8` is

```text
theta=5/16,
phi=1/4.
```

X10 attacks this unique top corner by coupling the exact root gcd identified in merged `4cs` to the one-host Gaussian reconstruction of merged `s7-32` and to the `C_-/C_+` Cayley orientation split of merged `4cr`.

The outcome is an exact dichotomy.

1. If the common odd root gcd is larger than `B^(1/16)` by a fixed power, the k-side one-host parameterization already gives a strict power saving below `5/8`.
2. Therefore every potentially saturating packet has root gcd at most `B^(1/16+o(1))`.  On that branch the bad common-core peel is at most `B^(1/8+o(1))`; since the full common core is `B^(3/8+o(1))`, the good Cayley core is at least `B^(1/4-o(1))`.  One of the same/opposite Gaussian orientation factors is consequently at least `B^(1/8-o(1))`.
3. The corresponding Cayley difference/sum has size at most `B^(1/4+o(1))`, so division by this dominant orientation factor leaves a short cofactor of size at most `B^(1/8+o(1))`.

No additional whole-family saving below `5/8` is claimed in X10.  The new minimal receiver is a unique top-corner incidence in which a small physical root gcd coexists with a large same/opposite Gaussian orientation divisor and a complementary short Cayley cofactor.

No external determinant method, large sieve, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported unique 5/8 corner

Merged `s7-32` gives three legal upper bounds for the same balanced physical block:

```text
E_s(theta)=max(2*theta,1-2*theta),
E_k(theta)=3*theta-1/4,
E_xi(phi)=3*phi-1/8.
```

Hence

```text
E(theta,phi)
 <= min(E_s(theta),E_k(theta),E_xi(phi))
 <= 5/8.
```

Equality can occur only at

```text
boxed:
theta=5/16,
phi=1/4.                                           (1.1)
```

Thus the X9 two-boundary receiver is superseded as a minimal object:

```text
X9_LOWER_CORELESS_RECEIVER_MINIMAL=false,
X9_UPPER_EDGE_CONTINUUM_MINIMAL=false.
```

The current saturation component count is one.

---

## 2. Exact top-corner scale ledger

At (1.1), the merged common-core scale pin gives

```text
chi
 =2*theta+2*phi-3/4
 =3/8.                                             (2.1)
```

Therefore

```text
C=B^(3/8+o(1)).                                    (2.2)
```

The reduced residuals satisfy

```text
u_res <= B^(1/8+o(1)),
v_res <= B^(1/8+o(1)),                             (2.3)
```

and

```text
q_k =C*u_res <= B^(1/2+o(1)),
q_xi=C*v_res <= B^(1/2+o(1)).                      (2.4)
```

The switched cells have scales

```text
beta,gamma = B^(3/16+o(1)),
S,T        = B^(1/8+o(1)),                         (2.5)
```

while

```text
R,J = B^(1/4+o(1)),
X*Y = B^(1/4+o(1)).                                (2.6)
```

Merged `4cq` writes the signed quotient products as

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res).
```

Thus, after the finite 2-primary decorations are absorbed,

```text
N:=a*b*c*d <= B^(1/4+o(1)).                        (2.7)
```

The Cayley root-product term is

```text
M:=4*r*s*X*Y*epsilon_x*epsilon_k,
```

with `r,s=B^o(1)` and finite `epsilon_x,epsilon_k`, so

```text
M <= B^(1/4+o(1)).                                 (2.8)
```

These two `1/4` scales will be used after the root-gcd dichotomy.

---

## 3. The exact common odd root gcd

Merged `4cs` proves

```text
H
 := oddpart(gcd(c_k^+,c_k^-))
  = oddpart(gcd(P,Q))
  = oddpart(gcd(X,Y)).                              (3.1)
```

It also proves the simultaneous square divisibilities

```text
boxed:
H^2 | C*u_res=q_k,
H^2 | X*Y.                                         (3.2)
```

Since `X*Y=B^(1/4+o(1))`, necessarily

```text
0 <= h <= 1/8+o(1)                                (3.3)
```

on a dyadic block

```text
H=B^(h+o(1)).                                      (3.4)
```

The first divisibility in (3.2), not merely the second, is the key new input for the k-one-host count below.

---

## 4. Square-divisor sparsity in the k one-host ledger

Merged `s7-32` proves the one-host reconstruction theorem

```text
fixed (q_k,lambda_beta,W_beta,finite decorations)
=> physical collision fiber B^o(1),                (4.1)
```

with

```text
N(lambda_beta)=oddpart(beta)=B^(3/16+o(1)),
N(W_beta)=q_k*O_2(1),
q_k<=B^(1/2+o(1)).                                 (4.2)
```

Without using `H`, this costs

```text
1/2+3/16=11/16.                                    (4.3)
```

Now impose the physical square divisibility

```text
H^2 | q_k.                                         (4.4)
```

Fix a dyadic `H=B^(h+o(1))`.  Write

```text
q_k=H^2*q_0.
```

The number of choices for the pair `(H,q_0)` is bounded by

```text
B^(h+o(1)) * B^(1/2-2h+o(1))
 =B^(1/2-h+o(1)).                                  (4.5)
```

The possible multiple representations of one `q_k` by square divisors are divisor-many and are absorbed in `B^o(1)`.  For fixed residual norm, `W_beta` has divisor-many Gaussian representations, exactly as in merged `s7-32`.

Therefore the physical top-corner count on the dyadic `H` block satisfies

```text
boxed:
E_k(h) <= 11/16-h.                                (4.6)
```

This is a genuine charged-once count: `H` is chosen as part of the residual-norm parameterization and is not multiplied again as an independent physical variable.

---

## 5. Large-H branch is strictly subcritical

Compare (4.6) with the current barrier:

```text
11/16-h < 5/8
<=> h>1/16.                                        (5.1)
```

Hence for every fixed `delta>0`,

```text
h >= 1/16+delta
=> E_k(h) <= 5/8-delta.                            (5.2)
```

Equivalently,

```text
boxed:
H >= B^(1/16+delta)
=> top-corner packet is power-saved by B^(-delta). (5.3)
```

Thus any sequence of dyadic packets capable of saturating the `5/8` whole-family bound must lie in

```text
boxed:
H <= B^(1/16+o(1)).                                (5.4)
```

This removes the entire large-root-gcd half of the top-corner obstruction.

```text
TOP_CORNER_LARGE_H_FIXED_POWER_SAVED=true.
```

---

## 6. Small-H forces a large good Cayley core

Merged `4cs` identifies the second common-core gcd peel with the same physical `H` and proves

```text
C_bad | oddpart(r*s)^2 * H^2.                     (6.1)
```

At the endpoint `r,s=B^o(1)`.  On the potentially saturating branch (5.4),

```text
boxed:
C_bad <= B^(1/8+o(1)).                             (6.2)
```

But the full common core has the exact scale (2.2), so

```text
C_*=C/C_bad
 >=B^(3/8-1/8-o(1))
 =B^(1/4-o(1)).                                    (6.3)
```

Hence

```text
boxed:
C_* >= B^(1/4-o(1)).                               (6.4)
```

This improves the generic upper-edge lower bound of merged `4cs` after the `H`-large branch has been removed.

More generally, before fixing the threshold, (6.1) gives on a dyadic `H=B^(h+o(1))`

```text
C_* >= B^(3/8-2h-o(1)).                            (6.5)
```

for every `0<=h<=1/16+o(1)` in the hard branch.

---

## 7. One Gaussian orientation factor is at least B^(1/8)

Merged `4cr` supplies the exact coprime Cayley sign allocation

```text
C_*=C_-*C_+,
gcd(C_-,C_+)=1,                                   (7.1)
```

where

```text
C_- | M-N,
C_+ | M+N,                                        (7.2)
```

and

- `C_-` is the opposite Gaussian relative-orientation support;
- `C_+` is the same Gaussian relative-orientation support.

Put

```text
C_sigma=max(C_-,C_+).                              (7.3)
```

Then from (6.5),

```text
boxed:
C_sigma >= B^(3/16-h-o(1)).                        (7.4)
```

In particular the potentially saturating range `h<=1/16+o(1)` gives

```text
boxed:
C_sigma >= B^(1/8-o(1)).                           (7.5)
```

Thus every remaining hard packet carries a fixed-power same- or opposite-orientation Gaussian common divisor of norm at least `B^(1/8-o(1))`.

This factor is not charged as a second independent spacing modulus.  It is a distinguished component of the already-present common core.

---

## 8. Dominant orientation gives a short Cayley cofactor

Choose the sign `sigma` corresponding to the dominant factor `C_sigma`:

```text
sigma=-  if C_sigma=C_-,
sigma=+  if C_sigma=C_+.
```

Define the nonzero Cayley value

```text
E_-:=M-N,
E_+:=M+N.                                         (8.1)
```

The minus value cannot vanish on an asymptotic physical packet: `M=N` would give the `lambda=4` singular branch, which merged X6/4cq eliminates on the balanced strip.  The plus value is positive.

By (2.7)-(2.8),

```text
0<|E_sigma| <= B^(1/4+o(1)).                       (8.2)
```

Since `C_sigma|E_sigma`, define

```text
t_sigma:=|E_sigma|/C_sigma.                        (8.3)
```

Combining (7.4) and (8.2) yields the dyadic tradeoff

```text
boxed:
t_sigma <= B^(1/16+h+o(1)).                       (8.4)
```

and therefore on the potentially saturating branch

```text
boxed:
t_sigma <= B^(1/8+o(1)).                          (8.5)
```

The two complementary exponents satisfy

```text
(3/16-h)+(1/16+h)=1/4.                             (8.6)
```

Thus the hard top corner has an exact large-divisor/short-cofactor balance:

```text
C_sigma >= B^(3/16-h-o(1)),
t_sigma <= B^(1/16+h+o(1)),
0<=h<=1/16+o(1).                                  (8.7)
```

At the worst endpoint `h=1/16`, both scales meet at `B^(1/8)`.

```text
DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION_PROVED=true.
```

---

## 9. Gaussian meaning of the dominant factor

Merged `4cr` lifts the two orientation components to Gaussian divisors.

There are coprime Gaussian integers `Pi_+,Pi_-` with

```text
N(Pi_+)=C_+,
N(Pi_-)=C_-,                                      (9.1)
```

such that, after the fixed common-core orientation is chosen,

```text
Pi_+*Pi_-       | Z_k,
Pi_+*conj(Pi_-) | Z_xi.                           (9.2)
```

Consequently the dominant rational factor `C_sigma` of Section 7 is exactly the norm of a Gaussian divisor shared by the k and xi plus hosts either with the same orientation or after conjugating the xi host.

On the hard branch its norm satisfies (7.5).  This is the exact Gaussian structure that must be coupled to the one-host reconstruction in the next X stage.

No claim is made that `Pi_sigma` may be multiplied into the common-core root-line modulus: doing so would recharge the same common core and violate the X7 double-charge guard.

---

## 10. Why X10 does not yet improve below 5/8

The reduction (8.7) is strong but does not alone decrease the global exponent.

There are two legal parameterizations at the top corner:

### Common-core ledger

Merged `s7-31` pays

```text
C support            : 3/8,
u_res support        : 1/8,
first primitive pair : 1/8,
second quotient pair : 0,
```

for total `5/8`.

### Xi one-host ledger

Merged `s7-32` pays

```text
q_xi residual norm : 1/2,
lambda_S norm      : 1/8,
physical fiber     : 0,
```

again for total `5/8`.

The dominant Cayley divisor is a factor of the common core already present in the first ledger, while in the second ledger it is a derived divisor of the reconstructed physical host.  Counting `C_sigma` and `t_sigma` independently has total exponent `1/4`, the same ambient scale as `M` or `N`, and therefore creates no automatic saving.

A new gain requires a **fiber/incidence theorem coupling** at least two of the following before summation:

```text
H,
C_sigma / Pi_sigma,
t_sigma,
q_xi=C*v_res,
Z_S=lambda_S^2 W_S,
primitive xi-agreement root line.
```

Hence

```text
X10_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false.
```

---

## 11. New minimal receiver

The surviving X-route object is

```text
TopCornerSmallRootGcdDominantCayleyGaussianShortCofactorIncidence.
```

It consists only of physical top-corner packets satisfying

```text
theta=5/16,
phi=1/4,
C=B^(3/8+o(1)),
u_res,v_res<=B^(1/8+o(1)),
q_k,q_xi<=B^(1/2+o(1)),
H=oddpart(gcd(X,Y))<=B^(1/16+o(1)),
C_bad<=B^(1/8+o(1)),
C_*>=B^(1/4-o(1)),
C_+C_-=C_*,
C_sigma=max(C_+,C_-)>=B^(1/8-o(1)),
t_sigma=|M sigma N|/C_sigma<=B^(1/8+o(1)),
N(Pi_sigma)=C_sigma,
Pi_sigma shared in the corresponding same/opposite Gaussian orientation,
Z_S=lambda_S^2 W_S,
N(lambda_S)=oddpart(S)=B^(1/8+o(1)),
N(W_S)=q_xi*O_2(1),
all primitive agreement orientations and physical reconstruction masks.
```

Here `|M sigma N|` denotes `|M-N|` on the opposite-orientation branch and `M+N` on the same-orientation branch.

This receiver is strictly smaller than

```text
TopCornerCommonCoreXiGaussianSquareHostPrimitiveAgreementIncidence
```

because its large-`H` part is already power-saved and its remaining good common core has an explicit dominant orientation divisor and short cofactor.

---

## 12. H / tH decision

No X-specific auxiliary H is needed at Stage14-X10.

The current reduction uses only:

- merged `s7-32` one-host reconstruction;
- merged `4cs` exact gcd identification and bad-core peel;
- merged `4cr` Cayley/Gaussian orientation allocation;
- elementary square-divisor sparsity;
- exact exponent bookkeeping.

There is still unused exact arithmetic in the short cofactor and in the simultaneous `q_xi=C*v_res` / Gaussian host / primitive agreement relation.  X11 should exhaust that internal coupling before requesting an averaged Gaussian incidence theorem.

```text
X10_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false.
```

A future X-H should be opened only if the small-`H`, dominant-orientation branch survives exact reconstruction and the remaining statement is genuinely an averaged moving-host Gaussian divisibility estimate.

---

## Stage boundary

```text
STAGE14_X10=COMPLETE_TOP_CORNER_ROOT_GCD_DICHOTOMY_AND_DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION
MERGED_X9_IMPORTED=true
MERGED_S7_32_IMPORTED=true
MERGED_4CS_IMPORTED=true
MERGED_4CR_ORIENTATION_IMPORTED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
CURRENT_GAP_TO_SQRT=1/8
FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=1
FIVE_EIGHTHS_UNIQUE_SATURATION_THETA=5/16
FIVE_EIGHTHS_UNIQUE_SATURATION_PHI=1/4
TOP_CORNER_COMMON_CORE_EXPONENT=3/8
TOP_CORNER_URES_EXPONENT_MAX=1/8
TOP_CORNER_VRES_EXPONENT_MAX=1/8
TOP_CORNER_QK_EXPONENT_MAX=1/2
TOP_CORNER_QXI_EXPONENT_MAX=1/2
TOP_CORNER_H_SQUARE_DIVIDES_QK=true
TOP_CORNER_K_ONE_HOST_H_DYADIC_EXPONENT=11/16-h
TOP_CORNER_LARGE_H_FIXED_POWER_SAVED=true
POTENTIAL_SATURATION_H_EXPONENT_MAX=1/16
POTENTIAL_SATURATION_C_BAD_EXPONENT_MAX=1/8
POTENTIAL_SATURATION_C_STAR_EXPONENT_MIN=1/4
POTENTIAL_SATURATION_DOMINANT_CAYLEY_FACTOR_EXPONENT_MIN=1/8
DOMINANT_CAYLEY_FACTOR_DYADIC_EXPONENT_MIN=3/16-h
DOMINANT_CAYLEY_SHORT_COFACTOR_DYADIC_EXPONENT_MAX=1/16+h
POTENTIAL_SATURATION_DOMINANT_CAYLEY_SHORT_COFACTOR_EXPONENT_MAX=1/8
DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION_PROVED=true
X9_LOWER_CORELESS_RECEIVER_MINIMAL=false
X9_UPPER_EDGE_CONTINUUM_MINIMAL=false
S7_32_TOP_CORNER_RECEIVER_MINIMAL=false
REMAINING_RECEIVER=TopCornerSmallRootGcdDominantCayleyGaussianShortCofactorIncidence
X10_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
X10_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT_RECOMMENDED=Stage14-X11
```
