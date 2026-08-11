# Stage14-s7-93 — pull the interior physical incidence to the primitive-ratio coordinate and open the complementary-E weight

## Status

`COMPLETE_INTERIOR_PHYSICAL_INCIDENCE_PULLBACK_AND_COMPLEMENTARY_E_WEIGHT_OPENING`

Consumes merged `Stage14-s7-90..92`, merged mainline `Stage14-4fi/4fj`, merged `Stage14-Work-bsX31`, merged q14 only as a literature-routing boundary, and batch-start main

```text
1cce848e748d6b02d7e878c6bd1b326e953bc98c.
```

Only merged results are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Import the already-proved radial endpoint discharge

Fix one surviving heavy exponent cell

```text
n=B^(nu+o(1)),
|N_*|>=B^(mu-o(1)),
0<mu<=nu,
```

and choose the merged 4fi parameter

```text
theta>nu-mu.
```

Merged 4fi proves that the radial product-window endpoint strips carry only `o(B^mu)` outer integers. Hence, on the identical global/s packet identified by Work-bsX31, one may restrict to an interior set

```text
N_int(theta)
```

with

```text
|N_int(theta)|>=B^(mu-o(1)).
```

No second endpoint saving is charged on the s-route.

```text
MERGED_GLOBAL_S_RADIAL_ENDPOINT_DISCHARGE_CONSUMED=true
S_ROUTE_RADIAL_ENDPOINT_SAVING_RECHARGED=false
INTERIOR_OUTER_SUPPORT_EXPONENT=mu
```

## 2. Exact pullback of the merged physical incidence

Merged s7-90..92 gives the bijective coordinate system

```text
n=E*u*v,
gcd(u,v)=1,
E=n/(u*v),
L=n*(u/v)=E*u^2,
|Xr|=alpha*n*(u/v),
|Yr|=beta*n*(v/u).
```

Merged 4fj writes the physical heavy incidence as

```text
I_int
 = sum_{n in N_int(theta)}
   sum_{L in C(n)} w_phys(n,L),
```

where fixed `n` has only `B^o(1)` admissible `L` candidates and every primitive/canonical/reverse-completion mask is retained by `w_phys`.

Pull this weight back through the exact s7-90..92 coordinate map. Define

```text
w_ratio(n,u,v,E)
 := w_phys(n,L=n*u/v)
```

on tuples satisfying

```text
gcd(u,v)=1,
u*v | n,
E=n/(u*v),
u/v in R_phys(n),
```

and set it to zero otherwise. Then exactly, up to only the already-frozen finite labels,

```text
I_ratio
 := sum_{n in N_int(theta)}
    sum_{gcd(u,v)=1, uv|n, u/v in R_phys(n)}
      w_ratio(n,u,v,n/(uv))

 = I_int.
```

Therefore the surviving heavy packet forces

```text
I_ratio>=B^(mu-o(1)).
```

This is a coordinate change, not a new count.

```text
PHYSICAL_INCIDENCE_PULLED_BACK_TO_RATIO_COORDINATE=true
GLOBAL_S_RATIO_AND_L_INCIDENCES_IDENTICAL=true
RATIO_AND_L_COUNTS_MULTIPLICABLE=false
INTERIOR_RATIO_PHYSICAL_INCIDENCE_REQUIRED_EXPONENT=mu
```

## 3. What the complementary E condition actually contains

From s7-90,

```text
E=J1*g^2,
J1=sqf(E).
```

For every positive integer `E`, the decomposition

```text
E=sqf(E) * (sqrt(E/sqf(E)))^2
```

is unique. Consequently the statement that `E` has a squarefree kernel is not a sparse condition and cannot be charged.

The inherited root-kernel coprimality from s7-85 does give the genuine deterministic condition

```text
gcd(sqf(E),K_Z)=1.
```

All remaining fixed-coefficient allocation, primitive/orientation, root-origin, parity/two-primary, canonical and reverse-completion conditions are bundled into a residual Boolean

```text
w_res(n,u,v,E) in {0,1}.
```

Thus one may write exactly

```text
w_ratio(n,u,v,E)
 = 1_{gcd(sqf(E),K_Z)=1}
   * w_res(n,u,v,E),
```

where `w_res` retains every condition not already forced by the normalized coordinate identities.

```text
E_SQUAREFREE_KERNEL_DECOMPOSITION_IS_TAUTOLOGICAL=true
GENERIC_SQUAREFREE_E_DENSITY_RECHARGE_ALLOWED=false
COMPLEMENTARY_E_FIXED_KERNEL_COPRIMALITY_EXPOSED=true
RESIDUAL_CANONICAL_REVERSE_WEIGHT_DEFINED=true
RESIDUAL_WEIGHT_INDEPENDENCE_ASSUMED=false
```

## 4. Receiver and H decision

The arithmetic inner weight has now been opened one layer: the complementary factor `E=n/(uv)` is explicit, its squarefree-kernel coprimality is explicit, and the genuinely unresolved physical content is isolated as `w_res`.

The receiver has not yet materially changed, because the primitive ratio pair `(u,v)` has not been compressed to its intrinsic divisor object. The next internal stage should set `q=uv`, exploit `gcd(u,v)=1`, and determine the exact prime-power orientation structure of the short ratio selector. It must also distinguish this inner-ratio endpoint issue from the already-discharged outer radial endpoints.

No new sH is opened yet. q14's Ford transfer remains premature while `w_res` is still correlated with the same divisor candidate.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_93_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_93=COMPLETE_INTERIOR_PHYSICAL_INCIDENCE_PULLBACK_AND_COMPLEMENTARY_E_WEIGHT_OPENING
MERGED_GLOBAL_S_RADIAL_ENDPOINT_DISCHARGE_CONSUMED=true
PHYSICAL_INCIDENCE_PULLED_BACK_TO_RATIO_COORDINATE=true
GLOBAL_S_RATIO_AND_L_INCIDENCES_IDENTICAL=true
E_SQUAREFREE_KERNEL_DECOMPOSITION_IS_TAUTOLOGICAL=true
COMPLEMENTARY_E_FIXED_KERNEL_COPRIMALITY_EXPOSED=true
RESIDUAL_CANONICAL_REVERSE_WEIGHT_DEFINED=true
INTERIOR_RATIO_PHYSICAL_INCIDENCE_REQUIRED_EXPONENT=mu
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_93_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-94
```