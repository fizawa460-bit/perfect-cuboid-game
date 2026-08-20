# Stage27-20-r303c — T weighted adapter theorem gate

STATUS=SUBMITTED_PENDING_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_T_WEIGHTED_ADAPTER_RECEIVER
PARENT_ROUTE=Stage27-20-r303b

The weighted-average T route is now separated from the frozen r302 MAIN wall route.

A sufficient package is:

(A) an averaged Gaussian-prime theorem whose exceptional target-class set satisfies
    |E| <= B^{-eta+o(1)} |C|
for fixed eta>0 over the exact family used by the frozen T packet;

(B) a physical pushforward collision bound
    sum_c w(c)^2 <= B^{rho+o(1)} M^2/|C|
with rho<eta.

Then
    sum_{c in E} w(c) <= B^{-(eta-rho)/2+o(1)} M,
so the averaged theorem becomes legally chargeable in the actual Stage27 physical measure. The remaining half-power ledger must then be checked against the gained exponent (eta-rho)/2.

This theorem shape is strictly weaker than individual-modulus prime occupancy and strictly stronger than unweighted BV/BDH. It is a genuine alternative upper route.

The first repo-internal missing lemma is therefore

TPhysicalTargetClassPushforwardCollisionDeficit

and the first external companion is

TExactGaussianPrimeExceptionalClassPowerSaving

with both quantified on the same target family.

R302_REMAINS_FROZEN=true
T_ROUTE_OPEN=true
WEIGHTED_AVERAGE_CROSSING_REDUCED=true
FIRST_MISSING_INTERNAL_LEMMA=TPhysicalTargetClassPushforwardCollisionDeficit
FIRST_MISSING_EXTERNAL_INPUT=TExactGaussianPrimeExceptionalClassPowerSaving
STRICT_SUB_SQRT_UPPER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r303d
