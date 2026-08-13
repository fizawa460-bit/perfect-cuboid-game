# Stage14-t10 — reflected character-sieve direction audit

## Purpose

Stage14-t9 proposed realizing the t8 exceptional residues as character weights over primitive Euclid parameters. Before importing a large-sieve theorem, this stage checks the logical direction of that residue condition.

The check changes the next step materially: the sparse residues isolated in t8 are **not necessary conditions for a triple**. They are precisely the places where the easy local-square argument stops being automatic and a deeper local analysis is required.

No estimate for `T(B)` is asserted here.

## 1. Reflected local identity

The reflected quartic is

\[
R^2=(q^2+1)^2+4\frac{1-s}{s}q^2.
\]

Write the physical base as

\[
s=X^2/S^2,
\qquad
\Delta_-=S^2-X^2.
\]

Let `p` be an odd prime with `p|Delta_-` and suppose first that `q` is `p`-adically integral and

\[
q^2+1\not\equiv0\pmod p.
\]

Then `(q^2+1)^2` is a unit square and the correction term is divisible by `p`, so

\[
R^2=(q^2+1)^2(1+p\alpha)
\]

for some `alpha in Z_p`. Since `p` is odd, `1+p Z_p` consists of squares. Thus the reflected square condition is locally automatic at such a prime.

Therefore the condition

\[
q^2\equiv-1\pmod p
\]

marks the **failure of the automatic-solubility proof**, not a congruence that every triple must satisfy.

## 2. Exact sparse-support rewrite

Write a reduced rational point coordinate

\[
q=u/v,
\qquad \gcd(u,v)=1.
\]

For an odd prime `p` with `p\nmid v`,

\[
q^2\equiv-1\pmod p
\iff
u^2+v^2\equiv0\pmod p.
\]

Hence the t8 exceptional support away from denominator primes is exactly the odd-prime support of

\[
\gcd(\Delta_-,u^2+v^2).
\]

Moreover, if `p|u^2+v^2` with `p\nmid uv`, then `-1` is a quadratic residue mod `p`, so necessarily

\[
p\equiv1\pmod4.
\]

Thus the explicit `p=1 mod 4` condition is redundant on this primitive numerator support: it follows from the sum-of-two-squares congruence itself.

Denominator primes `p|v` are not included in this rewrite and must remain in the full raw/descent local bookkeeping.

## 3. Why the naive character sieve cannot give the desired saving

The exact exceptional indicator for integral `q mod p` can be written schematically as

\[
1_{p\mid\Delta_-}\,1_{p\mid u^2+v^2}.
\]

Equivalently, one may detect it with additive or quadratic-character expansions. But averaging this indicator can only bound the set where the easy local argument needs extra work.

It cannot upper-bound all triples by a sparse-residue set, because triples with

\[
\gcd(\Delta_-,u^2+v^2)=1
\]

are not excluded by t8; at every new integral reflected prime, they pass the local square test automatically.

Therefore the implication needed for a sieve saving is false:

```text
TRIPLE => EXISTS exceptional split prime
```

is **not proved** and is not supplied by t8/t9.

The valid implication is only

```text
NO exceptional prime at a given new integral p
=> reflected local square condition automatic at p.
```

This reverses the proposed use of the sparse residues.

## 4. Correct role of the exceptional-support character sum

The sparse-support sum is still useful, but only as an **error/exception decomposition**:

1. generic reflected local regime: `gcd(Delta_-,u^2+v^2)=1` away from denominator/raw bad primes, where the new reflected local tests are automatic;
2. exceptional reflected regime: common split divisors, where one needs deeper Hilbert-symbol / valuation analysis.

A large sieve can potentially show that regime (2) is small. That simplifies the global triple problem, but it does not by itself make triples sparse, because regime (1) remains admissible.

Consequently a proof of

\[
T(B)=o(\sqrt B)
\]

must obtain its main saving from the genuinely global simultaneous condition left by t6:

\[
\text{compatible small rational points on }E_+(s)\text{ and }E_+(-s),
\]

or equivalently from the full Humbert--Edge lift / shared-`q` height condition, not from the t8 exceptional primes alone.

## 5. Handoff to Stage14-s / main track

Stage14-s5a/s5b is deriving the actual raw full-2-descent character matrix on the five Euclid factors

```text
m, n, m-n, m+n, m^2+n^2.
```

That is a necessary raw-activation sieve. The t-side reflected exceptional support should be appended as a secondary local-error layer, not multiplied as an independent thinning factor.

The next t-stage should therefore return to the global double-small-point gate and formulate a **paired activation count**:

\[
V_{\pm}(B)
=
\#\{F:\ E_+(s_F)\text{ and }E_+(-s_F)\text{ admit compatible physical small points}\}.
\]

The desired transfer would be a theorem of the form

\[
V_{\pm}(B)=o(\sqrt B),
\]

or a comparison

\[
V_{\pm}(B)=o(V(B))
\]

combined with a raw `V(B)=B^{1/2+o(1)}` law.

## Locked boundary

```text
STAGE14_T10=COMPLETE_CHARACTER_SIEVE_DIRECTION_AUDIT
EXCEPTIONAL_RESIDUE_IS_TRIPLE_NECESSARY_CONDITION=false
EXCEPTIONAL_RESIDUE_MARKS_FAILURE_OF_AUTOMATIC_LOCAL_ARGUMENT=true
EXCEPTIONAL_SUPPORT_AWAY_FROM_DENOMINATORS=gcd(Delta_-,u^2+v^2)
SPLIT_PRIME_CONDITION_REDUNDANT_ON_PRIMITIVE_SUM_OF_TWO_SQUARES_SUPPORT=true
T9_INDEPENDENT_THINNING_INTERPRETATION_REJECTED=true
EXCEPTIONAL_SUPPORT_LARGE_SIEVE_USEFUL_AS_ERROR_CONTROL=true
MAIN_TRIPLE_SAVING_MUST_BE_GLOBAL_SIMULTANEOUS_SMALL_POINT_OR_LIFT_COMPATIBILITY=true
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t11 paired reflected activation count / global compatibility target
```
