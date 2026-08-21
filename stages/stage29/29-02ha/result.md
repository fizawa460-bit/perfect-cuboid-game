# Stage29-02ha — audited full seven-line sign/Kummer-cover foundation

```text
ROUTE=FULL_ENDPOINT_AS_Z2^6_KUMMER_COVER_OF_P2_BRANCHED_ON_SEVEN_LINES
NOVELTY_IN_REPO=HIGH_VALUE_NEW_UNIFYING_FOUNDATION
LITERATURE_NOVELTY_CLAIM=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

The four canonical cuboid quadrics admit a second global base geometry distinct from the Stage28 toric `Y`, the Beauville irregular cover, and the modular `M(4,8)` model:

\[
\bar S\to\mathbf P^2,
\qquad
[a_1:a_2:a_3:b_1:b_2:b_3:c]\mapsto[a_1^2:a_2^2:a_3^2].
\]

The endpoint is generically a degree-64 `(Z/2)^6` sign/Kummer cover branched along

\[
xyz(x+y)(x+z)(y+z)(x+y+z)=0.
\]

This follows directly from the endpoint equations and has full endpoint coverage; it is not a parametrized thin family.

## Audited structural recoveries

### 1. Exact cover, canonical class, and `K^2`

The six generic squareclasses are independent, so the generic degree is exactly `64` and the deck group is `(Z/2)^6`.

Finite-cover Riemann--Hurwitz gives

\[
K_{\bar S}=\pi^*(K_{\mathbf P^2}+D/2)
=\pi^*(H/2)=O_{\bar S}(1),
\]

without requiring the seven-line branch divisor to be simple normal crossing at the six triple points. Hence

\[
K^2=64/4=16.
\]

```text
R29-KUM0=DISCHARGED
CANONICAL_CLASS_AUDIT=PASS
```

### 2. All 48 nodes and their fields of definition

The seven lines have exactly

```text
6 triple points
3 ordinary double points.
```

At every triple point the local three-root cover is

```text
u^2=r,
v^2=s,
w^2=r+s
=> w^2=u^2+v^2,
```

so each geometric point above the triple point is an `A1` node. The local inertia has order `8`, hence each triple point has eight geometric points above it:

```text
6 * 8 = 48 A1 nodes.
```

Fresh audit also resolves the arithmetic scope omitted at submission:

```text
24 nodes are Q-defined,
24 nodes are strictly Q(i)-defined.
```

The three coordinate triple fibers contribute the rational 24; the other three fibers carry the single `-1` squareclass obstruction and require `i`.

```text
R29-KUM0A=DISCHARGED
R29-KUM0B=DISCHARGED
NODE_FIELD_SPLIT=24_Q_PLUS_24_STRICT_QI
```

### 3. Seven K3 subcovers and exact Q/Q(i) symmetry

Quotienting by one coordinate sign removes that branch line. Each coordinate quotient is therefore a degree-32 `(Z/2)^5` cover of `P^2` branched on the other six lines, with canonical class zero; Testa--Stoll independently certify that the minimal resolutions are K3 surfaces.

The fresh audit strengthens the arrangement symmetry substantially. All 24 incidence automorphisms are actual `PGL_3(Q)` automorphisms of the base seven-line arrangement:

```text
Aut_P2(D) ~= S4.
```

But a base projectivity lifts to the sign cover over `F` only when its seven branch-line multipliers have one common squareclass in `F*/F*^2`. Exhaustive exact calculation gives

```text
Q-liftable base subgroup:      S3, order 6
Q(i)-liftable base group:      S4, order 24.
```

Thus the quotient-line orbits are exactly

```text
Q:     3 + 3 + 1
Q(i):  4 + 3,
```

which recovers the audited arithmetic pattern

```text
3*K_a + 3*K_b + 1*K_c
<-> 3*h8 + 3*h16 + 1*h32
```

and explains why `K_a` and `K_c` merge only after adjoining `i`.

Since the sign deck group has order `64`, the construction gives a geometric automorphism subgroup of order

```text
64 * 24 = 1536.
```

Testa--Stoll Theorem 1 independently proves that the full geometric automorphism group has exactly order `1536` and exact sequence

```text
1 -> mu_2^7/mu_2 -> Aut(Sbar) -> S4 -> 1.
```

Therefore the sign/Kummer construction recovers the full geometric automorphism group.

```text
R29-KUM2=DISCHARGED
R29-KUM2A=DISCHARGED
FULL_GEOMETRIC_AUT_ORDER_RECOVERED=1536
```

### 4. Exact rational lifting criterion

On the complement of all seven branch lines, a rational base point lifts exactly when

\[
\left[
\frac{x}{x+y+z},
\frac{y}{x+y+z},
\frac{z}{x+y+z},
\frac{x+y}{x+y+z},
\frac{x+z}{x+y+z},
\frac{y+z}{x+y+z}
\right]
\]

is trivial in `(Q*/Q*^2)^6`.

Equivalently, the seven branch values have one common rational squareclass. A positive rational lift can be homogenously cleared of denominators to give an integral cuboid candidate, followed by primitive normalization.

```text
R29-KUM1=DISCHARGED
FULL_ENDPOINT_COVERAGE=true
```

### 5. Exact local host

For every odd prime the seven-line incidence pattern remains `t3=6,t2=3`, so

\[
\#(\mathbf P^2\setminus D)(\mathbf F_p)=(p-3)^2.
\]

At a nonbranch `F_p` point, the fiber has an `F_p` point iff the six reference ratios are squares. This is an exact fixed seven-linear-form character-sum receiver. No local-density saving is yet claimed.

```text
R29-KUM-LOC1=OPEN_DOWNSTREAM_EXACT_CHARACTER_SUM
R29-KUM-LOC2=OPEN_DOWNSTREAM_BRANCH_VALUATION_LEDGER
LOCAL_DENSITY_SAVING_PROVED=false
```

## Bridge receivers retained

The sign tower creates real new interfaces but does not erase their adapters:

```text
R29-KUM3A = TwoFaceSignSubcoverToStage28ToricYBirationalAdapter
R29-KUM3B = JointV4AsResidualTwoSquareRootsOfFullSignTower
R29-KUM4  = Stage16To20PopulationMaskAsSignSubcoverLattice
R29-KUM5  = ArrangementS4VsModularResidualS4ActionAndQDescentCocycle
```

Current audited status:

```text
KUM3A=OPEN_HIGH_VALUE
KUM3B=FORMAL_CONDITIONAL_ON_KUM3A
KUM4=NEW_TARGETED_BACKFLOW_RECEIVER_NOT_EXECUTED
KUM5=OPEN_BOUNDED
```

The published automorphism exact sequence makes the arrangement/modular `S4` coincidence much more structured, but the exact action-level identification and Q-descent cocycle are not promoted without a dedicated adapter.

No old Stage14 analytic gate is reopened, and no local saving is multiplied with prior population savings without a matched physical-height/measure adapter.

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
BACKFLOW_EXECUTED=false
```

## Routing

PR #1302 merged during this audit and correctly removed the automatic transition to `29-03`. The new `29-02ha` result itself demonstrates that high-value foundation yield has not yet dried up, so the audited route is

```text
AUTO_ADVANCE_TO_29_03=false
STAGE29_02_EXTENSION_NAMESPACE_OPEN=true
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
NEXT_ITEM=29-02hb
NEXT_EXPECTED_COMMAND=Stage29-main-batch
```

`29-03` remains the later checkpoint once further independent foundation mining stops producing high-value structures.

## Final state

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
