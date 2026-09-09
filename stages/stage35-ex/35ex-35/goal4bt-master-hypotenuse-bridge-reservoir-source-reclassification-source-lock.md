# Stage35-EX Goal4BT source lock — Master hypotenuse makes the bridge reservoir source-known

Scope: reopen the audited Goal4BS parking state only through gate `B. NEW_SOURCE_FIXED_E1_INVARIANT`. This leaf corrects one historical source-classification statement in 35EX-10/11. It does not alter the audited V74 / Goal4AK authority, does not self-award hostile-audit credit, and does not prove E1.

## 1. Exact retained source

Keep the 35EX-02 notation

```text
c = gcd(U1,U2),
p = gcd(W1,V2),
q = gcd(V1,V2),
h = gcd(V1*U2,U1*V2) = c*q.
```

A Master-Hit means, before any E1-counterexample assumption,

```text
M = (V1*U2)^2 + (U1*V2)^2 = S^2
```

for the unique positive integer `S=sqrt(M)`.

Divide by the exact gcd `h=c*q`. Then

```text
A = (V1/q)*(U2/c),
B = (U1/c)*(V2/q),
A^2+B^2 = H^2
```

with the unique positive integer

```text
H = S/(c*q).                                      (BT-SOURCE-H)
```

This is exactly the primitive Master hypotenuse later written `H=u^2+v^2` in 35EX-03/08. Its existence and numerical value use only the Master-Hit square, not hypothetical E1 failure.

Therefore

```text
e = gcd(c,H)                                      (BT-E)
```

is also a source-computable integer attached to every Master-Hit.

## 2. Historical correction

35EX-08 correctly defined `e=gcd(c,H)`. 35EX-10 then said:

```text
The bridge divisor e is not source-known because it depends on the hypothetical Master hypotenuse H.
```

The adjective `hypothetical` is too strong. The bridge identity involving the E1 hypotenuse `w` is conditional on E1 failure, but the Master hypotenuse `H` is already fixed by the Master-Hit. Thus only the *necessity* of the bridge residue conditions is conditional; the integer `e` on which they are tested is source-known.

35EX-11's local routing theorem remains mathematically valid after this correction. What changes is the operational classification of the `e`-channel: it is a third source-known sieve channel, not an unknown auxiliary reservoir.

## 3. Corrected source-only bridge sieve

Under hypothetical E1 failure, 35EX-10 proves for every odd prime `ell|e`:

Branch L (`v2(V1)<v2(V2)`):

```text
Legendre(p*q,ell)=+1.                              (BT-L)
```

Branch R (`v2(V1)>v2(V2)`):

```text
Legendre(2*p*q,ell)=+1.                            (BT-R)
```

The branch is source-known, and now `e` is source-known. Hence these become source-only sufficient E1 kill predicates:

```text
Branch L:
  if some odd ell|e has Legendre(p*q,ell)=-1,
  the Master-Hit cannot be an E1 counterexample.

Branch R:
  if some odd ell|e has Legendre(2*p*q,ell)=-1,
  the Master-Hit cannot be an E1 counterexample.
```

35EX-09 proves, under the counterexample normal form, that this bridge reservoir is pairwise coprime to the cross reservoir and `T`. Therefore it is genuinely a third channel in the three-reservoir graph.

## 4. Nonredundancy witness — Branch L

Take the genuine Master-Hit

```text
(a,b,m,n)=(13,2,32,13).
```

Then

```text
(U1,V1,W1)=(165,52,173),
(U2,V2,W2)=(855,832,1193),
c=15, p=1, q=52,
M=20822490000=144300^2,
H=144300/(15*52)=185,
e=gcd(15,185)=5.
```

This is Branch L because

```text
v2(V1)=2 < 6=v2(V2).
```

The old source-known channels are

```text
D=11,
T=57=3*19,
t=D*V2/(2*p*q)=88=2^3*11,
K=(W1/p)*(V1/q)=173.
```

There is no odd split prime (`1 mod 4`) in either `t` or `T`, so the old 35EX-10 cross/T split-prime predicate does not fire.

But the corrected bridge channel sees

```text
ell=5|e,
Legendre(p*q,5)=Legendre(52,5)=Legendre(2,5)=-1.   (BT-WIT-L)
```

Hence this Master-Hit is excluded from being an E1 counterexample by the corrected bridge sieve.

## 5. Nonredundancy witness — Branch R

Take

```text
(a,b,m,n)=(33,32,22,17).
```

Then

```text
(U1,V1,W1)=(65,2112,2113),
(U2,V2,W2)=(195,748,773),
c=65, p=1, q=44,
M=171976090000=414700^2,
H=414700/(65*44)=145,
e=gcd(65,145)=5.
```

This is Branch R because

```text
v2(V1)=6 > 2=v2(V2).
```

The old channels are

```text
D=1,
T=3,
j=D*V2/(p*q)=17,
K=(W1/p)*(V1/q)=101424.
```

The only old split prime is `17|j`, and

```text
Legendre(2*K,17)=+1,
```

so the old 35EX-10 split-prime predicate does not fire. There is no odd split prime in `T`.

The corrected bridge channel has

```text
ell=5|e,
Legendre(2*p*q,5)=Legendre(88,5)=Legendre(3,5)=-1. (BT-WIT-R)
```

so this Branch-R Master-Hit is likewise excluded from being an E1 counterexample only after the source-known `e` correction.

## 6. Reopen verdict

This is not merely a rephrasing of Goal4BS's historical `35EX-02..06` factor graph:

- `e` comes from the Master hypotenuse and the 35EX-08 bridge;
- the corrected predicate is source-evaluable before assuming E1;
- the two witnesses above show the `e` predicate can fire when the old source-known cross/T split-prime predicates do not.

Therefore the audited parking gate is legally reopened through

```text
REOPEN_GATE_B_TRIGGERED=true
NEW_SOURCE_FIXED_E1_INVARIANT=SOURCE_KNOWN_BRIDGE_RESERVOIR_RESIDUE_PROFILE
```

What is **not** proved:

```text
UNIVERSAL_BAD_BRIDGE_PRIME_EXISTENCE=false
UNIVERSAL_E1_PROOF=false
R29_PESCH_E1_CLOSED=false
STAGE35_CLOSED=false
```

## 7. Next leaf

```text
35EX-35_GOAL4BU_THREE_SOURCE_RESERVOIR_RECIPROCITY_COUPLING_PREFLIGHT
```

Question: once `cross`, `T`, and `e` are all source-known, does their pairwise-coprime three-reservoir graph force a global Jacobi/reciprocity relation or universal bad-prime condition that was unavailable under the historical classification of `e`?

No merge. No hostile-audit credit. Mathematical authority remains V74 / Goal4AK.
