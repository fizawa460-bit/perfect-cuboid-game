# Stage14-4fg — normalized radial acceptance to squareclass divisor-window occupancy

## Status

`COMPLETE_NORMALIZED_RADIAL_ACCEPTANCE_TO_SQUARECLASS_DIVISOR_WINDOW_OCCUPANCY`

Consumes Stage14-4ff on the same batch branch and merged `Stage14-s7-85/86`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed squareclass normal form

After the merged agreement compression and the fixed noncommon kernel split, s7-85/86 gives fixed coprime squarefree data

```text
A*B=K_Z
```

and every root-factor candidate above normalized radial integer `n` has

```text
|Xr|=J*A*a^2,
|Yr|=J*B*b^2,
J*a*b=c0*n,                                      (1)
```

where

```text
J squarefree,
gcd(J,K_Z)=1.
```

All signs, two-primary conventions, common-core/root labels and the agreement pair are already frozen at charged-once `B^o(1)` cost.

## 2. Collapse the two moving root factors to one divisor-like coordinate

Define

```text
L:=J*a^2.                                         (2)
```

Then the first root factor is exactly

```text
|Xr|=A*L.                                         (3)
```

From `b=c0*n/(J*a)` and (2),

```text
|Yr|
 = J*B*b^2
 = B*c0^2*n^2/(J*a^2)
 = B*c0^2*n^2/L.                                  (4)
```

Thus the two root factors are not independent divisor variables. Once `(n,L)` is fixed, both are forced and satisfy the fixed product identity automatically.

The admissibility of `L` is exact:

```text
J=sqf(L),
L=J*a^2,
gcd(J,K_Z)=1,
J*a | c0*n.                                       (5)
```

Equivalently, since `sqrt(J*L)=J*a`,

```text
sqrt(sqf(L)*L) | c0*n,
gcd(sqf(L),K_Z)=1.                                (6)
```

For fixed `n` the number of such `L` is divisor-many, consistent with the merged s7-86 fiber bound.

```text
ROOT_PAIR_SINGLE_L_COORDINATE_PROVED=true
ROOT_X_FACTOR=A_times_L
ROOT_Y_FACTOR=B_c0_squared_n_squared_over_L
FIXED_N_L_CANDIDATE_COUNT=Bo1
```

## 3. Physical size masks become reciprocal divisor windows

Let the frozen physical root-factor size/chamber conditions be written as the already-existing allowed windows

```text
|Xr| in I_X,
|Yr| in I_Y,
```

with any finite chart/end-point splitting absorbed into `B^o(1)` labels. Substituting (3)--(4) gives exactly

```text
L in I_X/A,                                       (7)
L in B*c0^2*n^2 / I_Y.                            (8)
```

Hence, after the frozen finite masks, normalized radial acceptance is an existence problem for an admissible squareclass divisor `L` in the intersection of two reciprocal windows depending on `n`.

Define

```text
D_rad(n)
 := {L:
      sqrt(sqf(L)*L) | c0*n,
      gcd(sqf(L),K_Z)=1,
      L satisfies (7) and (8),
      all remaining transported primitive/canonical masks hold}.
```

Then

```text
A_rad(n)=1  <=>  D_rad(n) is nonempty.             (9)
```

This keeps every physical mask and the original existential quantifier order. No independence between divisor existence and the other masks is assumed.

## 4. What has been exhausted

Stage14-4fe proved that the bare factorization equation accepts every normalized `n`. Therefore the square-root obstruction cannot be reduced further by charging

```text
J*a*b=c0*n
```

or the fixed squareclass identity as an independent sparse condition.

The only heavy-ray thinning still available inside this coordinate system is the occupancy of the **physical reciprocal divisor windows** in (7)--(9), together with the transported primitive/canonical masks on the same candidate `L`.

A surviving heavy ray requires

```text
# {n<=B^(rho-delta+o(1)) : D_rad(n) nonempty}
 >= B^(mu-o(1)),
0<mu<=rho-delta,
rho=1/4-phi<=1/24.                                (10)
```

```text
BARE_FACTORIZATION_RECHARGE_FORBIDDEN=true
RADIAL_THINNING_REDUCED_TO_PHYSICAL_DIVISOR_WINDOW_OCCUPANCY=true
HEAVY_REQUIRED_ACCEPTED_N_SUPPORT_EXPONENT=mu
```

## 5. Material receiver change and H decision

The heavy branch has changed from an opaque polynomial radial-support condition to an explicit one-dimensional squareclass divisor-window selector:

```text
FixedPrimitiveRayFixedAgreementPairNormalizedRadialSquareclassDivisorWindowPhysicalOccupancy
WithMassExponentMuAtMostOneQuarterMinusPhi.
```

This is a material receiver change, so the main batch stops here under the shared contract.

No new H is opened at this boundary. Before a theorem audit, the next internal stage must freeze the exact dyadic geometry of the two reciprocal `L` windows and determine whether their intersection is a genuinely short divisor interval, a balanced divisor window, or can be dense on a saturating packet. Existing non-heavy mainline H gates remain unchanged and are not cross-promoted.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairNormalizedRadialSquareclassDivisorWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi
RECEIVER_MATERIALLY_CHANGED=true
NEW_MAIN_H_NEEDED=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fh
```
