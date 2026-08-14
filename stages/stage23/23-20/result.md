# Stage23-20 — finite-data baseline and aggressive attack inventory

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage23 compares the matched adjacent strata `N2(B)/N1(B)` under the frozen primitive/canonical integral-space contract. This checkpoint keeps finite evidence separate from theorem claims and begins the aggressive lower-bound / reparametrization search required by the Stage23 controller.

## 1. Matched finite baseline

The frozen Stage17 exact census gives `N1(2000)=1434`; the frozen Stage19 exact census gives `N2(2000)=5`. Hence the largest threshold literally shared by the two checkpoint20 CSVs is

\[
\boxed{N_2(2000)/N_1(2000)=5/1434\approx0.00348675.}
\]

Stage19 also has exact counts through `B=100000`, while the Stage17 checkpoint20 CSV stops at `B=2000`, so no raw Stage23 ratio is formed beyond the common grid without a new matched Stage17 census. The finite ratio is diagnostic only.

```text
MATCHED_THRESHOLD=2000
N1_AT_MATCHED_THRESHOLD=1434
N2_AT_MATCHED_THRESHOLD=5
FINITE_RATIO=5/1434
FINITE_RATIO_DECIMAL=0.0034867503486750348
FINITE_DATA_USED_AS_PROOF=false
NEW_MATCHED_CENSUS_LAUNCHED=false
```

## 2. Stronger target finite evidence retained separately

Stage19's validated numerical oracle later reaches

\[
N_2(500000000)=3495.
\]

This is useful for testing proposed Stage23 constructions, but cannot be divided by an unavailable matched `N1(500000000)` census and cannot prove a Stage23 asymptotic. By monotonicity it gives only the already audited constant target floor `N2(B)>=3495` for `B>=500000000`.

## 3. Parameter / escape attack inventory

The controller forbids stopping merely because Stage19 already has the upper bound `N2(B)<<_epsilon B^(1/2+epsilon)`. The following attack directions were therefore checked against the frozen Stage17/19 interfaces.

### A. Scalar-family attack

Take a known Stage19 cuboid and scale all edges. This preserves the Diophantine equations but multiplies `gcd(a,b,c)`, so every nontrivial multiple leaves the primitive Stage23 target population.

```text
ATTACK=SCALAR_HOMOTHETY
ESCAPE_FOUND=false
FAILURE=NONTRIVIAL_MULTIPLES_ARE_NONPRIMITIVE
SCALES_TO_UNBOUNDED_PRIMITIVE_FAMILY=false
```

### B. Shared-edge double-Pythagorean coordinates

The Stage18/19 target can be written in shared-edge double-Pythagorean toric coordinates. The extra integral-space condition is not automatically solved by that parametrization; it becomes the exact coupled squareclass equation

\[
\operatorname{sf}(m^2r^2+n^2s^2)=\operatorname{sf}(m^2s^2+n^2r^2).
\]

Thus the existing target parametrization does not itself produce an infinite primitive Stage19 family. It relocates the obstruction into a coupled Gaussian-norm squareclass coincidence.

```text
ATTACK=SHARED_EDGE_DOUBLE_PYTHAGOREAN_REPARAMETRIZATION
ESCAPE_FOUND=false
FAILURE=SPACE_DIAGONAL_REAPPEARS_AS_COUPLED_SQUARECLASS_EQUALITY
```

### C. Squareclass-forcing attack

One may try to force the two Gaussian norms into the same squareclass by imposing extra parameter equalities or symmetries. The frozen ledger contains no audited subfamily for which such forcing simultaneously gives: positive edges, strict canonical ordering, exactly two rather than three square faces, integral space diagonal, global primitivity, infinitely many distinct physical objects, and controlled unbounded height.

Degenerate equalities such as identifying the two parameter pairs risk collapsing edge distinctness/symmetry or changing the face mask; without a proved primitive family they cannot be promoted to a lower bound.

