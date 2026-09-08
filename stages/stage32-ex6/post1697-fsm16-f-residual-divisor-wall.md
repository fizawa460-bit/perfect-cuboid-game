# Stage32-EX6 post1697 — FSM16 f-divisor residual nonnode wall

Status: **EXPLORATORY EXACT RE-ENTRY THRESHOLD — NO O266 EXCLUSION**.

## Question

The previous retained FSM16 weighted-node calculation gives, at the hypothetical `O=266` endpoint,

`D_node=-(1488+8E)k`,

where

`E=eta81+rho81+eta105+rho105>=0`,

and hence, on the genus-one normalization,

`D_nonnode=(1488+8E)k`.

Can the published Freitag–Salvati Manni proof explain part of this nonnode compensation by a divisor whose degree is independent of the Stage32 two-factor Riemann–Hurwitz slack ledger?

## Published FSM16 input

Use Freitag–Salvati Manni, *Parametrization of the box variety by theta functions*, Theorem 3.1 proof, arXiv:1303.6495.

Their tensor is

`T = Delta(z)^k Delta(w)^k f(z,w) (dz dw)^(8k)`.

The proof states that:

1. `T` is holomorphic away from the 48 exceptional curves;
2. for sufficiently large `k`, `f` can be chosen nonzero along the curve and nonzero at all 48 nodes;
3. the zero divisor of `f` is a `2k`-multiple of the canonical divisor;
4. the degree `d` of the curve is its intersection with the canonical divisor.

Therefore, counted with intersection multiplicity, the pullback of the `f`-zero divisor to the normalization has exact degree

`deg(div(f)|_N)=2kd`.

The theorem phrases this as a lower bound of `2kd` tensor zeros because other factors of `T` may contribute additional zeros. The exact statement used here is only the degree of the `f`-divisor contribution.

Because `f` is chosen nonzero at all nodes, this entire `f`-divisor contribution is nonnode.

## Apply the fixed V6 degree

The retained EX6 carrier degree is

`d=186`.

Hence

`deg(div(f)|_N)=2*k*186=372k`.

This `372k` comes from the canonical divisor class in the published FSM16 proof; it is not obtained by replaying the Stage32 `q/eta/rho` factor-Riemann–Hurwitz ledger.

## Residual signed nonnode degree

Divisor addition is linear. Subtract the exact `f`-divisor contribution from the retained total nonnode signed divisor:

`D_res_nonnode := D_nonnode - deg(div(f)|_N)`.

Then

`D_res_nonnode = (1488+8E)k - 372k`

and therefore

`D_res_nonnode = (1116+8E)k >= 1116k`.

Equivalently, even after the entire canonical `f`-zero divisor is credited to the required nonnode compensation, the remaining factors in the FSM16 tensor must carry signed nonnode divisor degree at least `1116k`.

This is a strict sharpening of the previous re-entry target: a future closure cannot merely point to the `f` zeros counted in the published theorem. Those account for only `372k` of the required `(1488+8E)k` compensation.

## What is and is not proved

The residual divisor is a **signed divisor difference**. This note does **not** claim that the quotient obtained by formally removing `f` is an effective divisor, a globally descended tensor on the box surface, or holomorphic pointwise on the normalization.

No upper bound on `D_res_nonnode` is proved here.

The Stage32 two-factor slack data remain used only to determine the node pole debt. They are not reused as an allegedly independent upper bound on the residual nonnode divisor.

No global V6 carrier is constructed.

No `O=266` exclusion follows.

## Re-entry threshold

Within this weighted-tensor architecture, a genuinely new closure input may take one of the following forms:

- an independent member-level upper bound
  `D_res_nonnode < (1116+8E)k`;
- a uniform independent upper bound `D_res_nonnode <=1115k`, which would close for every `E>=0`;
- an independent support/landing theorem incompatible with carrying residual signed degree `(1116+8E)k`;
- a replacement tensor or correspondence whose divisor budget is strictly stronger.

A computation derived only by algebraically replaying the same `q81/eta81/rho81` and `q105/eta105/rho105` identities is not an independent cap.

## Decision

`FSM16_F_DIVISOR_CONTRIBUTION_PER_K = 372`

`FSM16_RESIDUAL_NONNODE_SIGNED_DEGREE = (1116+8E)k`

`FSM16_RESIDUAL_NONNODE_MINIMUM_PER_K = 1116`

`FSM16_F_ZEROS_ALONE_CLOSE_ENDPOINT = false`

`O266_ENDPOINT_EXCLUDED = false`

No O264 descent, endpoint credit, Perfect Cuboid credit, hostile-audit credit, or merge is implied.
