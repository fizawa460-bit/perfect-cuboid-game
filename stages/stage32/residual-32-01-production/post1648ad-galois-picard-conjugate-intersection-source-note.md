# Stage32 post-1648AD Galois Picard conjugate intersection

Scope: scratch-only continuation of the post-1648Z Galois factor-swap descent gate for the fixed Stage32 V6 class at `g1-d186`, `O=210`, `qprime=4`, `Q=602`. This leaf computes the exact Picard class of the complex conjugate and its intersection number with the original class. It does not identify the geometric support of that intersection and does not exclude any Q602 residue.

## Locked inputs

### Fixed V6 divisor class

`stages/stage32/32-21/post1473-v6-witness-body-recovered.json`

- git blob SHA-1: `dae90ed19395355bebeebe2a6aa6bb1c6e53c244`
- canonical SHA-256: `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`
- retained Picard coordinates SHA-256: `2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726`
- exact self-intersection: `D^2=758`

The 64 coordinates are the same historical retained Magma `Basis(Pic)` coordinates used with `picard_base_rows_retained.py` in the V6 self-intersection replay.

### Previous Galois descent gate

`stages/stage32/residual-32-01-production/post1648z-galois-factor-swap-asymmetric-bidegree-descent-gate.json`

- canonical SHA-256: `cc2fc48738e35d62883e7cf94f6b75c8153d066346b72a0b9ce05deaae1eb36b`
- git blob SHA-1: `d94a0c5cd19ce1f91b803f92233474fe0b99df49`

It source-locks the nontrivial `sigma in Gal(Q(i)/Q)` and proves from the asymmetric modular-factor bidegree `(105,81)` that `sigma(D) != D`.

### Retained integral Picard Galois action

Load only through `stages/stage33/33-07/picard_base_rows_retained.py`; this file is a retained compact asset and is not whole-fetched here.

Exact returned bundle locks:

- canonical SHA-256: `d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c`
- upstream Stoll `Cuboids/cuboids.magma` git blob SHA-1: `0422b69847f2afb97cb7b3ed02ebef91279f61b1`
- exact payloads used: `picard_gram_64x64`, `picard_action_cc_64x64`

The retained Stage33 bridge records this as the historical Magma `Basis(Pic)` with row-action convention. Thus if `A_cc` is the retained action on basis rows and `x_D` is the divisor-coordinate column, the conjugate coordinate column is

`x_sigma = A_cc^T x_D`.

The verifier independently checks `A_cc^2=I` and `A_cc G A_cc^T=G` before using this convention.

For additional source-level provenance, `stages/stage33/33-07/galois-known-class-permutations.json` has canonical SHA-256 `e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30` and locks complex conjugation as an exact involutive permutation of the same 140 known divisor classes, from the same upstream blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Exact computation

Integer matrix arithmetic gives

- `D^2 = 758`;
- `sigma(D)^2 = 758`;
- `D . sigma(D) = 1288`;
- `(D + sigma(D))^2 = 4092`;
- `(D - sigma(D))^2 = -1060`;
- `sigma(D) != D`.

The last inequality agrees independently with the prior asymmetric-bidegree proof and is not being inferred merely from the new coordinates.

## Geometric meaning and firewall

For a hypothetical geometrically irreducible curve `C` in class `D`, the previous gate gives `C != sigma(C)`. Hence `C intersect sigma(C)` is zero-dimensional, and its total geometric intersection degree counted with multiplicity is exactly `1288`.

Every Q-rational point of `C` is fixed by sigma and therefore lies in `C intersect sigma(C)`. Consequently the previous qualitative finite-intersection gate now has an exact intersection-number bound. However the Picard intersection number does **not** identify the support, residue fields, multiplicities, or whether any support point is Q-rational. It also does not prove that the retained effective divisor in class `D` is an integral genus-one carrier.

Therefore this leaf does not remove residues `73,97,235`, does not set `Q602_excluded`, and does not grant receiver/route/theorem/endpoint credit.

## Next exact interface

The remaining genuinely new task is geometric rather than lattice-theoretic:

`IDENTIFY_THE_SUPPORT_OF_C_INTERSECT_sigma(C)_FOR_A_HYPOTHETICAL_INTEGRAL_V6_CARRIER_AND_TEST_ITS_Q_RATIONAL_PART_OR_PROVE_IT_BOUNDARY_DEGENERATE`.

Do not repeat the Picard intersection-number computation or treat `1288` as a support computation.
