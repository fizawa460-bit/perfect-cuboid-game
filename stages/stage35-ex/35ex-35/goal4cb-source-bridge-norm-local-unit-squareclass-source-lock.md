# Stage35-EX Goal4CB source lock — complete odd bridge-prime local square test

Scope: consume exact-green Goal4CA and spend the remaining local unit layer of the source bridge norm `B_e`. For every odd bridge prime `ell|e`, this leaf gives the complete `Q_ell`-square criterion: valuation parity plus the residual unit Legendre class. It yields a further source-only per-Master-Hit E1 kill predicate, but does not prove that some bridge prime always kills. Mathematical authority remains V74 / Goal4AK. No merge.

## 1. Exact parent

Goal4CA is exact-green at

```text
head = 766f3d432ee9099eb15d2cebe2c481ea7a293532
Goal4CA dedicated run = 34423996853 SUCCESS
```

Retain

```text
X=q*H/e,
Y=c*D*T/e,
B_e=X^2+Y^2,
gcd(X,Y)=1,
F_E1=(c*e)^2*B_e.
```

Thus an E1 counterexample requires `B_e` to be an integer square.

## 2. Complete odd-prime local square criterion

Fix an odd prime `ell|e`. Put

```text
d_ell = v_ell(B_e),
U_ell = B_e / ell^d_ell.                         (CB-unit)
```

Then `U_ell` is an `ell`-adic unit. For odd `ell`, the standard Hensel square criterion is

```text
B_e in Q_ell^{*2}
iff d_ell is even and Legendre(U_ell,ell)=+1.      (CB-local)
```

Indeed a square has even valuation and square residue after removing that valuation. Conversely, if the valuation is even and the unit residue is a square modulo `ell`, a square root of the unit lifts uniquely because the derivative of `z^2-U_ell` is a unit at a nonzero root modulo `ell`.

Therefore the source-only bridge-prime kill predicate is exactly

```text
if some ell|e satisfies
  d_ell odd
or
  d_ell even and Legendre(U_ell,ell)=-1,
then the Master-Hit cannot be an E1 counterexample. (CB-kill)
```

Goal4CA is the odd-valuation half. Goal4CB adds the missing even-valuation unit half.

## 3. Unbalanced bridge primes are automatically locally square

Goal4CA proves that if

```text
v_ell(c) != v_ell(H),
```

then exactly one of `X,Y` is divisible by `ell`, the other is a unit, and

```text
d_ell=0.
```

Moreover

```text
B_e == X^2 mod ell
```

or

```text
B_e == Y^2 mod ell,
```

with the displayed nonzero term a unit. Hence

```text
Legendre(U_ell,ell)=+1.                            (CB-unbalanced)
```

So **no unbalanced bridge prime can fire either half of the complete local test**. All bridge-prime pruning is confined to the source-balanced stratum

```text
v_ell(c)=v_ell(H)=v_ell(e).                        (CB-balanced)
```

This strengthens Goal4CA's localization statement.

## 4. Balanced stratum and finite Hensel evaluation of the unit bit

Assume `(CB-balanced)`. Then `X,Y` are `ell`-adic units.

If `d_ell=0`, the remaining bit is simply

```text
Legendre(B_e,ell).                                  (CB-depth0)
```

If `d_ell>0`, Goal4CA supplies the source-selected Hensel root `theta` of `-1` satisfying

```text
theta == X/Y mod ell,
theta^2=-1.
```

The factorization

```text
B_e=(X-theta*Y)*(X+theta*Y)
```

has

```text
v_ell(X-theta*Y)=d_ell,
v_ell(X+theta*Y)=0.
```

For a finite source computation, lift `theta` only modulo `ell^(d_ell+1)` and put

```text
C_ell = (X-theta*Y)/ell^d_ell mod ell.              (CB-C)
```

Then `C_ell` is nonzero modulo `ell` and

```text
U_ell == C_ell*(X+theta*Y)
      == C_ell*(2*X) mod ell.                       (CB-unit-factor)
```

Thus the residual local-square bit is finite, canonical, and source-computable; it is not another free Gaussian conjugation choice.

