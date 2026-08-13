# Stage14-4cq — dual common-core Cayley divisor collapse and symmetric quarter-quarter reduction

## Status

`COMPLETE_DUAL_COMMON_CORE_CAYLEY_DIVISOR_COLLAPSE_AND_SYMMETRIC_QUARTER_QUARTER_REDUCTION`

Stage14-4cq consumes merged `14-4cp`, merged `14-s7-29`, merged `14-X6`, and the signed reciprocal reconstruction of `14-s7-28/14-4cn`.

The current unconditional whole-family bound remains

```text
V(B) << B^(3/4+o(1)).
```

No new exponent below `3/4` is promoted here. The new result is a strict reduction of the saturation geometry: after a controlled gcd-square peel, the common core imposed on both reciprocal plus hosts forces its good part to divide a Cayley coefficient difference-of-squares once `XY` is fixed. This gives an alternative charged-once count which saves every `phi=1/4` block with `theta>1/4`. The only block not power-saved by the combined ledgers is the symmetric corner

```text
theta=phi=1/4.
```

This supersedes the `theta=5/16` saturation tag written in 4cp: s7-29 by itself saturates on the full `phi=1/4` face; the dual-Cayley count introduced here collapses that face to the symmetric corner.

---

## 1. Imported balanced strip and primitive pair

Use the merged 4cg/s7-29 strip

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
R,J         = B^(phi+o(1)),
S,T         = B^(3/8-phi+o(1)),

3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Put

```text
A=alpha*r,
D=delta*s,
P=R*X,
Q=J*Y,
```

with `r,s=B^o(1)` and `XY=B^(1/4+o(1))` in the balanced physical packet.

The two common-core plus hosts are

```text
H_k^+  = D^2+A^2,
H_xi^+ = Q^2+P^2,
```

and by 4cg/4cm

```text
C | H_k^+,
C | H_xi^+.
```

The signed primitive allocation of s7-27/s7-28 is

```text
D+A=aU,
D-A=bV,
Q+P=cn,
Q-P=dm,
```

with

```text
gcd(U,V)=1,
gcd(m,n)=1,
UV=oddpart(RJ),
mn=oddpart(alpha*delta),
```

and full quotient products

```text
oddpart(ab)=oddpart(u_res),
oddpart(cd)=oddpart(v_res).
```

The reciprocal Edwards coefficient is exactly

```text
lambda
 = 16*r*s*X*Y*epsilon_x*epsilon_k/(a*b*c*d),
```

where `epsilon_x,epsilon_k in {1,2}` are the 2-primary agreement factors.

---

## 2. First common-core gcd-square peel

Let

```text
g_A=gcd(A,D).
```

Merged 4cl gives

```text
g_A | r*s.
```

Write

```text
A=g_A*A_0,
D=g_A*D_0,
gcd(A_0,D_0)=1.
```

Define

```text
C_1 := C / gcd(C,g_A^2).
```

Since `C | D^2+A^2=g_A^2(D_0^2+A_0^2)`, cancellation gives

```text
C_1 | D_0^2+A_0^2.
```

Every odd prime of `C_1` is a unit on `A_0D_0`. Thus the Cayley ratio

```text
x := (D_0+A_0)/(D_0-A_0)
```

is a unit modulo `C_1` and satisfies

```text
x^2 == -1 (mod C_1).
```

The factor removed at this step divides `g_A^2|(rs)^2`.

---

## 3. Second common-core gcd-square peel

Let

```text
g_P=gcd(P,Q).
```

Merged 4cl gives

```text
g_P | X*Y.
```

Write

```text
P=g_P*P_0,
Q=g_P*Q_0,
gcd(P_0,Q_0)=1.
```

Starting from `C_1`, define

```text
C_* := C_1 / gcd(C_1,g_P^2).
```

Then

```text
C_* | Q_0^2+P_0^2,
gcd(C_*,P_0Q_0)=1.
```

Hence

```text
y := (Q_0+P_0)/(Q_0-P_0)
```

is a unit modulo `C_*` and

```text
y^2 == -1 (mod C_*).
```

The total removed factor

```text
C_bad := C/C_*
```

satisfies

```text
boxed:
C_bad | g_A^2*g_P^2 | (r*s*X*Y)^2.                 (3.1)
```

Therefore, once `r,s,XY` are fixed, the bad part has only `B^o(1)` possibilities.

---

## 4. Unit check for the Edwards coefficient

On `C_*`, the four signed factors `D+A,D-A,Q+P,Q-P` are units.

Merged s7-29 gives

```text
gcd(C,oddpart(RJ))=1.
```

On the k side, if an odd `p` divided both `C` and `alpha*delta`, then 4cm gives

```text
p | H_xi^+,
p | H_xi^-.
```

