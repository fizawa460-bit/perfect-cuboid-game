# Stage14-s7-36 — row/column reoptimization and the 9/16 proportional barrier

## Status

`COMPLETE_ROW_COLUMN_REOPTIMIZATION_AND_9_16_PROPORTIONAL_BARRIER_PROMOTION`

Stage14-s7-36 consumes merged `s7-35` and merged `4cv` on current main.

The entering strongest whole-family theorem is

```text
V(B) << B^(4/7+o(1)).
```

Merged `4cv` independently supplies an exact row/column reconstruction theorem for the same joint common core `J`, but its published `7/12` ledger predates the stronger s7-35 collapse

```text
g_star = H_star^2 * B^o(1).
```

The purpose of s7-36 is to insert that exact collapse into the row/column count without double charging the common core.

The result is:

```text
nonproportional branch: E <= 19/34,
proportional branch:    E <= 9/16.
```

Since

```text
19/34 < 9/16 < 4/7,
```

the whole-family theorem becomes

```text
boxed:
V(B) << B^(9/16+o(1)).
```

Thus the global obstruction changes character.  The row/column nonproportional incidence is no longer the main barrier; the only maximal branch is now the exact proportional relation

```text
L_-=0.
```

No external incidence theorem is used.

---

## 1. Imported exact data

Use the balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Write

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

Merged s7-32/s7-35 retain the complete counts

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4,
E_xi,raw <= 3phi-1/8.
```

The two cross-root cells are

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)),
H=H_S H_T,
gcd(H_S,H_T)=1.
```

Choose the larger cross cell and write

```text
H_star=B^(eta_star+o(1)),
H_other=B^(eta_other+o(1)),
eta_star>=eta_other.
```

Merged s7-35 proves the exact endpoint-small extra-gcd collapse

```text
g_star/H_star^2 | oddpart(omega1*omega2),
omega1*omega2=B^o(1).
```

Hence at exponent scale

```text
boxed:
rho=log_B g_star = 2eta_star+o(1).                 (1.1)
```

Merged s7-34 gives the fourth-power-root complete count

```text
boxed:
E_H <= 3phi-1/8-3eta_star-3eta_other.              (1.2)
```

---

## 2. Import the merged 4cv row/column theorem

Merged 4cv reads one already-charged joint core `J` in two directions.

Let

```text
M=4rsXY epsilon_x epsilon_k,
N=abcd,
```

and

```text
L_-=z1*r2*s2-z2*r1*s1,
L_+=z1*r2*s2+z2*r1*s1.
```

Every odd prime power of `J` has two relative signs:

```text
Cayley row:      M-N versus M+N,
linear column:   L_- versus L_+.
```

Thus

```text
J=J_{--}J_{-+}J_{+-}J_{++}
```

with pairwise-coprime cells.

Define row products

```text
J_C-=J_{--}J_{-+},
J_C+=J_{+-}J_{++},
```

and column products

```text
J_L-=J_{--}J_{+-},
J_L+=J_{-+}J_{++}.
```

Then

```text
J_C- | M-N,
J_C+ | M+N,
J_L- | L_-,
J_L+ | L_+.
```

The same `J` is being partitioned.  Row and column moduli are not independent spacing moduli and are never multiplied as a second copy of the core.

```text
MERGED_4CV_ROW_COLUMN_RECONSTRUCTION_IMPORTED=true.
```

---

## 3. Column reconstruction

On the nonproportional branch

```text
L_-L_+ != 0,
```

write

```text
L_-=J_L- h_-,
L_+=J_L+ h_+.
```

If

```text
J=B^(j+o(1)),
```

then

```text
|h_-h_+|
 = |L_-L_+|/J
 <= B^(1/4-j+o(1)).                                (3.1)
```

The column values reconstruct

```text
z1*r2*s2=(L_++L_-)/2,
z2*r1*s1=(L_+-L_-)/2.
```

Since `r_i,s_i=B^o(1)`, fixing the column cofactors and the already-charged `J` recovers `(z1,z2)` and hence `M` with divisor-many multiplicity.

---

## 4. Cayley row CRT

The row relations give

```text
N == M  (mod J_C-),
N == -M (mod J_C+).
```

Since

```text
gcd(J_C-,J_C+)=1,
J_C-J_C+=J,
```

CRT fixes one residue class

```text
N == N_0 (mod J).
```

Because

```text
N<=B^(1/4+o(1)),
```

the number of lifts is

```text
B^(1/4-j+o(1)).                                    (4.1)
```

Once `N=abcd` is fixed, the signed quotient quadruple is divisor-many.  In particular, `u_res` and `v_res` are not charged separately after this reconstruction.

Combining the two short supports gives the complete row/column count from merged 4cv:

```text
boxed:
E_RC <= 2phi+1/2-2j.                               (4.2)
```

---

## 5. Insert the s7-35 gcd collapse into the joint-core lower bound

