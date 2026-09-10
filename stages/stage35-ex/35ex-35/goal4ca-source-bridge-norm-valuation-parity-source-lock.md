# Stage35-EX Goal4CA source lock — source bridge norm and odd-prime valuation parity sieve

Scope: consume exact-green Goal4BZ and prove the selected source bridge-norm valuation theorem. This leaf turns the Goal4BT source reclassification into a new per-Master-Hit E1 kill predicate at primes of `e`. It is a local sieve, not a universal E1 proof. Mathematical authority remains V74 / Goal4AK. No merge.

## 1. Exact parent

Goal4BZ is exact-green at

```text
head = aef846dcacb25ab22927b339fd990a68fa5203a6
Goal4BZ dedicated run = 34422872919 SUCCESS
```

Retain the Master-Hit source data

```text
c=gcd(U1,U2),
p=gcd(W1,V2),
q=gcd(V1,V2),
D=U1/c,
T=U2/c,
H=sqrt((V1*U2)^2+(U1*V2)^2)/(c*q),
e=gcd(c,H).
```

All of these are source-computable before any E1-counterexample assumption.

## 2. Exact source bridge norm is an equivalent E1 square receiver

Define

```text
X = q*H/e,
Y = c*D*T/e,
B_e = X^2+Y^2.                                      (CA-Be)
```

The Master square is

```text
(V1*U2)^2+(U1*V2)^2=(c*q*H)^2.
```

Using

```text
W1^2-V1^2=U1^2,
U1=c*D,
U2=c*T,
```

the raw E1 radicand satisfies the exact source identity

```text
F_E1
 := (W1*U2)^2+(U1*V2)^2
  = (c*q*H)^2+(U1*U2)^2
  = (c*q*H)^2+(c^2*D*T)^2
  = (c*e)^2*B_e.                                    (CA-scale)
```

Hence, for a Master-Hit,

```text
F_E1 is an integer square  iff  B_e is an integer square.  (CA-equiv)
```

Equivalently the canonically normalized E1 radicand differs from `B_e` by the rational square `(e/p)^2`. Since a positive integer which is a rational square is an integer square, no integrality gap occurs.

Thus `B_e` is globally endpoint-equivalent to the E1 square target. The new information in this leaf is not the reparameterization itself; it is the source-selected local prime family `ell|e` and the exact valuation structure there.

## 3. The bridge legs are source-coprime

The primitive Master triple gives

```text
A=(V1/q)*T,
B=D*(V2/q),
A^2+B^2=H^2,
gcd(A,H)=gcd(B,H)=1.
```

Therefore

```text
gcd(H,D)=gcd(H,T)=1.                                (CA-HDT)
```

Also the canonical gcd theorem gives

```text
gcd(q,c)=gcd(q,D)=gcd(q,T)=1.
```

Consequently

```text
gcd(q*H,c*D*T)=gcd(H,c)=e,
```

and after division by `e`,

```text
gcd(X,Y)=1.                                         (CA-coprime)
```

This is unconditional on the Master-Hit; no hypothetical E1 square has been used.

## 4. Exact valuation stratification at a bridge prime

Let `ell|e`. Since `c` is odd, every such `ell` is odd. Put

```text
k=v_ell(e)=min(v_ell(c),v_ell(H)),
c1=v_ell(c)-k,
h1=v_ell(H)-k.
```

By `(CA-HDT)` and the canonical coprimalities, `q,D,T` are `ell`-adic units. Hence exactly

```text
v_ell(X)=h1,
v_ell(Y)=c1,
min(c1,h1)=0.                                       (CA-XYval)
```

If

```text
v_ell(c) != v_ell(H),
```

then exactly one of `X,Y` is divisible by `ell` and the other is a unit. Therefore

```text
B_e=X^2+Y^2 is an ell-adic unit,
v_ell(B_e)=0.                                       (CA-unbalanced)
```

So positive bridge-norm valuation is possible only on the source-balanced stratum

```text
v_ell(c)=v_ell(H)=v_ell(e).                         (CA-balanced)
```

This sharply localizes the new sieve.

## 5. Balanced stratum: one-sided Hensel/Gaussian depth

Assume `(CA-balanced)`. Then `X,Y` are both units modulo `ell`.

If `ell` does not divide `B_e`, then `v_ell(B_e)=0`. Otherwise define the source-selected residue

```text
theta_0 = X*Y^(-1) mod ell.                         (CA-theta0)
```

Because `ell|X^2+Y^2`,

```text
theta_0^2=-1 mod ell.
```

Let `theta in Z_ell` be the unique Hensel lift satisfying

```text
theta^2=-1,
theta == theta_0 mod ell.                           (CA-theta)
```

The derivative `2*theta_0` is a unit, so the lift is unique. In `Z_ell`,

