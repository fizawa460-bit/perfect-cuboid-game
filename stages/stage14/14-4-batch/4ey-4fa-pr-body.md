## Stage14-4 batch — 4ey through 4fa

Starts from latest merged main `7f8b5c1f683a68ba2bcf8a9393b26d8872a5c457`.

- `4ey`: reconstructs the odd squarefree xi-agreement product by the fixed-ray squareclass identity `UV=sf_odd(K*Z)` up to frozen finite decorations.
- `4ez`: proves `G=gcd(UV,K) >= B^(4phi-1/2-o(1)) >= B^(1/3-o(1))` on every square-root packet.
- `4fa`: freezes exact `G|K` at divisor-many cost, allocates it into `(U,V)`, and uses the existing primitive common-core root-line count conditionally on this new large divisor to reduce the agreement-pair fiber to `B^o(1)`. After fixing `(U,V)`, only the short radial square scale remains, with `#h <= B^(1/4-phi+o(1)) <= B^(1/24+o(1))`.

The heavy-ray branch is not declared closed because the concentrated exact-`C` mass exponent `eta` is not uniformly known to exceed `1/24`.

```text
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairShortRadialSquareScalePhysicalIncidence
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4fb
```
