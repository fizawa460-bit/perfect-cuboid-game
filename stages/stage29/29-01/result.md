# Stage29-01 — global certified map lock

```text
TASK_ID=Stage29-01
ROLE=GLOBAL_CERTIFIED_MAP_LOCK
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
NUMBERING=INCREMENTAL
PERFECT_CUBOID_ENDPOINT_OPENED=false
```

## 1. Stage29 mission

Stage29 is the synthesis/routing stage between the completed population program and a later direct perfect-cuboid endpoint attack. It does not introduce a new population condition and does not infer existence/nonexistence from rarity.

The two endpoint entrances to be compared later are:

```text
ENTRANCE_A=Stage19 + third integral face
ENTRANCE_B=Stage20 + integral space diagonal
COMMON_ENDPOINT=three integral faces + integral space diagonal
```

The endpoint itself remains deferred while Stage29 compares the two descriptions and extracts the best exact receiver.

## 2. Strongest certified population surface imported at 29-01

All counts use primitive canonical physical cuboids under the common Euclidean cutoff `R<=B` unless explicitly stated otherwise.

### Ambient

`U(B) ~ [pi/(36 zeta(3))] B^3`.

### One face, no space: M1

Use the strongest audited upstream interface already accepted by Stage21/22:

`M1(B) ~ [3/(4 pi^2)] B^2 log B`.

### One face + space: N1

`N1(B) ~ [kappa/(24 pi)] B (log B)^3`, with positive leading constant.

Hence the exact first space-cost asymptotic is

`N1/M1 ~ (kappa*pi/18) (log B)^2/B`.

### Exactly two faces, no space: M2

`M2(B) ~ C_M2 B (log B)^5`, `C_M2>0`.

Hence the second-face adjacent-stratum size ratio is

`M2/M1 ~ (4 pi^2 C_M2/3) (log B)^4/B`.

This ratio is not an objectwise survival probability because the exact-one and exact-two strata are disjoint.

### Exactly two faces + space: N2

The Stage27 closeout corridor is

`B^(1/4) << N2(B) <<_epsilon B^(1/2+epsilon)`.

Therefore

`B^(-3/4)(log B)^(-5) << N2/M2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5)`.

The true N2 exponent is not identified. Neither `1/4` nor `1/2` may be treated as the intrinsic exponent.

Relative to the one-face+space population,

`B^(-3/4)(log B)^(-3) << N2/N1 <<_epsilon B^(-1/2+epsilon)(log B)^(-3)`

up to positive fixed constants in the asymptotic source normalization.

Stage27 also certifies positive-divergent enhancement of two-face-conditioned space survival relative both to the ambient space rate and to the one-face-conditioned space rate. This is interaction information, not an independent saving to multiply again.

### Exactly three faces, no space: M3

Use the strongest merged/audited Stage28/Stage26 surface currently in `main`:

`M3(B) >> B^(1/3)`

with the audited explicit liminf coefficient from the injective Saunderson cone, while

`M3(B) <<_eta B (log B)^(5-eta)` for fixed `0<eta<1/46`.

The true M3 exponent is not identified and no asymptotic is known.

Stage26 proves the exact-two / exact-three adjacent-stratum comparison tends to zero in the appropriate common-host formulation. Combining the strongest population bounds gives a coarse size-ratio corridor compatible with that theorem; Stage29 will not promote a construction-family ratio to the full-population ratio.

### Perfect-cuboid endpoint: P

Define only as a symbolic future endpoint:

`P(B)=# {primitive canonical cuboids under R<=B with all three face diagonals integral and R integral}`.

No Stage16–29 theorem currently supplies an asymptotic, positive lower bound, zero count, or nonexistence theorem for `P(B)`. Stage29-01 makes no endpoint count claim.

## 3. Stage28 bridge information admitted at 29-01

Only merged/audited Stage28 information is certified input. In particular, merged checkpoint60-r2 gives

