# Stage27-18e — space-diagonal survival receiver

```text
TASK_ID=Stage27-18e
ROLE=SPACE_DIAGONAL_SURVIVAL_RECEIVER
STATUS=EXACT_RECEIVER_WITH_THEOREM_GATE
```

On every localized Stage18 packet `T`, define unit physical weights and the exact survivor indicator

`I_surv(omega)=1_{sf(A(omega))=sf(D(omega))}`.

Then

`S_T = sum_{omega in T} I_surv(omega)`,
`M18,T = sum_{omega in T} 1`,
`N2(B)=sum_T S_T`.

Thus the Stage18 -> Stage19 transfer is literally a same-measure restriction operator; there is no probabilistic independence step.

A sufficient upper theorem is the following packetwise-plus-exception statement.  For fixed `delta,eta>0`, decompose the packets into regular and exceptional sets such that

`sum_{T exceptional} M18,T <= B^{-eta+o(1)} M2(B)`

and for every regular packet

`S_T <= B^{-delta+o(1)} M18,T`.

Then

`N2(B) <= B^{-min(delta,eta)+o(1)} M2(B)`.

Since `M2(B)~C B(log B)^5`, this gives

`N2(B) <= B^{1-min(delta,eta)+o(1)}`.

To improve the already-certified `B^{1/2+o(1)}` Stage19 upper bound by this transfer alone, one therefore needs

`min(delta,eta) > 1/2`.

This numerical threshold is important: a small fixed-power survival deficit from Stage18 is genuine information but does **not** beat the existing half-power numerator theorem.  The re-excavation must either produce survival exponent strictly greater than `1/2`, combine legally with the inherited Stage14 numerator structure, or strengthen the lower side.

The repository currently certifies only `S/M18 -> 0` from the same-measure split-prime parity sieve, not a `B^{-1/2-epsilon}` survival ratio.  Therefore no new Stage19 exponent is claimed here.

The exact next upper receiver is

`Stage18LocalizedSpaceDiagonalSurvivalExponentGreaterThanHalf`

or a hybrid theorem that couples the Stage18 localization to the inherited Stage14 half-power structure without double charging the same squareclass/core conditions.

For the lower side, the exact receiver remains an actual positive-dimensional Stage18 subfamily satisfying `sf(A)=sf(D)` with physical height exponent and finite-to-subpower multiplicity strong enough to improve the current Stage19 lower exponent.

```text
SURVIVAL_OPERATOR_EXACT=true
CURRENT_CERTIFIED_SURVIVAL=ZERO_DENSITY_ONLY_PLUS_INHERITED_NUMERATOR_BOUND
PURE_STAGE18_TRANSFER_THRESHOLD_FOR_NEW_UPPER=delta_effective>1/2
NEW_STAGE19_UPPER_EXPONENT_PROVED=false
NEW_STAGE19_LOWER_EXPONENT_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NATURAL_STOP=NEW_LOCALIZATION_OR_SURVIVAL_INPUT_REQUIRED
NEXT_RECOMMENDED=Stage27-18-audit
```
