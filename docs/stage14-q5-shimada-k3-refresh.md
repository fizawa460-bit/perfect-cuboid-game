# Stage14-q5 — Shimada K3 / lattice computational refresh

## Status

```text
STAGE14_Q5=COMPLETE_SHIMADA_K3_LATTICE_REFRESH
CHECKED_AT=2026-08-09
PRIMARY_GEOMETRIC_WEAPON=Shimada level-4 modular K3 lattice/automorphism package
PRIMARY_WEAPON_ALREADY_CONSUMED_BY_14_4=true
FIXED_M4_GEOMETRIC_ROUTE_REOPEN=false
DIRECT_NEW_GEOMETRIC_THEOREM_COUNT=0
NEXT_Q_STAGE=Stage14-q6 cross-track weapon test
```

## Purpose

Stage14-q5 audits whether the Shimada level-4 modular K3 computation package still contains an unused geometric weapon capable of advancing the current Stage14-4 frontier, or whether that package has already been consumed by the earlier M-degree-4 bisection classification.

The answer is now clear: the decisive Shimada data were already imported, identified, enumerated, independently verified, and used to close the sole fixed physical `M`-degree-four square-root mechanism. The current Stage14-4 frontier is analytic/moving-family, not an unresolved finite K3-lattice classification.

## 1. Primary-source refresh

Ichiro Shimada's paper

> *The elliptic modular surface of level 4 and its reduction modulo 3*

studies the level-4 elliptic modular K3 surface, with Picard number 20, using the Neron--Severi lattice, reduction modulo 3, and explicit automorphism computations. Shimada's author site continues to publish the associated computational data.

The general computational philosophy is backed by Shimada's lattice/automorphism algorithms for K3 surfaces: finite generators and chamber/lattice computations can turn geometric curve-class questions into exact integral-lattice problems when the relevant polarization and involutions are identified.

For Stage14, this was not merely background. The exact package was consumed operationally.

## 2. What Stage14 already extracted

### Stage14-4ah

The physical polarization was identified intrinsically:

```text
M = pi^*(-K_Y)
M^2 = 8
H_M(P) = physical space diagonal d
```

and every fixed physical rational curve capable of a `B^(1/2)` height contribution had to satisfy

```text
M.C = 4
```

with the extremal mechanism a rational bisection.

### Stage14-4ai

All lower/genus-zero degree-four mechanisms were eliminated, leaving exactly one case:

```text
split singular anticanonical D in |-K_Y|
```

whose pullback would split as

```text
pi^*D = C + delta(C)
```

with a physical rational `M`-degree-four component.

### Stage14-4aj

PR #190 converted that surviving geometry into the exact Shimada-lattice interface. It identified the Stage14 deck involution as a two-torsion translation composed with Shimada's inversion, supplied the physical `M` fingerprint, and reduced the split case to root conditions

```text
C^2 = -2
M.C = 4
delta(C) = M-C.
```

The official computation objects explicitly listed for ingestion were

```text
GramS0
L40vs
Wout0
AutX0h0
SixFs
fsigma
zsigma
AutX0f
iotasigmaz
MWtorsigmaz
Tsigma
Galmu
```

with finite label matching for the two fiber directions, deck torsion, boundary torsion, and the Stage14 polarization.

### Stage14-4ak

PR #199 performed the decisive independent exact enumeration. With

```text
x = 2C-M,
```

a split component would require

```text
delta(x)=-x
x^2=-16
x = M mod 2.
```

The saturated deck anti-invariant lattice has rank 6 and determinant 256. Norm-16 vectors are abundant, but the required parity coset is empty:

```text
PARI norm-16 +/- representatives = 510
independent exact LDL norm-16 vectors = 1020
parity-compatible norm-16 vectors = 0
parity-compatible split-root pairs = 0
```

Therefore Stage14 froze

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

This is the key q5 fact. The Shimada package did its intended job.

## 3. Current 14-4 frontier is no longer geometric

After 4ak the main track explicitly returned to the collective/moving arithmetic mechanism. 4al and later stages formulate the population as a moving-base activation problem, and the current 4ax/4ay frontier is local-character dispersion over Euclid parameters.

Consequently, a new broad search for K3 automorphisms, rational curves, or Neron--Severi roots would not address the current named obstruction.

The present unresolved objects are of the form

