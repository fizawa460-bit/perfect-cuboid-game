# Stage19-50 — lower-bound / construction ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 counts the primitive canonical exactly-two-face population with integral space diagonal,
\[
N_2(B)=\#\mathcal A_2(B).
\]
Checkpoint40 certified the one-sided ceiling
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]
Checkpoint50 asks what lower bound or construction is actually certified on the same physical population.

## 1. Numerical-reuse preflight

The Stage14 numerical observatory is the canonical finite oracle for Stage19.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03 / AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_POPULATION_ADAPTER=select exact-two face mask from retained Stage14 integral-space ledger; d=R gives d<=B iff R<=B
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

No new census is launched.

## 2. Strongest certified finite lower floor

The exact Stage14-num census gives
\[
N_2(500{,}000{,}000)=3495.
\]
These are distinct primitive canonical Stage19 objects. Since the cutoff populations are nested in `B`, `N_2(B)` is monotone nondecreasing. Therefore the finite census implies the rigorous finite floor
\[
\boxed{N_2(B)\ge3495\qquad(B\ge500{,}000{,}000).}
\]

This is a constant lower bound obtained from a frozen exact finite census plus monotonicity. It is **not** an asymptotic lower law and does not imply `N_2(B)->infinity`.

The directional B500m counts
\[
(N_a,N_b,N_c)=(1374,1371,750)
\]
likewise give finite directional floors after that cutoff, but no directional asymptotic is promoted.

## 3. No certified unbounded or matching lower bound

The frozen Stage14 theorem interface explicitly supplies only
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]
and states that neither a matching lower bound nor an asymptotic is proved. Stage15 preserves the same boundary.

The currently certified arsenal contains structural parametrizations, gluing maps, multiplicity controls, upper-bound machinery, local squareclass sieves, and exact finite enumeration, but no audited construction theorem producing infinitely many **primitive canonical Stage19 objects** with controlled increasing height.

Accordingly none of the following is certified:
\[
N_2(B)\to\infty,
\]
\[
N_2(B)\gg B^\delta\quad(\delta>0),
\]
or
\[
N_2(B)\gg B^{1/2-o(1)}.
\]
In particular there is no matching lower bound to the checkpoint40 half-power ceiling.

This is a statement about the **current certified theorem ledger**, not a theorem that no such construction can exist.

## 4. Why scaling does not close the gap

A single integral-space exactly-two cuboid can be scaled by an integer, but Stage19 counts only primitive triples with
\[
\gcd(a,b,c)=1.
\]
All nontrivial scalar multiples are therefore excluded from the physical population. Hence the existence of one or finitely many Stage19 objects cannot be turned into an unbounded primitive lower bound by homothety.

Likewise, the finite census containing 3495 primitive objects does not by itself exhibit a one-parameter or positive-rank construction whose outputs are provably distinct primitive objects for infinitely many parameters.

## 5. Numerical sharpness diagnostics do not become constructions

The extended finite panel has thousands of survivors, but
\[
\frac{N_2(B)}{\sqrt B}
\]
has not passed the predeclared terminal stability gate. More fundamentally, even perfect empirical stability would remain finite evidence and would not constitute a lower-bound proof.

Thus the numerical weapon has two legitimate roles here:

1. certify a strong finite existence floor and regression oracle;
2. test proposed future constructions against the exact population.

It cannot manufacture an asymptotic lower theorem.

The finite record `T=0` through B500m is unrelated to the Stage19 lower-bound question except as retained mask information and is not a perfect-cuboid nonexistence claim.

## 6. Checkpoint verdict

At the current certified resolution:

- **finite nonemptiness is very strong:** at least 3495 primitive canonical Stage19 objects are certified below B500m;
- **constant lower floor:** `N_2(B)>=3495` for every `B>=500000000`;
- **unboundedness:** not proved;
- **infinite primitive construction:** not certified;
- **positive-power lower bound:** not proved;
- **matching half-power lower bound:** not proved;
- **half-power sharpness/intrinsic status:** remains unresolved;
- **new computation:** unnecessary because NUM-R01–R03 already dominate the finite evidence need.

The missing unbounded/matching lower bound is retained as an explicit open gate rather than inferred from the finite census.

## 7. Non-claims

- no claim that the Stage19 population is finite;
- no claim that no infinite family exists;
- no claim `N_2(B)->infinity`;
- no `N_2(B)~C sqrt(B)` asymptotic;
- no positive-power lower bound;
- no matching lower bound;
- no use of scalar multiples as primitive objects;
- no perfect-cuboid conclusion.

```text
EVIDENCE_LEVEL=PROVED
CHECKPOINT=50
LOWER_BOUND_CLASS=FINITE_CONSTANT_FLOOR_ONLY
FINITE_FLOOR=N_2(B) >= 3495 for B >= 500000000
FINITE_FLOOR_SOURCE=NUM-R01 / AR-040 exact finite census + monotonicity
FINITE_FLOOR_EVIDENCE=COMPUTED
UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_CONSTRUCTION_CERTIFIED=false
POSITIVE_POWER_LOWER_BOUND=false
MATCHING_HALF_POWER_LOWER_BOUND=false
HALF_POWER_SHARP=false
HALF_POWER_INTRINSIC=UNRESOLVED
SCALING_CONSTRUCTION_VALID=false
SCALING_FAILURE_REASON=primitive population excludes nontrivial scalar multiples
OPEN_GATE=UNBOUNDED_OR_MATCHING_LOWER_BOUND_FOR_STAGE19
OPEN_GATE_STATUS=UNRESOLVED
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=60
CODEX_REQUIRED=false
CODEX_REASON=No implementation gap; checkpoint is a theorem/negative-knowledge ledger using frozen interfaces and exact finite reuse.
```