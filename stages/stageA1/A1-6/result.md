# StageA1 A1-6 — local-sieve completeness and saturation

## Scope

A1-5 reduced every hypothetical survivor of the first two reconstruction covers of the corrected equation-(6) family to the two arithmetic branches `g=1` or `g=6`. A1-6 tests the remaining local/congruence route before allowing any further search escalation.

Write

```text
F(x)=x^16-16x^12+256x^10-446x^8+256x^6-16x^4+1.
```

The first-two-cover condition is `y^2=F(x)`, with the degenerate reductions `x=0,+/-1,infinity` excluded from a genuine anchored survivor.

All statements below remain family-specific. Equation (6) is not a proved universal parametrization of perfect cuboids.

## 1. The prime-divisibility sieve is complete

The degree-16 polynomial `F` is squarefree, with

```text
disc(F)=2^132 * 3^4 * 5^8 * 13^2 * 19^6.
```

Hence for every prime

```text
p not in {2,3,5,13,19}
```

the smooth projective model of `y^2=F(x)` has good reduction and genus `7`.

Suppose an odd good-reduction prime `p>3` had no affine survivor `x mod p` outside

```text
{0,+1,-1}.
```

Since

```text
F(0)=1,
F(+1)=F(-1)=36,
```

each of these three x-values has exactly two points above it, and the even-degree monic model has two points at infinity. Thus

```text
#C(F_p) <= 8.                                      (A1.6.1)
```

But Hasse-Weil gives

```text
#C(F_p) >= p+1-14*sqrt(p).                         (A1.6.2)
```

For every `p>=211`, the right side is strictly greater than `8`. Indeed

```text
p+1-14*sqrt(p)>8
```

is equivalent, for `p>7`, to

```text
p^2-210p+49>0,
```

which already holds at `p=211` and then increases.

Therefore every prime whose affine survivor set is contained in `{0,+/-1}` lies below `211`, apart from the already listed bad-reduction primes, which also lie below `211`.

The exact exhaustive finite-field check over all 45 odd primes below `211` gives

```text
p in {3,5,7,23}                                    (A1.6.3)
```

and no others. The checker is `local_sieve.py`.

Thus the A1-4 list `{3,5,7,23}` is not merely a search-below-500 observation: it is the complete list of primes for this particular "only degenerate residue classes survive" divisibility mechanism.

## 2. The p=3 member is vacuous for a primitive ratio

For coprime integers `a,b`, one always has

```text
3 | a*b*(a^2-b^2).
```

If `3|ab` this is immediate. Otherwise `a^2=b^2=1 (mod 3)`, so `3|(a^2-b^2)`.

Hence the `p=3` member of (A1.6.3) supplies no new restriction on a reduced rational `x=a/b`. The genuinely restrictive fixed-prime divisibility filters are exactly

```text
5 | a*b*(a^2-b^2),
7 | a*b*(a^2-b^2),
23 | a*b*(a^2-b^2).                               (A1.6.4)
```

This recovers the A1-5 consequence `805|MN`, but now with a proof that no further prime of the same type exists.

## 3. The primes 5, 7, 23 are p-adically saturated

Return to the integral receiver

```text
A=a^8-8a^4b^4+b^8,
B=16a^3b^3(a^2-b^2),
F(a/b)=b^-16*(A^2+B^2).
```

Let `p` be any of `5,7,23` and assume the forced condition

```text
p | a*b*(a^2-b^2).
```

Then `p|B`, but `p` does not divide `A`:

- if `p|a`, then `A=b^8 (mod p)`;
- if `p|b`, then `A=a^8 (mod p)`;
- if `p|(a^2-b^2)`, then `A=-6b^8 (mod p)`.

In every case coprimality and `p>=5` make `A` a p-adic unit. Therefore

```text
A^2+B^2 = A^2 * (1+(B/A)^2),
```

with `B/A in p Z_p`. The unit `1+(B/A)^2` has a square root in `Z_p` by Hensel's lemma, starting from `1 mod p` because the derivative `2` is a unit.

So once (A1.6.4) is met, the same prime supplies no higher-power obstruction. In particular, replacing the mod-p check by mod-`p^k` at `p=5,7,23` cannot turn the existing divisibility condition into a contradiction.

## 4. The first-two-cover curve is everywhere locally soluble off the degenerate locus

There is no place-by-place local-emptiness proof available for this curve.

For every odd prime `p`, take the p-adic value

```text
x=p.
```

Then `x` is not `0,+/-1`, and

```text
F(p)=1 (mod p).
```

Thus `F(p)` has a p-adic square root by Hensel's lemma from `y=1 mod p`.

For `p=2`, take `x=2`. Every nonconstant term of `F(2)` is divisible by `8`, so

```text
F(2)=1 (mod 8),
```

and hence `F(2)` is a square in `Q_2`.

At the real place, `x=1/2` gives

```text
F(1/2)=164097/65536 > 0.
```

Consequently the affine nondegenerate locus of the first-two-cover curve has a point over every completion of `Q`.

This does not prove a rational point exists. It proves the opposite kind of statement needed for routing: a global exclusion, if true, cannot come from emptiness at a single completion.

## 5. Routing consequence

A1-6 closes the elementary local/congruence branch in a precise sense:

1. the complete fixed-prime divisibility list of the A1-4 type is `{3,5,7,23}`;
2. `p=3` is automatic for primitive `(a,b)`;
3. `p=5,7,23` are p-adically saturated after their forced divisibility condition is met;
4. the nondegenerate first-two-cover curve is everywhere locally soluble.

Therefore another larger finite search, another scan for primes of the same trivial-reduction type, or lifting only the same three primes to higher powers would not be substantive progress. The unresolved object is now a genuinely global rational-point/reconstruction-cover problem on an everywhere-locally-soluble high-genus cover, with the positive-rank genus-1 quotient already recorded in A1-4.

This is the natural external theorem/computational-algebra wall to freeze if StageA1 is integrated now.

## 6. Firewalls

A1-6 does **not** prove:

- that `y^2=F(x)` has no rational nondegenerate point;
- that the full equation-(6) anchor boundary has no rational point;
- that equation (6) covers every anchored Hilbert cube;
- any new necessary condition for an arbitrary perfect cuboid;
- existence or nonexistence of a perfect cuboid.

```text
A1_6_STATUS=SUBMITTED_FOR_AUDIT
A1_6_LOCAL_SIEVE_COMPLETE=true
A1_6_TRIVIAL_REDUCTION_ONLY_PRIMES=3,5,7,23
A1_6_NONVACUOUS_FIXED_DIVISIBILITY_PRIMES=5,7,23
A1_6_P_ADIC_SATURATION_5_7_23=true
A1_6_EVERYWHERE_LOCALLY_SOLUBLE_NONDEGENERATE=true
A1_6_GLOBAL_RATIONAL_POINT_PROBLEM_CLOSED=false
A1_6_NEW_ARBITRARY_CUBE_CONSTRAINT=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
