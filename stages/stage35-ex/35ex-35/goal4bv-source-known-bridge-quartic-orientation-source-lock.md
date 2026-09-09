# Stage35-EX Goal4BV source lock — source-known bridge-prime quartic orientation

Scope: consume exact-green Goal4BU and answer only its next-leaf preflight question: does an early Pesch bridge prime `ell|e` carry a quartic datum whose Gaussian orientation is fixed by the Master-Hit source? Yes. This does **not** prove a quartic obstruction, branch exclusion, E1, Stage35 closure, or any Perfect Cuboid claim. Mathematical authority remains V74 / Goal4AK.

## 1. Exact parent and retained source data

Goal4BU is exact-green at

```text
head = 3f66b64a14d5a7f7ddc5b43759429d355279af9f
```

Retain

```text
D=U1/c,
T=U2/c,
A=(V1/q)*T,
B=D*(V2/q),
A^2+B^2=H^2,
gcd(A,B)=gcd(A,H)=gcd(B,H)=1,
e=gcd(c,H).
```

Goal4BT/BU make `H` and `e` source-computable from a Master-Hit before any E1-failure assumption. Hence `A,B,H,e` are source-fixed.

For a hypothetical E1 counterexample, 35EX-10/11 and Goal4BU give, for every odd prime `ell|e`,

```text
ell = 1 mod 4,
Branch L: (p*q/ell)=+1,
Branch R: (2*p*q/ell)=+1.                         (BV-Q2)
```

The present leaf first asks whether the denominator orientation needed to lift `(BV-Q2)` to order four is itself canonical.

## 2. The reduced Master triple gives a source root of -1

Let `ell` be any odd prime dividing `e`. Since `e|H`,

```text
A^2+B^2 = 0 mod ell.
```

Primitivity gives `ell∤A` and `ell∤B`. Therefore

```text
iota_e(ell) := A*B^(-1) mod ell                    (BV-iota)
```

is defined and satisfies

```text
iota_e(ell)^2 = -1 mod ell.                         (BV-root)
```

This root is not an auxiliary sign choice: `A` and `B` are ordered source expressions, so `iota_e(ell)` is determined by the Master-Hit.

The alternative root `-iota_e(ell)` is the conjugate orientation and is not equally selected by `(BV-iota)`.

## 3. Canonical Gaussian prime and one-sided factor

Following the already established Goal4BF normalization, define

```text
p_{e,ell} = (ell, i-iota_e(ell)) subset Z[i].       (BV-P)
```

In the quotient, `i` maps to `iota_e(ell)`, hence

```text
A-i*B = 0 mod p_{e,ell}.
```

At the conjugate prime, `i=-iota_e(ell)`, so

```text
A-i*B = A+iota_e(ell)*B = 2*A != 0 mod ell,
```

because `ell` is odd and `ell∤A`. Thus exactly one Gaussian prime above `ell` divides the source factor `A-iB`.

Since

```text
N(A-iB)=A^2+B^2=H^2,
```

the one-sided valuation is

```text
v_{p_{e,ell}}(A-iB)=2*v_ell(H),
v_{bar p_{e,ell}}(A-iB)=0.                          (BV-val)
```

Choose the unique primary generator

```text
pi_{e,ell} == 1 mod (1+i)^3.                         (BV-primary)
```

Therefore every odd bridge prime `ell|e` has a source-selected Gaussian prime and a unique primary representative. This is exactly the missing precondition identified by Goal4BU; it is an early-bridge construction, not a reuse of the later endpoint reservoirs from Goal4BF--BO.

## 4. Source-fixed quartic bridge datum

Let

```text
N_L = p*q,
N_R = 2*p*q.
```

For `ell|e`, the standard source coprimalities imply `ell∤p*q`; hence the quartic residue character modulo `pi_{e,ell}` is defined. Set

```text
Q_e(ell) = [N_L/pi_{e,ell}]_4    in Branch L,
Q_e(ell) = [N_R/pi_{e,ell}]_4    in Branch R.        (BV-Q4)
```

All entries in `(BV-Q4)` are source-fixed once the branch is fixed. Squaring recovers the quadratic bridge test:

```text
Q_e(ell)^2 = (N_L/ell) in Branch L,
Q_e(ell)^2 = (N_R/ell) in Branch R.                  (BV-square)
```

Under the hypothetical-counterexample necessary condition `(BV-Q2)`,

```text
Q_e(ell) in {+1,-1}.                                 (BV-real-phase)
```

Thus Goal4BV obtains a genuine order-four lift of the earlier Pesch bridge predicate. The quadratic sieve loses one residual sign bit at each locally-good bridge prime.

## 5. Exact source diagnostics

Goal4BU's Branch-L source witness

```text
(a,b,m,n)=(13,4,96,91),
A=55,
B=1512,
H=1513,
e=17
```

gives

```text
iota_e(17)=55/1512=13 mod 17,
13^2=-1 mod 17.
```

With `N_L=p*q=104`, the corresponding quartic residue is the real phase `-1`.

Goal4BU's Branch-R source witness

```text
(a,b,m,n)=(88,7,98,37),
A=2684,
B=14763,
H=15005,
e=5
```

gives

```text
iota_e(5)=2684/14763=3 mod 5,
3^2=-1 mod 5.
```

With `N_R=2*p*q=56`, the corresponding quartic residue is `+1`.

These are source diagnostics only. They do not satisfy or refute all equations of a hypothetical E1 counterexample and therefore do not prove that both quartic phases survive the full E1 system.

## 6. Goal4BV verdict

Certified provisionally:

```text
BRIDGE_PRIME_SOURCE_ROOT_OF_MINUS_ONE=true
BRIDGE_GAUSSIAN_PRIME_ORIENTATION_SOURCE_FIXED=true
BRIDGE_PRIMARY_GENERATOR_CANONICAL=true
BRIDGE_ONE_SIDED_GAUSSIAN_VALUATION=true
BRIDGE_QUARTIC_DATUM_SOURCE_FIXED=true
QUADRATIC_BRIDGE_TEST_LIFTS_TO_QUARTIC=true
LOCALLY_GOOD_QUADRATIC_BRIDGE_LEAVES_ONE_REAL_QUARTIC_BIT=true.   (BV-VERDICT)
```

Not certified:

```text
quartic bridge sign forced by the full E1 equations;
universal bad quartic bridge prime;
branch exclusion;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

## 7. Next leaf

The remaining question is no longer whether a bridge quartic character is well-defined. It is whether the **full E1 bridge equations**, beyond the Master-Hit source alone, force the surviving real phase in `(BV-real-phase)`.

```text
35EX-35_GOAL4BW_BRIDGE_QUARTIC_PHASE_FORCING_PREFLIGHT
```

Goal4BW should derive the quartic phase from the 35EX-08/10/11 bridge identities and test whether every hypothetical E1 counterexample forces a fixed sign or a nontrivial global product relation. If no such relation is forced, freeze the residual phase gauge rather than charging another reciprocity obstruction.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