```text
ATTACK=DIRECT_SQUARECLASS_FORCING
ESCAPE_FOUND=false
FAILURE=NO_CERTIFIED_NONDEGENERATE_PRIMITIVE_INFINITE_SUBFAMILY
```

### D. Split-prime parity attack

The Stage19 local sieve describes rejection at good split primes by valuation-parity disagreement. Restricting parameters to satisfy finitely many local parity conditions does not certify the global equality of squareclasses, which requires agreement at all relevant primes. Conversely, the local sieve is a zero-density mechanism, not an existing constructive parametrization of the global survivor set.

```text
ATTACK=SPLIT_PRIME_PARITY_SATISFYING_FAMILY
ESCAPE_FOUND=false
FAILURE=FINITE_LOCAL_CONDITIONS_DO_NOT_CERTIFY_GLOBAL_SQUARECLASS_EQUALITY
```

### E. Stage17 common-coordinate overlay

Stage17 has an abundant one-face-plus-space population with

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3.
\]

Adding a second square face cannot be obtained by merely relabelling the Stage17 parameterization: the target must enter the shared-edge double-Pythagorean geometry and satisfy the Stage19 squareclass condition. No audited map from a positive-density or positive-power Stage17 parameter subset onto primitive Stage19 objects is present in the repository.

```text
ATTACK=STAGE17_STAGE19_COMMON_COORDINATE_OVERLAY
ESCAPE_FOUND=false
FAILURE=NO_CERTIFIED_POSITIVE_POWER_SOURCE_SUBFAMILY_MAPPING_TO_STAGE19
```

## 4. What the search does and does not establish

The attack inventory does **not** prove that an infinite primitive Stage19 family cannot exist. It establishes only that the currently frozen parametrizations, local sieve, scaling operation, and Stage17 overlay do not already supply such a theorem for free.

Accordingly the Stage19 lower-bound gate remains genuinely open:

```text
UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_CONSTRUCTION_FOUND=false
POSITIVE_POWER_LOWER_BOUND_FOUND=false
MATCHING_HALF_POWER_FAMILY_FOUND=false
COUNTEREXAMPLE_TO_HALF_POWER_INTRINSICNESS_FOUND=false
HALF_POWER_INTRINSIC=UNRESOLVED
```

## 5. Checkpoint verdict

Checkpoint20 now has both pieces required by the Stage23 controller: a matched finite census on the common inherited grid and a concrete attack inventory explaining why the obvious parametrization escapes do not yet scale to a certified primitive target family.

The next checkpoint may use the Stage17 asymptotic and Stage19 upper theorem to prove a zero-density upper thinning law, but `upper-bound only` is not sufficient to settle the true Stage23 exponent. The lower-bound / obstruction attack remains live.

```text
EVIDENCE_LEVEL=COMPUTED+PROVED_LEDGER
CHECKPOINT=20
NUM_REUSE_CHECK=PASS
SOURCE_FINITE_ASSET=stages/stage17/17-20/counts.csv
TARGET_FINITE_ASSET=stages/stage19/19-20/counts.csv
MATCHED_CENSUS_REQUIRED=true
MATCHED_CENSUS_STATUS=PASS_ON_COMMON_GRID
PARAMETER_ATTACK_INVENTORY_REQUIRED=true
PARAMETER_ATTACK_INVENTORY_STATUS=PASS
CANDIDATE_FAMILY_GENERATION_REQUIRED=true
CANDIDATE_FAMILY_GENERATION_STATUS=ATTEMPTED_NO_CERTIFIED_ESCAPE
FAILED_FAMILY_CATALOG_REQUIRED=true
FAILED_FAMILY_CATALOG_STATUS=RECORDED
ALTERNATIVE_COORDINATES_TESTED=true
FINITE_DATA_USED_AS_PROOF=false
NEW_ANALYTIC_THEOREM=false
NEW_COMPUTATION_REQUIRED=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=30
CODEX_REQUIRED=false
CODEX_REASON=checkpoint uses frozen exact censuses and theorem/parametrization interfaces; no implementation gap
```
