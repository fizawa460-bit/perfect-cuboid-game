# StageA2 A2-5 — rational-point closure of the published-minus18 two-cover receiver

## Scope

A2-5 starts only from the audited A2-4 receiver

```text
Cplus : R^2=t^2-5t-5,     S^2=t^2-t-1,
Cminus: R^2=-(t^2-5t-5), S^2=-(t^2-t-1),
```

with the published equation-(6) coefficient permanently locked at `-18`.

No StageA1 `-8` curve, rank computation, Mordell-Weil sieve, or 7-adic result is imported.

The goal is to determine `Cplus(Q)` and `Cminus(Q)` exactly enough to decide whether any nondegenerate finite `t` survives.

## 1. Birational quartic for Cplus

Use the rational point `(t,R)=(-1,1)` on the first conic and the line

```text
R = 1 + m(t+1).
```

The second intersection is

```text
t = -(m^2+2m+6)/(m^2-1),
R = -(m^2+7m+1)/(m^2-1).
```

Writing

```text
S = y/(m^2-1)
```

turns the second square equation into the smooth genus-1 quartic

```text
Qplus: y^2 = m^4+6m^3+23m^2+22m+29.           (A2.5.1)
```

Its polynomial discriminant is

```text
12960000 = 2^8 * 3^4 * 5^4 != 0.
```

The map above is birational on the ordinary affine chart; the points lost by the line parameterization are tracked separately below.

## 2. Birational quartic for Cminus

Use the rational point `(t,R)=(1,3)` and the line

```text
R = 3 + m(t-1).
```

The second intersection is

```text
t = (m^2-6m+4)/(m^2+1),
R = -3(m^2-m-1)/(m^2+1).
```

Writing

```text
S = y/(m^2+1)
```

gives

```text
Qminus: y^2 = m^4+6m^3-37m^2+42m-11.          (A2.5.2)
```

Again

```text
disc(Qminus polynomial)=12960000 != 0.
```

Thus both `Qplus` and `Qminus` are smooth genus-1 curves with rational points.

## 3. Common Jacobian

For a binary quartic

```text
f=a m^4+b m^3+c m^2+d m+e,
```

use the classical invariants

```text
I = 12ae-3bd+c^2,
J = 72ace+9bcd-27ad^2-27b^2e-2c^3.
```

For **both** (A2.5.1) and (A2.5.2), exact arithmetic gives

```text
I=481,
J=9758.
```

Hence both quartics have the same Jacobian

```text
E15: Y^2 = X^3 - 27 I X - 27 J
           = X^3 - 12987 X - 263466.            (A2.5.3)
```

The cubic factors as

```text
X^3-12987X-263466=(X+102)(X+21)(X-123).
```

The exact Mordell-Weil datum is independently available in two stable sources:

1. **LMFDB 15.a5**: rank `0`, torsion `Z/2Z x Z/4Z`, hence exactly `8` rational points.  The LMFDB minimal model is

   ```text
   y^2+xy+y=x^3+x^2-10x-10.
   ```

   Its invariants are `c4=481`, `c6=4879`, `Delta=50625`.  For (A2.5.3),

   ```text
   c4=623376=6^4*481,
   c6=227634624=6^6*4879,
   Delta=110199605760000=6^12*50625,
   ```

   so this is the exact rational isomorphism class `15.a5`, not merely a same-j identification.

2. Leprévost–Pohst–Schöpp, *Units in some parametric families of quartic fields*, Acta Arith. 127 (2007), 205–216, DOI `10.4064/aa127-3-1`, proof of Theorem 2.5, pp. 4–5.  They use precisely the short model

   ```text
   Y^2=X^3-12987X-263466
   ```

   and list all eight rational points of this rank-zero torsion curve.

Since each of `Qplus` and `Qminus` has a rational point, choosing one as origin identifies the genus-1 curve with its Jacobian over `Q`. Therefore each quartic has **exactly eight rational points**.

## 4. Eight points on Qplus and their images

The following eight rational points are explicit on `Qplus`:

```text
m=-7/2, y=+/-45/4,          (2 points)
m= 1,   y=+/-9,             (2 points)
m=-1,   y=+/-5,             (2 points)
m=infinity, y/m^2=+/-1.     (2 points)
```

There are already eight of them, and `#Qplus(Q)=8`, so this list is complete.

Their images on `Cplus` are:

- `m=-7/2` gives `t=-1, R=1, S=+/-1`;
- the two quartic infinities give the remaining `t=-1, R=-1, S=+/-1` points;
- `m=+1` and `m=-1` are the four projective `t=infinity` points.

Thus

```text
Cplus(Q): t in {-1, infinity} only.
```

Under the A2-4 conic map:

- `t=-1` maps to a projective infinity of `E18`;
- `t=infinity` maps to `z=2`, hence `k=1`, the excluded wall `c^2=d^2`.

So `Cplus` contains no nondegenerate finite candidate.

## 5. Eight points on Qminus and their images

The eight rational points on `Qminus` are

```text
m=1/2, y=+/-5/4,            (2 points)
m=1,   y=+/-1,              (2 points)
m=3,   y=+/-5,              (2 points)
m=infinity, y/m^2=+/-1.     (2 points)
```

Again this is already the full set because `#Qminus(Q)=8`.

Their images on `Cminus` are:

- `m=1/2` gives `t=1, R=3, S=+/-1`;
- the two quartic infinities give `t=1, R=-3, S=+/-1`;
- `m=1` gives `t=-1/2, R=3/2, S=+/-1/2`;
- `m=3` gives `t=-1/2, R=-3/2, S=+/-1/2`.

Therefore

```text
Cminus(Q): t in {1, -1/2} only.
```

Under the A2-4 map:

- `t=1` maps to a projective infinity of `E18`;
- `t=-1/2` maps to `z=2`, hence the same excluded `k=1` wall.

So `Cminus` also contains no nondegenerate finite candidate.

## 6. Exact E18 closure

A2-4 proved that every rational point of the published-minus18 quotient

```text
E18: Y^2=z^4-40z^2+256z-112
```

lifts to one of `Cplus` or `Cminus`.  A2-5 has now determined both cover point sets completely.

Every rational point of the cover receiver maps either to

```text
z=infinity
```

or to

```text
z=2 -> k=1 -> c^2=d^2,
```

which is an excluded source-parameter wall.

Hence there is **no nondegenerate rational point on the published equation-(6) anchor boundary**.

This is a complete exclusion of that specific published family boundary.  It is not a theorem about arbitrary perfect cuboids because equation (6) has never been proved to dominate all anchored Hilbert cubes.

The later reconstruction tests (`k` square, `u^2+4` square, source-factor positivity/nonvanishing) do not need to be invoked: every quotient point has already died at infinity or the earlier `k=1` wall.

## 7. Firewalls and routing

```text
A2_5_STATUS=SUBMITTED_FOR_AUDIT
A2_5_CPLUS_QPOINTS=8_COMPLETE
A2_5_CMINUS_QPOINTS=8_COMPLETE
A2_5_COMMON_JACOBIAN=15.a5
A2_5_COMMON_JACOBIAN_RANK=0
A2_5_COMMON_JACOBIAN_TORSION=Z/2Z_x_Z/4Z
A2_5_E18_NONDEGENERATE_RATIONAL_POINTS=0
A2_5_PUBLISHED_EQUATION6_ANCHOR_NONDEGENERATE_POINTS=0
A2_5_FAMILY_SPECIFIC_EXCLUSION_COMPLETE=true
A2_5_GENERAL_COVERAGE_PROVED=false
A2_5_ARBITRARY_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
A2_5_PERFECT_CUBOID_FOUND=false
A1_MINUS8_RESULTS_IMPORTED=false
AUDIT_REQUIRED=true
NEXT_IF_AUDIT_PASSES=A2_CLOSE_PUBLISHED_MINUS18_FAMILY_EXCLUSION
NEXT_EXPECTED_COMMAND=StageA2-audit
```
