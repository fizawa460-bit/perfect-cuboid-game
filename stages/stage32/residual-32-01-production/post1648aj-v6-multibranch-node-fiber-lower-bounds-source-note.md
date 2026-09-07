# Stage32 post1648AJ — V6 multibranch-node and normalization-fiber lower bounds

Scratch-only exact combinatorial consequence of post1648AI. No theorem / receiver / route / endpoint credit is granted by this file.

## Parent leaf

- post1648AI exact scratch head: `31ad1e33a569ae3f753bff002ef8c4fc980aad93`
- AI canonical: `8506d88f630e5d097de5355491e91f072f7728bac484490e3ab3067db7b9db97`
- AI dedicated CI: run `34076480820`, job `101603494707`, SUCCESS.

AI proves the bounded statement:

`NO_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER_UNIBRANCH_OVER_ALL_BOX_SURFACE_NODES`.

The present leaf quantifies what any remaining carrier would have to do over the exceptional divisor.

## Exact local intersection accounting

On the smooth minimal resolution, let `E_i` be one of the 48 exceptional curves and let

`m_i = Ctilde . E_i`

be the retained V6 exceptional pairing. If the normalization of the strict transform has points
`P_{i,1},...,P_{i,b_i}` above `E_i`, then local intersection additivity gives

`m_i = sum_j ord_{P_{i,j}}(nu^* E_i)`,

and every summand is a positive integer.

For an FSM minimal `(4,4)` branch, post1648AI locks the local invariant orders `[1,1,1]`, hence the branch contributes exceptional intersection exactly `1`.

Let `t_i` be the number of minimal `(4,4)` branches above node `i`. Therefore:

- `0 <= t_i <= m_i`;
- if `m_i=1`, the node cannot be multibranch and contributes at most one minimal branch;
- if `m_i>1` and the node is unibranch, its unique branch is nonminimal, hence `t_i=0`;
- a multibranch node can contribute at most `m_i` minimal branches.

These are local intersection-counting statements on the resolution, not existence assertions for a carrier.

## FSM pole capacity

For V6, `g=1`, `d=186`. The FSM tensor has

`#zeros >= 2kd = 372k`

and, by post1648AI, only minimal `(4,4)` branches can contribute positive pole order, each by at most `8k`.

Hence if `T=sum_i t_i`, divisor degree zero forces

`372k <= #poles <= 8k T`,

so

`T >= 47`.

The exact V6 exceptional vector is

`[1,1,1,2,2,0,1,2,8,4,7,2,9,5,1,10,5,11,7,1,3,1,13,1,6,2,12,16,4,3,5,6,5,10,8,1,10,15,11,2,5,11,4,10,2,4,3,13]`.

It has exactly nine unit entries, at labels

`[1,2,3,7,15,20,22,24,36]`.

The two largest nonunit masses are `16` and `15`.

If at most two surface nodes were multibranch, the maximum possible number of minimal branches would be

`9 + 16 + 15 = 40 < 47`.

Therefore any remaining V6 genus-one carrier must be multibranch over at least **three distinct** met box-surface nodes.

## Stronger normalization-fiber lower bound

For fixed mass `m_i>0` and chosen minimal-branch count `t_i`, the smallest possible total number `b_i` of normalization points above that node is bounded below by

- `b_i >= 1` if `t_i=0`;
- `b_i >= t_i+1` if `0<t_i<m_i`, because the residual positive intersection mass needs another nonminimal branch;
- `b_i >= m_i` if `t_i=m_i`, since all `m_i` units of intersection are already assigned to minimal branches.

For the unique zero-mass exceptional curve, `b_i=0`.

Exact integer dynamic programming over the retained 48-vector, subject to `sum_i t_i >= 47`, gives

`sum_i b_i >= 72`.

Since the retained support consists of 47 met nodes, the normalization-fiber excess over one point per met node is therefore at least

`72 - 47 = 25`.

This is a lower bound only. It neither constructs these branches nor classifies their analytic types.

## Exact conclusion and firewalls

Any integral geometric-genus-1 V6 carrier, if it exists, must satisfy both:

1. at least three distinct met box-surface nodes are multibranch;
2. the total number of normalization preimages over the 47 met nodes is at least 72 (branch excess at least 25).

Smooth-ambient-locus singularities may coexist and are not excluded. No integral carrier is materialized. Q602/O210 remain open and no downstream Stage32 credit is promoted.
