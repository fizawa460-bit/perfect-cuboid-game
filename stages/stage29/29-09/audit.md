# Stage29-09 — fresh adversarial audit

```text
PR=1315
SUBMISSION_HEAD=c63a9d976bb99b207bfc1dc96a25f131973c54df
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
BOUNDED_REPAIR=CONTROLLER_OVERLAY_SYNC_29_08_MERGED_PLUS_29_09_AUDIT_STATE
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## 1. Seven-line incidence and branch counts — PASS

The seven forms

```text
x, y, z, x+y, x+z, y+z, x+y+z
```

remain seven distinct lines in every odd characteristic. Their intersection pattern is exactly six triple points and three ordinary double points; no extra collision appears at `p=3`. The only characteristic where `-1=1` collapses the arrangement is `p=2`, which the submission correctly isolates.

Fresh line-by-line character counting gives

```text
A1 = 3/4*(p-4-eps)
   + (1+eps)/8*(p-5)
   + 3(1+eps)/16*(p-11-4*eta-aE),
A2 = 3/4*(1+eps)*(1+eta),
A3 = 3/2*(3+eps),
```

with `eps=chi(-1)`, `eta=chi(2)`, and `aE` the trace of `E:y^2=x^3-x`.

The three coordinate lines give the first term. The total-sum line contributes only when `-1` is a square. On each pair-sum line the remaining three simultaneous character conditions reduce to the standard cubic character sum for `x(x-1)(x+1)`, hence the displayed `E` trace. The three double points are eligible iff `p=1 mod 8`; the three non-coordinate triple points are eligible iff `p=1 mod 4`.

Independent exact enumeration was rerun through all 45 odd primes below 200 and matches every formula, including `p=3`.

```text
R29-KUM-LOC1-ODD=DISCHARGED_EXACT
ODD_PRIME_BRANCH_INCIDENCE_AUDIT=PASS
P3_EXTRA_INTERSECTION=false
```

## 2. Normal-cover fibers and A0 Frobenius substitution — PASS

At an eligible base point with `k` vanishing branch forms, projective sign choices give exactly

```text
k=0 -> 64
k=1 -> 32
k=2 -> 16
k=3 -> 8
```

rational points in the normal-cover fiber. This is the exact projective count; algebraic cover degree is not interpreted as physical multiplicity.

Therefore

```text
#Sbar(Fp)=64*A0+32*A1+16*A2+8*A3.
```

Substituting the audited Stage29-02e good-odd-prime Frobenius identity

```text
#Sbar(Fp)=1+p^2+3*a16+a32+3*a8
          +p*(10+2*eps+eps*eta+3*eta)
```

and the audited `A1,A2,A3` expressions simplifies identically to

```text
64*A0 = p^2 + p*(-24-8*eps+3*eta+eps*eta)
        +(135+86*eps+12*eta+12*eps*eta)
        +3*a16+a32+3*a8
        +6*(1+eps)*aE.
```

The algebraic difference is identically zero. Hence `A0=p^2/64+O(p)` and the leading `1/64` is an exact local geometric density on the seven-line `P2` host, not an independence heuristic.

## 3. p-adic continuation q1/q2/q3 — PASS

For a smooth branch cylinder `L=pT`, matching the unit squareclass requires `v_p(T)` odd and the leading unit character fixed. Normalized Haar summation gives

```text
q1=1/(2*(p+1)).
```

At each eligible ordinary double point the two branch parameters are transverse and the relevant unit multipliers are squares, so

```text
q2=q1^2=1/(4*(p+1)^2).
```

At every triple point the three vanishing forms are literally of the shape

```text
r, s, r+s
```

with no hidden nonsquare multiplier. If `nu` is the measure for `R,S,R+S` to have even valuations and one prescribed unit character, residue decomposition gives

```text
nu = Nc/p^2
    + ((p-1)(1+eps)/(4p^2))*q1
    + ((p-1)/p^2)*q1
    + p^(-4)*nu,
