# Stage14-s7-39 — Cayley/residual fixed-power disjointness, square-root lost-core transfer, and the 17/32 bound

## Status

`COMPLETE_CAYLEY_RESIDUAL_DISJOINTNESS_SQUARE_ROOT_LOST_CORE_AND_17_32_PROMOTION`

Stage14-s7-39 consumes merged `s7-38`, merged `4cw`, merged `X12`, merged `s7-37`, and the exact Cayley-good-core unit statement of merged `4cr/4cs`.

The entering canonical whole-family theorem is

```text
V(B) << B^(61/112+o(1)).
```

The decisive observation is that the positive fixed-power annulus left in the `s7-38/4cw` equality ledger cannot actually survive the already-merged Cayley unit condition.

Merged `4cr` proves for its Cayley-good core that

```text
gcd(C_Cayley, M*N)=1,
```

while merged `4cs` identifies the common odd opposite-quotient gcd with the common root gcd

```text
H=oddpart(gcd(c,d))=oddpart(gcd(X,Y)).
```

Since

```text
N=a*b*c*d,
```

every prime of `H` divides `N`. Hence

```text
boxed:
gcd(C_Cayley,H)=1.                                (0.1)
```

Merged `s7-35` proves for the selected residual host

```text
g_star/H_star^2 | oddpart(omega1*omega2),
omega1*omega2=B^o(1),
H_star|H.
```

Therefore the fixed-power support removed by residual primitivity is disjoint from the Cayley-good core. Consequently

```text
boxed:
C_Cayley/J = B^o(1),
J=C_Cayley*B^o(1).                                (0.2)
```

This collapses the former Cayley-only annulus.

Moreover the lost core is now only the Cayley gcd-square bad support, so after endpoint-small decoration is removed,

```text
D0 | H^2,
D:=C/J.
```

Its square-root divisor, rather than merely the X12 fourth-root divisor, lies in the common physical root gcd and therefore in the endpoint-linear column. This strengthens the whole-family theorem to

```text
boxed:
V(B) << B^(17/32+o(1)).
```

No external sieve, determinant theorem, genus-one theorem, H, or tH theorem is used.

---

## 1. Imported notation

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

The two cross-root cells are

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)),
H=H_S*H_T,
gcd(H_S,H_T)=1.
```

Dyadically write

```text
H=B^(s_H+o(1)).                                    (1.1)
```

Merged `s7-34` supplies the fourth-power complete count

```text
boxed:
E_H <= 3phi-1/8-3s_H.                             (1.2)
```

The standard complete bounds retained throughout are

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.                                 (1.3)
```

Merged `s7-37` gives the proportional branch

```text
E_prop <= 7/16.                                    (1.4)
```

Thus only the nonproportional branch remains relevant above square-root scale.

---

## 2. The Cayley-good core is coprime to the common root gcd

Use the merged `4cr` Cayley-good core, denoted here by

```text
C_Cayley | C.
```

The exact unit check in `4cr` gives

```text
boxed:
gcd(C_Cayley,M*N)=1,                              (2.1)
```

