# Stage35-EX Goal4CC source lock — post-bridge-local fresh-route audit selects the canonical E1 cross-gcd pair

Scope: consume exact-green Goal4CB and execute the Cycle Exploration Safety Protocol after the source bridge-prime local-square route is complete. This audit runs a blind pass from the exact source norm receiver, then deduplicates against 35EX-02/04/08/09/12/13 and the Goal4BS parking ledger. The new live route is the pair of source-known canonical E1 cross gcds `p=gcd(W1,V2)` and `d=gcd(V1,W2)`, whose balanced valuation strata were not previously frozen as local-square sieves. Mathematical authority remains V74 / Goal4AK. No merge.

## 1. Exact parent

Goal4CB is exact-green at

```text
head = f10685d8404160cf945d80a327e489711b85e1a0
Goal4CB dedicated run = 34424246899 SUCCESS
```

Retain

```text
F_E1=(W1*U2)^2+(U1*V2)^2=(c*e)^2*B_e,
X=q*H/e,
Y=c*D*T/e,
B_e=X^2+Y^2,
gcd(X,Y)=1.
```

Goal4CA/CB completely determine whether `B_e` is a square in `Q_ell` for every odd `ell|e`.

## 2. Blind pass — what the completed bridge receiver still exposes

### CC-A — primes already supported on the two bridge legs

For every odd prime `ell|X*Y`, coprimality gives exactly one of `X,Y` divisible by `ell`. Hence

```text
v_ell(B_e)=0
```

and `B_e` is the square of the other leg modulo `ell`. Therefore every odd source prime carried directly by

```text
q*(H/e)*(c/e)*D*T
```

is automatically locally square. This includes all `T`-primes and all primes entering only through `D`, `q`, `H/e`, or `c/e`.

At `2`, `q` is divisible by at least `4` for primitive Euclid data while `Y` is odd, so

```text
B_e == 1 mod 8.
```

Thus the ordinary 2-adic square condition is also automatic at this receiver.

Classify:

```text
SOURCE_LEG_SUPPORT_LOCAL_SQUARE_REENTRY=DOMINATED_AUTOMATIC.
```

### CC-B — full factorization of B_e

Testing every prime divisor of `B_e` and requiring even valuation is exactly the original condition that `B_e` be an integer square, hence exactly E1 by Goal4CA. No receiver reduction occurs.

Classify:

```text
FULL_B_e_FACTORIZATION=ENDPOINT_EQUIVALENT.
```

### CC-C — primitive bridge parametrization / divisor descent

If `B_e` is a square, `(X,Y,sqrt(B_e))` is the primitive bridge Pythagorean triple already derived in 35EX-08, and its coprime double-square / factor-allocation system is the 35EX-08/09 route. 35EX-09 records that no admissible size-decreasing counterexample map is proved.

Classify:

```text
BRIDGE_PRIMITIVE_PARAMETRIZATION=HISTORICAL_EQUIVALENT_35EX_08_09.
```

### CC-D — fixed-S S-unit/Thue from the fresh norm primes

The squarefree support of `B_e` outside the known source legs varies with the Master-Hit. Recasting those primes as an S-unit/Thue support has the same uniformity defect frozen by 35EX-12: per-hit finite support is not one fixed finite `S` or a fixed finite coefficient family.

Classify:

```text
FRESH_NORM_PRIME_SUNIT_THUE=BLOCKED_DYNAMIC_SUPPORT.
```

### CC-E — another bridge Gaussian/quartic/higher character

Goal4CB already gives the complete `Q_ell` square condition at each `ell|e`. Any higher character at the same bridge prime, without an independent new source identity, cannot strengthen the yes/no question whether `B_e` is a square in `Q_ell`.

Classify:

```text
HIGHER_BRIDGE_LOCAL_CHARACTER=EQUIVALENT_OR_RECHARGE.
```

## 3. New blind candidate — the canonical E1 cross gcd p

The raw E1 norm has a second source-selected cancellation family already present in 35EX-02:

```text
p=gcd(W1,V2).
```

The canonical gcd theorem gives

```text
g0=c*p,
gcd(c,p)=1,
p odd.
```

Fix `ell|p` and put

```text
a_ell=v_ell(W1),
b_ell=v_ell(V2),
k=min(a_ell,b_ell)=v_ell(p).
```

Because `ell` divides neither `c` nor `e`, the local squareclass of `B_e` is the local squareclass of the raw norm `F_E1`.

If `a_ell!=b_ell`, the two summands of

```text
F_E1=(W1*U2)^2+(U1*V2)^2
```

