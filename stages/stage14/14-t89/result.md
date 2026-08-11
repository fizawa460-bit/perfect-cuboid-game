# Stage14-t89 — restore the full fixed-U prime/cofactor gap and absorb short-cover archimedean masks into a bounded Q-weight

## Status

`COMPLETE_STRONG_FIXED_U_Q_GAP_AND_SHORT_COVER_MASK_ABSORPTION`

Stage14-t89 consumes merged Stage14-t88, merged Stage14-t87, and the completed immutable Stage14-tH25 snapshot.  The tH25 target is not edited or reopened.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

The purpose of t89 is to translate the strongest surviving physical completion masks into the one-dimensional `Q` coordinates from t88.  The key point is that t88 used only the weakened separation `ell>2*k0*delta0`; the older exact fixed-`U` inequality from t65 is stronger.  Restoring that inequality makes the short-cover coordinate bounds and the t74/t75/t78 angular hyperbolas automatic.  All remaining completion data are therefore representation-local arithmetic selectors on a `B^o(1)` fixed-`Q` Gaussian fiber.

---

## 1. Imported t88 packet

Fix

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
m=N(U),
h*k=epsilon*m,
```

together with the reciprocal/inversion orientation and the t86 two-primary branch

```text
eta in {1,2},
delta=eta*delta0,
k0=eta*k.
```

Merged t88 gives

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
delta0=Q/ell,
```

and, on the only t87-unsaved selector-conductor branch,

```text
d=B^o(1).
```

For a fixed Gaussian factor

```text
a=A+iB,
N(a)=k0,
```

and one primitive cofactor representation

```text
gamma=u+i*v,
N(gamma)=delta0,
```

t88 identifies the oriented cover as

```text
W_sigma=a*gamma=p-i*sigma*q.
```

The full fixed-packet fiber over one `Q` is already `B^o(1)`.

```text
MERGED_T88_IMPORTED=true
MERGED_TH25_CONSUMED=true
TH25_TARGET_REOPENED=false
```

---

## 2. Restore the full t65 separation

Merged t65 proves the exact fixed-`U` inequality

```text
ell > 2*epsilon*m*delta.
```

Using

```text
epsilon*m=h*k,
delta=eta*delta0,
k0=eta*k,
```

this becomes

```text
boxed:
ell > 2*h*k0*delta0.                              (2.1)
```

This is strictly stronger than the weakened inequality used in t88 whenever `h>1`.

Multiplying by `ell` and using `Q=ell*delta0` gives the strong scalar gap

```text
boxed:
ell^2 > 2*h*k0*Q.                                (2.2)
```

Since

```text
h*k0 = eta*epsilon*m,
```

we may also write

```text
ell^2 > 2*eta*epsilon*m*Q.                         (2.3)
```

The original physical budget

```text
epsilon*ell*m*delta/2 <= B
```

becomes exactly

```text
boxed:
h*k0*Q <= 2B.                                     (2.4)
```

Equivalently this is the t88 interval

```text
eta*Q <= Y_U=2B/(epsilon*m).
```

```text
FULL_T65_FIXED_U_SEPARATION_RESTORED=true
STRONG_Q_LPF_GAP=ell^2>2*h*k0*Q
Q_BUDGET_EQUIVALENCE=h*k0*Q<=2B
```

---

## 3. Exact fixed linear-form chart for the short cover

Write

```text
a=A+iB,
gamma=u+i*v.
```

Then

```text
a*gamma=(A*u-B*v)+i*(A*v+B*u).
```

Because

```text
W_sigma=p-i*sigma*q,
```

we have

```text
p=A*u-B*v,
q=-sigma*(A*v+B*u).                                (3.1)
```

Define the physical short-cover coordinates

```text
r=q-p,
t=q+p.                                             (3.2)
```

Thus `(r,t)` is obtained from `(u,v)` by two fixed integral linear forms.  The coefficient matrix has determinant

```text
boxed:
|det((u,v)->(r,t))|=2*(A^2+B^2)=2*k0.              (3.3)
```

Also

```text
boxed:
r^2+t^2=2*(p^2+q^2)=2*k0*delta0.                  (3.4)
```

This chart is exact for both orientations `sigma=+-1`.

```text
COVER_LINEAR_FORM_CHART_PROVED=true
COVER_LINEAR_FORM_DETERMINANT=2*k0
SHORT_COVER_NORM_IDENTITY=r^2+t^2=2*k0*delta0
```

