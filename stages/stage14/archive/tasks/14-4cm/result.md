# Stage14-4cm — quadratic-branch elimination and top-theta signed-linear reduction

## Status

`COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_TOP_THETA_SIGNED_LINEAR_QUOTIENT_REDUCTION`

This stage consumes merged 4cl, s7-25, and X4.  X4 preserves the charged-once X-route interpretation of the 4cl off-diagonal receiver; 4cm now strengthens that receiver itself.

Merged s7-25 proves that every block a fixed distance below `theta=5/16` is already power-saved.  Therefore only

```text
theta=5/16,
3/16 <= phi <= 1/4
```

can still saturate `7/8`.

The main exact theorem here is that the quadratic cyclotomic `i` branch of 4cl is physically empty on **both** reciprocal sides.  Hence the nine branch types of 4cl/X4 reduce to the four signed linear-linear types.

No new whole-family exponent is promoted.  The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Exact packet and notation

Use

```text
U_s=S*T,          V_a=R*J,
M_s=beta*gamma,   N_a=alpha*delta,
```

so `xi=U_s V_a` and `k=M_s N_a`.

Merged 4cg gives

```text
q_k=C*u_res,
q_xi=C*v_res,
```

and

```text
xi*q_k = H_k^+ H_k^-,
k*q_xi = H_xi^+ H_xi^-.
```

With

```text
r=r1*r2,  s=s1*s2,
X=x1*x2,  Y=y1*y2,
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y,
```

we have

```text
H_k^-  = D^2-A^2,
H_xi^- = V^2-U^2.
```

The common-core definition is exactly

```text
oddpart(H_k^+)  = C*oddpart(U_s),
oddpart(H_xi^+) = C*oddpart(M_s).
```

---

## 2. Complementary minus-factor odd parts

Taking odd parts in

```text
(U_s*V_a)*(C*u_res)=H_k^+*H_k^-
```

and cancelling `C*oddpart(U_s)` gives

```text
boxed:
oddpart(H_k^-)
 = oddpart(R*J)*oddpart(u_res).                     (2.1)
```

Likewise

```text
boxed:
oddpart(H_xi^-)
 = oddpart(alpha*delta)*oddpart(v_res).             (2.2)
```

Thus the plus/minus decomposition is complementary:

```text
H_k^+  odd support: C and xi-switch support,
H_k^-  odd support: u_res and xi-agreement support,
H_xi^+ odd support: C and k-switch support,
H_xi^- odd support: v_res and k-agreement support.
```

This uses only exact multiplicativity of odd parts.

---

## 3. Both quadratic cyclotomic branches are empty

From (2.1),

```text
oddpart(RJ) | H_k^-=(D-A)(D+A).
```

Merged 4cl also gives

```text
gcd(oddpart(RJ),A*D)=1.
```

Hence no odd prime of `RJ` can also divide `D^2+A^2`: if an odd `p` divided both `D^2-A^2` and `D^2+A^2`, it would divide both `2D^2` and `2A^2`, contradicting the base coprimality.

Therefore

```text
boxed:
M_xi^i=1,
XI_CYCLOTOMIC_I_BRANCH_EMPTY=true.                  (3.1)
```

Similarly, (2.2) and merged 4cl give

```text
oddpart(alpha*delta)|(V-U)(V+U),
gcd(oddpart(alpha*delta),U*V)=1,
```

so

```text
boxed:
M_k^i=1,
K_CYCLOTOMIC_I_BRANCH_EMPTY=true.                   (3.2)
```

Consequently the five branch types involving `i`

```text
(-,i), (+,i), (i,-), (i,+), (i,i)
```

are empty.  The 4cl/X4 nine-type receiver reduces to

```text
(-,-), (-,+), (+,-), (+,+).                        (3.3)
```

No Gaussian large-sieve or quadratic-quadratic H theorem is needed for these branches: they do not exist physically.

---

## 4. Full two-way signed allocation

Define

```text
L_xi^- = gcd(oddpart(RJ),D-A),
L_xi^+ = gcd(oddpart(RJ),D+A).
```

The two factors are odd-coprime on the agreement support, so

```text
L_xi^- L_xi^+ = oddpart(RJ),
gcd(L_xi^-,L_xi^+)=1.                               (4.1)
```

Likewise

```text
L_k^- = gcd(oddpart(alpha*delta),V-U),
L_k^+ = gcd(oddpart(alpha*delta),V+U),
```

with

```text
L_k^- L_k^+ = oddpart(alpha*delta),
gcd(L_k^-,L_k^+)=1.                                 (4.2)
```

Thus every odd agreement prime has exactly one sign label, with no third cyclotomic branch.

---

## 5. Square-root dominant moduli on the only saturation edge

From (4.1)-(4.2), choose dominant signs with

```text
L_xi,dom >= oddpart(RJ)^(1/2),
L_k,dom  >= oddpart(alpha*delta)^(1/2).              (5.1)
```

On the merged s7-25 top-theta edge,

```text
R,J=B^(phi+o(1)),
alpha,delta=B^(5/16+o(1)).
```

Removing the possible factor 2 does not affect exponents, hence

```text
boxed:
L_xi,dom >= B^(phi-o(1)),                           (5.2)

boxed:
L_k,dom >= B^(5/16-o(1)).                          (5.3)
```

This improves the three-way cube-root moduli recorded in 4cl.

---

## 6. Signed linear quotient pair

Let `sigma,tau in {-,+}` be dominant signs and define

