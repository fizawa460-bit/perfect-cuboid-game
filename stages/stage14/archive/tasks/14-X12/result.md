# Stage14-X12 — lost-core fourth-root column coupling and the 71/128 bound

## Status

`COMPLETE_LOST_CORE_FOURTH_ROOT_COLUMN_COFACTOR_COUPLING_AND_71_128_PROMOTION`

Stage14-X12 is based on latest merged main through `Stage14-s7-37` and consumes the merged `Stage14-X11` theorem together with the exact `s7-35`, `4cu`, and `4cv/s7-36` joint-core arithmetic.

The entering whole-family theorem is

```text
V(B) << B^(19/34+o(1)).
```

Merged `s7-37` has already made the proportional branch strictly sub-square-root:

```text
E_prop <= 7/16.
```

Thus X12 works only on the nonproportional branch and on its current `19/34` receiver.  The two remaining short quantities there were previously charged independently:

```text
L_-=J_L- h_-,
L_+=J_L+ h_+,
|h_-h_+| <= B^(1/4-j+o(1)),

N=N_0(M,J_C-,J_C+)+J h_N,
#h_N <= B^(1/4-j+o(1)).
```

The new point is that the part of the common core omitted from the selected joint core,

```text
D=C/J,
```

is not free.  After the endpoint-small decoration is removed, a fourth-root divisor of `D` is forced into the physical cross-root gcd and hence into the column cofactor product `h_-h_+`.  This legally sparsifies an already-charged support; it does **not** multiply the joint core by the cross-root gcd as a second modulus.

The resulting complete count improves the nonproportional branch to

```text
E_nonprop <= 71/128,
```

and therefore

```text
boxed:
V(B) << B^(71/128+o(1)).
```

The gain over merged `19/34` is

```text
19/34-71/128=9/2176,
```

and the remaining gap to square-root scale is

```text
71/128-1/2=7/128.
```

No external sieve, determinant theorem, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported nonproportional row/column packet

Keep the balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

Merged `s7-36/X11` gives on the nonproportional branch

```text
L_-L_+ != 0,
```

and the exact 2x2 partition of one selected joint core

```text
J=J_{--}J_{-+}J_{+-}J_{++},
```

with pairwise-coprime cells.  Set

```text
J_C-=J_{--}J_{-+},
J_C+=J_{+-}J_{++},
J_L-=J_{--}J_{+-},
J_L+=J_{-+}J_{++}.
```

Then

```text
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

Write

```text
J=B^(j+o(1)).
```

The column reading is

```text
L_-=J_L- h_-,
L_+=J_L+ h_+,
|h_-h_+|<=B^(1/4-j+o(1)),                         (1.1)
```

and reconstructs `(z1,z2)` and `M` with divisor-many multiplicity.  The Cayley-row CRT then gives

```text
N=N_0+J h_N,
#h_N<=B^(1/4-j+o(1)),                              (1.2)
```

followed by divisor-many signed-quotient reconstruction.

The old row/column complete count was therefore

```text
E_RC<=2phi+1/2-2j.                                 (1.3)
```

---

## 2. Imported cross-root and selected-host data

Use the two cross-root cells

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)),
H=H_S H_T,
gcd(H_S,H_T)=1.
```

Choose `star` with `H_star>=H_other` at dyadic scale and write

```text
H_star =B^(eta_star+o(1)),
H_other=B^(eta_other+o(1)),
eta_star>=eta_other>=0.
```

Merged `s7-35` proves the exact residual-gcd collapse

```text
g_star=H_star^2 * B^o(1),
```

so at exponent scale

```text
rho=2eta_star.                                     (2.1)
```

Merged `s7-34` gives

```text
H^4 | q_xi
```

and the complete fourth-power-root count

```text
boxed:
E_H<=3phi-1/8-3eta_star-3eta_other.                (2.2)
```

---

## 3. Do not multiply `J` by the switched root gcd

A tempting shortcut would be to combine

```text
J|L_-L_+,
H_star|L_-L_+,
```

as though `J` and `H_star` were coprime.  This is invalid.

Merged `4cu` explicitly keeps switched-cell prime powers inside the joint core whenever their residual Gaussian orientation survives.  Therefore a switched-cell prime may divide `J`, and no statement of the form

