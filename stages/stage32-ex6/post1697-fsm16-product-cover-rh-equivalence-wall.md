# Stage32EX6 — FSM16 product-cover RH equivalence wall

Status: `EXPLORATORY_EXACT_BOUNDED_EQUIVALENCE_WALL_NO_ENDPOINT_CREDIT`.

## Scope

This leaf re-enters the merged EX6 O=266 endpoint only to test whether the retained FSM16 residual non-node degree target

`D_res_nonnode=(1116+8E)k`

contains an independent degree obstruction beyond the already-retained Stage32 two-factor Riemann--Hurwitz slack.

It does not assume or construct a global V6 carrier. All statements below are conditional on the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used by the merged EX6 lineage.

## Source locks

Retained Stage32 inputs:

- `post1473-specific-class-multibranch-beauville-odd-branch-wall.md`: the connected Beauville double cover `Y->N`, and an irreducible normalized product-cover component `D->Y` unramified of degree `q' in {1,2,4}`.
- `post1484-v6-modular-factor-bidegree-source-note.md`: for the exact V6 factor degrees `(105,81)`, integrality forces `q'=4`; the two projections `D->X(8)` have degrees `105` and `81`.
- `post1648an-a1-strict-transform-delta-feasibility-source-note.md`: local endpoint branch parameters `A=a1/4`, `B=a2/4`, with `A,B>0`, `A+B` even, and exceptional contact `m=min(A,B)`.
- `post1648ar-two-factor-slack-minimal-branches-source-note.md`: at O266, `m=1`, `b=|A-B|/2`, and
  - `52=q81_node+eta81+rho81`,
  - `28=q105_node+eta105+rho105`,
  - `E=eta81+rho81+eta105+rho105`,
  - hence `q81_node+q105_node=80-E`.
- merged EX6 weighted/f-residual contracts: `D_res_nonnode=(1116+8E)k`.

External primary source:

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1 proof / arXiv:1303.6495. We use only:

- `X(8)` has genus 5;
- the tensor is `T=Delta(z)^k Delta(w)^k f(z,w)(dz dw)^(8k)`;
- in the X(8) cusp uniformizer `p=exp(2*pi*i*z/8)`, `Delta(z)` has order 8 while `dz` has logarithmic pole order 1;
- away from cusps `Delta` is nonzero.

## Product-cover genus and projection ramification

At O266, the Beauville double cover satisfies

`2*g(Y)-2=O=266`,

so

`g(Y)=134`.

The exact modular-factor source forces `q'=4`, and `D->Y` is unramified of degree four. Therefore

`2*g(D)-2=4*(2*g(Y)-2)=1064`,

hence

`g(D)=533`.

For the two projection maps to the genus-five curve X(8), Riemann--Hurwitz gives exact total ramification

- degree 105 projection: `R105=1064-8*105=224`;
- degree 81 projection: `R81=1064-8*81=416`.

Thus

`R105+R81=640`.

## Exact local adapter at an O266 node

At O266 every exceptional contact has `m=min(A,B)=1`.

The normalized Beauville double cover is ramified at every one of the 266 node contacts. Since `D->Y` is unramified of degree four, each point of `N` has exactly four points above it on `D`, each with ramification index two for `D->N`.

If `s` is a local parameter on `D`, then a local parameter on `N` is a unit times `s^2`. The X(4) factor cusp coordinate is the square of the X(8) cusp uniformizer. Combining this with the retained AN orders shows that the two local projection degrees `D->X(8)` at a lift are exactly `A` and `B`.

Therefore the sum of the two projection ramification orders at one lift is

`(A-1)+(B-1)=A+B-2=2b`.

There are four lifts, so one N-node branch with boundary slack `b` contributes exactly

`8b`

to the combined product-cover projection ramification.

Summing all node branches gives

`R_node(D)=8*(q81_node+q105_node)=8*(80-E)=640-8E`.

Hence the combined ramification away from the O266 node lifts is exactly

`R_nonnode(D)=640-(640-8E)=8E`.

Factorwise this is the exact scaled AR pair:

- `R105_nonnode=224-8*q105_node=8*(eta105+rho105)`;
- `R81_nonnode=416-8*q81_node=8*(eta81+rho81)`.

Thus the retained AR slack identities are precisely the product-cover Riemann--Hurwitz decomposition divided by eight.

## FSM16 residual divisor upstairs

Consider the FSM16 tensor with the `f` divisor removed locally. On `D`, for either projection:

- at a cusp point of local projection degree `e`, `Delta(z)^k` contributes `8e*k` and `(dz)^(8k)` contributes `-8k`, so the signed order is `8(e-1)k`;
- at an interior point of local projection degree `e`, `Delta` is nonzero and the pulled-back differential contributes `8(e-1)k`.

Thus the local orders patch to a nonnegative residual divisor on `D`, with exact total degree

`D_res(D)=8*(R105+R81)k=5120k`.

At the four lifts of an O266 node branch, the residual order is `16b*k` per lift, hence `64b*k` per N-node branch. Therefore

`D_res,node(D)=64*(q81_node+q105_node)k=(5120-64E)k`,

and the exact non-node residual divisor upstairs is

`D_res,nonnode(D)=64E*k`.

In particular,

`(1/8) D_res,nonnode(D)=8E*k`.

## Relation to the merged EX6 residual target

The merged EX6 normalization-side residual degree is

`D_res_nonnode(N)=(1116+8E)k`.

The product-cover computation shows that the variable part is exactly the old two-factor slack:

`D_res_nonnode(N) - (1/8)D_res,nonnode(D) = 1116k = 6*d*k`

for `d=186`.

This is an exact numerical comparison. This leaf does **not** assert a new canonical descent identity for a global `T/f` tensor on `N`; the merged firewall that `T/f` need not descend globally remains in force.

## Decision

The degree-only continuation of the weighted FSM16 residual route is not an independent obstruction. Once lifted to the exact q'=4 product-cover component, its variable non-node degree is exactly the same `E` already present in the AR two-factor Riemann--Hurwitz slack.

Canonical decisions:

- `FSM16_PRODUCT_COVER_RH_ADAPTER = SOURCE_LOCKED`;
- `FSM16_RESIDUAL_VARIABLE_PART = 8E_ON_N_EQUIVALENT_TO_64E_UPSTAIRS`;
- `FSM16_DEGREE_ONLY_RESIDUAL_ROUTE = EQUIVALENT_TO_AR_TWO_FACTOR_RH_SLACK`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

A future useful FSM16/product-cover re-entry must add information that is not determined by total ramification degree: for example support/incidence restrictions on where the `64E*k` upstairs residual divisor may lie, simultaneous critical-value constraints, member-level landing restrictions, or a genuinely different tensor/correspondence inequality.

## Firewalls

- No global V6 carrier is constructed.
- No O266 exclusion follows.
- No lower-O descent follows.
- No claim is made that the normalization-side residual divisor is effective.
- No global descended `T/f` tensor on `N` is asserted.
- The exact equivalence concerns degree/ramification bookkeeping only; support and incidence data are not identified by this calculation.
- Stage32 MAIN authority and current O210/Q602 routing are unchanged.
- No Perfect Cuboid existence or nonexistence credit follows.
