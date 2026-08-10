# Stage14 minimal common theorem envelope and receiver separation

This document freezes the largest common analytic object shared by the live
collision and Gaussian routes.  It is an interface theorem envelope, not a new
incidence or dispersion estimate.

## Common core

Fix an exact physical packet `X` and a common auxiliary-prime family `P`.  Each
state retains the full label

\[
 z=(R,\xi,k,U,V,\mathfrak b,\mathfrak i,\mathfrak r),
\]

all physical masks, and a coefficient `a_z`.  For an admissible row
`c_z(p)` define

\[
 \mathcal K_X(a,c)=
 \sum_{z\ne z'}a_z\overline {a_{z'}}
 \left|\sum_{p\in\mathcal P}c_z(p)c_{z'}(p)\right|^2.
\]

The envelope `CommonPhysicalCenteredPrimePairKernel` consists only of:

1. an exact or multiplicity-controlled physical-state lift;
2. the same prime family and the same good-prime masks;
3. signed common-refinement aggregation before the norm;
4. the shared `U/V` modulus and divisor hyperbola;
5. exact subtraction of `z=z'` once;
6. separation of the residue diagonal from principal squareclass coherence;
7. completion before ordered-pair collapse;
8. uniformity on the receiver's critical strip.

These clauses identify a common kernel.  They do not bound it.

## Receiver extensions

| receiver | extra hypotheses beyond the core | admissible conclusion | owner |
|---|---|---|---|
| `PositiveXiKCollision` | unit/nonnegative specialization; same-`k` row coherence; `o(P)` bad-prime budget; centered `H_xi^2 P` scale | `C_off(xi) << H_xi^2/P * B^o(1)` | s |
| `SignedGaussianDispersion` | actual Gaussian rows; selector-sensitive signed estimate; compatible conductor and split-prime scale | a bound for `K_X(a,c_G)` only on its stated coefficient class | t/tH or named dispersion owner |
| `SharedUBipartiteSquareclassEnergy` | fixed primitive `U`; divisor fan retained; both `(pi,V)` coordinates retained; squareclass fibers counted without row/column globalization | after merged tH15, same-`pi` and same-`V` slices are near-linear; only `SharedUPhysicalBipartiteDispersion` may close the transverse term and hence `E_U <= R_U B^o(1)` | t/tH15/t55 |
| `PrimePairProjectiveSlopeDispersion` | alias-free projective slope adapter; exact centered correction; joint distinct-prime averaging | the named projective second moment | s |

## Separation theorem

The common core alone implies none of the receiver conclusions.  The following
promotions are prohibited unless the listed extension hypotheses are proved:

- signed Gaussian cancellation to positive collision control (positivity and
  same-`k` coherence are missing);
- raw `H P^2` Gaussian scale to centered `H^2 P` scale;
- projective no-alias geometry to joint prime-pair dispersion;
- a fixed-`U` divisor fan, or separate row/column estimates, to bipartite
  squareclass energy;
- any one receiver theorem to another merely because both instantiate
  `CommonPhysicalCenteredPrimePairKernel`.

The H0 two-row sign example and the Gaussian squareclasses `1,6` at primes
`5,13` witness the first two logical separations.  The Latin-square guard from
the t route witnesses the row/column-to-bipartite separation.  Merged tH15
sharpens this last boundary by proving the same-`pi` and same-`V` slices and
isolating the transverse term; it does not prove the transverse dispersion.

## Import rule

An owning line may import the common core and exact adapters.  It must prove its
own extension hypotheses on the exact physical coefficient space.  A failed
extension is returned to that owner and does not block toolbox main.  Toolbox
does not own a new arithmetic theorem and does not combine conditional
receivers by taking their minimum.

## Current boundary

`CommonPhysicalCenteredPrimePairKernel` is frozen as the minimal common
envelope.  All four named estimates in the table remain open.  In particular,
the envelope does not improve the unconditional physical whole-family exponent
`7/8`.