```text
J*H_star^2 | L_-L_+
```

is used in X12.

```text
SWITCHED_CELL_PRIMES_MAY_REMAIN_IN_J=true.
JOINT_CORE_CROSS_ROOT_PRODUCT_SHORTCUT_USED=false.
```

The correct new object is the **lost core quotient** `C/J`.

---

## 4. Exact lost-core quotient support

Merged `4cu` defines two divisors of the common core:

```text
C_Cayley | C,
C_res    | C,
J=gcd(C_Cayley,C_res).                             (4.1)
```

Here

```text
C/C_Cayley | endpoint-small * H_star^2 H_other^2,  (4.2)
```

while

```text
C_res=C/gcd(C,g_star^2),
```

so

```text
C/C_res | g_star^2.                                (4.3)
```

By the merged s7-35 identity `g_star/H_star^2|endpoint-small`, there is an integer

```text
Omega=B^o(1)
```

built only from the already-harmless endpoint-small decoration such that

```text
C/C_Cayley | Omega * H_star^2 H_other^2,
C/C_res    | Omega * H_star^4.                     (4.4)
```

For any two divisors `A,B` of `C`,

```text
C/gcd(A,B)=lcm(C/A,C/B).
```

Applying this to (4.1), define

```text
boxed:
D:=C/J.                                            (4.5)
```

Then (4.4) gives the exact support inclusion

```text
boxed:
D | Omega * H_star^4 H_other^2.                    (4.6)
```

This is an lcm statement.  No two bad supports are multiplied as independent moduli.

Remove the endpoint-small overlap by

```text
D_0:=D/gcd(D,Omega).                               (4.7)
```

Prime by prime, (4.6) implies

```text
boxed:
D_0 | H_star^4 H_other^2.                          (4.8)
```

Since `Omega=B^o(1)`, if `D=B^(chi-j+o(1))`, then

```text
D_0=B^(chi-j+o(1)).                                (4.9)
```

---

## 5. The fourth-root divisor of the lost core lies in `H`

For a positive integer `n`, define

```text
R_4(n):=prod_p p^ceil(v_p(n)/4).                   (5.1)
```

From (4.8), for every odd prime `p`,

```text
v_p(D_0)<=4v_p(H_star)+2v_p(H_other).
```

The two cross cells are coprime, so each prime occurs in at most one of them.  Hence

```text
ceil(v_p(D_0)/4)
 <=v_p(H_star)+v_p(H_other).
```

Therefore

```text
boxed:
R_4(D_0) | H_star H_other=H.                       (5.2)
```

Also trivially

```text
R_4(D_0)>=D_0^(1/4),
```

so from (4.9)

```text
boxed:
R_4(D_0)>=B^((chi-j)/4-o(1)).                      (5.3)
```

This is a forced physical divisor, not a new freely summed modulus.

---

## 6. Every cross-root divisor enters both endpoint linear forms

Every odd divisor of `H_S` divides both `z1` and `z2`: it occurs through `y1` in `z1` and through `x2` in `z2`.  Similarly every odd divisor of `H_T` occurs through `x1` and `y2` and again divides both `z1,z2`.

Hence

```text
boxed:
H | gcd(L_-,L_+).                                  (6.1)
```

Combining (5.2) and (6.1),

```text
R_4(D_0)|L_-,
R_4(D_0)|L_+.                                      (6.2)
```

Now

```text
L_-=J_L- h_-,
L_+=J_L+ h_+,
gcd(J_L-,J_L+)=1.
```

At each prime power of `R_4(D_0)`, at most one of the two column moduli can contain that prime.  The opposite column cofactor must therefore carry the full required prime power.  Thus

```text
boxed:
R_4(D_0) | h_-h_+.                                 (6.3)
```

This is the new X12 coupling theorem.

```text
LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true.
```

---

## 7. Refined column support

Before X12, the column cofactor product had support exponent

```text
s=1/4-j.
```

After `C,J,Omega` are fixed, `R_4(D_0)` is fixed and (5.3), (6.3) force a divisor of exponent at least `(chi-j)/4` into `h_-h_+`.

