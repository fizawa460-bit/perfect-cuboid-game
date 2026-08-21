# Stage29-02ha — full seven-line sign/Kummer-cover foundation

## Verdict at submission

```text
ROUTE=FULL_ENDPOINT_AS_Z2^6_KUMMER_COVER_OF_P2_BRANCHED_ON_SEVEN_LINES
NOVELTY_IN_REPO=HIGH_VALUE_NEW_UNIFYING_FOUNDATION
LITERATURE_NOVELTY_CLAIM=false
AUDIT_REQUIRED=true
```

The four canonical cuboid quadrics admit a second global base geometry that is distinct from the Stage28 toric `Y`, the Beauville irregular cover, and the modular `M(4,8)` model:

\[
\bar S\to\mathbf P^2,
\qquad
[a_1:a_2:a_3:b_1:b_2:b_3:c]\mapsto[a_1^2:a_2^2:a_3^2].
\]

The endpoint is generically a degree-64 `(Z/2)^6` sign/Kummer cover branched along

\[
xyz(x+y)(x+z)(y+z)(x+y+z)=0.
\]

This follows directly from the endpoint equations and therefore has full endpoint coverage; it is not a parametrized thin family.

## Exact structural recoveries

### 1. Canonical class and `K^2`

The uniform order-two branch formula gives

\[
K=\pi^*(-3H+7H/2)=\pi^*(H/2)=O_{\bar S}(1),
\]

and

\[
K^2=64/4=16,
\]

recovering the audited canonical embedding and invariant.

### 2. All 48 nodes from one arrangement ledger

The seven lines have exactly

```text
6 triple points
3 ordinary double points.
```

Over each triple point the local sign cover has an `A1` model and eight geometric points above it. Hence

\[
6\cdot8=48
\]

`A1` nodes, exactly the Testa–Stoll singularity count.

### 3. The seven coordinate K3 quotients

Quotienting by the sign of one canonical coordinate removes that line from the branch set. The resulting coordinate quotient is a degree-32 `(Z/2)^5` cover of `P^2` branched on six lines, for which

\[
K=\pi^*(-3H+6H/2)=0.
\]

Together with the source-certified resolutions, this identifies all seven coordinate quotients as the six-line K3 subcovers of the one seven-line endpoint tower.

The Q-visible line partition

```text
A1,A2,A3 / B1,B2,B3 / C
```

matches the audited

```text
3*K_a + 3*K_b + 1*K_c
<-> 3*h8 + 3*h16 + 1*h32.
```

The geometric arrangement symmetry has order 24 and line orbits `4+3`; the four-orbit is `{A1,A2,A3,C}`, consistent with the source fact that the A- and C-type K3s become isomorphic after adjoining `i`.

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

Thus perfect-cuboid existence becomes an exact positive-chamber rational-point problem on `P^2` with a six-coordinate Kummer torsor class. No family-coverage issue remains at this adapter.

### 5. The old population tower becomes a subcover tower

Once a chosen two-face host is lifted, the two missing endpoint conditions are literally the remaining square roots for the third face and the space diagonal. Generically they form a V4 extension. This creates a direct new receiver to identify the Stage28 joint V4 as the residual two-character quotient of the full sign tower.

Likewise Stage16–20 condition masks can be represented as partial square-root lifts inside one `(Z/2)^6` subcover lattice, subject to separate physical height/primitivity adapters.

## New receivers

```text
R29-KUM0  = FullEndpointAsSevenLineZ2^6KummerCover
R29-KUM0A = SevenLineIncidenceLedger
R29-KUM0B = SixTriplePointsTimesEightEquals48A1
R29-KUM1  = ExactBasePlaneSquareclassTorsorCriterion
R29-KUM2  = CoordinateK3AsSixLineKummerSubcovers
R29-KUM2A = ArithmeticThreeOneThreeFromBranchLineQOrbits
R29-KUM3A = TwoFaceSignSubcoverToStage28ToricYBirationalAdapter
R29-KUM3B = JointV4AsResidualTwoSquareRootsOfFullSignTower
R29-KUM4  = Stage16To20PopulationMaskAsSignSubcoverLattice
R29-KUM5  = ArrangementS4VsModularLevel4ResidualS4Identification
R29-KUM-LOC1 = SevenLinearFormCommonSquareclassLocalDensity
R29-KUM-LOC2 = BranchValuationTransitionLedger
```

Submission grading:

```text
KUM0=PASS_CANDIDATE_DIRECT
KUM0A=PASS_CANDIDATE_EXACT
KUM0B=PASS_CANDIDATE_EXACT_LOCAL
KUM1=PASS_CANDIDATE_DIRECT
KUM2=PASS_CANDIDATE
KUM2A=PASS_CANDIDATE_NEEDS_Q_LIFT_SCOPE_AUDIT
KUM3A=OPEN_HIGH_VALUE
KUM3B=PASS_FORMAL_CONDITIONAL_ON_KUM3A
KUM4=NEW_TARGETED_BACKFLOW_RECEIVER
KUM5=OPEN_PROMISING
```

## Firewalls

The physical-open scheme from Stage29-02f is larger geometrically than `P^2\D`: over Q-points with nonzero rational edges the extra four branch lines cannot vanish, so the seven-line complement is safe for physical rational-point lifting, but no scheme-level equality of the two opens is asserted.

The order-24 arrangement symmetry and the order-24 modular residual group from Stage29-02g are not identified merely because both are abstractly `S4`; this is explicitly left as `R29-KUM5`.

No old Stage14 analytic gate is reopened and no local-density saving is multiplied with earlier population savings without a matched measure/height adapter.

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
OLD_GATE_REPLAY=false
BACKFLOW_EXECUTED=false
NEW_BACKFLOW_RECEIVER_CREATED=true
```

## Routing

Because a genuinely new HIGH_VALUE foundation was found after the nominal `a..g` pass, the Stage29-02 mining stop condition is **not** satisfied.

After fresh audit PASS, continue foundation mining at

```text
NEXT_ITEM=29-02hb
```

rather than advancing immediately to `29-03`. `29-03` remains the later checkpoint once new HIGH_VALUE foundations dry up.