```text
B_e=(X-theta*Y)*(X+theta*Y).
```

The first factor is divisible by `ell` by construction, while

```text
X+theta*Y == 2*X != 0 mod ell.
```

Therefore exactly

```text
v_ell(B_e)=v_ell(X-theta*Y).                         (CA-depth)
```

Thus the full positive valuation is a source-fixed one-sided split-prime depth, not a free conjugation choice.

## 6. Source-only odd-valuation kill predicate

By `(CA-equiv)`, an E1 counterexample requires `B_e` to be a square. Hence every prime valuation of `B_e` must be even. In particular:

```text
if some ell|e has v_ell(B_e) odd,
then the Master-Hit cannot be an E1 counterexample.  (CA-kill)
```

Everything in `(CA-kill)` is source-computable. No hypothetical `r,s,u,v,w` is needed to evaluate the predicate.

This is strictly stronger than merely testing the Goal4BT quadratic bridge symbol on some Master-Hits.

## 7. Branch-L nonredundancy against Goal4BU

Take the genuine Master-Hit

```text
(a,b,m,n)=(13,4,96,91).
```

Then

```text
(U1,V1,W1)=(153,104,185),
(U2,V2,W2)=(935,17472,17497),
c=17,p=1,q=104,
H=1513,e=17,D=9,T=55,
branch=L.
```

The source reservoirs are

```text
t=756,
T=55,
e=17.
```

There is no split prime in `t`; `5|T` satisfies

```text
(p*q/5)=+1,
```

and the bridge prime satisfies

```text
(p*q/17)=+1.
```

So the Goal4BU three-channel quadratic sieve is fully admissible. But

```text
X=9256,
Y=495,
B_e=85918561,
v_17(B_e)=1.                                        (CA-WIT-L)
```

Therefore Goal4CA kills this hit although Goal4BU does not.

## 8. Branch-R nonredundancy against Goal4BU

Take the genuine Master-Hit

```text
(a,b,m,n)=(96,91,28,27).
```

Then

```text
(U1,V1,W1)=(935,17472,17497),
(U2,V2,W2)=(55,1512,1513),
c=55,p=1,q=168,
H=185,e=5,D=17,T=1,
branch=R.
```

The cross reservoir is

```text
j=D*V2/(p*q)=153=3^2*17.
```

Its only split prime satisfies

```text
(2*K/17)=+1,
K=(W1/p)*(V1/q)=1819688.
```

There is no split prime in `T=1`, and the bridge prime satisfies

```text
(2*p*q/5)=+1.
```

Thus the Goal4BU quadratic sieve again passes. But

```text
X=6216,
Y=187,
B_e=38673625,
v_5(B_e)=3.                                         (CA-WIT-R)
```

So Goal4CA also contributes genuinely new Branch-R pruning.

## 9. Parity alone is not universal

Goal4BU's genuine Branch-R witness

```text
(a,b,m,n)=(88,7,98,37)
```

has

```text
c=135,p=1,q=28,H=15005,e=5,D=57,T=61,
X=84028,
Y=93879,
B_e=15873971425,
v_5(B_e)=2.                                         (CA-even-survivor)
```

Its quadratic cross/T/e tests all pass, and the bridge valuation parity also passes. Therefore

```text
UNIVERSAL_ODD_VALUATION_AT_e=false.                 (CA-no-universal)
```

However after removing `5^2`, the remaining 5-adic unit is a quadratic nonresidue. Thus parity is not the full local square test and immediately exposes the next unspent source layer.

## 10. Verdict and next leaf

Certified provisionally:

```text
SOURCE_BRIDGE_NORM_B_e_EXPLICIT=true
E1_SQUARE_IFF_B_e_SQUARE=true
SOURCE_BRIDGE_LEGS_COPRIME=true
UNBALANCED_e_PRIME_HAS_V_Be_ZERO=true
BALANCED_POSITIVE_DEPTH_ONE_SIDED_HENSEL=true
SOURCE_ONLY_ODD_VALUATION_KILL_PREDICATE=true
BRANCH_L_NONREDUNDANT_VS_GOAL4BU=true
BRANCH_R_NONREDUNDANT_VS_GOAL4BU=true
UNIVERSAL_ODD_VALUATION_AT_e=false
E1_PROVED=false
STAGE35_CLOSED=false
```

The next exact leaf is

```text
35EX-35_GOAL4CB_SOURCE_BRIDGE_NORM_LOCAL_UNIT_SQUARECLASS_PREFLIGHT
```

Question: after the exact valuation is even, does the `ell`-adic unit of `B_e` supply a further source-only quadratic local-square obstruction, and how much of the Goal4BU survivor population does it remove? Freeze the result as a local sieve; do not infer a universal E1 theorem from bounded evidence.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.