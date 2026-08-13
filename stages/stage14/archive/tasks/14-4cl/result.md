# Stage14-4cl — prime allocation, physical diagonal elimination, and reciprocal cyclotomic reduction

## Status

`COMPLETE_PHYSICAL_PROPORTIONAL_BRANCH_ELIMINATION_AND_RECIPROCAL_CYCLOTOMIC_REDUCTION`

Merged Stage14-4ck reduces the balanced endpoint cell fiber to

```text
G*q_k*r*s * F(U,V)
 = 2*q_xi*X*Y * F(A,D),

F(a,b)=a*b*(b-a)*(b+a),

U=R*X,
V=J*Y,
A=alpha*r,
D=delta*s,
```

with `D>A>0`, `V>U>0`. Merged Stage14-X3 independently reaches the same four-agreement-cell quartic receiver and identifies a fixed-power **relaxed proportional/diagonal obstruction** if the physical cross-role locks and switch-product integrality are discarded.

Stage14-4cl imports that warning and uses exactly the omitted physical structure. The proportional branch is impossible at the endpoint, and the surviving off-proportional problem admits a canonical prime-allocation and reciprocal cyclotomic decomposition.

No whole-family power saving is promoted. The unconditional endpoint remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Fixed outer data

Condition on

```text
(C,u_res,v_res),
X_root=(x_1,y_1,x_2,y_2),
(r_1,r_2,s_1,s_2,g_1,g_2),
```

at the `B^o(1)` cost already established by 4ck/X2/X3. Put

```text
q_k=C*u_res,
q_xi=C*v_res,

r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,
G=g_1*g_2.
```

The moving agreement cells are `alpha,delta,R,J`, with

```text
gcd(alpha,delta)=1,
gcd(R,J)=1,
gcd(alpha*delta,R*J)=1,                 (1.1)
```

because the `k` and `xi` labels are coprime in the primitive packet.

Define

```text
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y.                                  (1.2)
```

The imported quartic equation is

```text
boxed:
G*q_k*r*s*F(U,V)
 = 2*q_xi*X*Y*F(A,D).                   (1.3)
```

---

## 2. X3 relaxed proportional obstruction is not physical

The proportional branch is

```text
U/A = V/D,                              (2.1)
```

or equivalently

```text
U*D=V*A.                                (2.2)
```

Substituting (1.2),

```text
R*delta*X*s = J*alpha*Y*r.              (2.3)
```

By (1.1), `R*delta` is coprime to `J*alpha`. Therefore, away from the finite 2-primary convention,

```text
boxed:
oddpart(R*delta) | Y*r,                 (2.4)

boxed:
oddpart(J*alpha) | X*s.                 (2.5)
```

At the balanced endpoint,

```text
R,J=B^(phi+o(1)),
alpha,delta=B^(theta+o(1)),
X,Y=B^(1/8+o(1)),
r,s=B^o(1),

theta+phi>=3/8-o(1).                   (2.6)
```

Hence (2.4) would require

```text
B^(theta+phi-o(1)) <= B^(1/8+o(1)),    (2.7)
```

contradicting (2.6) by a fixed exponent gap

```text
3/8-1/8=1/4.                            (2.8)
```

Thus

```text
boxed:
PHYSICAL_PROPORTIONAL_QUARTIC_BRANCH_EMPTY=true.    (2.9)
```

This directly removes the relaxed diagonal family isolated by X3 from the physical endpoint receiver. It does **not** prove that the remaining off-proportional energy is power-sparse.

```text
RELAXED_DIAGONAL_FIXED_POWER_OBSTRUCTION_IMPORTED=true
RELAXED_DIAGONAL_OBSTRUCTION_SURVIVES_PHYSICAL_MASKS=false
PHYSICAL_RECEIVER_COUNTEREXAMPLE_PROVED=false
```

---

## 3. Moving gcds are supported on fixed data

Let

```text
g_U=gcd(U,V),
g_A=gcd(A,D).
```

Since `U=R X`, `V=J Y` and `gcd(R,J)=1`, primewise

```text
boxed:
g_U | X*Y.                                  (3.1)
```

Similarly `A=alpha r`, `D=delta s` and `gcd(alpha,delta)=1` give

```text
boxed:
g_A | r*s.                                  (3.2)
```

Therefore

```text
#(g_U,g_A) <= tau(XY)*tau(rs)=B^o(1).       (3.3)
```

