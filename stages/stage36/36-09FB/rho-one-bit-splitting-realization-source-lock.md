# Stage36 36-09FB — one-bit arithmetic realization of the partial-Legendre route

## Purpose

36-09FA replaces full pattern hashes by exact partial-Legendre leaf charts on one fixed coarse support type. FB now uses the arithmetic relations among the factors of `P` and `Q` to collapse those chart conditions further. On the retained factor shape, the six conditions of Chart A and a second six-condition leaf chart reduce to one genuinely variable quadratic splitting bit.

Entry authority is V288, exact head `7c3cfca4eb2f84d71621099c16dd58c7e7212802`, CI `34415780996 / 102680229625`. The exact fixed-p registry on entry is 208; the exact full-template count is 17 and the promoted FA partial-chart count is 2.

## Arithmetic factor shape

Keep

```text
K=729=3^6,
u=17627 (mod 34440),
d=u,
f=2u+K,
e=4u+K,
P=8u^2-K^2,
|Q|=8u^2+8Ku+K^2.
```

Assume the exact factor shape

```text
d=u                 prime, d=3 (mod 8),
f=2u+729            prime, f=7 (mod 8),
e=4u+729            prime, e=5 (mod 8),
P=7 p1 p2,           p1,p2 distinct primes =1 (mod 8),
|Q|=41 q1 q2,        q1,q2 distinct primes =7 (mod 8).
```

All displayed primes are distinct. Since `u=2 mod 3`,

```text
s=P/7=p1 p2 =2 (mod 3).
```

Thus exactly one P1-factor is `2 mod 3` and the other is `1 mod 3`; label them

```text
p1=2 (mod 3),
p2=1 (mod 3).
```

Use the FA bit convention `chi_r(x)=0` for Legendre `+1`, `1` for Legendre `-1`.

## Forced reciprocity identities

The progression and factor equations force the following identities; they are not extra hypotheses.

### P-factors against d

Modulo `d`,

```text
7 p1 p2 = P = -K^2.
```

Also `d=1 mod 7` and `d=3 mod 4`, hence by quadratic reciprocity

```text
(7/d)=-(d/7)=-1,
(-1/d)=-1.
```

Therefore

```text
(p1/d)(p2/d)=+1,
```

so

```text
(p1/d)=(p2/d)=: A.
```

The CRT progression also gives `d=38 mod 41`. Since `41=1 mod 4` and `(38/41)=-1`,

```text
(41/d)=-1.
```

### P-factors against e

Modulo `e=4d+K`,

```text
P = -K^2/2.
```

Here `e=5 mod 8`, `e=5 mod 7`, so

```text
(-2/e)=-1,
(7/e)=(e/7)=(5/7)=-1.
```

Consequently

```text
(p1/e)(p2/e)=+1,
```

and hence

```text
(p1/e)=(p2/e)=: B.
```

This common sign `B` is the only splitting bit retained by the FB sufficient criterion.

### P-factors against f

First, `f=7 mod 8` and `f=3 mod 7`, hence

```text
(7/f)=-(f/7)=+1.
```

Also `f=26 mod 41`, so

```text
(41/f)=(26/41)=-1.
```

For either `p in {p1,p2}`, the congruence `p|P` gives `8d^2=K^2 mod p`. Cross-multiplying yields

```text
e/f = K/(2d)   (mod p).
```

Thus

```text
d e f = (K/2) f^2   (mod p).
```

Because `p=1 mod 8`, both `K=27^2` and `2` are quadratic residues modulo p. Therefore `d e f` is a square modulo p, and quadratic reciprocity gives

```text
(p/f)=(p/d)(p/e).
```

In particular

```text
(p1/f)=(p2/f)=A B.
```

These identities are exact and explain why the larger FA charts contain redundant conditions when restricted to the arithmetic factor shape.

## Two leaf charts covering both A-signs when B=-1

### Case A=+1

If

```text
B=(p1/e)=(p2/e)=-1
```

and `A=+1`, then the promoted FA Chart A holds automatically:

```text
chi_3(p1)=1,
chi_3(p2)=0,
chi_d(p1)=0,
chi_d(p2)=0,
chi_d(41)=1,
chi_e(p2)=1.
```

Hence the 24x24 support matrix has 22 legal leaf pivots, residual core `0_2`, rank 22, and Sel2 dimension 2.

### Case A=-1

A second exact leaf trace, represented by `u=1642495667`, has symbolic RREF

```text
chi_3(p1)=1,
chi_3(p2)=0,
chi_d(p2)=1,
chi_f(p1)=0,
chi_f(p2)=0,
chi_f(41)=1.
```

Call this Chart C. As in FA, every unlisted reciprocity bit is a don't-care variable: the six displayed equations alone preserve 22 legal rank-one leaf eliminations and the residual zero 2-core.

When `A=-1` and `B=-1`, all six Chart-C conditions are forced by the identities above:

```text
(p2/d)=A=-1,
(p1/f)=(p2/f)=AB=+1,
(41/f)=-1,
```

with the two mod-3 conditions automatic from the labeling.

Therefore Chart C covers the entire `A=-1, B=-1` branch.

## One-bit conditional theorem

The two cases exhaust `A in {+1,-1}`. Thus on the displayed factor shape,

```text
(p1/e)=-1
```

alone is sufficient for

```text
rank_F2 M = 22 = 2n-2,
dim_F2 Sel^2(E_rho,p/Q)=2.
```

Equivalently one may use `(p2/e)=-1`, because the two signs are forced equal.

This theorem is global over all arithmetic realizations of the stated factor shape; it is not restricted to a bounded search box. It is nevertheless conditional on that factor shape and on the one splitting sign. It does not assert that infinitely many such realizations exist.

The EH no-4/no-3 conditions remain uniform from FA on the progression, so every actual factor-shape realization with `B=-1` has empty retained physical receiver sector and its complete positive EK literal orbit is excluded.

## New exact realizations

Four realizations outside the exact 208-value registry are retained to witness both `A` signs and both observed `q/f` signs:

```text
j=36089, u=1242922787, A=+1, B=-1
j=41685, u=1435649027, A=+1, B=-1
j=47691, u=1642495667, A=-1, B=-1
j=73259, u=2523057587, A=-1, B=-1
```

Their factor data are locked in the FB certificate. All four have the stated 1+1+1+2+2 factor shape, rank 22, residual nullity 2, uniform EH clearance, and disjoint four-point literal orbits. After exact-head CI consumption the fixed-p registry may move

```text
208 -> 224.
```

The witnesses came from a targeted finite scan. The scan is not promoted as exhaustive or as density/infinitude evidence.

## Diagnostic only: the opposite sign

A finite diagnostic over the first `200000` progression indices found 43 realizations of the exact factor shape. In that diagnostic set:

```text
B=-1 : 25/25 had rank 22,
B=+1 : 18/18 had rank 20.
```

Only the `B=-1 => rank 22` direction is promoted, because it is proved symbolically by the two leaf charts. The `B=+1` observation is not promoted to a necessary condition or global rank-20 theorem.

## Next leaf

```text
36-09FC_RHO_ONE_BIT_SPLITTING_FORCE_PREFLIGHT
```

The next question is whether the single condition `(p1/e)=-1` can itself be forced by a fixed congruence/norm/splitting construction, rather than checked after factoring `P/7`.

## Credit firewall

FB does not prove infinitely many factor-shape realizations, does not prove the one-bit condition necessary, does not classify all residual cores or maximal-rank profiles, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
