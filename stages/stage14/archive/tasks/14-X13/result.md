# Stage14-X13 — reverse reciprocal divisor reconstruction and square-root closure

## Status

`COMPLETE_REVERSE_RECIPROCAL_COLUMN_TO_ROW_RECONSTRUCTION_AND_SQRT_PROMOTION`

Stage14-X13 consumes latest merged main through `Stage14-4cy`, `Stage14-s7-40`, and merged `Stage14-t78`.  The global arithmetic input is the merged `4cy/s7-40` unique-`23/44` contraction together with the older exact reciprocal reconstruction of merged `s7-27/s7-28` and the row/column quantifier order of merged `4cv`.

The entering canonical whole-family theorem is

```text
V(B) << B^(23/44+o(1)).
```

The decisive observation is that the two short coordinates retained by `4cy/s7-40` are not independent.  The endpoint-linear column reconstructs `M`.  Once the primitive xi-agreement pair `(U,V)` and `M` are fixed, the two exact reciprocal difference-of-squares equations may be read in reverse.  Their positive factor pairs reconstruct the opposite agreement pair and then the first signed quotient pair with divisor-many multiplicity.  In particular

```text
fixed (U,V,M)
=> N=a*b*c*d has B^o(1) possibilities.
```

Thus the Cayley row `N`-lift is a filter, not an additional fixed-power support, after the column has reconstructed `M`.

On the surviving low-core nonproportional region this removes one entire copy of the short exponent `1/4-chi` and gives

```text
E_X13 <= 2phi + (1/4-chi)
       = 1-2theta.
```

Together with the always-available k-host count on `theta<=1/4`, the high-core emptiness of merged `4cx`, and the proportional `7/16` bound of merged `s7-37`, this yields the exact square-root upper bound

```text
boxed:
V(B) << B^(1/2+o(1)).
```

No external sieve, determinant theorem, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported balanced packet and current theorem

Use the merged balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

The always-available complete counts include

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.
```

Merged `s7-37` gives on the proportional branch

```text
boxed:
E_prop<=7/16<1/2.                                  (1.1)
```

Merged `4cx` proves that every fixed-power nonproportional packet with

```text
chi>1/4
```

is empty.  Therefore the only nonproportional region needing a count satisfies

```text
boxed:
chi<=1/4.                                          (1.2)
```

Merged `4cy/s7-40` further prove a complete low-core row/column count and collapse the old `23/44` equality segment to one endpoint.  X13 will not use their row-lift cost; it replaces that final step by an exact reverse reciprocal reconstruction.

---

## 2. Imported column reconstruction after the cross-root/lost-core peels

Use the row/column notation

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,

M=4*r*s*X*Y*epsilon_x*epsilon_k,
N=a*b*c*d.
```

The endpoint-linear forms are

```text
L_- = z1*r2*s2-z2*r1*s1,
L_+ = z1*r2*s2+z2*r1*s1.
```

Merged `4cv` proves that, after fixing the once-charged common-core data and a legal column sign allocation,

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+
```

reconstruct `(z1,z2)` with only divisor-many endpoint-small ambiguity, hence reconstruct `M`.

Merged `4cx/4cy` remove the lost-core and cross-root common factors from this column support and prove uniformly on `chi<=1/4`

```text
boxed:
E_col <= 1/4-chi.                                  (2.1)
```

The common-core plus first primitive xi-agreement pair costs

```text
C:                       chi,
primitive (U,V):          2phi-chi,
```

so before any row step the charged-once fixed-power cost is

```text
boxed:
2phi+(1/4-chi).                                    (2.2)
```

The only question is whether a further `N`-lift must be paid after `M` is known.  The rest of X13 proves that it must not.

---

## 3. `M` fixes the root product `X*Y`

The physical root products are

```text
X=x1*x2,
Y=y1*y2,
```

and

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2}.
```

Hence exactly

```text
z1*z2 = 4*X*Y/(g1*g2).                             (3.1)
```

