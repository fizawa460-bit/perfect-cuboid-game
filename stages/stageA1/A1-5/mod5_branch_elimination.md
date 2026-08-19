# StageA1 A1-5 strengthening — primitive descent plus the mod-5 branch elimination

## Scope

This note strengthens the A1-5 primitive-Pythagorean receiver without increasing any finite search bound. It uses only the exact A1-5 descent together with the already audited A1-4 fact that every rational first-two-cover survivor reduces modulo `5` to `x=0,+/-1,infinity`.

The conclusion remains specific to the corrected equation-(6) Hilbert-cube family.

Let `a,b` be coprime nonzero integers with `a^2 != b^2`, and put

```text
A = a^8 - 8a^4b^4 + b^8,
B = 16a^3b^3(a^2-b^2),
d = a^2-b^2,
g = gcd(|A|,|B|)=gcd(|d|,6).
```

Assume

```text
A^2+B^2=C^2.
```

A1-5 then gives a primitive Pythagorean pair `M>N>0`, `gcd(M,N)=1`, of opposite parity, with

```text
|A|/g = M^2-N^2,
|B|/g = 2MN,
MN = (8/g)|a^3b^3d|.                     (A1.5.S1)
```

## 1. A prime-factor quadratic-residue filter

Let `q>=5` be prime with `q == 1 (mod 4)`.

Because `M,N` are coprime, any prime dividing `MN` divides exactly one of them. Since `-1` is a square modulo such a `q`, equation

```text
|A|/g = M^2-N^2
```

implies that whenever `q|MN` and `q` does not divide `A/g`, the residue class of `A/g` must be a quadratic residue modulo `q`.

There are two source locations.

### Case q divides ab

If `q|a` (the case `q|b` is symmetric), coprimality gives `q` not dividing `b`, and

```text
A == b^8 (mod q).
```

Hence a survivor must satisfy

```text
(g/q)=+1,                                      (A1.5.S2)
```

where `(./q)` is the Legendre symbol.

### Case q divides d=a^2-b^2

Then `q` does not divide `ab` and

```text
A == -6 b^8 (mod q).
```

As `(-1/q)=+1`, a survivor must satisfy

```text
((6/g)/q)=+1.                                 (A1.5.S3)
```

Thus primes `q==1 (mod 4)` dividing the numerator/denominator part and primes dividing the difference part are subject to two complementary squareclass tests determined only by `g`.

## 2. The audited p=5 sieve kills g=2 and g=3

A1-4 proved that every rational first-two-cover survivor satisfies

```text
5 | a b (a^2-b^2).                            (A1.5.S4)
```

The nonzero quadratic residues modulo `5` are `1,4`.

For the four possible gcd values,

```text
g mod 5       : 1, 2, 3, 1       for g=1,2,3,6,
(6/g) mod 5   : 1, 3, 2, 1       for g=1,2,3,6.
```

Therefore:

- if `5|ab`, condition (A1.5.S2) permits only `g=1` or `g=6`;
- if `5|d`, condition (A1.5.S3) again permits only `g=1` or `g=6`.

By (A1.5.S4), one of these source locations must occur. Consequently every rational first-two-cover survivor satisfies the exact global branch restriction

```text
g in {1,6}.                                   (A1.5.S5)
```

The intermediate gcd branches `g=2` and `g=3` are impossible.

This is not finite-search evidence: it is a proved consequence of the primitive descent and the exact mod-5 sieve.

## 3. Translate g in {1,6} back to a,b

Since `g=gcd(|a^2-b^2|,6)`, coprimality gives two and only two branches.

### Branch E: g=1

`a^2-b^2` is odd, so `a,b` have opposite parity. Also `3` does not divide `a^2-b^2`; for coprime `a,b` this forces exactly one of `a,b` to be divisible by `3`. Hence

```text
6 | ab.                                        (A1.5.S6E)
```

### Branch O: g=6

`a^2-b^2` is even, so coprime `a,b` are both odd. Also `3|a^2-b^2`; this forces neither `a` nor `b` to be divisible by `3`. Hence

```text
gcd(ab,6)=1.                                  (A1.5.S6O)
```

Equivalently, every rational first-two-cover survivor obeys the compact dichotomy

```text
2|ab  <=>  3|ab.                              (A1.5.S7)
```

The two excluded mixed cases are:

```text
both a,b odd with 3|ab,        (g=2),
opposite parity with 3 not|ab. (g=3)
```

## 4. Branch-specific divisibility of MN

A1-4 also gives `5*7*23=805 | MN`.

In Branch E (`g=1`), the even member of `a,b` contributes at least `2^3` through the cube in (A1.5.S1), the prefactor contributes another `2^3`, and the member divisible by `3` contributes at least `3^3`. Hence

```text
2^6 * 3^3 * 5 * 7 * 23 = 1391040 | MN.        (A1.5.S8E)
```

In Branch O (`g=6`), both `a,b` are odd and `d=a^2-b^2` is divisible by `24`. Thus

```text
MN = 4 |a^3b^3(d/3)|
```

has at least `2^5`, and therefore

```text
2^5 * 5 * 7 * 23 = 25760 | MN.                (A1.5.S8O)
```

These are exact family-specific consequences, not heuristic density statements.

## 5. Coprime factorization of the odd leg

Because `M,N` have opposite parity,

```text
R=M-N,
S=M+N
```

are positive odd integers. Moreover

```text
gcd(R,S)=1,
RS=|A|/g,
S^2-R^2=4MN=(32/g)|a^3b^3d|.                 (A1.5.S9)
```

So after the mod-5 branch elimination the next exact receiver has only two arithmetic branches (`g=1` and `g=6`) and a coprime odd factorization `RS=|A|/g` coupled to the cube-heavy difference-of-squares equation (A1.5.S9).

This is strictly narrower than the submitted four-branch primitive receiver.

## 6. Firewalls and next decision

Nothing here proves that the equation-(6) family has no anchored point, and nothing is promoted to arbitrary perfect cuboids. The source family is still non-universal.

The next main step is allowed only if the two-branch system (A1.5.S9), together with the cube-exponent allocation in `MN`, yields another genuine descent, finite cover decomposition, rational-point theorem, or new local obstruction. Merely renaming `R,S` or increasing a search bound is not progress.

```text
A1_5_MOD5_BRANCH_ELIMINATION_PROVED=true
A1_5_ALLOWED_G_VALUES=1,6
A1_5_EXCLUDED_G_VALUES=2,3
A1_5_SURVIVOR_DICHOTOMY=6|ab OR gcd(ab,6)=1
A1_5_BRANCH_E_MN_DIVISOR=1391040
A1_5_BRANCH_O_MN_DIVISOR=25760
A1_5_COPRIME_RS_RECEIVER_PROVED=true
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```
