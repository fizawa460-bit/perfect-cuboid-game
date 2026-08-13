# Stage14-t141 — dyadic endpoint principal-mass localization and the quarter-width floor

## Status

`COMPLETE_ENDPOINT_DYADIC_MASS_LOCALIZATION_AND_QUARTER_WIDTH_FLOOR`

Consumes Stage14-t140 on the same batch branch and the merged fixed-residue baseline from t135/t139.

Let `M_edge,T_edge` denote the principal and selected physical masses on the endpoint branch. Since the selected prime residue is one ordinary Gaussian residue modulo `d`, pointwise

```text
K_z(beta_*) <= |P_z|.
```

Therefore

```text
T_edge <= sum_z |P_z|
       = |(Z[i]/dZ[i])^x| * M_edge
       = B^o(1) * M_edge,
```

because merged t139 retains `d=B^o(1)`.

## 1. Capacity-light endpoint mass is already harmless

If for some fixed `delta>0`

```text
M_edge <= B^(1/2-delta),
```

then

```text
T_edge <= B^(1/2-delta+o(1)).
```

Hence an endpoint sequence that can obstruct a uniform strict sub-square-root bound must satisfy

```text
M_edge = B^(1/2-o(1))
```

along some saturating sequence. This is only a necessary condition for an obstruction; no lower bound is asserted for arbitrary fixed-U packets.

More generally, if

```text
M_edge=B^(eta+o(1))
```
with `eta>0`, the same argument below gives an additive-width floor `B^(eta/2-o(1))`.

```text
ENDPOINT_CAPACITY_LIGHT_BRANCH_FIXED_POWER_HARMLESS=true
OBSTRUCTING_ENDPOINT_SEQUENCE_REQUIRES_PRINCIPAL_MASS_B_HALF_MINUS_O1=true
```

## 2. Dyadic localization

Split the endpoint widths into

```text
0<H<=1,
2^j < H <= 2^(j+1),
```

up to the endpoint maximum. There are `O(log B)=B^o(1)` layers.

The `H<=1` layer has only `B^o(1)` principal capacity by t140 and cannot carry a saturating endpoint mass.

If a layer has `Y=2^j<=sqrt(B)`, t140 gives

```text
M_Y <= B^o(1) Y^2.
```

If `Y>sqrt(B)`, then the desired quarter-width lower bound is automatic.

Thus if

```text
M_edge=B^(eta+o(1)),
```
then some dyadic layer carries

```text
M_Y >= B^(eta-o(1)).
```

For a nontrivial layer with `Y<=sqrt(B)`, writing

```text
Y=B^(lambda+o(1))
```
forces

```text
eta <= 2*lambda,
lambda >= eta/2.
```

In particular, on every sequence capable of obstructing the local trivial `B^(1/2+o(1))` exponent,

```text
boxed:
H(z) is localized to a layer
H ~ B^(lambda+o(1)),
lambda >= 1/4-o(1).
```

Equivalently, the genuinely ultra-short range

```text
H <= B^(1/4-epsilon)
```
for any fixed `epsilon>0` has principal capacity at most

```text
B^(1/2-2*epsilon+o(1))
```
and is already harmless for the whole `1/2` exponent.

```text
ENDPOINT_DYADIC_LAYER_COUNT=Bo1
ENDPOINT_PRINCIPAL_SCALE_LOCALIZES_TO_ONE_WIDTH_LAYER=true
GENERAL_WIDTH_FLOOR_LAMBDA_GE_ETA_OVER_2=true
SUBSQRT_OBSTRUCTION_ENDPOINT_WIDTH_FLOOR=1/4-o1
ULTRASHORT_BELOW_QUARTER_WIDTH_BRANCH_DISCHARGED_BY_CAPACITY=true
```

## 3. What remains

The endpoint prime problem is no longer allowed to use arbitrarily tiny additive intervals on a sequence that threatens the exponent. The live endpoint obstruction has mesoscopic norm width at least `B^(1/4-o(1))`, while still possibly being much shorter than the cumulative Mitsui scale.

This is a capacity localization, not yet a theorem discharge. The modulus may lie either inside or outside the positive tH31 Mitsui-safe range. The next stage must cross the width localization with that modulus split before deciding whether a fresh short-interval H audit is justified.

The beyond-Mitsui long-headroom branch remains unchanged.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH32_NEEDED=false
PREFERRED_RECEIVER=SharedUQuarterScaleOrLargerEndpointFixedGaussianResiduePrimeOccupancyOrLongHeadroomBeyondMitsuiModulusBias
NEXT_INTERNAL_TARGET=EndpointWidthByModulusCrossSplitAndShortIntervalTheoremFreeze
NEXT=Stage14-t142
