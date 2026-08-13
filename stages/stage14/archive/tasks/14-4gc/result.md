# Stage14-4gc — pull fixed-E completion support back to the primitive rectangular pair incidence

## Status

`COMPLETE_FIXED_E_COMPLETION_OUTER_SUPPORT_TO_PRIMITIVE_PAIR_INCIDENCE_PULLBACK`

Consumes only merged theorem sources from batch-start main

```text
a0c01e4f1236e2a3c1f718f056fee6d4f1c73e20
```

namely merged `Stage14-4fz..4gb`, merged `Stage14-s7-108..110`, merged `Stage14-q16`, and merged `Stage14-Work-byX37`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the completion-only fixed-E principal rectangle

Freeze one exact fixed-complementary-dilation principal packet

```text
E=E0,
D,V fixed integer factor windows,
#D=B^(kappa_D+o(1)),
#V=B^(kappa_V+o(1)),
kappa:=kappa_D+kappa_V>=mu-o(1).
```

Merged 4ga/4gb proves that the actual primitive/unitary bare pair set

```text
R_prim
 := {(u,v): u in D, v in V, gcd(u,v)=1}
```

has

```text
#R_prim=B^(kappa+o(1)),
```

and that its outer product image also has the same fixed-power exponent.  For an outer product `m=uv`, merged 4gb defines the physical completion Boolean `C_phys(m)` and the survival budget

```text
# {m:C_phys(m)=1}=B^(tau_phys+o(1)),
delta_comp=kappa-tau_phys,
kappa-delta_comp>=mu.
```

## 2. Define the exact pair-level completion Boolean

For an exact primitive pair `(u,v) in R_prim`, define

```text
C_pair(u,v)=1
```

iff **that exact representation** `m=uv`, with the frozen fixed-E/ray/agreement/chart data, admits at least one full Stage14 physical completion satisfying every canonical, root-origin, allocation, parity/two-primary, reverse and post-column condition retained by merged 4gb.

Then the outer completion support is exactly the image of the accepted pair incidence:

```text
T_pair := {(u,v) in R_prim : C_pair(u,v)=1},
S_phys := {uv : (u,v) in T_pair}.
```

No condition is discarded by this pullback.  It only restores the representation that was existentially quantified in the outer Boolean.

```text
PAIR_LEVEL_COMPLETION_BOOLEAN_DEFINED=true
OUTER_COMPLETION_SUPPORT_IS_ACCEPTED_PAIR_PRODUCT_IMAGE=true
PHYSICAL_MASK_DROPPED=false
```

## 3. Product fibers are subpolynomial, so the completion exponent is preserved

For every polynomially bounded outer product `m`,

```text
# {(u,v) in D x V : uv=m}
 <= tau(m)
 = B^o(1).
```

Hence also on the primitive subset,

```text
#S_phys <= #T_pair <= B^o(1)*#S_phys.
```

Therefore if

```text
#T_pair=B^(tau_pair+o(1)),
```

then exactly at fixed-power scale

```text
tau_pair=tau_phys.
```

The completion deficit may equivalently be measured on primitive pair incidences:

```text
delta_comp=kappa-tau_pair.
```

Thus the survival condition remains

```text
kappa-delta_comp>=mu.                              (1)
```

This is a support-coordinate equivalence, not a second multiplicative saving and not an independence statement.

```text
FIXED_E_ACCEPTED_PAIR_TO_OUTER_PRODUCT_FIBER=Bo1
FIXED_E_COMPLETION_SUPPORT_EXPONENT_PRESERVED_UNDER_PAIR_PULLBACK=true
FIXED_E_COMPLETION_DEFICIT_RECHARGED=false
```

## 4. Why the pair coordinate is the correct place to open completion

On fixed `E0`, the normalized radial/root coordinates already used by merged 4fw are

```text
m=u*v,
n=E0*u*v,
|Xr|=alpha*E0*u^2,
|Yr|=beta*E0*v^2,
```

with fixed positive packet coefficients `alpha,beta`.  The radial scale is likewise fixed by the pair through

```text
h=d0*n=d0*E0*u*v.
```

Thus every integer entering the reverse reciprocal reconstruction is an exact function of `(u,v)` plus only already-frozen `B^o(1)` packet labels.  Keeping only `m` obscures this structure; pulling back to `(u,v)` exposes it without changing the exponent ledger.

The next stage will substitute these formulas into the exact reciprocal equations and separate the bare reciprocal divisor/CRT solvability from the remaining root/canonical/post-column filter.

## 5. H decision

No new heavy main H is opened at this coordinate-pullback stage.  The arithmetic species of `C_pair` must first be written explicitly.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4gd
```

## Boundary

```text
STAGE14_4GC=COMPLETE_FIXED_E_COMPLETION_OUTER_SUPPORT_TO_PRIMITIVE_PAIR_INCIDENCE_PULLBACK
PAIR_LEVEL_COMPLETION_BOOLEAN_DEFINED=true
FIXED_E_ACCEPTED_PAIR_TO_OUTER_PRODUCT_FIBER=Bo1
FIXED_E_COMPLETION_SUPPORT_EXPONENT_PRESERVED_UNDER_PAIR_PULLBACK=true
FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=kappa_minus_delta_comp_ge_mu
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4gd
```