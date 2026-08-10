# Stage14-4cm — quadratic-branch elimination and signed reciprocal linear reduction

## Status

`COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_TOP_THETA_SIGNED_LINEAR_QUOTIENT_REDUCTION`

Stage14-4cm consumes merged Stage14-4cl and merged Stage14-s7-25 on the same balanced physical endpoint packet.

Stage14-4cl reduced the fixed-residual/root-line formulation to nine possible dominant reciprocal cyclotomic branch types `(-,+,i) x (-,+,i)`.  Stage14-s7-25 independently proved that every block with `theta<5/16` by a fixed amount already has a fixed-power saving, so only the top-theta edge

```text
theta=5/16,
3/16 <= phi <= 1/4
```

can still saturate `7/8`.

The main new point is that the quadratic `i` branch is not merely arithmetically special: on a physical packet it is **empty** on both reciprocal sides.  This follows by returning to the exact odd-part definition of the common core.

Consequently the nine branch types collapse to four signed linear-linear types, and the dominant agreement moduli improve from cube-root size to square-root size.  On the top-theta edge the two corresponding quotient variables have total raw support exponent at most `1/8`.

No whole-family fixed-power saving is promoted yet, because the map from an admissible xi-switch product to the signed quotient pair has not been proved to have subpolynomial average fiber.

The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported notation

Use the eight balanced cells

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta.
```

Put

```text
U_s = S*T,                 # xi switch product
V_a = R*J,                 # xi agreement product
M_s = beta*gamma,          # k switch product
N_a = alpha*delta.         # k agreement product
```

Thus

```text
xi=U_s*V_a,
k=M_s*N_a.
```

Merged 4cg gives

```text
q_k=C*u_res,
q_xi=C*v_res,
```

and the four factors

```text
H_k^+  = delta^2*s^2 + alpha^2*r^2,
H_k^-  = delta^2*s^2 - alpha^2*r^2,
H_xi^+ = J^2*Y^2 + R^2*X^2,
H_xi^- = J^2*Y^2 - R^2*X^2,
```

where

```text
r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2.
```

The exact product identities are

```text
xi*q_k = H_k^+*H_k^-,
k*q_xi = H_xi^+*H_xi^-.
```

The common-core definition is

```text
oddpart(H_k^+)  = C*oddpart(U_s),
oddpart(H_xi^+) = C*oddpart(M_s).
```

Define the scaled bases used in 4ck/4cl:

```text
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y.
```

Then

```text
H_k^-  = D^2-A^2,
H_xi^- = V^2-U^2.
```

---

## 2. Exact complementary odd-part identities

Take odd parts in

```text
(U_s*V_a)*(C*u_res)=H_k^+*H_k^-.
```

Since odd part is multiplicative and

```text
oddpart(H_k^+)=C*oddpart(U_s),
```

we may cancel the identical positive odd factors `C*oddpart(U_s)` and obtain

```text
boxed:
oddpart(H_k^-)
 = oddpart(V_a)*oddpart(u_res).                    (2.1)
```

No probabilistic independence or coprimality heuristic is used here.

Similarly, from

```text
(M_s*N_a)*(C*v_res)=H_xi^+*H_xi^-
```

and

```text
oddpart(H_xi^+)=C*oddpart(M_s),
```

we obtain

```text
boxed:
oddpart(H_xi^-)
 = oddpart(N_a)*oddpart(v_res).                    (2.2)
```

Thus the common-core plus-factor decomposition has an exact complementary minus-factor decomposition:

```text
plus k side:   C * oddpart(U_s),
minus k side:  oddpart(u_res) * oddpart(V_a),

plus xi side:  C * oddpart(M_s),
minus xi side: oddpart(v_res) * oddpart(N_a).
```

This identity was implicit in the merged factor products but had not been promoted as the branch-elimination theorem.

---

## 3. The xi-side quadratic cyclotomic branch is empty

Merged 4cl defined the xi reciprocal allocation from

```text
oddpart(RJ) | D^4-A^4
            =(D-A)(D+A)(D^2+A^2).
