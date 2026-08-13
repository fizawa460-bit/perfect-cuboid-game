# Stage14-s7-35 — extra xi residual gcd collapse and the 4/7 bound

## Status

`COMPLETE_EXTRA_XI_RESIDUAL_GCD_COLLAPSE_AND_4_7_PROMOTION`

Stage14-s7-35 consumes merged `s7-34` on current main.  The predecessor theorem is

```text
V(B) << B^(47/80+o(1)),
```

with possible equality only at

```text
theta=47/160,
phi=1/4,
chi=27/80,
H=B^(1/80+o(1)),
g_star=B^(3/80+o(1)),
J_star=B^(1/4+o(1)).
```

The characteristic obstruction was an apparent fixed-power residual coordinate-gcd factor

```text
G_extra = g_star/H_star^2 = B^(1/40+o(1)).
```

The new exact point is that such a moving fixed-power factor cannot exist.  For either xi switched host, after removing the forced cross-root square, every further odd rational coordinate-gcd prime is supplied by the endpoint-small factors `omega_1,omega_2`.  Hence

```text
g_S/H_S^2 | oddpart(omega_1*omega_2),
g_T/H_T^2 | oddpart(omega_1*omega_2).
```

Since `omega_i=B^o(1)`, one has at exponent scale

```text
g_S=H_S^2*B^o(1),
g_T=H_T^2*B^o(1).
```

Thus the `1/40` extra-gcd saturation branch of s7-34 is impossible.

Combining this exact support collapse with the s7-34 fourth-power theorem

```text
H^4 | q_xi
```

and the exact pre-relaxation 4cu joint-core inequality improves the forced xi saving from

```text
3(chi-1/4)/7
```

to

```text
3(chi-1/4)/4.
```

Exact strip minimax then gives

```text
boxed:
V(B) << B^(4/7+o(1)).
```

Therefore

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=4/7
IMPROVEMENT_OVER_PREVIOUS_47_80=9/560
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

No external sieve, determinant method, genus-one theorem, or H/tH input is used.

---

## 1. Imported switched xi hosts

Use

```text
Z_S
 = R*x_2^2*omega_1
   + i*J*y_1^2*omega_2
 = lambda_S^2 W_S,

Z_T
 = J*y_2^2*omega_1
   + i*R*x_1^2*omega_2
 = lambda_T^2 W_T,
```

with

```text
N(lambda_S)=oddpart(S),
N(lambda_T)=oddpart(T),

oddpart(N(W_S))
 =oddpart(N(W_T))
 =q_xi.
```

Define the two cross-root cells

```text
H_S=oddpart(gcd(x_2,y_1)),
H_T=oddpart(gcd(x_1,y_2)),
H=H_S H_T,
gcd(H_S,H_T)=1.
```

Merged 4cu/s7-34 prove

```text
H_S^2 | g_S,
H_T^2 | g_T,

g_S=oddpart(gcd(Re W_S,Im W_S)),
g_T=oddpart(gcd(Re W_T,Im W_T)),

H^4 | q_xi.
```

The endpoint-small factors are

```text
omega_i=g_i*r_i*s_i=B^o(1).
```

---

## 2. Residual coordinate gcd is coprime to its switched cell

We prove first

```text
boxed:
gcd(g_S,S)=1,
gcd(g_T,T)=1.                                      (2.1)
```

Consider an odd prime `p|S`.  Pairwise coprimality of the xi cells gives

```text
p∤R*J*T.
```

Statewise reducedness gives more.  Since

```text
P_1=RS*x_1^2,
Q_1=TJ*y_1^2,
gcd(P_1,Q_1)=1,
```

we have

```text
p∤y_1.
```

And since

```text
P_2=RT*x_2^2,
Q_2=SJ*y_2^2,
gcd(P_2,Q_2)=1,
```

we have

```text
p∤x_2.
```

The k-square roots entering `omega_1,omega_2` are also p-units.  Indeed `p` lies in the xi support, while `gcd(k,xi)=1`; more elementarily, in state 1 one has `p|P_1`, `p∤Q_1`, so neither `Q_1-P_1` nor `Q_1+P_1` is divisible by `p`, and the same argument applies in state 2 with `p|Q_2`, `p∤P_2`.

Therefore both integer coordinates of `Z_S` are p-units:

```text
p∤Re Z_S,
p∤Im Z_S.                                         (2.2)
```

If `p|g_S`, then the rational Gaussian integer `p` divides `W_S`, hence also

