# StageA1 A1-5 — primitive Pythagorean descent of the first-two-cover receiver

## Scope

A1-4 reduced the first two reconstruction covers of the corrected equation-(6) anchor family to the exact square condition

```text
C^2 = A(a,b)^2 + B(a,b)^2,
```

for coprime nonzero integers `a,b`, `a^2 != b^2`, where

```text
A = a^8 - 8 a^4 b^4 + b^8,
B = 16 a^3 b^3 (a^2-b^2).
```

This task does not increase the finite search height. It replaces that numerical receiver by an exact primitive-Pythagorean descent.

The result remains specific to the published equation-(6) Hilbert-cube family. It is not a condition on every perfect cuboid.

## 1. Exact common-divisor lemma

Put

```text
d = a^2-b^2,
g = gcd(|A|,|B|).
```

Then

```text
g = gcd(|d|,6).                                  (A1.5.1)
```

In particular `g` is exactly one of `1,2,3,6`.

### Proof

Because `gcd(a,b)=1`,

```text
gcd(A,a)=gcd(b^8,a)=1,
gcd(A,b)=gcd(a^8,b)=1.
```

Hence any odd prime dividing `g` must divide `d=a^2-b^2`. For such a prime `q`, with `q` not dividing `ab`, the congruence `a^2=b^2 (mod q)` gives

```text
A = a^8-8a^4b^4+b^8 = -6 b^8 (mod q),
```

so `q=3`.

If `3|d`, then `3` does not divide `ab`. Writing `a^2=b^2+3h` and reducing modulo `9` gives

```text
A = -6 b^8 (mod 9),
```

so `v_3(A)=1`. Thus the odd part of `g` is exactly `3` when `3|d`, and otherwise `1`.

For the 2-part: if one of `a,b` is even and the other odd, then `A` is odd, so `2` does not divide `g`. If both are odd, then odd fourth and eighth powers are `1 (mod 16)`, hence

```text
A = 1-8+1 = 10 (mod 16),
```

so `v_2(A)=1`. Since `2|d` exactly in the both-odd case, the 2-part of `g` is exactly `2` when `2|d` and otherwise `1`.

Combining the 2- and 3-parts proves (A1.5.1).

## 2. The normalized triple is primitive

Assume the first-two-cover condition holds:

```text
C^2=A^2+B^2.
```

By definition of `g`,

```text
(A/g)^2 + (B/g)^2 = (C/g)^2
```

is a primitive integer Pythagorean triple. Moreover `A/g` is odd and `B/g` is even. Therefore there exist coprime positive integers `M>N`, of opposite parity, such that after an allowed sign on the odd leg,

```text
|A|/g = M^2-N^2,
|B|/g = 2MN,
 C/g  = M^2+N^2.                                (A1.5.2)
```

Equivalently,

```text
MN = (8/g) |a^3 b^3 (a^2-b^2)|.               (A1.5.3)
```

This is an exact descent: every rational survivor of the first two square covers yields a primitive Pythagorean parameter pair `(M,N)` satisfying (A1.5.2)-(A1.5.3), and conversely such a pair reconstructs the square `C^2=A^2+B^2`.

## 3. Pairwise-coprime source factors

For coprime `a,b`, the three integers

```text
|a|,
|b|,
|a^2-b^2|
```

are pairwise coprime. Therefore, away from the small primes `2,3` already isolated in `g`, equation (A1.5.3) has a rigid allocation property.

For every prime `q>=5`:

- if `q|a`, then exactly one of `M,N` contains the full exponent `3 v_q(a)`;
- if `q|b`, then exactly one of `M,N` contains the full exponent `3 v_q(b)`;
- if `q|(a^2-b^2)`, then exactly one of `M,N` contains the full exponent `v_q(a^2-b^2)`;
- the other member of `{M,N}` is `q`-coprime.

This follows from `gcd(M,N)=1` and (A1.5.3).

Thus primes coming from the edge-ratio numerator or denominator enter the primitive Pythagorean parameters with exponents divisible by `3`, while primes from the difference factor carry their original exponent. The only exceptional bookkeeping is at `2` and `3`, where `g=gcd(a^2-b^2,6)` removes exactly the common part.

## 4. Compatibility with the A1-4 local sieve

A1-4 proved the family-specific local condition

```text
p | a b (a^2-b^2)
```

for each

```text
p in {3,5,7,23}.
```

For `p=5,7,23`, the prime is not absorbed by `g`, so (A1.5.3) implies

```text
5*7*23 = 805 | MN.                              (A1.5.4)
```

The prime `3` has two cases:

- if `3|a b`, then `3` survives in `MN` with exponent at least `3`;
- if `3|(a^2-b^2)`, then `3|g` and one factor of `3` is removed in (A1.5.3).

No contradiction follows from this alone, but the local sieve now feeds an exact primitive-Pythagorean receiver rather than only a finite search.

## 5. What this changes

A1-5 is substantive progress because it replaces the raw genus-7 first-two-cover square test by the exact arithmetic system

```text
g = gcd(a^2-b^2,6),
|a^8-8a^4b^4+b^8|/g = M^2-N^2,
MN = (8/g)|a^3b^3(a^2-b^2)|,
gcd(M,N)=1,
M not congruent N (mod 2).
```

The next useful attack is no longer "search to a larger height". It is to test whether the nearly-coprime factorization of `M-N` and `M+N`, together with the cube-exponent allocation in `MN`, gives a genuine descent, a finite cover family, or a local obstruction. If that step only renames the same genus-7 curve, StageA1 should pause.

## 6. Firewalls

This result proves none of the following:

- that the equation-(6) family has no anchored rational point;
- that the equation-(6) family is universal;
- that every perfect cuboid satisfies (A1.5.2)-(A1.5.3);
- existence or nonexistence of a perfect cuboid.

The receiver is family-specific because `A` and `B` come from the corrected equation-(6) reconstruction tower.

```text
A1_5_STATUS=SUBMITTED_FOR_AUDIT
A1_5_NEW_EXACT_GCD_LEMMA=true
A1_5_GCD_FORMULA=gcd(a^2-b^2,6)
A1_5_PRIMITIVE_PYTHAGOREAN_DESCENT=true
A1_5_CUBE_EXPONENT_ALLOCATION=true
A1_5_LOCAL_SIEVE_INTEGRATED=true
A1_5_NEW_ARBITRARY_CUBE_CONSTRAINT=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
