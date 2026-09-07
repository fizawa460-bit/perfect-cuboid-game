# Stage32EX6 post-1697 — FSM16 weighted node-divisor wall

Status: **EXPLORATORY EXACT BOUNDED WALL — NO ENDPOINT CLOSURE CREDIT**.

## Question

After the `S_cusp` cardinality route was shown to be dominated by the retained AR minimal-branch bound, can the actual signed local divisor order of the Freitag–Salvati Manni tensor produce a sharper O266 obstruction?

## Source locks

External source:

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1; arXiv:1303.6495.

In the proof of Theorem 3.1, for

`T = Delta(z)^k Delta(w)^k f(z,w) (dz dw)^(8k)`, 

the branch through a box node has modular cusp exponents `a1,a2`, the differential factor contributes pole order `16k`, `Delta(z)^k Delta(w)^k` contributes zero order `(a1+a2)k`, and `f` is chosen nonzero at the nodes. Therefore the signed local divisor order at that node branch is exactly

`ord_branch(T) = (a1+a2-16) k`,

with negative sign meaning a pole.

Retained Stage32 adapters:

- `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`;
- `stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches-source-note.md`.

They source-lock

`a1=4*A`, `a2=4*B`, `A,B>0`, `A+B` even,

`m=min(A,B)`,

and for `A!=B`

`b=|A-B|/2`,

where `b` is the node-boundary contribution to exactly one of the two factor ledgers.

## Endpoint specialization

At `O=266`, every exceptional contact has multiplicity `m=1`. Hence on every one of the `N=266` node branches,

`min(A,B)=1`.

Because `A+B` is even, the other entry has the form `1+2b` with integer `b>=0`. Therefore

`A+B = 2+2b`,

`a1+a2 = 4(A+B) = 8+8b`.

Substitution into the exact FSM16 local divisor order gives

`ord_branch(T) = 8(b-1)k`.

Thus:

- `b=0`, equivalently `(A,B)=(1,1)`, contributes a pole of order `8k`;
- `b=1`, equivalently `{A,B}={1,3}`, is divisor-neutral at the node;
- `b>=2` contributes a node zero of order `8(b-1)k`.

This is stronger information than counting only the `(1,1)` branches.

## Exact summed node contribution

By the retained AR semantics, the sum of `b` over all endpoint node branches is exactly

`q81_node + q105_node`.

Hence the total signed divisor contribution of all 266 node branches is

`D_node/k = 8 * (q81_node + q105_node - 266)`.

At O266, `t=0`, and AR gives

`52 = q81_node + eta81 + rho81`,

`28 = q105_node + eta105 + rho105`,

with all slack variables nonnegative. Therefore

`q81_node + q105_node <= 80`.

Consequently

`D_node/k <= 8*(80-266) = -1488`.

Equivalently, the endpoint forces a net node pole debt of at least

`1488 k`.

Since `q81_node,q105_node>=0`, the exact node pole debt lies in the interval

`1488 k <= -D_node <= 2128 k`.

## Slack-refined form

Define

`E = eta81 + rho81 + eta105 + rho105 >= 0`.

The two AR identities give

`q81_node + q105_node = 80-E`.

Therefore the exact node signed divisor is

`D_node = -(1488 + 8E) k`.

The pulled-back tensor has divisor degree

`16(2g-2)k = 0`

because the normalization genus is `g=1`. Thus the complement of the node fibres must carry the exact opposite signed contribution:

`D_nonnode = (1488 + 8E) k`.

In particular,

`D_nonnode >= 1488 k`.

This is the new quantitative re-entry threshold.

## What would close this route

A global/member-level theorem would exclude O266 through this exact tensor-divisor architecture if it forced, for the same tensor and the same carrier,

`D_nonnode < 1488 k`.

More generally, if it retains the AR slack variable `E`, the sharp contradiction threshold is

`D_nonnode < (1488 + 8E) k`.

Potential sources of such a bound would have to control the actual non-node divisor of the pulled-back tensor: smooth-boundary zeros, ramification/differential contributions, and the zero divisor of `f`, without double-counting terms already encoded in AR.

No such upper bound is presently source-locked. The published FSM16 proof supplies a lower bound on zeros, not the required upper bound on the non-node signed divisor. Therefore the weighted calculation does not itself exclude O266.

## Decision

`FSM16_WEIGHTED_NODE_DIVISOR = EXACT_POLE_DEBT_THRESHOLD_OBTAINED`

`MINIMUM_NODE_POLE_DEBT_PER_K = 1488`

`O266_ENDPOINT_EXCLUDED = false`.

Useful re-entry is no longer an `S_cusp` counting problem. It is an upper-bound problem for the exact non-node signed divisor contribution, with threshold `1488k` at minimum and `1488k+8Ek` in the slack-refined form.

## Firewalls

- The local signed order is taken from the exact FSM16 proof ingredients plus the already-retained AN/AR adapter.
- No claim is made that the FSM16 tensor is holomorphic on the resolved surface; the source explicitly says this was not proved.
- No upper bound on `D_nonnode` is asserted.
- No global V6 carrier is constructed.
- No endpoint exclusion, O264 descent, theorem, receiver, or Perfect Cuboid credit follows.
- No merge is authorized.