```text
Z_S=lambda_S^2 W_S,
```

contradicting (2.2).  Thus `p∤g_S`.  The T-host proof is symmetric.

Hence

```text
XI_RESIDUAL_GCD_COPRIME_TO_SWITCH_CELL=true.
```

---

## 3. Square descent does not change the odd rational gcd away from the cell

Fix an odd prime `p|g_S`.  By Section 2,

```text
p∤S=N(lambda_S).
```

Multiplication by the Gaussian integer `lambda_S^2` is therefore an invertible `2x2` linear transformation over `Z/p^e Z` for every `e>=1`.  Consequently

```text
p^e | Re W_S, Im W_S
<=>
p^e | Re Z_S, Im Z_S.                             (3.1)
```

Prime by prime,

```text
boxed:
g_S
 =oddpart(gcd(Re Z_S,Im Z_S)).                    (3.2)
```

Likewise

```text
g_T
 =oddpart(gcd(Re Z_T,Im Z_T)).                    (3.3)
```

Therefore

```text
XI_RESIDUAL_GCD_EQUALS_RAW_HOST_ODD_GCD=true.
```

This eliminates the possibility that Gaussian square descent itself creates a new fixed-power rational coordinate gcd.

---

## 4. Remove the forced cross-root square

Write

```text
x_2=H_S*x_2',
y_1=H_S*y_1'
```

in odd parts.  By definition

```text
gcd(x_2',y_1')=1
```

at odd primes.

The S-host coordinates become

```text
Re Z_S
 =H_S^2 * R*x_2'^2*omega_1,

Im Z_S
 =H_S^2 * J*y_1'^2*omega_2.                       (4.1)
```

We claim

```text
boxed:
oddpart(gcd(R*x_2'^2,J*y_1'^2))=1.                 (4.2)
```

Indeed:

- `gcd(R,J)=1` by the xi cell decomposition;
- `gcd(R,y_1)=1` follows from reducedness of state 1;
- `gcd(J,x_2)=1` follows from reducedness of state 2;
- `gcd(x_2',y_1')=1` by construction.

Thus every odd prime remaining in the gcd of the two coordinates in (4.1) must be supplied by at least one of the endpoint factors `omega_1,omega_2`.

The elementary valuation inequality for coprime `A,B`,

```text
gcd(A*u,B*v) | u*v,
```

gives

```text
boxed:
g_S/H_S^2
 | oddpart(omega_1*omega_2).                       (4.3)
```

The symmetric T-host factorization gives

```text
boxed:
g_T/H_T^2
 | oddpart(omega_1*omega_2).                       (4.4)
```

Hence

```text
XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true.
```

Since

```text
omega_1*omega_2=B^o(1),
```

we conclude uniformly

```text
boxed:
g_S=H_S^2*B^o(1),
g_T=H_T^2*B^o(1).                                  (4.5)
```

In particular

```text
XI_EXTRA_GCD_FIXED_POWER_SUPPORT=false.
```

The s7-34 `G_extra=B^(1/40)` equality branch is therefore eliminated exactly.

---

## 5. Exponent consequence for the selected host

Choose `star in {S,T}` with

```text
H_star>=H_other
```

at exponent scale and write

```text
H_star=B^(eta_star+o(1)),
H_other=B^(eta_other+o(1)),
H=B^(eta+o(1)),
g_star=B^(rho+o(1)).
```

Then

```text
eta=eta_star+eta_other,
eta_star>=eta_other.
```

Section 4 gives the new exponent identity

```text
boxed:
rho=2eta_star.                                     (5.1)
```

The `B^o(1)` endpoint factor is absorbed in the `o(1)` term.

This is strictly stronger than the predecessor inequality

```text
rho>=2eta_star.
```

The predecessor's apparent extra coordinate-gcd degree of freedom is gone.

---

## 6. Joint-core pressure forces H itself

Merged s7-34 retains the exact pre-relaxation joint-core lower bound

```text
J_star
 >= B^(chi-2rho-2eta_other-o(1)).                  (6.1)
```

On the nonproportional branch,

```text
J_star | L_-L_+,
|L_-L_+|<=B^(1/4+o(1)).                            (6.2)
```

Therefore, with

```text
d=max(0,chi-1/4),
```

we have

```text
d
 <=2rho+2eta_other.                                (6.3)
```

Insert `rho=2eta_star`:

```text
d
 <=4eta_star+2eta_other
 <=4(eta_star+eta_other)
 =4eta.                                             (6.4)
```

