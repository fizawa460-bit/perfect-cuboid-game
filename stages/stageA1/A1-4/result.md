# StageA1 A1-4 — bounded rational-point closure attempt

## Scope

This is the bounded A1-4 attempt originally authorized by the audited A1-3 checkpoint. It works only with the corrected equation-(6) anchor tower

```text
E: Y^2 = z^4 - 20 z^2 + 256 z - 412,
```

followed by the exact reconstruction conditions from A1-3. It does not claim that equation (6) covers all perfect cuboids.

## 1. The genus-1 quotient is not the bottleneck

For the binary quartic

```text
f(z)=z^4-20z^2+256z-412,
```

use the classical invariants

```text
I = -4544,
J = -1160192.
```

With the standard binary-quartic convention its Jacobian is

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

Hence `P` is not torsion: if it were torsion, `4P` would be torsion, while Nagell-Lutz on the integral short Weierstrass equation would force rational torsion points to have integral coordinates. Therefore the Jacobian has positive Mordell-Weil rank.

Because the quartic itself has the rational point `(z,Y)=(2,6)`, it is a trivial torsor under its Jacobian, so the quotient has infinitely many rational points. The reconstruction square covers, not rational points on the genus-1 quotient alone, are the relevant obstruction.

This does not produce a perfect cuboid.

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

The first is the known degenerate point `k=1`. The other two fail the first reconstruction condition because

```text
(26/3)^2 - 4 = 640/9,
(-287/30)^2 - 4 = 78769/900,
```

and neither is a rational square.

This finite search is diagnostic, not a proof that no other quotient point lifts.

## 3. Combine the first two square covers exactly

A1-3 requires

```text
z^2-4 is a square,
k is a square,
z=k+1/k.
```

Write

```text
k=x^2,  x in Q^*.
```

Then

```text
z=x^2+x^-2,
z^2-4=(x^2-x^-2)^2.
```

Thus surviving the first two covers is exactly equivalent to finding rational `x != 0,+/-1` such that

```text
D(x^2) is a rational square,
```

where

```text
D(k)=k^8-16k^6+256k^5-446k^4+256k^3-16k^2+1.
```

For reduced `x=a/b`, define

```text
A_h = a^8 - 8a^4b^4 + b^8,
B_h = 16a^3b^3(a^2-b^2).
```

Then the square condition is the exact integer identity

```text
b^16 D((a/b)^2) = A_h^2 + B_h^2.          (A1.4.2)
```

So the first two reconstruction covers become a structured rational Pythagorean-square problem.

## 4. Strengthened bounded exact search

The rerun exhaustively enumerates all reduced positive pairs

```text
1 <= a,b <= 5000,
gcd(a,b)=1,
a != b.
```

Sign of `x` is irrelevant because only `x^2` occurs. Exactly

```text
15200914
```

pairs are tested. For every pair the integer on the right of (A1.4.2) is tested for exact integer squareness.

Result:

```text
NONDEGENERATE_FIRST_TWO_COVER_SURVIVORS=0
```

Hence no rational parameter `x=a/b` of numerator/denominator height at most `5000` reaches even the first two square covers. The third condition `u^2+4` never needs to be tested in this range.

This is a rigorous finite computation only; it is not promoted to a theorem about all rational points.

## 5. Exact local sieve

For an odd prime `p`, reduce

```text
v^2=D(x^2)
```

modulo `p`. Exhaustive affine checking for all primes `<500` shows that exactly

```text
p in {3,5,7,23}
```

have the property that every affine `x in F_p` for which `D(x^2)` is a square lies in

```text
{0,+1,-1}.
```

Projectively one must also allow `x=infinity`. Therefore, if a rational survivor is written `x=a/b` in lowest terms, then for each of these four primes either `p|b`, or the affine reduction is `0,+/-1`. Equivalently,

```text
p | a b (a^2-b^2).                         (A1.4.3)
```

This is a proved family-specific congruence filter. It is not a global obstruction, because a rational point can reduce into one of these projectively degenerate residue classes at every listed prime. The `p=3` case is in particular tautological at the affine level because `F_3={0,+/-1}`.

## 6. What was and was not closed

The bounded A1-4 attempt establishes:

1. the corrected genus-1 quotient has positive Mordell-Weil rank;
2. the first two square covers combine to the exact structured equation (A1.4.2);
3. no nondegenerate combined-cover point occurs for reduced `x=a/b` with `a,b<=5000`;
4. the exact family-specific divisibility filter (A1.4.3) holds for `p=3,5,7,23`.

It does **not** establish:

- the complete rational points of the genus-3 cover;
- the complete rational points after all three reconstruction covers;
- exclusion of the entire equation-(6) anchor boundary;
- a reverse map from every perfect cuboid into equation (6);
- a new necessary condition for an arbitrary perfect cuboid;
- existence or nonexistence of a perfect cuboid.

## 7. Audit routing verdict

The submitted draft applied the earlier A1-3 rule literally and set `RECONNAISSANCE_NEGATIVE` after this bounded attempt. The independent audit accepts the mathematical results above but repairs that routing decision because the operator subsequently overrode the one-attempt stop: StageA1 may continue while it is producing substantive new mathematics.

A1-4 itself qualifies as substantive progress. It proves positive rank of the quotient, combines two reconstruction covers into one exact structured curve condition, verifies a large exact finite range, and extracts a new family-specific local divisibility filter. These are not mere renamings of the A1-3 receiver.

Continuation is therefore allowed under a progress-based anti-loop rule:

- a new proved identity, curve/cover reduction, rational-point statement, local obstruction, coverage result, or exact theorem adapter counts as progress;
- merely increasing a finite search bound without a changed receiver does not by itself count;
- equivalent repackaging or renaming of the same unresolved condition does not count;
- if successive batches stop producing concrete mathematical narrowing, StageA1 pauses;
- if the route reaches an external theorem wall better suited to Work, freeze that exact wall rather than manufacturing subdivisions.

The audited status is

```text
A1_4_STATUS=BOUNDED_ATTEMPT_COMPLETE
A1_4_QUOTIENT_POSITIVE_RANK_PROVED=true
A1_4_FIRST_TWO_COVERS_COMBINED=true
A1_4_HEIGHT5000_PAIRS_EXAMINED=15200914
A1_4_HEIGHT5000_SURVIVORS=0
A1_4_LOCAL_SIEVE_PRIMES=3,5,7,23
A1_4_COMPLETE_FAMILY_CLOSURE=false
A1_4_NEW_ARBITRARY_CUBE_CONSTRAINT=false
A1_4_PERFECT_CUBOID_FOUND=false
A1_4_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
STAGE_A1_STATUS=RECONNAISSANCE_ACTIVE_OPERATOR_OVERRIDE
STAGE_A1_STOP_AFTER_AUDIT=false
AUDIT_VERDICT=PASS_WITH_ROUTING_REPAIR
REPAIR_REQUIRED=false
NEXT_EXPECTED_COMMAND=StageA1-main-batch
```