Since

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k,
```

we also have

```text
boxed:
M=r*s*epsilon_x*epsilon_k*g1*g2*z1*z2.             (3.2)
```

All factors other than `(z1,z2)` in (3.2) are endpoint-small or finite 2-primary decorations already fixed at `B^o(1)` cost in the merged column quantifier order.

Thus the imported column reconstruction fixes `M`, and equivalently fixes

```text
boxed:
X*Y=M/(4*r*s*epsilon_x*epsilon_k)                  (3.3)
```

whenever a physical completion exists.

---

## 4. Reverse the second reciprocal equation

Use the full signed quotient notation of merged `s7-27/s7-28`:

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-,

p=L_k^+,
q=L_k^-.
```

The exact reciprocal equations are

```text
(a*U)^2-(b*V)^2
 =4*r*s*epsilon_k*p*q,                             (4.1)

(c*p)^2-(d*q)^2
 =4*X*Y*epsilon_x*U*V.                             (4.2)
```

Fix `(U,V,M)` together with the endpoint-small/2-primary decoration.  By (3.3), `X*Y` is fixed.  Therefore the positive integer

```text
W_2:=4*X*Y*epsilon_x*U*V                           (4.3)
```

is fixed.

On every physical point,

```text
c*p=Q+P,
d*q=Q-P,
Q>P>0.
```

Consequently

```text
(c*p-d*q)(c*p+d*q)=W_2,                            (4.4)
```

with both factors positive.

A fixed polynomially bounded integer has only divisor-many ordered positive factor pairs.  Hence (4.4) gives only `B^o(1)` possibilities for

```text
F_2^-:=c*p-d*q,
F_2^+:=c*p+d*q.
```

For each such pair,

```text
c*p=(F_2^++F_2^-)/2,
d*q=(F_2^+-F_2^-)/2,                               (4.5)
```

and parity/positivity are only filters.  Each positive product in (4.5) has divisor-many ordered factorizations.  Therefore

```text
boxed:
fixed (U,V,M)
=> # {(c,d,p,q)} <= B^o(1).                        (4.6)
```

All coprimality, squarefree-cell, orientation, dyadic and physical masks only reduce this count.

---

## 5. Reverse the first reciprocal equation

For each divisor-many tuple `(c,d,p,q)` from Section 4, define

```text
W_1:=4*r*s*epsilon_k*p*q.                          (5.1)
```

This integer is fixed.  On a physical point

```text
a*U=D+A,
b*V=D-A,
D>A>0.
```

Thus (4.1) factors as

```text
(a*U-b*V)(a*U+b*V)=W_1.                            (5.2)
```

Again there are only divisor-many positive factor pairs

```text
F_1^-:=a*U-b*V,
F_1^+:=a*U+b*V.
```

For each pair,

```text
a*U=(F_1^++F_1^-)/2,
b*V=(F_1^+-F_1^-)/2.                               (5.3)
```

Since `(U,V)` is already fixed, divisibility by `U,V` determines `(a,b)` when a physical solution exists.  Therefore

```text
boxed:
fixed (U,V,M,c,d,p,q)
=> # {(a,b)} <= B^o(1).                            (5.4)
```

Combining (4.6) and (5.4),

```text
boxed:
fixed (U,V,M)
=> # {(a,b,c,d,p,q)} <= B^o(1).                    (5.5)
```

In particular

```text
boxed:
fixed (U,V,M)
=> # {N=a*b*c*d} <= B^o(1).                        (5.6)
```

This is the new reverse reciprocal divisor reconstruction lemma.

---

## 6. The Cayley row lift is no longer a support variable

Merged `4cv/4cy` uses the Cayley row congruences

```text
N == M  (mod C_-),
N == -M (mod C_+)
```

only after the column has reconstructed `M`.  The old count then paid a short lift for `N`.

