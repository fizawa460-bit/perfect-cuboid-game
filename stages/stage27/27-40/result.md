# Stage27-40 — strict sub-square-root upper attack

```text
TASK_ID=Stage27-40
CHECKPOINT=40
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=PROVED_MECHANISM_BOUNDARY_CANDIDATE_PLUS_EXACT_REOPEN_CONTRACT
TARGET=N2(B)
CURRENT_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
STRICT_SUB_SQRT_TARGET=N2(B)<<_epsilon B^(mu+epsilon), mu<1/2
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_N2_EXPONENT_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
```

## 1. Authorization and population

Checkpoint30 hostile audit passed and PR #1024 merged at

```text
cf0f2a378ca6a3338670063821efb513e0aaeb73
```

The target remains the same primitive canonical physical population

\[
N_2(B)=\#\{0<a<b<c,\ \gcd(a,b,c)=1,\ R\in\mathbf Z,\ R\le B,\ \text{exactly two integral face diagonals}\}.
\]

No population, cutoff, multiplicity, or measure adapter is changed here.

## 2. Current half-power theorem and its exact bottleneck

Stage14 Theorem 2.1 gives

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

Its active proof chain is

\[
N_2(B)\le E(B),
\qquad
E(B)\ll V(B)B^{o(1)},
\qquad
V(B)\ll B^{1/2+o(1)}.
\]

The elliptic-fiber degree contributes only `B^o(1)`. The fixed exponent `1/2` is therefore supplied by the whole-family active-vertex host in Stage14 Proposition 3.6, not by a large vertical fiber.

On the balanced packet, the terminal complete-host case split is:

- proportional branch: exponent at most `7/16`;
- nonproportional `theta<=1/4`: `E_k<=3theta-1/4<=1/2`;
- nonproportional `theta>=1/4`: high-core cells with `chi>1/4` are empty and the remaining receiver gives `E_RRF<=1-2theta<=1/2`.

Thus any strict whole-family exponent improvement must remove a fixed-power portion of the boundary saturation near the `1/2` faces of this complete-host envelope, or replace the complete-host count by a genuinely stronger same-measure theorem. Merely reducing divisor/fiber multiplicity cannot change the exponent.

```text
HALF_POWER_SOURCE=ACTIVE_VERTEX_HOST
VERTICAL_FIBER_FIXED_POWER_BOTTLENECK=false
SUBPOLYNOMIAL_FIBER_IMPROVEMENT_CANNOT_GIVE_STRICT_SUBHALF=true
```

## 3. Latest Stage15-6 causal squareclass mechanism

Stage15-6 gives the exact same-measure local acceptance law for every good split prime `p=1 mod 4`:

\[
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}{(p+1)^2(p^2+6p+1)},
\]

so

\[
1-\rho_p=\frac4p+O(p^{-2}).
\]

For each fixed finite set `S` of such primes, the congruence-refined host has density `prod_{p in S} rho_p`; taking `B->infinity` first and then enlarging `S` proves `N2/M2->0`.

The local Euler product itself satisfies

\[
\prod_{\substack{p\le z\\p\equiv1\pmod4}}\rho_p
=(\log z)^{-2+o(1)}.
\]

Consequently, even a hypothetical uniform implementation of this *same parity tensor* through a polynomial prime range `z=B^A` would naturally yield only

\[
(\log B)^{-2+o(1)}
\]

thinning. It would not by itself produce a factor `B^{-delta}` for fixed `delta>0`.

This is a mechanism-specific negative certificate. It is **not** an impossibility theorem for every future method.

```text
LOCAL_PARITY_SIEVE_SAME_MEASURE=true
LOCAL_PRODUCT_POLYNOMIAL_RANGE_SCALE=LOGARITHMIC_ONLY
GROWING_MODULUS_ALONE_WITH_SAME_RHO_P_IMPLIES_FIXED_POWER=false
FIXED_PRIME_ZERO_DENSITY_PROMOTED_TO_POWER=false
```

## 4. Reopened and rejected upper routes

The Stage14/15 824-record attack inventory and the post-Stage25 discovery ledger were re-read against the checkpoint40 target.

### U40-A — Stage14 complete-host saturation

This is the direct route to a strict exponent improvement. A successful theorem must improve the saturated nonproportional boundary uniformly on the same physical measure, e.g. replace the complete `1/2` envelope by `1/2-delta` for one fixed `delta>0` on every saturation cell not already below half.

**Status:** `EXTERNAL_OR_NEW_INTERNAL_THEOREM_REQUIRED`.

### U40-B — fixed-prime / growing-modulus squareclass sieve (Q11)

