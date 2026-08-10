# Stage14-t75 — angular cancellation split, primitive short-gap lemma, and Type-I/Type-II cover reduction

## Status

`COMPLETE_ANGULAR_GCD_COLUMN_SPLIT_PRIMITIVE_SHORT_GAP_AND_TYPE_I_TYPE_II_COVER_REDUCTION`

Stage14-t75 consumes merged t74 and merged tH20. The current strongest whole-family theorem comes from merged Stage14-X11:

```text
V(B) << B^(19/34+o(1)).
```

No additional whole-family saving is claimed by t75.

## 1. Imported post-t74 packet

Fix

```text
(U, epsilon, k, h, kappa, beta).
```

Write

```text
H   = odd(h),
Dpi = b^2-a^2,
DV  = q^2-p^2,
g   = gcd(odd(Dpi),odd(DV)),
c   = odd(Pminus/ell).
```

Merged t74 gives

```text
c = H*odd(DV)/g,
ell*c < 2B,
ell*g*c < 2B,
2c < ell,
q-p,q+p < sqrt(ell),
h*ell*((q-p)^2+(q+p)^2) <= 4B,
fixed (U,epsilon,k,h,ell,c) physical fiber = B^o(1).
```

Put

```text
r=q-p,
t=q+p,
R=odd(r),
T=odd(t).
```

Primitivity gives

```text
gcd(r,t) in {1,2},
gcd(R,T)=1.
```

## 2. Exact two-column split of `g`

Let

```text
A   = odd(Dpi),
g_r = gcd(A,R),
g_t = gcd(A,T).
```

Since `gcd(R,T)=1`,

```text
g = g_r*g_t,
gcd(g_r,g_t)=1.
```

Define

```text
R0=R/g_r,
T0=T/g_t.
```

Then exactly

```text
c/H = R0*T0,
gcd(R0,T0)=1.
```

Thus the angular cancellation and the uncancelled short cofactor are allocated uniquely to the two physical cover columns.

```text
ANGULAR_G_SPLITS_UNIQUELY_ACROSS_COVER_COLUMNS=true
ANGULAR_G_COLUMN_FACTORS_COPRIME=true
SHORT_COFACTOR_OVER_H_EQUALS_UNCANCELLED_ODD_COLUMN_PRODUCT=true
UNCANCELLED_ODD_COVER_COLUMNS_COPRIME=true
```

## 3. Primitive short-gap lemma

Write `r=2^a R`, `t=2^b T`. Because `gcd(r,t)<=2`, one has `min(a,b)<=1`.

- If `a<=1`, then `r<=2R<=2RT`.
- If `a>1`, then `b<=1`; since `r<t`, `r<t<=2T<=2RT`.

Therefore

```text
q-p = r <= 2*R*T = 2*odd(r*t).
```

Using `odd(r*t)=g*c/H`,

```text
boxed:
q-p <= 2*g*c/H.
```

Hence small `g*c/H` forces a short physical cover gap.

```text
PRIMITIVE_SHORT_GAP_LEMMA_PROVED=true
SMALL_G_TIMES_RESIDUAL_COFACTOR_FORCES_SHORT_Q_MINUS_P=true
```

## 4. Large-`g` block

For fixed `(U,epsilon,k,h,ell)`, the Gaussian direction is `O(1)`, so `A=odd(Dpi)` is fixed up to `O(1)`. Since `g|A` and t74 gives

```text
c < 2B/(ell*g),
```

while fixed `(ell,c)` has only `B^o(1)` physical lifts, for any threshold `G>=1`,

```text
N_large-g
 << B^o(1) * sum_ell sum_{g|A, g>=G} B/(ell*g)
 << B^(1+o(1))/G.
```

Here

```text
sum_{g|A,g>=G} 1/g <= tau(A)/G = B^o(1)/G
```

and `sum_{ell<=B^O(1)}1/ell=B^o(1)`.

This is a one-state parameter-mass saving, not a pair-energy theorem.

```text
LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED=true
LARGE_ANGULAR_G_SAVING_FACTOR=G^-1
LARGE_ANGULAR_G_PAIR_ENERGY_CLOSED=false
```

## 5. Balanced / highly-unbalanced cover split

For `L>=1`, split by

```text
balanced:          1 < t/r <= L,
highly unbalanced: t/r > L.
```

From

```text
h*ell*(r^2+t^2) <= 4B,
```

high imbalance implies

```text
(1+L^2)r^2 < 4B/(h*ell),
```

hence

```text
boxed:
r < 2/sqrt(1+L^2) * sqrt(B/(h*ell))
  <= 2/L * sqrt(B/(h*ell)).
```

On the balanced branch, `t<=Lr`; combining with the short-gap lemma gives

```text
boxed:
t <= 2L*g*c/H.
```

```text
COVER_IMBALANCE_SPLIT_EXACT=true
HIGH_IMBALANCE_FORCES_SHORT_GAP=true
BALANCED_COVER_CONTROLLED_BY_G_TIMES_C_OVER_H=true
```

## 6. Highly-unbalanced branch becomes Type-I

Fix

```text
(U,epsilon,k,h,kappa,beta,ell,r).
```

