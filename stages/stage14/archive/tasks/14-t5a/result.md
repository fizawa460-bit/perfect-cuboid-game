# Stage14-t5a — split-root-void handoff

## Purpose

Record the exact Stage14-t consequence of the Stage14-4ak Shimada-lattice computation without overclaiming beyond the currently frozen upstream state.

The Stage14-t5 bridge on `main` already established that any surviving fixed physical rational `M`-degree-4 root `C` would satisfy

```text
M = C + delta(C)
C^2 = -2
M.C = 4
```

and that the third-square relative cover restricts to `C` with branch degree

```text
(2M).C = 8.
```

Generic odd branch support `b_odd=8` gives genus `3`; genus `0/1` escape requires special parity collision.

## New upstream signal from Stage14-4ak

PR #194 executes the Shimada lattice ingestion and reports no split root in the relevant anti-invariant lattice. PR #199 adds an independent exact verification: PARI is used only to obtain the saturated anti-invariant integer kernel, while a separate pure-Python exact LDL recursion enumerates all vectors of norm at most `16` and finds no norm-16 vector.

The cross-check target is

```text
anti_invariant_rank = 6
norm16_representatives = 0
parity_compatible_split_root_pairs = 0
exact_norm16_vectors = 0
norm16_void = true
```

At the time this t-side handoff is written, #199 is still an open draft and the 4ak theorem boundary is therefore not yet imported as a canonical `main` theorem.

## Conditional consequence once 4ak is frozen on main

If the independently verified split-root void is merged/recovered onto `main`, then the entire Stage14-t5 root-by-root branch-parity program on the fixed minimal `M`-degree-4 stratum becomes vacuous:

```text
FIXED_M4_SPLIT_ROOT_COUNT = 0
FIXED_M4_TRIPLE_BRANCH_PARITY_CASES = 0
```

Hence the triple correction cannot contribute at the observed `sqrt(B)` scale through the specific fixed minimal-bisection mechanism isolated by Stage14-4ai/4aj.

This is stronger than merely saying that a generic surviving root would lift to genus `3`: there is no surviving fixed root on which to perform that restriction.

## What this does NOT prove

It does **not** prove

```text
T(B)=o(sqrt(B))
```

because Stage14-t still lacks a global theorem ruling out all moving/non-fixed mechanisms whose union might in principle contribute at `sqrt(B)` scale. It also does not by itself transfer a raw-pair asymptotic to the exactly-two count.

Higher physical-degree fixed rational curves are individually below the minimal `M`-degree-4 exponent, but a global summation over moving families is a separate problem and is not claimed here.

## Status

```text
STAGE14_T5A=SPLIT_ROOT_VOID_HANDOFF_PREPARED
T5_BRANCH_DEGREE_8_INTERFACE_REMAINS_VALID=true
UPSTREAM_4AK_PRIMARY_VOID_REPORTED=true
UPSTREAM_4AK_INDEPENDENT_VERIFY_PR=199
UPSTREAM_4AK_INDEPENDENT_VERIFY_MERGED=false
FIXED_M4_TRIPLE_AUDIT_VACUOUS_AFTER_4AK_FREEZE=true
T_O_SQRT_B_PROVED=false
EXACTLY_TWO_TRANSFER_PROVED=false
```

## Next

After Stage14-4ak is independently verified and present on `main`, Stage14-t should stop spending effort on fixed `M`-degree-4 branch-contact cases and redirect to the residual global question:

```text
Can the union of moving/higher-degree triple loci contribute at sqrt(B) scale?
```

Only a theorem controlling that residual union can close `T(B)=o(sqrt(B))`.
