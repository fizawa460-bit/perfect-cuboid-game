# Stage32EX6 post-1697 — FSM16 modular-tensor multibranch wall

Status: **EXPLORATORY EXACT BOUNDED WALL — ADAPTER GAP CORRECTED; NO ENDPOINT CLOSURE CREDIT**.

## Question

Can the modular-tensor degree bound of Freitag–Salvati Manni exclude the hypothetical fixed-V6 genus-one carrier at the endpoint `O=266`?

## External source lock

Freitag–Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1; arXiv:1303.6495.

Their Theorem 3.1 states that if an integral curve `C` on the box variety has bijective normalization map `Cbar -> C`, geometric genus `g`, and projective degree `d`, then

`d <= 176 + 16g`.

The proof constructs, for positive integer `k`, a pulled-back symmetric tensor with

`16(2g-2)k = #zeros - #poles`.

The proof gives `#zeros >= 2kd`. At a cusp branch the modular parameters satisfy `a1,a2>0`, `a1==a2==0 mod 4`, `a1+a2==0 mod 8`; the local tensor pole order is at most `16k-(a1+a2)k`, hence at most `8k`, with positive pole budget only for `(a1,a2)=(4,4)`. Under bijective normalization the 48 nodes therefore give `#poles<=384k` and the published bound.

## Existing endpoint and first near-misses

At `O=266` the retained V6 target has

- geometric genus `g=1`;
- projective degree `d=186`;
- `B=266` normalization contacts over the exceptional divisor;
- all exceptional multiplicities equal to one;
- positive node support 47, with multibranch behavior.

The published theorem gives `d<=192`, so `d=186` survives by 6. Replacing the universal 48-node count by the exact 47-node support in a counterfactual bijective case gives `d<=188`, still surviving by 2.

Without bijectivity, the safe branchwise pole count gives

`d <= 16g-16+4B`,

hence only `d<=1064` at `g=1,B=266`.

## Correction: the Stage32/FSM16 branch adapter was already retained

The previous version of this EX6 note incorrectly said that no branch-level adapter from the FSM16 cusp parameters to the Stage32 AN local pair was source-locked. That was false.

The retained Stage32 source already contains the exact adapter:

- `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, blob `512fcc70afb1acf16956fd4b7a2b9b935a052150`;
- `stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches-source-note.md`, blob `da9b6ba755b8bd43d5b342d5540053caeb218f57`.

Those files source-lock

`a1=4*A`, `a2=4*B`,

with `A,B>0`, `A+B` even, and exceptional multiplicity

`m=min(A,B)`.

They also identify the unique FSM-minimal Stage32 branch as `(A,B)=(1,1)`. Consequently

`FSM16 cusp (a1,a2)=(4,4)  <=>  Stage32 FSM-minimal (A,B)=(1,1)`.

So the adapter gap is closed.

## O266 specialization

At `O=266`, every exceptional contact has `m=1`, so every branch has `min(A,B)=1`. Because `A+B` is even, a nonminimal endpoint branch is necessarily of the form

`(A,B)=(1,2r+1)` or `(2r+1,1)`, `r>=1`.

The endpoint also has `t=e-N=0`. The retained two-factor slack identities therefore become

`52 = q81_node + eta81 + rho81`,

`28 = q105_node + eta105 + rho105`,

with all terms nonnegative.

Every nonminimal endpoint branch contributes at least one unit to exactly one of `q81_node` or `q105_node`. Hence

`#nonminimal <= q81_node+q105_node <= 80`,

and among the 266 endpoint branches

`#FSM-minimal >= 266-80 = 186`.

Under the recovered adapter this is exactly

`S_cusp := #{branches with FSM16 pair (4,4)} >= 186`.

## Tensor threshold and dominance

The FSM16 tensor pole-count argument alone requires, for `g=1,d=186`,

`8*S_cusp >= 2d = 372`,

so only

`S_cusp >= 47`.

Thus the exact Stage32 two-factor geometry already forces a much stronger lower bound:

`186 >= 47`,

with margin `139`.

Equivalently:

- the tensor-cardinality route would need a new theorem `S_cusp<=46` to contradict the tensor inequality;
- but the retained AR geometry would already be contradicted by the far weaker upper bound `S_cusp<=185`.

Therefore any future attack whose only new output is an upper bound on the number of `(4,4)` cusp branches is **strictly dominated by the existing AR minimal-branch bound**. The FSM16 tensor adds no exclusion power to that cardinality architecture after the adapter is restored.

This does not say that the FSM16 tensor is globally useless. A genuinely different use could still control exact pole orders, cancellations/zeros, or a modified tensor rather than only counting maximal-pole branches.

## Decision

`FSM16_STAGE32_BRANCH_ADAPTER = SOURCE_LOCKED`.

`FSM16_S_CUSP_CARDINALITY_ROUTE = DOMINATED_BY_AR_MINIMAL_BRANCH_BOUND`.

`O266_ENDPOINT_EXCLUDED = false`.

## Re-entry boundary

Do not spend another EX6 batch merely trying to prove the old `S_cusp<=46` threshold through cusp counting. A useful re-entry now needs one of:

1. a genuinely global/member-level theorem forcing `S_cusp<=185` (which would already contradict AR directly);
2. exact tensor-divisor information stronger than the branch-count upper bound, e.g. forced extra zeros or reduced actual pole orders/cancellation;
3. a replacement tensor with a stronger local pole deficit;
4. a global landing/jet or simultaneous-fibration/correspondence inequality independent of this cusp-count architecture.

No O264 descent or endpoint closure follows from this wall.
