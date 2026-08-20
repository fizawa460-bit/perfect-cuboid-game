# StageA1 A1-9 — finite elliptic-twist descent of the genus-2 factors

## Scope

A1-8 replaced the first-two-cover genus-7 curve by the elliptic quotient

```text
E: Y^2 = Q(z),
Q(z)=z^4-20z^2+256z-412,
```

and three smooth genus-2 factors

```text
G0: W0^2=(z^2-4)Q(z),
G+: W+^2=(z+2)Q(z),
G-: W-^2=(z-2)Q(z).
```

A1-9 attacks `G+` and `G-` by an exact squareclass descent. It does **not** enlarge the old height search and does not repeat the saturated local-prime scan.

All statements remain specific to the corrected equation-(6) Hilbert-cube family.

## 1. Primitive homogeneous form

Write a finite rational `z` in lowest terms as

```text
z=a/b, gcd(a,b)=1, b>0,
```

and put

```text
H(a,b)=a^4-20a^2b^2+256ab^3-412b^4.
```

Then

```text
Q(a/b)=H(a,b)/b^4.
```

For a rational point on the odd-degree genus-2 models, clearing denominators gives an integer square:

```text
G-: c^2=b(a-2b)H(a,b),
G+: c^2=b(a+2b)H(a,b).                         (A1.9.1)
```

The relevant gcds are

```text
gcd(b,a±2b)=1,
gcd(b,H)=1,
gcd(a-2b,H) | Q(2)*b^4 = 36 b^4,
gcd(a+2b,H) | Q(-2)*b^4 = -988 b^4.
```

Since `gcd(a±2b,b)=1`, the last two simplify to

```text
gcd(a-2b,H) | 36,
gcd(a+2b,H) | 988=4*13*19.                    (A1.9.2)
```

The exact endpoint values are

```text
Q(2)=36,
Q(-2)=-988=-4*13*19.
```

## 2. Square denominator lemma

In either `G+` or `G-`, the factor `b` in (A1.9.1) is coprime to the other two factors. Therefore

```text
b is a square.                                  (A1.9.3)
```

Write `b=v^2`.

This is already a strict rational-point restriction on both genus-2 factors: every finite rational `z` occurring on `G+` or `G-` has square denominator in lowest terms.

## 3. The 2-part does not enter the squareclass

Let `t=a±2b`.

- If `b` is even, then `a` is odd, so `t` and `H` are odd.
- If `b` and `a` are odd, then again `t` and `H` are odd.
- If `b` is odd and `a` is even, then `v_2(H)=2`. Since `b t H` is a square, `v_2(t)` is even.

Thus the squareclass shared by `t` and `H` never contains `2`.

## 4. Exact finite squareclass sets

Because the product `tH` is a square, `t` and `H` have the same signed squareclass. By (A1.9.2) and the 2-adic observation:

### `G-`

Every finite rational point on `G-` determines

```text
delta in D-={+1,-1,+3,-3}
```

such that

```text
z-2 = delta*u^2,
Q(z) = delta*v^2.                               (A1.9.4-)
```

Conversely any rational solution of (A1.9.4-) gives a rational point on `G-`.

### `G+`

Every finite rational point on `G+` determines

```text
delta in D+={±1, ±13, ±19, ±247}
```

such that

```text
z+2 = delta*u^2,
Q(z) = delta*v^2.                               (A1.9.4+)
```

Conversely any rational solution of (A1.9.4+) gives a rational point on `G+`.

So the genus-2 rational-point problem has become a finite collection of elliptic-twist conditions plus one square-coordinate condition.

## 5. Jacobians of the quartic twists

For squarefree signed `delta`, let

```text
T_delta: Q(z)=delta*v^2.
```

Its Jacobian is the quadratic twist

```text
E_delta:
W^2 = X^3 + delta^2*7668 X + delta^3*489456.    (A1.9.5)
```

This follows equivalently by twisting the A1-4 Jacobian, or from the binary-quartic invariants: multiplying the quartic by `delta` multiplies `I` by `delta^2` and `J` by `delta^3`.

## 6. Exact external adapter for all four `G-` classes

The following minimal models are exactly Q-isomorphic to (A1.9.5). In each line the change to the A1-9 short model is explicit.