Condition on the two gcds and write

```text
U=g_U*u,
V=g_U*v,
A=g_A*a,
D=g_A*d,

gcd(u,v)=gcd(a,d)=1.                       (3.4)
```

Then

```text
F(U,V)=g_U^4*f(u,v),
F(A,D)=g_A^4*f(a,d),

f(m,n)=m*n*(n-m)*(n+m).                    (3.5)
```

---

## 4. Primitive quartic factors have disjoint odd support

For `gcd(m,n)=1`, the four integers

```text
m,
n,
n-m,
n+m                                      (4.1)
```

are pairwise coprime away from 2. In particular,

```text
gcd(n-m,n+m)|2,                            (4.2)
```

and every other pair has gcd one.

Thus every odd prime dividing `f(m,n)` belongs to exactly one primitive factor.

```text
PRIMITIVE_SPLIT_QUARTIC_ODD_FACTOR_SUPPORT_DISJOINT=true. (4.3)
```

This recovers X3's fixed-value `B^o(1)` fiber theorem and also allows a cross-value allocation matrix.

---

## 5. Exact 4 x 4 good-prime allocation matrix

After fixing `g_U,g_A`, rewrite (1.3) as

```text
K_L*f(u,v)=K_R*f(a,d),                    (5.1)
```

where

```text
K_L=G*q_k*r*s*g_U^4,
K_R=2*q_xi*X*Y*g_A^4                      (5.2)
```

are fixed in the current outer fiber.

Set

```text
L=(u,v,v-u,v+u),
Rvec=(a,d,d-a,d+a).                       (5.3)
```

For every odd prime

```text
p not dividing 2*K_L*K_R,                 (5.4)
```

(4.3) gives a unique `L_i` and unique `Rvec_j` containing `p`, while (5.1) forces equal valuations. Therefore each good prime has one unique allocation cell

```text
(i,j) in {1,2,3,4}^2.                    (5.5)
```

Let `m_ij` be the product, with valuations, of good primes assigned to `(i,j)`. Then the sixteen `m_ij` are pairwise coprime and

```text
goodpart(L_i)=product_j m_ij,
goodpart(Rvec_j)=product_i m_ij.          (5.6)
```

Primes dividing `2*K_L*K_R` are fixed after the outer conditioning. Distributing their polynomially bounded valuations among the eight primitive factors costs only `B^o(1)`.

Hence the off-proportional quartic equality has a `B^o(1)` refinement into a 4 x 4 prime-allocation matrix subject to

```text
L_3=L_2-L_1,
L_4=L_2+L_1,
Rvec_3=Rvec_2-Rvec_1,
Rvec_4=Rvec_2+Rvec_1.                     (5.7)
```

```text
QUARTIC_GOOD_PRIME_ALLOCATION_MATRIX_4X4_PROVED=true.
```

---

## 6. Physical switch integrality gives reciprocal fourth-difference divisibility

Merged 4ck/X3 give

```text
S*T = H_k^+H_k^-/(q_k*R*J),
beta*gamma = H_xi^+H_xi^-/(q_xi*alpha*delta).
```

Since

```text
H_k^+H_k^-=D^4-A^4,
H_xi^+H_xi^-=V^4-U^4,
```

we obtain

```text
boxed:
D^4-A^4 = q_k*(R*J)*(S*T),             (6.1)

boxed:
V^4-U^4 = q_xi*(alpha*delta)*(beta*gamma). (6.2)
```

In particular,

```text
boxed:
R*J | D^4-A^4,                           (6.3)

boxed:
alpha*delta | V^4-U^4.                   (6.4)
```

These are precisely the switch-product integrality conditions whose removal creates X3's relaxed obstruction.

---

## 7. Agreement moduli are coprime to the opposite bases

Primitive packet coprimality gives

```text
gcd(xi,k*omega_1*omega_2)=1,
gcd(k,xi*z_1*z_2)=1.
```

Since `R*J|xi`, `alpha*delta|k`, every odd prime of `r*s` occurs in `omega_1*omega_2`, and every odd prime of `X*Y` occurs in `z_1*z_2`,

```text
boxed:
gcd(oddpart(RJ),A*D)=1,                  (7.1)

boxed:
gcd(oddpart(alpha*delta),U*V)=1.         (7.2)
```

Thus an odd agreement prime in (6.3)-(6.4) cannot lie in an opposite base.