The number of possible ordered cofactor pairs is therefore

```text
B^o(1)
 * B^(1/4-j-(chi-j)/4)
```

rather than `B^(1/4-j)`: once the product divided by the forced divisor is fixed, allocation among the two factors is divisor-many.

Hence the effective column support exponent is

```text
boxed:
1/4-j-(chi-j)/4.                                   (7.1)
```

The row CRT lift remains

```text
1/4-j.                                             (7.2)
```

No saving from the same divisor is charged a second time.

---

## 8. Refined row/column complete count

The common-core plus primitive-pair part still costs exactly

```text
C:                   chi,
primitive pair:      2phi-chi,
```

so together it is `2phi`.

Add (7.1)-(7.2):

```text
boxed:
E_RC4
 <=2phi
   +(1/4-j-(chi-j)/4)
   +(1/4-j)
 =2phi+1/2-chi/4-7j/4.                             (8.1)
```

Merged `4cu/s7-35` gives the exact pre-relaxation selected-core lower bound

```text
j>=chi-4eta_star-2eta_other.                       (8.2)
```

Insert (8.2) into (8.1):

```text
boxed:
E_RC4
 <=2phi+1/2-2chi
   +7eta_star+(7/2)eta_other.                      (8.3)
```

This is a complete count of the same nonproportional physical block as (2.2).

---

## 9. `7:3` cancellation and the nonproportional envelope

For the same block, compare

```text
E_H
 <=3phi-1/8-3eta_star-3eta_other,

E_RC4
 <=2phi+1/2-2chi
   +7eta_star+(7/2)eta_other.
```

Since both are complete alternative counts,

```text
E_nonprop<=min(E_H,E_RC4)
         <=(7E_H+3E_RC4)/10.                       (9.1)
```

The selected-cross exponent cancels exactly:

```text
7*(-3)+3*7=0.
```

The other-cross exponent is favorable:

```text
7*(-3)+3*(7/2)=-21/2.
```

Therefore

```text
E_nonprop
 <=(3/2)phi-(6/5)theta+41/80
   -(21/20)eta_other
 <=(3/2)phi-(6/5)theta+41/80.                      (9.2)
```

Using `phi<=1/4`,

```text
boxed:
E_nonprop<=71/80-(6/5)theta.                       (9.3)
```

---

## 10. Exact whole-strip minimax: `71/128`

Use the merged complete k- and s-counts in addition to (9.3).

### `theta<=1/4`

The k one-host count gives

```text
E_k<=3theta-1/4<=1/2<71/128.
```

### `1/4<=theta<=71/256`

The s-count is

```text
E_s=2theta<=71/128.
```

### `theta>=71/256`

By (9.3),

```text
E_nonprop
 <=71/80-(6/5)(71/256)
 =71/128.
```

Merged `s7-37` gives the proportional branch

```text
E_prop<=7/16<1/2<71/128.
```