```text
delta=+1:
  LMFDB 6080.r1: y^2=x^3+x^2+95x+703
  X=9x+3, W=27y

delta=-1:
  LMFDB 6080.i1: y^2=x^3-x^2+95x-703
  X=9x-3, W=27y

delta=+3:
  LMFDB 54720.bl1: y^2=x^3+852x+18128
  X=9x, W=27y

delta=-3:
  LMFDB 54720.ba1: y^2=x^3+852x-18128
  X=9x, W=27y
```

The LMFDB records give Mordell-Weil rank `1` and trivial torsion for all four curves. Thus `G-` is not killed by a rank-zero shortcut, but it is reduced exactly to four rank-one elliptic square-coordinate problems. That is a suitable target for elliptic Chabauty / Mordell-Weil sieve computation rather than genus-2 brute force.

Stable source locators:

- `https://www.lmfdb.org/EllipticCurve/Q/6080/r/1`
- `https://www.lmfdb.org/EllipticCurve/Q/6080/i/1`
- `https://www.lmfdb.org/EllipticCurve/Q/54720/bl/1`
- `https://www.lmfdb.org/EllipticCurve/Q/54720/ba/1`

## 7. One `G+` component is rigorously removed

For `delta=19`, (A1.9.5) is Q-isomorphic to

```text
LMFDB 115520.cf1:
y^2=x^3+x^2+34175x+4616575,
```

by

```text
X=9x+3,
W=27y.
```

LMFDB records this elliptic curve with

```text
rank = 0,
torsion = trivial.
```

Therefore the genus-1 quartic torsor

```text
T_19: Q(z)=19 v^2
```

has no rational point.

Reason: if `T_19(Q)` were nonempty, choosing one rational point would identify the torsor with its Jacobian `E_19`. Since `E_19(Q)` is trivial, `T_19(Q)` would then contain exactly one point. But the involution `(z,v)->(z,-v)` is defined over Q and has no rational fixed point:

- an affine fixed point would require `v=0`, hence a rational root of `Q`, and `Q` has none;
- the two points at infinity are rational only if `19` is a rational square, which it is not.

Hence no rational point exists on `T_19`.

Consequently the `delta=+19` component of `G+` is impossible:

```text
G+_delta=19 = EMPTY over Q.                     (A1.9.6)
```

For comparison, `delta=-19` maps to LMFDB `115520.bc1`, which has rank `1`, so that sign is not removed by the same argument.

Stable source locators:

- `https://www.lmfdb.org/EllipticCurve/Q/115520/cf/1`
- `https://www.lmfdb.org/EllipticCurve/Q/115520/bc/1`

## 8. What remains

After A1-9:

- `G-` is a union of four rank-one elliptic square-coordinate receivers (`delta=±1,±3`);
- `G+` has eight formal squareclasses, but `delta=+19` is removed exactly;
- the remaining `G+` classes are `±1, ±13, -19, ±247`;
- `G0` has not yet received the analogous three-factor squareclass descent;
- no larger finite-height search is justified.

A next substantive batch may do one of:

1. certify the remaining `G+` twist ranks and remove any further rank-zero/trivial-torsion torsors;
2. run an exact Mordell-Weil sieve / elliptic-Chabauty computation on the four `G-` rank-one branches;
3. perform the analogous finite squareclass descent for `G0` if it yields a strictly smaller finite receiver.

If those computations cannot be certified, freeze the exact elliptic-twist wall rather than returning to the old genus-7 search.

## 9. Firewalls

This result does **not** prove:

- that `G+`, `G-`, or the full first-two-cover curve has no rational points;
- that equation (6) is universal;
- any necessary condition for an arbitrary perfect cuboid;
- existence or nonexistence of a perfect cuboid.

```text
A1_9_STATUS=SUBMITTED_FOR_AUDIT
A1_9_SQUARE_DENOMINATOR_LEMMA=true
A1_9_GMINUS_SQUARECLASSES=+1,-1,+3,-3
A1_9_GPLUS_SQUARECLASSES=+1,-1,+13,-13,+19,-19,+247,-247
A1_9_GMINUS_ALL_FOUR_ELLIPTIC_JACOBIANS_RANK1=true
A1_9_GPLUS_DELTA19_ELIMINATED=true
A1_9_NEW_ARBITRARY_CUBE_CONSTRAINT=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
