# Stage35-EX 35EX-11 — reciprocity routing and exact local-route freeze

## Scope

Continue under the conditional E1-counterexample reductions through 35EX-10. Keep

```text
D = U1/c,
T = U2/c,
K = (W1/p)*(V1/q).
```

The goal of this leaf is exactly the 35EX-10 follow-up:

1. test whether every Master-Hit must contain a bad split prime in the source-known cross or difference reservoir;
2. test whether quadratic reciprocity couples the locally admissible reservoir primes strongly enough to force a contradiction.

The first statement is false as a statement about all Master-Hits. The second does not close at the current three-reservoir squareclass layer. What does close exactly is a prime-by-prime routing theorem: inert primes are oriented by the source Legendre symbols, while locally-good split primes retain a binary edge choice.

No E1 theorem or receiver credit is claimed.

## 1. Branch L: exact odd-prime routing

Recall

```text
t = r*s/q = u*v/p,
gcd(t,T)=1.
```

For an odd prime `ell`, put

```text
lambda_ell = (-1/ell).
```

### 1A. Cross reservoir t

If `ell|t`, then exactly one of `r,s` and exactly one of `u,v` vanishes modulo `ell`.

The two factor-edge reservoirs are

```text
t13 = gcd(r,v)*gcd(s,u),
t24 = gcd(r,u)*gcd(s,v)
```

at squarefree-prime level. The sign of

```text
(r^2-s^2)*(u^2-v^2) = K*T^2
```

is negative exactly on the `13` edge and positive exactly on the `24` edge. Therefore

```text
ell on t13  => (K/ell)=lambda_ell,
ell on t24  => (K/ell)=+1.                 (L-t-route)
```

Consequences:

- if `ell=3 mod4`, then `(K/ell)=-1` forces `t13` and `(K/ell)=+1` forces `t24`;
- if `ell=1 mod4`, both edge choices require `(K/ell)=+1`, reproducing the 35EX-10 split-prime kill predicate, but a locally-good split prime is not oriented by this symbol alone.

### 1B. Difference reservoir T

If `ell|T`, write

```text
r = eps*s,
u = delta*v,
eps,delta in {+1,-1} mod ell.
```

The `T`-edge is `23` when `eps*delta=+1` and `14` when `eps*delta=-1`. The cross equation gives

```text
(eps*delta)*(p/q) = square mod ell.
```

Hence

```text
ell on T23 => (p*q/ell)=+1,
ell on T14 => (p*q/ell)=lambda_ell.          (L-T-route)
```

Thus inert primes of `T` are source-oriented, while split primes survive only when `(p*q/ell)=+1` and then retain both edge choices.

### 1C. Bridge reservoir e

Every odd prime of

```text
e=gcd(c,H)
```

divides a primitive Pythagorean hypotenuse, hence is `1 mod4`. 35EX-10 gives the necessary condition

```text
(p*q/ell)=+1.
```

At this layer such a locally-good bridge prime can still choose between `e12` and `e34`; no inert bridge prime exists.

## 2. Branch R: exact odd-prime routing

Recall

```text
j = (u^2-v^2)/p = 2*r*s/q,
gcd(j,T)=1.
```

### 2A. Cross reservoir j

At squarefree-prime level the two cross edges are `j13` and `j24`. A direct sign check in

```text
(r^2-s^2)*(2*u*v) = K*T^2
```

gives

```text
ell on j13 => (2*K/ell)=+1,
ell on j24 => (2*K/ell)=lambda_ell.          (R-j-route)
```

So for `ell=3 mod4` the symbol uniquely orients the prime; for `ell=1 mod4`, local admissibility is exactly `(2*K/ell)=+1` and the edge remains ambiguous.

### 2B. Difference reservoir T

If `ell|T`, then `r=eps*s` while exactly one of `u,v` vanishes modulo `ell`. Tracking the two possibilities in

```text
2*p*r*s = q*(u^2-v^2)
```

gives

