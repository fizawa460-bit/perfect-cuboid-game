# Stage36 36-09FE — forced-CRT factor-shape realization

## Purpose

36-09FD converted the fixed-quartic Frobenius condition into two explicit CRT branches for every good seed prime. FE asks the next narrower question from the FD source contract: are the remaining FB factor-shape conditions arithmetically compatible with those forced branches at all?

Entry authority is V294, exact head `cec3ff043efe72025ec6f9ee232c9f0bd6a7b1d1`, CI `34424593468 / 102707016628`. The exact fixed-parameter exclusion registry is 224. FD is exact-green consumed; no receiver, R29, Q11, endpoint, or Perfect Cuboid closure is available.

## Seed-17 forced branches

Keep

```text
K=729,
U0=17627,
M=34440,
u=U0+M*j,
P(u)=8u^2-K^2,
|Q(u)|=8u^2+8Ku+K^2.
```

FD proves that the good seed `p0=17` gives exactly the two branches

```text
j = 6 (mod 17),
j = 9 (mod 17),
```

and hence

```text
u = 224267 (mod 585480),
u = 327587 (mod 585480).
```

On either branch, any realization of the exact FB factor shape has `17` as one of the two `P1` factors. The FC/FD theorem then forces the retained splitting bit `B=-1`, so the factor-shape realization has support rank 22, Selmer dimension 2, and empty retained fixed-p physical receiver sector.

## Exact compatibility on both branches

The remaining factor-shape conditions are not incompatible with either CRT branch. Four already-promoted arithmetic realizations give two witnesses on each branch.

The `j=9 mod 17` branch is already present in the exact-green FA authority:

```text
j=1029,  u=35456387,
P/7 = 17 * 84514647329569,
|Q|/41 = 3911 * 62721466127;

j=19117, u=658407107,
P/7 = 17 * 29142851667095329,
|Q|/41 = 47 * 1799690289681191.
```

The `j=6 mod 17` branch is already present in the exact-green FB authority:

```text
j=47691, u=1642495667,
P/7 = 17 * 181364169150501409,
|Q|/41 = 120994711 * 4350592447;

j=73259, u=2523057587,
P/7 = 17 * 427954257970971169,
|Q|/41 = 4768607 * 260476801271.
```

For every displayed row, `u`, `2u+729`, and `4u+729` are prime; the two factors of `P/7` are distinct primes `1 mod 8`; the two factors of `|Q|/41` are distinct primes `7 mod 8`; and the two `P1` factors split as one `1 mod 3` and one `2 mod 3`. Thus these are literal realizations of the FB factor shape, not merely congruence candidates.

Therefore FE proves the finite compatibility statement

```text
both seed-17 forced CRT branches contain exact FB factor-shape realizations.
```

This removes a possible local/congruence incompatibility failure mode. It does not turn finite compatibility into an unbounded or infinite realization theorem.

## Additional exact diagnostics

A direct finite scan of the same two branches found two further exact factor-shape rows:

```text
j=156494 = 9 (mod 17), u=5389670987,
P/7 = 17 * 1952843922561982369,
|Q|/41 = 111558143 * 50807686679;

j=164634 = 6 (mod 17), u=5670012587,
P/7 = 17 * 2161280183982411169,
|Q|/41 = 7079 * 886139956936943.
```

The FE verifier checks these rows exactly, including deterministic primality of all displayed factors. They are retained only as diagnostic strengthening. FE does not use them to expand the fixed-parameter registry, and makes no disjointness credit against the full historical 224 registry.

## What FE changes

The route is now

```text
one-bit Selmer condition
 -> fixed quartic Frobenius type
 -> seed-prime CRT forcing
 -> exact factor-shape compatibility on both forced branches.
```

So the next obstruction is no longer existence of even one compatible row on a branch. What remains open is an unbounded control statement for the simultaneous primality / two-prime factor-shape requirements along a forced branch.

The next leaf is

```text
36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT.
```

## Credit firewall

FE does not prove infinitely many FB factor-shape realizations, positive density, simultaneous-primality infinitude, semiprime-factorization infinitude, or a sieve theorem. It does not claim the FB sign necessary, does not enlarge the exact fixed-parameter registry beyond 224, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
