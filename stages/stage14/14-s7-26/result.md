# Stage14-s7-26 — common-core elimination of the agreement `i` branches and top-edge reciprocal linear allocation

## Status

`COMPLETE_COMMON_CORE_AGREEMENT_I_BRANCH_ELIMINATION_AND_TOP_EDGE_LINEAR_ALLOCATION`

Stage14-s7-26 consumes merged `s7-25` together with merged `4cg` and the newer merged mainline `4cl`.

The `s7-25` quantifier is kept:

```text
fixed (C,u_res,v_res,U_sw=S*T)
=> B^o(1) decorated physical packets.
```

The remaining `7/8` saturation set is the top-theta edge

```text
theta=5/16,
3/16 <= phi <= 1/4.
```

Merged `4cl` refines the physical quartic problem by assigning every odd agreement prime to one of the three cyclotomic factors `-`, `+`, or `i`.  On the common-core packet this three-way split is not sharp.  The plus-factor coprimality already proved in merged `4cg` forces the entire odd agreement products into the two linear factors.  Thus the `i` branch is empty on both the `xi`-agreement and `k`-agreement sides.

The nine dominant branch types of `4cl` collapse to four reciprocal linear branch types, and the dominant moduli strengthen from one-third powers to square-root powers of the agreement products.

No whole-family fixed-power saving is claimed in this stage.  The current unconditional exponent remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported common packet and notation

Keep the balanced cells

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta.
```

Use product coordinates

```text
X_sw := S*T,
X_ag := R*J,
K_sw := beta*gamma,
K_ag := alpha*delta.                                 (1.1)
```

Thus

```text
xi = X_sw*X_ag,
k  = K_sw*K_ag.                                      (1.2)
```

Let

```text
r = r_1*r_2,
s = s_1*s_2,
X = x_1*x_2,
Y = y_1*y_2.                                         (1.3)
```

As in merged `4cl`, define

```text
A = alpha*r,
D = delta*s,
P = R*X,
Q = J*Y.                                             (1.4)
```

The physical inequalities are

```text
D>A>0,
Q>P>0.                                               (1.5)
```

The four common-core host factors are exactly

```text
H_k^+  = D^2+A^2,
H_k^-  = D^2-A^2,
H_xi^+ = Q^2+P^2,
H_xi^- = Q^2-P^2.                                   (1.6)
```

Merged `4cg` and `s7-25` give

```text
q_k  = C*u_res,
q_xi = C*v_res,                                      (1.7)

oddpart(H_k^+)  = C*oddpart(X_sw),
oddpart(H_xi^+) = C*oddpart(K_sw).                  (1.8)
```

All statements below refer to this same physical pair.  No common-core and quartic savings are multiplied independently.

---

## 2. The agreement products are coprime to the opposite plus factors

Merged `4cg` proves the exact primewise statements

```text
gcd(H_k^+,  oddpart(X_ag)) = 1,
gcd(H_xi^+, oddpart(K_ag)) = 1.                     (2.1)
```

In the present notation this is

```text
gcd(D^2+A^2, oddpart(R*J)) = 1,                     (2.2)

gcd(Q^2+P^2, oddpart(alpha*delta)) = 1.             (2.3)
```

These are stronger than merely saying that `i`-branch primes are `1 mod 4`: no odd agreement prime may occur in the `i` factor at all.

This is the exact common-core refinement that was not used in the three-way upper decomposition of `4cl`.

---

## 3. Every odd xi-agreement prime lies in `D-A` or `D+A`

The residual product identity is

```text
xi*q_k = H_k^+*H_k^-.                               (3.1)
```

Every odd prime `p|X_ag` divides `xi`.  By (2.1), `p` does not divide `H_k^+`.  Hence

```text
p | H_k^- = D^2-A^2 = (D-A)(D+A).                  (3.2)
```

Because `p` is coprime to `A*D`, it cannot divide both `D-A` and `D+A`.

Define

```text
X_ag^- := gcd(oddpart(X_ag),D-A),
X_ag^+ := gcd(oddpart(X_ag),D+A).                   (3.3)
```

Then exactly

```text
boxed:
X_ag^-*X_ag^+ = oddpart(X_ag),                      (3.4)

gcd(X_ag^-,X_ag^+) = 1,                            (3.5)

X_ag^- | D-A,
X_ag^+ | D+A.                                       (3.6)
```

In particular the `4cl` quadratic allocation is trivial on the common-core intersection:

```text
boxed:
M_xi^i=1.                                           (3.7)
```

---

## 4. Every odd k-agreement prime lies in `Q-P` or `Q+P`

Similarly

```text
k*q_xi = H_xi^+*H_xi^-.                            (4.1)
```

For every odd `p|K_ag`, merged `4cg` gives `p∤H_xi^+`.  Therefore

```text
p | H_xi^- = Q^2-P^2=(Q-P)(Q+P).                   (4.2)
```

Define

```text
K_ag^- := gcd(oddpart(K_ag),Q-P),
K_ag^+ := gcd(oddpart(K_ag),Q+P).                   (4.3)
```

Then

```text
boxed:
K_ag^-*K_ag^+ = oddpart(K_ag),                      (4.4)