Hence

```text
boxed:
eta >= (chi-1/4)/4                                 (6.5)
```

whenever `chi>1/4`.

Thus

```text
NONPROPORTIONAL_FORCED_H_EXPONENT=(chi-1/4)/4.
```

---

## 7. Fourth-power one-host count gives a 3d/4 saving

Merged s7-34 proves the complete xi one-host count

```text
E_xi,H
 <=3phi-1/8-3eta.                                  (7.1)
```

Using Section 6,

```text
boxed:
E_xi
 <=3phi-1/8
   -3(chi-1/4)/4                                   (7.2)
```

for `chi>1/4`.

Therefore

```text
NONPROPORTIONAL_FORCED_SAVING=3*(chi-1/4)/4.
```

This improves the s7-34 coefficient from `3/7` to `3/4` without multiplying two savings: only the complete H-count is used after exact arithmetic forces the size of H.

---

## 8. Exact whole-strip minimax

For `chi<=1/4`, merged s7-34 already gives

```text
E<=11/20.                                          (8.1)
```

For `chi>1/4`, compare the complete counts

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4,
E_xi<=3phi-1/8-3(chi-1/4)/4.                       (8.2)
```

The relevant maximizer has `theta>1/4`, so

```text
E_s=2theta.
```

Using

```text
chi=2theta+2phi-3/4
```

and maximizing in `phi<=1/4` gives

```text
E_xi
 <=1-(3/2)theta.                                   (8.3)
```

The two active envelopes meet when

```text
2theta=1-(3/2)theta,
```

hence

```text
boxed:
theta=2/7,
E=4/7.                                             (8.4)
```

Exact rational enumeration of the entire balanced strip confirms that the unique maximum of the proved nonproportional envelope is

```text
boxed:
theta=2/7,
phi=1/4,
chi=9/28,
E=4/7.                                             (8.5)
```

At that point

```text
E_k=17/28>4/7.
```

Merged 4cu's proportional branch remains

```text
E_prop<=9/16<4/7,                                  (8.6)
```

and the low-core region satisfies

```text
11/20<4/7.                                         (8.7)
```

Therefore

```text
boxed:
V(B) << B^(4/7+o(1)).                              (8.8)
```

The gain over merged s7-34 is

```text
47/80-4/7=9/560.                                   (8.9)
```

---

## 9. Equality profile at 4/7

At

```text
(theta,phi,chi)=(2/7,1/4,9/28),
```

we have

```text
d=chi-1/4=1/14.                                   (9.1)
```

For equality in

```text
d<=4eta_star+2eta_other<=4eta,
```

one must have

```text
boxed:
eta_other=0,
eta_star=eta=1/56.                                 (9.2)
```

Thus all fixed-power common-root support lies in a single cross cell:

```text
H_star=B^(1/56+o(1)),
H_other=B^o(1).                                    (9.3)
```

Section 5 then gives

```text
g_star=B^(1/28+o(1)).                              (9.4)
```

The joint core exponent is

```text
chi-2rho-2eta_other
 =9/28-2/28
 =1/4.                                             (9.5)
```

Hence

```text
J_star=B^(1/4+o(1)).                               (9.6)
```

Since simultaneously

```text
J_star|L_-L_+,
|L_-L_+|<=B^(1/4+o(1)),
```

the complementary integer cofactor is only divisor-size:

```text
boxed:
|L_-L_+|/J_star=B^o(1).                            (9.7)
```

Thus

```text
FOUR_SEVENTHS_LINEAR_PRODUCT_COFACTOR_EXPONENT=0.
```

The former fixed-power `G_extra` has disappeared entirely.  The new saturation packet instead has a **single cross-root cell** and a **full endpoint linear-product joint core**.

---

## 10. New minimal receiver

Define

```text
FourSeventhsSingleCrossRootFullJointCoreLinearProductIncidence.
```

Any packet saturating the proved `4/7` envelope must satisfy

```text
(theta,phi)=(2/7,1/4),
C=B^(9/28+o(1)),

H_star=B^(1/56+o(1)),
H_other=B^o(1),
H=B^(1/56+o(1)),

g_star=H_star^2*B^o(1)=B^(1/28+o(1)),

