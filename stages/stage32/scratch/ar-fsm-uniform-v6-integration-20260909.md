# Stage32 MAIN scratch — AR/FSM uniform V6 integration

Status: scratch exact unaudited cross-lane integration only. No Stage32 MAIN, Q602/O210, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Inputs

This leaf combines only retained exact formulas already present on current main:

- `post1648ar-two-factor-slack-minimal-branches.json` and its source note:
  `t=266-N`, `52=t+q81_node+eta81+rho81`, `28=t+q105_node+eta105+rho105`, hence `t<=28`, `N>=238`, and at least 186 FSM-minimal node branches.
- the EX6 FSM16 weighted-node local order:
  `ord_branch(T)/k = 8(a+b-2)`, where `a=min(A,B)` and `b=|A-B|/2` when unequal;
- the EX6 exact `f`-zero divisor contribution for fixed degree `d=186`: `2kd=372k`;
- the fixed V6 exceptional pairing vector, total mass `266`, positive support `47`.

No endpoint-only identity is imported as an assumption.

## Uniform weighted-node cancellation

Let

`E = eta81+rho81+eta105+rho105 >= 0`.

Adding the two AR slack identities gives

`q81_node+q105_node = 80-2t-E`.

Across all node branches,

`sum a = 266`, `sum b = q81_node+q105_node`, and `N=266-t`.

Therefore

`D_node/(8k) = sum(a+b-2)`
`= 266 + (80-2t-E) - 2(266-t)`
`= -186-E`.

Thus

`D_node = -(1488+8E)k`.

The dependence on `t` cancels exactly. On the genus-one normalization the total tensor divisor degree is zero, so

`D_nonnode = (1488+8E)k`.

Subtracting the exact canonical `f`-zero contribution `372k` gives the same residual signed nonnode threshold as the O266 endpoint calculation:

`D_res_nonnode = (1116+8E)k`.

The new point is not a stronger endpoint result; it is that the retained threshold is algebraically uniform over the fixed-V6 carrier semantics covered by AR, including the current O210 target, rather than depending on `t=0`.

## Exact node-load consequences

AR gives `N>=238` normalization branches over the 47 positive exceptional nodes.

Write `m_i=V6.E_i`. Since each branch over node `i` contributes positive exceptional order, its branch count `r_i` satisfies `1<=r_i<=m_i`, and `sum r_i=N`.

Starting with one branch at each positive node gives 47 branches. Reaching 238 requires at least 191 extra branches. The 23 largest capacities `m_i-1` sum to only 190, while the 24 largest sum to 194. Hence at least **24 of the 47 positive surface nodes are multibranch**.

Also,

`sum_i min(m_i,10)=232<238`.

Therefore at least one node has at least **11 normalization branches**. Such a node must have `m_i>=11`, restricting its label to

`[18,23,27,28,38,39,42,48]`.

These are necessary conditions only. They do not identify an actual node, construct a carrier, or exclude O210.

## Decision

The current MAIN normalization-location problem has a much stronger scratch reduction than the previous 47-to-38 filter:

- surface-node multibranch is forced by retained AR semantics;
- at least 24 positive nodes are multibranch;
- at least one of eight high-capacity labels has at least 11 normalization branches;
- the weighted FSM tensor node debt is uniformly `-(1488+8E)k`;
- after the exact `f` contribution, residual signed nonnode degree is `(1116+8E)k`.

The first missing independent input is now a source-bound/member-level restriction on this high branch load, landing/tangent collisions, or an upper bound on the residual signed nonnode divisor. Replaying the same AR slack identities does not count as an independent cap.
