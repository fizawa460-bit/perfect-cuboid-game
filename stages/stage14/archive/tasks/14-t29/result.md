# Stage14-t29 — visible largest-prime matching and square-sieve boundary

## Purpose

Stage14-t28 reduced the unique dangerous `(alpha,beta)=(1,1)` fibre to

\[
Z^2=g_1g_2g_3g_4,
\]

with

\[
g_1=bp-aq,\quad g_2=aq+bp,\quad g_3=bq-ap,\quad g_4=bq+ap,
\]

and squarefree packet factors `g_i=d_i z_i^2`. It also showed that the canonical largest odd direction prime

\[
\ell=P^+(\Delta)_{\rm odd},\qquad
\Delta=2ab(b^2-a^2)(a^2+b^2),
\]

need not occur in any `d_i`.

Stage14-t29 splits the non-torsion packet into the kernel-visible and residual branches more sharply. The main new fact is that a visible odd direction prime is not free to occupy an arbitrary even subset of the four kernels: the direction column determines one of three perfect matchings, and primitivity forces exactly one matched pair. This produces an explicit large-modulus linear congruence on `(p,q)`.

However, reducing the weighted biquadrate modulo that same visible prime produces no new character condition: the reduced quartic congruence is already a tautological consequence of the matching congruence. Thus the canonical largest prime is useful as an **incidence modulus**, but not as a black-box square-sieve prime.

## 1. Odd direction support is disjoint by column

Because `(a,b)=1`, the four integers

\[
a,\qquad b,\qquad b^2-a^2,\qquad a^2+b^2
\]

have pairwise disjoint odd prime support. Indeed, any common divisor of `a` or `b` with either quadratic factor divides both `a` and `b`, while

\[
\gcd(b^2-a^2,a^2+b^2)\mid2.
\]

Hence every odd prime `ell|Delta` belongs to exactly one of the four direction columns.

This makes the canonical largest odd prime column unambiguous.

## 2. Three exact perfect matchings

Reduce the four linear forms modulo an odd direction prime `ell`.

### 2.1 `ell|a` or `ell|b`

The forms pair as

\[
\boxed{M_{ab}=\{\{1,2\},\{3,4\}\}}.
\]

If `ell|a`, then modulo `ell`

```text
g1 = g2 = b p,
g3 = g4 = b q.
```

Thus the pair `{1,2}` is divisible exactly when `ell|p`, and `{3,4}` exactly when `ell|q`.

If `ell|b`, the roles are reversed:

```text
g1 = -g2 = -a q,
g3 = -g4 = -a p.
```

Thus `{1,2}` corresponds to `ell|q` and `{3,4}` to `ell|p`.

Since `(p,q)=1`, an odd `ell` cannot divide both matched pairs.

### 2.2 `ell|(b^2-a^2)`

Now `b/a=+1` or `-1` modulo `ell`, and the matching is

\[
\boxed{M_-=\{\{1,3\},\{2,4\}\}}.
\]

One pair is equivalent to

\[
p\equiv q\pmod\ell,
\]

and the other to

\[
p\equiv-q\pmod\ell,
\]

with the assignment depending on the sign of `b/a`. Again both cannot occur for primitive `(p,q)` at an odd prime.

### 2.3 `ell|(a^2+b^2)`

Such an odd prime satisfies `ell=1 mod 4`. Put

\[
\rho=b a^{-1}\pmod\ell,
\qquad \rho^2=-1.
\]

The matching is

\[
\boxed{M_+=\{\{1,4\},\{2,3\}\}}.
\]

Specifically,

\[
\ell\mid g_1,g_4
\iff q\equiv\rho p\pmod\ell,
\]

and

\[
\ell\mid g_2,g_3
\iff q\equiv-\rho p\pmod\ell.
\]

The two conditions cannot hold simultaneously unless `ell|p,q`, forbidden by primitivity.

## 3. Kernel-visible prime theorem

Suppose now that the cover product is a square and write

\[
g_i=d_i z_i^2
\]

with squarefree `d_i`. If an odd direction prime `ell` is kernel-visible, then `ell` occurs in an even number of the `d_i`.

The matching analysis above shows more:

\[
\boxed{\text{a visible odd direction prime occurs in exactly one matched pair of kernels.}}
\]

It never occupies all four kernels. The matched pair is uniquely determined by the column of `ell` and one binary congruence state on `(p,q)`.

For the canonical largest prime on the t27 large branch,

\[
\ell>X^\eta,
\]

this gives an exact primitive congruence of modulus larger than `X^eta`.

Thus the visible branch has only `O(1)` state loss at the canonical prime, stronger than the generic `8^omega(Delta)=X^o(1)` packet bound.

## 4. Why the visible prime does not itself give a square-sieve character

The weighted biquadrate from t28 is

\[
\boxed{
g_1^2+g_4^2=g_2^2+g_3^2}
\]

or equivalently

\[
d_1^2z_1^4+d_4^2z_4^4=d_2^2z_2^4+d_3^2z_3^4.
\]

At a kernel-visible direction prime, reducing this equation modulo `ell` gives no independent condition.

