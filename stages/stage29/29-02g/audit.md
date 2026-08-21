# Stage29-02g — fresh audit

```text
AUDITED_PR=1301
AUDITED_SUBMISSION_HEAD=9ce142dfb558ae34f92da6ee3f4dfe3c08055d02
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Verdict

The Testa--Stoll Q-moduli datum is source-exact, the ordinary-8-congruence firewall is valid, the generic quotient index is 24, and the kernel

```text
K8=ker(SL2(Z/8)->SL2(Z/4))
```

has eight elements with four ordinary symplectic conjugacy classes of sizes `1,3,3,1`.

Two scope repairs are load-bearing:

1. the `degree 24 / S4` statement is a generic function-field quotient statement, not an everywhere finite morphism between arbitrary chosen compactifications;
2. the four `K8` conjugacy classes are an abstract symplectic conjugacy classification. They are not yet certified to be exactly the four arithmetic equivalence strata of Q-rational endpoint descent data, because the retained level-4 sign datum and the sigma-twisted descent action still have to be incorporated.

These repairs preserve the modular compression while leaving the genuinely arithmetic work in `R29-MOD1C` and special-locus bookkeeping in `R29-MOD1D/R29-MOD2B`.

## Source audit

Testa--Stoll Section 4 states that the genus-5 curve `X` is a model of `X(8)`, that

```text
Aut_geom(X)=PSL2(Z/8), |PSL2(Z/8)|=192,
ker(PSL2(Z/8)->PSL2(Z/4))=G0~=(Z/2)^3,
PSL2(Z/4)~=S4,
```

and that over `Q(i)`

```text
Sbar ~= (X(8) x X(8))/Delta G0.
```

The same section gives the exact Q-form and the rational-point datum

```text
E/Q(i),
(P1,P2) basis of E[4],
psi:E[8]->Ebar[8],
psi(P1)=Pbar1,
psi(P2)=-Pbar2.
```

Thus

```text
R29-MOD1A=DISCHARGED_ON_NONCUSP_FINE_MODULI_LOCUS
```

with cusp/extra-automorphism bookkeeping retained in `R29-MOD1D`.

Fisher defines `Z(8,1)` as the ordinary symplectic 8-congruence surface up to simultaneous quadratic twist, proves it rational over Q, and Corollary 1.3 gives infinitely many non-isogenous rational 8-congruent pairs. Therefore bare ordinary 8-congruence cannot itself supply a rarity/nonexistence obstruction.

```text
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED_AUDITED
```

## Generic degree-24 quotient

The diagonal quotient chain over `Q(i)` is

```text
(X x X)/Delta G0
  --> (X x X)/Delta PSL2(Z/8).
```

Since `G0` is normal and the quotient is `PSL2(Z/4)~=S4`, the generic function-field extension has degree

```text
[PSL2(Z/8):G0]=192/8=24
```

and generic Galois group `S4` on the locus with trivial stabilizer.

The target is the ordinary symplectic 8-congruence moduli surface birationally represented by Fisher's `Z(8,1)`; Fisher only fixes `Z(8,1)` up to birational equivalence. Hence the audited statement is

```text
R29-MOD2=DISCHARGED_GENERIC_BIRATIONAL_QUOTIENT
GENERIC_DEGREE=24
GENERIC_RESIDUAL_GROUP=S4
EVERYWHERE_FINITE_COVER_CLAIM=false
```

Branch, cusp and stabilizer behavior remains `R29-MOD2B`.

## Conjugation defect

For the exact Testa--Stoll datum define

```text
kappa=psi^sigma o psi:E[8]->E[8].
```

The level-4 sign identities imply that `kappa` fixes `E[4]` pointwise. Since the torsion correspondence is symplectic, after choosing a symplectic level-8 basis,

```text
kappa in K8=ker(SL2(Z/8)->SL2(Z/4)).
```

Every element is uniquely

```text
I+4A mod 8,
A in sl2(F2),
```

so `|K8|=8`. Under ordinary conjugation by the full symplectic basis-change group, the reduction action is `SL2(F2)` and the eight matrices split into four conjugacy classes:

```text
1,3,3,1.
```

The committed checker reproduces this exactly.

The bounded repair is interpretive: the endpoint datum also retains an asymmetric level-4 sign operator under sigma. A basis change preserving a fixed displayed sign normal form is not automatically the full `SL2(F2)` action. Therefore the four ordinary conjugacy classes are a valid invariant compression of possible `kappa`, but are not yet promoted to the exact arithmetic quotient of rational endpoint descent data.

```text
R29-MOD1B=DISCHARGED_AS_ABSTRACT_K8_CONJUGACY_CLASSIFICATION
ARITHMETIC_DEFECT_STRATA_EXACTLY_FOUR_PROVED=false
R29-MOD1C=TwistedSigmaDescentActionAndArithmeticAnalysisOfK8Classes
```

## Routing

This suffix sharpens the already accepted F5 modular foundation and does not constitute a new independent `ha`-grade foundation. No Stage16--28 reentry follows directly from 02g; the next planned item `29-03` is exactly the checkpoint that decides whether any targeted backflow is justified.

PR #1300 / Stage29-02f is already merged and the controller is synchronized during this audit.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02G_AUDIT=PASS
BOUNDED_REPAIR=GENERIC_BIRATIONAL_DEGREE24_SCOPE_PLUS_TWISTED_DEFECT_ORBIT_SCOPE
R29_MOD1A=DISCHARGED_GENERIC_MODULI_LOCUS
R29_MOD1B=DISCHARGED_ABSTRACT_K8_CONJUGACY
R29_MOD2=DISCHARGED_GENERIC_BIRATIONAL_QUOTIENT
ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED
GENERIC_DEGREE24=PASS
ARITHMETIC_DEFECT_STRATA_EXACTLY_FOUR_PROVED=false
NEW_HA_GRADE_FOUNDATION_FOUND=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-03
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
