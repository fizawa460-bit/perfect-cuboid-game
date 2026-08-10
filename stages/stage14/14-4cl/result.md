# Stage14-4cl — prime allocation and reciprocal cyclotomic reduction

## Status

`COMPLETE_PRIMITIVE_QUARTIC_PRIME_ALLOCATION_AND_RECIPROCAL_CYCLOTOMIC_REDUCTION`

Stage14-4ck reduces the balanced endpoint cell fiber, for fixed residual triple and primitive physical root line, to the split quartic equation

```text
G*q_k*r*s * F(U,V)
 = 2*q_xi*X*Y * F(A,D),

F(a,b)=a*b*(b-a)*(b+a),

U=R*X,
V=J*Y,
A=alpha*r,
D=delta*s,
```

with

```text
D>A>0,
V>U>0,
```

and with switched products recovered divisor-many from the agreement cells.

Stage14-4cl uses the factorization of `F` and, crucially, the switch-product integrality that is still present in the same physical packet. The result is that the remaining receiver is not a generic binary-quartic equal-value problem. After `B^o(1)` refinements it is a reciprocal prime-allocation problem with two exact three-branch cyclotomic divisibilities.

No whole-family power saving is promoted here. The unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported fixed data and notation

Condition on

```text
(C,u_res,v_res),
X_root=(x_1,y_1,x_2,y_2),
(r_1,r_2,s_1,s_2,g_1,g_2),
```

at the `B^o(1)` cost already justified in 4ck/X2. Put

```text
q_k=C*u_res,
q_xi=C*v_res,

r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,
G=g_1*g_2.
```

The four moving agreement cells are

```text
alpha,delta,R,J,
```

and

```text
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y.
```

Merged balanced-cell coprimality gives

```text
gcd(alpha,delta)=1,
gcd(R,J)=1.
```

The 4ck quartic equation is

```text
boxed:
G*q_k*r*s*F(U,V)
 =2*q_xi*X*Y*F(A,D).                    (1.1)
```

---

## 2. The moving gcds are supported on fixed data

Define

```text
g_U=gcd(U,V),
g_A=gcd(A,D).
```

Since `U=R X`, `V=J Y` and `gcd(R,J)=1`, every prime in `g_U` must already occur in the fixed product `X*Y`. More precisely, prime by prime,

```text
boxed:
g_U | X*Y.                                  (2.1)
```

Likewise `A=alpha r`, `D=delta s` and `gcd(alpha,delta)=1` imply

```text
boxed:
g_A | r*s.                                  (2.2)
```

Hence the possible values of `g_U` and `g_A` over a fixed residual/root/small-data fiber are divisor-many:

```text
#(g_U,g_A) <= tau(XY)*tau(rs)=B^o(1).       (2.3)
```

We may therefore condition on `g_U,g_A` before the quartic count.

Write

```text
U=g_U*u,
V=g_U*v,
A=g_A*a,
D=g_A*d,

gcd(u,v)=gcd(a,d)=1.                      (2.4)
```

Then

```text
F(U,V)=g_U^4*f(u,v),
F(A,D)=g_A^4*f(a,d),

f(m,n)=m*n*(n-m)*(n+m).                   (2.5)
```

---

## 3. Primitive split-quartic factors are odd-pairwise-coprime

For a primitive pair `gcd(m,n)=1`, consider

```text
m,
n,
n-m,
n+m.                                      (3.1)
```

Every gcd between two distinct entries is `1`, except possibly

```text
gcd(n-m,n+m) | 2.                          (3.2)
```

Therefore their odd parts are pairwise coprime.

Equivalently, every odd prime dividing `f(m,n)` belongs to exactly one of the four primitive factors in (3.1).

This gives

```text
PRIMITIVE_SPLIT_QUARTIC_ODD_FACTOR_SUPPORT_DISJOINT=true.  (3.3)
```

The only intrinsic overlap inside the four-factor form is 2-primary and costs `O(1)` branches.

---

## 4. Exact 4 x 4 cross-prime allocation matrix

After fixing `g_U,g_A`, rewrite (1.1) as

```text
K_L*f(u,v)=K_R*f(a,d),                    (4.1)
```

where the now-fixed coefficients are

```text
K_L=G*q_k*r*s*g_U^4,
K_R=2*q_xi*X*Y*g_A^4.                     (4.2)
```

Let

```text
L=(u,v,v-u,v+u),
Rvec=(a,d,d-a,d+a).                        (4.3)
```

For every odd prime

```text
p not dividing 2*K_L*K_R,                 (4.4)
```

Section 3 says that `p` occurs in one unique component `L_i` and one unique component `Rvec_j`. Equation (4.1) then gives equality of those two `p`-adic valuations.

Thus every good prime has a unique cell

```text
(i,j) in {1,2,3,4}^2.                     (4.5)
```