- On `M_ab`, if `{1,2}` vanishes, the remaining relation is `g4^2=g3^2`; this already follows from `ell|a` or `ell|b`. The `{3,4}` case is symmetric.
- On `M_-`, if `{1,3}` vanishes, the remaining relation is `g4^2=g2^2`; this follows from `b=+/-a` and `p=+/-q`. The other pair is symmetric.
- On `M_+`, if `{1,4}` vanishes, the remaining relation is `g2^2+g3^2=0`; this follows from `rho^2=-1` and `q=rho p`. The other pair is symmetric.

Therefore

\[
\boxed{\text{the canonical visible prime is an incidence modulus, not an independent character sieve gate.}}
\]

A square/polynomial sieve can still be attempted with **auxiliary primes not already forced by the direction support**, but t29 does not yet prove the required moving-packet average.

## 5. Diagonal-quartic black-box boundary

For fixed packet coefficients, the t28 equation is a diagonal quartic surface

\[
d_1^2z_1^4+d_4^2z_4^4-d_2^2z_2^4-d_3^2z_3^4=0.
\]

Its coefficient product is automatically a square. Diagonal quartic surfaces in this square-product class can have Zariski-dense rational points once a suitable rational point off the standard lines and coordinate planes is present. Thus generic rational-point sparsity on the fixed quartic surface is not a valid substitute for the Stage14 support/reconstruction conditions.

Reference: A. Logan, D. McKinnon, R. van Luijk, *Density of rational points on diagonal quartic surfaces*, arXiv:0812.4779, Theorem 1.1.

Pierce--Xu Burgess bounds remain a possible auxiliary-prime input for admissible fixed forms, but the current problem still has moving packet coefficients, an existential projection to directions, and the physical reconstruction/height constraints. No direct theorem application yielding `A_11=O(B^(1/2-delta))` is asserted here.

Reference: L. B. Pierce, J. Xu, *Burgess bounds for short character sums evaluated at forms*, arXiv:1907.03108.

## 6. Residual kernel-invisible branch

If the canonical largest direction prime divides none of the squarefree kernels, the t28 coefficient packet does not expose it.

There are then two logically possible subcases:

1. the prime divides a matched pair of `g_i` to even valuations, so its parity disappears from all `d_i`;
2. it divides none of the rational linear factors, and only the Gaussian/dual congruence state from t26 remains.

The frozen synthetic non-torsion hits fall entirely in the second residual type, but this is finite evidence only and is not promoted to an asymptotic theorem.

Hence t26 remains necessary for the invisible branch.

## 7. Exact next counting target

For a dyadic shell `X<D<=2X`, choose the canonical largest odd direction prime `ell=P^+(Delta)`.

The non-torsion active directions split into:

1. **visible matching branch:** `ell` occurs in exactly one matched kernel pair and forces one primitive line in `(p,q) mod ell`;
2. **rational-even invisible branch:** the same matched line occurs but the `ell`-adic valuations disappear from the squarefree kernels;
3. **Gaussian/dual residual branch:** no `g_i` is divisible by `ell`, so the t26 split-prime or dual congruence must be used;
4. **smooth branch:** `ell<=X^eta` from t27.

The next useful positive theorem must retain the direction variables and prove a family incidence estimate. Merely applying a square sieve to the visible diagonal quartic at the canonical prime is insufficient.

## 8. Frozen synthetic audit

The t29 audit reuses the t28 box `a,b,p,q<=40` and verifies the perfect-matching theorem on every primitive physical-interval tuple, not only on square-cover hits.

Frozen totals:

```text
primitive interval tuples                         239121
canonical-prime rational matching incidences        6371
canonical-prime no-linear-factor residual          232750

matching incidences:
  sum column {1,4}                                  2294
  sum column {2,3}                                  2294
  difference column {1,3}                            587
  difference column {2,4}                            260
  b column {1,2}                                     466
  b column {3,4}                                     466
  a column {1,2}                                       2
  a column {3,4}                                       2

non-diagonal square-cover hits                       98
  kernel-visible                                     32
  kernel-invisible residual                          66

visible square hits:
  sum column                                           30
  difference column                                     2
  a/b columns                                           0
```

All `6371` rational matching incidences satisfy the corresponding reduced-biquadrate tautology. The finite proportions are diagnostic only.

## Boundary

```text
STAGE14_T29=COMPLETE_VISIBLE_LARGEST_PRIME_MATCHING_AND_SIEVE_BOUNDARY
ODD_DIRECTION_SUPPORT_COLUMNS_PAIRWISE_DISJOINT=true
VISIBLE_PRIME_PERFECT_MATCHING_THEOREM=true
VISIBLE_PRIME_EXACTLY_ONE_MATCHED_KERNEL_PAIR=true
VISIBLE_LARGE_PRIME_PRIMITIVE_CONGRUENCE_EXPLICIT=true
VISIBLE_CANONICAL_PRIME_NEW_CHARACTER_GATE=false
VISIBLE_CANONICAL_PRIME_IS_INCIDENCE_MODULUS=true
GENERIC_DIAGONAL_QUARTIC_POINT_COUNT_SUFFICIENT=false
KERNEL_INVISIBLE_GAUSSIAN_DUAL_BRANCH_STILL_REQUIRED=true
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t30 family incidence attack on the visible primitive congruence lines, with auxiliary-prime character averaging and the t26 Gaussian/dual residual branch kept separate
```
