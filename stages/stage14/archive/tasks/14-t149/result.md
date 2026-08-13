# Stage14-t149 — residue/host-normalized endpoint width floors and single-interval receiver

## Status

`COMPLETE_RESIDUE_HOST_NORMALIZED_WIDTH_FLOORS_AND_RECEIVER_CHANGE`

Consumes Stage14-t147/t148 on this batch branch, merged Stage14-t146/tH32, and merged Stage14-Work-byX37.

The endpoint obstruction is now disjointly divided into:

```text
SPARSE:
  #Z(Y)=B^o(1),
  bad principal mass localizes to one actual cofactor z_*;

MANY:
  Y/(h*k0) has positive B-power growth,
  M_Y <= B^o(1)*Y^2/(h*k0*d^2).
```

## 1. MANY forces the residue/host-normalized width floor

A whole-exponent-obstructing endpoint layer must have

```text
M_Y >= B^(1/2-o(1)).                               (1.1)
```

On MANY, t148 gives

```text
M_Y <= B^o(1)*Y^2/(h*k0*d^2).                     (1.2)
```

Combining (1.1)--(1.2),

```text
Y^2
 >= B^(1/2-o(1)) * h*k0*d^2,
```

hence

```text
boxed:
Y >= B^(1/4-o(1))*d*sqrt(h*k0).                   (1.3)
```

This strictly refines t146's host-only floor

```text
B^(1/4-o(1))*sqrt(h*k0).
```

The new factor `d` comes from the ordinary Gaussian residue density already present in the exact t135 baseline.

```text
RESIDUE_HOST_NORMALIZED_MANY_WIDTH_FLOOR_PROVED=true
RESIDUE_HOST_NORMALIZED_MANY_WIDTH_FLOOR=BsQuarterTimes_d_TimesSqrtHK0
```

## 2. Beyond-Mitsui MANY gains d^(3/2)

Merged t144 proves on every beyond-Mitsui endpoint packet

```text
h*k0 >= C*d
```

for a fixed positive packet constant `C`.  Therefore (1.3) implies

```text
boxed:
Y >= B^(1/4-o(1))*d^(3/2).                         (2.1)
```

Since

```text
d>exp(c_safe*sqrt(log B)),
```
this is a pseudopolynomial strengthening of the quarter boundary by at least

```text
exp((3*c_safe/2)*sqrt(log B)).
```

It remains `B^o(1)` and hence is not a fixed positive exponent gain.

```text
BEYOND_MITSUI_MANY_WIDTH_FLOOR=BsQuarterTimes_d^(3/2)
BEYOND_MITSUI_D_THREE_HALVES_WIDTH_GAIN_PROVED=true
BEYOND_MITSUI_D_THREE_HALVES_FIXED_POWER_GAIN=false
```

## 3. SPARSE principal mass is residue-normalized near-full on one interval

Stage14-t148 freezes one cofactor `z_*` with

```text
M_{z_*} >= B^(1/2-o(1)).
```

But exactly

```text
M_{z_*}
 = |P_{z_*}|/|R_d|
 <= B^o(1)*H_*/d^2,                               (3.1)
```

because the unrestricted prime count is at most the additive interval length and `|R_d|=d^2*B^o(1)`.

Therefore every sparse principal bad sequence satisfies the quantitative necessary condition

```text
boxed:
H_*/d^2 >= B^(1/2-o(1)),                          (3.2)
```

or equivalently

```text
H_* >= B^(1/2-o(1))*d^2.                          (3.3)
```

This statement is intentionally at `B^o(1)` precision.  Since `d=B^o(1)`, it does not contradict the physical `H_*=O(sqrt(B))`; instead it says the sparse survivor is not merely exponent-near-full but residue-normalized near-full.

```text
SPARSE_SINGLE_INTERVAL_RESIDUE_NORMALIZED_NEAR_FULL_PROVED=true
SPARSE_SINGLE_INTERVAL_NECESSARY_CONDITION=H_over_d2_GE_BsHalfMinusO1
```

## 4. Reconsume the positive tH32 safe-modulus boundary without recharge

On safe moduli, completed tH32 already proves fixed-residue occupancy for

```text
H >= H_Kai(B)
 := B^(1/2)*exp(-c_short*sqrt(log B)).
```

Therefore:

- a safe SPARSE single interval survives only below `H_Kai(B)` while satisfying (3.2);
- a safe MANY layer survives only below `H_Kai(B)` while satisfying (1.3).

Any safe subrange where the lower capacity floor itself reaches `H_Kai(B)` is discharged by the already-consumed tH32 theorem; no new theorem is charged.

The exact surviving safe compatibility conditions are recorded as

```text
SPARSE:
  B^(1/2-o(1))*d^2 <= H_* < H_Kai(B),

MANY:
  B^(1/4-o(1))*d*sqrt(h*k0) <= Y < H_Kai(B),
```

with the `o(1)` factors understood as the charged representation/divisor losses already present upstream.

```text
TH32_SAFE_COVERAGE_RECONSUMED_WITHOUT_RECHARGE=true
SAFE_SPARSE_SUBKAI_RESIDUE_NORMALIZED_INTERVAL_REMAINS=true
SAFE_MANY_SUBKAI_RESIDUE_HOST_NORMALIZED_INTERVAL_REMAINS=true
```

## 5. Beyond-Mitsui long-headroom branch remains separate

The endpoint annulus capacity argument still does not bound the long-headroom branch.  Its modulus remains fixed-U hosted and its baseline still contains `1/|R_d|`, but no legal principal-capacity estimate below `B^(1/2)` is established here for the full long reciprocal hyperbola.

```text
LONG_HEADROOM_BEYOND_MITSUI_BRANCH_UNCHANGED=true
```

## 6. New minimal receiver

The t146 endpoint labels are superseded by the disjoint normalized receivers

```text
(A) SafeMitsuiSingleCofactorSubKaiResidueNormalizedNearFullPrimeOccupancy
    with H_*/d^2 >= B^(1/2-o(1)) and H_*<H_Kai(B)

OR

(B) SafeMitsuiManyCofactorResidueHostNormalizedIntermediatePrimeOccupancy
    with Y >= B^(1/4-o(1))*d*sqrt(h*k0) and Y<H_Kai(B)

OR

(C) BeyondMitsuiSingleCofactorResidueNormalizedNearFullPrimeOccupancyBias
    with H_*/d^2 >= B^(1/2-o(1))

OR

(D) BeyondMitsuiManyCofactorResidueHostNormalizedEndpointPrimeOccupancyBias
    with Y >= B^(1/4-o(1))*d^(3/2)

OR

(E) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

This is a material receiver change and reaches the `t149` normal revisit condition named by merged Work-byX37.

No `tH33` is opened.  The safe prime theorem hypothesis is still exactly the tH32 target, merely on a smaller internally certified width range; the beyond-Mitsui individual-modulus issue was already identified in tH30 and has not yet become a materially new theorem-compatible family.  The next internal step should compare the two safe normalized floors with the known tH32/Stucky boundaries and separately quantify the beyond-Mitsui individual-character obstruction after the new `d^2` normalization.

```text
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
PREFERRED_RECEIVER=SharedUResidueNormalizedSingleIntervalOrResidueHostNormalizedManyEndpointPlusBeyondMitsuiLongBias
NEXT_INTERNAL_TARGET=SafeNormalizedWidthCoverageVersusBeyondMitsuiIndividualCharacterGapAudit
NEXT=Stage14-t150
```