Hence `p|P*Q`; but merged 4cl gives

```text
gcd(oddpart(alpha*delta),P*Q)=1,
```

a contradiction. Thus

```text
boxed:
gcd(C,oddpart(alpha*delta))=1.                      (4.1)
```

Consequently `a,b,c,d` are units modulo `C_*` after the gcd-square peel, and the rational coefficient `lambda` has an invertible denominator modulo `C_*`.

---

## 5. Dual common-core Cayley congruence

The exact reciprocal Edwards equation from 4cn is

```text
(x^2-1)(y^2-1)=lambda*x*y.
```

Modulo `C_*`, Sections 2--3 give

```text
x^2 == y^2 == -1.
```

Therefore

```text
boxed:
lambda*x*y == 4 (mod C_*).                         (5.1)
```

Every odd prime-power factor of `C_*` has exactly two square roots of `-1`. Hence primewise `x*y=+1` or `-1`, and (5.1) yields

```text
boxed:
lambda^2 == 16 (mod C_*).                          (5.2)
```

Substitute

```text
lambda=16*r*s*X*Y*epsilon_x*epsilon_k/(a*b*c*d).
```

Because `C_*` is odd and the denominator is a unit, dividing by the unit `16` gives

```text
boxed:
C_* |
  (4*r*s*X*Y*epsilon_x*epsilon_k-a*b*c*d)
  (4*r*s*X*Y*epsilon_x*epsilon_k+a*b*c*d).         (5.3)
```

This is the dual common-core Cayley divisor lock. Primewise, the relative orientation of the two Gaussian roots allocates each prime power of `C_*` to one of the two factors in (5.3).

---

## 6. The lambda=4 branch is empty on the whole balanced strip

Merged X6 proved the exact singular parity identities

```text
K_switch=beta*gamma in {1,2},
Xi_switch=S*T in {1,2}
```

for every physical `lambda=4` packet before using top-theta sizes.

The size contradiction holds on the entire balanced strip:

```text
beta*gamma
 = B^(1-2theta+o(1))
 >= B^(3/8-o(1)),

S*T
 = B^(3/4-2phi+o(1))
 >= B^(1/4-o(1)).
```

Thus

```text
boxed:
BALANCED_STRIP_LAMBDA4_SINGULAR_BRANCH_EMPTY=true. (6.1)
```

The first factor in (5.3) is therefore nonzero on every asymptotic physical block; the second factor is positive. For fixed `(u_res,v_res,a,b,c,d,r,s,XY)`, `C_*` divides a fixed nonzero integer and `C_bad` divides `(rsXY)^2`. Hence

```text
boxed:
fixed residual/quotient + r,s + XY
=> #C <= B^o(1).                                  (6.2)
```

This is a legal alternative quantifier order: choose the root product `XY` first and recover `C` by divisor data.

---

## 7. Alternative block ledger

The residual pair satisfies

```text
u_res*v_res <= B^(1/4+o(1)),
```

so choosing it costs at most `B^(1/4+o(1))`. The root product has `XY=B^(1/4+o(1))`, hence at most `B^(1/4+o(1))` values. Once residuals, quotient decoration, `r,s`, and `XY` are fixed, (6.2) makes `C` divisor-many.

For a block `C=B^(c+o(1))`, the s7-29 primitive common-core root-line lemma gives

```text
#(U,V) <= B^(2phi-c+o(1)).
```

Every primitive pair has `B^o(1)` physical completions by s7-28; pre-fixing `XY` merely discards pairs whose reconstructed root product is different.

Hence

```text
boxed:
E_dual(theta,phi,c)
 <= 1/2+2phi-c.                                    (7.1)
```

Together with s7-29,

```text
boxed:
E(theta,phi,c)
 <= min(2phi+1/4, 1/2+2phi-c).                    (7.2)
```

Every block with `c>1/4` therefore gains the fixed amount `c-1/4` beyond the s7-29 ledger.

---

## 8. Correct saturation face and common-core size on phi=1/4

The s7-29 bound `2phi+1/4` saturates at `3/4` whenever `phi=1/4`; it does not by itself force `theta=5/16`. Therefore the 4cp tag

```text
THREE_QUARTER_SATURATION_REQUIRES_THETA=5/16
```

is superseded here. Before the dual-Cayley bound, the possible saturation face is

```text
phi=1/4,
1/4 <= theta <= 5/16.                              (8.1)
```

On this face the dyadic sizes determine the common-core exponent. We have

```text
H_k^+=D^2+A^2=B^(2theta+o(1)),
S*T=B^(1/4+o(1)),
oddpart(H_k^+)=C*oddpart(S*T).
```

The 2-primary factor is `B^o(1)`, so

