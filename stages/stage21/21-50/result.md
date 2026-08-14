# Stage21-50 — lower-side mechanism and constructive-survivor diagnostic

EVIDENCE_LEVEL=PROVED
CHECKPOINT=50
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT

## 1. Purpose

Checkpoint30 proves

\[
N_1(B)/M_1(B)\sim (\kappa\pi/18)(\log B)^2/B.
\]

Checkpoint40 leaves the two logarithms mechanistically unresolved. Checkpoint50 tests whether the explicit AR-039 survivor family can account for the full transition scale.

## 2. AR-039 original construction interface

The AR-039 registry and its Stage11 source define admissible coprime parameters

\[
m>n\ge1,\qquad m\equiv2\pmod{14},\qquad n\equiv1\pmod{14},
\]

with

\[
x=m^2-n^2,\quad y=2mn,\quad p=m^2+n^2,
\]
\[
c=(p^2-1)/2,\qquad d=(p^2+1)/2.
\]

After canonical sorting of `x,y`, the resulting cuboid is primitive, has integral space diagonal `d`, and exactly one integral face. AR-039 records that this is an injective two-parameter subfamily.

Its audited lower bound is

\[
N_{\rm AR039}(B)\ge
\frac{\sqrt2}{120\pi^2}B^{1/2}-O(B^{1/4}\log B).
\]

## 3. New upper count for the AR-039 family

The Stage11 source gives the exact height formula

\[
d=\frac{(m^2+n^2)^2+1}{2}.
\]

If an AR-039 point satisfies `d<=B`, then

\[
(m^2+n^2)^2\le 2B-1<2B.
\]

Hence

\[
m^2<m^2+n^2<(2B)^{1/2},
\]

so

\[
m<(2B)^{1/4}.
\]

For each such `m`, there are at most `m-1` possible positive `n<m`; dropping the congruence and coprimality restrictions only enlarges the count. Therefore the number of admissible parameter pairs with `d<=B` is at most

\[
\sum_{m<(2B)^{1/4}}(m-1)=O(B^{1/2}).
\]

Because AR-039 is injective on admissible parameter pairs, the same upper bound holds for the constructed cuboids:

\[
\boxed{N_{\rm AR039}(B)=O(B^{1/2})}.
\]

Combined with the audited lower bound,

\[
\boxed{N_{\rm AR039}(B)=\Theta(B^{1/2})}.
\]

This upper argument uses only the exact AR-039 height formula and injectivity already stated in the frozen registry/source; no new arithmetic equidistribution theorem is required.

## 4. Conditional scale of the whole AR-039 family

The strongest matched Stage16 source law is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Therefore

\[
\boxed{
\frac{N_{\rm AR039}(B)}{M_1(B)}
=\Theta\!\left(B^{-3/2}(\log B)^{-1}\right)
}.
\]

The true Stage21 conditional survival is

\[
\frac{N_1(B)}{M_1(B)}
\sim \frac{\kappa\pi}{18}B^{-1}(\log B)^2.
\]

Thus

\[
\frac{N_{\rm AR039}(B)/M_1(B)}{N_1(B)/M_1(B)}
=O\!\left(B^{-1/2}(\log B)^{-3}\right)\to0.
\]

Equivalently,

\[
\boxed{N_{\rm AR039}(B)=o(N_1(B))}.
\]

So the **entire** AR-039 family, not merely its certified lower contribution, is asymptotically negligible in Stage17 and cannot explain the full `(log B)^2` enhancement.

## 5. Mechanism consequence

The known explicit two-parameter construction is too thin by a factor tending to infinity. Any constructive explanation of the full Stage21 enhancement would need a substantially larger family, on the `B(log B)^3` numerator scale up to constant order, or a theorem showing how many such parameter families collectively fill that bulk.

The present result therefore upgrades checkpoint40's boundary:

```text
FULL_TRANSITION_SCALE=B^-1*(log B)^2
AR039_FAMILY_COUNT=Theta(B^1/2)
AR039_CONDITIONAL_SCALE=Theta(B^-3/2*(log B)^-1)
AR039_IS_NEGLIGIBLE_IN_N1=true
AR039_EXPLAINS_LOG_SQUARED_ENHANCEMENT=false
KNOWN_EXPLICIT_FAMILY_MECHANISM_EXCLUDED=true
BULK_ARITHMETIC_MECHANISM_STILL_REQUIRED=true
OPEN_GATE=LOG_SQUARED_ENHANCEMENT_BULK_MECHANISM_UNRESOLVED
```

## 6. Provenance / contract

The load-bearing AR-039 facts are frozen in `docs/stage14-arsenal.md` (imported by PR #878) and sourced there to `stages/stage11/scripts/audit_shared_p_convolution.py`. The source explicitly defines the admissible parameters, the exact formulas, validates primitivity/exactly-one, and supplies the height relation. The registry explicitly labels the family injective.

```text
UPSTREAM_INTERFACE=AR-039 / Stage11 source
POPULATION_MATCH=true
CUTOFF_MATCH=true_after_d_equals_R
MULTIPLICITY_MATCH=true_by_injectivity
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
NEW_UPPER_ARGUMENT=elementary_parameter_count_from_exact_height
FINITE_DATA_USED_AS_PROOF=false
DOUBLE_CHARGE_CHECK=PASS
```

Checkpoint30/40 theorems are unchanged.

```text
NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage21-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