```text
medium determinant dispersion
microscopic small-side modes
state-split norm mixed-sign D*S dispersion
```

and the separate global/Sha and first-small-point retainers. These are analytic/arithmetic family problems, not finite lattice enumeration problems.

## 4. Classification of Shimada assets after refresh

### DIRECT — already consumed

The following are direct, exact computational assets, but their Stage14 M-degree-four application is complete:

- Neron--Severi Gram data;
- distinguished fiber classes and their automorphism orbit;
- fiber-preserving automorphisms;
- inversion and Mordell--Weil torsion translations;
- chamber/wall data;
- Galois-action data;
- exact lattice enumeration infrastructure.

They should remain frozen infrastructure and regression references.

### BACKGROUND — not a new Stage14 weapon

General K3 automorphism/lattice literature remains useful for interpretation, but q5 finds no reason to reopen a general K3 classification search while the fixed minimal curve mechanism has already been eliminated.

### BLOCKED as a response to the current frontier

The following tempting moves are now explicitly blocked unless a later stage creates a new geometric target:

1. searching for more `M.C=4` rational bisections;
2. re-running the same Shimada root enumeration with broader automorphism orbits;
3. replacing the exact parity-coset void by generic K3 rational-curve existence results;
4. using existence of infinitely many rational curves over an algebraic closure to infer a `Q`-rational physical accumulating family;
5. treating a newly found higher-degree rational curve as an explanation of the finite `sqrt(B)` signal without satisfying the proliferation budget from Stage14-s4c.

## 5. Reopen conditions

The geometric/K3 literature radar should reopen only if an active proof route produces one of these concrete triggers:

### Trigger A — new fixed low-degree divisor class

A rigorous reduction produces a new physical fixed-curve class not covered by the `M.C=4` classification, together with explicit numerical intersection constraints. Then Shimada's lattice machinery may again be direct.

### Trigger B — finite higher-degree orbit classification becomes decisive

A later argument shows that only finitely many `M.C=d` classes for a specific small `d>4` can matter and gives a quantitative reason why their finite classification could close a theorem gate.

### Trigger C — new Galois/descent ambiguity

An algebraic curve class is found geometrically but rationality over `Q` remains the only obstruction. Then `Galmu`/automorphism orbit data can again be relevant.

### Trigger D — new fibration changes the arithmetic problem

A later stage identifies a genus-one/elliptic fibration for which the current moving-family obstruction becomes a finite Mordell--Weil or lattice-orbit problem. In that case Shimada's broader elliptic-K3 computational framework should be rescanned.

Without one of these triggers, q5 recommends **do not spend a Stage14 worker on K3 geometry**.

## 6. Interaction with current finite `sqrt(B)` signal

Stage14-num5 now reports that the finite effective exponent has drifted downward rather than stabilized at `1/2`. This reinforces the post-4ak caution: the early `sqrt(B)`-looking signal should not motivate reopening the eliminated fixed-curve mechanism.

Even if a `B^(1/2)` asymptotic eventually reappears, Stage14-s4c already shows that higher-degree fixed strata would require a growing number of strata. That is a collective proliferation problem, not a single forgotten Shimada root.

## 7. q5 decision

The literature radar result is therefore mainly a closure certificate:

```text
SHIMADA_DATA_LIVE_AND_REPRODUCIBLE=true
STAGE14_PHYSICAL_M_IDENTIFIED=true
STAGE14_DECK_ACTION_IDENTIFIED=true
M4_ROOT_SEARCH_EXECUTED=true
M4_ROOT_SEARCH_INDEPENDENTLY_VERIFIED=true
REQUIRED_PARITY_COSET_EMPTY=true
FIXED_M4_GEOMETRIC_MECHANISM_CLOSED=true
CURRENT_14_4_OBSTRUCTION_IS_K3_LATTICE_PROBLEM=false
REOPEN_K3_ONLY_ON_NEW_EXPLICIT_GEOMETRIC_TRIGGER=true
```

## Handoff

Stage14-q6 should perform the cross-track weapon test using the now-clean separation:

- q2 analytic dispersion weapons -> current 14-4 / s frontiers;
- q3 Le Boudec-style large-prime + complete-2-descent architecture -> height retainer;
- q4 square/polynomial sieve -> t collision-energy route;
- q5 Shimada K3 machinery -> **frozen, consumed**, reopen only on a new explicit geometric trigger.
