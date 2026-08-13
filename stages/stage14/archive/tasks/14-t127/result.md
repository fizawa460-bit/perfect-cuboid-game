# Stage14-t127 — freeze the centered projective hyperbola Fourier correlation

## Status

`COMPLETE_CENTERED_NONBOUNDARY_PROJECTIVE_HYPERBOLA_FOURIER_FREEZE`

Consumes Stage14-t126 on the same batch branch together with merged `Stage14-t112`, merged `Stage14-tH26`, and merged `Stage14-tH28` as negative historical applicability boundaries.

Keep the t126 notation

```text
G=G(d),
g=|G|=B^o(1),
X_U=2B/(h*k0),
L_B=2*sqrt(B),
```

and the charged-once nonboundary physical primitive cofactor family `Omega_nb`.

Define centered cumulative cofactor-class discrepancy

```text
E_c(y):=F_c(y)-F(y)/g.
```

Then exactly

```text
sum_{c in G} E_c(y)=0
```

for every `y`.

By the t126 transposition,

```text
T-M
 = sum_{pi_ell: ell>L_B}
     E_[pi_ell](X_U/ell).
```

Thus near-total selected-class depletion is exactly a negative cumulative cofactor-class discrepancy sampled along the moving Gaussian-prime projective class on the reciprocal hyperbola.

## Finite Fourier form

The class-matching relation is

```text
[gamma]*[a]*[pi_ell]=1 in G.
```

Character orthogonality gives the exact identity

```text
1_{[gamma][a][pi_ell]=1}
 = 1/g * sum_{chi in G^}
     chi([gamma]) chi([a]) chi([pi_ell]).
```

Therefore

```text
T
 = M + D,
```

with

```text
D
 = 1/g * sum_{chi != 1}
       chi([a])
       sum_{
         gamma in Omega_nb,
         pi_ell canonical split,
         ell>L_B,
         N(gamma)*ell<=X_U
       }
       chi([gamma]) chi([pi_ell]).
```

All packet restrictions are retained in `Omega_nb`; no absolute value has been applied before the principal/nonprincipal separation.

The principal character is exactly the t112/t126 baseline `M`.  Consequently a fixed-power selected-class depletion

```text
T <= B^(-delta) M
```

forces the aggregate nonprincipal Fourier contribution to satisfy

```text
D <= -(1-B^(-delta)) M.
```

In particular the remaining obstruction is not ordinary small equidistribution error.  It is a principal-scale negative bilinear correlation on the exact Gaussian cofactor/prime hyperbola.

## Why a fresh theorem audit is now justified

Merged tH26 was negative partly because the cofactor coefficient retained an opaque nonmultiplicative physical selector `c_U(gamma)`.  The t91--t124 chain has since:

- parameterized primitive generic representations exactly;
- confined packet-local interactions to a `B^o(1)` exceptional support;
- removed the finite D4/sign-normalization obstruction from the live nonboundary family;
- separated the projective prime selector from the cofactor core;
- reduced the moving prime interval to the exact nested hyperbola above.

The remaining object is therefore sufficiently explicit for a new independent audit.  The audit must not assume multiplicativity of the full nonboundary cofactor indicator; it must test whether existing Gaussian/Hecke bilinear, dispersion, large-sieve, prime-ideal, or projective/Kloosterman technology applies to this exact hyperbola with `d=B^o(1)` and the retained primitive/nonboundary physical support.

This is an exact theorem-ready coordinate freeze of the same selected-class depletion mechanism, not a new arithmetic mechanism; hence the minimal receiver has not materially changed yet.

```text
CENTERED_COFACTOR_CLASS_DISCREPANCY_DEFINED=true
SELECTED_DEPLETION_EQUALS_CENTERED_PROJECTIVE_HYPERBOLA_CORRELATION=true
PROJECTIVE_HYPERBOLA_FINITE_FOURIER_EXPANSION_EXACT=true
PRINCIPAL_CHARACTER_EQUALS_T126_BASELINE=true
FIXED_POWER_DEPLETION_REQUIRES_PRINCIPAL_SCALE_NEGATIVE_FOURIER_CORRELATION=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=FixedPacketNonboundaryPrimitiveGaussianCofactorPrimeProjectiveHyperbolaDispersion
T_ROUTE_H_TARGET=stages/stage14/14-t127/th29-target.md
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=true
PREFERRED_RECEIVER=SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion
NEXT=Stage14-tH29
```
