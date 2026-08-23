# Stage32-03: exact affine-lattice closure of the e4/a32 terminal wall

This bounded successor consumes the 44 `UNKNOWN(timeout)` terminal cells recorded by PR #1344 for

```text
d=6, g=1, e=4, a=32.
```

It does not rerun or replace any completed #1343/#1344 cell. The inherited SMT2 files and timeout checkpoints remain byte-for-byte preserved and are linked to every new result by SHA256.

## Exact algorithm

Let `x` be the 64 integral coordinates in the source-locked primitive Picard basis. For each terminal cell, form the ten-row integer map `A` consisting of:

1. `H.x`;
2. the total exceptional intersection mass;
3. the first 46 nonexceptional intersections;
4. the first 23 nonexceptional intersections;
5. exceptional intersections 1–24;
6. nonexceptional intersections 47–69;
7. exceptional intersections 1–12;
8. exceptional intersections 25–36;
9. nonexceptional intersections 1–11;
10. nonexceptional intersections 1–5.

FLINT computes row HNF with its unimodular transformation on `A^T`. This independently proves that `rank(A)=10`, checks membership of each target in `A Z^64`, constructs an exact integral base point `x0`, and supplies a saturated integral kernel `N` of dimension 54. The HNF image has index 8. All 44 targets pass the image test; none is excluded by congruence alone.

On the fixed-budget affine lattice `x=x0+Nz`, the form `-N^T G N` is positive definite. Exact Gram-LLL produces a unimodularly equivalent reduced kernel. Completing the square changes the adjunction inequality into a shifted positive-definite ellipsoid. An exact Fincke–Pohst recursion, using FLINT rationals, exhausts every integral lattice point in that ellipsoid.

At every recursion node, each of the 140 source-locked intersection forms is bounded over the remaining continuous ellipsoid by exact Cauchy–Schwarz:

```text
fixed < 0 and fixed^2 > remaining_radius * dual_norm
```

is an exact infeasibility certificate for that branch. No floating-point value is used for a bound, pruning decision, feasibility decision, or census result. The fixed weighted identity

```text
sum(D_i.x) + 5 sum(E_j.x) = 19d
```

is independently checked while constructing the fixed map and is inherited by every affine point.

Each checkpoint records the old SMT2/checkpoint hashes, HNF image coordinates, exact completed-square radius, exhaustive node/prune counts, exact survivors, and a deterministic enumeration transcript hash. `verify_affine_lattice_evidence.py` rebuilds HNF, the saturated kernel, Gram-LLL, LDL data, and every search from `picard-core.json`; it does not accept the stored summary fields as proof.

## Outcome

All 44 inherited cells close exactly as `UNSAT`; the exact survivor count and remaining `UNKNOWN` count are both zero. The closure-evidence canonical SHA256 is `dc2aef2da0191ecf46af8f0e5ecaf1d3a537a9404f29bc4cad519b84b1882a81`. The representative neighboring regression is complete and matches all four proof-bearing predecessor results exactly.

## Reproduction

Use Python 3.10+ with the pinned packages in `requirements.txt`. The commands below intentionally require the preserved #1344 checkpoint tree so that the inherited problem hashes are checked before any replacement certificate is accepted.

```text
python -m pip install -r requirements.txt

python run_affine_lattice_closure.py \
  --core <run-32624596141-artifact>/picard-core.json \
  --inherited-evidence ../32-02/local-evidence.json \
  --predecessor-checkpoint-dir <stage32-z3-production-20260823> \
  --output-dir certificates --workers 4

python run_neighbor_regression.py \
  --core <run-32624596141-artifact>/picard-core.json \
  --predecessor-checkpoint-dir <stage32-z3-production-20260823> \
  --output-dir regression

python verify_affine_lattice_evidence.py \
  --core <run-32624596141-artifact>/picard-core.json \
  --inherited-evidence ../32-02/local-evidence.json \
  --predecessor-checkpoint-dir <stage32-z3-production-20260823> \
  --certificate-dir certificates --regression-dir regression --workers 4
```

The closure runner is resumable: a complete checkpoint is validated and reused; a missing cell alone is computed. Existing predecessor files are read-only.

## Scope boundary

This package stops after the 44-cell closure, exact verification, and four-cell representative neighboring regression. It does not run the full predecessor regression, attack any other residual, extend the low-degree prefix, or start the Stage32 production census.