```

Equation (2.1) is stronger:

```text
oddpart(RJ) | H_k^- = D^2-A^2=(D-A)(D+A).          (3.1)
```

Moreover merged 4cl gives

```text
gcd(oddpart(RJ),A*D)=1.
```

For an odd prime `p` coprime to `A*D`, the two integers

```text
D^2-A^2,
D^2+A^2
```

cannot both vanish modulo `p`, since their sum and difference would force `p|2D^2` and `p|2A^2`.

Hence

```text
boxed:
gcd(oddpart(RJ),D^2+A^2)=1.                        (3.2)
```

In the notation of 4cl,

```text
boxed:
M_xi^i=1.                                           (3.3)
```

Thus no odd xi-agreement prime occupies the quadratic cyclotomic branch.

---

## 4. The k-side quadratic cyclotomic branch is empty

The same argument uses (2.2):

```text
oddpart(alpha*delta)
 | H_xi^-
 = (V-U)(V+U).                                      (4.1)
```

Merged 4cl gives

```text
gcd(oddpart(alpha*delta),U*V)=1.
```

Therefore

```text
boxed:
gcd(oddpart(alpha*delta),V^2+U^2)=1,               (4.2)
```

and hence

```text
boxed:
M_k^i=1.                                            (4.3)
```

The Gaussian/quadratic branch is absent from the physical endpoint on both reciprocal sides.

Consequently every branch type involving `i` is empty:

```text
(-,i), (+,i), (i,-), (i,+), (i,i).
```

The nine 4cl dominant branch types reduce exactly to the four signed linear-linear types

```text
(-,-), (-,+), (+,-), (+,+).                        (4.4)
```

---

## 5. Exact signed allocation of the full agreement products

Define

```text
L_xi^- = gcd(oddpart(RJ),D-A),
L_xi^+ = gcd(oddpart(RJ),D+A).
```

Because the two linear factors are odd-coprime on the agreement support,

```text
boxed:
L_xi^-*L_xi^+ = oddpart(RJ),
gcd(L_xi^-,L_xi^+)=1.                               (5.1)
```

Likewise define

```text
L_k^- = gcd(oddpart(alpha*delta),V-U),
L_k^+ = gcd(oddpart(alpha*delta),V+U),
```

and obtain

```text
boxed:
L_k^-*L_k^+ = oddpart(alpha*delta),
gcd(L_k^-,L_k^+)=1.                                 (5.2)
```

Primewise sign labels therefore still cost only

```text
2^omega(RJ)*2^omega(alpha*delta)=B^o(1),            (5.3)
```

but there is no third branch.

---

## 6. Square-root dominant moduli

From (5.1)-(5.2), one of the two xi linear moduli and one of the two k linear moduli satisfy

```text
L_xi,dom >= oddpart(RJ)^(1/2),
L_k,dom  >= oddpart(alpha*delta)^(1/2).              (6.1)
```

The cells are squarefree, so removing the possible factor `2` does not change any power exponent.

Merged s7-25 proves that only

```text
theta=5/16,
3/16<=phi<=1/4                                      (6.2)
```

can still saturate the current endpoint.

On this edge,

```text
R,J=B^(phi+o(1)),
alpha,delta=B^(5/16+o(1)),
```

hence

```text
boxed:
L_xi,dom >= B^(phi-o(1)),                           (6.3)

