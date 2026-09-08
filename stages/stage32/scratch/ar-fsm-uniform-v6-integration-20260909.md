# Stage32 MAIN scratch — AR/FSM uniform V6 integration

Status: scratch exact unaudited cross-lane integration only. No Stage32 MAIN, Q602/O210, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Correction

The first scratch version incorrectly stated `sum_i min(V6.E_i,10)=232` and therefore claimed a forced 11-branch node. Exact replay gives

- `sum_i min(V6.E_i,9)=232`,
- `sum_i min(V6.E_i,10)=244`.

Thus `N>=238` forces a node with at least **10** branches, not 11. The earlier 11-branch statement is superseded by this repaired file.

## Inputs

Retained AR gives

`t=266-N`,
`52=t+q81_node+eta81+rho81`,
`28=t+q105_node+eta105+rho105`,

hence `t<=28`, `N>=238`, and at least 186 FSM-minimal node branches. The fixed V6 exceptional capacity vector has total mass 266 and positive support 47.

The EX6 FSM16 local order is

`ord_branch(T)/k = 8(a+b-2)`,

with `a=min(A,B)` and `b=|A-B|/2` when unequal. The fixed degree `d=186` gives exact `f`-zero divisor contribution `2kd=372k`.

## Uniform weighted-node cancellation

Let `E=eta81+rho81+eta105+rho105>=0`. Adding the two AR identities gives

`q81_node+q105_node=80-2t-E`.

Across node branches, `sum a=266`, `sum b=q81_node+q105_node`, `N=266-t`. Therefore

`D_node/(8k)=266+(80-2t-E)-2(266-t)=-186-E`,

so

`D_node=-(1488+8E)k`,
`D_nonnode=(1488+8E)k`,
`D_res_nonnode=(1116+8E)k`.

The `t` dependence cancels exactly. This is an algebraic uniformization within the retained AR carrier semantics, not new endpoint credit.

## Corrected node-load consequences

Write `m_i=V6.E_i` and let `r_i` be the number of normalization branches over positive surface node `i`. Then `1<=r_i<=m_i` and `sum r_i=N>=238`.

1. At least 24 of the 47 positive nodes are multibranch. Starting from 47 branches, at least 191 extras are needed. The 23 largest excess capacities `m_i-1` sum to 190, whereas the 24 largest sum to 194.

2. At least 19 positive nodes are contact-saturated: `r_i=m_i`. Indeed `sum_i(m_i-r_i)=266-N=t<=28`, so at most 28 positive nodes can have nonzero deficit.

3. At least one node has at least 10 normalization branches, because `sum_i min(m_i,9)=232<238`. The possible labels are

`[16,18,23,27,28,34,37,38,39,42,44,48]`.

No 11-branch conclusion follows from this argument because `sum_i min(m_i,10)=244>=238`.

4. Let `x_i` count FSM-minimal branches at node `i`. Since `sum x_i>=186` and `x_i<=m_i`, capacity truncation gives the necessary distribution ladder:

- at least 14 nodes have `x_i>=2`;
- at least 10 nodes have `x_i>=3`;
- at least 7 nodes have `x_i>=4`;
- at least 5 nodes have `x_i>=5`;
- at least 2 nodes have `x_i>=6`.

These are necessary branch-load constraints only. They do not force exceptional landing collisions, construct a carrier, or exclude O210.

## Current use

The branch-load route now needs genuinely independent landing/tangent/support information. Replaying AR cannot provide that independence. Separately, the weighted-tensor route still needs an independent upper bound on residual signed nonnode divisor `(1116+8E)k`.