## 5. Branch-L nonredundancy after Goal4CA parity

Take the genuine Master-Hit

```text
(a,b,m,n)=(22,17,33,32).
```

Its source data are

```text
c=65,p=1,q=44,H=145,e=5,D=3,T=1,
branch=L,
X=1276,
Y=39,
B_e=1629697.
```

The Goal4BU quadratic channels all pass. At the bridge prime

```text
v_5(c)=v_5(H)=1,
v_5(B_e)=0,
U_5 == B_e == 2 mod5,
(2/5)=-1.                                           (CB-WIT-L)
```

Hence Goal4CA parity does not fire, but Goal4CB kills this hit.

## 6. Branch-R positive-even-depth nonredundancy

Use the Goal4CA even survivor

```text
(a,b,m,n)=(88,7,98,37).
```

Here

```text
c=135,p=1,q=28,H=15005,e=5,D=57,T=61,
branch=R,
X=84028,
Y=93879,
B_e=15873971425.
```

The Goal4BU quadratic channels pass and Goal4CA parity passes because

```text
v_5(B_e)=2.
```

But after removing the even valuation,

```text
U_5=B_e/5^2,
U_5 == 2 mod5,
(2/5)=-1.                                           (CB-WIT-R)
```

So Goal4CB adds genuine pruning even at positive even Hensel depth.

## 7. The complete bridge-prime local test is not universal

Take the genuine Master-Hit

```text
(a,b,m,n)=(24,1,18,7).
```

It has

```text
c=25,p=1,q=12,H=485,e=5,D=23,T=11,
branch=R,
X=1164,
Y=1265,
B_e=2955121.
```

The Goal4BU quadratic channels pass. At `ell=5`,

```text
v_5(c)=2,
v_5(H)=1,
```

so the bridge prime is unbalanced. Accordingly

```text
v_5(B_e)=0,
B_e == 1 mod5,
Legendre(B_e,5)=+1.                                 (CB-survivor)
```

Thus the **complete** local square test at every prime of `e` passes, while

```text
B_e=13*53*4289
```

is not a square. Therefore

```text
UNIVERSAL_BAD_LOCAL_SQUARE_PRIME_IN_e=false.        (CB-no-universal)
```

The failure occurs at primes outside the distinguished bridge support. Simply testing all prime divisors of `B_e` would be the original E1 square problem again, not a new source reduction.

## 8. Route boundary

Goal4CA+CB completely exhaust the ordinary odd-prime `Q_ell` square condition on the source-known bridge support `ell|e`:

```text
BRIDGE_LOCAL_SQUARE_TEST_COMPLETE=true.
```

Higher residue characters at the same `ell` cannot strengthen the question "is `B_e` a square in `Q_ell`?" once `(CB-local)` passes. Re-entering quartic/higher characters without an independent new source identity would therefore be a recharge of the already-complete local square test.

The next legal action is a fresh-route audit after the material Goal4BT/CA/CB bridge receiver rather than another bridge-prime character refinement:

```text
35EX-35_GOAL4CC_POST_SOURCE_BRIDGE_LOCAL_COMPLETION_FRESH_ROUTE_AUDIT
```

The audit should distinguish any genuinely new structural support or descent from the endpoint-equivalent instruction "factor `B_e` completely and test whether every valuation is even."

## 9. Verdict

Certified provisionally:

```text
ODD_BRIDGE_QELL_SQUARE_CRITERION_COMPLETE=true
UNBALANCED_BRIDGE_PRIMES_AUTOMATICALLY_LOCAL_SQUARE=true
BALANCED_UNIT_BIT_SOURCE_COMPUTABLE=true
SOURCE_ONLY_EVEN_VALUATION_UNIT_KILL=true
BRANCH_L_NONREDUNDANT_AFTER_CA=true
BRANCH_R_POSITIVE_EVEN_DEPTH_NONREDUNDANT_AFTER_CA=true
UNIVERSAL_BAD_LOCAL_SQUARE_PRIME_IN_e=false
BRIDGE_LOCAL_SQUARE_ROUTE_COMPLETE=true
E1_PROVED=false
STAGE35_CLOSED=false
```

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