Therefore every physical block satisfies

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128.     (10.1)
```

Equivalently,

```text
boxed:
V(B) << B^(71/128+o(1)).                           (10.2)
```

The improvement and remaining gap are

```text
boxed:
IMPROVEMENT_OVER_MERGED_19_34=9/2176,
CURRENT_GAP_TO_SQRT=7/128.                         (10.3)
```

---

## 11. New equality profile

Equality in the proved high-core envelope requires

```text
theta=71/256,
phi=1/4.                                           (11.1)
```

Then

```text
chi=39/128.                                        (11.2)
```

Equality in the `7:3` cancellation forces

```text
eta_other=0
```

and equality of the two complete counts gives

```text
eta_star=3/128,
rho=2eta_star=3/64.                                (11.3)
```

The selected joint core is then at its lower edge

```text
j=chi-4eta_star=27/128.                            (11.4)
```

Thus

```text
lost core D=C/J:                   3/32,
raw column cofactor support:       5/128,
forced fourth-root divisor:        3/128,
effective column quotient support: 1/64,
row CRT lift support:              5/128.           (11.5)
```

The refined `71/128` ledger is

```text
C + primitive-pair fiber:          1/2,
effective column quotient:         1/64,
row CRT lift:                       5/128,
-----------------------------------------
total:                              71/128.
```

The old `19/34` equality point is strictly subcritical under the X12 count.

---

## 12. New receiver

Define

```text
SeventyOneOneHundredTwentyEighthsLostCoreFourthRootColumnCRTLiftIncidence.
```

Any packet saturating the proved X12 envelope must retain simultaneously

```text
theta=71/256,
phi=1/4,
chi=39/128,
eta_star=3/128,
eta_other=0,
rho=3/64,
j=27/128,
D=C/J=B^(3/32+o(1)),
R_4(D_0)=B^(3/128+o(1)),
R_4(D_0)|h_-h_+,
(h_-h_+)/R_4(D_0) support <=B^(1/64+o(1)),
h_N support <=B^(5/128+o(1)),
all primitive/reduced/canonical physical masks.
```

The next exact target is no longer a symmetric twin-short problem.  It is an asymmetric coupling between a `1/64` effective column quotient and a `5/128` Cayley-row CRT lift, with `M` reconstructed from the column before `N=N_0(M)+Jh_N` is lifted.

---

## 13. H / tH decision

X12 uses only exact divisor/lcm arithmetic, merged physical gcd placement, divisor-many factor allocation, and convex minimax.

There is still unused exact arithmetic between the reconstructed column value `M`, the CRT residue `N_0(M)`, the effective column quotient, and `h_N`.  Therefore an external average theorem is premature.

```text
X12_AUXILIARY_H_NEEDED=false,
X_ROUTE_BLOCKED_BY_H=false,
GENERIC_GENUS_ONE_H_REOPENED=false,
TH20_CROSS_PROMOTED_TO_X12=false.
```

The fixed-U t75 receiver remains a different coefficient space.

---

## Stage boundary

```text
STAGE14_X12=COMPLETE_LOST_CORE_FOURTH_ROOT_COLUMN_COFACTOR_COUPLING_AND_71_128_PROMOTION
MERGED_X11_IMPORTED=true
MERGED_S7_37_IMPORTED=true
MERGED_S7_35_IMPORTED=true
MERGED_4CU_IMPORTED=true
LOST_CORE_QUOTIENT_D_EQUALS_C_OVER_J=true
LOST_CORE_QUOTIENT_DIVIDES_ENDPOINT_SMALL_HSTAR4_HOTHER2=true
LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_H=true
CROSS_ROOT_DIVIDES_BOTH_ENDPOINT_LINEAR_FORMS=true
LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true
COLUMN_COFACTOR_SAVING=(chi-j)/4
REFINED_ROW_COLUMN_COMPLETE_COUNT=2phi+1/2-chi/4-7j/4
REFINED_ROW_COLUMN_AFTER_J_LOWER=2phi+1/2-2chi+7eta_star+7eta_other/2
NONPROPORTIONAL_WEIGHTED_COMPLETE_COUNT_COMBINATION=7:3
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=71/128
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128
IMPROVEMENT_OVER_MERGED_19_34=9/2176
CURRENT_GAP_TO_SQRT=7/128
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_SATURATION_THETA=71/256
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_SATURATION_PHI=1/4
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_COMMON_CORE_EXPONENT=39/128
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_LIVE_CROSS_ROOT_EXPONENT=3/128
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_OTHER_CROSS_ROOT_EXPONENT=0
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_SELECTED_XI_GCD_EXPONENT=3/64
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_JOINT_CORE_EXPONENT=27/128
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_LOST_CORE_EXPONENT=3/32
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_RAW_COLUMN_COFACTOR_EXPONENT=5/128
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_FORCED_FOURTH_ROOT_DIVISOR_EXPONENT=3/128
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_EFFECTIVE_COLUMN_QUOTIENT_EXPONENT=1/64
SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_ROW_CRT_LIFT_EXPONENT=5/128
SWITCHED_CELL_PRIMES_MAY_REMAIN_IN_J=true
JOINT_CORE_CROSS_ROOT_PRODUCT_SHORTCUT_USED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
REMAINING_RECEIVER=SeventyOneOneHundredTwentyEighthsLostCoreFourthRootColumnCRTLiftIncidence
X12_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT_RECOMMENDED=Stage14-X13
```