Exact local conditions are reusable and same-measure. However the exact product is logarithmic. Growing-modulus uniformity is valuable for an effective log-rate and causal refinement, but **is not sufficient by itself** for strict sub-half polynomial exponent progress.

**Status:** `USEFUL_BUT_NOT_STRICT_SUBHALF_BY_ITSELF`.

### U40-C — admissible physical-diagonal Kummer support (Q06)

The audited reduction reaches a `(4,4)` product-square/Kummer support receiver under physical height `Y<=2B`, with only `B^o(1)` fixed-diagonal fibers. The old target `|S(B)|<<B^(1/2+o(1))` merely reproduces half-power scale. Checkpoint40 sharpens the required future contract:

\[
\boxed{|S(B)|\ll_\varepsilon B^{1/2-\delta+\varepsilon}}
\]

for some fixed `delta>0`, on the exact admissible physical support, is sufficient for strict sub-half `N2`.

A theorem only of order `B^(1/2+o(1))` is **not** progress at Stage27-40.

**Status:** `EXTERNAL_STRICT_SUPPORT_GATE`.

### U40-D — moving genus-one small-support receiver (Q05)

The moving genus-one/intersection-of-two-quadrics reduction is exact on its compatible subfamily, but no same-measure global norm-core aggregation or uniform physical-height theorem was previously available. To affect the whole-family exponent, a future result must include both:

1. a global adapter covering the saturation-band physical measure up to `B^o(1)` multiplicity; and
2. a fixed-power deficit `B^{-delta}` relative to the half-power complete host.

Uniform finiteness or rank-dependent pointwise bounds without a global measure adapter do not suffice.

**Status:** `EXTERNAL_MOVING_FAMILY_GATE`.

### U40-E — MAIN/T/S external analytic receivers

Stage14 final records three genuinely different gates:

- MAIN: uniform primitive-rectangle nested quadratic-divisor root first moment;
- T: pointwise Gaussian residue long-interval prime occupancy beyond the current conductor envelope;
- S: target-class principal domination on the conditioned moving-character measure.

Checkpoint40 does not conflate them and does not multiply hypothetical savings. Any one may reopen only if its exact theorem supplies a fixed-power deficit on **every retained saturation cell** or an exceptional-set estimate that is chargeable in the same physical measure.

**Status:** `EXTERNAL_THEOREM_SPECIES_DISTINCT`.

## 5. External-literature radar

A fresh primary-source search was made for uniform rational-point results on moving genus-one curves and Kummer/quartic surfaces. The papers located do not, on their stated theorem surfaces, provide the exact same-measure `R<=B` support theorem with exponent `1/2-delta` required above. No external theorem is imported by this checkpoint.

```text
EXTERNAL_THEOREM_ADAPTER_FOUND=false
EXTERNAL_RESULT_IMPORTED=false
```

## 6. Checkpoint40 verdict

The strict sub-square-root theorem is **not** proved:

\[
\boxed{
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
}
\]

remains the strongest audited global upper.

But checkpoint40 closes two false shortcuts and produces an exact restart interface:

1. improving only the `B^o(1)` elliptic/divisor fibers cannot change the `1/2` exponent;
2. making the existing local parity sieve effective through polynomial-size primes still yields logarithmic, not polynomial, thinning for that same local tensor.

A genuine strict sub-half result must therefore attack the **horizontal saturation-band support/complete-host mass** or introduce a different global arithmetic theorem with a same-measure fixed-power deficit.

The highest-priority reopen contracts for Stage27-60 are:

```text
U40-G1=SATURATION_BAND_COMPLETE_HOST_POWER_DEFICIT
U40-G2=PHYSICAL_KUMMER_SUPPORT_B^(1/2-delta+epsilon)
U40-G3=MOVING_GENUS_ONE_GLOBAL_MEASURE_PLUS_POWER_DEFICIT
U40-G4=MAIN_OR_T_OR_S_EXTERNAL_GATE_WITH_SAME_MEASURE_FIXED_POWER_DEFICIT
```

Checkpoint50 remains the lower attack and is not pre-empted by this negative upper result.

```text
UPPER_ATTACK_EXECUTED=true
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_MU=1/2
NEW_MU_LT_HALF_PROVED=false
MECHANISM_SPECIFIC_NEGATIVE_CERTIFICATE_CANDIDATE=true
HALF_POWER_HORIZONTAL_SATURATION_IDENTIFIED=true
LOCAL_PARITY_SIEVE_FIXED_POWER_ROUTE_CLOSED=true
EXACT_REOPEN_CONTRACTS_MATERIALIZED=true
FINITE_ALPHA_USED_AS_PROOF=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=50
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_EXPECTED_COMMAND=Stage27-audit
```