---

## 4. The short-coordinate bounds are automatic

By (2.1) and (3.4),

```text
r^2+t^2=2*k0*delta0 < ell/h <= ell.
```

Hence

```text
boxed:
|r|<sqrt(ell),
|t|<sqrt(ell).                                     (4.1)
```

Therefore the short-coordinate constraints carried from t74 onward no longer need to be imposed independently on the t88 survivor.  They follow from the strong fixed-`U` gap.

```text
T74_SHORT_R_T_BOUNDS_AUTOMATIC_FROM_STRONG_Q_GAP=true
```

---

## 5. The angular hyperbolas are automatic

Because a physical cover has nonzero `p,q`,

```text
|r*t|=|q^2-p^2| < p^2+q^2=k0*delta0.              (5.1)
```

Let

```text
H=odd(h),
Rr=odd(r),
Tt=odd(t).
```

Then

```text
Rr*Tt=odd(r*t) <= |r*t|.
```

Merged t75/t78 define the angular gcd `g` and short cofactor `c` by

```text
g*c=H*Rr*Tt,
c=H*Rr*Tt/g.                                      (5.2)
```

Using `H<=h`, (5.1), and (2.1),

```text
c <= H*Rr*Tt
  < h*k0*delta0
  < ell/2.                                         (5.3)
```

Therefore

```text
boxed:
2*c<ell.                                           (5.4)
```

Multiplying (5.2) by `ell` and using (2.4),

```text
ell*c < h*k0*Q <= 2B,                              (5.5)
```

and more strongly

```text
boxed:
ell*g*c
 = ell*H*Rr*Tt
 < h*k0*Q
 <= 2B.                                            (5.6)
```

Thus the sharp t74/t75/t78 archimedean constraints

```text
2*c<ell,
ell*c<2B,
ell*g*c<2B,
ell*H*Rr*Tt<2B,
r,t<sqrt(ell)
```

are all consequences of the strong `Q` gap plus the single scalar budget `h*k0*Q<=2B`.

They remain true physical statements, but they are no longer independent thinness conditions in the t88 coordinates.

```text
T74_SHORT_COFACTOR_BOUND_AUTOMATIC=true
T74_ELL_C_HYPERBOLA_AUTOMATIC=true
T75_T78_ANGULAR_HYPERBOLA_AUTOMATIC=true
SHORT_COVER_ARCHIMEDEAN_MASKS_CHARGED_SEPARATELY=false
```

---

## 6. What physical selectors remain

After Sections 2--5, the genuinely nonautomatic completion data are arithmetic/local rather than archimedean:

```text
primitive cover / gcd masks,
fixed kappa and beta tag,
reciprocal and inversion orientation,
angular gcd / four-cell allocation labels,
endpoint-small projective selector d|Im(a*w),
positivity and canonical unit conventions.
```

For fixed `Q`, t88 gives only `B^o(1)` possible primitive Gaussian representations

```text
w=gamma*pi,
N(w)=Q,
```

and only `B^o(1)` choices for `a` of norm `k0`.  Each of the remaining selectors is evaluated on one such finite label; none creates a new polynomially long variable.

Define the exact physical representation weight

```text
omega_U(Q)
 := # {fixed-packet Gaussian labels above Q satisfying every remaining
       arithmetic/local completion mask}.                         (6.1)
```

Then uniformly

```text
boxed:
0 <= omega_U(Q) <= B^o(1).                         (6.2)
```

A concrete divisor envelope is

```text
omega_U(Q)
 <= O(1)*r_2(k0)*r_2(delta0)
 <= B^o(1).                                         (6.3)
```

The endpoint projective group has `B^o(1)` size and is absorbed into the same weight.

```text
ALL_REMAINING_PHYSICAL_MASKS_ARE_REPRESENTATION_LOCAL=true
PHYSICAL_COMPLETION_BOUNDED_Q_WEIGHT_PROVED=true
PHYSICAL_Q_WEIGHT_SUP_NORM=Bo1
NO_INDEPENDENT_SHORT_COVER_ARCHIMEDEAN_SUM_REMAINS=true
```

---

## 7. Final one-dimensional weighted kernel

For a fixed packet, the surviving count is now exactly dominated by

```text
sum_Q omega_U(Q) * 1_{Q satisfies canonical-LPF kernel},           (7.1)
```

where