Before the coarse `chi-3rho` relaxation, merged 4cu/s7-34 give the exact selected-core lower bound

```text
j >= chi-2rho-2eta_other.                          (5.1)
```

By s7-35,

```text
rho=2eta_star+o(1).
```

Therefore

```text
boxed:
j >= chi-4eta_star-2eta_other-o(1).                (5.2)
```

Insert this into (4.2):

```text
E_RC
 <= 2phi+1/2-2chi
    +8eta_star+4eta_other.                         (5.3)
```

This is the row/column count after the extra residual gcd has been eliminated.

```text
S7_35_EXTRA_GCD_COLLAPSE_INSERTED_INTO_ROW_COLUMN_LEDGER=true.
```

---

## 6. Charged-once cancellation with the fourth-power-root count

Set

```text
A=3phi-1/8,
B=2phi+1/2-2chi.
```

Then

```text
E_H  <= A-3eta_star-3eta_other,
E_RC <= B+8eta_star+4eta_other.
```

These are alternative complete counts for the same physical block, so

```text
E <= min(E_H,E_RC).
```

Use the weighted average

```text
min(E_H,E_RC)
 <= (8E_H+3E_RC)/11.
```

The `eta_star` coefficient cancels exactly:

```text
8*(-3)+3*8=0.
```

The `eta_other` coefficient is favorable:

```text
8*(-3)+3*4=-12.
```

Hence

```text
E
 <= (8A+3B)/11
    -(12/11)eta_other
 <= (8A+3B)/11.                                   (6.1)
```

Substituting

```text
chi=2theta+2phi-3/4
```

gives

```text
boxed:
E_nonprop
 <= (18phi-12theta+5)/11.                          (6.2)
```

No common-core orientation is charged twice: the same `J` appears only through the one row/column reconstruction count.

---

## 7. Exact nonproportional minimax

Combine

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4,
E_xi,raw <= 3phi-1/8,
E_RC/H <= (18phi-12theta+5)/11.
```

Since `phi<=1/4`, the last term satisfies

```text
E_RC/H <= 19/22-(12/11)theta.                      (7.1)
```

In the active region `theta>1/4`,

```text
E_s=2theta.
```

The two active envelopes meet at

```text
2theta=19/22-(12/11)theta,
```

so

```text
boxed:
theta=19/68,
E=19/34.                                           (7.2)
```

The exact whole-strip Fraction audit confirms

```text
boxed:
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34. (7.3)
```

The equality point of this nonproportional envelope is unique:

```text
boxed:
theta=19/68,
phi=1/4,
chi=21/68.                                         (7.4)
```

At equality the weighted cancellation also forces

```text
eta_other=0,
eta_star=3/136,
rho=3/68,
j=15/68.                                          (7.5)
```

Therefore both row/column short supports have exponent

```text
1/4-j=1/34.                                        (7.6)
```

Thus

```text
NONPROPORTIONAL_SATURATION_THETA=19/68
NONPROPORTIONAL_SATURATION_PHI=1/4
NONPROPORTIONAL_JOINT_CORE_EXPONENT=15/68
NONPROPORTIONAL_TWIN_SHORT_SUPPORT_EXPONENT=1/34.
```

This entire branch lies strictly below `9/16` because

```text
9/16-19/34=1/272.                                  (7.7)
```

---

## 8. Proportional branch becomes the global barrier

The row/column argument above requires

```text
L_-L_+ != 0.
```

Positivity makes `L_+>0`, so the complementary branch is exactly

```text
boxed:
L_-=0.                                             (8.1)
```

Equivalently,

```text
z1*r2*s2=z2*r1*s1.                                 (8.2)
```

Reduce the endpoint-small ratio and write

```text
r1*s1:r2*s2 = a:b,
gcd(a,b)=1,
a,b=B^o(1).
```

Then

```text
z1=a*t,
z2=b*t,
t=B^(1/8+o(1)).                                    (8.3)
```

Merged 4cu proves that this full common integer scale survives the k switched Gaussian square descent.  Thus the k one-host count gains `1/8`:

```text
boxed:
E_k,prop <= 3theta-3/8.                             (8.4)
```

Together with the unchanged complete counts,

```text
E_prop
 <= min(
      max(2theta,1-2theta),
      3phi-1/8,
      3theta-3/8
    ).                                             (8.5)
```

The exact strip audit gives

```text
boxed:
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16.      (8.6)
```

Equality requires

```text
boxed:
theta=5/16,
11/48<=phi<=1/4.                                   (8.7)
```

Correspondingly

```text
1/3<=chi<=3/8.                                     (8.8)
```

Thus after the nonproportional row/column collapse the former subcritical proportional branch becomes the unique global type of saturation, although it occupies a phi interval rather than a single point.

---

## 9. Whole-family promotion

Every physical packet is either nonproportional or proportional. Therefore

```text
E
 <= max(19/34,9/16)
 = 9/16.
