# Stage14-s7-91 — eliminate the common dilation and expose a primitive coprime divisor-ratio selector

## Status

`COMPLETE_COMMON_DILATION_ELIMINATION_TO_PRIMITIVE_COPRIME_DIVISOR_RATIO_SELECTOR`

Consumes batch-local `Stage14-s7-90`, merged `Stage14-4fg`, and merged `Stage14-Work-brX30`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering primitive-ratio normal form

Stage14-s7-90 gives exactly

```text
n=E*u*v,
gcd(u,v)=1,
|Xr|=alpha*E*u^2,
|Yr|=beta *E*v^2,
h=d0*n,
```

where `alpha,beta,d0` are fixed positive packet coefficients and the inherited squareclass condition is transported through

```text
sqf(E)=J1.
```

All original physical masks remain attached to the same candidate.

## 2. Eliminate E using the normalized radial value

Since

```text
E=n/(u*v),
```

an accepted primitive pair necessarily satisfies

```text
u*v | n.
```

Substitution into the two root factors gives the exact reciprocal formulas

```text
boxed:
|Xr|=alpha*n*(u/v),
|Yr|=beta *n*(v/u).
```

Their product is therefore

```text
|Xr|*|Yr|=alpha*beta*n^2,
```

while the projective ratio is

```text
|Xr|/|Yr|=(alpha/beta)*(u/v)^2.
```

The common dilation no longer appears in the archimedean root-window equations. It is recovered after the primitive pair is chosen by

```text
E=n/(uv).
```

The transported squareclass/gcd masks become conditions on this exact complementary factor `E`.

```text
COMMON_DILATION_ELIMINATED_FROM_ROOT_WINDOWS=true
PRIMITIVE_PAIR_PRODUCT_DIVIDES_N=true
COMPLEMENTARY_DILATION_E=n_over_uv
ROOT_X=alpha_n_u_over_v
ROOT_Y=beta_n_v_over_u
```

## 3. Exact physical ratio-window selector

Within one frozen dyadic/finite physical chart, write the retained root windows as

```text
I_X=[X_-,X_+],
I_Y=[Y_-,Y_+].
```

These are the same transported physical windows used by merged 4fg; any endpoint/chart subdivision costs only `B^o(1)`.

The first root condition is equivalent to

```text
u/v in R_X(n)
 := [X_-/(alpha*n), X_+/(alpha*n)].
```

The second is equivalent to

```text
u/v in R_Y(n)
 := [beta*n/Y_+, beta*n/Y_-].
```

Therefore define the exact primitive ratio window

```text
R_phys(n):=R_X(n) intersect R_Y(n).
```

Then normalized heavy-ray acceptance is equivalent to the existence of positive coprime integers `(u,v)` such that

```text
u*v | n,
u/v in R_phys(n),
E=n/(uv),
sqf(E) satisfies every inherited squareclass/gcd mask,
all remaining primitive/orientation/root-origin/allocation/canonical/reverse-completion masks hold.
```

This preserves the original existential quantifier. No divisor-pair density is assumed.

```text
PHYSICAL_ROOT_WINDOWS_PROJECTED_TO_PRIMITIVE_RATIO=true
PRIMITIVE_RATIO_WINDOW=R_phys_of_n
ORIGINAL_EXISTENTIAL_QUANTIFIER_PRESERVED=true
TRANSPORTED_COMPLEMENTARY_E_MASKS_RETAINED=true
```

## 4. Finite-fiber equivalence with the merged L-coordinate

Merged 4fg / Work-brX30 use

```text
L_s=J1*a1^2.
```

In the s7-90 variables,

```text
L_s=E*u^2=n*(u/v).
```

Thus

```text
u/v=L_s/n.
```

So the primitive ratio selector and the merged reciprocal divisor-window selector are the same arithmetic coordinate after division by `n`; they are not multiplicable counts.

```text
L_s_equals_n_times_u_over_v=true
GLOBAL_S_L_WINDOW_AND_PRIMITIVE_RATIO_COUNTS_MULTIPLICABLE=false
PRIMITIVE_RATIO_REPARAMETRIZES_MERGED_L_COORDINATE=true
```

## 5. H decision

No new `sH` is opened. Before any theorem audit, the next internal stage can determine the exact geometry of `R_phys(n)` and separate the purely archimedean nonemptiness condition from the genuinely arithmetic primitive-divisor-ratio occupancy.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_91_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_91=COMPLETE_COMMON_DILATION_ELIMINATION_TO_PRIMITIVE_COPRIME_DIVISOR_RATIO_SELECTOR
COMMON_DILATION_ELIMINATED_FROM_ROOT_WINDOWS=true
PRIMITIVE_PAIR_PRODUCT_DIVIDES_N=true
PHYSICAL_ROOT_WINDOWS_PROJECTED_TO_PRIMITIVE_RATIO=true
L_s_equals_n_times_u_over_v=true
ORIGINAL_EXISTENTIAL_QUANTIFIER_PRESERVED=true
TRANSPORTED_COMPLEMENTARY_E_MASKS_RETAINED=true
GLOBAL_S_L_WINDOW_AND_PRIMITIVE_RATIO_COUNTS_MULTIPLICABLE=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_91_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-92
```
