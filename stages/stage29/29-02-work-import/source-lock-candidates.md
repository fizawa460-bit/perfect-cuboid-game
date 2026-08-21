# Stage29-02 Work import — primary-source audit lock

```text
ROLE=PRIMARY_SOURCE_AUDIT_LEDGER
STATUS=PASS_WITH_BOUNDED_SCOPE_REPAIR
AUDIT_RECORD=stages/stage29/29-02-work-import/audit.md
```

The independent Work report was used only to locate candidate sources. The following load-bearing interfaces were freshly checked before promotion.

## Freitag--Salvati Manni low-genus bound — PASS

Eberhard Freitag; Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1.

Audited theorem interface:

```text
C integral curve on the box variety
normalization -> C bijective
normalization genus = g
projective/canonical degree = d
=> d <= 176 + 16g.
```

The cuboid/box surface is the same endpoint projective surface used in Stage29. Bijective normalization is essential and leaves multibranch-at-node curves outside the theorem.

```text
FSM_THEOREM_3_1_AUDIT=PASS_EXACT
29_02C_LG1=SATISFIED_BY_PR1292_AUDIT
```

## Beauville irregular cover — PASS structural, arithmetic descent open

Arnaud Beauville, *A tale of two surfaces*, arXiv `1303.1910`, Proposition 1 and the cuboid specialization remarks.

Audited structural package:

```text
X=(C x C')/Gamma, Gamma=(Z/2)^2
q=4
pg=7
K^2=32
canonical map degree=2
canonical quotient=four-quadric cuboid surface with 48 nodes
etale (Z/2)^2 tower and Albanese map to an abelian fourfold
```

The complex/geometric structure is locked. Q-field-of-definition, rational lifting and twists are not solved and define `29-02d`.

## Testa--Stoll Theorem 10 — PASS with open-locus scope firewall

Damiano Testa; Michael Stoll, *Curves on the surface of cuboids*, Theorem 10.

Audited proper-surface statement:

```text
Br_1(S)/im Br(Q)=0
```

for the smooth minimal projective cuboid surface `S`. This kills nonconstant **algebraic Brauer classes on the proper surface**. It does not automatically compute the algebraic Brauer group of the physical open `U`, because deleting boundary divisors may introduce residue classes.

```text
PROPER_S_ALGEBRAIC_BRAUER_NONCONSTANT=ABSENT
PHYSICAL_OPEN_ALGEBRAIC_BRAUER_CLOSED=false
R29-BR0=PhysicalOpenBoundaryBrauerResidueAudit
```

## Modular `M(4,8)` interpretation — PASS as receiver

Freitag--Salvati Manni's `M(4,8)` description and Testa--Stoll Section 4 lock the relevant endpoint modular structure: level-4 data together with a compatible symplectic 8-torsion isomorphism, with the exact conjugate-self condition needed for Q-descent. Fisher's 8-congruence surfaces are retained as a firewall against treating ordinary 8-congruence as rare enough to solve the endpoint.

```text
R29-MOD1=ConjugateSelf8CongruenceWithLevel4QDescent
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED
```

## Horie--Yamauchi cohomology input — bounded use only

The endpoint L-function / rational semisimplified l-adic decomposition remains a valid input for 29-02e/02f, but it does not determine integral lattices, torsion, extensions or Brauer evaluation maps.

## Certification state

```text
WORK_REPORT_SELF_CERTIFYING=false
FRESH_PRIMARY_SOURCE_AUDIT_COMPLETED=true
LOAD_BEARING_SOURCE_LOCKS=PASS_WITH_BRAUER_SCOPE_REPAIR
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
