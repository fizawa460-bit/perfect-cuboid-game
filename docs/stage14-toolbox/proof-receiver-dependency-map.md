# Stage14 main/s proof-receiver dependency map

This document answers one question: **given a proved object, what is the next legal receiver?**

It is not a new proof and it does not strengthen any source theorem.

## 1. Quantifier ladder

```text
L0 local state / character row
 |
 | global rational point must come from the physical problem
 v
L1 global rational witness
 |
 | primitive denominator normalization
 v
L2 integral witness coordinate
 |
 | signed squarefree packet + full radical support
 v
L3 fixed signed kernel packet
 |\
 | \ arithmetic: radical / CRT incidence
 |  \ geometry: two quadrics
 v   v
L4 fixed curve / fixed fiber
 |
 | explicit physical-image / multiplicity transfer
 v
L5 physical edge / transferred face pair
 |
 | fixed-fiber closure exposes support count
 v
L6 active direction / reduced-coordinate base
 |
 | reduced fixed quartic + product-square descent
 v
L7 restricted square-part / coefficient sector
 |
 | exhaustive recombination
 v
L8 whole physical family
```

Never jump a level without a merged handoff theorem.

## 2. Dispatch table

| You currently have | Preferred receiver | Key toolbox entry | What it may produce |
|---|---|---|---|
| local character/Q2 admissibility | global-witness handoff | `TB-RECIPE-dispatch-local-to-global-witness` | only a legal entrance to global counting |
| integral witness + edge kernels | radical or geometry dispatch | `TB-RECIPE-dispatch-witness-to-radical-geometry` | coordinate incidence, radical-poor base count, or fixed genus-one curve |
| physical two-face pair | dual compact half-angle receiver | `TB-RECIPE-dispatch-compact-half-angle-physical` | exact denominator/cancellation/gcd-cell routing |
| fixed direction with `B^o(1)` partners | active-direction receiver | `TB-RECIPE-dispatch-fixed-fiber-active-direction` | exponent-equivalent active-base count |
| balanced reduced-coordinate quartic | inert-prime square-sieve receiver | `TB-RECIPE-dispatch-balanced-inert-square-sieve` | thick packet relative `H^(-1/2)` saving |
| thin square part + large shared coefficient | shared-`xi` cell switch | `TB-RECIPE-dispatch-shared-xi-cell-switch` | cell relative `T^(-1/2)` saving |
| several candidate savings | composition audit | `TB-WARNING-proof-receiver-composition-boundary` | legal sector recombination only |

## 3. Core dependency chains

### 3.1 Local-to-witness chain

```text
five columns
 -> odd local rows + Q2 state
 -> LOCAL_ADMISSIBLE
 -X-> global point

physical hit
 -> actual global rational point
 -> Z=A/D^2, W=Y/D^3
 -> Y^2=A(A-S^2D^2)(A+X^2D^2)
```

The crossed arrow is deliberately forbidden.

### 3.2 Witness arithmetic/geometry fork

```text
integral witness
 -> d0=tau0*a*b, d1=tau1*a*c, d2=tau2*b*c
 -> full radicals R_S,R_X,R_H

if usable radical is large:
  composite projective-line incidence

if supported radical is poor:
  sparse supported base/classes

if packet is fixed and point geometry matters:
  two quadrics -> smooth genus-one curve
```

A fixed genus-one curve is not itself a moving-family saving.

### 3.3 Physical compact-selector chain

```text
physical pair
 -> two torsion translates
 -> D_+,D_-,k_+,k_-
 -> Q=D_+D_-, K=k_+k_-
 -> QK=X2/kappa
 -> q--,q-+,q+-,q++
 -> denominator / cancellation / shared half-angle receiver
```

The four gcd cells are deterministic divisor allocation, not random sign bits.

### 3.4 Fixed fiber to active base

Merged s6-09 gives, at the appropriate physical receiver,

```text
A_phys(B) <= E_phys(B) <= A_phys(B) B^o(1).
```

So once the fixed fiber is closed, the next power-scale object is the number of active directions/bases, not further fixed-curve refinements.

### 3.5 Current reduced-quartic receiver

Merged s7-07 reduces the hard physical image to

```text
ker(F(P,Q))=ker(F(R,S)),
F(A,B)=AB(B-A)(B+A),
QS<<B.
```

At inert primes the complete character trace vanishes. Merged 4bv product-square descent gives

```text
P=a*x^2, Q=b*y^2, R=c*z^2, S=d*h^2,
ab=cd=xi,
N_packet << M*H^(-1/2) B^o(1).
```

This closes thick square-part packets.

### 3.6 Thin shared-xi receiver and current whole-family bound

Merged s7-08 factors

```text
r=gcd(a,c), s=gcd(a,d), t=gcd(b,c), j=gcd(b,d),
a=rs, b=tj, c=rt, d=sj, xi=rstj.
```

A forced large coefficient gives a large cell `q~T`. Varying that cell gives a non-square quartic and

```text
# cell solutions << T^(1/2) B^o(1).
```

With

```text
lambda=9/19,
tau=2/19,
theta=8/19,
```

the exhaustive sectors all lie at or below

```text
V(B) << B^(18/19+o(1)).
```

Thus the current toolbox ledger is

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
CURRENT_REMAINING_GAP_TO_SQRT=17/38
```

## 4. Receiver status legend

```text
STRUCTURAL
  exact identity / parametrization; no saving by itself

FIXED-OBJECT
  controls a fixed packet, curve, direction, or coordinate

SECTOR
  controls a proved subset of the physical family

WHOLE-FAMILY
  only after an exhaustive recombination
```

Before composing two receiver outputs, apply `TB-WARNING-proof-receiver-composition-boundary`.

## 5. Current reusable route in one line

```text
Pythagorean/Euclid
 -> local interface
 -> physical global witness
 -> integral witness
 -> kernel/radical or compact selector
 -> genus-one / incidence
 -> fixed-fiber closure
 -> reduced quartic
 -> inert square sieve
 -> shared-xi cell switch
 -> exhaustive 18/19 whole-family bound
```

This is a toolbox route map, not a claim that every physical object must pass through every branch.