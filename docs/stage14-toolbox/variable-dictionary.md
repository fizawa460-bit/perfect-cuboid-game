# Stage14-toolbox cross-route variable and normalization dictionary

This document is a use-oriented dictionary for the merged Stage14 `14-4` main route and `s` route. It does not introduce new mathematics. It normalizes the already-proved interfaces so a later stage can move from a physical two-face object to Euclid support, descent/kernel variables, the integral small-point witness, and the compact physical denominator without silently changing meanings.

## 1. Translation chain

```text
physical two-face object
  (S,X,H), (S2,X2,H2), d
        |
        | first-face Euclid normalization
        v
  S=2mn, X=(m-n)(m+n), H=m^2+n^2
        |
        | five odd support columns
        v
  m | n | (m-n) | (m+n) | (m^2+n^2)
        |
        | supported Kummer/global witness
        v
  Z=A/D^2, W=Y/D^3
  G0=A
  G1=A-S^2D^2
  G2=A+X^2D^2
        |
        | signed squarefree extraction
        v
  Gi=di ui^2
  d0=tau0*a*b
  d1=tau1*a*c
  d2=tau2*b*c
  a|rad_odd(S), b|rad_odd(X), c|rad_odd(H)
        |
        | fixed packet
        v
  d0u0^2-d1u1^2=S^2D^2
  d2u2^2-d0u0^2=X^2D^2
        |
        | physical compact torsion normalization
        v
  Q=P_phys+(0,0),  -X^2<Z_Q<0
  physical signs (--+), four admissible 2-adic/sign packets
        |
        | second-face / space-diagonal expansion
        v
  g=gcd(S,S2), G=g*d, R=H2-S2
  N+=HG+S^2H2+X^2S2
  N-=HG-S^2H2-X^2S2
  U=G-HS2, V=HH2-G
        |
        v
  Z_P=N+/R
  Z_T=-N-/R=-UV/X2^2
  D_T^2=R/gcd(N-,R)=X2^2/gcd(X2^2,UV)
        |
        | partner Euclid half-angle chart
        v
  R=kappa*t^2, D_T|t, k=t/D_T
  gcd(N-,R)=kappa*k^2
```

The cards under `docs/stage14-toolbox/cards/` are the canonical interfaces. This page is only the human-readable map.

## 2. First-face variables

For the normalized Euclid chart used by the s5/s6 support decomposition:

```text
S = 2mn
X = m^2-n^2 = (m-n)(m+n)
H = m^2+n^2
m>n>0, gcd(m,n)=1, m,n opposite parity.
```

The five odd support columns are

```text
A-column: m
B-column: n
C-column: m-n
D-column: m+n
E-column: m^2+n^2.
```

Do not confuse these column labels with the rational-coordinate numerator `A` in `Z=A/D^2`.

## 3. Global witness variables

On

```text
E_{S,X}: W^2=Z(Z-S^2)(Z+X^2),
```

a bounded-height rational witness is written primitively as

```text
Z=A/D^2,
W=Y/D^3,
D>0,
gcd(A,D)=1.
```

Define

```text
G0=A,
G1=A-S^2D^2,
G2=A+X^2D^2.
```

Then

```text
G0-G1=S^2D^2,
G2-G0=X^2D^2,
G2-G1=H^2D^2,
Y^2=G0G1G2.
```

Write

```text
Gi=di ui^2
```

with signed squarefree `di`. The odd kernel has the edge factorization

```text
d0=tau0*a*b,
d1=tau1*a*c,
d2=tau2*b*c,

a|rad_odd(S),
b|rad_odd(X),
c|rad_odd(H),
```

and `tau_i in {+1,-1,+2,-2}` with sixteen abstract sign/2-adic patterns. The fixed packet variables are

```text
sigma=(tau0,tau1,tau2,a,b,c).
```

## 4. Main-route / s-route shared two-quadrics

The main route `14-4bg` and `s6-01` use the same integral witness object after normalization:

```text
d0u0^2-d1u1^2=S^2D^2,
d2u2^2-d0u0^2=X^2D^2.
```

Equivalently, after inserting the edge packet,

```text
tau0*a*b*u0^2-tau1*a*c*u1^2=S^2D^2,
tau2*b*c*u2^2-tau0*a*b*u0^2=X^2D^2.
```

The third difference is automatically `H^2D^2`.

This equality of normalized objects is a dictionary statement, not permission to transfer every estimate between routes. A bound must still match its quantifiers: fixed packet vs moving family, coordinate density vs packet existence, unweighted vs weighted, and `M` scale vs physical `B` scale.

