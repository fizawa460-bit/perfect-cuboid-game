# StageA1 A1-11 — exact elliptic-adapter firewall and finite-wall freeze candidate

## Scope

A1-10 reduced the remaining finite affine `G0` problem to the exact simultaneous receivers

```text
Q(z)=delta*v^2,
z^2-4=delta*u^2,
```

with

```text
delta in {±1,±3,±13,±19,±39,±57,±247,±741},
```

and eliminated `delta=+19`. The ten newly unclassified squareclasses are

```text
±13, ±39, ±57, ±247, ±741.
```

A1-11 attempts the controller-authorized next step: attach certified Mordell-Weil rank/torsion data or a certified MW-sieve adapter to these exact twists. The purpose of this batch is to make the external-adapter boundary mathematically exact and to prevent a same-`j` false identification.

All statements remain specific to the corrected equation-(6) Hilbert-cube family.

## 1. Exact target elliptic curves

The quartic torsor

```text
T_delta: Q(z)=delta*v^2,
Q(z)=z^4-20z^2+256z-412
```

has Jacobian

```text
E_delta:
W^2=X^3+7668*delta^2*X+489456*delta^3.
```

For the short model `y^2=x^3+A_delta*x+B_delta`,

```text
c4(E_delta) = -368064*delta^2,
c6(E_delta) = -422889984*delta^3.
```

The ten target coefficient pairs are therefore:

```text
 delta   A_delta       B_delta
 +13      1295892       1075334832
 -13      1295892      -1075334832
 +39     11663028      29034040464
 -39     11663028     -29034040464
 +57     24913332      90643825008
 -57     24913332     -90643825008
+247    467817012    7375721612688
-247    467817012   -7375721612688
+741   4210353108  199144483542576
-741   4210353108 -199144483542576
```

These equations, rather than `j` alone, are the exact objects whose Mordell-Weil information is needed.

## 2. Exact Q-isomorphism adapter test

For Weierstrass curves over `Q` with this non-special `j` invariant (`j=357911/950`, hence `j != 0,1728`), a claimed Q-isomorphism from a candidate model `E'` to `E_delta` must have a rational scaling parameter `u` satisfying

```text
c4(E_delta)/c4(E') = u^4,
c6(E_delta)/c6(E') = u^6.
```

Translations in `x` and the usual `r,s,t` changes do not alter this invariant criterion. Therefore a same-`j` LMFDB row is **not** a valid rank adapter unless the two ratios are compatible powers of the same rational `u`.

This is the exact firewall used in A1-11.

## 3. Same-j false adapters found and rejected

The official LMFDB search page for

```text
j = 357911/950
```

contains many quadratic twists with the same `j` invariant:

- https://www.lmfdb.org/EllipticCurve/Q/?jinv=357911%2F950

Several rows look superficially relevant because their discriminants contain the same odd prime support as the A1-10 squareclasses. They are **not** the target curves.

### Example: `32110.x1` is not `E_13`

LMFDB model:

```text
y^2+x*y+y=x^3+x^2+250*x+2985.
```

Its invariants are

```text
c4=-11999,
c6=-2489201.
```

For the exact target `E_13`,

```text
c4(E_13)/c4 = 5184 = 2^6*3^4.
```

A rational fourth power has every prime valuation divisible by `4`; `v_2(5184)=6`, so this ratio is not a rational fourth power. Hence `32110.x1` is not Q-isomorphic to `E_13`.

### Example: `256880.cx1` is not `E_-13`

LMFDB model:

```text
y^2=x^3+x^2+4000*x-183052.
```

Here

```text
c4=-191984,
c6=159308864,
```

and

```text
c4(E_-13)/c4 = 324 = 2^2*3^4,
```

which is again not a rational fourth power. So this is not the exact `delta=-13` twist.

The same invariant check rejects the tempting same-`j` rows

```text
32490.s1   as E_+57,
259920.fm1 as E_-57,
288990.bg1 as E_-39.
```

In particular their published ranks must **not** be imported into StageA1 as ranks of the A1-10 target twists.

`verify.py` recomputes all five rejections exactly from the displayed Weierstrass coefficients.

## 4. Why this matters

A rank-zero same-`j` curve would be enough to tempt an invalid torsor elimination. A1-11 shows that this shortcut is not licensed: quadratic twists all have the same `j`, while the A1-10 receiver fixes a precise squareclass `delta` and therefore a precise Q-isomorphism class.

Accordingly:

```text
SAME_J_IS_NOT_AN_EXACT_TWIST_ADAPTER=true
NO_NEW_RANK_ZERO_ELIMINATION_CERTIFIED_IN_A1_11=true
```

This preserves the validity of the earlier `delta=+19` elimination, because A1-9 supplied and audited an explicit Q-isomorphism for that exact model. A1-11 does not disturb any A1-9 result.

## 5. Exact computational wall

The remaining task is now sharply specified:

1. locate the exact Q-isomorphism class of each displayed `E_delta` (`delta=±13,±39,±57,±247,±741`) by coefficient/model lookup or minimalization;
2. certify rank and torsion (or Selmer bounds) on that exact class;
3. for positive-rank cases, impose the second square-coordinate condition by elliptic Chabauty / Mordell-Weil sieve.

The current StageA1 execution environment does not provide SageMath, Magma, PARI/GP or `mwrank`, and the available LMFDB web index exposes same-`j` search rows but does not furnish a certified exact coefficient lookup for these ten target short models. Consequently the requested rank/MW-sieve step cannot be certified here without importing an unproved or potentially wrong model identification.

This is exactly the controller's stated stopping condition: a targeted global attempt has reached a concrete external computational-algebra wall, with no unresolved elementary local-prime or finite-height step left to repeat.

## 6. Proposed routing

A1-11 therefore proposes

```text
STAGE_A1_STATUS=FROZEN_EXACT_FINITE_ELLIPTIC_WALL
STOP_AFTER_AUDIT=true
```

This is a **freeze**, not a proof of family exclusion and not a perfect-cuboid result.

Reopen StageA1 only if one of the following becomes available:

- certified Sage/Magma/PARI/mwrank output for the exact `E_delta` models;
- an exact LMFDB/Cremona label plus explicit Q-isomorphism for one of the ten targets;
- a certified MW-sieve / elliptic-Chabauty computation satisfying the second square-coordinate condition;
- a new global theorem that closes one or more of the exact finite receivers;
- a proved universal reverse map or a valid adapter into another proved project receiver.

## 7. Firewalls

A1-11 does **not** prove:

- that any of the ten remaining target twists has rank 0 or positive rank;
- that `G0`, `G+`, `G-`, or the first-two-cover curve has no rational points;
- that equation (6) is universal;
- any necessary condition for an arbitrary perfect cuboid;
- existence or nonexistence of a perfect cuboid.

Stage27 and StructureRadar remain unchanged.

```text
A1_11_STATUS=SUBMITTED_FOR_AUDIT
A1_11_EXACT_TARGET_TWISTS=10
A1_11_SAME_J_ADAPTER_FIREWALL=true
A1_11_FALSE_ADAPTERS_REJECTED=5
A1_11_NEW_RANK_ZERO_ELIMINATION=false
PROPOSED_STAGE_A1_STATUS=FROZEN_EXACT_FINITE_ELLIPTIC_WALL
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
