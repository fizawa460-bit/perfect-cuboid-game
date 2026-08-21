# Stage29-02hd — adversarial audit

```text
AUDITED_PR=1306
AUDITED_SUBMISSION_HEAD=0fa54d2177d5497c3d0b9a94d80aaf86ab1a5966
AUDIT_MODE=ADVERSARIAL_BROAD_SCREEN
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Executive verdict

The proposed practical mining stop survives, but only after narrowing what it means. The screen did **not** prove that all fresh candidates are merely old foundations. In particular, the Peschmann route has not yet been exactly crosswalked to F2 and its independence is unresolved.

The valid stop statement is only:

```text
NO_CERTIFIED_NINTH_FOUNDATION_FOUND_IN_THIS_BROAD_PASS=true
```

This is enough for project routing because the `h*` namespace remains reopenable and no literature-exhaustiveness claim is made.

## Attack 1 — was Peschmann prematurely collapsed into F2?

Yes, partially. The same residual pattern

```text
two faces built in + third-face square + space square
```

is strong evidence for an F2/joint-V4 crosswalk, but it is not the crosswalk itself.

Repaired state:

```text
PESCHMANN_PROVEN_F2_ADAPTER=false
PESCHMANN_INDEPENDENCE_RESOLVED=false
PESCHMANN_NEW_FOUNDATION_PROMOTED=false
R29-PESCH1=OPEN_EXACT_CROSSWALK
```

Fresh source audit also adds Peschmann `arXiv:2604.28072`: primitive Euler-brick parametrization up to scaling plus an unconditional exclusion on 1,072 explicit master-tuple fibers. Those finite-family results are not imported into Stage population statements.

## Attack 2 — exact four-quadric web

The committed checker survives direct algebraic inspection. For the diagonal web the seven coefficient hyperplanes are exact, every triple is independent, the rank-<=4 locus is therefore zero-dimensional, and the checker enumerates 17 projective points. Exactly six points have four zero coefficients and hence rank 3.

```text
R29-QWEB0=DISCHARGED
R29-QWEB1=DISCHARGED
R29-QWEB-ABELIAN=RED_FOR_SCREENED_RANK4_CURVE_TRIGGER
R29-QWEB-CLIFFORD=AMBER_OPEN
```

No general nonexistence theorem is inferred from the absence of the screened Adler–van Moerbeke trigger.

## Attack 3 — Terasoma generic/singular transfer

The submission correctly leaves the 48-node specialization/resolution adapter open. The general four-quadric/K3 theorem ecosystem is not promoted directly to the singular cuboid specialization.

```text
R29-TERA1=OPEN
TERASOMA_INDEPENDENT_FOUNDATION_PROMOTED=false
```

## Attack 4 — fundamental-group source freshness and Chabauty–Kim scope

The source lock was stale. The current paper is `arXiv:2310.12710v3`, revised 2026-07-06, by Benjamin Enriquez, David Jarossay, Francesco Maria Saettone and Yotam Svoray, under the title *The fundamental group of surfaces parametrizing cuboids*.

The projective cuboid surface and resolution are simply connected; selected open face-cuboid loci have `F3 semidirect Z^2` fundamental groups and free pro-unipotent Malcev completion on three generators.

The audit removes the overbroad claim that surface/higher-dimensional Chabauty–Kim theory is unavailable in general. Only the project-specific statement remains:

```text
CUBOID_OPEN_EFFECTIVE_CHABAUTY_KIM_ADAPTER_AVAILABLE=false
```

## Attack 5 — broad-screen omissions

Bremner's 2018 perfect `K`-rational cuboid theorem is now explicitly screened. It gives perfect cuboids over infinitely many cubic fields and over some number field of every degree at least two, but neither Q-rational existence nor a Q-rational obstruction. It is therefore `RED_FOR_Q_ENDPOINT_FOUNDATION`.

This addition improves the screen but still does not make it exhaustive.

## Attack 6 — population / arithmetic overreach

No automatic transfer survives for

```text
M1,N1,M2,N2,M3
R<=B
primitivity
canonical ordering
face multiplicity
asymptotics
Brauer residues.
```

```text
BACKFLOW_TO_STAGE16_28=false
STAGE16_20_POPULATION_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
CANONICAL_ORDER_TRANSFER=false
ASYMPTOTIC_TRANSFER=false
BRAUER_TRANSFER_AUTOMATIC=false
```

## Mining-stop verdict

The stop is a routing checkpoint, not a theorem of mathematical exhaustion.

```text
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=true
STOP_SCOPE=NO_CERTIFIED_NINTH_FOUNDATION_IN_THIS_BROAD_PASS
UNRESOLVED_ADAPTER_OR_INDEPENDENCE_CANDIDATES_EXIST=true
PESCHMANN_INDEPENDENCE_RESOLVED=false
LITERATURE_EXHAUSTIVENESS_CLAIM=false
NO_MORE_FOUNDATIONS_EXIST_CLAIM=false
H_NAMESPACE_REOPENABLE=true
```

## Controller-preservation closeout

A final audit-diff check caught an unrelated metadata regression in `stages/stage29/controller.json`: the first audit rewrite had compressed previously audited fields in `work_import`, `child_02f`, `child_02g`, and `child_02ha`. Those fields have now been restored exactly while retaining only the intended 02hc merge synchronization and 02hd routing additions.

```text
CONTROLLER_METADATA_PRESERVATION_AUDIT=PASS
UNRELATED_PRIOR_AUDIT_METADATA_DELETED=false
```

## Final state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02HD_AUDIT=PASS
BOUNDED_REPAIR=PESCHMANN_SCOPE_PLUS_SOURCE_FRESHNESS_PLUS_BROAD_SCREEN_COVERAGE_PLUS_STOP_SEMANTICS_PLUS_CONTROLLER_PRESERVATION
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
AUTO_ADVANCE_TO_29_03=false
NEXT_ITEM=29-03_FOUNDATION_BACKFLOW_DECISION
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
