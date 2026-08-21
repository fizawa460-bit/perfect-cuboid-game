# Stage29-02g — audited modular / Q-descent source lock

```text
ROLE=MODULI_M4_8_Q_DESCENT_SOURCE_LOCK
STATUS=AUDITED_PASS_AFTER_SCOPE_REPAIR
```

## Primary endpoint source

Damiano Testa and Michael Stoll, *The surface parametrizing cuboids*, current accepted/published version of arXiv:1009.0388 / Math. Comp. DOI `10.1090/mcom/4238`, Section 4.

Audited load-bearing statements:

```text
X is a genus-5 model of X(8),
Aut_geom(X)=PSL2(Z/8), |PSL2(Z/8)|=192,
PSL2(Z/8)->PSL2(Z/4)~=S4,
kernel G0~=(Z/2)^3,
Sbar_Q(i)~=(X(8)xX(8))/Delta G0.
```

The same section gives the Q-form through Weil restriction and, on the noncuspidal modular locus, the Q-rational-point datum

```text
E/Q(i),
(P1,P2) basis of E[4],
psi:E[8]->Ebar[8],
psi(P1)=Pbar1,
psi(P2)=-Pbar2.
```

Source locator: current PDF Section 4, pp. 8--9. The generic-moduli/cusp scope is retained explicitly in the audit.

## Modular provenance

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), arXiv:1303.6495.

This remains independent provenance for the level `(4,8)` modular presentation. The exact Q-form used by this suffix is taken from Testa--Stoll.

## Ordinary 8-congruence firewall

Tom Fisher, *Explicit moduli spaces for congruences of elliptic curves*, Math. Z. 295 (2020), arXiv:1804.10195.

Fisher defines `Z(N,epsilon)` up to birational equivalence as the surface of N-congruent elliptic-curve pairs up to simultaneous quadratic twist. For `(N,epsilon)=(8,1)`, the ordinary symplectic 8-congruence surface is rational over Q; Corollary 1.3 gives infinitely many non-isogenous rational pairs.

```text
ORDINARY_8_CONGRUENCE_ALONE=RED_AUDITED
EXACT_CONJUGATE_SELF_LEVEL4_CONDITION_REQUIRED=true
```

## Audit scope locks

```text
MODULAR_INTERPRETATION_EXACT_ON_GENERIC_NONCUSP_LOCUS=true
GENERIC_DEGREE24_QUOTIENT_AUDITED=true
EVERYWHERE_FINITE_DEGREE24_COVER=false
ABSTRACT_K8_CONJUGACY_1_3_3_1_AUDITED=true
ARITHMETIC_DEFECT_STRATA_EXACTLY_FOUR_PROVED=false
Q_RATIONAL_POINT_SET_COMPUTED=false
CONJUGATE_SELF_DESCENT_SOLVED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
