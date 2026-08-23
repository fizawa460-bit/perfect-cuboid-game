# Stage32-01 hostile audit — production preflight

## Verdict

`PASS_PREFLIGHT_ONLY_EXACT_CLASS2_POLYHEDRAL_WALL_EXPOSED`

The submitted 32-01 branch does **not** complete the unibranch numerical census and receives no `R29-LG2` discharge credit. It does, however, successfully complete and source-lock the production preflight needed to continue 32-01.

## Independently audited facts

The latest PR-head workflow run `32610810714` executed the source-locked Magma preflight and independent verifier successfully before the later pilot was cancelled. The successful audited preflight establishes:

```text
UPSTREAM_BLOB=0422b69847f2afb97cb7b3ed02ebef91279f61b1
PICARD_RANK=64
H2=16
HPERP_RANK=63
NODE_COUNT=48
KNOWN_FILTER_COUNT=140
WINDOW_ROW_COUNT=183
RAW_63D_CVP_STARTED=false
```

The generalized `(genus,degree)` formulas were emitted for all 183 rows in the frozen windows and the degree-2 / degree-4 regression values agree with the upstream templates. The sparse Picard-core export also completed successfully and is tied to the same immutable upstream blob.

## Exact stopping wall

The next exact pilot forms the rational polyhedral cone cut out by the 140 nonnegative-intersection halfspaces and asks whether its homogeneous tail in `H.x=0` is trivial. This is a sound necessary-condition reduction for a genuinely new irreducible curve: a new irreducible curve has nonnegative intersection with every distinct frozen irreducible curve / exceptional divisor.

On the latest PR-head run, PyNormaliz 2.24 entered the exact tail-cone computation and was cancelled after about 12.5 minutes. No tail-ray result was produced. Therefore:

```text
POLYHEDRAL_TAIL_COMPACTNESS_CERTIFIED=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
```

This is not a Class-3 theorem wall. It is an exact smaller Class-2 / algorithmic wall:

```text
L32-01-POLYTAIL:
certify or avoid the 64-variable / 140-halfspace tail-cone computation,
preferably after symmetry, quotient, redundancy, or exact LP reductions,
then construct a resumable graded enumeration of bounded positive-degree slices.
```

A cancelled Normaliz computation gives no mathematical conclusion about compactness or noncompactness.

## Audit firewall

No credit is granted for effectivity, multibranch coverage, route color change, endpoint exclusion, or perfect-cuboid existence/nonexistence.

## Next state

```text
32_01_PREFLIGHT=VERIFIED
32_01_COMPLETE=false
SMALLER_CLASS2_LEAF=L32-01-POLYTAIL
AUDIT_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=32-01-POLYTAIL-REDUCTION-AND-GRADED-ENUMERATOR
NEXT_EXPECTED_COMMAND=Stage32-main-batch
```