Sections 4--5 show that at precisely this point in the quantifier order, `(U,V,M)` already admits only `B^o(1)` possible `N` values through the original reciprocal equations.  Therefore the row congruences merely reject some of those divisor-many candidates.  They do not generate a new polynomial support.

Hence

```text
boxed:
ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false,             (6.1)

boxed:
POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=B^o(1). (6.2)
```

Once `(a,b,c,d,p,q)` and `X*Y` are reconstructed, merged `s7-28` supplies only divisor-many labelled cell/switch/root completion.  No residual support is reintroduced.

There is no double charge: the common core is used once for the primitive pair/column spacing, while the reverse factorization uses exact integer equalities and divisor bounds only.

---

## 7. New nonproportional complete count

On the surviving low-core region `chi<=1/4`, use the legal order

```text
C
-> primitive common-core pair (U,V)
-> reduced endpoint-linear column data
-> z1,z2 and M
-> reverse reciprocal factorization
-> divisor-many N and remaining physical reconstruction.
```

The fixed-power costs are only

```text
C:                         chi,
primitive (U,V):            2phi-chi,
reduced column support:     1/4-chi,
reverse reciprocal row:     0.
```

Therefore

```text
boxed:
E_RRF
 <=2phi+1/4-chi.                                   (7.1)
```

Using

```text
chi=2theta+2phi-3/4,
```

this simplifies exactly to

```text
boxed:
E_RRF<=1-2theta.                                   (7.2)
```

For `chi>1/4`, merged `4cx` already proves the fixed-power nonproportional region empty.

---

## 8. Whole-strip square-root bound

We now combine only complete bounds for the same physical family.

### 8.1. Proportional branch

By merged `s7-37`,

```text
E_prop<=7/16<1/2.                                  (8.1)
```

### 8.2. Nonproportional branch with `theta<=1/4`

Use the merged k-host complete count:

```text
E<=E_k<=3theta-1/4<=1/2.                           (8.2)
```

### 8.3. Nonproportional branch with `theta>=1/4`

If `chi>1/4`, the fixed-power packet is empty by merged `4cx`.  Otherwise use (7.2):

```text
E<=E_RRF<=1-2theta<=1/2.                           (8.3)
```

These cases cover the full balanced physical packet.  Therefore

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,        (8.4)

boxed:
V(B) << B^(1/2+o(1)).                              (8.5)
```

Relative to the entering merged theorem,

```text
23/44-1/2=1/44.                                    (8.6)
```

Thus

```text
boxed:
IMPROVEMENT_OVER_MERGED_23_44=1/44,
SQRT_B_UPPER_BOUND_PROVED=true.                    (8.7)
```

No fixed positive saving below square root is claimed.

---

## 9. Remaining square-root saturation band

The proof shows that any sequence saturating the new `1/2` envelope must be nonproportional and satisfy

```text
boxed:
theta=1/4.                                         (9.1)
```

Indeed `E_k<1/2` for `theta<1/4`, while `E_RRF<1/2` for `theta>1/4`.

At `theta=1/4`,

```text
chi=2phi-1/4,
E_RRF=1/2,
E_k=1/2,
E_s=1/2.                                           (9.2)
```

The balanced strip gives

```text
1/8<=phi<=1/4.                                     (9.3)
```

Retaining the merged fourth-power cross-root complete count

```text
E_H<=3phi-1/8-3s,
H=B^(s+o(1)),
```

shows that square-root saturation additionally requires

```text
3phi-1/8-3s >= 1/2,
```

i.e.

```text
boxed:
phi-s>=5/24.                                       (9.4)
```

Hence every possible equality packet lies in the narrower band

```text
boxed:
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
chi=2phi-1/4 in [1/6,1/4].                         (9.5)
```

At the right endpoint `phi=1/4`, the reduced column support is already `B^o(1)` and the full `1/2` cost is carried by the common-core plus primitive-pair base.  At the left endpoint `phi=5/24`, the base and column contribute respectively `5/12` and `1/12`.

Thus the old twin-short receiver is closed.  The new obstruction to any strict sub-square-root bound is a theta-quarter common-core/primitive-pair versus single-column reconstruction band.

Define

```text
SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence.
```

Its mandatory fixed-power data are

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
nonproportional,
column support<=B^(1/2-2phi+o(1)),
post-column reciprocal completion=B^o(1),
row CRT lift independent support = false.
```

