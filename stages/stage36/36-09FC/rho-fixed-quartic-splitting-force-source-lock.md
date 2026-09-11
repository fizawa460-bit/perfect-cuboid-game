# Stage36 36-09FC — fixed quartic splitting realization of the FB one-bit condition

## Purpose

36-09FB reduced the retained factor-shape Selmer condition to the single quadratic sign

```text
B=(p1/e)=(p2/e)=-1.
```

FC removes the remaining `u`-dependent Legendre-symbol presentation. On the exact FB factor shape, the sign is equivalent to the factorization type of one fixed polynomial

```text
F(Y)=Y^4-2Y^2-1.
```

No bounded search is needed for this equivalence.

Entry authority is V290 at branch head `8eeb0d00448320beb0c1d39708919e76bbb01319`; the receipt-only exact-head CI is `34416716286 / 102683105148`. The exact fixed-p registry is 224, the exact full-template count is 17, the promoted partial-Legendre chart count is 3, and the promoted one-bit criterion count is 1.

## Exact FB factor-shape input

Retain

```text
K=729,
d=u,
e=4d+K,
P=8d^2-K^2=7p1p2,
```

with `e` prime `5 mod 8` and `p1,p2` distinct primes `1 mod 8`. FB proves

```text
(p1/e)=(p2/e)=B
```

and `B=-1` is sufficient for support-matrix rank `22=2n-2`, hence `dim_F2 Sel^2=2` and the retained fixed-p receiver exclusion.

Fix either `p in {p1,p2}`.

## From the arithmetic factor to a fixed square-root of 2

Because `p | P`,

```text
8d^2 = K^2 (mod p).
```

Since `p` does not divide `K`, define

```text
r = 4d/K (mod p).
```

Then

```text
r^2 = 16d^2/K^2 = 2 (mod p).
```

Also

```text
e/K = (4d+K)/K = 1+r (mod p).
```

As `K=27^2` is a rational square and `p=e=1 mod 4` after reducing the reciprocity sign (`p=1 mod 8`, `e=5 mod 8`), quadratic reciprocity gives

```text
B=(p/e)=(e/p)=(e/K mod p / p)=(1+r / p).
```

Thus the FB bit is the quadratic character of `1+r`, where `r^2=2`.

## Fixed quartic elimination

The equation

```text
y^2 = 1+r
```

implies

```text
(y^2-1)^2=r^2=2,
```

hence

```text
F(y)=y^4-2y^2-1=0.
```

Conversely, if `F(y)=0`, then

```text
(y^2-1)^2=2.
```

Therefore `y^2-1` is one of the two square roots `r,-r` of 2, so a root of `F` exists exactly when at least one of `1+r`, `1-r` is a square modulo `p`.

But `p=1 mod 8`, hence `-1` is a square modulo `p`, and

```text
(1+r)(1-r)=-1.
```

Consequently

```text
chi_p(1+r)=chi_p(1-r).
```

The two choices rise and fall together. Thus

```text
B=+1  <=>  F has a root mod p,
B=-1  <=>  F has no root mod p.
```

This equivalence is independent of which square root of 2 is called `r`.

## Exact splitting type

Over `F_p`, choose either `r` with `r^2=2`. Then

```text
F(Y)=(Y^2-(1+r))(Y^2-(1-r)).
```

For odd `p`, `F` is separable. Since the two quadratic characters are equal, there are only two factorization types on the retained `p=1 mod 8` support:

```text
B=+1 : (1,1,1,1), four linear factors;
B=-1 : (2,2), two irreducible quadratic factors.
```

Therefore the exact FB sufficient condition can be rewritten without any `e`-dependent Legendre notation:

```text
F(Y)=Y^4-2Y^2-1 has factorization type (2,2) modulo p1
```

or equivalently modulo `p2`.

## Fixed-quartic conditional theorem

On every arithmetic realization of the exact FB factor shape,

```text
F mod p1 has type (2,2)
```

implies

```text
B=-1
=> rank_F2 M = 22
=> dim_F2 Sel^2(E_rho,p/Q)=2
=> retained fixed-p physical receiver sector is empty.
```

The same statement holds with `p2`. Because FB already proves `(p1/e)=(p2/e)`, the two P-factors have the same fixed-quartic splitting type.

This is a global conditional theorem over the factor shape. It is not a density statement and does not assert existence of infinitely many arithmetic realizations.

## Exact replay

The four FB promotion witnesses

```text
u=1242922787,
u=1435649027,
u=1642495667,
u=2523057587
```

all have `B=-1`. For both P1 prime factors in each row, FC verifies directly that `r=4u/729` satisfies `r^2=2`, both `1+r` and `1-r` are nonsquares, and `F` has type `(2,2)`. No new orbit is added in FC; the exact registry remains 224.

## What FC changes

FC replaces the last moving Legendre-symbol condition by a fixed polynomial splitting condition. The route has now compressed

```text
full 45-bit pattern
  -> FA partial charts (6/9 bits)
  -> FB one arithmetic bit B
  -> FC one fixed quartic splitting type.
```

The next leaf is

```text
36-09FD_RHO_FIXED_QUARTIC_FROBENIUS_REALIZATION_PREFLIGHT.
```

Its purpose is to determine whether the required `(2,2)` Frobenius/splitting class can be forced in a parametric arithmetic construction compatible with the exact FB factor shape, rather than checked after factorization.

## Credit firewall

FC does not prove the `(2,2)` class occurs infinitely often among P-factors of the retained family, does not prove the FB condition necessary, does not classify all Selmer profiles, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
