# Stage14-4cv — joint-core row/column reconstruction and the 7/12 bound

## Status

`COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION`

This revision is based on latest merged main through `s7-34`.  It consumes merged `4cu`, merged `s7-33`, and checks compatibility with merged `s7-34`.

The entering mainline bound is `19/32`; s7-34 independently gives `47/80`.  The row/column reconstruction below is stronger:

```text
boxed: V(B) << B^(7/12+o(1)).
```

No external incidence theorem is used.

## 1. Imported exact data

Write

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4,
3/16<=theta<=5/16,
1/8<=phi<=1/4,
0<=theta-phi<=1/8,
theta+phi>=3/8.
```

Use the full signed quotients

```text
a=c_x^+, b=c_x^-, c=c_k^+, d=c_k^-,
N=a*b*c*d.
```

Merged s7-27 gives

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res),
```

up to the finite 2-primary decoration. Hence `N<=B^(1/4+o(1))` because `u_res*v_res<=B^(1/4+o(1))`.

Put

```text
r=r1*r2, s=s1*s2, X=x1*x2, Y=y1*y2,
M=4*r*s*X*Y*epsilon_x*epsilon_k.
```

Since `z_i=2*x_i*y_i/g_i`, fixed `(z1,z2)` plus endpoint-small/2-primary data fixes `M` exactly.

Merged 4cr gives

```text
C_- | M-N,
C_+ | M+N,
gcd(C_-,C_+)=1.
```

Merged 4cu chooses a switched xi host and gives

```text
g_star=B^(rho+o(1)),
J=J_star|C,
J>=B^(chi-3rho-o(1)),
J|L_-L_+,
```

where

```text
L_-=z1*r2*s2-z2*r1*s1,
L_+=z1*r2*s2+z2*r1*s1,
0<|L_-L_+|<=B^(1/4+o(1))
```

on the nonproportional branch.  The selected xi-host complete count is

```text
E_xi<=3phi-1/8-rho.                                (1.1)
```

The proportional branch is already `<=9/16` by 4cu.

Merged s7-33 identifies the common-core Gaussian orientation with the primitive root-line orientation and proves that double charging it is forbidden.  It also supplies a physical counterexample to the stronger canonical `S/T` associate split.  Neither forbidden shortcut is used below.

## 2. Exact 2x2 partition of the same joint core

Every odd prime power of `J` has two already-proved relative signs:

- Cayley row sign: whether it belongs to `C_-` or `C_+`;
- endpoint-linear column sign: whether it divides `L_-` or `L_+`.

Define the four pairwise-coprime cells

```text
J_{--}, J_{-+}, J_{+-}, J_{++},
J=J_{--}J_{-+}J_{+-}J_{++}.
```

Row products:

```text
J_C-=J_{--}J_{-+},
J_C+=J_{+-}J_{++},
J_C- J_C+=J,
J_C-|M-N,
J_C+|M+N.
```

Column products:

```text
J_L-=J_{--}J_{+-},
J_L+=J_{-+}J_{++},
J_L- J_L+=J,
J_L-|L_-,
J_L+|L_+.
```

This is one modulus viewed in two directions.  No row modulus is multiplied by a column modulus as an independent spacing gain.

## 3. Column cofactors reconstruct `z1,z2`

Write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+.
```

If `J=B^(j+o(1))`, then

```text
|h_-h_+|=|L_-L_+|/J<=B^(1/4-j+o(1)).              (3.1)
```

Hence the ordered cofactor pair costs at most `B^(1/4-j+o(1))`.

Then

```text
z1*r2*s2=(L_++L_-)/2,
z2*r1*s1=(L_+-L_-)/2.
```

The `r_i,s_i` tuple is endpoint-small, so `(z1,z2)` has only divisor-many lifts. Thus `M` is fixed up to `B^o(1)`.

## 4. Cayley rows reconstruct `N=abcd` by CRT

The row congruences are

```text
N == M  (mod J_C-),
N == -M (mod J_C+).
```

Because `gcd(J_C-,J_C+)=1`, CRT fixes one residue `N_0 mod J`.  Since `N<=B^(1/4+o(1))`, write

```text
N=N_0+J*h_N,
|h_N|<=B^(1/4-j+o(1)).                             (4.1)
```

So the CRT lift costs at most `B^(1/4-j+o(1))`.

For fixed `N`, the positive quadruple `(a,b,c,d)` has at most `tau_4(N)=B^o(1)` possibilities.  Therefore `u_res` and `v_res` are reconstructed from the signed quotient products and are not charged independently in this alternative count.

## 5. Row/column complete count

Use the legal order

```text
C
-> primitive common-core pair (U,V)
-> divisor-many 2x2 allocation of J|C
-> h_-,h_+
-> z1,z2 and M
-> CRT lift h_N and N
-> divisor-many a,b,c,d
-> merged reciprocal reconstruction.
```

The fixed-power costs are

```text
C:                    chi
primitive (U,V):      2phi-chi
linear cofactors:     1/4-j
CRT N-lift:           1/4-j.
```

Therefore

```text
boxed: E_RC<=2phi+1/2-2j.                          (5.1)
```

Using merged 4cu `j>=chi-3rho-o(1)` gives

```text
boxed: E_RC<=2phi+1/2-2chi+6rho.                   (5.2)
```

## 6. Eliminate rho and prove 7/12

For the same nonproportional block:

```text
E_xi<=3phi-1/8-rho,
E_RC<=2phi+1/2-2chi+6rho.
```

Since `min(A,B)<=(6A+B)/7`, the `rho` terms cancel:

```text
E <= (20phi-2chi-1/4)/7
  = (16phi-4theta+5/4)/7.                          (6.1)