J_star=B^(1/4+o(1)),
J_star|L_-L_+,
|L_-L_+|/J_star=B^o(1).
```

This receiver is strictly narrower than the s7-34 extra-gcd receiver because there is no fixed-power residual coordinate-gcd support left outside the single forced root square.

The next exact leverage is therefore not a sieve theorem.  It is the factorization of the essentially full joint core between the two endpoint linear signs `L_-` and `L_+`, together with the already-existing Cayley same/opposite row allocation.

---

## 11. Relation to open parallel 4cv

At the time this stage is cut, PR #540 (`Stage14-4cv`) is still open/draft and is not used as a canonical theorem source.

Its row/column cofactor idea is compatible with the new receiver, but s7-35 proves its `4/7` theorem independently from merged main only.  No unmerged `7/12` claim is imported.

```text
OPEN_4CV_USED_AS_CANONICAL_SOURCE=false.
```

If 4cv merges before s7-36, its row/column reconstruction may be imported only after checking it against the stronger `4/7` saturation profile above.

---

## 12. H / tH decision

No auxiliary H/tH theorem is needed at s7-35.

The obstruction is again exact and finite-dimensional: at possible saturation the endpoint product cofactor is only `B^o(1)`, so the next task is to split the full joint core across `L_-` and `L_+` and compare that column allocation with the Cayley row allocation.

Therefore

```text
S7_35_AUXILIARY_H_NEEDED=false
TH18_CROSS_PROMOTED_TO_S7_35=false
T72_CROSS_PROMOTED_TO_S7_35=false
T73_CROSS_PROMOTED_TO_S7_35=false
T74_CROSS_PROMOTED_TO_S7_35=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

A new s-specific H target should be considered only if the full-joint-core row/column reconstruction leaves a genuine positive-dimensional averaged incidence after s7-36.

---

## 13. Next stage

`Stage14-s7-36` should start from

```text
J_star=B^(1/4+o(1)),
J_star|L_-L_+,
|L_-L_+|/J_star=B^o(1),
```

and the unique single-cross-root profile

```text
H_star=B^(1/56+o(1)),
H_other=B^o(1).
```

The first task is to write the primewise joint core as the `2x2` row/column sign partition induced by

```text
C_-/C_+
```

and

```text
L_-/L_+,
```

then determine whether the two column factors plus `B^o(1)` cofactors reconstruct `(z_1,z_2)` and whether the Cayley row CRT reconstructs the remaining signed-quotient product without a new fixed-power lift.

Do not invoke H before that exact reconstruction is exhausted.

---

## Stage boundary

```text
STAGE14_S7_35=COMPLETE_EXTRA_XI_RESIDUAL_GCD_COLLAPSE_AND_4_7_PROMOTION
MERGED_S7_34_IMPORTED=true
MERGED_4CU_STRUCTURE_RETAINED=true
XI_RESIDUAL_GCD_COPRIME_TO_SWITCH_CELL=true
XI_RESIDUAL_GCD_EQUALS_RAW_HOST_ODD_GCD=true
XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true
XI_EXTRA_GCD_FIXED_POWER_SUPPORT=false
SELECTED_XI_GCD_EXPONENT=2eta_star
NONPROPORTIONAL_FORCED_H_EXPONENT=(chi-1/4)/4
NONPROPORTIONAL_FORCED_SAVING=3*(chi-1/4)/4
LOW_CORE_REGION_UPPER_BOUND_EXPONENT=11/20
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=4/7
IMPROVEMENT_OVER_PREVIOUS_47_80=9/560
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
FOUR_SEVENTHS_SATURATION_THETA=2/7
FOUR_SEVENTHS_SATURATION_PHI=1/4
FOUR_SEVENTHS_SATURATION_COMMON_CORE_EXPONENT=9/28
FOUR_SEVENTHS_SINGLE_CROSS_ROOT_EXPONENT=1/56
FOUR_SEVENTHS_OTHER_CROSS_ROOT_EXPONENT=0
FOUR_SEVENTHS_SELECTED_XI_GCD_EXPONENT=1/28
FOUR_SEVENTHS_JOINT_CORE_EXPONENT=1/4
FOUR_SEVENTHS_LINEAR_PRODUCT_COFACTOR_EXPONENT=0
REMAINING_RECEIVER=FourSeventhsSingleCrossRootFullJointCoreLinearProductIncidence
OPEN_4CV_USED_AS_CANONICAL_SOURCE=false
S7_35_AUXILIARY_H_NEEDED=false
TH18_CROSS_PROMOTED_TO_S7_35=false
T72_CROSS_PROMOTED_TO_S7_35=false
T73_CROSS_PROMOTED_TO_S7_35=false
T74_CROSS_PROMOTED_TO_S7_35=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-36
```