# Stage23-40 Q06 source-level execution

This note executes Q06 from its actual Stage14 source receivers instead of treating `(4,4) Kummer` as a label.

## Source attack IDs opened

The concrete source chain is:

1. `Stage14-4ah` / PR #164: physical Kummer polarization and exact physical height.
2. `Stage14-tH15` / PR #457: explicit projective `(4,4)` fixed-squareclass receiver and transverse Frobenius incidence.
3. `Stage14-t64` / PR #497: quotient of the generic `(4,4)` label to the sharper rational cross-ratio / Jacobi square-lift model.

These are the Q06 source-level receiver artifacts used below.

## Exact physical-height import

Stage14-4ah works on the two-face Kummer surface with resolved double cover `pi:X->Y`, `Y=Bl_4(P1xP1)`, `L=-K_Y`, and

`M=pi^*L`, `M^2=8`.

For a primitive physical point with projective coordinates `Phi(P)=[e:x:y]`, it proves exactly

`H_M(P)=sqrt(e^2+x^2+y^2)=d`.

Stage23's target population Stage19 is exactly the primitive/canonical two-face population with integral space diagonal and cutoff `d<=B`. Therefore the Q06 height adapter is lossless:

```text
STAGE23_PHYSICAL_HEIGHT=d
Q06_KUMMER_HEIGHT=H_M
HEIGHT_IDENTITY=H_M=d
HEIGHT_ADAPTER_LOSS=0
```

No `B^alpha` distortion is inserted.

## Actual receiver map

The Stage14-tH15 source fixes a primitive Gaussian cofactor `U=a+ib` and uses projective slopes

`x=Re(pi)/Im(pi)`, `y=Re(V)/Im(V)`.

For each branch it gives an explicit polynomial `P_U(x,y)` of bidegree at most `(4,4)` such that a fixed squareclass fiber is

`Z^2 = kappa P_U(x,y)`.

The same source partitions squareclass energy as

`E_U = R_U + I_same_pi + I_same_V + I_transverse`

with the same-pi and same-V slices routed to one-dimensional Stage14 bounds, leaving the transverse incidence. It introduces external split primes and characters

`c_s(p)=chi_p(Ftilde_s)`

and proves the positive receiver

`I_transverse (P-2b)^2 <= Frob_tr`,

where `Frob_tr` has the exact Cauchy-free inclusion-exclusion expansion from the full, same-pi, same-V and diagonal pieces.

For Stage23 the literal target point `(a,b,c,d)` first chooses one of its two integral faces as oriented source face and is then mapped to the corresponding Stage14 two-face physical state. Canonical ordering makes the number of face/orientation choices bounded absolutely. Hence the Stage23-to-Q06 map has bounded combinatorial multiplicity before any arithmetic fiber multiplicity is counted.

```text
STAGE23_TO_Q06_RECEIVER=literal two-face object -> bounded oriented-face state -> (U,pi,V,branch) projective receiver
ORIENTATION_MULTIPLICITY=O(1)
PHYSICAL_OBJECT_MULTIPLICITY_FIXED=true
```

The remaining multiplicity is precisely the arithmetic multiplicity inside a fixed receiver fiber, not an uncontrolled population conversion.

## Sharper source-level quotient

Stage14-t64 shows the generic `(4,4)` label is not the minimal geometry. With

`T=t^2`, `X=x^2`,

it defines the exact rational cross-ratio

`R=(X-T)/(1-TX)`

and proves `[F]=[R]`. A fixed squareclass `R=s` gives the Mobius transport

`X=(T+s)/(1+sT)`.

Demanding the physical square lift gives the Jacobi quartic

`y^2=(t^2+s)(1+s t^2)`.

Thus the source-level Q06 receiver available to Stage23 is actually sharper than a generic K3 count: it is a coupled family of Jacobi genus-one square lifts with exact physical height inherited from Stage14-4ah.

## Height/multiplicity push

What the source chain certifies for Stage23 is:

1. physical height is exactly `d`, so no height-comparison loss;
2. canonical physical-object to oriented receiver multiplicity is bounded;
3. same-row / same-column principal multiplicities are already separated by the tH15 partition;
4. the unresolved part is transverse squareclass incidence / coupled Jacobi square-lift incidence.

What it does **not** certify is a point-count estimate for that transverse receiver strong enough to improve

`N2(B) <<_epsilon B^(1/2+epsilon)`.

The `M.C>=4` result of Stage14-4ah implies that any single fixed physical rational curve has bounded-height exponent at most `1/2`; it does not bound the number of moving curves/fibers. Hence it reproduces the half-power barrier but does not beat it.

The tH15/t64 receiver likewise gives an exact incidence target but leaves the required global transverse dispersion unproved.

Therefore Q06 reaches the following source-level boundary:

```text
Q06_SOURCE_ATTACK_IDS_OPENED=true
Q06_ACTUAL_RECEIVER_MAP_MATERIALIZED=true
Q06_PHYSICAL_HEIGHT_IDENTITY_PROVED=true
Q06_HEIGHT_LOSS=0
Q06_STAGE23_ORIENTATION_MULTIPLICITY=O(1)
Q06_ROW_COLUMN_MULTIPLICITY_PARTITIONED=true
Q06_TRANSVERSE_RECEIVER=SharedUTransverseJacobiSquareLiftIncidence
Q06_SINGLE_FIXED_RATIONAL_CURVE_EXPONENT_LE_1_2=true
Q06_MOVING_FAMILY_COUNT_CONTROL_PROVED=false
Q06_TRANSVERSE_DISPERSION_PROVED=false
Q06_STRONGER_THAN_HALF_POWER_BOUND_PROVED=false
```

This is now a source-level execution failure, not a failure to open the source. Further progress from Q06 requires a new theorem controlling the moving transverse Jacobi/Kummer family under the exact `d=H_M` height, or an equivalent uniform incidence/dispersion theorem.