Define `m_ij` to be the product, with valuation, of all good primes assigned to `(i,j)`. The sixteen integers `m_ij` are pairwise coprime and satisfy

```text
goodpart(L_i)=product_j m_ij,
goodpart(Rvec_j)=product_i m_ij.           (4.6)
```

Primes dividing `2*K_L*K_R` are fixed after the outer conditioning. Distributing their polynomially bounded valuations among the eight primitive factors costs only

```text
B^o(1).                                    (4.7)
```

Consequently the quartic equality has an exact `B^o(1)` refinement into a **4 x 4 prime-allocation matrix** plus the additive relations

```text
L_3=L_2-L_1,
L_4=L_2+L_1,
Rvec_3=Rvec_2-Rvec_1,
Rvec_4=Rvec_2+Rvec_1.                      (4.8)
```

This is substantially narrower than an unrestricted quartic-energy problem.

---

## 5. Switch integrality gives two reciprocal fourth-difference divisibilities

The 4ck recovery formulas are

```text
S*T = H_k^+H_k^-/(q_k*R*J),
beta*gamma = H_xi^+H_xi^-/(q_xi*alpha*delta).
```

Using

```text
H_k^+H_k^-=D^4-A^4,
H_xi^+H_xi^-=V^4-U^4,
```

we obtain the exact identities

```text
boxed:
D^4-A^4 = q_k*(R*J)*(S*T),              (5.1)

boxed:
V^4-U^4 = q_xi*(alpha*delta)*(beta*gamma). (5.2)
```

In particular,

```text
boxed:
R*J | D^4-A^4,                            (5.3)

boxed:
alpha*delta | V^4-U^4.                    (5.4)
```

These are not heuristic local densities. They are exact consequences of the physical switched-cell integrality.

---

## 6. The agreement moduli are coprime to the opposite bases

Merged primitive coprimalities give

```text
gcd(xi,k*omega_1*omega_2)=1,
gcd(k,xi*z_1*z_2)=1.
```

Since `R*J | xi`, `alpha*delta | k`, and every odd prime of `r*s` occurs in `omega_1*omega_2`,

```text
boxed:
gcd(oddpart(RJ),A*D)=1.                   (6.1)
```

Likewise every odd prime of `X*Y` occurs in `z_1*z_2`, up to the fixed 2-primary convention, so

```text
boxed:
gcd(oddpart(alpha*delta),U*V)=1.          (6.2)
```

Therefore an odd agreement prime dividing the opposite fourth-power difference cannot disappear into the bases themselves.

---

## 7. Unique three-way cyclotomic allocation of every agreement prime

Factor

```text
D^4-A^4=(D-A)(D+A)(D^2+A^2),              (7.1)
V^4-U^4=(V-U)(V+U)(V^2+U^2).              (7.2)
```

For an odd prime `p` coprime to the two bases, the three factors in either line are pairwise coprime at `p`. Hence every odd `p|R*J` lies in exactly one of

```text
D-A,
D+A,
D^2+A^2.                                  (7.3)
```

Similarly every odd `p|alpha*delta` lies in exactly one of

```text
V-U,
V+U,
V^2+U^2.                                  (7.4)
```

Define canonically

```text
M_xi^- = gcd(oddpart(RJ),D-A),
M_xi^+ = gcd(oddpart(RJ),D+A),
M_xi^i = gcd(oddpart(RJ),D^2+A^2),

M_k^-  = gcd(oddpart(alpha*delta),V-U),
M_k^+  = gcd(oddpart(alpha*delta),V+U),
M_k^i  = gcd(oddpart(alpha*delta),V^2+U^2).          (7.5)
```

Then exactly

```text
boxed:
M_xi^- * M_xi^+ * M_xi^i = oddpart(RJ),             (7.6)

boxed:
M_k^- * M_k^+ * M_k^i = oddpart(alpha*delta).       (7.7)
```

and the three factors on each line are pairwise coprime.

The same construction may be applied separately to `R,J` and to `alpha,delta`; no primewise choice remains once the physical quadruple is fixed. For counting purposes, conditioning on one of the three labels per prime costs at most

```text
3^omega(RJ)*3^omega(alpha*delta)=B^o(1).             (7.8)
```

---

## 8. Quadratic branches are Gaussian-split

If an odd prime `p` belongs to `M_xi^i`, then

```text
D^2 == -A^2 (mod p),
p does not divide A*D.
```

Thus `-1` is a quadratic residue modulo `p`, and

```text
p == 1 (mod 4).                                      (8.1)
```

The identical conclusion holds for every odd prime of `M_k^i`.

Hence

```text
boxed:
odd primes on either i-branch are 1 mod 4.          (8.2)
```

This is the exact rational cyclotomic shadow of the Gaussian square-divisor structure seen earlier in 4cf; no Gaussian density is multiplied into the count.

---

## 9. Dominant-branch lower bounds

From the product decompositions (7.6)-(7.7),

