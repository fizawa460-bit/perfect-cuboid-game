# Stage15-6bo — hybrid exponent ledger and exact next theorem gate

Base: Stage15-6bn.

This stage quantifies what a legal global `q^{-2}` charge would buy when combined with the already-proved low-core quartic count.

Stage15-6ap gives, for fixed norm core `k` (hence `k=q` or `2q`),

\[
N_k(B)\ll B^{5/8+o(1)}k^{-1/2}.
\]

Summing the low-core range `q<=Q` costs

\[
N_{low}(B;Q)\ll B^{5/8+o(1)}Q^{1/2}.
\]

If 6bl--6bm can be upgraded to the aggregate high-core estimate dictated by the joint local density,

\[
N_{high}(B;Q)\ll B^{1+o(1)}\sum_{q>Q}q^{-2}
\ll B^{1+o(1)}Q^{-1},
\]

then balancing the two terms gives

\[
Q=B^{1/4},\qquad N_2(B)\ll B^{3/4+o(1)}.
\]

Thus the first honest payoff of the new global charge is a self-contained causal `3/4` exponent, not the final half-power. This is still a genuine Stage15-only thinning theorem if the uniform high-core estimate is proved.

The exact next theorem interface is therefore narrower than the old half-power target:

```text
UniformTwoCoordinateToricCongruenceCount
for actual squarefree S/O core q,
q >= B^(1/4-o(1)),
with aggregate high-core mass <= B^(3/4+o(1)).
```

No claim is made that Huang's current error term already supplies this interface; 6bn explicitly blocked that promotion pending extraction.

```text
STAGE15_6_SUBSTAGE=6bo
STAGE15_6BO_AUDIT_VERDICT=NEW_GATE
STAGE15_6BO_LOW_q_BOUND=B^(5/8+o(1))*Q^(1/2)
STAGE15_6BO_REQUIRED_HIGH_q_BOUND=B^(1+o(1))/Q
STAGE15_6BO_BALANCE_Q=B^(1/4)
STAGE15_6BO_CONDITIONAL_CAUSAL_EXPONENT=3/4
STAGE15_6BO_UNCONDITIONAL_CAUSAL_3_4_PROVED=false
STAGE15_6BO_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6BO_EXIT=UNIFORM_TORIC_CONGRUENCE_WINDOW_FOR_CAUSAL_THREE_QUARTERS
```