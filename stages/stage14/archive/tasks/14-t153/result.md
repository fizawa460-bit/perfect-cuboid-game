# Stage14-t153 — long-headroom dyadic Gaussian-lattice harmonic capacity

## Status

`COMPLETE_LONG_HEADROOM_DYADIC_LATTICE_HARMONIC_CAPACITY`

Consumes merged Stage14-t152, the fixed ordinary cofactor/prime residues from t135, and latest merged Work-caX39. No global/s adapter is imported.

Keep

```text
X_U = 2B/(h*k0),
L_B = 2*sqrt(B),
q_d = |(Z[i]/dZ[i])^x| = d^2*B^o(1),
R(z) = X_U/(L_B*N(z)).
```

On the long-headroom branch `R(z)>=B^theta` for the already fixed `theta>0`, so `N(z)` is bounded away from the endpoint annulus considered in t150--t152.

For one norm-dyadic shell

```text
Z_N={z : N<N(z)<=2N,
           z primitive,
           z in the frozen open sector,
           z == rho_* (mod d),
           frozen packet labels},
```

the full residue coset `rho_*+d Z[i]` gives the elementary planar lattice bound

```text
#Z_N <= C*(N/d^2 + sqrt(N)/d + 1).
```

Primitivity, sector orientation and packet predicates only remove points.

For each `z in Z_N`, the unrestricted canonical split-prime interval is contained in

```text
L_B < ell <= X_U/N(z) <= X_U/N,
```

so trivially

```text
|P_z| <= X_U/N.
```

Therefore the exact fixed-prime-residue principal baseline on one shell satisfies

```text
M_N
 = 1/q_d * sum_{z in Z_N}|P_z|
 <= C*X_U/q_d
      *(1/d^2 + 1/(d*sqrt(N)) + 1/N).
```

This is the long-headroom analogue of the endpoint double-residue capacity from t151. The main two-dimensional area term is independent of the dyadic cofactor norm:

```text
M_N,area <= C*X_U/(q_d*d^2).
```

There are only `O(log B)=B^o(1)` dyadic shells, so localization in `N` is free at fixed-power scale.

```text
LONG_HEADROOM_DYADIC_SHELL_DEFINED=true
LONG_COFACTOR_FIXED_RESIDUE_LATTICE_COUNT_PROVED=true
LONG_DYADIC_PRINCIPAL_CAPACITY=M_N_LE_XU_OVER_qd_TIMES_(d^-2_plus_d^-1_N^-1/2_plus_N^-1)
LONG_AREA_CAPACITY_INDEPENDENT_OF_DYADIC_N=true
LONG_DYADIC_SHELL_COUNT=Bo1
```

This stage only opens the shell geometry. The area/boundary/singleton alternatives are separated in t154.

```text
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
TH33_NEEDED=false
NEXT=Stage14-t154
```