```text
max(M_xi^-,M_xi^+,M_xi^i) >= oddpart(RJ)^(1/3),     (9.1)
max(M_k^-, M_k^+, M_k^i ) >= oddpart(alpha*delta)^(1/3). (9.2)
```

At exponent scale,

```text
R,J=B^(phi+o(1)),
alpha,delta=B^(theta+o(1)),
```

so every surviving packet has at least one xi-side cyclotomic modulus of exponent

```text
>= 2*phi/3-o(1),                                     (9.3)
```

and at least one k-side cyclotomic modulus of exponent

```text
>= 2*theta/3-o(1).                                   (9.4)
```

At the unique conditional `7/8` corner

```text
(theta,phi)=(5/16,1/4),
```

these become

```text
boxed:
xi dominant cyclotomic modulus >= B^(1/6-o(1)),     (9.5)

boxed:
k dominant cyclotomic modulus  >= B^(5/24-o(1)).    (9.6)
```

Thus the sharp corner splits into only nine dominant branch types

```text
(-,-), (-,+), (-,i),
(+,-), (+,+), (+,i),
(i,-), (i,+), (i,i).                                (9.7)
```

---

## 10. New minimal receiver

Sections 2-9 show that `CommonCoreBinaryQuarticAgreementIncidence` should no longer be treated as a generic moving equal-value equation.

After `B^o(1)` refinement, every packet is described by

```text
- fixed residual/root/small data;
- conditioned gcds g_U|XY and g_A|rs;
- one 4 x 4 good-prime allocation matrix for the split quartic equality;
- the four additive row/column relations;
- one xi-side three-way cyclotomic allocation of RJ into D-A,D+A,D^2+A^2;
- one k-side three-way cyclotomic allocation of alpha*delta into V-U,V+U,V^2+U^2;
- the switched-product positivity/squarefree completion masks;
- all original balanced dyadic and reconstruction conditions.
```

Define the resulting receiver

```text
ReciprocalCyclotomicQuarticAllocationIncidence.      (10.1)
```

Then

```text
boxed:
CommonCoreBinaryQuarticAgreementIncidence
 <= B^o(1) * ReciprocalCyclotomicQuarticAllocationIncidence. (10.2)
```

No independent density has been inserted.

The live obstruction is now the count of **mutually generated moduli**: `RJ` is a divisor of the fourth-power difference generated by `(alpha,delta)`, while `alpha*delta` is a divisor of the fourth-power difference generated by `(R,J)`, with the same packet also satisfying the quartic allocation matrix.

---

## 11. What this does and does not prove

4cl proves:

```text
- moving gcds cost only B^o(1);
- primitive quartic factors have disjoint odd prime support;
- the moving quartic equality has a 4 x 4 good-prime allocation matrix;
- RJ and alpha*delta satisfy reciprocal fourth-difference divisibility;
- every odd agreement prime has a unique -, +, or i cyclotomic branch;
- i-branch primes are 1 mod 4;
- the unique sharp corner has dominant moduli B^(1/6) and B^(5/24).
```

It does **not** prove

```text
RECIPROCAL_CYCLOTOMIC_QUARTIC_ALLOCATION_INCIDENCE_PROVED=false,
FIXED_RESIDUAL_ROOT_AGREEMENT_QUARTIC_FIBER_BO1_PROVED=false,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

The whole-family endpoint therefore remains `7/8`.

---

## 12. Mainline H decision

No external theorem is needed for 4cl. Every step is exact gcd algebra, unique prime allocation, divisor refinement, or elementary cyclotomic congruence.

In particular, a generic binary-quartic energy theorem is **not yet the correct H target**: the physical packet has reciprocal self-generated moduli that such a theorem would discard.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
```

Stage14-4cm should count the nine dominant branch types. The linear branches `D-A`, `D+A`, `V-U`, `V+U` should be exhausted by congruence/divisor parameterization first; the `(i,i)` or mixed quadratic branches should retain their `1 mod 4` / Gaussian structure. Only if a genuine average theorem remains after that branchwise attack should a mainline H audit be opened.

The parallel `tH17` result concerns the fixed-U Kummer route and is not imported into this positive reciprocal-cyclotomic receiver.

---

## Stage boundary

```text
STAGE14_4CL=COMPLETE_PRIMITIVE_QUARTIC_PRIME_ALLOCATION_AND_RECIPROCAL_CYCLOTOMIC_REDUCTION
MERGED_4CK_IMPORTED=true
MERGED_X2_COMPATIBILITY_CHECKED=true
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
RECIPROCAL_CYCLOTOMIC_QUARTIC_ALLOCATION_INCIDENCE_PROVED=false
FIXED_RESIDUAL_ROOT_AGREEMENT_QUARTIC_FIBER_BO1_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cm attack the nine dominant reciprocal cyclotomic branch types, beginning with linear-linear and linear-quadratic cases before deciding whether the quadratic-quadratic branch needs a mainline H audit
```