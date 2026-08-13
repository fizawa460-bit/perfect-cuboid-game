# Stage14-t154 — long-headroom sparse/area lattice split and one-cofactor freeze

## Status

`COMPLETE_LONG_HEADROOM_SPARSE_AREA_LATTICE_SPLIT_AND_SINGLE_COFACTOR_FREEZE`

Consumes Stage14-t153.

The t153 shell capacity is

```text
M_N <= C*X_U/q_d
       *(1/d^2 + 1/(d*sqrt(N)) + 1/N).
```

## 1. Area regime

If

```text
N >= d^2,
```

then

```text
1/(d*sqrt(N)) <= 1/d^2,
1/N <= 1/d^2.
```

Hence the whole shell is controlled by the area term:

```text
M_N <= C*X_U/(q_d*d^2).
```

No boundary receiver survives separately at fixed-power scale.

If a long area shell can carry principal-scale mass

```text
M_N >= B^(1/2-o(1)),
```

then necessarily

```text
X_U/(q_d*d^2) >= B^(1/2-o(1)),
```

or, using `X_U=2B/(h*k0)`,

```text
boxed:
h*k0*q_d*d^2 <= B^(1/2+o(1)).
```

Since `q_d=d^2*B^o(1)`, equivalently

```text
h*k0*d^4 <= B^(1/2+o(1)).
```

This is a necessary host/modulus compatibility condition, not yet a fixed-power saving because `d=B^o(1)`.

## 2. Sparse small-norm regime

If

```text
N < d^2,
```

then the disk `N(z)<2d^2` has Euclidean radius `O(d)`. A single residue coset `rho_*+d Z[i]` has only `O(1)` lattice points in such a disk. Therefore all long shells below `d^2` together contain only `O(1)` actual cofactors after the frozen sector/packet filters.

A fixed-power depleted principal long mass on this regime localizes nonnegatively to one actual cofactor `z_*` exactly as in t148. Put `n_*=N(z_*)`. Its principal baseline satisfies

```text
M_{z_*}
 <= X_U/(q_d*n_*).
```

Thus principal scale requires

```text
X_U/(q_d*n_*) >= B^(1/2-o(1)),
```

or

```text
boxed:
n_* <= B^(1/2+o(1))/(h*k0*q_d).
```

In headroom form, since `N_0=sqrt(B)/(h*k0)` and `R_*=N_0/n_*`, this gives

```text
boxed:
R_* >= q_d*B^(-o(1)).
```

So a sparse long survivor is forced to have residue-group-sized headroom.

```text
LONG_AREA_REGIME=N_GE_d2
LONG_AREA_PRINCIPAL_CAPACITY=XU_OVER_qd_d2
LONG_AREA_PRINCIPAL_COMPATIBILITY=hk0_qd_d2_LE_BsHalfPlusO1
LONG_BOUNDARY_SEPARATE_RECEIVER=false
LONG_SPARSE_REGIME=N_LT_d2
LONG_SPARSE_TOTAL_ACTUAL_COFACTORS=O(1)
LONG_SPARSE_FIXED_POWER_DEPLETION_LOCALIZES_TO_ONE_COFACTOR=true
LONG_SPARSE_HEADROOM_FLOOR=qd_TIMES_BminusO1
```

The prime-distribution theorem boundary has not changed yet. Stage14-t155 tests the already-audited Mitsui/Kai theorem at the actual upper norm scale of each long cofactor rather than at the uniform endpoint scale.

```text
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
TH33_NEEDED=false
NEXT=Stage14-t155
```