`I_sp=(N2/M2)/(N1/M1)`,
`I_face=(M3/M2)/(M2/M1)`,
`J_28=I_face/I_sp`,
`K_28=(log B)^2 J_28`,

and

`M3/N2 ~ (24*pi*C_M2/kappa) K_28`.

Thus Stage19/Stage20 asymptotic ordering is equivalent to the unresolved interaction-curvature scale. The critical raw scale for `J_28` is `(log B)^(-2)`.

The known first geometric differential is branch-profile level:

`space completion: 4 x genus-0 branch components`,
`third-face completion: 2 x genus-1 branch components`.

No audited theorem currently converts that differential into the missing physical-height marginal ordering.

## 4. Pending Stage28 frontier

PR #1282 is currently an open Draft and is not certified Stage29 input. Its candidate low-degree fixed-curve spectrum / common-polarization M-degree-six statements are deliberately excluded from the theorem surface above until fresh Stage28 audit and merge.

```text
STAGE28_CERTIFIED_FRONTIER=merged/audited material through PR_1281
STAGE28_OPEN_CANDIDATE_PR=1282
PR1282_USED_AS_PROVED_INPUT=false
STAGE28_REFRESH_REQUIRED_BEFORE_ENDPOINT_ENTRANCE_SELECTION=true
```

If Stage28 closes with no new certified theorem affecting the bridge or branch geometry, Stage29 records `NO_MATERIAL_BACKFILL`. If it does add a relevant theorem, Stage29 imports the delta once, without rerunning 29-01 from scratch.

## 5. StageA2 relation fixed at entry

StageA2 proves a family-specific exclusion for the published equation-(6) `-18` anchored family. It does not provide a reverse map from arbitrary perfect cuboids and therefore cannot be used as an endpoint nonexistence theorem.

What Stage29 may reuse is the method species:

`parameter reduction -> quotient/cover decomposition -> quartic/low-genus model -> Jacobian -> rank/torsion/descent -> rational-point closure`.

Any Stage29 A2 transfer must be applied to a natural Stage19/20 endpoint slice with height/multiplicity/coverage status stated explicitly.

```text
A2_FAMILY_EXCLUSION_PROMOTED_TO_GENERAL=false
A2_METHOD_REUSE_ALLOWED=true
COVERAGE_CLAIM_REQUIRES_PROOF=true
```

## 6. 29-01 first gap scan

The global population ledger needed to begin Stage29 is present. No missing Stage16–27 population state or transition prevents 29-02.

One upstream certification gap exists: Stage28 is still active through open PR #1282, so its final frontier is not yet frozen. This does not block 29-02/29-03 because those stages can use certified merged inputs, but it blocks a final endpoint-entrance selection until Stage28 is refreshed.

A second, operational discrepancy exists: the older canonical Stage16–29 roadmap still prints a generic Stage29 `10..70` sequence. The Stage29-specific `stages/stage29/roadmap.md` records the operator-authorized incremental sequence and is the Stage29 execution authority pending roadmap synchronization.

```text
GAP_SCAN_29_01=FOUND_PENDING_UPSTREAM_CERTIFICATION
BLOCKS_NEXT_STEP=false
BLOCKS_FINAL_ENTRANCE_SELECTION=true
MISSING_ANALYSIS_BEFORE_29_02=NONE
NEXT=Stage29-02
```

## 7. Immediate next analysis

29-02 should construct the condition-cost matrix without forcing incomparable quantities into a single fake exponent. It must separately track:

- exact power/log asymptotics;
- interval-valued power exponents;
- zero-density results;
- local sieve dimensions;
- cover/branch geometry;
- construction lower efficiencies;
- literal-survival versus adjacent-stratum size-ratio semantics.

The purpose is to identify which condition costs are actually known and which apparent differences are artifacts of unequal theorem strength.

```text
NEW_PERFECT_CUBOID_CLAIM=false
NEW_N2_EXPONENT=false
NEW_M3_EXPONENT=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
