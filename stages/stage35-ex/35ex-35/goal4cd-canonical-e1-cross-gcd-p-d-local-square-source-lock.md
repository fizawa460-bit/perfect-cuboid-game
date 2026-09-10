# Stage35-EX Goal4CD source lock — complete local-square sieve on the canonical E1 cross-gcd pair p/d

Scope: consume exact-green Goal4CC and prove the selected source-only local theorem on

```text
p=gcd(W1,V2),
d=gcd(V1,W2).
```

For every odd prime in either canonical cross gcd, the local E1-square condition is automatic off one balanced valuation stratum and is completely decided on that stratum by valuation parity plus a residual unit Legendre bit. The joint `p/d/e` source-selected local family gives new per-Master-Hit pruning but is not universal. Mathematical authority remains V74 / Goal4AK. No merge.

## 1. Exact parent

Goal4CC is exact-green at

```text
head = e56cec5b587f21ad905008536065c9d809e56e98
Goal4CC run = 34424751268 SUCCESS
Goal4CC job = 102707479471 SUCCESS
```

Keep the two exact raw presentations of the same E1 radicand

```text
F_E1=(W1*U2)^2+(U1*V2)^2,                           (CD-Fp)
F_E1=(U1*W2)^2+(V1*U2)^2.                           (CD-Fd)
```

Goal4CA gives

```text
F_E1=(c*e)^2*B_e,
B_e=(q*H/e)^2+(c*D*T/e)^2.                          (CD-Be)
```

The canonical gcd facts are

```text
p=gcd(W1,V2),
d=gcd(V1,W2),
c,p,d pairwise coprime,
p,d odd,
e|c.                                                (CD-gcd)
```

Thus every prime of `p*d` is a unit for the square scaling factor `(c*e)^2`.

## 2. Complete p-prime theorem

Fix an odd prime `ell|p`. Put

```text
a=v_ell(W1),
b=v_ell(V2),
k=min(a,b)=v_ell(p).
```

Primitivity gives

```text
ell∤U1,
ell∤U2.
```

### 2.1 Unbalanced p-primes are automatically locally square

If `a<b`, then the first summand of `(CD-Fp)` has strictly smaller valuation, so

```text
v_ell(B_e)=2*a=2*k
```

and after removing `ell^(2k)` the residual unit is congruent modulo `ell` to

```text
((W1/ell^k)*U2/(c*e))^2.
```

If `b<a`, the same argument gives the square unit

```text
(U1*(V2/ell^k)/(c*e))^2.
```

Hence

```text
v_ell(W1) != v_ell(V2)
=> B_e is a square in Q_ell.                         (CD-p-unbalanced)
```

### 2.2 Balanced p-primes carry the complete local bit

Only when

```text
v_ell(W1)=v_ell(V2)=k                              (CD-p-balanced)
```

can cancellation occur. Define the source-reduced norm

```text
R_p,ell
 = ((W1/ell^k)*U2)^2
 + (U1*(V2/ell^k))^2.                               (CD-Rp)
```

Then exactly

```text
B_e = ell^(2k) * R_p,ell / (c*e)^2.                 (CD-p-scale)
```

Since both removed factors are rational squares in `Q_ell`,

```text
B_e in Q_ell^{*2} iff R_p,ell in Q_ell^{*2}.        (CD-p-equiv)
```

For

```text
r=v_ell(R_p,ell),
U=R_p,ell/ell^r,
```

the complete odd-prime criterion is

```text
r even and Legendre(U,ell)=+1.                      (CD-p-local)
```

Everything is source-computable from the Master-Hit.

## 3. Complete d-prime theorem

Fix an odd prime `ell|d`. Put

```text
a'=v_ell(V1),
b'=v_ell(W2),
k'=min(a',b')=v_ell(d).
```

Primitivity gives `ell∤U1*U2`. Using `(CD-Fd)`, the identical valuation argument proves

```text
v_ell(V1) != v_ell(W2)
=> B_e is a square in Q_ell.                         (CD-d-unbalanced)
```

Only the balanced stratum

```text
v_ell(V1)=v_ell(W2)=k'                              (CD-d-balanced)
```

is nontrivial. Define

```text
R_d,ell
 = (U1*(W2/ell^k'))^2
 + ((V1/ell^k')*U2)^2.                              (CD-Rd)
```

Then

```text
B_e = ell^(2k') * R_d,ell / (c*e)^2,                (CD-d-scale)
```

so `B_e` is a square in `Q_ell` iff `R_d,ell` is. Again the exact test is even valuation plus square residual unit.

This is the index-swap companion of the `p` theorem, but on an ordered Master-Hit it supplies a distinct source-prime family because `gcd(p,d)=1`.

## 4. Source-only joint kill predicate