have unequal valuations. The lower-valuation term survives with a square unit, giving

```text
v_ell(B_e)=2*k
```

and an automatically square residual unit.

Only the balanced source stratum

```text
v_ell(W1)=v_ell(V2)=v_ell(p)                         (CC-p-balanced)
```

can carry a nontrivial local square obstruction. This is structurally parallel to Goal4CA's `e`-balanced stratum but is a different source gcd.

A genuine Master-Hit already demonstrates nontriviality:

```text
(a,b,m,n)=(9,8,6,5),
p=5,
e=1,
B_e=3584425,
v_5(B_e)=2,
(B_e/5^2) mod5 = 2,
(2/5)=-1.                                           (CC-p-witness)
```

So the `p` family can kill after the entire `e`-bridge route is vacuous or passed.

## 4. Index-swap companion d is distinct on an ordered hit

35EX-13 introduced

```text
d=gcd(V1,W2)
```

and the exact alternate norm identity

```text
F_E1=(U1*W2)^2+(V1*U2)^2.                            (CC-alt)
```

Primitivity gives

```text
d odd,
gcd(c,d)=gcd(p,d)=gcd(q,d)=1.
```

Exactly the same valuation argument shows that an odd `ell|d` is automatically locally square unless

```text
v_ell(V1)=v_ell(W2)=v_ell(d).                        (CC-d-balanced)
```

The balanced `d` family is not redundant on one ordered Master-Hit even though it is the index-swap copy of the `p` construction. For example

```text
(a,b,m,n)=(17,10,97,88),
p=1,
d=17,
e=1,
B_e=133709815369,
v_17(B_e)=3.                                         (CC-d-witness)
```

Thus a joint source sieve should evaluate both canonical orientations rather than discard `d` merely because the whole Master-Hit population is swap-symmetric.

## 5. Historical dedup

- 35EX-02 defines `p` and proves the canonical gcd split, but does not freeze a source-only local-square test at balanced `p` primes.
- 35EX-04 allocates the forced `p` support inside the hypothetical counterexample product rectangle; it explicitly says the cross equation alone does not close E1. It does not evaluate `F_E1` locally at source `p` primes.
- 35EX-13 defines `d` and proves the alternate-norm/Gaussian ratio coupling. Its new receiver is the joint Gaussian source squareclass, not the balanced `d`-prime local-square criterion above.
- Goal4CA/CB cover only `ell|e`.

Therefore the joint `p/d` balanced-cancellation local test is a genuinely unspent source-fixed route in the current retained ledger.

## 6. Candidate ledger and selected next gate

```text
LIVE:
  CANONICAL_E1_CROSS_GCD_P_D_BALANCED_LOCAL_SQUARE

UNTESTED:
  none immediately cheaper than the selected local theorem

BLOCKED:
  BRIDGE_ADMISSIBLE_DESCENT_MAP
  FIXED_S_SUNIT_THUE_COMPLETION
  BQ_GLOBAL_RATIONAL_REALIZATION_HEIGHT_ADAPTER
  ELLIPTIC_HEIGHT_DISCRIMINANT_QUANTITATIVE_ADAPTER

EQUIVALENT_OR_DOMINATED:
  SOURCE_LEG_SUPPORT_LOCAL_SQUARE
  FULL_B_e_FACTORIZATION
  BRIDGE_PRIMITIVE_PARAMETRIZATION
  HIGHER_BRIDGE_LOCAL_CHARACTER
```

Select

```text
35EX-35_GOAL4CD_CANONICAL_E1_CROSS_GCD_P_D_LOCAL_SQUARE_PREFLIGHT
```

Goal4CD should prove the complete odd-prime local square criterion on `p` and `d`, isolate the two balanced strata, give branchwise/source witnesses, and test whether the joint `p/d/e` source-selected local family is universal. If a genuine Master-Hit passes all three families while `B_e` is nonsquare, freeze this local-gcd route and broaden again.

## 7. Cycle exit

```text
CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW
CYCLE_ACTIVE_RECEIVER=CANONICAL_E1_CROSS_GCD_P_D_BALANCED_LOCAL_SQUARE
CYCLE_LIVE_CANDIDATES=1
CYCLE_UNTESTED_CANDIDATES=0
CYCLE_EXHAUSTIVE_VIEW_AUDIT=true
CYCLE_BLIND_REDISCOVERY=true
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=false
CYCLE_NEW_VIEW=CANONICAL_E1_CROSS_GCD_P_D_BALANCED_LOCAL_SQUARE
CYCLE_NEW_VIEW_SOURCE=BLIND_PLUS_INTERNAL_DERIVATION
```

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
