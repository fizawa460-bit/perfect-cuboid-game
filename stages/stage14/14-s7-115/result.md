# Stage14-s7-115 — split the fixed-E two-sided extension deficit into reciprocal-CRT and residual post-completion deficits

## Status

`COMPLETE_FIXED_E_TWO_SIDED_EXTENSION_DEFICIT_TO_RECIPROCAL_CRT_PLUS_POST_COMPLETION`

Consumes batch-local `Stage14-s7-114`, merged `Stage14-s7-113`, merged mainline `Stage14-4ge`, and merged `Stage14-Work-bzX38 + q17`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Nested extension support on the aligned packet

On the fixed-E two-sided packet let

```text
S_pre = {chi : C_pre(chi)=1}.
```

Using s7-114, define the reciprocal-support subset

```text
S_rec = {chi in S_pre : Omega_rec(chi) nonempty}.
```

The full physical support is

```text
S_phys = {chi in S_rec : C_post(chi)=1},
```

where `C_post` contains exactly the residual root-origin/canonical/post-column acceptance left after one reciprocal/CRT witness exists. This is the same support nesting as merged 4ge, now recorded in the s ledger.

```text
S_FIXED_E_TWO_SIDED_SUPPORT_NESTING_PRE_REC_POST=true
```

## 2. Deficit additivity

Write

```text
#S_pre  = B^(sigma+o(1)),
#S_rec  = B^(rho+o(1)),
#S_phys = B^(tau+o(1)).
```

Define

```text
delta_rec  := sigma-rho >= 0,
delta_post := rho-tau >= 0.
```

Then the s7-113 extension deficit satisfies exactly

```text
delta_ext = delta_rec + delta_post.
```

Consequently, if ambient support has exponent `kappa`, heavy survival on this branch is

```text
kappa-delta_pre-delta_rec-delta_post >= mu.
```

No independence is used; this is nested-support bookkeeping only.

```text
S_FIXED_E_TWO_SIDED_DELTA_EXT_EQUALS_DELTA_REC_PLUS_DELTA_POST=true
S_FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=kappa_minus_delta_pre_minus_delta_rec_minus_delta_post_ge_mu
```

## 3. q17 consumption boundary

Merged q17 found no direct theorem for the exact support

```text
Omega_rec(u,v) nonempty
```

and named direct selector construction and first/second-moment support transfer as the next tests. This result is consumed only as a literature/theorem boundary.

```text
Q17_DIRECT_FULL_THEOREM_CONSUMED=false
Q17_RECIPROCAL_SUPPORT_THEOREM_AVAILABLE=false
Q17_EXPLICIT_CONSTRUCTION_HANDOFF_RELEVANT=true
Q17_MOMENT_TO_SUPPORT_HANDOFF_RELEVANT=true
```

The `B^o(1)` upper bound on `#Omega_rec(chi)` remains only a multiplicity statement and contributes no existence lower bound.

## 4. Near-threshold consequence

On any surviving sequence with

```text
kappa=mu+o(1),
```

nonnegativity forces

```text
delta_pre=o(1),
delta_rec=o(1),
delta_post=o(1).
```

Thus the reciprocal selector and residual post-completion acceptance must each retain full exponent separately on a near-threshold survivor.

## 5. Boundary

This stage refines only the aligned fixed-E two-sided branch. The other s realizations retain the two-level `pre -> existential extension` ledger from s7-113.

```text
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-116
```

## Required locks

```text
STAGE14_S7_115=COMPLETE_FIXED_E_TWO_SIDED_EXTENSION_DEFICIT_TO_RECIPROCAL_CRT_PLUS_POST_COMPLETION
S_FIXED_E_TWO_SIDED_DELTA_EXT_EQUALS_DELTA_REC_PLUS_DELTA_POST=true
Q17_RECIPROCAL_SUPPORT_THEOREM_AVAILABLE=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-116
```
