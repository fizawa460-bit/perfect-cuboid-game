# Stage32EX6 scratch — rank-3 nonminimal node ramification coupling

Status: `SCRATCH_EXACT_BOUNDED_RANK3_NONMINIMAL_NODE_RAMIFICATION_COUPLING_NO_ENDPOINT_CREDIT`

Scratch only. This leaf does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

- PR #1715 retained EX6 head used for authority context:
  `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- O266 retained AR slack:
  `80 = Q + Eta + Rrho`, with `Q=q81_node+q105_node`.
- Six-rank3 scalar budget scratch leaf:
  `scratch-six-rank3-simultaneous-rh-budget.md`.
- Rank3 ruling/globalization scratch leaf:
  `scratch-rank3-fibration-ruling-fourjet-adapter-wall.md`.
- Standard-cusp rank3/theta adapter:
  `scratch-standard-cusp-r3-theta-fourjet-adapter.md`.
- Replay verifier:
  `scratch_verify_rank3_nonminimal_ramification_coupling.py`.

## 1. Nonminimal O266 branches have an exact rank3 local-degree charge

At O266 every node branch has `min(A,B)=1`. For a nonminimal branch, parity gives either

`(A,B)=(1,1+2b)`

or

`(A,B)=(1+2b,1)`

with integer `b>=1`.

In the resolved A1 chart the exceptional slope is `u=q/p`. Therefore the branch has either

`ord(u)=b`

or

`ord(1/u)=b`.

For the rank-three fibration assigned to that node block, the global pencil parameter is a Möbius coordinate on the same exceptional ruling. At the standard modular cusp the exact theta adapter is

`T = u + u*(1-u^8)*x^4 + O(x^8)`.

Hence when `u` tends to zero with order `b`, the correction has strictly higher order and

`ord(T)=b`.

When `u` has a pole of order `b`, the reciprocal target coordinate gives the same local degree `b`.

Thus every nonminimal O266 branch with AR node charge `b` has exact local degree `b` in its assigned rank-three pencil and contributes

`b-1`

Riemann--Hurwitz ramification units there.

Summing over all nonminimal branches, if `L` is their number, AR's node resource is

`Q = sum b`,

so the aggregate six-rank3 nonminimal node ramification is exactly

`R_rank3_nonminimal_node = Q-L`.

This is stronger than merely using `L<=Q`.

## 2. Total six-rank3 RH capacity is exactly 850

For the six rank-three base blocks with exceptional masses `M_j`, the full RH degree of block `j` is

`186-M_j`.

Because the six blocks partition all O266 exceptional contacts,

`sum M_j = 266`.

Therefore the sum of the six complete RH degrees is

`sum_j (186-M_j) = 6*186-266 = 850`.

This identity does not require an explicit numbered EXC-to-block adapter.

## 3. Aggregate flatness/failure inequality

Let

- `L` = number of nonminimal O266 node branches;
- `M=266-L` = number of FSM-minimal branches;
- `F_r` = number of minimal branches that fail rank3-`r`-flatness.

Each rank3-`r`-flat minimal branch consumes at least `r` RH units. The nonminimal branches consume exactly `Q-L` node RH units. Thus a necessary condition is

`r*(M-F_r) + (Q-L) <= 850`.

Substitute `M=266-L`:

`r*(266-L-F_r) + Q-L <= 850`.

At O266, every nonminimal branch consumes at least one unit of `Q`, hence `L<=Q`. For fixed `Q`, the inequality is easiest to satisfy at maximal `L=Q`. Therefore

`r*(266-Q-F_r) <= 850`.

Using

`Q=80-E`, `E:=Eta+Rrho`,

we obtain

`F_r >= max(0, ceil(186+E-850/r))`.

For the first load-bearing values:

- `F_4 >= max(0,E-26)`;
- `F_5 >= 16+E`;
- `F_6 >= 45+E`;
- `F_7 >= 65+E`.

These are exactly the same failure floors produced independently by the finite six-block integer optimization. The new derivation explains why: the blockwise optimization is the distributed form of one aggregate RH identity plus the exact nonminimal charge `Q-L`.

## 4. Interpretation

The strongest unconditional scalar statement at the current level is still

`F_5 >= 16+E >=16`.

So every hypothetical O266 carrier must have at least sixteen FSM-minimal node branches whose assigned global rank-three pencil has local degree at most five.

For `r=4`, rank3-four-flat failure is forced only when `E>=27`, with at least `E-26` failures.

This does not itself exclude O266 because no retained theorem forces rank3-five-flatness or rank3-four-flatness on the complementary population. It does, however, convert the previous partition optimization into a local AR-compatible ramification law and removes dependence on any sampled six-block mass vector.

## Canonical scratch decisions

- `NONMINIMAL_BRANCH_LOCAL_FORM = (1,1+2b)_or_(1+2b,1)`;
- `NONMINIMAL_ASSIGNED_RANK3_LOCAL_DEGREE = b`;
- `NONMINIMAL_ASSIGNED_RANK3_RH_COST = b-1`;
- `AGGREGATE_NONMINIMAL_RANK3_NODE_RAMIFICATION = Q-L`;
- `TOTAL_SIX_RANK3_RH_DEGREE = 850`;
- `AGGREGATE_RANK3_FLATNESS_BUDGET = r*(266-L-F_r)+(Q-L)<=850`;
- `RANK3_R4_FLAT_FAILURES_GTE = max(0,E-26)`;
- `RANK3_R5_FLAT_FAILURES_GTE = 16+E`;
- `RANK3_R6_FLAT_FAILURES_GTE = 45+E`;
- `RANK3_R7_FLAT_FAILURES_GTE = 65+E`;
- `SIX_BLOCK_DP_AND_AGGREGATE_COUPLING_AGREE = true`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- The rank3 local-degree statement concerns the unique rank-three pencil attached to the branch's eight-node base block; it is not summed over six pencils per branch.
- The standard-cusp theta formula is used only to source-lock that the ruling parameter has the same leading order as the A1 slope. No finite landing condition is inferred.
- `Q-L` is part of the same six-rank3 RH budget and is not double-counted as an independent eta/rho cap.
- The equality of the aggregate and blockwise failure floors does not prove an actual block-mass vector.
- No member equation, hostile audit, retained consolidation, Stage32 MAIN, lower-O, or Perfect Cuboid credit follows.
