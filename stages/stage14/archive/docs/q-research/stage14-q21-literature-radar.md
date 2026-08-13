# Stage14-q21 — q17-good packet / filtered-tau3 pushforward intersection literature radar

## Trigger

Merged `Stage14-s7-143` freezes the exact support obstruction

```text
H = G intersect pi(Lambda),
```

where `G` is the q17-good reciprocal-CRT packet support and `pi(Lambda)` is the pushforward image of the already-charged filtered-tau3 witness support. Scalar and polynomial `(E,m)` measures are separate.

This is not a rerun of q17: the reciprocal-CRT inner kernel is already identified. It is not a rerun of q20: the exact conditioned divisor correlation has already been normalized through the pushforward/intersection formalism.

```text
STAGE14_Q21=COMPLETE_Q17_GOOD_PACKET_PUSHFORWARD_INTERSECTION_LITERATURE_RADAR
Q21_EXACT_OBSTRUCTION=FilteredTau3ConditionedQ17GoodPacketPushforwardIntersectionLowerCoverage
```

## Promotion standard

A direct theorem must, on every frozen principal cell, preserve:

1. the exact filtered-tau3 first-layer conditioning;
2. the q17 reciprocal-CRT good-packet predicate defining `G`;
3. the deterministic pushforward `pi`;
4. the charged scalar or polynomial `(E,m)` outer measure;
5. a lower-support / lower-ratio conclusion for `G intersect pi(Lambda)`;
6. the existing quantifier order, without replacing an individual cell by modulus/residue averaging.

Average divisor counts, one-sided fiber bounds, or equidistribution of a larger ambient sequence are insufficient unless an exact adapter to the intersection support is proved.

## Primary-source radar

### Fouvry--Tenenbaum — multiplicative functions in large arithmetic progressions

Primary source: arXiv:2004.04766, *Multiplicative functions in large arithmetic progressions and applications*.

Useful architecture: Bombieri--Vinogradov type distribution for broad multiplicative-function classes and applications to arithmetic correlations.

Verdict: `NEAR_DISTRIBUTION_ARCHITECTURE`, not direct. The Stage14 target is an intersection of a conditioned pushforward image with a separately defined q17-good support on every principal cell; no exact identification with their admissible sequence/AP average is proved.

### Nguyen — generalized divisor functions in arithmetic progressions

Primary source: arXiv:2308.06839, *Generalized divisor functions in arithmetic progressions: I*.

Useful architecture: distribution of `d_k` in arithmetic progressions, including beyond-square-root modulus ranges under averaging/structural hypotheses.

Verdict: `NEAR_FILTERED_TAU3_DISTRIBUTION`, not direct. Stage14 still lacks an exact map from `H=G intersect pi(Lambda)` to a single generalized-divisor AP sum preserving the q17-good predicate and charged measure.

### Shparlinski — restricted divisor function in arithmetic progressions

Primary source: arXiv:1003.5347, *On the Restricted Divisor Function in Arithmetic Progressions*.

Useful architecture: asymptotics for restricted factor-pair counts in short arithmetic progressions.

Verdict: `BACKGROUND_RESTRICTED_DIVISOR_SUPPORT`, not direct. It controls restricted divisor counts, not the lower density of the intersection between the filtered-tau3 pushforward image and the q17-good support.

### Grimmelt--Merikoski — divisor function along AP / binary cubic polynomial

Primary source: arXiv:2508.17979, *The divisor function along arithmetic progressions and binary cubic polynomials*.

Useful architecture: strong divisor equidistribution for factorable moduli and polynomial applications.

Verdict: `NEAR_FACTORABLE_MODULUS_DISTRIBUTION`, not direct. No current Stage14 encoding turns the exact good-packet intersection into their divisor-AP or binary-cubic average while retaining both charged measure variants.

## Direct-theorem verdict

No audited primary source directly proves the required uniform lower coverage

```text
#(G intersect pi(Lambda)) >= B^(-o(1)) #pi(Lambda)
```

(or an equivalent branch-specific lower ratio) on every frozen Stage14 principal cell while preserving all filters and charged measures.

```text
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q17_GOOD_PUSHFORWARD_INTERSECTION_DIRECT_THEOREM_FOUND=false
GENERALIZED_DIVISOR_AP_TO_INTERSECTION_ADAPTER_PROVED=false
MULTIPLICATIVE_FUNCTION_AP_TO_INTERSECTION_ADAPTER_PROVED=false
RESTRICTED_DIVISOR_TO_INTERSECTION_ADAPTER_PROVED=false
FACTORABLE_MODULUS_DIVISOR_TO_INTERSECTION_ADAPTER_PROVED=false
```

## Handoff

Before opening a new s-local H, test whether the q17-good indicator can be expressed against the pushforward measure by an exact nonnegative correlation weight:

```text
Q21_GOOD_PACKET_INDICATOR_CORRELATION_ENCODING_TEST
RECEIVER=Stage14-s7-144
```

Target a formula of the form

```text
#Lambda_H = sum_{lambda in Lambda} 1_G(pi(lambda))
```

with `1_G(pi(lambda))` expanded into a fixed-complexity divisor/AP/congruence weight that preserves every first-layer filter.

If this succeeds, next test whether a first/second moment or dispersion estimate controls this exact nonnegative correlation:

```text
Q21_INTERSECTION_FIRST_SECOND_MOMENT_TEST
RECEIVER=Stage14-s7-145+
```

If the indicator cannot be normalized to an existing theorem architecture, freeze the exact intersection correlation itself as a new H-ready target rather than silently averaging away the conditioned measure.

```text
Q21_NEXT_SEARCH_TRIGGER=exact_indicator_normal_form_or_new_H_ready_intersection_correlation_or_new_external_result
Q21_POST_MASK_SEARCHED=false
Q21_FIXED_U_SEARCHED=false
```
