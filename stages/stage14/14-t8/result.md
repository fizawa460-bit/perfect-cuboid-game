# Stage14-t8 — reflected 2-descent moving-prime boundary

## Purpose

Stage14-t7 showed that the cheapest shared-`q` fixed-prime square-class sieve is vacuous on physical Pythagorean bases. Stage14-t8 therefore keeps the raw and reflected quartics separate and identifies where a genuinely new local condition can occur.

This stage does **not** prove `T(B)=o(sqrt(B))`. It isolates the exact moving-prime subset on which a future family large sieve must operate.

## Reflected quartic in physical coordinates

The third-face/reflected quartic is

\[
R^2=q^4+2Cq^2+1,
\qquad C=\frac2s-1.
\]

It has the exact form

\[
\boxed{
R^2=(q^2+1)^2+4\frac{1-s}{s}q^2.
}
\]

Write the physical Pythagorean base as

\[
s=t^2=\frac{X^2}{S^2},
\qquad S^2+X^2=H^2,
\qquad \gcd(S,X)=1.
\]

Then

\[
\frac{1-s}{s}=\frac{S^2-X^2}{X^2}.
\]

Thus the reflected member introduces the moving difference factor

\[
\boxed{\Delta_-=S^2-X^2}.
\]

At the level of the two j-families, the raw member has bad base divisor `s(s+1)` and the reflected member has bad base divisor `s(s-1)`. Their union is supported on

\[
s(1-s^2),
\]

which on the physical base is contained in primes dividing

\[
2SXH\Delta_-.
\]

The new support relative to the raw Stage14-s arithmetic is therefore carried by `Delta_-` (up to overlap and the prime 2).

## Exact odd-prime local lemma

Let `p` be an odd prime with

\[
p\mid \Delta_-,\qquad p\nmid SX.
\]

Then `s` is a `p`-adic unit and `1-s in p Z_p`. Put

\[
u=q^2+1.
\]

If `u` is a `p`-adic unit, then

\[
R^2=u^2\left(1+4\frac{1-s}{s}\frac{q^2}{u^2}\right),
\]

and the parenthesized factor lies in `1+p Z_p`. For odd `p`, every element of `1+p Z_p` is a square in `Q_p`. Hence

\[
\boxed{
p\mid\Delta_-,\ p\text{ odd},\ q^2+1\not\equiv0\pmod p
\Longrightarrow
\text{the reflected square condition is locally automatic at }p.
}
\]

Therefore a new `Delta_-` prime can create a nontrivial local reflected gate only on the exceptional residue branch

\[
\boxed{q^2\equiv-1\pmod p.}
\]

This has an immediate splitting consequence:

- if `p == 3 mod 4`, `-1` is not a quadratic residue, so every such new prime is automatically harmless for this local gate;
- if `p == 1 mod 4`, there are two exceptional residue classes `q == +/- i mod p`, and only those classes require deeper valuation/descent analysis.

Thus the moving reflected sieve is supported not on all primes of `Delta_-`, but only on the split Gaussian primes of `Delta_-` together with the prime `2` and overlap primes already present in the raw arithmetic.

## Relation to Stage14-s

Stage14-s4b/s5 shows that raw Kummer square classes are supported on moving first-face arithmetic primes and that a single-fiber point bound cannot control the number of activated bases. The correct raw-side next tool is a Pythagorean family 2-descent large sieve.

Stage14-t8 sharpens the triple version of that target. After raw activation, the extra reflected condition must be tested on

\[
\Delta_-=S^2-X^2,
\]

but odd inert primes `p == 3 mod 4` contribute no new obstruction through the reflected quartic. The only potentially useful new character conditions occur at split primes `p == 1 mod 4`, on the two residues `q^2 == -1 mod p`, plus the 2-adic and overlap-prime conditions.

This is a moving-prime sparse-residue sieve, not an independent fixed-prime-density sieve.

## What is still missing

To obtain a quantitative saving after raw activation one must control, uniformly over primitive Euclid parameters, how often the physical small point `q` lands in the exceptional residues at split prime divisors of `Delta_-`, while simultaneously satisfying the raw 2-descent class and height window.

A theorem of the desired shape would combine:

1. primitive Pythagorean/Euclid-parameter averaging;
2. the raw Stage14-s 2-descent/Kummer class;
3. split prime divisors `p | Delta_-`, `p == 1 mod 4`;
4. the exceptional congruences `q^2 == -1 mod p`;
5. the physical logarithmic small-point window.

No independence between prime divisors is assumed here.

## Locked boundary

```text
STAGE14_T8=COMPLETE_REFLECTED_MOVING_PRIME_LOCAL_BOUNDARY
REFLECTED_QUARTIC_REWRITE_LOCKED=true
REFLECTED_NEW_MOVING_FACTOR=Delta_minus=S^2-X^2
PAIR_BAD_SUPPORT_SUBSET=primes_dividing_2*S*X*H*Delta_minus
ODD_NEW_PRIME_LOCAL_GATE_AUTOMATIC_IF_Q2_PLUS_1_UNIT=true
INERT_DELTA_PRIMES_P_EQ_3_MOD_4_NEW_GATE_TRIVIAL=true
SPLIT_DELTA_PRIMES_P_EQ_1_MOD_4_EXCEPTIONAL_RESIDUES=q^2==-1_mod_p
FIXED_PRIME_INDEPENDENT_DENSITY_SAVING_PROVED=false
MOVING_SPLIT_PRIME_LARGE_SIEVE_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t9 Euclid-parameter split-prime exceptional-residue large-sieve target
```