---

## 8. Unique three-way cyclotomic allocation

Factor

```text
D^4-A^4=(D-A)(D+A)(D^2+A^2),             (8.1)
V^4-U^4=(V-U)(V+U)(V^2+U^2).             (8.2)
```

For odd primes coprime to the bases, the three factors on either line are pairwise coprime. Define

```text
M_xi^- = gcd(oddpart(RJ),D-A),
M_xi^+ = gcd(oddpart(RJ),D+A),
M_xi^i = gcd(oddpart(RJ),D^2+A^2),

M_k^-  = gcd(oddpart(alpha*delta),V-U),
M_k^+  = gcd(oddpart(alpha*delta),V+U),
M_k^i  = gcd(oddpart(alpha*delta),V^2+U^2).          (8.3)
```

Then exactly

```text
boxed:
M_xi^-*M_xi^+*M_xi^i=oddpart(RJ),       (8.4)

boxed:
M_k^-*M_k^+*M_k^i=oddpart(alpha*delta).  (8.5)
```

Each triple is pairwise coprime. Equivalently, every odd agreement prime has one unique branch label

```text
-, +, or i.                              (8.6)
```

Conditioning on these prime labels costs at most

```text
3^omega(RJ)*3^omega(alpha*delta)=B^o(1). (8.7)
```

The construction may also be applied separately to `R,J,alpha,delta` if cellwise branch data are needed later.

---

## 9. Quadratic branches are split-Gaussian

For an odd `p|M_xi^i`,

```text
D^2 == -A^2 (mod p),
p does not divide A*D.
```

Hence `-1` is a quadratic residue modulo `p`, so

```text
p == 1 (mod 4).                           (9.1)
```

The same holds for every odd `p|M_k^i`.

```text
CYCLOTOMIC_I_BRANCH_ODD_PRIMES_ARE_1_MOD_4=true.    (9.2)
```

No `1/2` density is inserted; this is an exact support statement.

---

## 10. Dominant branch at the sharp corner

From (8.4)-(8.5),

```text
max(M_xi^-,M_xi^+,M_xi^i) >= oddpart(RJ)^(1/3),
max(M_k^-,M_k^+,M_k^i) >= oddpart(alpha*delta)^(1/3). (10.1)
```

With

```text
R,J=B^(phi+o(1)),
alpha,delta=B^(theta+o(1)),
```

there is an xi cyclotomic modulus of exponent at least `2phi/3-o(1)` and a k modulus of exponent at least `2theta/3-o(1)`.

At the unique conditional `7/8` corner

```text
(theta,phi)=(5/16,1/4),
```

this gives

```text
boxed:
xi dominant modulus >= B^(1/6-o(1)),     (10.2)

boxed:
k dominant modulus >= B^(5/24-o(1)).     (10.3)
```

There are only nine dominant branch types

```text
(-,-), (-,+), (-,i),
(+,-), (+,+), (+,i),
(i,-), (i,+), (i,i).                     (10.4)
```

---

## 11. New minimal receiver

X3 names the post-quartic physical object

```text
OffDiagonalCrossRoleSwitchIntegralQuarticEnergy.
```

Stage14-4cl proves two refinements of that receiver:

1. the proportional/diagonal branch is actually empty under the physical cross-role masks;
2. the remaining off-proportional branch has the 4 x 4 quartic prime-allocation matrix and both reciprocal three-way cyclotomic allocations.

Define

```text
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence. (11.1)
```

Then, up to the already explicit `B^o(1)` gcd/exceptional-prime refinements,

```text
boxed:
CrossRoleSwitchIntegralQuarticAgreementIncidence
 <= B^o(1)
    * OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence. (11.2)
```

No physical pair is double charged.

The remaining obstruction is an off-diagonal count with **mutually generated moduli**:

```text
RJ | D^4-A^4,
alpha*delta | V^4-U^4,
```

plus the same 4 x 4 prime-allocation matrix and all original squarefree/balanced/reconstruction masks.

---

## 12. What remains open

Closed in 4cl:

```text
- X3 relaxed proportional obstruction eliminated physically;
- moving gcds reduced to B^o(1) fixed-data divisors;
- primitive split-quartic odd supports separated;
- 4 x 4 good-prime allocation matrix;
- reciprocal fourth-difference divisibilities;
- unique -, +, i cyclotomic allocation on both agreement products;
- i-branch primes restricted to 1 mod 4;
- sharp-corner dominant moduli 1/6 and 5/24.
```

