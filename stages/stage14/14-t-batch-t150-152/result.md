# Stage14-t-batch — t150 through t152

## Status

`STAGE14_T_BATCH=COMPLETE`

Starts from latest merged main

```text
007ff032d7f757035029a04d6065b605c8a65ef0
```

and executes three substantive fixed-U work units.

## Stage14-t150

Replaces the per-norm `B^o(1)` representation envelope for endpoint cofactors by a direct lattice count.  Because all live cofactors already satisfy

```text
z == rho_* (mod d)
```

inside one fixed broad Gaussian sector, they lie in one affine lattice coset of covolume `d^2`.

For a dyadic endpoint width layer `Y<H<=2Y`, the exact endpoint map gives norm thickness

```text
Delta_n <= Y/(2*h*k0)
```

and radius

```text
r_0 <= B^(1/4)/sqrt(h*k0).
```

Hence

```text
#Z(Y)
 <= C*(
      Y/(h*k0*d^2)
      + B^(1/4)/(d*sqrt(h*k0))
      + 1 ).
```

This removes the opaque `B^o(1)` per-norm representation loss.

## Stage14-t151

Combines the cofactor-lattice density with the already-fixed ordinary Gaussian prime-residue denominator

```text
q_d=|(Z[i]/dZ[i])^x|.
```

The principal endpoint capacity becomes

```text
M_Y
 <= C*(Y+1)/q_d * (
      Y/(h*k0*d^2)
      + B^(1/4)/(d*sqrt(h*k0))
      + 1 ).
```

At fixed-power scale the lattice-boundary term does not form an independent receiver.  The singleton term is exactly the sparse residue-normalized near-full branch; every other principal endpoint obstruction is carried by the two-dimensional annulus area term.

## Stage14-t152

The annulus-area principal condition forces

```text
Y
 >= B^(1/4-o(1))
    * d * sqrt(q_d*h*k0).
```

Since `q_d=d^2*B^o(1)`, this is

```text
Y >= B^(1/4-o(1))*d^2*sqrt(h*k0).
```

This supersedes the merged t149 floor by one additional factor `d`.

On beyond-Mitsui endpoint packets, merged t144 gives `h*k0>=C*d`, hence

```text
Y >= B^(1/4-o(1))*d^(5/2).
```

The sparse one-cofactor branch is retained with its exact group-order normalization

```text
H_*/q_d >= B^(1/2-o(1)).
```

The long-headroom beyond-Mitsui branch remains separate.

## New receiver

```text
SafeMitsuiSingleCofactorSubKaiExactResidueGroupNearFullPrimeOccupancy
OR
SafeMitsuiGaussianLatticeAreaManyCofactorSubKaiPrimeOccupancy
OR
BeyondMitsuiSingleCofactorExactResidueGroupNearFullPrimeOccupancyBias
OR
BeyondMitsuiGaussianLatticeAreaManyCofactorEndpointPrimeOccupancyBias
OR
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The fourth branch carries the strengthened necessary width

```text
Y >= B^(1/4-o(1))*d^(5/2).
```

This is a material receiver change, so the common batch contract stops after three substantive units.

## H decision

No new tH is opened.

```text
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
```

Completed tH32 already covers the same safe fixed-sector/fixed-residue theorem object above its near-full threshold; only the internally certified lower width floor has changed.  The beyond-Mitsui individual-modulus branch is still outside that theorem range and has not yet become a new theorem-compatible target.

## Batch ledger

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=007ff032d7f757035029a04d6065b605c8a65ef0
BATCH_PUBLICATION_MAIN_SHA=007ff032d7f757035029a04d6065b605c8a65ef0
BATCH_FIRST_STAGE=Stage14-t150
BATCH_LAST_STAGE=Stage14-t152
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
GAUSSIAN_COFACTOR_LATTICE_RESIDUE_DENSITY_PROVED=true
DOUBLE_RESIDUE_NORMALIZED_ENDPOINT_CAPACITY_PROVED=true
T149_MANY_WIDTH_FLOOR_SUPERSEDED=true
BEYOND_MITSUI_D_FIVE_HALVES_WIDTH_GAIN_PROVED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
TH33_NEEDED=false
NEXT=Stage14-t153
```

`Stage14-t153` should audit the long-headroom branch using the same fixed cofactor-residue lattice in a weighted harmonic/dyadic reciprocal-hyperbola count, without importing the endpoint annulus estimate outside its range.
