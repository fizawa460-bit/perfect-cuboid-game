# Stage14-s7-54 — pairwise covariance projection equivalence

## Status

`COMPLETE_PAIRWISE_PROJECTION_EQUIVALENCE_REDUCTION`

Consumes merged `Stage14-s7-53`, merged `Stage14-s7-48`, and merged `Stage14-X15`.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Retain

```text
X_+ = epsilon_+ C_* S T = D^2+A^2,
X_- = epsilon_- u_* R J = D^2-A^2,
X_0 = 2DA = 2 alpha delta r s,
X_+^2 = X_-^2 + X_0^2.
```

The three pairwise covariance branches are

```text
(+,-): (X_+,X_-),
(+,k): (X_+,X_0),
(-,k): (X_-,X_0).
```

Merged s7-48 identifies `(+,-)` as the Gaussian norm / rotated coordinate-product receiver. Merged X15 gives the primitive Pythagorean cone parameterization. Fixing any admissible pair recovers the third projection with only `B^o(1)` ambiguity after inherited primitive/sign decorations.

```text
PAIRWISE_PLUS_MINUS_TO_PACKET_FIBER=Bo1
PAIRWISE_PLUS_K_TO_PACKET_FIBER=Bo1
PAIRWISE_MINUS_K_TO_PACKET_FIBER=Bo1
PAIRWISE_BRANCHES_POWER_EQUIVALENT=true
PAIRWISE_BRANCH_COUNT_AT_FIXED_POWER=1
PAIRWISE_COVARIANCE_DOUBLE_OR_TRIPLE_CHARGE_ALLOWED=false
SECOND_INDEPENDENT_MODULUS_DENSITY_FROM_PAIRWISE_REPARAMETRIZATION=false
```

Thus the three covariance terms are coordinate views of one common two-projection compatibility mass and cannot be charged as independent fixed-power receivers.

The s7-53 dichotomy becomes

```text
PAIRWISE_BRANCH:
  one common two-projection physical covariance receiver;
CONNECTED_TRIPLE_BRANCH:
  pairwise covariances power-small but connected kappa_3 survives.
```

Next determine whether the centered common pairwise receiver is exactly the s7-49/s7-50 inverse-fraction full-conductor error in another coordinate system or contains an additional pairwise principal-density component.

```text
STAGE14_S7_54=COMPLETE_PAIRWISE_PROJECTION_EQUIVALENCE_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_54_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_PAIRWISE_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanTwoProjectionPhysicalCovariance
REMAINING_CONNECTED_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanConnectedThreeProjectionCumulant
NEXT=Stage14-s7-55
```
