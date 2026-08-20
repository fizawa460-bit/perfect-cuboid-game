# StageA1 A1-10 — exact finite squareclass descent for `G0`

## Scope

A1-8 produced

```text
G0: W0^2=(z^2-4)Q(z),
Q(z)=z^4-20z^2+256z-412.
```

A1-9 gave finite elliptic-twist descents for `G+` and `G-`. A1-10 performs the analogous descent for `G0`. This is a global squareclass reduction, not a larger finite-height search and not another scan of the saturated A1-6 local-prime mechanism.

All statements remain specific to the corrected equation-(6) Hilbert-cube family.

## 1. Primitive integral receiver

Write a finite rational point with

```text
z=a/b, gcd(a,b)=1, b>0,
H(a,b)=a^4-20a^2b^2+256ab^3-412b^4.
```

Since

```text
Q(a/b)=H(a,b)/b^4,
z^2-4=(a^2-4b^2)/b^2,
```

and `b^6` is a square, every rational point on `G0` gives

```text
c^2=(a^2-4b^2)H(a,b)
   =(a-2b)(a+2b)H(a,b).                         (A1.10.1)
```

The exact gcd controls inherited from A1-9 are

```text
gcd(a-2b,a+2b) | 4,
gcd(a-2b,H) | 36,
gcd(a+2b,H) | 988=4*13*19.                     (A1.10.2)
```

## 2. Odd support of the squareclass of `H`

Let `q` be an odd prime whose exponent in `H` is odd. Because the product in (A1.10.1) is a square, `q` must also occur to odd exponent in one of `a-2b` or `a+2b`. By (A1.10.2):

- if `q|(a-2b)`, then `q=3`;
- if `q|(a+2b)`, then `q in {13,19}`.

Therefore the odd part of the squareclass of `H` is supported on

```text
{3,13,19}.                                      (A1.10.3)
```

No other odd prime can occur in the squareclass.

## 3. The 2-part of `H` is always square

For primitive `(a,b)`:

- if `b` is even, then `a` is odd and `H` is odd;
- if `a,b` are both odd, then `H` is odd;
- if `a` is even and `b` is odd, direct reduction modulo `8` gives `v_2(H)=2`.

Hence

```text
v_2(H) is always even.                           (A1.10.4)
```

Since `b^4` is itself a square, `Q(z)` has the same squareclass as `H`. Combining (A1.10.3)-(A1.10.4), every finite rational point on `G0` determines

```text
D0={±1,±3,±13,±19,±39,±57,±247,±741}.          (A1.10.5)
```

## 4. Exact 16-branch decomposition

For a rational point on `G0`, choose the unique signed squarefree representative `delta` of the squareclass of `Q(z)`. Then

```text
Q(z)=delta*v^2.
```

Because `(z^2-4)Q(z)` is a square, `z^2-4` has the same squareclass, so also

```text
z^2-4=delta*u^2.                                (A1.10.6)
```

By the previous sections,

```text
delta in D0.
```

Conversely, any rational solution of

```text
Q(z)=delta*v^2,
z^2-4=delta*u^2,
delta in D0                                      (A1.10.7)
```

gives a rational point on `G0`, since the product is `delta^2(uv)^2`.

Thus `G0(Q)` is **exactly** the union of sixteen elliptic-twist/conic receivers. This is a strict finite global reduction.

## 5. Elliptic factors

For every `delta in D0`, the quartic twist

```text
T_delta: Q(z)=delta*v^2
```

has Jacobian

```text
E_delta: W^2=X^3+delta^2*7668X+delta^3*489456.  (A1.10.8)
```

The second equation `z^2-4=delta*u^2` is the extra conic/square-coordinate condition to be imposed on the rational points of the torsor/twist.

A1-9 already audited the following overlapping factors:

- `delta=±1,±3`: the associated elliptic Jacobians have rank `1` and trivial torsion;
- `delta=-19`: rank `1`, trivial torsion;
- `delta=+19`: the quartic torsor `Q(z)=19v^2` has **no rational point**.

Therefore the `delta=+19` branch of `G0` is immediately empty as well:

```text
G0_delta=+19 = EMPTY over Q.                    (A1.10.9)
```

After this inherited elimination, at most fifteen branches remain. Five of them (`±1,±3,-19`) already have audited rank-one Jacobians; ten new squareclasses (`±13,±39,±57,±247,±741`) still require certified rank/Selmer or Mordell-Weil-sieve work.

## 6. What changed

Before A1-10, `G0` was an untreated genus-2 factor of the A1-8 Jacobian decomposition. After A1-10 it is no longer an opaque genus-2 rational-point problem: it is an exact finite union of sixteen explicit elliptic-twist receivers, one of which is already eliminated.

This satisfies the controller's explicit permission to descend `G0` only if a strict finite receiver is obtained.

The next substantive attack is now sharply finite:

1. certify ranks/torsion/Selmer data for the ten new `G0` twists;
2. eliminate any rank-zero trivial-torsion torsors by the A1-9 argument where applicable;
3. apply an MW sieve / elliptic Chabauty to the surviving rank-one square-coordinate branches of `G0`, `G+`, or `G-`.

If those exact computations cannot be certified, the correct action is to freeze this finite elliptic wall rather than return to the genus-7 search or saturated congruence route.

## 7. Firewalls

This result does **not** prove that `G0`, the first-two-cover curve, equation (6), or the perfect-cuboid problem has no rational solution. The receiver is family-specific. No condition is promoted to arbitrary perfect cuboids, and Stage27 / StructureRadar are unchanged.

```text
A1_10_STATUS=SUBMITTED_FOR_AUDIT
A1_10_G0_EXACT_FINITE_SQUARECLASS_DESCENT=true
A1_10_G0_SQUARECLASSES=±1,±3,±13,±19,±39,±57,±247,±741
A1_10_G0_DELTA19_ELIMINATED=true
A1_10_NEW_ARBITRARY_CUBE_CONSTRAINT=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
