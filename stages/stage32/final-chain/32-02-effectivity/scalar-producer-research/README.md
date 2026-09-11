# 32-02 scalar producer research

## Scope
Produce a fail-closed, source-locked record `{row_id,d,negative_hperp_square_N}` for a concrete 32-01 terminal/Picard witness, for consumption by the existing 32-02 RR gate.

## Non-goals
No FULL178 enumeration, CUT/EX5/MB computation, MAIN authority mutation, pruning credit, irreducibility/genus claim, or merge authorization.

## Success ladder
1. Replay a supplied integral Picard witness to exact `N=-y^2`.
2. Bind `d`, divisibility `m=16/gcd(d,16)`, and the RR inequality to that witness.
3. State precisely the missing producer fields needed for every final survivor.
