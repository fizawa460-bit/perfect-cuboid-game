# Stage36 36-09DE prime-private Brauer family source lock

## Classical inputs

1. Dirichlet's theorem on primes in arithmetic progressions: if `gcd(a,m)=1`, there are infinitely many primes `q` with `q ≡ a (mod m)`. A convenient modern reference is MIT 18.785 Number Theory I, Lecture 18, Theorem 18.1 (Dirichlet 1837).
2. Quadratic reciprocity and the Legendre symbol multiplicativity. For odd primes `r,q` with `r ≡ 1 (mod 4)`, `(r/q)=(q/r)`.

These are existing classical theorems; this file grants no new-theorem credit.

## Fixed progression

Set

`M = 5*13*29*37*41 = 2859545`.

Since `gcd(17,M)=1`, Dirichlet gives infinitely many primes

`q ≡ 17 (mod M)`.

All five prime factors of `M` are `1 mod 4`. Hence quadratic reciprocity gives, for every such fresh prime `q`,

- `(5/q)=(17/5)=-1`,
- `(13/q)=(17/13)=+1`,
- `(29/q)=(17/29)=-1`,
- `(37/q)=(17/37)=-1`,
- `(41/q)=(17/41)=-1`.

## Stage36 fixed-point specialization

On

`C3_2: z^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`,

at `t=3` the right-hand side is

`19721 = 13*37*41`,

and at `t=4` it is

`1178125/9 = 5^5*13*29/3^2`,

so its squareclasses are respectively `13*37*41` and `5*13*29`. The character values above make both right-hand sides nonzero squares modulo every fresh `q ≡17 mod M`, hence Hensel lifting in `z` gives `Q_q` receiver points at both fixed `t` values.

For the Creutz--Viray class

`E_q=(q,t^2+4)_2`,

the second entries are `13` at `t=3` and `20=4*5` at `t=4`. Therefore

`(q,13)_q=+1`, while `(q,20)_q=-1`.

For any previously chosen class with first entry a different rational prime, both Hilbert entries are `q`-adic units at these two points, so its evaluation is zero there.

## Firewalls

This source lock supplies only the prime-production and local-character mechanism. It does not identify the resulting infinite explicit subgroup with the full Creutz--Viray image or the full Brauer group, does not prove adelic solubility, and does not by itself produce a Brauer--Manin obstruction or fixed-parameter exclusion.