Then `A`, `R`, `g_r`, `R0` are fixed. Condition on

```text
g_t=gcd(A,odd(t))
```

and on `v2(t)`. This costs only `tau(A)*O(log B)=B^o(1)`.

The cofactor identity becomes

```text
boxed:
c = H*R0*odd(t)/g_t.
```

Thus `c` is a scaled linear value of the single moving long coordinate `t`. The physical predicates remain

```text
h*ell*(r^2+t^2)<=4B,
t<sqrt(ell),
delta=(r^2+t^2)/(2k),
ell*delta<=Y_U,
fixed (kappa,beta) tag,
reconstructed positive companion.
```

Therefore the highly-unbalanced branch is no longer the genuine two-variable Type-II obstruction.

```text
HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I=true
HIGH_IMBALANCE_TYPE_I_POWER_SAVING_PROVED=false
```

## 7. Genuine post-t75 Type-II block

After stratifying large `g` and reducing the highly-unbalanced branch, the surviving two-variable block has

```text
g small on its dyadic scale,
1 < (q+p)/(q-p) <= L,
gcd(q-p,q+p) in {1,2},
q-p,q+p < sqrt(ell),
h*ell*((q-p)^2+(q+p)^2)<=4B,
```

with exact coprime column data

```text
g=g_r*g_t,
c/H=R0*T0,
gcd(R0,T0)=1,
ell*g*c<2B.
```

The minimal receiver is

```text
SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedShortCoverTypeIIDispersionEnergy
```

and is not closed here.

```text
POST_T75_GENUINE_TWO_VARIABLE_BLOCK_IS_BALANCED_SMALL_G=true
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_SMALL_ANGULAR_GCD_BALANCED_SHORT_COVER_TYPE_II_DISPERSION_ENERGY_PROVED=false
```

## 8. Consumed tH20 audit

Merged tH20 proves

```text
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_DIRECT_EXTERNAL_SIEVE_B_POWER_SAVING_EXPONENT=0
ANGULAR_DIVISOR_SWITCHING_POST_T74_PREFERRED=true
TH21_NEEDED=false
```

and recommends exhausting `g` plus balanced/unbalanced short-factor geometry before introducing a new bilinear-dispersion contract. This matches t75 exactly.

The t75 algebra does not depend on tH20, so tH20 is consumed but not charged as a hard theorem input.

```text
TH20_MERGED=true
TH20_CONSUMED_BY_T75=true
TH20_RESULT_CONSISTENT_WITH_T75=true
TH20_USED_AS_HARD_THEOREM_PREDECESSOR=false
TH21_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
```

## 9. Frozen diagnostics

At `B=10000`:

```text
560 reciprocal states
419 invisible states
419 column-split checks
419 primitive-short-gap checks
419 Type-I linearization checks
419 imbalance checks
4085 independent primitive short-gap regression cases
```

For diagnostic thresholds only

```text
g>=5,
(q+p)/(q-p)>4,
```

one obtains

```text
large-g states             60
balanced states           293
highly-unbalanced states  126
max (q-p)/(g*c/H)           2
max imbalance               9
```

These are regression data, not asymptotic hypotheses.

## 10. Shared exponent and next step

Merged Stage14-X11 proves

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34
```

with a gap to `1/2` equal to `1/17`. t75 itself proves no further global saving.

Stage14-t76 should work only on

```text
SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedShortCoverTypeIIDispersionEnergy
```

and compare the coprime residual columns `R0,T0` with the fixed squareclass/tag root orientation on dyadic `(ell,r,t)` scales.

`tH21` is not needed yet. Open it only if t76 isolates a genuinely new short-cover bilinear phase/kernel not already covered by tH20.

## Locked boundary

```text
STAGE14_T75=COMPLETE_ANGULAR_GCD_COLUMN_SPLIT_PRIMITIVE_SHORT_GAP_AND_TYPE_I_TYPE_II_COVER_REDUCTION
MERGED_T74_IMPORTED=true
MERGED_TH20_IMPORTED=true
MERGED_X11_GLOBAL_19_34_LEDGER_IMPORTED=true
ANGULAR_G_SPLITS_UNIQUELY_ACROSS_COVER_COLUMNS=true
SHORT_COFACTOR_OVER_H_EQUALS_UNCANCELLED_ODD_COLUMN_PRODUCT=true
PRIMITIVE_SHORT_GAP_LEMMA_PROVED=true
LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED=true
LARGE_ANGULAR_G_PAIR_ENERGY_CLOSED=false
COVER_IMBALANCE_SPLIT_EXACT=true
HIGH_IMBALANCE_FORCES_SHORT_GAP=true
HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I=true
HIGH_IMBALANCE_TYPE_I_POWER_SAVING_PROVED=false
POST_T75_GENUINE_TWO_VARIABLE_BLOCK_IS_BALANCED_SMALL_G=true
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_SMALL_ANGULAR_GCD_BALANCED_SHORT_COVER_TYPE_II_DISPERSION_ENERGY_PROVED=false
TH20_MERGED=true
TH20_CONSUMED_BY_T75=true
TH20_USED_AS_HARD_THEOREM_PREDECESSOR=false
TH21_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34
T75_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t76
```
