# Stage32 post1648AR — two-factor slack and minimal-node-branch bound

Scratch-only necessary-condition adapter. This leaf combines the exact AO special-fibre bookkeeping with the AQ residual-`G`/cusp-grid lock. It derives an exact nonnegative slack identity for each factor projection and uses the two factor directions simultaneously to force many node branches to be the unique FSM-minimal local type. It does not construct or exclude a V6 carrier and grants no MAIN theorem/receiver/route/endpoint credit.

## Parent locks

- AQ finalized exact-head CI head: `1dfb1fb463b3ace0b36354677b6fcbd20a5513ae`.
- AQ canonical SHA256: `1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e`.
- AO canonical SHA256: `39e217c7223732b1834b7e9b96b4361807227f823a5624842a97eddf71390378`.
- V6 exceptional mass: `e=266`.

The local cusp-exponent semantics are those already source-locked in AH/AN from Freitag--Salvati Manni. Write

`a1=4*A`, `a2=4*B`,

with `A,B>0` integers and `A+B` even. Along a normalization branch through a box-surface node, the two target factor orders are `A,B`; on the `A1` resolution the exceptional intersection multiplicity is

`a=min(A,B)`.

If `A!=B`, the strict transform lands on exactly one of the two boundary intersection points of the exceptional curve, with boundary intersection multiplicity

`b=|A-B|/2`.

If `A=B`, that node-boundary contribution is zero. The unique FSM-minimal type is `(A,B)=(1,1)`.

## Exact special-fibre slack identity

Let `N` be the total number of normalization branches over the met box-surface nodes. Since every such branch has exceptional contact `a>=1` and the total exceptional mass is `e=266`, define

`t=e-N=sum(a-1)>=0`.

Fix one factor direction. Let:

- `n` be the factor degree;
- `q` be the total intersection with the six multiplicity-two boundary elliptics in that factor direction;
- `q_node` be the part of `q` occurring at node branches;
- `q_smooth=q-q_node` be the boundary intersection away from box-surface nodes;
- `s` be the number of normalization points contributing to `q_smooth`;
- `eta=q_smooth-s>=0` be the excess smooth-boundary contact multiplicity;
- `rho>=0` be total ramification of the factor map away from the six special fibres.

At a node branch the special-fibre order is `a+2b`, so its ramification contribution is `a+2b-1`. Summed over all node branches this is

`e-N+2*q_node = t+2*q_node`.

At a smooth-boundary point with boundary intersection multiplicity `b>=1`, the special-fibre order is `2b`, hence the ramification contribution is `2b-1`. Summed over those points this is

`2*q_smooth-s`.

The normalization has genus one and the factor base is `P1`, so Riemann--Hurwitz gives total ramification `2n`. Therefore

`2n = t + 2*q_node + 2*q_smooth - s + rho`.

Using `s=q_smooth-eta=q-q_node-eta`, this becomes the exact nonnegative slack identity

`2n-q = t + q_node + eta + rho`.

For the exact two Stage32 factor directions:

- degree 81 with `q=110`: `52 = t + q81_node + eta81 + rho81`;
- degree 105 with `q=182`: `28 = t + q105_node + eta105 + rho105`.

Consequently `t<=28`, hence `N=266-t>=238`, recovering AO's strongest node-preimage bound but now as part of an exact decomposition.

## At least 186 FSM-minimal node branches

Call a node branch nonminimal if `(A,B)!=(1,1)`.

Every nonminimal node branch consumes at least one unit from the three resources `t`, `q81_node`, `q105_node`:

1. if `min(A,B)>1`, then that branch contributes at least one to `t=sum(a-1)`;
2. if `min(A,B)=1` but `(A,B)!=(1,1)`, then `A,B` have the same parity, so the other value is at least `3`; therefore `|A-B|/2>=1`, and the branch contributes at least one to exactly one of `q81_node` or `q105_node`.

Thus

`#nonminimal <= t + q81_node + q105_node`.

From the two slack identities,

`q81_node <= 52-t`,
`q105_node <= 28-t`,

so

`#nonminimal <= 80-t`.

Since the total number of node branches is `N=266-t`, the number of FSM-minimal `(1,1)` branches satisfies

`#minimal >= (266-t)-(80-t)=186`.

Each of these at least 186 branches has:

- exceptional intersection multiplicity exactly `1`;
- zero node-boundary contact in both factor directions;
- local factor orders `(1,1)`;
- zero ramification contribution for both factor maps at that node branch;
- a nonzero finite exceptional landing ratio `lambda`, hence landing away from the two boundary-intersection points on that exceptional curve.

The residual node-stabilizer involution sends `lambda` to `-lambda`; the present leaf does not constrain the actual landing values or force collisions among them.

## Firewalls

- Scratch only; shared `MAIN-STATE.json` and Stage32 authority remain unchanged.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- `V6_carrier_excluded=false`.
- The 186 bound is a necessary branch-type count, not a member construction and not an impossibility result.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit.
