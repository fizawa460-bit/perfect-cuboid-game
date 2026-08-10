# Stage14-X11 — proportional 9/16 barrier after nonproportional fourth-power row/column collapse

## Status

`COMPLETE_NONPROPORTIONAL_ROW_COLUMN_FOURTH_POWER_COLLAPSE_AND_9_16_PROMOTION`

This revision is synchronized to merged main

```text
3b8e841b11a7d444412946315e7763492df10a72
```

and consumes merged `X10`, `s7-33`, `4cu`, `s7-34`, `s7-35`.  The later merged `4cv` is compatible but is not needed as a theorem source: the row/column reconstruction is rederived below from the already-merged `4cu` orientation data.

The entering canonical theorem is merged `s7-35`:

```text
V(B) << B^(4/7+o(1)).
```

X11 proves

```text
boxed:
V(B) << B^(9/16+o(1)).
```

The improvement is

```text
4/7-9/16=1/112,
```

and the remaining gap to square-root scale is

```text
9/16-1/2=1/16.
```

No external sieve, determinant theorem, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported balanced strip

Keep

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

chi=2theta+2phi-3/4,
C=B^(chi+o(1)).
```

Merged `s7-32` supplies complete counts

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.
```

Merged `4cu` splits the physical family into

```text
nonproportional: L_-L_+ != 0,
proportional:    L_-=0,
```

where

```text
L_-=z_1 r_2 s_2-z_2 r_1 s_1,
L_+=z_1 r_2 s_2+z_2 r_1 s_1.
```

Positivity excludes `L_+=0`.

---

## 2. Exact s7-35 residual-gcd collapse

Write the two cross-root cells as

```text
H_star =B^(eta_star+o(1)),
H_other=B^(eta_other+o(1)),
eta_star>=eta_other>=0.
```

For the selected xi residual host let

```text
g_star=B^(rho+o(1)).
```

Merged `s7-35` proves, at exponent scale,

```text
boxed:
rho=2eta_star.                                      (2.1)
```

Merged `s7-34/s7-35` also give the fourth-power complete xi count

```text
boxed:
E_H <=3phi-1/8-3eta_star-3eta_other.               (2.2)
```

The exact pre-relaxation `4cu` joint-core lower bound is

```text
boxed:
j>=chi-2rho-2eta_other
     =chi-4eta_star-2eta_other,                    (2.3)
```

for `J=B^(j+o(1))`.

---

## 3. Row/column reconstruction on the nonproportional branch

The rank-two orientation theorem of merged `4cu` gives a 2x2 partition of the same already-charged joint core:

```text
J=J_{--}J_{-+}J_{+-}J_{++},
```

with pairwise-coprime cells.  Define

```text
J_C-=J_{--}J_{-+},   J_C+=J_{+-}J_{++},
J_L-=J_{--}J_{+-},   J_L+=J_{-+}J_{++}.
```

Then

```text
J_C-J_C+=J,
J_L-J_L+=J,

J_C- | M-N,
J_C+ | M+N,
J_L- | L_-,
J_L+ | L_+,
```

where

```text
M=4rsXY epsilon_x epsilon_k,
N=abcd<=B^(1/4+o(1)).
```

This is one modulus viewed by rows and columns.  It is not two independent spacing moduli; merged `s7-33`'s no-double-charge rule is retained.

Write

```text
L_-=J_L- h_-,
L_+=J_L+ h_+.
```

Since `0<|L_-L_+|<=B^(1/4+o(1))`,

```text
|h_-h_+|<=B^(1/4-j+o(1)).                          (3.1)
```

Fixing the two cofactors reconstructs `z_1,z_2` and hence `M` with divisor-many multiplicity.  The Cayley rows then give

```text
N == M  (mod J_C-),
N ==-M  (mod J_C+),
```

so CRT fixes one class modulo `J`.  Because `N<=B^(1/4+o(1))`,

```text
#N<=B^(1/4-j+o(1)).                                (3.2)
```

For fixed `N`, `(a,b,c,d)` is divisor-many.  Hence

```text
boxed:
E_RC<=2phi+1/2-2j
    <=2phi+1/2-2chi+8eta_star+4eta_other.          (3.3)
```

---

## 4. Nonproportional branch: 19/34

For the same nonproportional physical block, (2.2) and (3.3) are alternative complete counts.  Therefore

```text
E_nonprop
 <=min(E_H,E_RC)
 <=(8E_H+3E_RC)/11.                                (4.1)
```

Expanding exactly,

```text
8E_H+3E_RC
 <=30phi+1/2-6chi-12eta_other.
```

Since `eta_other>=0`,

```text
E_nonprop
 <=(30phi+1/2-6chi)/11
 =(18phi-12theta+5)/11.                            (4.2)
```

Using `phi<=1/4`,

```text
E_nonprop<=19/22-(12/11)theta.                     (4.3)
```

Combine with the merged `E_s,E_k` counts:

- `theta<=1/4`: `E_k<=1/2`;
- `1/4<=theta<=19/68`: `E_s=2theta<=19/34`;
- `theta>=19/68`: (4.3) gives `E_nonprop<=19/34`.

Thus

```text
boxed:
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34. (4.4)
```

Equality in this derived envelope is localized at

```text
theta=19/68,
phi=1/4,
chi=21/68,
eta_star=3/136,
eta_other=0,
rho=3/68,
j=15/68.
```

The row and column short supports are each

```text
1/4-j=1/34.
```