```text
ell on T14 => (2*p*q/ell)=+1,
ell on T23 => (2*p*q/ell)=lambda_ell.        (R-T-route)
```

Again inert primes are source-oriented; split primes survive only with symbol `+1` and retain both edge choices.

### 2C. Bridge reservoir e

Every odd prime of `e` is split and 35EX-10 gives

```text
(2*p*q/ell)=+1.
```

No inert bridge prime occurs, and the surviving split prime is not edge-oriented by this condition alone.

## 3. Exact source witness against universal bad-split-prime existence

The existing genuine Master-Hit regression tuple

```text
(a,b,m,n) = (4,3,16,5)
```

has

```text
(U1,V1,W1) = (7,24,25),
(U2,V2,W2) = (231,160,281),
c=7, p=5, q=8,
D=1, T=33, K=15,
branch=L,
t=2.
```

Therefore

```text
odd split primes in t: none,
odd split primes in T=3*11: none.
```

So the statement

> every Master-Hit contains a split prime in the source-known cross or difference reservoir

is false.

This witness is not an E1 counterexample; indeed no such claim is made. It refutes only the proposed source-only universal-bad-split-prime existence theorem.

The same witness also shows the inert routing is internally consistent:

```text
(40/3)=+1  -> 3 goes to T23,
(40/11)=-1 -> 11 goes to T14,
```

where `40=p*q` and `(-1/3)=(-1/11)=-1`. Moreover `e|c=7`, while every odd prime of `e` must be `1 mod4`, hence here necessarily `e=1` under a hypothetical counterexample. Thus the current local squareclass-routing rules themselves do not contradict this source configuration.

## 4. What quadratic reciprocity does and does not add here

The three reservoirs `cross`, `T`, and `e` are pairwise coprime. At squareclass level every odd prime is allocated independently to one of the two edges incident to its reservoir:

```text
cross : 13 or 24,
T     : 14 or 23,
e     : 12 or 34.
```

The formulas above do the following:

- inert primes (`3 mod4`) are uniquely oriented by a source Legendre symbol;
- bad split primes (`1 mod4`, symbol `-1`) are impossible;
- locally-good split primes (`1 mod4`, symbol `+1`) retain a binary edge choice.

Quadratic reciprocity may rewrite each symbol with numerator and denominator interchanged, but at the present layer this does not couple distinct reservoir primes: the factorwise squareclass theorem is a direct product of these primewise edge choices. There is no fixed modulus or fixed finite support set whose global Jacobi symbol is forced to be `-1`.

Therefore the exact legal conclusion is not that every possible reciprocity argument is impossible. It is narrower:

```text
CURRENT_THREE_RESERVOIR_LOCAL_SYMBOL_LAYER_GIVES_NO_GLOBAL_CONTRADICTION=true
UNIVERSAL_SOURCE_ONLY_BAD_SPLIT_PRIME_EXISTENCE=false
```

Any stronger reciprocity close must introduce an additional global relation among the source units or among the surviving split-prime orientation bits. That relation is not contained in 35EX-09/10.

## 5. Route decision

The local-valuation route has now reached its exact boundary:

```text
SOURCE_ONLY_SPLIT_PRIME_KILL_PREDICATE_PROVED=true
INERT_PRIME_EDGE_ROUTING_PROVED_CONDITIONALLY=true
UNIVERSAL_BAD_SPLIT_PRIME_EXISTENCE_PROVED=false
CURRENT_LOCAL_RECIPROCITY_COUPLING_CLOSE_PROVED=false
```

The roadmap's next unspent theorem species is the exact `E1-SUNIT-THUE` adapter test. The next legal leaf is therefore

```text
35EX-12_SUNIT_THUE_ADAPTER_OR_DYNAMIC_SUPPORT_BLOCKER
```

It must first determine whether the surviving prime-oriented factor equations can be converted into an S-unit/Thue-type equation with a genuinely fixed finite support. If the support remains source-dependent, freeze that route before any finite enumeration.

## Credit boundary

```text
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
