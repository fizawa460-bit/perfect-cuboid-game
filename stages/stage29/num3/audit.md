# Stage29-num3 — one-pass lightweight audit

```text
AUDITED_PR=1296
AUDITED_MATHEMATICAL_HEAD=218439b20b3eb12381bce29db9f472a0b59ebe79
AUDIT_REGRESSION_HEAD=2f46a38b5e351abe59696a4550ae243a491aed97
AUDIT_SCOPE=FIVE_REQUESTED_CHECKS_ONLY
AUDIT_VERDICT=PASS
```

This is the requested single lightweight correctness audit. It is not an invitation to repeat adversarial review loops after the five requested checks pass.

## 1. Shared-edge multiplicity: `M2 = G - 3*M3`

There are three face types, indexed by edge pairs `ab`, `ac`, `bc`.

- If exactly two face diagonals are integral, the two successful face types have exactly one common coordinate edge. Therefore the cuboid contributes exactly one shared-edge incidence to `G`.
- If all three face diagonals are integral, each coordinate edge is the common edge of one pair of successful faces. Therefore every primitive Euler cuboid contributes exactly three shared-edge incidences to `G`.

The shared-edge counter uses an unordered partner pair `{x,y}` for each fixed edge `e`, so there is no partner-order doubling. Hence, under the same primitive/cutoff contract,

```text
G = M2 + 3*M3
M2 = G - 3*M3
```

exactly. The directional subtraction `M2_j=G_j-M3` is also exact because an Euler cuboid contributes once with the shared edge in each of the three canonical coordinate positions.

```text
IDENTITY_M2_EQ_G_MINUS_3M3=PASS
SHARED_EDGE_MULTIPLICITY_EXACT=PASS
PARTNER_ORDER_DOUBLE_COUNT=false
```

## 2. Möbius primitivity

For a fixed shared edge `e`, the aggregate counter applies

```text
1_{gcd(e,x,y)=1} = sum_{d|e, d|x, d|y} mu(d).
```

It factors `e`, enumerates every squarefree divisor with its Möbius sign, filters the complete partner list by divisibility by `d`, and counts the corresponding unordered pairs under the identical Euclidean cutoff. This is exact Möbius inversion for `gcd(e,x,y)=1`, which is the same condition as `gcd(a,b,c)=1` after canonical reordering.

The independent direct counter does not use Möbius inversion: it explicitly evaluates `gcd(e,gcd(x,y))==1`. Exact agreement with that implementation at `10^6` and `10^7` is therefore also an independent regression of the primitivity layer.

```text
MOBIUS_PRIMITIVITY=PASS
GCD_ABC_EXACT=PASS
```

## 3. Euclidean cutoff and canonical population

The Möbius counter computes

```text
B2 = B^2
e2 = e^2
room = B2-e2
x^2+y^2 <= room
```

using `__uint128_t` in the load-bearing square/sum comparisons, so this is exactly

```text
e^2+x^2+y^2 <= B^2.
```

The partner pair is unordered and distinct. For a positive integer Pythagorean face, `e=x` would imply an integral hypotenuse `sqrt(2)e`, so equal box edges cannot arise in a successful face. Thus each accepted cuboid has three distinct positive edges. Comparing `e` with the sorted partners assigns whether the shared edge is canonical `a`, `b`, or `c`; it does not create a second object count.

The direct comparator independently generates scaled primitive Pythagorean triples, groups by shared leg, explicitly tests the same Euclidean cutoff and gcd condition, and obtains the same canonical directional counts.

```text
EUCLIDEAN_CUTOFF_R_LE_B=PASS
CANONICAL_STRICT_ORDER_NO_LEAK=PASS
DIRECTION_PARTITION=PASS
```

## 4. Independent direct regressions at `10^6` and `10^7`

Audit CI run:

```text
RUN=32450628885
```

compiles and runs two materially different implementations:

- direct enumerator: Euclid primitive triples + all scales + explicit pair loop + explicit gcd;
- aggregate enumerator: divisor-of-square partner generation + Möbius inversion + two-pointer pair counting.

They agree exactly in total `M2` and all three directional counts:

```text
B=1,000,000
M2=13,817,725
M3=219
M2_direction=[4,592,536,5,816,786,3,408,403]
DIRECT_EQUALS_MOBIUS=true

B=10,000,000
M2=224,273,087
M3=656
M2_direction=[76,864,512,93,602,678,53,805,897]
DIRECT_EQUALS_MOBIUS=true
```

The direct run also independently recovers `N2(10^6)=255`, `N2(10^7)=720`, and `P=0` at both checkpoints. Existing aggregate-only checks at `5*10^6` and `5*10^7` also pass in the same run.

Because the two counters differ in partner generation, primitivity enforcement and pair counting, the `10^6`/`10^7` exact equality is accepted as a sufficient independent regression for this numerical method.

```text
INDEPENDENT_DIRECT_REGRESSION_B1M=PASS
INDEPENDENT_DIRECT_REGRESSION_B10M=PASS
ADDITIONAL_INDEPENDENT_REGRESSION_REQUIRED=false
```

## 5. Integer-range / overflow audit through `B=10^9`

For the production aggregate algorithm with `B<=10^9`:

- `B^2,t^2 <= 10^18 < 2^64`; load-bearing square sums use `u128` anyway.
- The odd SPF stores only smallest prime factors `<=sqrt(10^9)<31623`, safely inside `uint16_t`.
- Partner coordinates and divisors consumed by the algorithm are at most the `10^9`/`10^18` scales represented by `u64`.
- The maximum number of distinct prime factors below `10^9` is below the fixed factor-array capacity `12`.
- A monotone prime-exponent enumeration for `n<=10^9` gives `max tau(n^2)=47,385`; hence fewer than `23,692` positive partners occur for one edge. The crude total unordered-pair bound is therefore below `2.81*10^17`, safely below `2^64`.
- Even a crude bound of `512` squarefree-divisor filters per edge times `23,692` partners times `10^9` edges is about `1.22*10^16`, also below `2^64`.
- Signed per-edge Möbius accumulators are many orders below `int64_t` range.

The direct comparator also stays integer-safe at `B<=10^9`: coordinates fit `uint32_t`, while `e^2+x^2+y^2<=3*10^18<2^64`.

The aggregate SPF allocation at `B=10^9` is about one billion bytes. That is an operational memory/runtime concern, not an integer-overflow or exactness defect. A full `M2(10^9)` production run has not been performed by this audit.

```text
INTEGER_RANGE_TO_B1E9=PASS
OVERFLOW_BLOCKER=false
FULL_M2_1E9_PRODUCTION_RUN=false
```

## Final verdict

All five requested checks pass. No additional adversarial-review cycle is required for the correctness contract audited here. Any later work should be a production-scale execution/engineering task, not another replay of these five proofs.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT_STAGE29_NUM3_LIGHT_AUDIT=PASS
IDENTITY_M2_EQ_G_MINUS_3M3=PASS
MOBIUS_PRIMITIVITY=PASS
CUTOFF_AND_CANONICAL=PASS
INDEPENDENT_DIRECT_REGRESSION_B1M=PASS
INDEPENDENT_DIRECT_REGRESSION_B10M=PASS
INTEGER_RANGE_TO_B1E9=PASS
FULL_M2_1E9_PRODUCTION_RUN=false
ADDITIONAL_ADVERSARIAL_REVIEW_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=Stage29-num3-production-or-integration
NEXT_EXPECTED_COMMAND=Stage29-num3-production
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
