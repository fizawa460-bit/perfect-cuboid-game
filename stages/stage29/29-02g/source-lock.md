# Stage29-02g — modular / Q-descent source lock

```text
ROLE=MODULI_M4_8_Q_DESCENT_SOURCE_LOCK
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

## Primary endpoint source

Damiano Testa and Michael Stoll, *The surface parametrizing cuboids*, current accepted/published version of arXiv:1009.0388 / Math. Comp. DOI 10.1090/mcom/4238, Section 4.

Load-bearing statements in the current PDF (Section 4, pp. 8–9):

```text
X: u^2=2xy, v^2=x^2-y^2, w^2=x^2+y^2
```

is a genus-5 model of `X(8)` whose noncuspidal points carry full symplectic level-8 structure. Its geometric automorphism group is

```text
PSL_2(Z/8Z), |PSL_2(Z/8Z)|=192.
```

The reduction map

```text
PSL_2(Z/8Z) -> PSL_2(Z/4Z) ~= S4
```

has kernel

```text
G0 ~= (Z/2Z)^3,
```

and the endpoint surface over `Q(i)` is

```text
Sbar_Q(i) ~= (X(8) x X(8))/Delta G0.
```

The same section gives the exact Q-form as the quotient of the Weil restriction `Res_{Q(i)/Q}(X_Q(i))` by `G0`. A Q-rational endpoint point corresponds to an elliptic curve `E/Q(i)`, a basis `P1,P2` of `E[4]`, and an induced 8-torsion isomorphism

```text
psi:E[8] -> Ebar[8]
psi(P1)=Pbar1
psi(P2)=-Pbar2,
```

where bar is the nontrivial automorphism of `Q(i)/Q`.

This is the exact endpoint receiver. It is stronger than ordinary 8-congruence.

## Modular parametrization source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), arXiv:1303.6495.

The source identifies the box variety with a modular variety and gives the theta-function / level `(4,8)` presentation over the Gaussian field. In this suffix it is used as independent provenance for the modular-level description; the exact Q-form is taken from Testa--Stoll Section 4.

## Ordinary 8-congruence firewall

Tom Fisher, *Explicit moduli spaces for congruences of elliptic curves*, arXiv:1804.10195.

Fisher defines `Z(N,epsilon)` as the surface parametrizing pairs of N-congruent elliptic curves with Weil-pairing power epsilon. For `N=8, epsilon=1`, the ordinary congruence surface is rational over Q, and Corollary 1.3 supplies infinitely many non-isogenous rational pairs. Thus ordinary symplectic 8-congruence is not rare enough to be an endpoint obstruction.

```text
ORDINARY_8_CONGRUENCE_ALONE=RED
EXACT_CONJUGATE_SELF_LEVEL4_CONDITION_REQUIRED=true
```

## Scope firewall

```text
MODULAR_INTERPRETATION_EXACT=true
Q_RATIONAL_POINT_SET_COMPUTED=false
CONJUGATE_SELF_DESCENT_SOLVED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
