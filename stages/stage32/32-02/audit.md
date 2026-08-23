# Stage32-02 exact local replacement — stopped at isolated Class-2 wall

## Outcome

This successor preserves PR #1343 as a mathematically valid, audited predecessor. It does not rewrite or supersede any #1343 checkpoint. The replacement backend was run locally against the exact `picard-core.json` from run `32624596141`.

The narrowed success conditions were **not** all reached:

```text
ALL_28_RESIDUALS_EXACTLY_CLOSED=false
PREDECESSOR_REGRESSION_COMPLETE=false
PREDECESSOR_REGRESSION_MATCH=NOT_EVALUATED
```

Fourteen of the 28 formerly unresolved `(d=6,g=1,e,a)` singletons are exactly closed with zero survivors: 13 directly and one by a complete deterministic partition. The other 14 remain incomplete. In particular, the fully exercised fallback for `e=4,a=32` retains 44 terminal cells with exact solver result `UNKNOWN(timeout)` after 300 seconds per cell. Its last parent run took `4541.977076` seconds and produced 1,194 complete exact UNSAT checkpoints in the accumulated local tree. The predecessor regression was not started because the user-directed stopping rule applies as soon as a residual remains UNKNOWN after the current deterministic fallback.

The machine-readable disposition and every terminal label, SMT2 hash, checkpoint hash, and runtime are in `local-evidence.json`. Its canonical hash is:

```text
5ddd03fce75acc1cab427aa3bd2c8c621c4180c11f7a33c410566bb50f22bf21
```

The complete local evidence tree remains preserved at the run location used to generate that manifest. It contains 4,109 files (383,271,634 bytes), including 1,450 checkpoints, 1,450 exact SMT2 problems, and 1,194 proof files. The canonical sorted file-hash-manifest digest is:

```text
87dfa2c7f84ec2d6ba1352f2ddbfc0957e7929da01ff6bf44ed3b7e75f1dbda0
```

## Exact replacement algorithm

The backend searches the 64 integral coordinates of the source-locked primitive Picard basis. Thus Picard lattice-image and congruence restrictions are imposed by construction. For a candidate `x`, it forms all 140 exact integral intersection linear forms and imposes:

1. all 140 intersections are nonnegative;
2. `H.x=d`;
3. the independently checked identity
   `sum(D_i.x) + 5 sum(E_j.x) = 19d`;
4. the exact adjunction lower bound `x.G.x >= -d-2+2g`;
5. the immutable exceptional and nonexceptional group budgets inherited from #1343;
6. deterministic successive subgroup budgets when a parent returns UNKNOWN.

The implementation uses Z3 `QF_NIA` over integers with random seed zero and one solver thread per leaf. A leaf receives census credit only after final `UNSAT`; `UNKNOWN`, timeout, floating-point feasibility, or a model limit never receives completion credit. Every complete leaf records the SMT2 hash, proof hash, result hash, runtime, and solver statistics. All 140 known classes are excluded by the same nonnegative-intersection search because each known class has a negative self-intersection with itself.

The deterministic partition coordinates used by the current fallback are sums over these fixed source-locked ranges:

- nonexceptional `1..23`;
- exceptional `1..24`;
- nonexceptional `47..69`;
- exceptional `1..12` and `25..36`;
- nonexceptional `1..11` and `1..5`.

These partitions are exhaustive disjoint integer-budget decompositions. They do not use the rejected raw 63-dimensional ball or the rejected monolithic tail cone.

## Reproduction

Use Python 3.10+ and install `requirements.txt`. Obtain the locked artifact `stage32-01-low-degree-verified-prefix` from run `32624596141`, then run:

```text
python run_pr1343_regression.py \
  --artifact-dir <stage32-01-low-degree-verified-prefix> \
  --output-dir <checkpoint-directory> \
  --scope residual --workers 4 --timeout 300 --proof
```

To reproduce the isolated parent directly:

```text
python run_exact_z3_partition.py \
  --core <artifact-directory>/picard-core.json \
  --output-dir <checkpoint-directory> \
  --degree 6 --genus 1 --exceptional-mass 4 --curve-group-mass 32 \
  --workers 4 --timeout 300 --proof
```

To hash an existing tree without rerunning any proof:

```text
python summarize_local_evidence.py \
  --checkpoint-dir <checkpoint-directory> \
  --output local-evidence.json
```

`run_exact_normaliz_budget.py` is retained only as the exact project-and-lift diagnostic that established that a direct monolithic Normaliz polytope was also not a production solution on the tested host. It receives no census credit.

## Runtime and next blocker

Completed exact leaves ranged from `0.008258` to `299.556197` seconds, with an accumulated solver time of `6425.670018` seconds. The remaining wall is no longer the Magma Online 60-second cap. It is exact nonlinear integer UNSAT proof search in 44 balanced central terminal cells of `d6-g1-e4-a32`, listed verbatim in `local-evidence.json`. Per the narrowed task, no additional partition level or algorithm investigation was attempted after this blocker was confirmed.

The measured host was Windows 11 Home `10.0.26200`, Intel Core i7-10750H (6 cores / 12 logical processors), Python `3.10.6`, and Z3 `4.15.3`. Runtime numbers are host measurements, not hardware-independent bounds.

The latest #1343 owner audit comment independently identifies the same balanced-central-cell pathology and reserves affine HNF/SNF or intersection-coordinate lattice-image reduction for a successor. That proposal was not implemented or tested here.

Automorphism/orbit counts are unavailable because no source-locked automorphism action matrices are present in the inherited core. No orbit-deduplicated count is claimed.

## Audit and firewall state

PR #1343 remains:

```text
CHECKPOINT_INTEGRITY_HARDENING=PASS
PRODUCTION_ENUMERATOR_ARCHITECTURE=SOUND_SO_FAR
LOW_DEGREE_PREFIX_COMPLETE=false
AUDIT_FINAL_VERDICT=WAIT
```

This successor does not retroactively award #1343 census credit. The receiver firewalls remain:

```text
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

No statement about the existence or nonexistence of a perfect cuboid is made.
