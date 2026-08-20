# Stage27-18g — upper survival transfer

```text
TASK_ID=Stage27-18g
ROLE=UPPER_TRANSFER
STATUS=THEOREM_GATE
```

The pure Stage18-transfer route would improve the current Stage19 half-power upper only if the effective same-measure survival exponent satisfies `delta_eff>1/2`, because `M2(B)=B^{1+o(1)}` up to logarithms.

The repository currently provides two valid upper facts:

- inherited Stage14 whole-family numerator bound `N2(B)<<B^{1/2+o(1)}`;
- same-measure Stage19 split-prime parity sieve proving `N2(B)/M2(B)->0`.

Neither implies a quantitative `B^{-1/2-epsilon}` survival ratio on Stage18 packets.  Combining them naively would double-charge the same survivor predicate rather than yield a stronger exponent.

A genuinely new upper transfer therefore needs one of:

1. a packetwise Stage18 mass theorem plus same-measure survival `S_T<=B^{-1/2-epsilon+o(1)}M18,T` outside negligible packet mass;
2. a hybrid identity showing that the Stage14 half-power numerator structure and Stage18 localization charge independent arithmetic information;
3. a new determinant/incidence/character adapter on the localized Stage18 source measure that produces an additional fixed-power saving without reusing squareclass/core entropy already paid upstream.

No such theorem is currently present in the repository or the already-rematched StructureRadar arsenal.  This is therefore a genuine theorem gate, not a reason to manufacture further renamed subroutes.

```text
CURRENT_STAGE19_UPPER_MU=1/2
PURE_TRANSFER_REQUIRED_SURVIVAL_EXPONENT=>1/2
NEW_STAGE19_UPPER_EXPONENT_PROVED=false
HYBRID_INDEPENDENT_CHARGE_PROVED=false
UPPER_TRANSFER_GATE=Stage18LocalizedSurvivalExponentGreaterThanHalf_OR_LegalIndependentHybrid
NEXT_DERIVED_ROUTE=Stage27-18h
```
