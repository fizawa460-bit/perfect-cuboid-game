# Stage35-EX 35EX-10B — exact split-prime obstruction

## Scope

Continue under the conditional E1-counterexample normal form through 35EX-09. Put

```text
D = U1/c,
T = U2/c,
K = (W1/p)*(V1/q).
```

For an odd prime `ell` not dividing the denominator of a displayed unit, write

```text
chi_ell(x) = Legendre symbol (x/ell).
```

This leaf derives a source-computable local obstruction for every split prime `ell = 1 mod 4` occurring in the live cross or difference reservoir. It also restricts the possible bridge reservoir `e`.

The result is conditional E1 exclusion for an individual Master-Hit; it is not a global proof of E1.

## 1. Branch L

Recall

```text
r^2-s^2 = (W1/p)*T,
u^2-v^2 = (V1/q)*T,
p*r*s   = q*u*v,
t = r*s/q = u*v/p,
gcd(t,T)=1.
```

### 1A. Split primes in the cross reservoir t

Let `ell = 1 mod 4` divide `t`. Then `ell` divides exactly one of `r,s` and exactly one of `u,v`, because both parameter pairs are primitive. Also `ell` does not divide `T`.

Therefore modulo `ell`

```text
r^2-s^2 = +/- square != 0,
u^2-v^2 = +/- square != 0.
```

Multiplying the two branch equations gives

```text
K*T^2 = +/- square.
```

Since `ell = 1 mod 4`, `-1` is a square modulo `ell`; since `T` is a unit, this forces

```text
chi_ell(K)=+1.                              (L-cross)
```

In particular `K` is automatically an `ell`-adic unit under this hypothesis.

### 1B. Split primes in the difference reservoir T

Let `ell = 1 mod 4` divide `T`. Because `gcd(t,T)=1`, all of `r,s,u,v` are nonzero modulo `ell`, while

```text
r^2 = s^2,
u^2 = v^2.
```

Write

```text
r = eps*s,
u = delta*v,
eps,delta in {+1,-1}.
```

The cross-equation gives

```text
eps*delta*(p/q) = (v/s)^2 mod ell.
```

For `ell = 1 mod 4`, both signs are quadratic residues. Hence

```text
chi_ell(p*q)=+1.                            (L-difference)
```

### 1C. Split primes in the bridge reservoir e

Every odd prime dividing

```text
e = gcd(c,H)
```

already satisfies `ell = 1 mod 4`, because it divides the primitive Pythagorean hypotenuse `H`.

Such an `ell` divides both primitive hypotenuses `w` and `H`, so for a chosen `i^2=-1 mod ell`

```text
r/s = eps*i,
u/v = delta*i
```

with `eps,delta=+/-1`. The same Branch-L cross-equation again yields

```text
eps*delta*(p/q) = square mod ell.
```

As `-1` is square, every prime of `e` obeys

```text
chi_ell(p*q)=+1.                            (L-bridge)
```

Thus the support of `e` is restricted to the split prime divisors of `c` on which `p*q` is a quadratic residue.

## 2. Branch R

Recall

```text
r^2-s^2 = (W1/p)*T,
2*u*v   = (V1/q)*T,
2*p*r*s = q*(u^2-v^2),
j = (u^2-v^2)/p = 2*r*s/q,
gcd(j,T)=1.
```

### 2A. Split primes in the cross reservoir j

Let `ell = 1 mod 4` divide `j`. Then `ell` divides exactly one of `r,s`, while

```text
u = +/- v != 0 mod ell.
```

Hence

```text
r^2-s^2 = +/- square,
2*u*v   = +/- 2*square.
```

Multiplication gives

```text
K*T^2 = +/- 2*square.
```

For a split prime the sign is square, so equivalently

```text
chi_ell(2*K)=+1.                            (R-cross)
```

### 2B. Split primes in the difference reservoir T

Let `ell = 1 mod 4` divide `T`. Then

```text
r = eps*s != 0 mod ell
```

and the Master even-leg equation forces exactly one of `u,v` to vanish modulo `ell`. Therefore

```text
u^2-v^2 = delta*z^2
```

with `delta=+/-1` and `z != 0`. The cross-equation becomes

```text
eps*delta*(2*p/q) = square mod ell.
```

Again both signs are squares, so

```text
chi_ell(2*p*q)=+1.                          (R-difference)
```

### 2C. Split primes in the bridge reservoir e

Let `ell|e`. Then `ell=1 mod 4` and

```text
r/s = eps*i,
u/v = delta*i,
i^2=-1 mod ell.
```

The Branch-R cross-equation gives

```text
2*p*eps*i*s^2 = -2*q*v^2,
```

hence `(-eps*i)*(p/q)` is a square. The signs are squares. For `ell=1 mod 4`, a square root `i` of `-1` is itself a square exactly when `ell=1 mod 8`; this is the same criterion as `chi_ell(2)=+1`. Therefore

```text
chi_ell(2*p*q)=+1.                          (R-bridge)
```

So in Branch R the support of `e` is restricted to split prime divisors of `c` on which `2*p*q` is a quadratic residue.

## 3. Source-only E1 kill predicate

The quantities

```text
c,p,q,D,T,K
```

are determined by the original Master-Hit before assuming E1 failure. The branch is also source-determined by comparing

```text
v2(V1), v2(V2).
```

The cross reservoir is source-determined as

```text
Branch L: t = D*V2/(2*p*q),
Branch R: j = D*V2/(p*q).
```

Therefore every Master-Hit has a rigorous source-only sufficient predicate for E1:

```text
Branch L is killed if
  exists ell|t, ell=1 mod4 with chi_ell(K)=-1,
  or exists ell|T, ell=1 mod4 with chi_ell(p*q)=-1.

Branch R is killed if
  exists ell|j, ell=1 mod4 with chi_ell(2*K)=-1,
  or exists ell|T, ell=1 mod4 with chi_ell(2*p*q)=-1.
```

If the predicate fires, that Master-Hit cannot be an E1 counterexample.

The bridge divisor `e` is not source-known because it depends on the hypothetical Master hypotenuse `H`, but its admissible prime support is simultaneously restricted by `(L-bridge)` or `(R-bridge)`.

## 4. What this proves and what remains

This is a genuine local obstruction, stronger than the 35EX-09 parity graph: some moving split primes are forbidden entirely rather than merely routed to one of two factor edges.

It does not prove that every Master-Hit contains a forbidden split prime. Inert primes `ell=3 mod4` retain a sign choice that routes them between the two allowed factor edges, and a Master-Hit can also have only locally admissible split primes.

Therefore

```text
SPLIT_PRIME_SOURCE_ONLY_KILL_PREDICATE_PROVED=true
UNIVERSAL_BAD_SPLIT_PRIME_EXISTENCE_PROVED=false
E1_PROVED=false
```

A global close would now require a theorem forcing at least one bad split prime in `t/j` or `T`, or a stronger reciprocity relation coupling the locally admissible primes. Without that extra theorem the split-prime route remains a partial but proof-capable per-Master-Hit sieve.