Since `19/34<9/16`, the nonproportional branch is no longer globally critical.

---

## 5. Proportional branch is the new global barrier

Merged `4cu` proves that `L_-=0` implies

```text
z_1 r_2 s_2=z_2 r_1 s_1.
```

After reducing the endpoint-small ratio,

```text
z_1=a t,
z_2=b t,
a,b=B^o(1),
t=B^(1/8+o(1)).                                   (5.1)
```

The full integer `t` divides both coordinates of the k switched residual host.  The gcd-stratified k one-host count therefore gives

```text
boxed:
E_prop,k<=3theta-3/8<=9/16.                        (5.2)
```

Consequently

```text
E<=max(19/34,9/16)=9/16,
```

and hence

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=9/16.       (5.3)
```

This proves a new saving beyond merged `4/7`.

---

## 6. Proportional saturation localization

The raw bound (5.2) can attain `9/16` only at

```text
theta=5/16.                                        (6.1)
```

Then

```text
chi=2phi-1/8.
```

The fourth-power xi count remains

```text
E_H<=3phi-1/8-3eta_star-3eta_other.                (6.2)
```

The proportional identity already fixes the ratio of `(z_1,z_2)`; summing the common scale `t` costs `B^(1/8+o(1))`.  The Cayley rows still reconstruct `N mod J`, so a legal row count is

```text
E_prop,row<=2phi+3/8-j.                            (6.3)
```

Using `j>=chi-4eta_star-2eta_other` and (6.1),

```text
E_prop,row<=1/2+4eta_star+2eta_other.              (6.4)
```

Therefore

```text
min(E_H,E_prop,row)
 <=(4E_H+3E_prop,row)/7
 <=(12phi+1)/7,                                    (6.5)
```

where a nonpositive `-6eta_other/7` term is discarded.

Since

```text
(12*(47/192)+1)/7=9/16,
```

all proportional blocks with `phi<47/192` are strictly subcritical.  Thus any packet saturating the current envelope must satisfy

```text
boxed:
theta=5/16,
47/192<=phi<=1/4,
L_-=0.                                             (6.6)
```

At the lower endpoint `phi=47/192`, equality further forces

```text
eta_star=1/64,
eta_other=0,
j=29/96.
```

No claim is made that the full interval in (6.6) is nonempty; it is the surviving necessary locus of the proved envelope.

---

## 7. Remaining receiver

The new minimal X receiver is

```text
NineSixteenthsProportionalKResidualCommonScaleXiRowTransferIncidence.
```

It retains simultaneously

```text
theta=5/16,
47/192<=phi<=1/4,
L_-=0,
z_1=a t,
z_2=b t,
t=B^(1/8+o(1)),
t | gcd(Re W_beta,Im W_beta),
H^4|q_xi,
rho=2eta_star,
J row-Cayley CRT data,
all primitive/reduced/canonical physical masks.
```

The next X-stage should use the exact proportional identity before summing the common `t` scale: compare the k residual quotient after division by `t`, the xi fourth-power root cells, and the Cayley-row CRT class.

---

## 8. H / tH decision

All inputs are merged internal arithmetic theorems.  No genuine external average theorem is yet isolated.

```text
X11_AUXILIARY_H_NEEDED=false,
X_ROUTE_BLOCKED_BY_H=false,
GENERIC_GENUS_ONE_H_REOPENED=false,
TH20_CROSS_PROMOTED_TO_X11=false.
```

The fixed-U tH20 norm-value problem remains a distinct coefficient space.

---

## Stage boundary

```text
STAGE14_X11=COMPLETE_NONPROPORTIONAL_ROW_COLUMN_FOURTH_POWER_COLLAPSE_AND_9_16_PROMOTION
MERGED_X10_IMPORTED=true
MERGED_S7_33_IMPORTED=true
MERGED_4CU_IMPORTED=true
MERGED_S7_34_IMPORTED=true
MERGED_S7_35_IMPORTED=true
MERGED_4CV_COMPATIBILITY_CHECKED=true
OPEN_4CV_PR_540_USED_AS_THEOREM_INPUT=false
S7_35_RHO_EQUALS_TWO_ETA_STAR_IMPORTED=true
JOINT_CORE_ROW_COLUMN_PARTITION_REDERIVED=true
NONPROPORTIONAL_ROW_COLUMN_COMPLETE_COUNT=2phi+1/2-2chi+8eta_star+4eta_other
NONPROPORTIONAL_WEIGHTED_COMBINATION=8:3
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
NONPROPORTIONAL_SATURATION_THETA=19/68
NONPROPORTIONAL_SATURATION_PHI=1/4
NONPROPORTIONAL_SATURATION_JOINT_CORE_EXPONENT=15/68
NONPROPORTIONAL_SHORT_SUPPORT_EXPONENT=1/34
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=9/16
IMPROVEMENT_OVER_MERGED_4_7=1/112
CURRENT_GAP_TO_SQRT=1/16
NINE_SIXTEENTHS_SATURATION_THETA=5/16
NINE_SIXTEENTHS_SATURATION_PHI_LOWER=47/192
NINE_SIXTEENTHS_SATURATION_PHI_UPPER=1/4
PROPORTIONAL_LINEAR_MINUS_ZERO_REQUIRED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
REMAINING_RECEIVER=NineSixteenthsProportionalKResidualCommonScaleXiRowTransferIncidence
X11_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT_RECOMMENDED=Stage14-X12
```