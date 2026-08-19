# StageA1 A1-4 — bounded rational-point closure attempt

## Scope

This is the single bounded A1-4 attempt authorized by the audited A1-3 checkpoint. It works only with the corrected equation-(6) anchor tower

```text
E: Y^2 = z^4 - 20 z^2 + 256 z - 412,
```

followed by the exact reconstruction conditions from A1-3. It does not rotate to another Hilbert-cube family and does not claim that equation (6) covers all perfect cuboids.

## 1. The genus-1 quotient is not the bottleneck

For the binary quartic

```text
f(z)=z^4-20z^2+256z-412,
```

use the classical invariants

```text
I = 12ae - 3bd + c^2 = -4544,
J = 72ace + 9bcd - 27ad^2 - 27b^2e - 2c^3 = -1160192.
```

With the standard binary-quartic convention, its Jacobian is

```text
V^2 = U^3 - 27 I U - 27 J
    = U^3 + 122688 U + 31325184.
```

After `U=4X`, `V=8W`, an integral scaled model is

```text
J0: W^2 = X^3 + 7668 X + 489456.          (A1.4.1)
```

The rational point

```text
P=(30,864)
```

lies on (A1.4.1). Direct group-law calculation gives

```text
2P=(-24,-540),
3P=(670,-17504),
4P=(12369/100,1824903/1000).
```

Hence `P` is not torsion: if it were torsion, `4P` would be torsion, while Nagell-Lutz on the integral short Weierstrass equation would force a rational torsion point to have integral coordinates.

Because the quartic itself already has the rational point `(z,Y)=(2,6)`, it is a trivial torsor under its Jacobian. Therefore the quotient has infinitely many rational points. The A1-3 reconstruction square covers, not rational points on the genus-1 quotient alone, are the decisive obstruction.

This observation is structural only. It does not produce a perfect cuboid.

## 2. Explicit quotient points and the first cover

A deterministic reduced-fraction search over

```text
z=a/b,
|a| <= 1000,
1 <= b <= 1000,
gcd(|a|,b)=1
```

finds exactly three positive-`Y` representatives:

```text
(z,Y)=(2,6),
(z,Y)=(26/3,694/9),
(z,Y)=(-287/30,54631/900).
```

The first is the known degenerate point `k=1`. The other two fail the first reconstruction condition:

```text
(26/3)^2 - 4 = 640/9,        not a rational square,
(-287/30)^2 - 4 = 78769/900, not a rational square.
```

Thus the first nontrivial rational quotient points visible at this height do not even lift to rational `k`.

This finite search is diagnostic, not a proof that no other quotient point lifts.

## 3. Combine the first two square covers exactly

A1-3 requires

```text
z^2-4 is a square,
k is a square,
z=k+1/k.
```

The first two conditions can be combined without loss. Write

```text
k=x^2,  x in Q^*.
```

Then

```text
z=x^2+x^-2,
z^2-4=(x^2-x^-2)^2.
```

Conversely, any rational `k` with `z=k+1/k` and square `k` has this form. Therefore surviving the first two covers is exactly equivalent to finding rational `x != 0, +/-1` for which

```text
D(x^2) is a rational square,
```

where

```text
D(k)=k^8-16k^6+256k^5-446k^4+256k^3-16k^2+1.
```

Equivalently, if `x=a/b` is reduced,

```text
A_h = a^8 - 8a^4b^4 + b^8,
B_h = 16a^3b^3(a^2-b^2),
```

then

```text
b^16 D((a/b)^2) = A_h^2 + B_h^2.        (A1.4.2)
```

Thus the first two reconstruction covers turn the genus-3 discriminant condition into a highly structured rational Pythagorean-square condition.

## 4. Bounded exact search on the combined first-two-cover curve

The deterministic search enumerates all reduced positive pairs

```text
1 <= a,b <= 500,
gcd(a,b)=1,
a != b.
```

There are exactly `152230` such pairs. For every pair it evaluates the integer on the right of (A1.4.2) and tests exact integer squareness.

Result:

```text
NONDEGENERATE_FIRST_TWO_COVER_SURVIVORS=0
```

So no rational parameter `x=a/b` of numerator/denominator height at most 500 reaches even the first two square covers. The third condition `u^2+4` therefore never needs to be tested in this search range.

Again, this is finite evidence only and is not promoted to a rational-point theorem.

## 5. A small exact local sieve

For an odd prime `p`, reduce the first-two-cover condition

```text
v^2 = D(x^2)
```

modulo `p`. Exhaustive finite-field checking for all primes `<500` shows that exactly

```text
p in {3,5,7,23}
```

have the following property:

> every `x in F_p` for which `D(x^2)` is a square satisfies `x in {0,+1,-1}`.

Consequently, if a rational survivor is written `x=a/b` in lowest terms, then for each

```text
p in {3,5,7,23}
```

one necessarily has

```text
p | a b (a^2-b^2).                         (A1.4.3)
```

This is a proved family-specific congruence filter. It is not an obstruction to all rational points, because a rational point may reduce into a degenerate residue class at each of these finitely many primes.

## 6. What was and was not closed

The bounded A1-4 attempt establishes:

1. the corrected genus-1 quotient has positive Mordell-Weil rank, so the quotient itself is not a finite-point obstruction;
2. the first two square covers combine to the exact structured curve (A1.4.2);
3. no nondegenerate combined-cover point occurs for reduced `x=a/b` with `a,b <= 500`;
4. the exact local divisibility filter (A1.4.3) holds for `p=3,5,7,23`.

It does **not** establish:

- the complete rational points of the genus-3 cover;
- the complete rational points after all three reconstruction covers;
- exclusion of the entire equation-(6) anchor boundary;
- a reverse map from every perfect cuboid into equation (6);
- a new necessary condition for an arbitrary perfect cuboid;
- existence or nonexistence of a perfect cuboid.

## 7. Anti-loop verdict

The audited A1-3 contract allowed exactly one bounded A1-4 attempt and required StageA1 to stop unless that attempt produced at least one of:

- a nondegenerate anchored rational point;
- a complete family-specific rational-point closure;
- a new coverage/reverse-map theorem;
- a new necessary condition for arbitrary anchored cubes.

None of those four events occurred.

The family-specific algebra is worth retaining, especially the positive-rank quotient, the exact Pythagorean cover (A1.4.2), and the local sieve (A1.4.3), but continuing by inventing A1-4a/A1-4b or rotating to more Hilbert-cube families would violate the anti-loop rule.

Therefore the main-lane verdict is

```text
A1_4_STATUS=BOUNDED_ATTEMPT_COMPLETE
A1_4_QUOTIENT_POSITIVE_RANK_PROVED=true
A1_4_FIRST_TWO_COVERS_COMBINED=true
A1_4_HEIGHT500_SURVIVORS=0
A1_4_LOCAL_SIEVE_PRIMES=3,5,7,23
A1_4_COMPLETE_FAMILY_CLOSURE=false
A1_4_NEW_ARBITRARY_CUBE_CONSTRAINT=false
A1_4_PERFECT_CUBOID_FOUND=false
A1_4_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
STAGE_A1_STATUS=RECONNAISSANCE_NEGATIVE
STAGE_A1_STOP_AFTER_AUDIT=true
UNRELATED_FAMILY_ROTATION_ALLOWED=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