```text
ell=P(Q)=LPF(Q),
v_ell(Q)=1,
delta0=Q/ell,
all odd p|Q => p==1 mod 4,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
d=B^o(1),
0<=omega_U(Q)<=B^o(1).                              (7.2)
```

Hence on `Q~X`,

```text
N_packet(Q~X) <= X*B^o(1).                          (7.3)
```

This is stronger structurally than t88: no separate short-cover ellipse, angular hyperbola, or short-cofactor inequality remains to be carried as an independent analytic mask.

The residual difficulty is not a two-dimensional cover problem.  It is the distribution of a bounded but structured arithmetic weight `omega_U(Q)` on the canonical largest-prime sequence (7.2).

```text
ONE_DIMENSIONAL_WEIGHTED_Q_KERNEL_PROVED=true
SHORT_COVER_ARCHIMEDEAN_GEOMETRY_ELIMINATED_FROM_LIVE_RECEIVER=true
```

No fixed-power saving follows from the bound `omega_U(Q)<=B^o(1)` alone.  An arbitrary bounded weight could occupy every admissible `Q`, so no external sieve theorem should yet be claimed applicable.

```text
T89_FIXED_U_PACKET_POWER_SAVING_PROVED=false
```

---

## 8. tH decision

The completed tH25 snapshot remains final:

```text
TH25_COMPLETE=true
TH25_TARGET_REOPENED=false
TH25_REAUDIT_REQUESTED=false
```

A new tH26 is still premature.  The remaining object contains the structured bounded weight `omega_U(Q)`, but t89 has not yet exposed a theorem-ready centered, multiplicative, bilinear, or trace-function formula for that weight.

The correct next internal task is to open the arithmetic selectors inside `omega_U(Q)` once, identify which are automatic/divisor-local and which produce a genuine correlation in `Q`, and only then decide whether a new immutable H snapshot is warranted.

```text
TH26_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## 9. Preferred receiver

```text
SharedUStrongGapCanonicalLPFBoundedGaussianRepresentationWeightEnergy
```

with kernel

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
all odd p|Q => p==1 mod 4,
d=B^o(1),
0<=omega_U(Q)<=B^o(1).
```

The short-cover archimedean conditions are consequences, not additional factors.

---

## 10. Global ledger

Merged X15 confirms that the current whole-family theorem remains square-root and that fixed-`U` savings/reductions cannot be cross-promoted without a charged-once adapter.  Stage14-t89 proves no such adapter.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T89_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
NEXT=Stage14-t90
```

---

## Locked boundary

```text
STAGE14_T89=COMPLETE_STRONG_FIXED_U_Q_GAP_AND_SHORT_COVER_MASK_ABSORPTION
MERGED_T88_IMPORTED=true
MERGED_TH25_CONSUMED=true
FULL_T65_FIXED_U_SEPARATION_RESTORED=true
STRONG_Q_LPF_GAP=ell^2>2*h*k0*Q
Q_BUDGET_EQUIVALENCE=h*k0*Q<=2B
COVER_LINEAR_FORM_CHART_PROVED=true
COVER_LINEAR_FORM_DETERMINANT=2*k0
SHORT_COVER_NORM_IDENTITY=r^2+t^2=2*k0*delta0
T74_SHORT_R_T_BOUNDS_AUTOMATIC_FROM_STRONG_Q_GAP=true
T74_SHORT_COFACTOR_BOUND_AUTOMATIC=true
T74_ELL_C_HYPERBOLA_AUTOMATIC=true
T75_T78_ANGULAR_HYPERBOLA_AUTOMATIC=true
SHORT_COVER_ARCHIMEDEAN_MASKS_CHARGED_SEPARATELY=false
ALL_REMAINING_PHYSICAL_MASKS_ARE_REPRESENTATION_LOCAL=true
PHYSICAL_COMPLETION_BOUNDED_Q_WEIGHT_PROVED=true
PHYSICAL_Q_WEIGHT_SUP_NORM=Bo1
ONE_DIMENSIONAL_WEIGHTED_Q_KERNEL_PROVED=true
SHORT_COVER_ARCHIMEDEAN_GEOMETRY_ELIMINATED_FROM_LIVE_RECEIVER=true
T89_FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH25_COMPLETE=true
TH25_TARGET_REOPENED=false
TH26_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T89_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
PREFERRED_RECEIVER=SharedUStrongGapCanonicalLPFBoundedGaussianRepresentationWeightEnergy
NEXT=Stage14-t90
```
