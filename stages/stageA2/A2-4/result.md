# StageA2 A2-4 — exact factorization and finite two-cover descent

## Scope

A2-4 continues only the audited published-`-18` receiver

```text
E18: Y^2 = Q18(z) = z^4-40z^2+256z-112
```

from A2-3. No StageA1 `-8` Jacobian, rank, Mordell-Weil sieve, or 7-adic data is imported.

The A2-3 audit found the exact factorization

```text
Q18(z)=(z^2-8z+28)(z^2+8z-4).           (A2.4.1)
```

A2-4 exploits this factorization before any generic elliptic-curve machinery.

## 1. First exact squareclass split

Write a reduced rational point as

```text
z=a/b,  gcd(a,b)=1,  b>0,
```

and define the primitive binary quadratics

```text
F1(a,b)=a^2-8ab+28b^2,
F2(a,b)=a^2+8ab-4b^2.
```

Then

```text
Q18(a/b)=F1(a,b)F2(a,b)/b^4.
```

Also

```text
gcd(F1,b)=gcd(F2,b)=1,
F2-F1=16b(a-2b),
F1(2b,b)=16b^2.
```

Hence

```text
gcd(F1,F2) | 2^8.                         (A2.4.2)
```

So no odd prime can occur to odd valuation in both factors. Since

```text
z^2-8z+28=(z-4)^2+12 > 0
```

and a rational point on `E18` has `F1 F2 >=0`, the second factor is also positive (it has no rational zero). Therefore the common rational squareclass of the two factors is positive and supported only at `2`:

```text
z^2-8z+28 = delta U^2,
z^2+8z-4  = delta V^2,
delta in {1,2}.                            (A2.4.3)
```

This split is exact: every affine rational point on `E18` lies on one of these two branches, and conversely either branch gives a point on `E18` by `Y=+/- delta U V`.

## 2. The `delta=2` branch is empty over Q_5

Consider the projective system for `delta=2`:

```text
A^2-8AB+28B^2 = 2R^2,
A^2+8AB-4B^2 = 2S^2.                      (A2.4.4)
```

Modulo `5`:

- if `B=0`, then `A^2=2R^2`; because `2` is a nonsquare mod `5`, this forces `A=R=0`, impossible for a projective point;
- if `B!=0`, scale to `B=1`. Exhausting `A mod 5` gives no simultaneous solution.

Thus

```text
(A2.4.4)(Q_5)=empty,
```

and consequently every rational point on `E18` must satisfy the stronger exact split

```text
U^2=z^2-8z+28,
V^2=z^2+8z-4.                              (A2.4.5)
```

So the quotient rational-point problem has already descended to the intersection of two explicit conics.

## 3. Rational parameter on the first conic

The first conic in (A2.4.5) has the rational point

```text
(z,U)=(2,4).
```

Take the line

```text
U=4+t(z-2).
```

The second intersection with the conic gives the exact birational parameterization

```text
z = (2t^2-8t-6)/(t^2-1),
U = -4(t^2+t+1)/(t^2-1).                  (A2.4.6)
```

The values `t=+/-1` are the two points at infinity of the smooth quartic model. The excluded affine wall `(z,U)=(2,4)` occurs at `t=-1/2` in this parameterization.

Substituting (A2.4.6) into the second conic gives

```text
z^2+8z-4
 = 16 (t^2-5t-5)(t^2-t-1)/(t^2-1)^2.     (A2.4.7)
```

Therefore the remaining rational-point condition is

```text
(t^2-5t-5)(t^2-t-1) is a rational square. (A2.4.8)
```

## 4. Second exact squareclass split

For `t=a/b` reduced, define

```text
A(a,b)=a^2-5ab-5b^2,
B(a,b)=a^2-ab-b^2.
```

Then

```text
B-A=4b(a+b),
gcd(A,b)=1,
A(-b,b)=b^2,
```

so

```text
gcd(A,B) | 4.                              (A2.4.9)
```

Hence (A2.4.8) has a common signed squareclass