Still open:

```text
OFF_DIAGONAL_RECIPROCAL_CYCLOTOMIC_QUARTIC_ALLOCATION_INCIDENCE_PROVED=false
FIXED_RESIDUAL_ROOT_AGREEMENT_QUARTIC_FIBER_BO1_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
```

Therefore

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

---

## 13. H-line decision

No external theorem is needed for 4cl. The X3 relaxed obstruction is removed by exact physical coprimality and endpoint sizes; the remaining reduction is elementary prime allocation and cyclotomic divisibility.

A generic binary-quartic energy theorem is still not the correct H target because it would discard the reciprocal self-generated moduli that distinguish the physical problem from X3's relaxed diagonal family.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
```

Stage14-4cm should attack the nine dominant branch types. Linear-linear and linear-quadratic types should first be treated by exact congruence/divisor parameterization. The `(i,i)` branch should retain its `1 mod 4`/Gaussian structure. A mainline H audit is justified only if a genuine average theorem remains after this branchwise physical attack.

Parallel `tH17` is a fixed-U Kummer theorem audit and is not imported into this positive reciprocal-cyclotomic receiver.

---

## Stage boundary

```text
STAGE14_4CL=COMPLETE_PHYSICAL_PROPORTIONAL_BRANCH_ELIMINATION_AND_RECIPROCAL_CYCLOTOMIC_REDUCTION
MERGED_4CK_IMPORTED=true
MERGED_X3_IMPORTED=true
MERGED_X2_TRANSITIVELY_IMPORTED=true
RELAXED_DIAGONAL_FIXED_POWER_OBSTRUCTION_IMPORTED=true
PROPORTIONAL_BRANCH_RDELTA_DIVIDES_YR=true
PROPORTIONAL_BRANCH_JALPHA_DIVIDES_XS=true
PROPORTIONAL_BRANCH_ENDPOINT_EXPONENT_GAP=1/4
PHYSICAL_PROPORTIONAL_QUARTIC_BRANCH_EMPTY=true
RELAXED_DIAGONAL_OBSTRUCTION_SURVIVES_PHYSICAL_MASKS=false
PHYSICAL_RECEIVER_COUNTEREXAMPLE_PROVED=false
MOVING_GCD_UV_DIVIDES_FIXED_XY=true
MOVING_GCD_AD_DIVIDES_FIXED_RS=true
MOVING_GCD_REFINEMENT_COST=Bo1
PRIMITIVE_SPLIT_QUARTIC_ODD_FACTOR_SUPPORT_DISJOINT=true
QUARTIC_GOOD_PRIME_ALLOCATION_MATRIX_4X4_PROVED=true
QUARTIC_EXCEPTIONAL_PRIME_REFINEMENT_COST=Bo1
RECIPROCAL_XI_AGREEMENT_DIVIDES_OPPOSITE_FOURTH_DIFFERENCE=true
RECIPROCAL_K_AGREEMENT_DIVIDES_OPPOSITE_FOURTH_DIFFERENCE=true
XI_AGREEMENT_OPPOSITE_BASE_ODD_COPRIME=true
K_AGREEMENT_OPPOSITE_BASE_ODD_COPRIME=true
XI_THREE_WAY_CYCLOTOMIC_ALLOCATION_PROVED=true
K_THREE_WAY_CYCLOTOMIC_ALLOCATION_PROVED=true
CYCLOTOMIC_I_BRANCH_ODD_PRIMES_ARE_1_MOD_4=true
EXTREME_CORNER_XI_DOMINANT_CYCLOTOMIC_EXPONENT=1/6
EXTREME_CORNER_K_DOMINANT_CYCLOTOMIC_EXPONENT=5/24
EXTREME_CORNER_DOMINANT_BRANCH_TYPE_COUNT=9
OFF_DIAGONAL_RECIPROCAL_CYCLOTOMIC_QUARTIC_ALLOCATION_INCIDENCE_PROVED=false
FIXED_RESIDUAL_ROOT_AGREEMENT_QUARTIC_FIBER_BO1_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cm attack the nine off-diagonal reciprocal cyclotomic branch types, beginning with linear-linear and linear-quadratic cases before deciding whether the quadratic-quadratic branch needs a mainline H audit
```