```text
boxed:
c=2theta-1/4.                                      (8.2)
```

Substituting (8.2) into (7.1) at `phi=1/4` gives

```text
boxed:
E_dual(theta,1/4)
 <= 5/4-2theta.                                    (8.3)
```

Therefore for every fixed `eta>0`,

```text
theta >= 1/4+eta
=> E <= 3/4-2eta.                                  (8.4)
```

The only point on (8.1) where both ledgers can still equal `3/4` is

```text
boxed:
theta=phi=1/4,
c=1/4.                                             (8.5)
```

So the current `3/4` barrier has collapsed from a face to one symmetric dyadic corner.

---

## 9. Structure of the surviving symmetric corner

At

```text
theta=phi=1/4,
c=1/4,
```

the residual bounds become

```text
u_res = B^o(1),
v_res <= B^(1/4+o(1)).                            (9.1)
```

Hence `oddpart(a*b)=B^o(1)`, while

```text
UV=B^(1/2+o(1)),
C=B^(1/4+o(1)),
XY=B^(1/4+o(1)).                                  (9.2)
```

The surviving packet simultaneously satisfies a quarter-scale common-core Gaussian root line for `(U,V)`, the real/twisted four-root quadratic-value masks of X6, and the Cayley divisor lock (5.3), with the bad common-core part supported on `(rsXY)^2`.

The new minimal obstruction is

```text
SymmetricQuarterQuarterCayleyGaussianPrimitiveRootLineEnergy.
```

No current exact argument proves a fixed-power saving for this symmetric corner.

---

## 10. H / tH decision

The completed genus-one H audit is not the minimal receiver. The tH18 private-canonical-prime root-modulus problem is a different fixed-U coefficient space and is not cross-promoted.

The new symmetric corner still has exact prime-allocation structure to exhaust, especially the factorization of `C_*` between the two Cayley coefficient factors and its interaction with the Gaussian norm factorization of `F_+`. Therefore

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false.
```

If a genuine average theorem remains after the next exact divisor split, the H target should be the narrow object

```text
SymmetricQuarterQuarterCayleyGaussianPrimitiveRootLineEnergy
```

with `C~XY~B^(1/4)`, `UV~B^(1/2)`, `u_res=B^o(1)` and all original squarefree/orientation masks retained.

---

## Stage boundary

```text
STAGE14_4CQ=COMPLETE_DUAL_COMMON_CORE_CAYLEY_DIVISOR_COLLAPSE_AND_SYMMETRIC_QUARTER_QUARTER_REDUCTION
MERGED_4CP_IMPORTED=true
MERGED_S7_29_IMPORTED=true
MERGED_X6_IMPORTED=true
DUAL_COMMON_CORE_GCD_SQUARE_PEEL_PROVED=true
DUAL_COMMON_CORE_BAD_PART_DIVIDES_RSXY_SQUARE=true
COMMON_CORE_COPRIME_TO_K_AGREEMENT_ODD_PART=true
DUAL_COMMON_CORE_CAYLEY_LAMBDA_SQUARE_CONGRUENCE_PROVED=true
DUAL_COMMON_CORE_CAYLEY_DIVISOR_LOCK_PROVED=true
FIXED_RESIDUAL_QUOTIENT_ROOT_PRODUCT_COMMON_CORE_MULTIPLICITY=Bo1
BALANCED_STRIP_LAMBDA4_SINGULAR_BRANCH_EMPTY=true
ALTERNATIVE_DUAL_CAYLEY_BLOCK_EXPONENT=1/2+2phi-c
COMBINED_BLOCK_EXPONENT=min(2phi+1/4,1/2+2phi-c)
STAGE14_4CP_THETA_5_16_SATURATION_TAG_SUPERSEDED=true
PRE_DUAL_THREE_QUARTER_SATURATION_FACE=phi=1/4,theta_in_[1/4,5/16]
QUARTER_PHI_COMMON_CORE_EXPONENT=c=2theta-1/4
DUAL_CAYLEY_QUARTER_PHI_EXPONENT=5/4-2theta
CURRENT_THREE_QUARTER_SATURATION_CORNER=theta=phi=1/4,c=1/4
SYMMETRIC_CORNER_URES_EXPONENT=0
SYMMETRIC_CORNER_VRES_EXPONENT_MAX=1/4
SYMMETRIC_CORNER_C_EXPONENT=1/4
SYMMETRIC_CORNER_XY_EXPONENT=1/4
SYMMETRIC_CORNER_UV_EXPONENT=1/2
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4
NEW_WHOLE_FAMILY_POWER_SAVING_BELOW_3_4_PROVED=false
REMAINING_RECEIVER=SymmetricQuarterQuarterCayleyGaussianPrimitiveRootLineEnergy
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cr
```