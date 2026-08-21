# Stage29-02ha — fresh audit

```text
AUDITED_PR=1303
AUDITED_SUBMISSION_HEAD=042f6beaea577343240b7e18a01964de7012ce64
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Verdict

The seven-line sign/Kummer model is exact and genuinely useful as a new Stage29 foundation. The core claims all survive fresh audit:

```text
Sbar -> P2 is generically degree 64
G_sign ~= (Z/2)^6
branch divisor = xyz(x+y)(x+z)(y+z)(x+y+z)=0
K_Sbar = O_Sbar(1)
K^2=16
six triple points produce exactly 48 geometric A1 nodes
coordinate-sign quotients are the seven six-line K3 subcovers
rational lifting on the branch complement is exactly a six-squareclass torsor condition
```

The audit makes two bounded field-of-definition repairs and strengthens the symmetry package.

## 1. Generic cover and canonical class

On the chart `z!=0`, the endpoint function field is obtained from `Q(x/z,y/z)` by adjoining six independent squareclasses represented by the six nonconstant linear forms relative to `z`. Distinct irreducible branch divisors make these classes independent in the generic squareclass group. Thus the generic degree is exactly `2^6=64` and the deck group is the coordinate-sign group modulo common projective sign.

For the canonical divisor, no simple-normal-crossing assumption at the triple points is needed. Finite-cover Riemann--Hurwitz gives

```text
K_Sbar = pi^*K_P2 + R
pi^*D_i = 2 R_i
=> K_Sbar = pi^*(K_P2 + D/2).
```

With `D~7H` and `pi^*H=2 O_Sbar(1)`, this gives

```text
K_Sbar=O_Sbar(1),
K^2=64*(1/2)^2=16.
```

The A1 singularities are crepant.

```text
R29-KUM0=DISCHARGED
CANONICAL_CLASS_AUDIT=PASS
```

## 2. Incidence, A1 nodes, and node fields

The arrangement has exactly six triple points and three double points. At a triple point the local three-root model is

```text
u^2=r,
v^2=s,
w^2=r+s
=> w^2=u^2+v^2,
```

an A1 quadratic cone. The local inertia has order eight, so every triple point has eight **geometric** points above it and

```text
6*8=48
```

geometric A1 nodes.

The field scope omitted at submission is now explicit. The three coordinate triple fibers have one rational squareclass and contribute `24` Q-defined nodes. The other three triple fibers have a `-1` squareclass obstruction and contribute `24` nodes defined over `Q(i)` but not `Q`.

```text
R29-KUM0A=DISCHARGED
R29-KUM0B=DISCHARGED
NODE_FIELD_SPLIT=24_Q_PLUS_24_STRICT_QI
```

This independently recovers the exceptional-node field split already used in Stage29-02f.

## 3. Base S4, cover lifts, and the full automorphism group

The submission computed the incidence automorphism group abstractly. Fresh audit strengthened this to projective and arithmetic statements.

Using the four-line projective frame `{A1,A2,A3,C}`, all `24` permutations extend to exact `PGL_3(Q)` transformations preserving all seven lines. Hence

```text
Aut_P2(D) ~= S4.
```

For a base projectivity with

```text
phi^* L_i = lambda_i L_sigma(i),
```

a lift to the sign cover over `F` exists exactly when all seven `lambda_i` have one common class in `F*/F*^2`. Exhausting all 24 projectivities gives

```text
Q-liftable base subgroup:      6 ~= S3
Q(i)-liftable base group:     24 ~= S4.
```

Thus the arithmetic line orbits are exactly

```text
Q:     3 + 3 + 1
Q(i):  4 + 3.
```

The sign deck group has order `64`, so the geometric sign-cover automorphism subgroup has order `64*24=1536`. Testa--Stoll Theorem 1 independently proves that the full geometric automorphism group has order `1536` and fits

```text
1 -> mu_2^7/mu_2 -> Aut(Sbar) -> S4 -> 1.
```

Therefore the sign-cover construction recovers the full geometric automorphism group. This also closes the arithmetic orbit receiver left open in the submission:

```text
R29-KUM2=DISCHARGED
R29-KUM2A=DISCHARGED
Q_LIFTABLE_BASE_SUBGROUP=S3
QI_LIFTABLE_BASE_GROUP=S4
FULL_GEOMETRIC_AUT_ORDER_RECOVERED=1536
```

## 4. Exact rational lifting criterion

On `A=P2\D`, choose `L_c=x+y+z` as reference. For `q in A(Q)`, the fiber has a Q-point iff

```text
x/L_c,
y/L_c,
z/L_c,
(x+y)/L_c,
(x+z)/L_c,
(y+z)/L_c
```

are all rational squares. Equivalently all seven branch values have one common rational squareclass. This is precisely the triviality criterion for the `(Z/2)^6` fiber torsor.

For a positive rational lift, homogeneous clearing of denominators produces an integral cuboid candidate; primitive normalization can then be applied. This is a full-coverage endpoint adapter, not a thin-family parametrization.

```text
R29-KUM1=DISCHARGED
FULL_ENDPOINT_COVERAGE=true
```

## 5. Local finite-field adapter

For every odd prime the seven lines remain distinct with the same six-triple/three-double incidence. Inclusion--exclusion therefore gives

```text
#(P2\D)(F_p)=(p-3)^2.
```

For a nonbranch base point, an `F_p` lift exists iff the six reference ratios are squares, equivalently the seven values have one common quadratic character. This is an exact downstream character-sum receiver, not yet a computed density theorem.

```text
R29-KUM-LOC1=OPEN_DOWNSTREAM_EXACT_CHARACTER_SUM
R29-KUM-LOC2=OPEN_DOWNSTREAM_BRANCH_VALUATION_LEDGER
LOCAL_DENSITY_SAVING_PROVED=false
```

## 6. Bridges and residual receivers

The new tower does not by itself identify the Stage28 toric base or transfer population asymptotics. Those remain explicit adapters:

```text
R29-KUM3A=TwoFaceSignSubcoverToStage28ToricYBirationalAdapter
R29-KUM3B=JointV4AsResidualTwoSquareRootsOfFullSignTower
R29-KUM4=Stage16To20PopulationMaskAsSignSubcoverLattice
```

`R29-KUM3B` is formally correct after `KUM3A`; the exact boundary/height/multiplicity adapter is still load-bearing. `R29-KUM4` is a genuinely new targeted-backflow receiver, but **backflow has not been executed**.

The arrangement `S4` and the Stage29-02g modular residual `S4` are now much less mysterious: Testa--Stoll's published automorphism exact sequence supplies the same `S4` quotient on the cuboid surface. However, the exact identification with the specific modular residual action and its Q-descent cocycle is not promoted without a dedicated action-level adapter.

```text
R29-KUM5=OPEN_BOUNDED_ACTION_AND_Q_COCYCLE_IDENTIFICATION
BACKFLOW_TO_STAGE16_28=false
BACKFLOW_EXECUTED=false
```

## 7. Routing and controller synchronization

During this audit PR #1302 merged, correcting the earlier unauthorized automatic transition to `29-03`. The audited 29-02ha route is consistent with that policy:

```text
AUTO_ADVANCE_TO_29_03=false
STAGE29_02_EXTENSION_NAMESPACE_OPEN=true
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
NEXT_ITEM=29-02hb
NEXT_EXPECTED_COMMAND=Stage29-main-batch
```

The reason for continuing is concrete rather than cosmetic: `29-02ha` itself is a HIGH_VALUE full-coverage unifying foundation discovered after the nominal `a..g` screen. `29-03` remains available after high-value foundation yield drops.

## Final audit state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02HA_AUDIT=PASS
BOUNDED_REPAIR=GEOMETRIC_NODE_FIELD_SCOPE_PLUS_EXACT_Q_QI_SYMMETRY_LIFT
SOURCE_LOCK_AUDIT=PASS
R29_KUM0=DISCHARGED
R29_KUM0A=DISCHARGED
R29_KUM0B=DISCHARGED
R29_KUM1=DISCHARGED
R29_KUM2=DISCHARGED
R29_KUM2A=DISCHARGED
R29_KUM3A=OPEN_HIGH_VALUE
R29_KUM3B=FORMAL_CONDITIONAL_ON_KUM3A
R29_KUM4=NEW_TARGETED_BACKFLOW_RECEIVER
R29_KUM5=OPEN_BOUNDED
R29_KUM_LOC1=OPEN_DOWNSTREAM
R29_KUM_LOC2=OPEN_DOWNSTREAM
NODE_FIELD_SPLIT=24_Q_PLUS_24_STRICT_QI
FULL_GEOMETRIC_AUT_ORDER_RECOVERED=1536
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
AUTO_ADVANCE_TO_29_03=false
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
NEXT_ITEM=29-02hb
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
