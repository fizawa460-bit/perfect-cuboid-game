# Stage14-t112 — exact selected-class principal/centered decomposition

## Status

`COMPLETE_SELECTED_PROJECTIVE_CLASS_PRINCIPAL_CENTERED_DECOMPOSITION`

Consumes merged Stage14-t111 and merged Stage14-Work-bnX26.  No positive saving is imported from tH26 or tH28.

Fix a live fixed-U packet, one allowed norm-`k0` Gaussian factor `a`, and the merged endpoint modulus

```text
d=B^o(1),
G=G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x.
```

For a primitive cofactor `gamma` with

```text
n=N(gamma),
C_U(a,gamma)=1,
c(a,gamma)=([gamma][a])^(-1) in G,
```

let `P_gamma` be the set of canonical split Gaussian prime labels `pi_ell` with rational norm `ell` in the exact t109 physical interval

```text
I_B(n)=
(max(2*sqrt(B),2*h*k0*n), 2B/(h*k0*n)]
```

and satisfying the already-merged coprimality/unit conventions.  For `c in G`, define

```text
K_gamma(c)
 := # {pi in P_gamma : [pi]=c}.
```

Because projective classes partition `P_gamma`,

```text
sum_{c in G} K_gamma(c)=|P_gamma|.
```

Define the exact uniform-class principal level and centered discrepancy

```text
A_gamma := |P_gamma|/|G|,
Delta_gamma(c):=K_gamma(c)-A_gamma.
```

Then

```text
sum_{c in G} Delta_gamma(c)=0
```

and the number of physical dominant-prime completions of this cofactor is exactly

```text
K_gamma(c(a,gamma))
 = A_gamma + Delta_gamma(c(a,gamma)).
```

After summing over any charged-once cofactor block `Omega`, the fixed-U physical count is therefore

```text
T_Omega
 = M_Omega + D_Omega,

M_Omega
 := sum_{(a,gamma) in Omega}
      C_U(a,gamma) A_gamma,

D_Omega
 := sum_{(a,gamma) in Omega}
      C_U(a,gamma)
      Delta_gamma(c(a,gamma)).
```

This is an exact decomposition.  Equivalently, finite Fourier inversion on `G` gives

```text
1_{[pi]=c(a,gamma)}
 = 1/|G|
   + 1/|G| sum_{chi != 1}
       chi([pi]) conjugate(chi(c(a,gamma))),
```

which is the t90 endpoint-character expansion after the t109 cofactor core has been frozen explicitly.

Since

```text
|G|=B^o(1),
```

the principal factor `1/|G|` is only `B^(-o(1))`; projective-class averaging does not itself furnish a fixed `B^-delta` loss.

```text
SELECTED_CLASS_PRINCIPAL_CENTERED_DECOMPOSITION_EXACT=true
CLASS_DISCREPANCY_HAS_ZERO_CLASS_MEAN=true
FIXED_U_COUNT_EQUALS_PRINCIPAL_PLUS_SELECTED_CLASS_DISCREPANCY=true
PROJECTIVE_PRINCIPAL_FACTOR=BoMinus1
PROJECTIVE_PRINCIPAL_FACTOR_FIXED_POWER_SAVING=false
CENTERED_PROJECTIVE_CORRELATION_EXPOSED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUPrimitiveCofactorCorePrincipalPrimeMassPlusSelectedClassDiscrepancy
NEXT=Stage14-t113
```
