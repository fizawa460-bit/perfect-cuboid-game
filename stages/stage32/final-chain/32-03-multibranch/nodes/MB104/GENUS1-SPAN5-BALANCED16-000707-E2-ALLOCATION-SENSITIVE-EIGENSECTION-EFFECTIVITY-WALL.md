# Stage32 MB104 — `000707000f0f` e=2 allocation-sensitive eigensection effectivity wall

Status: **RETAINED EXACT RR WALL / MINIMUM SUPPORTED-EXCEPTIONAL VANISHING STILL AUTOMATIC FOR EVEN l / EXACT CANCELLATION JETS REMAIN LIVE / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Use the retained Picard64 parity, half-hyperplane factorization, and the even-l eigensection wall. Put

```text
l=2m,
m>=1,
x_j=2y_j,
b_j=y_j-4m.
```

Then

```text
0<=y_j<=8m,
-4m<=b_j<=4m.
```

The two conjugate effective divisors on the residual double cover have supported exceptional multiplicities

```text
G_1: y_j on E_j^+, 8m-y_j on E_j^-,
G_2: 8m-y_j on E_j^+, y_j on E_j^-.
```

Writing the two defining sections as invariant plus/minus anti-invariant eigensections shows that both eigensections must carry the common supported-exceptional vanishing

```text
mu_j=min(y_j,8m-y_j)=4m-|b_j|.                (MU)
```

This note asks whether that stronger, allocation-sensitive vanishing can make either eigenspace empty.

## 1. Downstairs classes after removing the common vanishing

For the invariant and anti-invariant eigensections define

```text
A_mu = 7m H - sum_j mu_j E_j,
B_mu = 7m H - L_abs - sum_j mu_j E_j.         (AB)
```

Here the sum runs over the fourteen supported box nodes. The supported exceptionals are disjoint from the sixteen absent-type branch exceptionals, so

```text
E_i.E_j=0 (i!=j),
E_j^2=-2,
H.E_j=0,
L_abs.E_j=0.
```

The retained absent half-line identities are

```text
H^2=16,
K_S=H,
chi(O_S)=8,
H.L_abs=0,
L_abs^2=-8.
```

Therefore, with

```text
M2=sum_j mu_j^2,
```

we get exactly

```text
A_mu^2 = 784m^2-2M2,
A_mu.K = 112m,

B_mu^2 = 784m^2-2M2-8,
B_mu.K = 112m.                                 (INT)
```

## 2. Riemann--Roch remains positive for every allocation

Surface Riemann--Roch gives

```text
chi(A_mu)=392m^2-56m+8-M2,
chi(B_mu)=392m^2-56m+4-M2.                    (RR-MU)
```

Since `0<=mu_j<=4m` at fourteen nodes,

```text
M2 <= 14*(4m)^2 = 224m^2.                    (M2MAX)
```

Hence uniformly

```text
chi(A_mu) >= 168m^2-56m+8,
chi(B_mu) >= 168m^2-56m+4.                    (RR-LOW)
```

For every `m>=1` both lower bounds are positive; at `m=1` they are respectively `120` and `116`.

## 3. The H2 terms vanish uniformly

By Serre duality,

```text
h^2(A_mu)=h^0(K-A_mu),
h^2(B_mu)=h^0(K-B_mu).
```

The supported exceptionals and `L_abs` are all orthogonal to the nef canonical class `H`. Thus

```text
H.(K-A_mu)=16(1-7m)<0,
H.(K-B_mu)=16(1-7m)<0.
```

Neither dual class can be effective. Therefore

```text
h^2(A_mu)=h^2(B_mu)=0.                         (H2)
```

Combining `(RR-LOW)` and `(H2)` gives the exact uniform lower bounds

```text
h^0(A_mu) >= 168m^2-56m+8 > 0,
h^0(B_mu) >= 168m^2-56m+4 > 0.                (H0-LOW)
```

So even after imposing the **minimum common exceptional vanishing forced by the allocation**, both ambient eigensection systems remain nonempty for every formal allocation and every `m>=1`.

## 4. What survives: exact cancellation, not ambient effectivity

The common vanishing `(MU)` removes only the smaller of the two multiplicities. The residual multiplicity pair is

```text
(y_j-mu_j, 8m-y_j-mu_j)
 = (2 max(b_j,0), 2 max(-b_j,0)).              (RES)
```

Thus at each supported node exactly one of the two conjugate combinations must acquire an additional cancellation of order

```text
q_j=2|b_j|.                                    (Q)
```

This is qualitatively different from asking for a nonzero section of `A_mu` or `B_mu`: it is a **relative jet-matching condition between the invariant and anti-invariant eigensections**. Riemann--Roch of the two ambient line bundles forgets that matching and therefore cannot see the residual sheet datum.

The retained fixed-finite-jet wall does not kill this route, because here the required jet depth `q_j` grows with the allocation imbalance and is not fixed independently of the candidate.

## Route consequence

Closed as a standalone obstruction:

```text
minimum allocation-sensitive exceptional vanishing
 -> one eigensection system is empty.
```

It never happens: both systems have large positive RR lower bounds.

The next live target is the adaptive cancellation map

```text
(s_+,s_-)
 -> supported exceptional normal jets
 -> require one of s_+ +/- s_- to vanish q_j=2|b_j| extra orders
 -> relate the resulting +/- choice to the residual G/H character.
```

A useful exact next step is to compute the local jet-target dimension on a supported `(-2)` exceptional and then determine the rank of the simultaneous global evaluation map. Only the latter can become a global obstruction.

## Firewalls

- This note proves nonemptiness of the ambient line systems only; it does not construct the required matched pair of eigensections.
- It does not prove independence or surjectivity of jet conditions at different nodes.
- It does not identify an individual conductor residual sheet.
- No weighted-cut upper bound is proved.
- The half-hyperplane/eigensection setup inherits the candidate status of the retained ambient-H1 linearization.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