A strict sub-square-root theorem must now save inside this band, not revisit the eliminated row lift.

---

## 10. Relation to the parallel routes

Merged `s7-40` and merged `4cy` are the two global inputs that expose the twin short coordinates.  X13 consumes both and then uses the older exact reciprocal system in the reverse direction.

The open `4cz` branch was inspected only as a consistency check.  Its same-side root-gcd peel is not used as a theorem input and is not cross-promoted into X13.

The merged fixed-`U` route through `t78` and the open `tH22` audit remain a different coefficient space.  No fixed-`U` ray-character theorem is used in the square-root promotion.

```text
OPEN_4CZ_CROSS_PROMOTED_TO_X13=false
T78_CROSS_PROMOTED_TO_X13=false
TH22_CROSS_PROMOTED_TO_X13=false.
```

---

## 11. H / tH decision

No auxiliary X-specific H/tH theorem is needed.

The square-root bound is obtained by exact factorization and divisor reconstruction.  The new equality band still exposes internal deterministic arithmetic: the primitive common-core pair `(U,V)`, the reconstructed column `(z1,z2)`, and the normalized k/xi host equations have not yet been coupled at theta `1/4`.

Therefore

```text
X13_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false.
```

A new external theorem should be considered only if the theta-quarter band survives a direct primitive-pair/column coupling audit.

---

## 12. Next

`Stage14-X14` should work only on

```text
SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence
```

and test whether the same fixed `(U,V,M)` reverse factorization, together with full k-dual saturation / normalized host equations, makes the remaining primitive common-core pair and the single column support dependent.

The first target is a strict saving on

```text
theta=1/4,
5/24<=phi<=1/4.
```

Do not reopen the row CRT lift; X13 proves that support is already divisor-reconstructible after the column.

---

## Stage boundary

```text
STAGE14_X13=COMPLETE_REVERSE_RECIPROCAL_COLUMN_TO_ROW_RECONSTRUCTION_AND_SQRT_PROMOTION
MERGED_4CY_IMPORTED=true
MERGED_S7_40_IMPORTED=true
MERGED_S7_27_S7_28_RECIPROCAL_SYSTEM_IMPORTED=true
FIXED_PRIMITIVE_X_PAIR_AND_M_DETERMINES_XY=true
SECOND_RECIPROCAL_EQUATION_REVERSED_BY_DIVISOR_FACTORIZATION=true
FIRST_RECIPROCAL_EQUATION_REVERSED_BY_DIVISOR_FACTORIZATION=true
FIXED_PRIMITIVE_X_PAIR_AND_M_TO_OPPOSITE_PAIR_MULTIPLICITY=Bo1
FIXED_PRIMITIVE_X_PAIR_AND_M_TO_SIGNED_QUOTIENT_MULTIPLICITY=Bo1
FIXED_PRIMITIVE_X_PAIR_AND_M_TO_N_MULTIPLICITY=Bo1
ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false
POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=Bo1
REVERSE_RECIPROCAL_NONPROPORTIONAL_COMPLETE_COUNT=2phi+1/4-chi
REVERSE_RECIPROCAL_NONPROPORTIONAL_COMPLETE_COUNT_SIMPLIFIED=1-2theta
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
IMPROVEMENT_OVER_MERGED_23_44=1/44
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
REMAINING_RECEIVER=SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence
OPEN_4CZ_CROSS_PROMOTED_TO_X13=false
T78_CROSS_PROMOTED_TO_X13=false
TH22_CROSS_PROMOTED_TO_X13=false
X13_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
NEXT_RECOMMENDED=Stage14-X14
```
