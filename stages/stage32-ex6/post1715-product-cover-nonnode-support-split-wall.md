# Stage32EX6 — product-cover nonnode ramification support split

Status: `EXPLORATORY_EXACT_BOUNDED_SUPPORT_SPLIT_NO_ENDPOINT_CREDIT`.

## Scope

This leaf continues the retained #1715 product-cover Riemann--Hurwitz equivalence only far enough to separate its exact non-node ramification degree by geometric support. It remains conditional on the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266`.

The previous #1715 leaf proved

`R_nonnode(D)=8E`,

where

`E=eta81+rho81+eta105+rho105`.

The question here is whether the `eta` and `rho` pieces have different exact support meanings upstairs on the `q'=4` product-cover component `D`.

## Exact inputs

From retained post1648AR, for one factor direction:

- `q_smooth` is boundary intersection away from box-surface nodes;
- `s` is the number of normalization points contributing to `q_smooth`;
- `eta=q_smooth-s=sum(b-1)>=0` over those smooth-boundary points;
- `rho>=0` is total ramification of the factor map away from the six special fibres.

At an O266 endpoint branch the Beauville cover is ramified. Away from those O-contacts, the Beauville cover is unramified, and the exact product-cover component is an unramified fourfold cover of the Beauville curve. Hence a non-node point of the normalization has eight lifts to `D`.

The retained #1715 product-cover contract source-locks that near a special fibre the `X(4)` cusp coordinate is the square of the `X(8)` cusp uniformizer.

## Smooth-boundary support

Let a smooth-boundary normalization point have boundary intersection multiplicity `b>=1` in one factor direction. AR gives special-fibre order `2b` for the normalization map to `X(4)`.

Because the local `X(8)->X(4)` cusp coordinate has degree two and `D->N` is unramified at this non-node point, each of the eight lifts to `D` has local degree `b` for the corresponding projection `D->X(8)`.

Therefore each lift contributes ramification order `b-1`, and the eight lifts contribute

`8(b-1)`.

Summing over the smooth-boundary points gives exactly

`R_special,smooth(D)=8*eta`.

Thus `eta` is not merely algebraic slack: upstairs it is exactly one eighth of the non-node projection ramification supported above smooth points of the six special fibres.

## Away-from-special support

At a normalization point away from the six special fibres, the modular map `X(8)->X(4)` is unramified. The eight lifts to `D` therefore preserve the local ramification order of the normalization factor map.

By AR, the total ramification order of the factor map on this locus is `rho`. Hence upstairs the corresponding contribution is exactly

`R_offspecial(D)=8*rho`.

Consequently, factorwise,

- `R81_nonnode(D)=8*eta81+8*rho81`;
- `R105_nonnode(D)=8*eta105+8*rho105`;

and together

`R_nonnode(D)=8*(eta81+rho81+eta105+rho105)=8E`.

This refines the previous total-degree equivalence without changing it.

## What the retained cusp/tangent sources do and do not constrain

The inspected retained chain AQ/AS/AT/AU concerns different support data:

- AQ fixes the 12 target-cusp multiplicities and their special-fibre incidence grid;
- AS gives the cusp-inertia action `lambda -> -lambda` on exceptional landing ratios at node branches and explicitly states that actual landing/jet information is missing;
- AT inserts the correct intermediate quotient/blowup and gives an exact structural conductor split, but explicitly remains nonexcluding;
- AU proves that the 12 target-cusp multiplicities alone cannot force an auxiliary component by weighted Bezout and again identifies tangent/higher-jet or an independent singularity inequality as the missing input.

None of these exact retained statements supplies a member-level adapter that bounds the smooth-boundary ramification support `eta_i` or the off-special ramification support `rho_i` for the actual hypothetical carrier. This is a bounded statement about the inspected source chain, not a repository-wide impossibility theorem.

In particular, the 12 cusp-grid multiplicities must not be recharged as an upper bound for `eta` or `rho` without a new exact adapter.

## Decision

The non-node product-cover budget has the exact support decomposition

`R_nonnode(D)=8eta81+8rho81+8eta105+8rho105`.

Therefore a useful next re-entry must do more than bound the total ramification degree. It must constrain at least one of the two support species:

1. smooth-boundary excess above the six special fibres (`eta81`, `eta105`);
2. ramification away from the six special fibres (`rho81`, `rho105`);
3. or a genuine simultaneous-support relation between the two projections.

Canonical decisions:

- `PRODUCT_COVER_NONNODE_SUPPORT_SPLIT = EXACT`;
- `PRODUCT_COVER_SMOOTH_SPECIAL_RAMIFICATION = 8ETA`;
- `PRODUCT_COVER_OFFSPECIAL_RAMIFICATION = 8RHO`;
- `CUSP_GRID_MULTIPLICITY_RECHARGE_AS_ETA_RHO_CAP = NOT_AUTHORIZED`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- No endpoint exclusion or lower-O descent follows.
- No claim is made that the retained cusp-grid data exhaust all possible support constraints in the repository or literature.
- No actual landing, tangent, jet, or simultaneous critical-value data are invented.
- No Stage32 MAIN or Perfect Cuboid credit follows.
- No hostile-audit credit or merge is implied.
