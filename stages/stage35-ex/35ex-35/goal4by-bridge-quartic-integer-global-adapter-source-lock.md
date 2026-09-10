# Stage35-EX Goal4BY source lock — integer bridge quartic adapter is source-redundant

Scope: consume exact-green Goal4BX and test the proposed integral adapter using the exact bridge double-square identities and the 35EX-09 factor-allocation graph. The adapter can be derived completely, but its apparent new quartic condition reduces algebraically to the already source-fixed Goal4BV quartic datum together with quadratic identities that are automatic from the Master source. Therefore this specific integer bridge-quartic route adds no new pruning credit. Mathematical authority remains V74 / Goal4AK. No merge.

## 1. Exact parent

Current retained parent head before this leaf:

```text
1033a99c16237f1d6ae0cf943d1b35e84a391967
```

At that head:

```text
Goal4BX dedicated run = 34420555860 SUCCESS
Stage35/35EX aggregate = 34420555856 SUCCESS
```

Goal4BX gives, for every odd bridge prime `ell|e`, a source-selected primary Gaussian prime and a real quartic phase. Write

```text
chi_ell(x) = Legendre(x,ell),
eps_ell(x) = x^((ell-1)/4) in {+1,-1} when chi_ell(x)=+1.
```

Retain

```text
iota = iota_e(ell),
omega = W1/V1 mod ell in {+1,-1},
F_omega = a + omega*b,
T=U2/c.
```

For Branch L use the cross reservoir `t`; for Branch R use `j`.

## 2. The bridge e-allocation is already source-fixed

Goal4BW gives

```text
rho=r/s=omega*iota mod ell.
```

In Branch L, `sigma=u/v=iota`. Reducing the four 35EX-05 vertices modulo `ell` gives

```text
L1/(s*v) = 1-omega,
L2/(s*v) = (omega-1)*iota,
L3/(s*v) = -(omega+1),
L4/(s*v) = (omega+1)*iota.                    (BY-L-vertices)
```

Hence

```text
omega=+1 => ell divides L1,L2  (e12),
omega=-1 => ell divides L3,L4  (e34).
```

In Branch R, `u/v=-iota`, and similarly

```text
R1/(s*v) = (omega-1)*(1-iota),
R2/(s*v) = (omega-1)*(1+iota),
R3/(s*v) = (omega+1)*(1-iota),
R4/(s*v) = (omega+1)*(1+iota).                (BY-R-vertices)
```

Thus the same rule holds:

```text
omega=+1 => ell divides R1,R2  (e12),
omega=-1 => ell divides R3,R4  (e34).          (BY-e-allocation)
```

So the bridge squareclass edge choice that was parametric in 35EX-09 becomes source-fixed once Goal4BW's relative-root orientation is inserted.

## 3. The surviving phase is a nonvanishing vertex-unit character

Define the nonvanishing carrier

```text
Branch L:
  K_L=L3 if omega=+1,
  K_L=L1 if omega=-1.

Branch R:
  K_R=R4 if omega=+1,
  K_R=R2 if omega=-1.
```

The exact pair products of 35EX-09 give, in both branches,

```text
K_branch^2 = iota*C*T*F_omega^2 mod ell,       (BY-K2)
```

where

```text
C=t in Branch L,
C=j in Branch R.
```

Indeed, in Branch L the nonvanishing pair has ratio `-iota`; since `(-iota)^(-1)=iota`, its chosen carrier squares to `iota*t*T*F_omega^2`. In Branch R the chosen carrier is the numerator of the ratio `iota`, giving `iota*j*T*F_omega^2`.

Goal4BW's residual roots satisfy

```text
z_L=q*v/s,
z_R=(1+iota)*q*v/s.
```

Because `s^2` is a square and `ell=1 mod4`, `(BY-L-vertices)` and `(BY-R-vertices)` imply the unified character formula

```text
chi_ell(z_branch)
 = chi_ell(q*F_omega/2) * eps_ell(iota*C*T).    (BY-apparent-adapter)
```

At first sight this is the desired integer quartic adapter: it expresses the residual Goal4BW bit through the exact factor graph.

## 4. The apparent adapter collapses to source algebra

The cross-reservoir definitions and `iota=A/B` give directly

```text
Branch L:
  iota*t*T = V1*T^2/(2*p*q).

Branch R:
  iota*j*T = V1*T^2/(p*q).                     (BY-C-collapse)
```

Also, because `ell|U1` and `omega=W1/V1=+/-1 mod ell`, one has

```text
F_omega^2=(a+omega*b)^2
            =W1+omega*V1
            =2*omega*V1 mod ell.               (BY-F2)
```

Put

```text
N_L=p*q,
N_R=2*p*q.
```

Then `(BY-C-collapse)` and `(BY-F2)` become

```text
Branch L:
  iota*t*T = (F_omega*T/2)^2 * omega/N_L.

Branch R:
  iota*j*T = (F_omega*T)^2 * omega/N_R.         (BY-square-collapse)
```

Consequently `(BY-apparent-adapter)` simplifies to

```text
Branch L:
  chi_ell(z_L)=chi_ell(q*T) * [omega/pi]_4/[N_L/pi]_4.

Branch R:
  chi_ell(z_R)=chi_ell(q*T/2) * [omega/pi]_4/[N_R/pi]_4.   (BY-reduced)
```

Here `pi=pi_{e,ell}` is the Goal4BV source-selected primary prime; all quartic values are real under the quadratically-good bridge condition.

## 5. The extra quadratic factors are automatic Master-source identities

They do not produce new E1 restrictions.

### Branch L

