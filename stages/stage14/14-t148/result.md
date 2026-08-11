# Stage14-t148 — disjoint sparse/many cofactor localization and one-cofactor endpoint freeze

## Status

`COMPLETE_SPARSE_MANY_COFACTOR_DISJOINT_LOCALIZATION_AND_SINGLE_INTERVAL_FREEZE`

Consumes Stage14-t147 on this batch branch together with merged Stage14-t146/t135.

For one endpoint dyadic layer `Z(Y)`, merged t145 gives

```text
#Z(Y) <= B^o(1)*(Y/(h*k0)+1).                     (1.1)
```

Stage14-t147 restores the exact ordinary-residue normalization

```text
M_Y
 <= B^o(1)/d^2
    * (Y/(h*k0)+1)(Y+1).                          (1.2)
```

## 1. Make the sparse/many alternatives disjoint

Put

```text
C_Y := Y/(h*k0).
```

After passing to an exponent-stable subsequence, exactly one of the following occurs.

### SPARSE

```text
C_Y=B^o(1).
```

Then (1.1) gives

```text
boxed:
#Z(Y)=B^o(1).                                      (1.3)
```

### MANY

There is a fixed `sigma>0` such that along the subsequence

```text
C_Y >= B^(sigma+o(1)).
```

Then the `+1` in (1.1)--(1.2) is exponent-negligible and the layer is genuinely the host-normalized many-cofactor branch.

Thus the `lambda>=1/2-o(1)` alternative from t146 is not treated as an independent entropy source when `C_Y` has positive B-power growth: that case belongs to MANY.  The genuinely sparse remainder has only subpolynomially many actual Gaussian cofactors.

```text
SPARSE_MANY_COFACTOR_SPLIT_DISJOINT=true
SPARSE_ENDPOINT_ACTUAL_COFACTOR_COUNT=Bo1
POSITIVE_POWER_COFACTOR_MULTIPLICITY_ASSIGNED_TO_MANY_BRANCH=true
```

## 2. Nonnegative localization freezes one actual Gaussian cofactor on SPARSE

For each `z in Z(Y)` define

```text
T_z
 := #{canonical split Gaussian primes pi:
      pi == beta_* (mod d),
      2*sqrt(B)<N(pi)<=X_U/N(z)},

M_z
 := |P_z|/|R_d|.
```

Then exactly

```text
T_Y=sum_z T_z,
M_Y=sum_z M_z.
```

Assume the bad fixed-power depletion on a principal-scale sparse layer:

```text
T_Y <= B^(-delta) M_Y,
M_Y >= B^(1/2-o(1)),
delta>0 fixed.                                    (2.1)
```

Let

```text
S_bad={z:T_z<=2*B^(-delta)M_z}.
```

If the complementary set carried more than `M_Y/2` of the baseline, then

```text
T_Y > 2*B^(-delta)*(M_Y/2)=B^(-delta)M_Y,
```

contradicting (2.1).  Hence

```text
sum_{z in S_bad} M_z >= M_Y/2.
```

By (1.3), one actual cofactor `z_* in S_bad` satisfies

```text
boxed:
M_{z_*} >= B^(1/2-o(1)),                           (2.2)
T_{z_*} <= 2*B^(-delta) M_{z_*}.                   (2.3)
```

The constant two is irrelevant at fixed-power scale.  Therefore every principal sparse bad sequence localizes to one actual primitive Gaussian cofactor, one exact endpoint, and one fixed ordinary prime residue.

```text
SPARSE_FIXED_POWER_DEPLETION_LOCALIZES_TO_ONE_ACTUAL_COFACTOR=true
SINGLE_COFACTOR_PRINCIPAL_BASELINE_SCALE=B^(1/2-o(1))
SINGLE_COFACTOR_FIXED_POWER_DEPLETION_RETAINED=true
```

## 3. The sparse receiver is now a single fixed-residue prime interval

For the localized cofactor put

```text
n_*=N(z_*),
H_*:=X_U/n_* - 2*sqrt(B).
```

The sparse branch is exactly

```text
T_{z_*}
 = #{pi canonical split:
     pi==beta_* (mod d),
     2*sqrt(B)<N(pi)<=2*sqrt(B)+H_*},

M_{z_*}
 = 1/|R_d|
   * #{pi canonical split:
       2*sqrt(B)<N(pi)<=2*sqrt(B)+H_*}.
```

No cofactor averaging remains on this branch.  Safe-modulus and beyond-Mitsui versions differ only by the already-existing modulus range.

Stage14-tH32 already audited the safe growing-residue short-interval problem uniformly in the endpoint, so freezing `z_*` does not by itself create a fresh theorem family.  Stage14-tH30 already records the broader individual-`d=B^o(1)` obstruction beyond the safe range.

```text
SPARSE_ENDPOINT_COFACTOR_AVERAGING_REMAINS=false
SPARSE_ENDPOINT_RECEIVER_IS_SINGLE_FIXED_RESIDUE_PRIME_INTERVAL=true
```

## 4. MANY remains an aggregate host/residue-normalized endpoint problem

On MANY, (1.2) reduces to

```text
M_Y
 <= B^o(1) * Y^2/(h*k0*d^2).                      (4.1)
```

The fixed-power consequence of this sharpened capacity is deferred to t149.

```text
MANY_COFACTOR_RESIDUE_HOST_NORMALIZED_CAPACITY=M_Y_LE_BO1_TIMES_Y2_OVER_hk0_d2
```

## 5. Receiver and H decision

This stage makes the t146 sparse/many alternatives disjoint and freezes the sparse side to one actual cofactor, but it does not yet impose the sharpened many-cofactor width floor.  The material receiver change is therefore deferred to t149 so that the complete normalized split is published once.

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
NEXT_INTERNAL_TARGET=ResidueHostNormalizedManyCofactorWidthFloorAndUnifiedReceiver
NEXT=Stage14-t149
```