gcd(K_ag^-,K_ag^+) = 1,                            (4.5)

K_ag^- | Q-P,
K_ag^+ | Q+P.                                       (4.6)
```

and

```text
boxed:
M_k^i=1.                                            (4.7)
```

Thus the physical common-core packet has no Gaussian/cyclotomic-`i` agreement branch on either side.

---

## 5. Exact cancellation with the residuals

The preceding divisibilities can be strengthened using the exact common-core odd-part normalization.

Write

```text
X_sw=2^e*X_sw,o,
H_k^+=2^a*C*X_sw,o.                                 (5.1)
```

From

```text
X_sw*X_ag*C*u_res=H_k^+*H_k^-                       (5.2)
```

we obtain exactly

```text
boxed:
2^a*H_k^- = 2^e*X_ag*u_res.                        (5.3)
```

Likewise, writing

```text
K_sw=2^f*K_sw,o,
H_xi^+=2^b*C*K_sw,o,                                (5.4)
```

we get

```text
boxed:
2^b*H_xi^- = 2^f*K_ag*v_res.                       (5.5)
```

Consequently the entire odd support of the two difference hosts is a two-factor linear allocation:

```text
oddpart((D-A)(D+A)) = oddpart(X_ag*u_res),          (5.6)

oddpart((Q-P)(Q+P)) = oddpart(K_ag*v_res).          (5.7)
```

After the harmless gcd refinements already isolated in `4cl`, the two linear factors on each line have disjoint odd support.  The residual primes and agreement primes are therefore allocated together between only two linear factors, not three cyclotomic factors.

---

## 6. Dominant agreement moduli improve from cube-root to square-root scale

Because (3.4) has only two factors,

```text
max(X_ag^-,X_ag^+) >= oddpart(X_ag)^(1/2).          (6.1)
```

Similarly

```text
max(K_ag^-,K_ag^+) >= oddpart(K_ag)^(1/2).          (6.2)
```

On the top-theta edge

```text
theta=5/16,
R,J=B^(phi+o(1)),
alpha,delta=B^(5/16+o(1)),                          (6.3)
```

so

```text
X_ag=R*J=B^(2*phi+o(1)),
K_ag=alpha*delta=B^(5/8+o(1)).                      (6.4)
```

Hence there is a dominant xi-agreement linear modulus

```text
boxed:
L_xi >= B^(phi-o(1)),                                (6.5)
```

and a dominant k-agreement linear modulus

```text
boxed:
L_k >= B^(5/16-o(1)).                               (6.6)
```

This strictly improves the `4cl` three-way lower bounds `2phi/3` and `5/24` on this common-core intersection.

The dominant sign pair now has only four possibilities:

```text
(-,-), (-,+), (+,-), (+,+).                         (6.7)
```

```text
TOP_EDGE_DOMINANT_LINEAR_BRANCH_TYPE_COUNT=4.
```

---

## 7. The complementary cofactors are genuinely short

The first dominant modulus divides one of

```text
D-A,
D+A,                                                 (7.1)
```

both of size at most

```text
B^(5/16+o(1)).                                       (7.2)
```

Thus if

```text
D+sigma*A = L_xi*c_xi,
```

for the dominant sign `sigma`, then

```text
boxed:
c_xi <= B^(5/16-phi+o(1)).                         (7.3)
```

The second dominant modulus divides one of

```text
Q-P,
Q+P,                                                 (7.4)
```

where

```text
P,Q=B^(phi+1/8+o(1)).                                (7.5)
```

So

```text
Q+tau*P = L_k*c_k
```

with

```text
boxed:
c_k <= B^(phi-3/16+o(1)).                          (7.6)
```

Since

```text
3/16<=phi<=1/4,                                     (7.7)
```

we have the uniform windows

```text
1/16 <= 5/16-phi <= 1/8,                            (7.8)