```text
delta in {+1,-1,+2,-2},
```

with

```text
A=delta R^2,
B=delta S^2.                               (A2.4.10)
```

The two branches `delta=+/-2` are again empty over `Q_5`: the projective reductions mod `5` have no point, including at infinity because `+/-2` are both nonsquares mod `5`.

Thus every rational point of the published quotient lies on exactly one of the two surviving two-cover branches

```text
Cplus:
  R^2=t^2-5t-5,
  S^2=t^2-t-1,

Cminus:
  R^2=-(t^2-5t-5),
  S^2=-(t^2-t-1).                          (A2.4.11)
```

Known projective/trivial points are:

```text
Cplus:  t=-1, R=S=+/-1       -> quartic infinity,
Cminus: t= 1, R=+/-3,S=+/-1 -> quartic infinity,
Cminus: t=-1/2, R=+/-3/2,S=+/-1/2 -> z=2 excluded wall.
```

No other rational point is claimed or excluded here.

## 5. First reconstruction cover in the t-coordinate

A genuine source anchor point must also recover rational `k` from

```text
k+1/k=z,
```

so A2-3 requires `z^2-4` to be a rational square. Under (A2.4.6), the condition becomes the exact identity

```text
z^2-4
 = -16(2t+1)(t^2-2t-2)/(t^2-1)^2.        (A2.4.12)
```

Therefore every finite nondegenerate source candidate on either `Cplus` or `Cminus` must additionally satisfy

```text
-(2t+1)(t^2-2t-2) is a rational square.    (A2.4.13)
```

The remaining A2-3 reconstruction conditions are still:

```text
k is a rational square,
u^2+4 is a rational square,
```

followed by all original equation-(6) nondegeneracy/source-factor checks.

## 6. What A2-4 achieved

The correct published quotient has been reduced without importing any StageA1 arithmetic:

```text
E18(Q)
  -> exact factor split delta in {1,2}
  -> delta=2 killed over Q_5
  -> intersection of two explicit conics
  -> rational t-parameter
  -> exact second split delta in {+/-1,+/-2}
  -> +/-2 killed over Q_5
  -> only Cplus and Cminus remain
  -> first reconstruction cover becomes (A2.4.13).
```

This is a strict structural narrowing. It is not a finite-height search and it is not a generic same-j/rank import.

The next natural exact target is to determine the rational points on `Cplus` and `Cminus` compatible with (A2.4.13), using fresh Jacobian/2-descent/Mordell-Weil information for these **published-minus18** covers only.

## 7. Firewalls

- The equation-(6) coefficient remains source-locked at `-18`.
- No StageA1 `-8` elliptic model, rank, MW sieve, or p-adic result is imported.
- Equation (6) is not proved universal for arbitrary anchored Hilbert cubes or perfect cuboids.
- A2-4 gives only family-specific necessary conditions.
- No perfect cuboid is found and no nonexistence theorem is proved.
- Stage27 and StructureRadar are unchanged.

```text
A2_4_STATUS=SUBMITTED_FOR_AUDIT
FIRST_FACTOR_SQUARECLASSES={1,2}
FIRST_DELTA2_Q5=EMPTY
E18_RATIONAL_POINTS_FORCE_BOTH_QUADRATIC_FACTORS_SQUARE=true
SECOND_FACTOR_SQUARECLASSES={+1,-1,+2,-2}
SECOND_PLUSMINUS2_Q5=EMPTY
SURVIVING_TWO_COVERS=Cplus,Cminus
FIRST_RECONSTRUCTION_T_COVER=-(2t+1)(t^2-2t-2)_IS_SQUARE
COMPLETE_E18_RATIONAL_POINT_CLOSURE=false
GENERAL_COVERAGE_PROVED=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
AUDIT_REQUIRED=true
NEXT=A2-5_PUBLISHED_MINUS18_TWO_COVER_RATIONAL_POINT_CLOSURE
NEXT_EXPECTED_COMMAND=StageA2-audit
```