boxed:
L_k,dom >= B^(5/16-o(1)).                          (6.4)
```

This strictly improves the 4cl generic three-way bounds `2phi/3` and `5/24`.

At the old extreme corner `phi=1/4`, the xi dominant modulus improves from exponent `1/6` to `1/4`, while the k dominant modulus improves from `5/24` to `5/16`.

---

## 7. Signed quotient variables

Choose signs `sigma,tau in {-,+}` attaining the dominant moduli and define positive integers

```text
t_xi := (D sigma A)/L_xi,dom,
t_k  := (V tau U)/L_k,dom,                          (7.1)
```

where `D sigma A` means `D-A` for `sigma=-` and `D+A` for `sigma=+`, and similarly for `V tau U`.

Because `D,A=B^(5/16+o(1))`, (6.3) gives

```text
boxed:
t_xi <= B^(5/16-phi+o(1)).                         (7.2)
```

Also

```text
U,V=B^(phi+1/8+o(1)),
```

so (6.4) gives

```text
boxed:
t_k <= B^(phi-3/16+o(1)).                          (7.3)
```

Adding the two exponents cancels `phi`:

```text
boxed:
(5/16-phi)+(phi-3/16)=1/8.                         (7.4)
```

Therefore the raw signed quotient-pair support satisfies

```text
boxed:
# {(t_xi,t_k)} <= B^(1/8+o(1))                     (7.5)
```

for each fixed dyadic top-edge block, after the `O(1)` choice of dominant signs.

Endpoint interpolation is exact:

```text
phi=3/16:
  t_xi exponent <=1/8,
  t_k  exponent <=0;

phi=1/4:
  t_xi exponent <=1/16,
  t_k  exponent <=1/16.                             (7.6)
```

---

## 8. Relation to the s7-25 charged-once receiver

Merged s7-25 proves

```text
fixed (C,u_res,v_res,U_s=S*T)
=> decorated physical packet fiber <=B^o(1).        (8.1)
```

It also proves that every block away from `theta=5/16` is already power-saved.

Thus 4cm may restrict attention to the top edge and attach to every admissible switch product `U_s` the exact data

```text
sigma,tau,
L_xi,dom,L_k,dom,
t_xi,t_k,                                                (8.2)
```

satisfying

```text
D sigma A = L_xi,dom*t_xi,
V tau U   = L_k,dom*t_k,                              (8.3)

L_xi,dom | oddpart(RJ),
L_k,dom  | oddpart(alpha*delta).                     (8.4)
```

All quantities remain on the same charged-once physical packet.

---

## 9. Quantifier guard

The support bound (7.5) is not by itself a whole-family saving.

The invalid shortcut is

```text
signed quotient pair has B^(1/8) support
=> admissible U_s has B^(1/8) support.
```

No injective or `B^o(1)`-fiber map

```text
U_s -> (t_xi,t_k)
```

has been proved.  The dominant moduli themselves are moving divisors of the reconstructed agreement products, and the physical root data are reconstructed in the s7-25 quantifier order rather than fixed in advance.

Accordingly

```text
SIGNED_QUOTIENT_SUPPORT_ALONE_IMPLIES_POWER_SAVING=false.
```

The quotient reduction is structural information for the next incidence count, not an exponent promotion.

---

## 10. New minimal receiver

Define

```text
TopThetaReciprocalSignedLinearQuotientXiSwitchIncidence
```

to count the top-theta charged-once data

```text
(C,u_res,v_res,U_s),
```

whose s7-25 reconstruction admits one of the four sign pairs and dominant divisor/quotient data (8.2)-(8.4).

The old receiver

```text
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence
```

has therefore reduced to a purely signed-linear object on the only dyadic edge capable of saturation.

A next sufficient theorem is a fixed-power average bound for the fibers of

```text
(C,u_res,v_res,U_s)
 -> (sigma,tau,t_xi,t_k)
```

or an equivalent determinant/divisor estimate using the two reciprocal linear equations (8.3).

---

## 11. H-line decision

Stage14-4cm uses only exact odd-part cancellation, merged coprimality, elementary factorization, and dyadic bookkeeping.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

In particular, the quadratic-quadratic branch does **not** require a Gaussian or external quartic-energy H audit because that branch is empty.

The next stage should first attack the two reciprocal signed linear equations by exact determinant/divisor parameterization.  A mainline H audit is justified only if a genuine average signed-linear incidence theorem remains after that arithmetic reduction.

Parallel fixed-U `tH17/t63` results are on a different coefficient space and are not cross-promoted.

---

## Stage boundary

```text
STAGE14_4CM=COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_TOP_THETA_SIGNED_LINEAR_QUOTIENT_REDUCTION
MERGED_4CL_IMPORTED=true
MERGED_S7_25_IMPORTED=true
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