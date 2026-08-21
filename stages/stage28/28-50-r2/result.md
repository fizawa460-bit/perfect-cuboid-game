# Stage28-50-r2 — maximal post-merge lower/construction deepening

```text
TASK_ID=Stage28-50-r2
CHECKPOINT=50
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Strongest new candidate theorem

The audited parent checkpoint proved

\[
M_3(B)\gg B^{1/3}.
\]

The r2 deepening sharpens this within the same generalized Saunderson mechanism.  Exact height algebra gives

\[
R\le 8r^6
\]

for Euclid parameters `(r,s)`.  On the cone

\[
1/8\le s/r\le4/5,
\]

the cube face diagonal `w^3` is uniquely the smallest physical face diagonal, making the physical output map injective on this cone.

The cone contains

\[
\frac{27}{20\pi^2}T^2+O(T\log T)
\]

primitive opposite-parity Euclid pairs with `r<=T`.  Therefore

\[
\boxed{
M_3(B)\ge\left(\frac{27}{40\pi^2}+o(1)\right)B^{1/3}
}
\]

and in particular

\[
\boxed{
\liminf_{B\to\infty}M_3(B)/B^{1/3}\ge27/(40\pi^2)>0.
}
\]

This is an explicit-coefficient strengthening, not a new exponent.

```text
M3_EXPLICIT_ONE_THIRD_LIMINF_COEFFICIENT_CANDIDATE=27/(40*pi^2)
SAUNDERSON_INJECTIVE_POSITIVE_DENSITY_CONE_CANDIDATE=true
SAUNDERSON_HEIGHT_CONSTANT_72_TO_8_CANDIDATE=true
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
```

## 2. No new exponent from the classical family inventory

The materially distinct closed-form families checked beyond the parent batch do not beat Saunderson's parameter/height efficiency:

```text
Saunderson: degree6 / two Euclid parameters -> 1/3
Rule1 transform: degree8 -> <=1/4
Lenhart/Piezas: degree8 after conic parametrization -> 1/4
```

Bremner's quartic-surface framework supplies many additional parametrizations, but the checked literature does not provide a matched primitive/canonical `R<=B` family with `kappa/h>1/3`.

## 3. Himane does not provide four free parameters

Himane T1-T3 start from two Pythagorean triples but require an additional mixed square equation.  No positive-density theorem for coupled pairs is supplied.  Counting both triples as independent would double-count freedom that the coupling removes.

```text
HIMANE_FREE_FOUR_PARAMETER_LOWER=false
HIMANE_KAPPA_OVER_H_GT_ONE_THIRD_PROVED=false
```

## 4. Peschmann's large Mordell-Weil output remains a height-count gate

Peschmann 2026 rigorously generates more than one million finite Master-Hits over hundreds of elliptic fibres.  The work does not give a uniform physical-height counting theorem as `(m,n)` varies, and explicitly identifies height/discriminant control as a missing ingredient.

The precise remaining theorem species is

```text
UniformMovingEllipticFibreSquareLiftHeightCount
```

for points `P in E_{m,n}(Q)` with the lift function `tau(P)` a positive rational square, uniformly in the moving base and under the primitive/canonical physical cutoff `R<=B`.

## 5. Stage19 branch-profile shortcut is unavailable

The four rational geometric branch components discovered at checkpoint40 do not meet the positive physical real torus: the real branch polynomial is a product of strictly positive sums of squares there.  Thus geometric rationality of the branch divisor does not by itself generate a positive physical `N2` family.

```text
SPACE_BRANCH_RATIONAL_COMPONENTS_SEED_PHYSICAL_N2=false
N2_KNOWN_CONSTRUCTION_EXPONENT=1/4
N2_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
```

## 6. Construction comparison after r2

The strongest explicit lower mechanisms remain

```text
Stage19 N2 known family exponent = 1/4
Stage20 M3 known family exponent = 1/3 with explicit positive liminf coefficient candidate
```

The selected-family exponent gap remains `1/12`.  It still does not order the full populations because neither true exponent is known.

The bridge lower also remains, for every fixed `epsilon>0`,

\[
M_3(B)/N_2(B)\gg_\epsilon B^{-1/6-\epsilon},
\]

since the epsilon now comes from the current `N2` upper rather than the `M3` lower.

## 7. Maximal bounded exploration status

Checkpoint50 has now tested fourteen materially distinct lower/construction lanes across the parent and r2 batches.  The new r2 work includes one genuine theorem strengthening candidate and six negative/boundary certificates.

The remaining legal lower receiver is

```text
OPEN_GATE_50_R2=HigherEfficiencyOffBranchPhysicalConstructionOrUniformMovingEllipticSquareLiftCount
M3_PROGRESS_GATE=kappa/h>1/3
N2_PROGRESS_GATE=kappa/h>1/4
REQUIRED_OUTPUT=strict exponent improvement or direct same-host marginal lower comparison
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

Blindly trying more named classical formulas without a better degree/freedom ratio is no longer a distinct route.  Further progress requires a genuinely denser off-branch construction or a moving-elliptic height/count theorem.

```text
MATERIALLY_DISTINCT_LOWER_ROUTES_TOTAL=14
CHECKPOINT50_R2_MAXIMAL_BOUNDED_EXPLORATION_CLAIM=true
M3_EXPONENT_ABOVE_ONE_THIRD_PROVED=false
N2_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=60
NEXT_EXPECTED_COMMAND=Stage28-audit
```