```

Combine with merged s7-32 complete bounds

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.
```

- If `theta<=1/4`, `E_k<=1/2`.
- If `1/4<=theta<=7/24`, `E_s=2theta<=7/12`.
- If `theta>=7/24`, use `phi<=1/4` in (6.1):
  `E<=3/4-(4/7)theta<=7/12`.
- Proportional branch: `E<=9/16<7/12`.

Thus

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12
IMPROVEMENT_OVER_PREVIOUS_19_32=1/96
IMPROVEMENT_OVER_MERGED_S7_34_47_80=1/240
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

## 7. Equality profile

Equality in the proved envelope is unique:

```text
theta=7/24,
phi=1/4,
chi=1/3,
rho=1/24,
j=chi-3rho=5/24.
```

Hence

```text
C~B^(1/3),
g_star~B^(1/24),
J~B^(5/24),
|h_-h_+|<=B^(1/24+o(1)),
|h_N|<=B^(1/24+o(1)).
```

The exact ledger is

```text
C + primitive root-line fiber: 1/2
linear cofactor support:        1/24
CRT N-lift support:             1/24
------------------------------------
total:                          7/12.
```

## 8. Compatibility with merged s7-34

Merged s7-34 adds

```text
H^4|q_xi,
E_xi,H<=3phi-1/8-3eta,
```

for `H=B^(eta+o(1))`, and on the nonproportional branch

```text
d=max(0,chi-1/4)<=2rho+eta.
```

These are compatible with the 4cv equality profile: at

```text
theta=7/24, phi=1/4, chi=1/3, rho=1/24
```

we have `d=1/12=2rho`, so `eta=0` is allowed.  Hence the fourth-power theorem does not automatically improve `7/12` further.  Instead the entire fixed-power selected residual gcd may lie in the s7-34 extra factor

```text
G_extra~B^(1/24)
```

when `H=B^o(1)`.

Thus s7-34 is imported as an additional necessary saturation filter, not multiplied as a new saving.

## 9. Remaining receiver and H decision

The current minimal receiver is

```text
SevenTwelfthsExtraResidualGcdRowColumnTwinShortCofactorIncidence.
```

At its equality profile it retains simultaneously

```text
H=B^o(1),
G_extra~B^(1/24),
J~B^(5/24),
L_-=J_L-*h_-,
L_+=J_L+*h_+,
|h_-h_+|<=B^(1/24+o(1)),
N=N_0+J*h_N,
|h_N|<=B^(1/24+o(1)).
```

There is still exact arithmetic to exploit between the extra residual gcd and the two surviving `1/24` cofactors.  Therefore no mainline H is requested.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T73_CROSS_PROMOTED_TO_MAINLINE=false.
```

`Stage14-4cw` should compare `G_extra`, the linear cofactor product, and the Cayley CRT lift primewise before any analytic average is invoked.

## Stage boundary

```text
STAGE14_4CV=COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION
MERGED_4CU_IMPORTED=true
MERGED_S7_33_IMPORTED=true
MERGED_S7_34_COMPATIBILITY_CHECKED=true
JOINT_CORE_TWO_BY_TWO_ROW_COLUMN_PARTITION_PROVED=true
JOINT_CORE_FOUR_CELLS_PAIRWISE_COPRIME=true
COLUMN_DATA_RECONSTRUCT_ENDPOINT_ROOTS_BO1=true
CAYLEY_ROW_CRT_DETERMINES_N_MOD_J=true
FIXED_N_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1
ROW_COLUMN_RECONSTRUCTION_BLOCK_EXPONENT=2phi+1/2-2j
ROW_COLUMN_RECONSTRUCTION_RHO_BOUND=2phi+1/2-2chi+6rho
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/12
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12
IMPROVEMENT_OVER_PREVIOUS_19_32=1/96
IMPROVEMENT_OVER_MERGED_S7_34_47_80=1/240
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SEVEN_TWELFTHS_SATURATION_THETA=7/24
SEVEN_TWELFTHS_SATURATION_PHI=1/4
SEVEN_TWELFTHS_SATURATION_COMMON_CORE_EXPONENT=1/3
SEVEN_TWELFTHS_SATURATION_SELECTED_XI_GCD_EXPONENT=1/24
SEVEN_TWELFTHS_SATURATION_JOINT_CORE_EXPONENT=5/24
SEVEN_TWELFTHS_LINEAR_COFACTOR_EXPONENT=1/24
SEVEN_TWELFTHS_CRT_LIFT_EXPONENT=1/24
SEVEN_TWELFTHS_ROOT_GCD_EXPONENT_CAN_BE_ZERO=true
SEVEN_TWELFTHS_EXTRA_RESIDUAL_GCD_EXPONENT=1/24
STRONG_CANONICAL_ST_SPLIT_USED=false
COMMON_CORE_ORIENTATION_DOUBLE_CHARGED=false
REMAINING_RECEIVER=SevenTwelfthsExtraResidualGcdRowColumnTwinShortCofactorIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T73_CROSS_PROMOTED_TO_MAINLINE=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cw
```