```

Hence

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16
IMPROVEMENT_OVER_PREVIOUS_4_7=1/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

The remaining gap to the square-root scale is

```text
boxed:
CURRENT_GAP_TO_SQRT=1/16.                          (9.1)
```

This is the smallest Stage14 whole-family gap reached by the s-route so far.

---

## 10. New minimal receiver

The old s7-35 receiver

```text
FourSeventhsSingleCrossRootFullJointCoreLinearProductIncidence
```

is no longer minimal.  The nonproportional row/column branch is already at `19/34`.

Any `9/16` saturation packet must instead satisfy

```text
L_-=0,
theta=5/16,
11/48<=phi<=1/4,
z1*r2*s2=z2*r1*s1,
z1=a*t,
z2=b*t,
a,b=B^o(1),
t=B^(1/8+o(1)),
t | gcd(Re W_beta,Im W_beta),
t | gcd(Re W_gamma,Im W_gamma),
q_k=t^2*q_k0,
q_k<=B^(1/2+o(1)),
q_k0<=B^(1/4+o(1)).                                (10.1)
```

Define the new receiver

```text
NineSixteenthsProportionalCommonZScaleKGaussianResidualIncidence.       (10.2)
```

The key unresolved structure is no longer an averaged row/column incidence. It is the primewise anatomy of the large common z-scale `t` inside the two physical root states and the two equal-residual k Gaussian hosts.

---

## 11. H / tH decision

No auxiliary H/tH theorem is needed at s7-36.

The new `9/16` obstruction still has unused exact arithmetic.  Primewise, the odd part of

```text
t=gcd(z1,z2)
```

can be decomposed according to whether a prime is shared by

```text
x1,x2;
y1,y2;
x1,y2;
y1,x2.
```

The last two are the already-known cross cells `H_T,H_S`; the first two are same-side common-root cells not yet isolated in the proportional branch.  That decomposition should be exhausted before asking for an averaged incidence theorem.

Therefore

```text
S7_36_AUXILIARY_H_NEEDED=false
TH20_CROSS_PROMOTED_TO_S7_36=false
T74_CROSS_PROMOTED_TO_S7_36=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

---

## 12. Next stage

`Stage14-s7-37` should attack the proportional receiver directly.

Primewise decompose

```text
oddpart(t)
```

into four pairwise-coprime root-gcd cells

```text
K_x = oddpart(gcd(x1,x2)),
K_y = oddpart(gcd(y1,y2)),
H_T = oddpart(gcd(x1,y2)),
H_S = oddpart(gcd(y1,x2)).
```

The first target is the exact identity, with valuations checked prime by prime,

```text
oddpart(t)=K_x*K_y*H_S*H_T,
```

followed by transfer of the same-side factors `K_x,K_y` into the two equal-residual xi/k Gaussian hosts.  Determine whether a positive-power same-side factor is forced whenever `t=B^(1/8)` but `H=B^o(1)`.

Do not invoke H before this decomposition is exhausted.

---

## Stage boundary

```text
STAGE14_S7_36=COMPLETE_ROW_COLUMN_REOPTIMIZATION_AND_9_16_PROPORTIONAL_BARRIER_PROMOTION
MERGED_S7_35_IMPORTED=true
MERGED_4CV_ROW_COLUMN_RECONSTRUCTION_IMPORTED=true
S7_35_EXTRA_GCD_COLLAPSE_INSERTED_INTO_ROW_COLUMN_LEDGER=true
ROW_COLUMN_COMMON_CORE_DOUBLE_CHARGED=false
NONPROPORTIONAL_WEIGHTED_COMPLETE_COUNT_COMBINATION=8:3
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
NONPROPORTIONAL_SATURATION_THETA=19/68
NONPROPORTIONAL_SATURATION_PHI=1/4
NONPROPORTIONAL_SATURATION_COMMON_CORE_EXPONENT=21/68
NONPROPORTIONAL_SATURATION_SELECTED_CROSS_ROOT_EXPONENT=3/136
NONPROPORTIONAL_SATURATION_SELECTED_XI_GCD_EXPONENT=3/68
NONPROPORTIONAL_SATURATION_JOINT_CORE_EXPONENT=15/68
NONPROPORTIONAL_TWIN_SHORT_SUPPORT_EXPONENT=1/34
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
PROPORTIONAL_SATURATION_THETA=5/16
PROPORTIONAL_SATURATION_PHI_RANGE=[11/48,1/4]
PROPORTIONAL_SATURATION_COMMON_CORE_EXPONENT_RANGE=[1/3,3/8]
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16
IMPROVEMENT_OVER_PREVIOUS_4_7=1/112
CURRENT_GAP_TO_SQRT=1/16
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
REMAINING_RECEIVER=NineSixteenthsProportionalCommonZScaleKGaussianResidualIncidence
S7_36_AUXILIARY_H_NEEDED=false
TH20_CROSS_PROMOTED_TO_S7_36=false
T74_CROSS_PROMOTED_TO_S7_36=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-37
```