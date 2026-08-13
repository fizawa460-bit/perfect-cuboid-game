# Stage14-t106 — expose boundary-bearing canonical-LPF Q support incidence

## Status

`COMPLETE_BOUNDARY_BEARING_Q_SUPPORT_INCIDENCE_DECOMPOSITION`

Consumes merged Stage14-t105, merged Stage14-t91/t89, and merged Stage14-Work-blX24 from latest main. Unmerged descendants are advisory only.

The fixed-U packet and canonical-LPF kernel remain

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
all odd p|Q => p==1 mod 4,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
0<=omega_B(Q)<=B^o(1).
```

Merged t105 defines `omega_B(Q)` as the number of accepted labels in the complete fixed-Q Gaussian background fiber. Therefore, exactly,

```text
omega_B(Q)>0
<=>
there exists a background label x in Omega_Q with b_Q(x)=1.
```

Define the charged-once incidence set

```text
I_B := {(Q,x): Q satisfies the canonical-LPF kernel,
               x in Omega_Q,
               b_Q(x)=1}.
```

and its scalar projection

```text
S_B := proj_Q(I_B).
```

Then

```text
S_B={Q:omega_B(Q)>0},
|I_B|=sum_Q omega_B(Q),
|S_B| <= |I_B| <= |S_B| B^o(1).
```

Thus the positive principal branch is, up to `B^o(1)`, exactly the cardinality of a scalar support projection. No inner-fiber density, multiplicity, or selector entropy may be charged again.

This removes the last ambiguity in treating `omega_B(Q)` as an arbitrary positive bounded weight: for saving purposes only its zero/nonzero support is polynomially relevant; all positive values are subpolynomial multiplicity.

```text
BOUNDARY_BEARING_Q_INCIDENCE_SET_DEFINED=true
BOUNDARY_BEARING_Q_SUPPORT_IS_EXACT_PROJECTION=true
POSITIVE_Q_WEIGHT_REDUCES_TO_SUPPORT_UP_TO_BO1=true
INNER_FIBER_MULTIPLICITY_RECHARGE_FORBIDDEN=true
FIXED_U_Q_SUPPORT_SPARSE_POWER_PROVED=false
```

The receiver is refined, not materially changed: it is still the boundary-bearing canonical-LPF Q support, now represented as a projection of the exact physical incidence relation.

## tH decision

No new theorem class is exposed yet; the incidence predicate still contains the complete Q-dependent Gaussian label.

```text
TH28_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUStrongGapCanonicalLPFBoundaryBearingQSupportProjection
NEXT=Stage14-t107
```