0 <= phi-3/16 <= 1/16.                              (7.9)
```

Most notably,

```text
boxed:
log_B c_xi + log_B c_k <= 1/8+o(1).                (7.10)
```

This is only a cofactor-support reduction.  The moving dominant moduli themselves have not been eliminated, so (7.10) is not promoted to a whole-family saving.

---

## 8. Compatibility with merged `4cl`

Merged `4cl` proves a valid three-way decomposition

```text
-, +, i
```

for the less-refined reciprocal quartic receiver.  It does not claim that all three branches are physically populated.

Stage14-s7-26 intersects that decomposition with the earlier common-core plus-factor coprimality from `4cg`.  On this narrower coefficient space,

```text
M_xi^i=M_k^i=1.                                     (8.1)
```

Therefore

```text
4cl nine dominant branch types
-> s7-26 four common-core linear branch types.       (8.2)
```

This is a legal strengthening on the same physical pair, not a contradiction of `4cl` and not an independent saving multiplication.

```text
MERGED_4CL_COMMON_CORE_REFINEMENT_COMPATIBLE=true.
```

---

## 9. The new top-edge receiver

For every top-edge residual triple and switch product retained by `s7-25`, reconstruct the divisor-many physical packet and attach the exact sign allocations

```text
X_ag^-*X_ag^+=oddpart(RJ),
K_ag^-*K_ag^+=oddpart(alpha*delta),                  (9.1)
```

with

```text
X_ag^- | D-A,
X_ag^+ | D+A,
K_ag^- | Q-P,
K_ag^+ | Q+P.                                       (9.2)
```

The remaining receiver is

```text
TopThetaReciprocalLinearAgreementAllocationIncidence. (9.3)
```

Equivalently, the admissible switch set from `s7-25`

```text
A(C,u,v)={X_sw=S*T : a legal physical completion exists}
```

is now tested against four reciprocal linear sign classes and the short dominant cofactors `(c_xi,c_k)`.

A sufficient next theorem is still an average saving

```text
sum_{top-edge (C,u,v)} #A(C,u,v)
 << B^(7/8-delta+o(1))                               (9.4)
```

for some fixed `delta>0`, but the analytic object is no longer a generic binary quartic or a Gaussian `i`-branch incidence.

---

## 10. What is and is not proved

Proved in s7-26:

```text
- both agreement i branches are empty;
- both agreement products have exact ± linear allocation;
- dominant xi agreement modulus exponent is at least phi;
- dominant k agreement modulus exponent is at least 5/16;
- only four dominant sign pairs remain;
- the two dominant linear cofactors have total exponent at most 1/8.
```

Not proved:

```text
- the four sign classes are sparse on average;
- fixed residual triple has B^o(1) admissible X_sw;
- the dominant moduli are determined by the short cofactors;
- a whole-family fixed-power saving below 7/8.
```

Accordingly

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## 11. H / tH decision

No auxiliary H line is needed yet.

The `i` branches disappear before any Gaussian or character-sum estimate is reached.  The surviving receiver is a four-class reciprocal **linear** divisibility problem.  The next step should first test exact divisor/congruence reconstruction inside these four physical sign classes.

Merged `tH17` belongs to the separate signed fixed-U Kummer/rectangle coefficient space and is not cross-promoted.

```text
TH17_CROSS_PROMOTED_TO_S7_26=false
S7_26_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.                 (11.1)
```

If s7-27 leaves a genuine average theorem after the four linear classes have been fully parameterized, then the H request should be formulated directly for `TopThetaReciprocalLinearAgreementAllocationIncidence`, preserving `(C,u,v,X_sw)` and the reciprocal sign allocations.

---

## Stage boundary

```text
STAGE14_S7_26=COMPLETE_COMMON_CORE_AGREEMENT_I_BRANCH_ELIMINATION_AND_TOP_EDGE_LINEAR_ALLOCATION
MERGED_S7_25_IMPORTED=true
MERGED_4CG_PLUS_FACTOR_COPRIMALITY_IMPORTED=true
MERGED_4CL_IMPORTED=true
XI_AGREEMENT_PLUS_FACTOR_ODD_COPRIME=true
K_AGREEMENT_PLUS_FACTOR_ODD_COPRIME=true
XI_AGREEMENT_I_BRANCH_EMPTY=true
K_AGREEMENT_I_BRANCH_EMPTY=true
XI_AGREEMENT_EXACT_TWO_WAY_LINEAR_ALLOCATION=true
K_AGREEMENT_EXACT_TWO_WAY_LINEAR_ALLOCATION=true
HK_MINUS_EXACT_RESIDUAL_CANCELLATION=true
HXI_MINUS_EXACT_RESIDUAL_CANCELLATION=true
TOP_EDGE_XI_DOMINANT_LINEAR_MODULUS_LOWER_EXPONENT=phi
TOP_EDGE_K_DOMINANT_LINEAR_MODULUS_LOWER_EXPONENT=5/16
TOP_EDGE_DOMINANT_LINEAR_BRANCH_TYPE_COUNT=4
TOP_EDGE_XI_DOMINANT_LINEAR_COFACTOR_UPPER_EXPONENT=5/16-phi
TOP_EDGE_K_DOMINANT_LINEAR_COFACTOR_UPPER_EXPONENT=phi-3/16
TOP_EDGE_DOMINANT_LINEAR_COFACTOR_TOTAL_EXPONENT=1/8
MERGED_4CL_COMMON_CORE_REFINEMENT_COMPATIBLE=true
TOP_THETA_RECIPROCAL_LINEAR_AGREEMENT_ALLOCATION_INCIDENCE_REQUIRED=true
TOP_THETA_RECIPROCAL_LINEAR_AGREEMENT_ALLOCATION_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH17_CROSS_PROMOTED_TO_S7_26=false
S7_26_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-27 attack the four reciprocal linear sign classes using the short dominant cofactors before requesting any averaged H theorem
```