where

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k,
N=a*b*c*d.
```

Merged `4cs` proves

```text
oddpart(gcd(c,d))=H.                               (2.2)
```

Hence every odd prime of `H` divides both `c` and `d`, and therefore divides `N`. Combining (2.1) and (2.2),

```text
boxed:
gcd(C_Cayley,H)=1.                                (2.3)
```

This is an exact support statement, not merely an exponent inequality.

The finite 2-primary decoration is separated throughout and costs `B^o(1)`.

---

## 3. Residual bad support is disjoint from the Cayley-good core

For the selected switched xi residual host, merged `s7-35` proves exactly

```text
g_star/H_star^2 | oddpart(omega1*omega2),          (3.1)
```

with

```text
H_star | H,
omega1*omega2=B^o(1).                             (3.2)
```

Therefore every odd prime of `g_star` outside the endpoint-small decoration lies in `H_star`, hence in `H`.

By (2.3),

```text
gcd(C_Cayley,g_star) | B^o(1),
```

and therefore

```text
boxed:
gcd(C_Cayley,g_star^2)=B^o(1).                    (3.3)
```

Merged `4cu/X12` define

```text
C_res = C/gcd(C,g_star^2),
J     = gcd(C_Cayley,C_res).                       (3.4)
```

For any divisors `A|C` and `G|C`, with `B=C/G`, one has

```text
A/gcd(A,B) | gcd(A,G).                             (3.5)
```

Apply (3.5) with

```text
A=C_Cayley,
G=gcd(C,g_star^2),
B=C_res.
```

Then (3.3) gives

```text
boxed:
C_Cayley/J = B^o(1).                               (3.6)
```

Equivalently, at fixed-power scale,

```text
boxed:
J=C_Cayley.                                        (3.7)
```

Thus the positive annulus

```text
A_C=C_Cayley/J
```

which was still allowed by the coarse `s7-38/4cw` exponent inequalities is not a genuine physical fixed-power degree of freedom.

```text
CAYLEY_RESIDUAL_FIXED_POWER_INTERSECTION_TRIVIAL=true.
CAYLEY_ONLY_ANNULUS_FIXED_POWER_EXPONENT=0.
```

---

## 4. The lost core is supported on the square of the full root gcd

Merged `4cq/4cr/4cs` obtain the Cayley-good core by two gcd-square peels. The first coordinate gcd is endpoint-small; the second odd coordinate gcd is exactly `H` by `4cs`.

Therefore there is an endpoint-small integer

```text
Omega=B^o(1)
```

such that

```text
boxed:
C/C_Cayley | Omega*H^2.                            (4.1)
```

By (3.6), replacing `C_Cayley` by `J` changes only endpoint-small support. Put

```text
D:=C/J.                                             (4.2)
```

Then

```text
D | Omega'*H^2,
Omega'=B^o(1).                                      (4.3)
```

Remove the harmless overlap by

```text
D0 := D/gcd(D,Omega').                              (4.4)
```

Prime by prime,

```text
boxed:
D0 | H^2.                                           (4.5)
```

Define the square-root envelope

```text
R2(D0):=prod_p p^ceil(v_p(D0)/2).                  (4.6)
```

From (4.5),

```text
boxed:
R2(D0) | H,                                         (4.7)
```

and trivially

```text
boxed:
R2(D0) >= D0^(1/2).                                 (4.8)
```

This is the square-root upgrade of the X12 fourth-root lost-core divisor.

```text
LOST_CORE_SQUARE_ROOT_DIVISOR_PROVED=true.
```

---

## 5. The square-root lost-core divisor enters the column cofactor product

Merged X12 proves the exact physical placement

```text
H | gcd(L_-,L_+),                                  (5.1)
```

where

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
J_L-*J_L+=J,
gcd(J_L-,J_L+)=1.                                 (5.2)
```

By (4.7), `R2(D0)` divides both `L_-` and `L_+`.

At each prime power of `R2(D0)`, at most one of the coprime column moduli `J_L-`,`J_L+` can absorb that prime. The opposite column cofactor retains the full required prime power. Hence

```text
boxed:
R2(D0) | h_-*h_+.                                  (5.3)
```

This argument uses the same charged column modulus `J`; no product `J*H` is introduced.

If

```text
J=B^(j+o(1)),
```

then

```text
D=B^(chi-j+o(1)),
R2(D0)>=B^((chi-j)/2-o(1)).                        (5.4)
```

The raw column cofactor product has support

```text
1/4-j.
```

After the forced square-root divisor is removed, its effective support is

```text
boxed:
ell_col
 <= max(0,1/4-j-(chi-j)/2).                        (5.5)
```

This replaces the X12/4cw fourth-root subtraction `(chi-j)/4` by `(chi-j)/2`.

---

## 6. Strengthened joint-core lower bound

Since `J=C_Cayley` at fixed-power scale and (4.1) removes at most the full root-gcd square,

```text
boxed:
j >= chi-2s_H.                                     (6.1)
```

Put

```text
d:=chi-1/4=2theta+2phi-1.                          (6.2)
```

From (5.5) and (6.1),

```text
ell_col
 <= max(0,s_H-d).                                  (6.3)
```

The full Cayley row is now the same fixed-power modulus as the column joint core. After the column reconstructs `M`, the Cayley CRT reconstructs

```text
N=N0+J*h_N,
```

so

```text
boxed:
ell_row
 <= max(0,1/4-j)
 <= max(0,2s_H-d).                                 (6.4)
```

Thus the new complete row/column count is

```text
boxed:
E_SRC
 <=2phi
   +max(0,s_H-d)
   +max(0,2s_H-d).                                 (6.5)
```

It is an alternative complete count of the same physical block as (1.2).

---

## 7. Uniform `17/32` minimax

We prove every physical block is at most `17/32`.

### 7.1. `theta<=1/4`

From (1.3),

```text
E<=E_k<=3theta-1/4<=1/2<17/32.                    (7.1)
```

### 7.2. `1/4<=theta<=17/64`

Here

```text
E<=E_s=2theta<=17/32.                              (7.2)
```

It remains to treat

```text
theta>=17/64.                                      (7.3)
```

### 7.3. Low-core region `d<=0`

For `s_H>=0`, both positive parts in (6.5) are active, so

```text
E_SRC<=2phi+3s_H-2d.
```

Average this with (1.2):

```text
min(E_H,E_SRC)
 <=(E_H+E_SRC)/2
 <=phi/2-2theta+15/16.                             (7.4)
```

Using `phi<=1/4` and (7.3),

```text
E<=17/16-2theta<=17/32.                            (7.5)
```

### 7.4. High-core region `d>0`

Because `J|L_-L_+` on the nonproportional branch and

```text
0<|L_-L_+|<=B^(1/4+o(1)),
```

we have `j<=1/4`. Combining with (6.1),

```text
s_H>=d/2.                                          (7.6)
```

#### Case A: `d/2<=s_H<=d`

Then

```text
E_SRC<=2phi+2s_H-d.
```

Use the weighted minimum

```text
min(E_H,E_SRC)<=(2E_H+3E_SRC)/5.
```

The `s_H` terms cancel:

```text
2*(-3)+3*2=0.
```

Hence

```text
E
 <=(12phi-1/4-3d)/5
 =6(phi-theta)/5+11/20
 <=17/20-6theta/5.                                 (7.7)
```

Under (7.3), the final expression is at most `17/32`.

#### Case B: `s_H>=d`

Now

```text
E_SRC<=2phi+3s_H-2d.
```

The equal-weight average cancels `s_H`:

```text
min(E_H,E_SRC)
 <=(E_H+E_SRC)/2
 <=phi/2-2theta+15/16
 <=17/32.                                          (7.8)
```

All balanced nonproportional blocks are covered. Together with (1.4),

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=17/32.       (7.9)
```

The gain over merged `61/112` is

```text
61/112-17/32=3/224.                                (7.10)
```

The remaining gap to square-root scale is

```text
17/32-1/2=1/32.                                    (7.11)
```

Thus

```text
IMPROVEMENT_OVER_PREVIOUS_61_112=3/224
CURRENT_GAP_TO_SQRT=1/32
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

---

## 8. Equality profile

Equality in the proved envelope is possible only when

```text
boxed:
theta=17/64,
phi=1/4.                                           (8.1)
```

Then

```text
chi=9/32,
d=1/32.                                           (8.2)
```

The two high-core cases meet at

```text
boxed:
s_H=1/32.                                         (8.3)
```

Equality in (6.1) gives

```text
boxed:
j=7/32.                                           (8.4)
```

Hence the lost core and the two short supports are

```text
D=C/J:                         B^(1/16+o(1)),
R2(D0):                        B^(1/32+o(1)),
raw column cofactor support:   B^(1/32+o(1)),
effective column support:      B^o(1),
row CRT lift support:          B^(1/32+o(1)).       (8.5)
```

Thus at possible saturation the column is already divisor-many; only one fixed-power row-lift coordinate remains.

The split

```text
s_H=eta_star+eta_other=1/32
```

need not be uniquely distributed between the two cross cells at this stage.

---

## 9. New receiver

The remaining minimal receiver is

```text
SeventeenThirtySecondsCayleyResidualDisjointSquareRootLostCoreSingleRowLiftIncidence.
```

Its potential equality packet carries

```text
theta=17/64,
phi=1/4,
chi=9/32,
H=B^(1/32+o(1)),
J=C_Cayley=B^(7/32+o(1)),
C/J=B^(1/16+o(1)),
R2(D0)=B^(1/32+o(1)),
effective column cofactor multiplicity=B^o(1),
row lift h_N<=B^(1/32+o(1)).
```

The next exact task is to substitute the now divisor-many reconstructed column `(L_-,L_+)`, hence `M`, into the signed reciprocal identities and determine whether the remaining `h_N` is fixed modulo a root-gcd or signed-quotient modulus larger than its `B^(1/32)` range.

---

## 10. H / tH decision

No auxiliary H/tH theorem is needed at s7-39.

The receiver has only one fixed-power scalar left, and its defining congruence is already explicit. An external average theorem would be premature before the remaining exact row-lift congruence is exhausted.

Merged `tH21` concerns the fixed-U clean-kappa Type-II coefficient space and is not cross-promoted to this whole-family common-core packet.

```text
S7_39_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
TH21_CROSS_PROMOTED_TO_S7_39=false.
```

---

## Stage boundary

```text
STAGE14_S7_39=COMPLETE_CAYLEY_RESIDUAL_DISJOINTNESS_SQUARE_ROOT_LOST_CORE_AND_17_32_PROMOTION
MERGED_S7_38_IMPORTED=true
MERGED_4CW_61_112_IMPORTED=true
MERGED_X12_IMPORTED=true
CAYLEY_GOOD_CORE_COPRIME_TO_COMMON_ROOT_GCD=true
CAYLEY_RESIDUAL_FIXED_POWER_INTERSECTION_TRIVIAL=true
CAYLEY_ONLY_ANNULUS_FIXED_POWER_EXPONENT=0
JOINT_CORE_EQUALS_CAYLEY_GOOD_CORE_AT_FIXED_POWER=true
LOST_CORE_SQUARE_ROOT_DIVISOR_PROVED=true
LOST_CORE_SQUARE_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true
JOINT_CORE_LOWER_EXPONENT=chi-2s_H
SQUARE_ROOT_REFINED_COLUMN_SUPPORT=max(0,s_H-d)
FULL_ROW_LIFT_SUPPORT=max(0,2s_H-d)
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=17/32
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=17/32
IMPROVEMENT_OVER_PREVIOUS_61_112=3/224
CURRENT_GAP_TO_SQRT=1/32
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SEVENTEEN_32_SATURATION_THETA=17/64
SEVENTEEN_32_SATURATION_PHI=1/4
SEVENTEEN_32_COMMON_CORE_EXPONENT=9/32
SEVENTEEN_32_TOTAL_CROSS_ROOT_EXPONENT=1/32
SEVENTEEN_32_JOINT_CAYLEY_CORE_EXPONENT=7/32
SEVENTEEN_32_LOST_CORE_EXPONENT=1/16
SEVENTEEN_32_FORCED_SQUARE_ROOT_EXPONENT=1/32
SEVENTEEN_32_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=0
SEVENTEEN_32_ROW_CRT_LIFT_EXPONENT=1/32
REMAINING_RECEIVER=SeventeenThirtySecondsCayleyResidualDisjointSquareRootLostCoreSingleRowLiftIncidence
S7_39_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
TH21_CROSS_PROMOTED_TO_S7_39=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-40
```
