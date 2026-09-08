# Stage32EX6 — product-cover Riemann–Hurwitz equivalence wall

Status: `EXPLORATORY_EXACT_BOUNDED_EQUIVALENCE_WALL_NO_ENDPOINT_CREDIT`.

## Scope

This leaf re-enters the merged EX6 O=266 endpoint only to test whether lifting the retained two-factor data to the exact product-cover component produces a new degree-only obstruction.

It does not assume or construct a global V6 carrier. All statements below are conditional on the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used by the merged EX6 lineage.

## Source locks

Retained Stage32 inputs:

- `post1473-specific-class-multibranch-beauville-odd-branch-wall.md`: the connected Beauville double cover `Y->N`, and an irreducible normalized product-cover component `D->Y` unramified of degree `q' in {1,2,4}`.
- `post1484-v6-modular-factor-bidegree-source-note.md`: for the exact V6 factor degrees `(105,81)`, integrality forces `q'=4`; the two projections `D->X(8)` have degrees `105` and `81`; the X(4) cusp coordinate is the square of the X(8) cusp uniformizer.
- `post1648an-a1-strict-transform-delta-feasibility-source-note.md`: local endpoint branch parameters `A=a1/4`, `B=a2/4`, with `A,B>0`, `A+B` even, and exceptional contact `m=min(A,B)`.
- `post1648ar-two-factor-slack-minimal-branches-source-note.md`: at O266, `m=1`, `b=|A-B|/2`, and
  - `52=q81_node+eta81+rho81`,
  - `28=q105_node+eta105+rho105`,
  - `E=eta81+rho81+eta105+rho105`,
  - hence `q81_node+q105_node=80-E`.

The genus-five fact for `X(8)` is source-locked in the retained post1473 note from Freitag–Salvati Manni.

## Product-cover genus and projection ramification

At O266, the Beauville double cover satisfies

`2*g(Y)-2=O=266`,

so

`g(Y)=134`.

The exact modular-factor source forces `q'=4`, and `D->Y` is unramified of degree four. Therefore

`2*g(D)-2=4*(2*g(Y)-2)=1064`,

hence

`g(D)=533`.

For the two projection maps to the genus-five curve `X(8)`, Riemann–Hurwitz gives exact total ramification

- degree 105 projection: `R105=1064-8*105=224`;
- degree 81 projection: `R81=1064-8*81=416`.

Thus

`R105+R81=640`.

## Exact local adapter at an O266 node

At O266 every exceptional contact has `m=min(A,B)=1`.

The normalized Beauville double cover is ramified at every one of the 266 odd node contacts. Since `D->Y` is unramified of degree four, each such point of `N` has four points above it on `D`. The composite `D->N` has local ramification index two at each lift.

Let `Q` be a local parameter on `N` and `s` one on `D`; then `Q` is a unit times `s^2`. The retained modular-factor note identifies an `X(4)` cusp coordinate with the square of the `X(8)` cusp uniformizer. Combined with the retained AN orders, the two local projection degrees `D->X(8)` at each lift are exactly `A` and `B`.

Therefore the sum of the two projection ramification orders at one lift is

`(A-1)+(B-1)=A+B-2=2b`.

There are four lifts, so one N-node branch with boundary slack `b` contributes exactly

`8b`

to the combined product-cover projection ramification.

Summing all node branches gives

`R_node(D)=8*(q81_node+q105_node)=8*(80-E)=640-8E`.

Hence the combined ramification away from the O266 node lifts is exactly

`R_nonnode(D)=640-(640-8E)=8E`.

Factorwise:

- `R105_nonnode=224-8*q105_node=8*(eta105+rho105)`;
- `R81_nonnode=416-8*q81_node=8*(eta81+rho81)`.

Thus the retained AR slack identities are exactly the product-cover Riemann–Hurwitz decomposition divided by eight.

## Consequence for the FSM16 continuation

The merged EX6 FSM16 leaf records the normalization-side signed residual target

`D_res_nonnode=(1116+8E)k`.

This leaf does **not** split the invariant FSM16 tensor by removing `f` upstairs: the full tensor is invariant because the weight-`4k` form `f` participates in the transformation law, and no global product-cover divisor for the remaining factors is claimed here.

What is exact is narrower: the only variable `E` appearing in the retained residual target is already exactly the non-node product-cover projection ramification divided by eight,

`E = R_nonnode(D)/8`.

Therefore merely recomputing total projection ramification degree on the q'=4 product cover cannot supply an independent bound on `E`; it reproduces the AR ledger identically. Any useful continuation must constrain more than total ramification degree.

The constant arithmetic identity `1116=6*186` is noted only as arithmetic and is not promoted to a tensor-descent formula.

## Decision

Canonical decisions:

- `PRODUCT_COVER_RH_ADAPTER = SOURCE_LOCKED`;
- `PRODUCT_COVER_NONNODE_RAMIFICATION = 8E`;
- `DEGREE_ONLY_PRODUCT_COVER_RH_ROUTE = EQUIVALENT_TO_AR_TWO_FACTOR_RH_SLACK`;
- `FSM16_RESIDUAL_UPSTAIRS_DIVISOR_CLAIMED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

A future useful re-entry must add information not determined by total ramification degree: support/incidence restrictions on the non-node critical divisor, simultaneous critical-value constraints for the two projections, member-level landing/tangent restrictions, or a genuinely different tensor/correspondence inequality.

## Firewalls

- No global V6 carrier is constructed.
- No O266 exclusion follows.
- No lower-O descent follows.
- No effectiveness statement for the normalization-side signed residual divisor is added.
- No global `T/f` tensor or product-cover residual tensor is asserted.
- The equivalence concerns ramification-degree bookkeeping only; support and incidence data remain unresolved.
- Stage32 MAIN authority and current O210/Q602 routing are unchanged.
- No Perfect Cuboid existence or nonexistence credit follows.
