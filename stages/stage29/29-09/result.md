# Stage29-09 — full endpoint local arithmetic

```text
STAGE=Stage29
ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
STATUS=AUDITED_PASS_AFTER_BOUNDED_REPAIR
ROLE=PRE_ATTACK_LOCAL_INFRASTRUCTURE
ATTACK_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

Fresh adversarial audit is recorded in `stages/stage29/29-09/audit.md`. The submitted mathematics survives; the bounded repair is controller-state synchronization via `controller-audit-state.json` after merged #1314.

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

and `a_E(p)` the trace of `E:y^2=x^3-x`, the audited exact branch counts are

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

No extra intersection appears at `p=3`; only `p=2` is exceptional.

Using the audited Stage29-02e endpoint Frobenius package and the exact fiber identity

\[
\#\bar S(F_p)=64A_0+32A_1+16A_2+8A_3,
\]

one obtains identically

\[
\boxed{
\begin{aligned}
64A_0(p)= {}&p^2+p(-24-8\epsilon+3\eta+\epsilon\eta)\\
&+(135+86\epsilon+12\eta+12\epsilon\eta)\\
&+3a_p(h_{16})+a_p(h_{32})+3a_p(h_8)\\
&+6(1+\epsilon)a_E(p).
\end{aligned}}
\]

Hence

\[
\frac{A_0(p)}{(p-3)^2}=\frac1{64}+O(1/p).
\]

```text
R29-KUM-LOC1-ODD=DISCHARGED_EXACT
R29-KUM-LOC1=PARTIAL_DISCHARGE_ODD_PRIMES_EXACT_BAD_PRIME_2_SEPARATE
ODD_PRIME_BRANCH_INCIDENCE_AUDIT=PASS
```

## 2. Exact odd-prime branch valuation ledger

Conditional on an eligible reduction cylinder,

\[
q_0=1,
\qquad
q_1=\frac1{2(p+1)},
\qquad
q_2=\frac1{4(p+1)^2}.
\]

At every triple point the vanishing branches are literally `r,s,r+s`; the third condition is correlated. Exact p-adic summation gives

\[
\boxed{
q_3(p)=
\frac{p^2-(3+\chi_p(-1))p+1}
{8(p+1)^2(p^2+1)}.
}
\]

Thus `q3 != q1^3` is certified genuinely joint endpoint information.

Every `F_p` projective cylinder has normalized mass `1/(p^2+p+1)`, so the exact odd-prime local density is

\[
\boxed{
\Delta_p=
\frac{A_0+A_1q_1+A_2q_2+A_3q_3}{p^2+p+1}.
}
\]

and `Delta_p=1/64+O(1/p)`.

```text
R29-KUM-LOC2-ODD=DISCHARGED_EXACT
JOINT_TRIPLE_BRANCH_CORRELATION_EXACT=true
INDEPENDENT_BRANCH_PRODUCT_ASSUMED=false
```

## 3. Real and 2-adic places

On the physical chamber `x,y,z>0`, all seven forms are positive, so there is no real squareclass obstruction.

The prime `2` remains separate. The Euler brick `(44,117,240)` proves only local nonemptiness: its three face sums are squares and

\[
44^2+117^2+240^2=73225\equiv1\pmod8,
\]

so the space sum is a square in `Q_2`. This is not a rational perfect cuboid and supplies no exact `Q_2` density.

```text
R29-KUM-LOC2-INFINITY=DISCHARGED_NO_POSITIVE_CHAMBER_OBSTRUCTION
R29-KUM-LOC2-2=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
R29-KUM-LOC2=PARTIAL_DISCHARGE_ODD_PRIMES_AND_INFINITY_DONE_P2_OPEN
```

## 4. Stage19/20 double-charge firewall

Stage19 and Stage20 local laws live on already-selected two-face hosts. The present law lives on the full seven-line `P^2(Q_p)` base. They are different measures and are not multiplied or re-credited.

A global use still requires control of physical height, primitivity, canonical ordering, multiplicity, and uniform equidistribution/large-sieve transfer.

```text
DOUBLE_CHARGE_FIREWALL=PASS
R29-KUM-LOC3=AMBER_PHYSICAL_HEIGHT_MEASURE_GLOBAL_ADAPTER
STAGE19_LOCAL_SAVING_RECREDITED=false
STAGE20_LOCAL_SAVING_RECREDITED=false
LOCAL_EULER_PRODUCT_GLOBAL_BOUND_CLAIM=false
```

## 5. Exact computation checkpoint

`local_density_check.py` exactly enumerates `P^2(F_p)` and verifies the branch formulas below 100. Fresh audit independently repeated the branch enumeration through every odd prime below 200 and independently re-derived the `q3` recurrence and the Stage29-02e Frobenius substitution.

```text
EXACT_REGRESSION=PASS_AUDITED
FLOATING_ARITHMETIC_USED=false
FINITE_REGRESSION_IS_NOT_GLOBAL_THEOREM=true
```

## 6. Controller / CI bounded repair

PR #1314 is merged at `b89bb92bf6bdb57b84262d39ed7005ea13d9403c`. Because 29-08 used an authoritative controller overlay, the aggregate `controller.json` still shows the older 29-07 snapshot. `controller-audit-state.json` now explicitly synchronizes merged 29-08 and audited 29-09 without rewriting historical metadata.

The red `Stage29-01 audit lock` remains a stale historical-state check: its verifier literally requires `controller["status"] == "29_01_AUDITED_PASS"` and the original `P_finite_zero_through_B == 500000000`. It is not a 29-09 content failure.

```text
CI_RED_CLASSIFICATION=STALE_STAGE29_01_LOCK_FALSE_POSITIVE
CI_CONTENT_BLOCKER=false
```

## 7. Final audit state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
CHECKPOINT29_09_AUDIT=PASS
BOUNDED_REPAIR=CONTROLLER_OVERLAY_SYNC_29_08_MERGED_PLUS_29_09_AUDIT_STATE
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ATTACK_ROUTE_COUNT_RETAINED=11
ROUTE_COUNT_CHANGE=0
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
R29-KUM-LOC2-2=OPEN_BOUNDED
R29-KUM-LOC3=AMBER_GLOBAL_ADAPTER_REQUIRED
NEXT_ITEM=GAP_SCAN_B_ROADMAP_REVIEW_B
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