```text
t_xi=(D sigma A)/L_xi,dom,
t_k =(V tau U)/L_k,dom,                             (6.1)
```

with the obvious interpretation of `sigma,tau` as difference/sum.

Since

```text
D,A=B^(5/16+o(1)),
U,V=B^(phi+1/8+o(1)),
```

we obtain

```text
boxed:
t_xi <= B^(5/16-phi+o(1)),                         (6.2)

boxed:
t_k <= B^(phi-3/16+o(1)).                          (6.3)
```

Therefore

```text
boxed:
log_B(t_xi-range)+log_B(t_k-range) <= 1/8+o(1).    (6.4)
```

Equivalently the raw quotient-pair support is at most

```text
B^(1/8+o(1)).                                       (6.5)
```

The endpoints balance as

```text
phi=3/16: (t_xi,t_k) exponents <=(1/8,0),
phi=1/4:  (t_xi,t_k) exponents <=(1/16,1/16).
```

---

## 7. Charged-once interpretation using s7-25 and X4

Merged s7-25 proves

```text
fixed (C,u_res,v_res,U_s=S*T)
=> legal decorated physical packet fiber <=B^o(1).  (7.1)
```

Merged X4 confirms that the off-diagonal 4cl constraints may be retained in the X1 charged-once packet without double charging.

Hence every admissible top-edge switch product carries exact data

```text
sigma,tau,
L_xi,dom,L_k,dom,
t_xi,t_k
```

satisfying

```text
D sigma A=L_xi,dom*t_xi,
V tau U=L_k,dom*t_k,
L_xi,dom|oddpart(RJ),
L_k,dom|oddpart(alpha*delta).                       (7.2)
```

This is a genuine reduction of the remaining receiver.

---

## 8. Quantifier guard

The `B^(1/8)` quotient-pair support does **not** itself prove a power saving.  We have not proved that

```text
(C,u_res,v_res,U_s)
 -> (sigma,tau,t_xi,t_k)
```

has `B^o(1)` or fixed-power-saving average fiber.

The dominant moduli are moving divisors of the reconstructed agreement products, and the s7-25 quantifier order reconstructs the root data only after `U_s` is fixed.

Therefore

```text
SIGNED_QUOTIENT_SUPPORT_ALONE_IMPLIES_POWER_SAVING=false.
```

---

## 9. New receiver

The new minimal mainline receiver is

```text
TopThetaReciprocalSignedLinearQuotientXiSwitchIncidence.
```

It counts top-edge charged-once tuples `(C,u_res,v_res,U_s)` satisfying one of the four signed reciprocal linear systems (7.2), with all original product, squarefree, interval, orientation, and reconstruction masks retained.

A sufficient next step is an average bound for the fiber over `(sigma,tau,t_xi,t_k)`, or an equivalent determinant/divisor parameterization of the two reciprocal linear equations.

---

## 10. H-line decision

Stage14-4cm uses exact odd-part cancellation, factorization, coprimality, and exponent bookkeeping only.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

In particular there is no reason to start a quadratic-quadratic/Gaussian H audit: the quadratic branch is empty.  Stage14-4cn should first attack the signed-linear quotient fiber algebraically.

---

## Stage boundary

```text
STAGE14_4CM=COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_TOP_THETA_SIGNED_LINEAR_QUOTIENT_REDUCTION
MERGED_4CL_IMPORTED=true
MERGED_S7_25_IMPORTED=true
MERGED_X4_IMPORTED=true
X1_CHARGED_ONCE_QUANTIFIER_ORDER_PRESERVED=true
ODDPART_HK_MINUS=oddpart(R*J)*oddpart(u_res)
ODDPART_HXI_MINUS=oddpart(alpha*delta)*oddpart(v_res)
COMPLEMENTARY_MINUS_ODDPART_DECOMPOSITION_PROVED=true
XI_CYCLOTOMIC_I_BRANCH_EMPTY=true
K_CYCLOTOMIC_I_BRANCH_EMPTY=true
MIXED_OR_QUADRATIC_DOMINANT_BRANCH_TYPES_EXIST=false
DOMINANT_BRANCH_TYPE_COUNT=4
XI_SIGNED_LINEAR_ALLOCATION_FULL_AGREEMENT_SUPPORT=true
K_SIGNED_LINEAR_ALLOCATION_FULL_AGREEMENT_SUPPORT=true
TOP_THETA_BARRIER=theta=5/16
TOP_THETA_ALLOWED_PHI_INTERVAL=[3/16,1/4]
TOP_THETA_XI_DOMINANT_LINEAR_MODULUS_EXPONENT=phi
TOP_THETA_K_DOMINANT_LINEAR_MODULUS_EXPONENT=5/16
TOP_THETA_XI_SIGNED_QUOTIENT_EXPONENT_MAX=5/16-phi
TOP_THETA_K_SIGNED_QUOTIENT_EXPONENT_MAX=phi-3/16
TOP_THETA_SIGNED_QUOTIENT_PAIR_SUPPORT_EXPONENT_MAX=1/8
TOP_THETA_RECIPROCAL_SIGNED_LINEAR_QUOTIENT_XI_SWITCH_INCIDENCE_PROVED=false
SIGNED_QUOTIENT_SUPPORT_ALONE_IMPLIES_POWER_SAVING=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4cn attack TopThetaReciprocalSignedLinearQuotientXiSwitchIncidence by determinant/divisor parameterization of the two reciprocal linear equations before deciding whether any external incidence H theorem is needed
```
