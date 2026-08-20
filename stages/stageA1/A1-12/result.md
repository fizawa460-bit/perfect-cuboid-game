# StageA1 A1-12 — explicit delta=1 elliptic map and elementary Mordell–Weil residue sieve

## Scope

After the A1-11 audit repair, the only squareclass relevant to an actual point on the nondegenerate first-two-cover curve is

```text
Q(z)=v^2,
z+2=s^2,
z-2=t^2,
Q(z)=z^4-20z^2+256z-412.
```

The audited elliptic model is

```text
E: y^2=x^3+x^2+95x+703,
P=(3,32),
E(Q)=Z P,
```

with rank `1` and trivial torsion (LMFDB `6080.r1`). A1-12 does not revisit the nontrivial quotient squareclasses. It derives an exact birational map from this specific rank-one model to the quartic and then performs a finite-field Mordell–Weil residue sieve on the multiplier `n` in `nP`.

All statements remain specific to the corrected equation-(6) StageA1 family.

## 1. Exact birational map from `6080.r1` to the quartic

For a point `(x,y)` on

```text
E: y^2=x^3+x^2+95x+703,
```

with `x != 3`, define

```text
z = -(y+32)/(x-3),
v = 2x+4-z^2.                                    (A1.12.1)
```

The key identity is

```text
[-z(x-3)-32]^2-(x^3+x^2+95x+703)
 = -(x-3)[x^2+(4-z^2)x+3z^2-64z+107].           (A1.12.2)
```

Hence a point of `E` with `x != 3` satisfies

```text
x^2+(4-z^2)x+3z^2-64z+107=0.
```

The discriminant of this quadratic in `x` is exactly

```text
(4-z^2)^2-4(3z^2-64z+107)
 = z^4-20z^2+256z-412
 = Q(z).                                          (A1.12.3)
```

Since `v=2x+4-z^2`, equations (A1.12.2)–(A1.12.3) give

```text
v^2=Q(z).
```

Conversely, from a quartic point `(z,v)` one recovers

```text
x=(v+z^2-4)/2,
y=-z(x-3)-32.                                    (A1.12.4)
```

Direct substitution gives the displayed Weierstrass equation. Thus (away from the standard exceptional points of the birational charts) (A1.12.1) and (A1.12.4) are mutually inverse.

The exceptional points are also explicit:

- `P=(3,32)` is a pole of `z` and corresponds to one quartic point at infinity;
- the identity `O` corresponds to the other point at infinity;
- at `-P=(3,-32)`, the quotient extends by the tangent slope. The tangent slope is `-2`, so `z=2`, and the extension gives `(z,v)=(2,6)`;
- `2P=(-3,-20)` gives `(z,v)=(2,-6)`.

The two finite points at `z=2` are the already-known degenerate wall.

## 2. Generator-index interpretation

Because `E(Q)=ZP`, every rational quartic point is represented by some multiplier `n in Z` (with the two infinity points handled by the exceptional chart above). For ordinary affine points,

```text
z_n = -(y(nP)+32)/(x(nP)-3).                     (A1.12.5)
```

Geometrically, `-z_n` is the slope of the line through `-P` and `nP`. The third intersection on the cubic is `(1-n)P`; therefore

```text
z_(1-n)=z_n,
v_(1-n)=-v_n.                                   (A1.12.6)
```

This recovers the first exact quotient points from A1-4 directly from generator multiples:

```text
-P   -> (2,6),
2P   -> (2,-6),
3P   -> (26/3, 694/9),
-2P  -> (26/3,-694/9),
4P   -> (-287/30,-54631/900),
-3P  -> (-287/30, 54631/900).
```

Thus the remaining StageA1 problem is now an explicit arithmetic condition on the integer multiplier `n`.

## 3. Exact finite-field Mordell–Weil residue sieve

The discriminant of the minimal model is

```text
Delta=-249036800=-2^19*5^2*19,
```

so every prime used below is a good-reduction prime.

For a good prime `p`, let

```text
N_p = order of P mod p in E(F_p).
```

Reduction is a group homomorphism, so `nP mod p` depends only on `n mod N_p`.

If a rational StageA1 survivor has finite reduction under (A1.12.1), then both

```text
z_n+2,
z_n-2
```

must be quadratic residues (zero allowed) in `F_p`.

For safety, the two pole residue classes (`O` and `P`) are retained rather than discarded: a finite rational point can reduce to a pole when `p` divides the denominator of `z`. The two classes giving the removable/degenerate value `z=2` are also retained. Therefore this is a necessary-condition sieve with no use of an unjustified denominator assumption.

Exact finite-field group-law enumeration gives:

```text
p     N_p     admissible n mod N_p
7       9     {0,1,2,8}
23     29     {0,1,2,28}
37     10     {0,1,2,9}
257    22     {0,1,2,21}
263    34     {0,1,2,33}
863    21     {0,1,2,20}
```

Equivalently, at every one of these six primes,

```text
n mod N_p in {0,1,2,-1}.                         (A1.12.7)
```

Every other residue class has finite `z` reduction and fails at least one of the two square tests.

This is a genuine Mordell–Weil residue restriction on the audited rank-one generator. It is not a height search on `x=a/b`.

## 4. Combined exact multiplier restriction

Combining the six congruence conditions by CRT gives

```text
M = lcm(9,29,10,22,34,21)
  = 3416490.
```

Exactly

```text
384
```

residue classes modulo `M` survive all six sieves. Thus every nondegenerate StageA1 survivor must satisfy

```text
n mod 3416490 in S_A1_12,
|S_A1_12|=384.                                   (A1.12.8)
```

The exact sorted residue set is generated deterministically by `verify.py`; its SHA-256 digest is

```text
63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874.
```

The surviving density is

```text
384/3416490 ~= 1.12396e-4,
```

so the exact multiplier search space is reduced to about one class in `8897`.

The set is invariant under `n -> 1-n`, as required by (A1.12.6).

## 5. What A1-12 does and does not close

A1-12 is substantive progress beyond the A1-11 wall because it provides:

1. an explicit birational map between the exact `delta=1` quartic and the audited rank-one minimal elliptic model;
2. an exact formula for the quartic coordinate in terms of `nP`;
3. a pure finite-field Mordell–Weil sieve, executable without Sage/Magma/PARI/mwrank;
4. a strict congruence reduction from all integers `n` to 384 classes modulo `3416490`.

It does **not** prove that the 384 classes contain no global survivor. Pole classes were intentionally retained when reduction alone cannot safely decide denominator parity. A complete closure still needs one of:

- prime-power/p-adic refinement of these residue classes;
- an elliptic divisibility/denominator recurrence argument;
- a stronger exact covering descent;
- a certified full Mordell–Weil sieve / elliptic-Chabauty computation.

Merely appending many more unrelated good primes without a structural improvement should not become an endless loop.

## 6. Firewalls

This result does not prove equation (6) universal, does not produce a necessary condition for arbitrary perfect cuboids, and does not prove perfect-cuboid existence or nonexistence. Stage27 and StructureRadar are unchanged.

```text
A1_12_STATUS=SUBMITTED_FOR_AUDIT
A1_12_EXPLICIT_DELTA1_BIRATIONAL_MAP=true
A1_12_MW_SIEVE_PRIMES=7,23,37,257,263,863
A1_12_COMBINED_MODULUS=3416490
A1_12_SURVIVING_MULTIPLIER_CLASSES=384
A1_12_SURVIVING_CLASS_SHA256=63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874
A1_12_COMPLETE_DELTA1_CLOSURE=false
A1_12_NEW_ARBITRARY_CUBE_CONSTRAINT=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
