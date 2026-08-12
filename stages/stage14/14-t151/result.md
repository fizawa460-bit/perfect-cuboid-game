# Stage14-t151 — double-residue normalized Gaussian annulus principal capacity

## Status

`COMPLETE_DOUBLE_RESIDUE_NORMALIZED_GAUSSIAN_ANNULUS_CAPACITY`

Consumes Stage14-t150 on this batch branch together with merged `Stage14-t147/t149` and the exact t135 fixed-prime-residue baseline.

Write

```text
q_d := |R_d| = |(Z[i]/dZ[i])^x|.
```

Merged t147 gives exactly

```text
q_d = product_{p|d}(p-1)(p-chi_4(p)),
q_d=d^2*B^o(1).
```

For one endpoint layer `Z(Y)`, Stage14-t150 gives

```text
#Z(Y)
 <= C*(
      Y/(h*k0*d^2)
      + B^(1/4)/(d*sqrt(h*k0))
      + 1 ).                                      (1.1)
```

## 1. Insert the fixed prime-residue denominator

For each `z in Z(Y)`, the unrestricted canonical split-prime interval has additive length `O(Y+1)`, hence

```text
|P_z| <= C*(Y+1).
```

The exact principal ordinary-residue baseline is

```text
M_Y = 1/q_d * sum_{z in Z(Y)} |P_z|.
```

Combining with (1.1),

```text
boxed:
M_Y
 <= C*(Y+1)/q_d * (
      Y/(h*k0*d^2)
      + B^(1/4)/(d*sqrt(h*k0))
      + 1 ).                                      (1.2)
```

For polynomially large live endpoint widths the three terms are

```text
A_area
 := Y^2/(q_d*h*k0*d^2),

A_boundary
 := Y*B^(1/4)/(q_d*d*sqrt(h*k0)),

A_single
 := Y/q_d.                                        (1.3)
```

The two appearances of the selector modulus are genuinely different and are both charged exactly once:

- `d^-2` in `A_area` is the density of the fixed **cofactor** Gaussian lattice coset;
- `q_d^-1=d^-2*B^o(1)` is the principal density of the fixed **prime** Gaussian residue.

```text
COFACTOR_RESIDUE_DENSITY_CHARGED=true
PRIME_RESIDUE_DENSITY_CHARGED=true
DOUBLE_RESIDUE_NORMALIZED_CAPACITY_PROVED=true
DOUBLE_RESIDUE_AREA_TERM=Y2_over_qd_hk0_d2
DOUBLE_RESIDUE_BOUNDARY_TERM=Y_Bquarter_over_qd_d_sqrtHK0
DOUBLE_RESIDUE_SINGLETON_TERM=Y_over_qd
```

## 2. The boundary term is not a new fixed-power receiver

The ratio of the area term to the boundary term is exactly, up to fixed constants,

```text
A_area/A_boundary
 = Y/(B^(1/4)*d*sqrt(h*k0)).                       (2.1)
```

Suppose the boundary term itself has principal fixed-power size

```text
A_boundary >= B^(1/2-o(1)).                       (2.2)
```

Then

```text
Y
 >= B^(1/4-o(1))*q_d*d*sqrt(h*k0).                (2.3)
```

Substituting (2.3) into (2.1) gives

```text
A_area/A_boundary >= q_d*B^(-o(1))=B^o(1).        (2.4)
```

Thus at the Stage14 fixed-power exponent ledger the boundary term cannot create a distinct positive-power obstruction: whenever it reaches principal scale, the area term is of the same fixed-power exponent or larger.  No quantitative pseudopolynomial comparison is claimed beyond that exponent statement.

```text
LATTICE_BOUNDARY_NEW_FIXED_POWER_RECEIVER=false
LATTICE_BOUNDARY_ABSORBED_IN_AREA_AT_FIXED_POWER_SCALE=true
```

## 3. The singleton term is exactly the sparse near-full mechanism

If

```text
A_single >= B^(1/2-o(1)),
```

then necessarily

```text
boxed:
Y/q_d >= B^(1/2-o(1)).                             (3.1)
```

This is the exact-group-order version of t149's sparse condition `H/d^2 >= B^(1/2-o(1))`.

It corresponds to only subpolynomially many relevant cofactors, including the one-cofactor localization from t148; it is not merged with the genuinely two-dimensional annulus-area mechanism.

```text
SPARSE_NEARFULL_EXACT_QD_NORMALIZATION_PROVED=true
SPARSE_NEARFULL_NECESSARY_CONDITION=Y_over_qd_GE_BsHalfMinusO1
```

## 4. The only non-nearfull principal endpoint mechanism is the area term

Outside the singleton/sparse near-full alternative, a principal endpoint layer must therefore satisfy at fixed-power scale

```text
A_area >= B^(1/2-o(1)),
```

that is

```text
Y^2/(q_d*h*k0*d^2) >= B^(1/2-o(1)).               (4.1)
```

The explicit width consequence is deferred to t152, where it will be compared to the merged t149 floor and the beyond-Mitsui host relation.

This stage changes the capacity formula but defers publication of the new receiver until the strengthened width floor is stated once in t152.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT_INTERNAL_TARGET=GaussianLatticeAreaManyCofactorWidthFloorAndReceiver
NEXT=Stage14-t152
```