The source Master parametrization gives

```text
(V1/q)*T=u^2-v^2.
```

Modulo `ell|H=u^2+v^2`,

```text
u^2-v^2=-2*v^2.
```

Therefore

```text
chi_ell(V1*T/q)=chi_ell(2).
```

On the other hand `(BY-F2)` and `chi_ell(omega)=+1` give

```text
chi_ell(V1)=chi_ell(2).
```

Cancelling yields

```text
chi_ell(q*T)=+1.                              (BY-L-auto)
```

### Branch R

Now

```text
(V1/q)*T=2*u*v.
```

At `ell|H`, `iota=-u/v` and `iota^2=-1`. For every prime `ell=1 mod4`,

```text
chi_ell(iota)=(-1)^((ell-1)/4)=chi_ell(2).
```

Hence

```text
chi_ell(u*v)=chi_ell(-iota)=chi_ell(2),
chi_ell(2*u*v)=+1.
```

Thus

```text
chi_ell(V1*T/q)=+1.
```

Using again `chi_ell(V1)=chi_ell(2)` gives

```text
chi_ell(q*T/2)=+1.                            (BY-R-auto)
```

Substituting `(BY-L-auto)` / `(BY-R-auto)` into `(BY-reduced)` gives exactly

```text
chi_ell(z_branch)=[N_branch/pi]_4/[omega/pi]_4,
```

which is Goal4BW's rearrangement of

```text
Q_e(ell)=[omega/pi]_4*chi_ell(z_branch).
```

Therefore the integer adapter is algebraically equivalent to the already source-fixed quartic datum. It is not a new sieve.

## 6. Exact integer diagnostics: same e-allocation, opposite residual bits

These diagnostics satisfy the primitive parameter-pair equations, the branch cross equation, the four-factor square condition, the first Euclid-pair additive equations, and the exact bridge double squares. They are not complete Master-Hits/E1 counterexamples because the second Euclid-pair completion is not imposed.

### Branch L, ell=e=17, omega=-1, allocation e34

Negative residual bit:

```text
(r,s,u,v)=(21,16,7,6),
p=1, q=8,
w=697, H=85,
e=17,
t=42, T=1,
(a,b)=(13,4),
(L1,L2,L3,L4)=(243,14,51,238),

p*w-q*H=17*1^2,
p*w+q*H=17*9^2,
z_L=3 mod17,
chi_17(z_L)=-1.
```

Positive residual bit:

```text
(r,s,u,v)=(49,8,14,5),
p=5, q=28,
w=2465, H=221,
e=17,
t=14, T=57,
(a,b)=(14,3),
(L1,L2,L3,L4)=(726,133,646,357),

p*w-q*H=17*19^2,
p*w+q*H=17*33^2,
z_L=9 mod17,
chi_17(z_L)=+1.
```

Both have the same bridge prime, the same `omega=-1`, and hence the same `e34` allocation, but opposite residual phases.

### Branch R, ell=e=41, omega=+1, allocation e12

Negative residual bit:

```text
(r,s,u,v)=(14,3,22,7),
p=145, q=28,
w=205, H=533,
e=41,
j=3, T=11,
(a,b)=(49,8),
(R1,R2,R3,R4)=(123,451,297,361),

p*w-q*H=41*19^2,
p*w+q*H=41*33^2,
z_R=24 mod41,
chi_41(z_R)=-1.
```

Positive residual bit:

```text
(r,s,u,v)=(21,16,23,2),
p=25, q=32,
w=697, H=533,
e=41,
j=21, T=1,
(a,b)=(64,23),
(R1,R2,R3,R4)=(41,861,841,189),

p*w-q*H=41*3^2,
p*w+q*H=41*29^2,
z_R=40 mod41,
chi_41(z_R)=+1.
```

Again the same bridge prime and same source-fixed allocation support both phases at this exact integer layer.

## 7. Goal4BY verdict

Certified provisionally:

```text
BRIDGE_E12_E34_ALLOCATION_SOURCE_FIXED_BY_OMEGA=true
INTEGER_FACTOR_GRAPH_GIVES_VERTEX_UNIT_QUARTIC_ADAPTER=true
APPARENT_INTEGER_QUARTIC_ADAPTER_REDUCES_TO_SOURCE_QE=true
BRANCH_L_CHI_QT_AUTOMATIC=true
BRANCH_R_CHI_QT_OVER_2_AUTOMATIC=true
GOAL4BY_ADDS_NEW_BRIDGE_QUARTIC_PRUNING=false
MECHANICAL_BRIDGE_QUARTIC_ROUTE_FAIL_CLOSED=true
```

Not certified:

```text
full E1 theorem;
nonexistence of a stronger odd-prime higher-adic invariant;
nonexistence of a new integral descent using data beyond the retained factor graph;
R29-PESCH-E1 closure;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

Cycle classification:

```text
CYCLE_ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
CYCLE_ACTIVE_RECEIVER=R29-PESCH-E1 hypothetical counterexample with source-known bridge reservoir e
CYCLE_NEW_VIEW=bridge factor allocation is source-fixed but its quartic unit character is algebraically redundant
CYCLE_NEW_VIEW_SOURCE=INTERNAL_DERIVATION
```

Because BU/BW/BX/BY now give multiple blocked reformulations of the same bridge receiver after the Goal4BT material change, the next legal action is an EXHAUSTIVE_VIEW_AUDIT with blind rediscovery before parking or opening another bridge-character layer.

Proposed next unit:

```text
35EX-35_GOAL4BZ_POST_BRIDGE_QUARTIC_FRESH_ROUTE_AUDIT
```

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.