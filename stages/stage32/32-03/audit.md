# Stage32-03 audit artifact

## Bounded question

Close exactly the 44 proof problems left as `UNKNOWN(timeout)` by PR #1344 at `d=6, g=1, e=4, a=32`, preserve their inherited identities, regress the replacement formulation on representative proof-bearing neighbors, package independently checkable evidence, and stop.

## Inherited state

PRs #1343 and #1344 remain valid bounded predecessors. No predecessor checkpoint, SMT2 problem, proof, manifest, audit comment, or history is changed. The source evidence is `../32-02/local-evidence.json`, canonical SHA256:

```text
5ddd03fce75acc1cab427aa3bd2c8c621c4180c11f7a33c410566bb50f22bf21
```

The exact source-locked `picard-core.json` file SHA256 is:

```text
eac92f66d02bb201668ae609108d37160953992915e08464b2bc5dea8f886d56
```

Each new cell checkpoint repeats the corresponding old checkpoint-file and SMT2 SHA256 values. The runner verifies those bytes in the preserved #1344 tree before computing or reusing a result.

## Method and certificate boundary

The replacement is an exact affine-lattice exhaustion, not a numerical feasibility test:

- exact HNF/image membership and a saturated 54-dimensional kernel from a unimodular transform;
- exact positive-definite kernel Gram matrix and exact Gram-LLL transform;
- exact completed-square adjunction ellipsoid;
- complete exact Fincke–Pohst recursion;
- all 140 nonnegative intersections used for exact ellipsoid branch certificates;
- deterministic per-cell checkpoint and transcript hashes;
- a verifier that recomputes the algebra and searches rather than trusting summary counts.

The fixed-budget map has rank 10, kernel dimension 54, and HNF image index 8. All 44 target vectors are in the image, so HNF congruence rejects zero cells. The closure comes from exact reduced-lattice enumeration plus the 140 intersection bounds.

Before selecting the closing recursion, the authorized intersection-coordinate formulation was measured on the first inherited hard cell. A deterministic independent set of 64 of the 140 intersection rows has full rank, determinant `-562949953421312 = -2^49`, largest Smith invariant 16, and inverse common denominator 16. The transformed integer QF_NIA problem still returned `UNKNOWN(timeout)` after `60.017492` seconds. An exact finite bit-vector encoding of the same bounded intersection coordinates also returned `UNKNOWN(timeout)` after `60.944290` seconds. Neither trial receives census credit. These measurements motivated the exact affine-kernel ellipsoid exhaustion; no unrelated backend branch was opened.

## Result

The generated machine-readable result is `certificates/closure-evidence.json`; its canonical SHA256 is:

```text
dc2aef2da0191ecf46af8f0e5ecaf1d3a537a9404f29bc4cad519b84b1882a81
```

All 44 inherited terminal cells are exactly `UNSAT`, with zero survivors and zero `UNKNOWN` results. The run visited 3,539,371 exact enumeration nodes and issued 4,586,903 exact intersection-ellipsoid prunes. Per-cell CPU runtimes ranged from `14.994719` to `66.948020` seconds and sum to `1794.454016` seconds under four workers.

The common lattice certificate canonical SHA256 is:

```text
4767ab2fb45fb056f79f8355fddb885d7404b18f5471faea634b055255f3eb29
```

The representative predecessor comparison is `regression/regression-evidence.json`, canonical SHA256:

```text
e54db891b116d88545d872da411cb04200e4797ce37c5310d40634f9caa32d89
```

The full independent recomputation returned `PASS_FULL_INDEPENDENT_RECOMPUTATION`; its recorded evidence canonical SHA256 is:

```text
b2a6ce99bc30c27d94b9a1be130fc17d25319065d6fb8f44e86c3968e37c4ca6
```

The audit-relevant success flag is:

```text
ALL_44_E4_A32_TERMINAL_CELLS_EXACTLY_CLOSED=true
```

The exact survivor count is zero. Any integral survivor would have been stored in full and independently checked against all Stage32 defining conditions; no unverified SAT model receives credit.

The representative regression uses four already-complete proof-bearing neighboring terminal cells, including difficult cells that took the predecessor 213–300 seconds as well as an outer boundary cell. It checks the old SMT2 and proof hashes and requires exact agreement of terminal result and survivor count.

## Runtime and remaining limitation

All runtimes are host measurements, not mathematical bounds. The host is recorded verbatim in the closure evidence together with Python, python-flint, SymPy, and worker versions. This specialized bounded method has not been benchmarked for other residuals or higher degrees. The next isolated computational question is growth of the exact ellipsoid recursion when fewer subgroup budgets are fixed; that scaling is unestablished. Per the task stop rule, no optimization or larger-census experiment is performed here.

## Firewalls

Closure of this isolated wall grants no Stage32 receiver or orbit credit. The state remains:

```text
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
LOW_DEGREE_PREFIX_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

No statement about the existence or nonexistence of a perfect cuboid is made.
