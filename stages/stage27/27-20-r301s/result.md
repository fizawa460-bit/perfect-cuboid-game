# Stage27-20-r301s — N2 exponent is the occupied q1-support exponent up to B^o(1)

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301r
SOURCE_STAGE=Stage20

## 1. Occupied first-coordinate support

Let

\[
Q(B)=\{x=q_1:\text{at least one physical Stage27 survivor with }R\le B\text{ has first coordinate }x\}.
\]

Every occupied `x` contributes at least one survivor, so after the fixed canonical-orientation convention

\[
\boxed{|Q(B)|\le N_2(B)}
\]

(up to a harmless absolute multiplicity if one works before canonical orientation).

Conversely, r301r proves the uniform aggregate bound

\[
W_x(B)=B^{o(1)}
\]

for the total number of survivors above one fixed `x`, after summing all compatible squareclasses.  Therefore

\[
N_2(B)
\le \sum_{x\in Q(B)}W_x(B)
\le |Q(B)|B^{o(1)}.
\]

Hence

\[
\boxed{
|Q(B)|\le N_2(B)\le |Q(B)|B^{o(1)}.
}
\]

This is the strongest structural consequence of the r301 squareclass/fiber lane so far: the unknown positive-power exponent is no longer hidden in the elliptic fibers.

## 2. Support corridor

The current Stage27 theorem surface gives

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Using the equivalence above gives

\[
\boxed{
B^{1/4-o(1)}\ll |Q(B)|\ll_\varepsilon B^{1/2+\varepsilon}.
}
\]

Thus the occupied first-coordinate support already has the same quarter-to-half exponent corridor as the population, up to subpolynomial factors.

## 3. Equivalent j-support formulation

R301m proved for

\[
J(B)=\{j(x):x\in Q(B)\}
\]

that

\[
|J(B)|\le |Q(B)|\le 2|J(B)|.
\]

Therefore

\[
\boxed{
N_2(B)=|J(B)|B^{o(1)}
}
\]

in the same exponent sense, and

\[
\boxed{
B^{1/4-o(1)}\ll |J(B)|\ll_\varepsilon B^{1/2+\varepsilon}.
}
\]

So `q1`-support and elliptic-moduli `j`-support are interchangeable at the fixed-power exponent level.

## 4. Exact new progress gate

If a future theorem proves

\[
|Q(B)|\ll B^{\sigma+o(1)},
\]

then r301r immediately gives

\[
\boxed{N_2(B)\ll B^{\sigma+o(1)}}.
\]

Therefore the upper half-wall is now equivalent to the support problem:

\[
\boxed{
\text{strict sub-square-root progress}
\iff
\text{prove an independent occupied-}q_1\text{ support exponent }\sigma<1/2
}
\]

within this receiver architecture.

Likewise any lower support exponent above `1/4` would automatically raise the population lower exponent, because `|Q(B)|<=N2(B)`.

This closes the need to search for further fixed-`x` fiber savings in the r301 lane: the fiber exponent has reached zero.  Any continuation should attack occupied support itself, not another reformulation of the same elliptic fibers.

## 5. Scope firewall

No independent support deficit is proved here.  In particular the existing bound `N2(B)<<B^(1/2+epsilon)` cannot be recycled as a new independent `Q(B)` theorem to claim a strict saving.

```text
STAGE27_20_R301S_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
N2_LE_Q1_SUPPORT_TIMES_SUBPOLYNOMIAL=true
Q1_SUPPORT_LE_N2=true
N2_Q1_SUPPORT_EXPONENT_EQUIVALENCE_PROVED=true
N2_J_SUPPORT_EXPONENT_EQUIVALENCE_PROVED=true
Q1_SUPPORT_LOWER=B^(1/4-o(1))
Q1_SUPPORT_UPPER=B^(1/2+epsilon)
FIXED_X_FIBER_ROUTE_SATURATED_AT_EXPONENT_ZERO=true
INDEPENDENT_Q1_SUPPORT_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301t
STOP_REASON=OCCUPIED_Q1_OR_J_SUPPORT_FIXED_POWER_DEFICIT_THEOREM_REQUIRED
```