## 5. Physical compact normalization

For a genuine physical point `P_phys`, s6-05 replaces the abstract need for repeated halving by the exact torsion translate

```text
T0=(0,0),
Q=P_phys+T0.
```

The coordinate map is

```text
Z(Q)=-S^2X^2/Z(P),
W(Q)=S^2X^2 W(P)/Z(P)^2.
```

The translated point lies on the compact real component

```text
-X^2<Z(Q)<0
```

and is automatically nonzero modulo `2E(Q)`. Its signed kernel chamber is `(--+)`, leaving exactly four admissible sign/2-adic packets.

The denominator of this particular physical compact representative is denoted

```text
D_T.
```

It is not the same symbol/object as the generic rational witness denominator `D`, and it is not the packet statistic `D_min`.

## 6. Physical pair variables

For two primitive oriented Pythagorean faces

```text
F =(S,X,H),
F2=(S2,X2,H2),
```

sharing a physical cuboid edge, let

```text
g=gcd(S,S2),
d=integer space diagonal,
G=g*d.
```

Then

```text
G^2=S^2H2^2+X^2S2^2.
```

Define

```text
R=H2-S2,
Nplus =HG+S^2H2+X^2S2,
Nminus=HG-S^2H2-X^2S2,
U=G-HS2,
V=HH2-G.
```

The physical and compact coordinates are

```text
Z_P=Nplus/R,
Z_T=-Nminus/R=-U*V/X2^2.
```

The compact denominator obeys

```text
D_T^2=R/gcd(Nminus,R)
     =X2^2/gcd(X2^2,U*V),
D_T^2|R,
D_T|X2.
```

## 7. Partner half-angle variables

Let `m2>n2` be the Euclid parameters of the primitive partner face. Define

```text
if S2=2m2n2:
    t=m2-n2, kappa=1

if S2=m2^2-n2^2:
    t=n2, kappa=2.
```

Then uniformly

```text
R=H2-S2=kappa*t^2,
D_T|t,
k=t/D_T,
gcd(Nminus,R)=kappa*k^2.
```

Here `k` is a cancellation cofactor. It is not a generic dyadic parameter and should not be identified with a kernel divisor unless a later theorem explicitly does so.

## 8. Denominator selectors: do not collapse them

```text
D      = denominator square-root in a chosen rational witness Z=A/D^2.
D_min  = least such denominator among bounded-height representatives of an abstract packet.
D_T    = denominator square-root of the canonical physical compact torsion translate.
```

Relations currently justified:

```text
for the physical packet containing Q=P_phys+(0,0):
D_min <= D_T.
```

The physical selector `D_T` has extra reconstruction identities (`D_T|X2`, half-angle/root-sign structure) that a generic `D_min` need not retain.

## 9. Symbol collision warnings

The following collisions are deliberate historical notation and must not be silently identified:

| Symbol | Meaning in one context | Different meaning elsewhere |
|---|---|---|
| `A` | numerator in `Z=A/D^2` | s5 `A`-column = `m` |
| `D` | witness denominator square-root | s5 `D`-column = `m+n`; also `D_min`, `D_T` are distinct selectors |
| `G_i` | witness factors `G0,G1,G2` | physical `G=g*d` is a single gluing scale |
| `U,V` | physical positive gaps in s6-06 | `U_i` or dyadic `U,V` in incidence bounds may denote box lengths |
| `g` | `gcd(S,S2)` in physical gluing | generic gcd symbols in older local arguments |
| `d` | physical space diagonal in s6-06 | `d_i` are signed squarefree witness kernels |
| `a,b,c` | odd edge-kernel divisors | physical cuboid edge letters in other project-level discussions |

A later proof may rename variables locally, but the toolbox dictionary should be used when moving statements between routes.

## 10. Current provenance boundary

Canonical content on this page is extracted only from merged sources:

- Stage14-4bg, PR #344, merge `80e59daf772f39ec6d48435717440e1c120c4e47`;
- Stage14-s6-01, PR #345, merge `86b91ffcd8bae79452ef75f187c8570a3819d386`;
- Stage14-4bj, PR #355, merge `7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7`;
- Stage14-s6-05, PR #356, merge `c2273d0388b48f8fb51d9dc69d8977efbc83db37`;
- Stage14-s6-06, PR #360, merge `42f4315b0659bd402a94adeb8822588ea153305a`.

Open Stage14-4bk is intentionally not used as canonical provenance in toolbox-ab.
