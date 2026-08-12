# Stage14-t152 — Gaussian-lattice area width floor and d^(5/2) beyond-Mitsui gain

## Status

`COMPLETE_GAUSSIAN_LATTICE_AREA_WIDTH_FLOOR_AND_RECEIVER_CHANGE`

Consumes Stage14-t150/t151 on this batch branch, merged `Stage14-t149`, merged `Stage14-t144`, completed `Stage14-tH32`, and merged `Stage14-Work-bzX38`.

Stage14-t151 proves that, outside the sparse/singleton near-full alternative, a principal endpoint layer can survive only through the two-dimensional cofactor-annulus area term

```text
Y^2/(q_d*h*k0*d^2) >= B^(1/2-o(1)),              (1.1)
q_d=|(Z[i]/dZ[i])^x|.
```

## 1. Strengthened many-cofactor width floor

Rearranging (1.1),

```text
boxed:
Y
 >= B^(1/4-o(1))
    * d * sqrt(q_d*h*k0).                          (1.2)
```

Merged t147 gives

```text
q_d=d^2*B^o(1).
```

Therefore at the Stage14 subpolynomial precision,

```text
boxed:
Y
 >= B^(1/4-o(1))
    * d^2 * sqrt(h*k0).                            (1.3)
```

This strictly supersedes the merged t149 many-cofactor floor

```text
B^(1/4-o(1))*d*sqrt(h*k0).
```

The new additional factor `d` is not a second use of the prime residue density.  It comes from counting the already-fixed cofactor residue `rho_* mod d` as one affine Gaussian lattice of covolume `d^2`.

```text
GAUSSIAN_LATTICE_AREA_MANY_WIDTH_FLOOR_PROVED=true
GAUSSIAN_LATTICE_AREA_MANY_WIDTH_FLOOR=BsQuarterTimes_d_TimesSqrt_qd_hk0
GAUSSIAN_LATTICE_AREA_MANY_WIDTH_FLOOR_SCALE=BsQuarterTimes_d2_TimesSqrtHK0
T149_MANY_WIDTH_FLOOR_STRICTLY_SUPERSEDED=true
```

## 2. Beyond-Mitsui endpoint gains d^(5/2)

Merged t144 proves on every beyond-Mitsui endpoint packet

```text
h*k0 >= C*d,
d>exp(c_safe*sqrt(log B)),                         (2.1)
```

with fixed positive packet constant `C`.

Insert (2.1) into (1.3):

```text
boxed:
Y
 >= B^(1/4-o(1))*d^(5/2).                         (2.2)
```

Thus the old beyond-Mitsui `d^(3/2)` gain from t149 is strengthened by another full factor `d`.

Since `d=B^o(1)`, even `d^(5/2)` is still subpolynomial in `B`; it is a real quantitative gain but not a fixed positive B-power saving.

```text
BEYOND_MITSUI_GAUSSIAN_LATTICE_MANY_WIDTH_FLOOR=BsQuarterTimes_d^(5/2)
BEYOND_MITSUI_D_FIVE_HALVES_WIDTH_GAIN_PROVED=true
BEYOND_MITSUI_D_FIVE_HALVES_FIXED_POWER_GAIN=false
```

## 3. Sparse/single-cofactor branch receives exact group-order normalization

The sparse alternative remains the one-cofactor fixed-residue prime interval from t148, now written with the exact ordinary Gaussian residue-group order:

```text
M_{z_*}
 = |P_{z_*}|/q_d,
```

so principal sparse mass requires

```text
boxed:
H_*/q_d >= B^(1/2-o(1)).                           (3.1)
```

On safe moduli completed tH32 still discharges

```text
H_* >= H_Kai(B)
 := B^(1/2)*exp(-c_short*sqrt(log B)).             (3.2)
```

Hence the surviving safe sparse interval remains

```text
H_*/q_d >= B^(1/2-o(1)),
H_* < H_Kai(B).                                    (3.3)
```

No new theorem input is used.

```text
SAFE_SPARSE_EXACT_QD_NEARFULL_RECEIVER_RETAINED=true
TH32_SAFE_NEARFULL_COVERAGE_RECONSUMED_WITHOUT_RECHARGE=true
```

## 4. Safe many endpoint after the new lattice-area floor

The safe-modulus many branch is now restricted by

```text
B^(1/4-o(1))*d*sqrt(q_d*h*k0)
 <= Y
 < H_Kai(B).                                       (4.1)
```

Equivalently at subpolynomial precision,

```text
B^(1/4-o(1))*d^2*sqrt(h*k0)
 <= Y
 < H_Kai(B).                                       (4.2)
```

Whenever the lower floor reaches the tH32 threshold, that subrange is already discharged.  Uniformly closing the remaining sub-Kai interval would still require information beyond the frozen tH32 theorem boundary; the current stage does not manufacture such a theorem from the stronger capacity alone.

```text
SAFE_MANY_GAUSSIAN_LATTICE_AREA_FLOOR_PROVED=true
SAFE_MANY_SUBKAI_INTERVAL_REMAINS_POSSIBLE=true
```

## 5. Long-headroom branch remains separate

The annulus argument is an endpoint-top geometry argument.  It does not yet estimate the full long-headroom reciprocal hyperbola.  The long-headroom beyond-Mitsui branch remains

```text
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The natural next internal target is to use the same fixed cofactor residue lattice in a weighted harmonic/dyadic count over the long-headroom range, without pretending that the endpoint annulus estimate already applies there.

```text
LONG_HEADROOM_BEYOND_MITSUI_BRANCH_UNCHANGED=true
```

## 6. New minimal fixed-U receiver

The merged t149 receiver is materially sharpened to

```text
(A) SafeMitsuiSingleCofactorSubKaiExactResidueGroupNearFullPrimeOccupancy
    with H_*/q_d >= B^(1/2-o(1)) and H_*<H_Kai(B)

OR

(B) SafeMitsuiGaussianLatticeAreaManyCofactorSubKaiPrimeOccupancy
    with
    Y >= B^(1/4-o(1))*d*sqrt(q_d*h*k0)
      = B^(1/4-o(1))*d^2*sqrt(h*k0)
    and Y<H_Kai(B)

OR

(C) BeyondMitsuiSingleCofactorExactResidueGroupNearFullPrimeOccupancyBias
    with H_*/q_d >= B^(1/2-o(1))

OR

(D) BeyondMitsuiGaussianLatticeAreaManyCofactorEndpointPrimeOccupancyBias
    with Y >= B^(1/4-o(1))*d^(5/2)

OR

(E) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

This is a material receiver change, so the shared Stage14 t-batch contract stops here after three substantive units.

No `tH33` is opened.  The safe external prime theorem remains exactly completed tH32 on the same modulus/sector/residue object; only the internally certified width floor has strengthened.  The beyond-Mitsui individual-modulus obstruction remains outside the pseudopolynomial theorem range and has not yet been converted to a new theorem-compatible family.

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
PREFERRED_RECEIVER=SharedUExactResidueGroupSparseNearFullOrGaussianLatticeAreaManyEndpointPlusBeyondMitsuiLongBias
NEXT_INTERNAL_TARGET=LongHeadroomFixedCofactorResidueWeightedLatticeHarmonicCapacityAudit
NEXT=Stage14-t153
```
