# Stage14-toolbox-aw — superseded-consumer and current-receiver audit

## Status

`COMPLETE_SUPERSEDED_CONSUMER_AUDIT_AND_THREE_QUARTER_RECEIVER_REFRESH`

Stage14-toolbox-av scheduled an audit of the first consumers `14-4ch`,
`14-s7-22`, and `14-t59`.  This stage performs that audit on current main, but
does not freeze those historical receivers as if later work had not happened.
It follows every consumer through merged `X1`, `s7-23--s7-29`, `4cp`, `t68`,
and `tH18` and records the first legal current certificate.

## Consumer and supersession matrix

| Historical consumer | Exact conclusion | Historical open gate | Current disposition |
|---|---|---|---|
| `14-4ch` | fixed eight cells plus `(C,u,v)` have `B^o(1)` physical lift | moving eight-cell multiplicity | X1 proves the charged-once joint common-core/CRT fiber lemma; s7-29 then proves the root-line count used in the `3/4` bound |
| `14-s7-22` | rank-three packets have a near-full dual character and tangent/conic split | packet-to-normal average fiber | s7-23 eliminates rank three; later rank-one reductions and s7-29 supersede this receiver |
| `14-t59` | exact `B^o(1)` orthogonal-rectangle decomposition with balanced energy | same-modulus rectangle second moment | no analytic promotion; t68 shows private canonical primes do not force the desired cross determinant and moves the live problem to mutually-Cayley-private square-scale energy |

The first two rows are compatible structural inputs on the same physical pair.
Their legal combination is the X1 charged-once joint packet, not multiplication
of two savings.  The third row is a different fixed-`U` coefficient space and
is not promoted from the main/s argument.

## Current main/s certificate

Merged s7-29 proves an unconditional charged-once

```text
V(B) << B^(3/4+o(1)).
```

Merged 4cp legally promotes this to the mainline and fixes the live receiver

```text
QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy.
```

Its saturation edge is `theta=5/16`, `phi=1/4`.  The old `7/8` receivers
`CoupledCommonCoreGaussianResidualIncidence` and
`BalancedDualCRTShortVectorEnergy` are historical ancestors, not current
promotion targets.  No additional saving below `3/4` is proved here.

## Current fixed-U certificate

The t59 rectangle theorem remains unproved and must not be manufactured from
orthogonality alone.  Merged tH18 correctly finds no direct imported
private-root large sieve.  Merged t68 then proves a stronger structural no-go:
on the clean principal fiber a private canonical prime does not transfer a
root orientation or determinant modulus to the other state.  Consequently
the old tH18 request is superseded and

```text
TH18_NEEDED=false.
```

The current local t receiver is

```text
SharedUMutuallyCayleyPrivateSquareScaleEnergy.
```

It remains unproved.  It neither supplies nor is supplied by the main/s
quarter-phi receiver.

## Promotion and supervisor decision

- promote the global exponent ledger from historical `7/8` to merged `3/4`;
- reject any certificate still naming 4ch/s7-22/t59 as the current receiver;
- reject reuse of `TH16_NEEDED=true` or the old tH18 target after t68;
- keep main/s and fixed-U estimates separate;
- open no toolbox-H line: the current gaps are exact arithmetic receivers,
  not unverified imports already claimed as theorems.

## Boundary

```text
STAGE14_TOOLBOX_AW=COMPLETE_SUPERSEDED_CONSUMER_AUDIT_AND_THREE_QUARTER_RECEIVER_REFRESH
HISTORICAL_4CH_CONSUMER_AUDITED=true
HISTORICAL_S7_22_CONSUMER_AUDITED=true
HISTORICAL_T59_CONSUMER_AUDITED=true
JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_PROVED=true
OLD_S_COMMON_CORE_RECEIVER_CURRENT=false
OLD_S_DUAL_CRT_RECEIVER_CURRENT=false
CURRENT_MAIN_S_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy
CURRENT_MAIN_S_RECEIVER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4
IMPROVEMENT_OVER_7_8=1/8
FIXED_U_T59_RECTANGLE_SECOND_MOMENT_PROVED=false
TH16_REQUEST_CURRENT=false
TH18_PREVIOUS_REQUEST_SUPERSEDED=true
TH18_NEEDED=false
CURRENT_FIXED_U_RECEIVER=SharedUMutuallyCayleyPrivateSquareScaleEnergy
CURRENT_FIXED_U_RECEIVER_PROVED=false
MAIN_S_AND_FIXED_U_RECEIVERS_EQUIVALENT=false
TOOLBOX_H_CONTINUATION_NEEDED=false
TOOLBOX_ROUTE_BLOCKED=false
NEW_AW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-toolbox-ax audit the first 4cq/s7-30/t69 consumers against the refreshed three-quarter certificates
```
