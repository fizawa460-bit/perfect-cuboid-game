# Stage35-EX Goal4BU source lock — three source-known reservoirs and quadratic reciprocity boundary

Scope: consume exact-green Goal4BT and test whether correcting the bridge reservoir `e` to source-known closes E1 by a global quadratic-reciprocity relation. Mathematical authority remains V74 / Goal4AK. This is provisional research only.

## 1. Exact parent

Goal4BT is exact-green at

```text
head = d2a65383b141824321c6cc0bf6b594a59c03957c
aggregate = 34400316014
verify-stage35-ex-current = 102631709439
Goal4BT dedicated = 34400316042
Goal4BS checkpoint replay = 34400316012
```

Goal4BT proves that for every Master-Hit

```text
H = sqrt((V1*U2)^2+(U1*V2)^2)/(c*q),
e = gcd(c,H)
```

are source-computable before any E1-failure assumption.

## 2. All three reservoirs are source-computable

Use

```text
D=U1/c,
T=U2/c,
K=(W1/p)*(V1/q).
```

Under the E1-counterexample normal form, the cross reservoir is

```text
Branch L: t = D*V2/(2*p*q),
Branch R: j = D*V2/(p*q).
```

If the displayed quotient is not integral, that branch is already impossible. When integral, the three reservoir values

```text
cross, T, e
```

are determined from the Master-Hit alone.

They are pairwise coprime under a hypothetical counterexample. In fact the coprimality is visible directly from the primitive Master triple:

```text
A=(V1/q)*T,
B=D*(V2/q),
A^2+B^2=H^2,
gcd(A,B)=gcd(A,H)=gcd(B,H)=1.
```

`T|A`; in Branch L `B=2*p*t`, in Branch R `B=p*j`; and `e|H`. Hence

```text
gcd(cross,T)=gcd(cross,e)=gcd(T,e)=1.              (BU-COPRIME)
```

## 3. Complete source-only quadratic sieve

35EX-10/11 plus Goal4BT give the necessary split-prime conditions.

Branch L:

```text
ell|t, ell=1 mod4  => (K/ell)=+1,
ell|T, ell=1 mod4  => (p*q/ell)=+1,
odd ell|e           => ell=1 mod4 and (p*q/ell)=+1. (BU-L)
```

Branch R:

```text
ell|j, ell=1 mod4  => (2*K/ell)=+1,
ell|T, ell=1 mod4  => (2*p*q/ell)=+1,
odd ell|e           => ell=1 mod4 and (2*p*q/ell)=+1. (BU-R)
```

The numerators are not independent:

```text
K*(p*q)=W1*V1.                                      (BU-KP)
```

But this identity does not turn the three moving moduli into a fixed-support Jacobi product.

A composite Jacobi symbol over the split radical can compress several necessary `+1` tests, but it is weaker than the primewise predicate: two bad primes can cancel in a product symbol. Therefore no new exclusion credit comes merely from multiplying the local conditions.

## 4. Source witnesses against a universal bad-prime theorem

### Branch L

The Master-Hit

```text
(a,b,m,n)=(13,4,96,91)
```

gives

```text
(U1,V1,W1)=(153,104,185),
(U2,V2,W2)=(935,17472,17497),
c=17,p=1,q=104,
S=2674984,
H=1513,
e=17,
D=9,T=55,K=185,
t=756.
```

This is Branch L. The cross reservoir has no odd split prime. `5|T` is split and

```text
(p*q/5)=+1,
```

while `17|e` and

```text
(p*q/17)=+1.                                        (BU-WIT-L)
```

So all three source-channel split-prime tests are simultaneously admissible, with nontrivial `T` and `e` split primes.

### Branch R

The Master-Hit

```text
(a,b,m,n)=(88,7,98,37)
```

gives

```text
(U1,V1,W1)=(7695,1232,7793),
(U2,V2,W2)=(8235,7252,10973),
c=135,p=1,q=28,
S=56718900,
H=15005,
e=5,
D=57,T=61,K=342892,
j=14763.
```

This is Branch R. The split primes `37|j`, `61|T`, and `5|e` satisfy respectively

```text
(2*K/37)=+1,
(2*p*q/61)=+1,
(2*p*q/5)=+1.                                       (BU-WIT-R)
```

Thus even with a nontrivial split prime in every one of the three source-known channels, the separate quadratic predicates can all pass.

These witnesses do not assert E1 failure. They refute only the proposed source theorem that every Master-Hit must contain a bad split prime in the three source channels.

## 5. Reciprocity boundary

35EX-09's factorwise squareclass graph remains a direct product of primewise edge allocations:

```text
cross : 13 or 24,
T     : 14 or 23,
e     : 12 or 34.
```

For inert primes the 35EX-11 symbols orient the edge. For locally-good split primes the quadratic symbol is `+1` on both allowed orientations, so the edge bit survives.

Quadratic reciprocity can rewrite each Legendre symbol with numerator and denominator exchanged. It does not, from the retained identities, supply a fixed global product of the surviving orientation bits. The moduli `cross,T,e` are moving and pairwise coprime, and primes outside their support can enter any attempted global Hilbert/Jacobi product unless an additional support-cleaning identity is proved.

Therefore the exact current-layer verdict is

```text
THREE_SOURCE_KNOWN_RESERVOIRS=true
UNIVERSAL_BAD_SPLIT_PRIME_IN_TRIPLE=false
QUADRATIC_RECIPROCITY_UNIVERSAL_CLOSE=false
SURVIVING_SPLIT_ORIENTATION_BITS_COUPLED=false       (BU-VERDICT)
```

This is not a theorem that no stronger reciprocity argument exists. It freezes only the quadratic three-reservoir layer now made source-complete by Goal4BT.

## 6. Next leaf

Because `e` is now source-known and every odd `ell|e` is split, the genuinely new unresolved question is whether a **quartic** orientation at those bridge primes detects information lost by the quadratic predicate.

```text
35EX-35_GOAL4BV_SOURCE_KNOWN_BRIDGE_QUARTIC_ORIENTATION_PREFLIGHT
```

This must not simply recharge Goal4BF--BO: those leaves concern the later endpoint Gaussian reservoir system. Goal4BV must first prove that the early Pesch bridge prime carries a source-fixed quartic datum at all.

No merge. No hostile-audit credit. No E1, Stage35, endpoint, or Perfect Cuboid credit.
