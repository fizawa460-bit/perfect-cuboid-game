# Stage29-11 — fresh adversarial audit

```text
PR=1318
SUBMISSION_HEAD=36d96afef76597deac04386ced0b062300c8387d
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Scope

Fresh audit covered the four 29-11 attack owners, their exact Q/field-of-definition semantics, Campedelli involution geometry, Beauville twist scope, modular defect compression and residual action, proper versus physical-open Brauer arithmetic, ownership/double-charge rules, and current source provenance.

## 1. Campedelli — PASS with positive child discharge

The audited Stage29-02hb adapter already proves that every admissible rank-three kernel is Q-defined and gives the same global factorization of the endpoint sign cover. On resolutions,

```text
S -> C_H
```

is finite etale degree eight. Hence every endpoint Q-point pushes forward to every audited `C_H(Q)`. This implication does not require a converse torsor lift.

Fresh source audit of Calabri--Mendes Lopes--Pardini verifies the new proposed geometric split. For a classical Campedelli surface, all involutions are composed with the bicanonical map; the resulting quotient is geometrically rational or birational to an Enriques surface. Since the classical deck group is `(Z/2)^3`, this applies to all seven nontrivial involutions.

Therefore the child receiver is genuinely discharged:

```text
R29-CAMP3-GEOM=DISCHARGED_GEOMETRIC_RATIONAL_OR_ENRIQUES_DICHOTOMY
```

The stronger arithmetic parent is not discharged. The source does not determine the exact rational-versus-Enriques assignment for each cuboid inherited Q-form, does not prove a geometric rational model descends to a Q-rational parametrization, and does not make any `C_H(Q)` empty. Thus

```text
R29-CAMP3=PARTIAL_GEOMETRIC_DONE_Q_FORM_AND_EXACT_INVOLUTION_ASSIGNMENT_OPEN
R29-CAMP2=OPEN_H_TORSOR_DESCENT
R29-CAMP4=OPEN
Q11-CAMPEDELLI=AMBER
```

The exact kernel census remains ten, with `8+2` geometric/Q(i) orbits and `6+2+2` certified-Q S3 orbits. No exact Q-isomorphism-class count is inferred.

## 2. Beauville — PASS with locator provenance repair

The audited Q-defined degree-two physical-open cover, constant `Z/2` deck group, pointwise torsor class

```text
delta(P) in Q*/Q*^2
```

and union-over-twists identity all remain exact. No theorem was found forcing the occurring physical squareclasses into a finite set, and the existing genus-two Selmer/Cassels--Tate tools do not supply uniform closure over this point-dependent family.

The previously audited swap/Weil-restriction Albanese target remains valid, while V4-kernel swap equivariance and Q-CM/twist arithmetic remain open.

Fresh source comparison finds a bibliographic discrepancy only: the currently surfaced Beauville PDF places the etale `(Z/2)^2` tower and Albanese pullback in `Remark 2`, whereas the historical 29-02d audit recorded `Remark 1`. The mathematical tower had already been independently audited, so this is recorded as provenance rather than reopening 29-02d.

```text
FINITE_TWIST_SET_PROVED=false
R29-BEAU2A=OPEN_BOUNDED
Q11-BEAUVILLE=AMBER
```

## 3. Modular — PASS

The exact audited data survive unchanged:

```text
K8=ker(SL2(Z/8)->SL2(Z/4)), |K8|=8,
ordinary symplectic conjugacy class sizes=1,3,3,1,
generic forgetting degree=24,
generic residual group=S4.
```

The 29-02g audit already records that the four ordinary conjugacy classes are not the exact arithmetic endpoint strata until the retained sigma-twisted level-4 sign action is incorporated. No completed computation closing that gap was found.

Likewise, equality of the abstract arrangement and modular residual groups as `S4` is not an action-level or Q-descent-cocycle adapter. Therefore

```text
R29-MOD1C=OPEN
R29-MOD1D=OPEN
R29-MOD2B=OPEN
R29-KUM5=OPEN_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER
Q11-MODULAR=AMBER
```

The ordinary 8-congruence obstruction remains a valid RED subroute, not a RED classification of the parent modular portfolio.

## 4. Brauer — PASS

The current Testa--Stoll cuboid PDF was checked directly: its Theorem 10 states that the algebraic Brauer group of the smooth proper surface is the image of `Br(Q)`. The Stage29-02f derived odd-primary proper transcendental exclusion remains separately audited.

These proper-surface results do not compute the physical-open Brauer group. The 72-component boundary, extended Picard complex, absolute-Galois unit terms, Gersten residues and two-primary evaluation maps remain open. No current source was found giving a Brauer--Manin obstruction on the physical endpoint open.

```text
R29-BR0A=OPEN
R29-BR0B=OPEN
R29-BR0G=OPEN
R29-BR2A=OPEN
R29-BR2B=OPEN
BRAUER_MANIN_OBSTRUCTION_PROVED=false
Q11-BRAUER=AMBER
```

`NF-PHYS2`, `QWEB-CLIFFORD` and `NF7` remain tools/adapters, not certified obstructions.

## 5. Ownership / final colors

No 29-12 joint-V4, local-squareclass, parametric or population-interaction result is re-credited. Campedelli-specific Brauer work stays subordinate to the primary Brauer owner when it becomes a Brauer computation. `R29-KUM5` remains under Q11-MODULAR.

No genuinely new primary mechanism was found, so the route count remains eleven.

```text
Q11_CAMPEDELLI=AMBER
Q11_BEAUVILLE=AMBER
Q11_MODULAR=AMBER
Q11_BRAUER=AMBER
R29_CAMP3_GEOM=DISCHARGED_GEOMETRIC_RATIONAL_OR_ENRIQUES_DICHOTOMY
R29_CAMP3=PARTIAL_GEOMETRIC_DONE_Q_FORM_AND_EXACT_INVOLUTION_ASSIGNMENT_OPEN
R29_KUM5=OPEN_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER
ATTACK_ROUTE_COUNT=11
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
```

## Verdict

The submission's four parent colors survive. The only repairs are the positive certification of the bounded Campedelli geometric child split and current Beauville source-locator provenance. Neither produces an endpoint obstruction.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
BOUNDED_REPAIR=CAMPEDELLI_GEOMETRIC_SPLIT_CERTIFICATION_PLUS_BEAUVILLE_CURRENT_LOCATOR_PROVENANCE
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-12_JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
