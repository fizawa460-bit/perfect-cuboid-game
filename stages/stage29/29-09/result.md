# Stage29-09 — full endpoint local arithmetic

```text
STAGE=Stage29
ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
STATUS=SUBMISSION_PENDING_AUDIT
ROLE=PRE_ATTACK_LOCAL_INFRASTRUCTURE
ATTACK_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Exact odd-prime seven-form local law

On the full endpoint sign-cover base

\[
L=(x,y,z,x+y,x+z,y+z,x+y+z),
\]

a rational lift requires all seven values to lie in one common squareclass. For odd `p`, stratify `P^2(F_p)` by the number `k` of vanishing branch lines and let `A_k(p)` count reduction points whose nonzero branch values have one common quadratic character.

With

\[
\epsilon=\chi_p(-1),\qquad \eta=\chi_p(2),
\]

and `a_E(p)` the trace of `E:y^2=x^3-x`, exact branch character sums give

\[
A_1=
\frac34(p-4-\epsilon)
+\frac{1+\epsilon}{8}(p-5)
+\frac{3(1+\epsilon)}{16}(p-11-4\eta-a_E(p)),
\]

\[
A_2=\frac34(1+\epsilon)(1+\eta),
\qquad
A_3=\frac32(3+\epsilon).
\]

Using the audited Stage29-02e endpoint Frobenius package and the exact fiber identity

\[
\#\bar S(F_p)=64A_0+32A_1+16A_2+8A_3,
\]

one obtains

\[
\boxed{
\begin{aligned}
64A_0(p)= {}&p^2+p(-24-8\epsilon+3\eta+\epsilon\eta)\\
&+(135+86\epsilon+12\eta+12\epsilon\eta)\\
&+3a_p(h_{16})+a_p(h_{32})+3a_p(h_8)\\
&+6(1+\epsilon)a_E(p).
\end{aligned}}
\]

Hence on the nonbranch finite-field host

\[
\frac{A_0(p)}{(p-3)^2}=\frac1{64}+O(1/p).
\]

This is exact local geometry, not a heuristic independence factor.

```text
R29-KUM-LOC1-ODD=DISCHARGED_CANDIDATE_EXACT
R29-KUM-LOC1=PARTIAL_DISCHARGE_ODD_PRIMES_EXACT_BAD_PRIME_2_SEPARATE
```

## 2. Exact odd-prime branch valuation ledger

Conditional on an eligible reduction cylinder, the continuation probabilities for `Q_p` squareclass lifting are

\[
\boxed{q_0=1},
\qquad
\boxed{q_1=\frac1{2(p+1)}},
\qquad
\boxed{q_2=\frac1{4(p+1)^2}}.
\]

At a triple point the local branches are `r,s,r+s`, so the third condition is correlated. Exact p-adic summation gives

\[
\boxed{
q_3(p)=
\frac{p^2-(3+\chi_p(-1))p+1}
{8(p+1)^2(p^2+1)}.
}
\]

In particular `q3 != q1^3`; this is genuinely joint endpoint information rather than a replay of one marginal blocker.

Every `F_p` projective cylinder has normalized Haar mass `1/(p^2+p+1)`, so the exact full odd-prime local density is

\[
\boxed{
\Delta_p=
\frac{A_0+A_1q_1+A_2q_2+A_3q_3}{p^2+p+1}.
}
\]

Thus

\[
\Delta_p=\frac1{64}+O(1/p).
\]

```text
R29-KUM-LOC2-ODD=DISCHARGED_CANDIDATE_EXACT
JOINT_TRIPLE_BRANCH_CORRELATION_EXACT=true
INDEPENDENT_BRANCH_PRODUCT_ASSUMED=false
```

## 3. Real and 2-adic places

On the physical real chamber `x,y,z>0`, all seven branch forms are positive, so there is no real squareclass obstruction.

The prime `2` is genuinely exceptional: the seven-line arrangement degenerates modulo 2 and odd-prime Legendre-symbol formulas do not transfer. There is no blanket `Q_2` obstruction: for the Euler brick `(44,117,240)`, all face sums are squares and

\[
44^2+117^2+240^2=73225\equiv1\pmod8,
\]

so the space sum is a square in `Q_2`. Exact normalized `Q_2` density remains a bounded state-automaton receiver.

```text
R29-KUM-LOC2-INFINITY=DISCHARGED
R29-KUM-LOC2-2=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
R29-KUM-LOC2=PARTIAL_DISCHARGE_ODD_PRIMES_AND_INFINITY_DONE_P2_OPEN
```

## 4. Comparison with Stage19/20 blocker laws

Stage19's matched two-face host has the split-prime space-diagonal deficiency

\[
1-\rho_p=4/p+O(p^{-2}),
\]

while Stage20's matched two-face toric host has third-face blocker mass

\[
2/p+O(p^{-2}).
\]

The present leading `1/64` law lives instead on the full `P^2` seven-line base. These are different hosts/measures and are not independent probabilities. No Stage19 or Stage20 saving is re-credited or multiplied into the endpoint law.

A global use of the seven-form local conditions requires a new adapter from rational points on the `P^2` base to primitive canonical physical cuboids with `R<=B`, including height distortion, multiplicity and uniform equidistribution/large-sieve control.

```text
R29-KUM-LOC3=AMBER_PHYSICAL_HEIGHT_MEASURE_GLOBAL_ADAPTER
STAGE19_LOCAL_SAVING_RECREDITED=false
STAGE20_LOCAL_SAVING_RECREDITED=false
LOCAL_EULER_PRODUCT_GLOBAL_BOUND_CLAIM=false
```

## 5. Exact computation checkpoint

`local_density_check.py` enumerates `P^2(F_p)` exactly, computes `A_0..A_3`, computes `a_E(p)` directly, verifies the closed branch formulas, reconstructs `#Sbar(F_p)` from exact fiber sizes, and evaluates the rational `Delta_p`. The default regression covers every odd prime below 100; a compact table through 47 is committed in `local-check-output.md`.

```text
EXACT_REGRESSION=PASS_INTERNAL
FLOATING_ARITHMETIC_USED=false
FINITE_REGRESSION_IS_NOT_GLOBAL_THEOREM=true
```

## 6. Routing and stop rule

This item remains infrastructure. It does not create a twelfth attack route. The new joint data are handed to the existing `J12-LOCAL-SQUARECLASS` owner, while the two open adapters are explicit rather than silently assumed.

```text
ATTACK_ROUTE_COUNT_RETAINED=11
ROUTE_COUNT_CHANGE=0
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
R29-KUM-LOC2-2=OPEN_BOUNDED
R29-KUM-LOC3=AMBER_GLOBAL_ADAPTER_REQUIRED
AUDIT_REQUIRED=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=GAP_SCAN_B_ROADMAP_REVIEW_B
NEXT_EXPECTED_COMMAND_AFTER_MERGE=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
