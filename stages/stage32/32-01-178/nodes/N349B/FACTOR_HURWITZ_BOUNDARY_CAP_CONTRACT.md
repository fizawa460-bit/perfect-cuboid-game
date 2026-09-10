# Stage32 32-01-178 N349B — factor-Hurwitz boundary cap

Status: `CONDITIONAL_ON_N349_HOSTILE_AUDIT`.

This is a preparatory necessary-condition reduction for the current 21 N342/N347 numerical Picard terminal families. It does not consume or promote N349 before a fresh external hostile-audit PASS.

## Locked local branch input

N349 records the following conditional boundary-equality consequence for an integral irreducible target curve with bijective normalization of genus `g=0` or `g=1`:

```text
all 48 box nodes occur,
and every local FSM translation pair is (a1,a2)=(4,4).
```

The retained local exponent convention is `a1=4*A`, `a2=4*B`. Hence every node branch has `(A,B)=(1,1)`, exceptional contact `a=min(A,B)=1`, and zero boundary contact in both factor directions. N342/N260 independently fix the exceptional pairing vector to `[1]^48`. Therefore there is exactly one normalization branch over each of the 48 met nodes, so

```text
e = 48,
B = 48,
e-B = 0.
```

## Six special fibres

The source-locked factor fibrations have six special fibres in each direction. For a boundary elliptic `E`, the resolved fibre class is

```text
F_E = 2E + sum(8 incident exceptional curves).
```

Within either factor direction the six exceptional-component sets partition all 48 exceptional curves. For a target class with all exceptional pairings equal to one, if

```text
b = C.E,
n = C.F_E,
```

then every special fibre in that direction gives

```text
n = 2b + 8.
```

Because the six divisors are fibres of the same morphism, the six values of `b` in one direction are equal. Thus, with `q` the total boundary intersection over the six multiplicity-two boundary elliptics,

```text
q = 6b = 3n - 24,
6n = 2q + 48.
```

## Riemann--Hurwitz cap

The previously source-locked special-fibre Hurwitz estimate is

```text
R >= e-B+q.
```

Here `e-B=0`, so `R>=q`. The factor base is `P1`; the normalization has genus `g`; and `n>=8`, so the restricted factor map is nonconstant and finite. Riemann--Hurwitz gives

```text
R = 2g - 2 + 2n.
```

Combining this with `q=3n-24` gives

```text
2g - 2 + 2n >= 3n - 24,
n <= 22 + 2g.
```

Equivalently, because `n=2b+8`, every one of the 12 boundary elliptic pairings must satisfy

```text
g=0: 0 <= C.E <= 7,
g=1: 0 <= C.E <= 8.
```

This is a necessary condition only. It is intentionally stronger than merely asking the exceptional landing to avoid the two fixed points: it also uses the two factor fibrations and Riemann--Hurwitz.

## Exact computational test

For each of the current 21 `(row_id,x4)` terminals, N349B will solve an exact integer linear feasibility problem in the retained Picard64 coordinates using only necessary conditions:

- current normal-total equality;
- all 48 exceptional pairings exactly `1`;
- current `x4` equality;
- all 92 known normal-curve pairings nonnegative;
- the 12 boundary pairings bounded by `7` for `g=0` or `8` for `g=1`.

The nonlinear self-square condition is deliberately omitted. Therefore an `UNSAT` result is a zero-loss obstruction for the stated Picard terminal family, conditional on the N349 boundary-equality input; `SAT` remains only a relaxed numerical Picard witness; `UNKNOWN` receives zero pruning credit.

## Firewalls

```text
N349_HOSTILE_AUDIT_CONSUMED=false
N349B_PROMOTION_ALLOWED=false
N349B_RESULT_IS_CONDITIONAL_ON_N349=true
SELF_SQUARE_USED=false
ACTUAL_INTEGRAL_IRREDUCIBLE_MEMBER_CONSTRUCTED=false
PRODUCTION_LEAF_CREDIT=false
N350_PRODUCER_REGISTRY_CHANGED=false
FULL178_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
MERGE_AUTHORIZED=false
```