Nc=(p-1)(p-4-eps)/8,
q3=p^(-2)*nu.
```

Solving this recurrence yields exactly

```text
q3=(p^2-(3+eps)*p+1)/(8*(p+1)^2*(p^2+1)).
```

Thus `q3 != q1^3` is certified genuine joint branch correlation.

```text
R29-KUM-LOC2-ODD=DISCHARGED_EXACT
JOINT_TRIPLE_BRANCH_CORRELATION_EXACT=true
INDEPENDENT_BRANCH_PRODUCT_ASSUMED=false
```

## 4. Exact P2(Qp) density — PASS

Reduction fibers of `P2(Z_p) -> P2(F_p)` have equal normalized mass `1/(p^2+p+1)`. For odd `p`, a unit squareclass is completely determined by valuation parity and residue quadratic character. Therefore

```text
Delta_p=(A0+A1*q1+A2*q2+A3*q3)/(p^2+p+1)
```

is exactly the normalized `P2(Q_p)` density of base points lifting to the full seven-form sign cover.

This statement is local only. It does not produce an Euler product bound for primitive canonical cuboids.

## 5. Real place and p=2 firewall — PASS

On the physical chamber `x,y,z>0`, all seven forms are positive, so there is no real obstruction.

The odd-prime formulas are not transferred to `p=2`. The witness `(44,117,240)` is valid only for local nonemptiness: its three face sums are rational squares and

```text
44^2+117^2+240^2=73225 == 1 mod 8,
```

so the space sum is a square in `Q_2`. This does not make `73225` a rational square and does not construct a perfect cuboid over `Q`.

```text
R29-KUM-LOC2-INFINITY=DISCHARGED_NO_POSITIVE_CHAMBER_OBSTRUCTION
R29-KUM-LOC2-2=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
R29-KUM-LOC2=PARTIAL_DISCHARGE_ODD_PRIMES_AND_INFINITY_DONE_P2_OPEN
```

## 6. Stage19/20 double-charge firewall — PASS

The Stage19 and Stage20 local laws live on already-selected two-face hosts. The present `Delta_p` lives on the full seven-line `P2(Q_p)` base. These are different measures. The submission correctly forbids multiplication or re-crediting of the Stage19/20 savings.

A global arithmetic use still needs an adapter controlling rational/physical height, primitive normalization, canonical ordering, multiplicity, and sufficiently uniform equidistribution or large-sieve transfer.

```text
DOUBLE_CHARGE_FIREWALL=PASS
R29-KUM-LOC3=AMBER_PHYSICAL_HEIGHT_MEASURE_GLOBAL_ADAPTER
LOCAL_EULER_PRODUCT_GLOBAL_BOUND_CLAIM=false
```

## 7. Bounded controller repair

PR #1314 is already merged at `b89bb92bf6bdb57b84262d39ed7005ea13d9403c`, but the aggregate `stages/stage29/controller.json` still displays the older 29-07 pending-merge snapshot because 29-08 intentionally persisted an authoritative controller overlay rather than rewriting the aggregate file.

This audit does not rewrite historical audited metadata. It adds a new authoritative 29-09 controller audit state that explicitly records:

```text
29-08 = AUDITED_PASS_MERGED
29-09 = AUDITED_PASS_PENDING_MERGE
NEXT_ITEM = GAP_SCAN_B_ROADMAP_REVIEW_B
```

The aggregate controller should be folded from the authoritative overlays on the next controller-consolidation write; its stale top-level display is not treated as a mathematical blocker.

## 8. CI classification

The only current workflow is the historical `Stage29-01 audit lock`. Its verifier literally asserts

```text
controller["status"] == "29_01_AUDITED_PASS"
```

and the original `P_finite_zero_through_B == 500000000`, so it is structurally stale for every intentionally advanced Stage29 state. The red run is therefore not evidence against 29-09 content.

```text
CI_RED_CLASSIFICATION=STALE_STAGE29_01_LOCK_FALSE_POSITIVE
CI_CONTENT_BLOCKER=false
```

## 9. Final routing

29-09 remains pre-attack infrastructure. No twelfth route is created, no Stage16-28 backflow is triggered, and no existence/nonexistence conclusion follows.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
CHECKPOINT29_09_AUDIT=PASS
BOUNDED_REPAIR=CONTROLLER_OVERLAY_SYNC_29_08_MERGED_PLUS_29_09_AUDIT_STATE
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
R29_KUM_LOC1_STATUS=PARTIAL_DISCHARGE_ODD_PRIMES_EXACT_BAD_PRIME_2_SEPARATE
R29_KUM_LOC1_ODD=DISCHARGED_EXACT
R29_KUM_LOC2_STATUS=PARTIAL_DISCHARGE_ODD_PRIMES_AND_INFINITY_DONE_P2_OPEN
R29_KUM_LOC2_ODD=DISCHARGED_EXACT
R29_KUM_LOC2_2_STATUS=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
R29_KUM_LOC3_STATUS=AMBER_PHYSICAL_HEIGHT_MEASURE_GLOBAL_ADAPTER
DOUBLE_CHARGE_FIREWALL=PASS
ROUTE_COUNT_CHANGE=0
ATTACK_ROUTE_COUNT_RETAINED=11
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM=GAP_SCAN_B_ROADMAP_REVIEW_B
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