Combining Goal4CB with the present theorem gives three pairwise source-selected families:

```text
e-primes: complete local test from Goal4CA/CB,
p-primes: complete local test from Goal4CD §2,
d-primes: complete local test from Goal4CD §3.       (CD-three)
```

If any one of these local tests fails, the Master-Hit cannot be an E1 counterexample.

This is stronger than Goal4BU's Legendre routing because the present tests are the complete local square conditions for the actual E1 radicand at the selected primes.

## 5. p-family nonredundancy after the bridge route

Take the genuine Master-Hit

```text
(a,b,m,n)=(9,8,6,5).
```

Then

```text
(U1,V1,W1)=(17,144,145),
(U2,V2,W2)=(11,60,61),
c=1,p=5,q=12,H=157,e=1,D=17,T=11,
B_e=3584425.
```

The bridge family is empty. At `ell=5`,

```text
v_5(W1)=v_5(V2)=1,
R_p,5=(29*11)^2+(17*12)^2=143377,
R_p,5 == 2 mod5.
```

Hence

```text
v_5(B_e)=2,
(B_e/5^2 mod5)=2,
(2/5)=-1.                                           (CD-p-witness)
```

The `p` local test kills the hit even though valuation parity alone passes.

## 6. d-family nonredundancy after p/e

Take the genuine Master-Hit

```text
(a,b,m,n)=(17,10,97,88).
```

Then

```text
(U1,V1,W1)=(189,340,389),
(U2,V2,W2)=(1665,17072,17153),
c=9,p=1,q=4,H=90997,e=1,D=21,T=185,
d=17,
B_e=133709815369.
```

At `ell=17`,

```text
v_17(V1)=v_17(W2)=1,
v_17(B_e)=3.                                         (CD-d-witness)
```

Thus the `d` family kills while both `p` and `e` families are empty.

## 7. Balanced p-primes can also survive

The genuine Master-Hit

```text
(a,b,m,n)=(41,16,118,91)
```

has

```text
p=13,d=1,e=1,
v_13(W1)=v_13(V2)=1,
B_e=325034658169,
v_13(B_e)=2,
(B_e/13^2) mod13=4.                                 (CD-p-balanced-survivor)
```

So even the balanced `p` stratum is not automatically bad.

## 8. The joint p/d/e source-local family is not universal

The classical genuine Master-Hit

```text
(a,b,m,n)=(4,3,16,5)
```

has

```text
c=7,p=5,d=1,q=8,H=101,e=1,D=1,T=33,
B_e=706225=5^2*13*41*53.
```

At the only selected prime `5`,

```text
v_5(W1)=2,
v_5(V2)=1,
```

so the `p` prime is unbalanced and therefore automatically locally square:

```text
v_5(B_e)=2,
(B_e/5^2) mod5=4.                                   (CD-joint-survivor)
```

There are no `d` or `e` primes. Hence every source-selected `p/d/e` local test passes, but `B_e` is not a square because the fresh norm primes `13,41,53` occur to odd exponent.

Therefore

```text
UNIVERSAL_BAD_PRIME_IN_P_D_E=false.                 (CD-no-universal)
```

## 9. Exact boundary and next leaf

Goal4CD completes the ordinary local-square test on every canonical cancellation family currently distinguished by the two E1 norm orientations and the Master bridge:

```text
CANONICAL_SOURCE_GCD_LOCAL_FAMILY_COMPLETE=true.
```

The remaining odd-exponent primes of a nonsquare `B_e` may lie entirely outside `p*d*e`, as `(CD-joint-survivor)` shows. Merely factoring those fresh norm primes is endpoint-equivalent to testing `B_e` square and inherits the dynamic-support blocker of 35EX-12.

The next legal action is therefore another fresh breadth audit, now with the exact fact that `e`, `p`, and `d` have all been exhausted as complete local-square source families:

```text
35EX-35_GOAL4CE_POST_CANONICAL_GCD_LOCAL_COMPLETION_FRESH_ROUTE_AUDIT
```

## 10. Verdict

Certified provisionally:

```text
P_UNBALANCED_LOCAL_SQUARE_AUTOMATIC=true
P_BALANCED_COMPLETE_LOCAL_TEST=true
D_UNBALANCED_LOCAL_SQUARE_AUTOMATIC=true
D_BALANCED_COMPLETE_LOCAL_TEST=true
P_FAMILY_NONREDUNDANT_AFTER_BRIDGE=true
D_FAMILY_NONREDUNDANT_AFTER_P_E=true
BALANCED_P_SURVIVORS_EXIST=true
UNIVERSAL_BAD_PRIME_IN_P_D_E=false
CANONICAL_SOURCE_GCD_LOCAL_FAMILY_COMPLETE=true
E1_PROVED=false
STAGE35_CLOSED=false
```

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
