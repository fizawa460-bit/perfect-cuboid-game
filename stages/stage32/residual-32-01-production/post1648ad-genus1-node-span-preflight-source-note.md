# Stage32 post1648AD — genus-1 node-span preflight

## Scope

This scratch leaf tests one external genus-1 necessary condition against the exact V6 Picard witness. It does **not** prove effectivity, integrality, existence of a carrier, a rational point, or any Q602/O210 exclusion.

Parent scratch head: `59caa0c09b69b780a659a7d0be1b30f50148c6e4` (post1648AC).

## External theorem lock

Nils Bruin, Jordan Thomas, Anthony Várilly-Alvarado,
*Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*,
Algebra & Number Theory 16 (2022), 1377–1405,
DOI `10.2140/ant.2022.16.1377`,
arXiv `1912.08908v3`, Theorem 1.2.

Only the following necessary-condition content is used: for the perfect-cuboid surface, a genus-1 curve is either a component of a hyperplane section or passes through at least six singularities whose projective span is a hyperplane. No stronger consequence is imported.

## Exact retained inputs

- V6 witness:
  `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`
  - blob `dae90ed19395355bebeebe2a6aa6bb1c6e53c244`
  - canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`
  - exceptional pairings: 47 positive, only zero 0-based exceptional index 5 (`EXC_006`).
- exceptional node coordinates:
  `stages/stage33/33-07/exceptional-p1-tangent-coordinates.json`
  - blob `f4a591bfac5e4e6e79b13309bdc006973d7c5b4e`
  - canonical `beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636`
  - all materialized node coordinates lie in `Q(i)`;
    encoding is `[real_numerator,real_denominator,i_numerator,i_denominator]`.

The verifier performs exact Gaussian elimination over `Q(i)`.

## Exact result

The 47 nodes with positive V6 exceptional pairing have homogeneous vector rank 7, hence projective span `P6`.

A deterministic greedy rank witness is

`EXC_001, EXC_002, EXC_003, EXC_005, EXC_009, EXC_010`.

Their six homogeneous vectors have exact rank 6, so these six nodes span a `P5`, i.e. a hyperplane in `P6`.

Conditional geometric reading: if an effective integral genus-1 carrier has strict-transform class equal to the exact V6 class D, then positive intersection with an exceptional divisor forces the proper transform to meet that exceptional divisor, hence the original curve meets the corresponding node. Under that hypothesis, the six-node hyperplane alternative of Bruin–Thomas–Várilly-Alvarado is already satisfied.

Therefore this theorem gives **no direct obstruction** to the hypothetical V6 carrier.

## Firewalls

- Picard class is not promoted to an effective/integral curve.
- Positive exceptional pairing is not promoted to unconditional node incidence.
- The literature necessary condition is not promoted to carrier existence.
- No residue is excluded.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- No controller / receiver / route / theorem / endpoint / perfect-cuboid credit.

## Next exact route

`SOURCE_BIND_ACTUAL_V6_CARRIER_EQUATION_OR_DISTINGUISHED_SECTION_OR_LOCAL_GALOIS_V4_COMMON_SUPPORT`

The genus-1 node-span necessary-condition lane is closed as a direct obstruction; do not repeat it without strictly stronger source-bound input.
