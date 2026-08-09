# Stage14-num-α — Space-Diagonal Collision Engine

## Purpose

Stage14-num-α is an experimental numerical side track dedicated to one question:

> Can the historical body-diagonal-first search architecture be converted into a materially faster **exact** Stage14 census engine without losing any primitive exactly-two-face objects?

The ordinary rolling `Stage14-numN` observatory remains authoritative until α reproduces its frozen key sets exactly.

## Frozen Stage14 target

The ordinary numerical population is

```text
0<a<b<c
gcd(a,b,c)=1
a^2+b^2+c^2=d^2
d<=B
at least two integral face diagonals
```

Thus α's natural outer variable `d` is already the ordinary Stage14 physical cutoff. Searching `d<=B` covers exactly the same finite height region.

## α1 exact dictionary — COMPLETE

Every active face gives an ordered opposite-edge representation

```text
d^2 = a^2+z^2 = b^2+y^2 = c^2+x^2.
```

For two ordered representations

```text
d^2=a^2+F_a^2=b^2+F_b^2,
```

the residual

```text
c^2=d^2-a^2-b^2=F_a^2-b^2=F_b^2-a^2
```

being a positive square is **equivalent** to reconstructing an integer cuboid with space diagonal `d` and at least those two face diagonals integral. The remaining face-square test separates `N2` from `T`.

Result: `stages/stage14/14-num-alpha1/result.md`.

Locked α1 decisions:

```text
PAIR_COLLISION_ENUMERATION_COMPLETE_FOR_STAGE14_NUM_POPULATION=true
PAIR_COLLISION_ENUMERATION_COMPLETE_FOR_TWO_FACE_OR_MORE=true
ALL_THREE_REQUIRES_CANONICAL_DEDUP_OF_THREE_WITNESSES=true
UNORDERED_REPRESENTATION_WITHOUT_ROLE_TRIAL_INCOMPLETE=true
FULL_ONE_FACE_FROM_PAIR_COLLISIONS_ALONE=false
FULL_ONE_FACE_REQUIRES_NESTED_FACE_DECOMPOSITION=true
PRIMITIVE_FILTER_MUST_USE_RECONSTRUCTED_EDGE_TRIPLE=true
STAGE14_PHYSICAL_CUTOFF_IS_SPACE_DIAGONAL=true
ALPHA_DIAGONAL_RANGE_EQUALS_MAIN_NUM_RANGE=true
D_ODD_AND_ONLY_1MOD4_PRIME_SUPPORT_SAFE=true
PERFECT_SPECIFIC_11_19_PRUNING_SAFE_FOR_N2=false
HISTORICAL_FAST_FACE_LIST_COMPLETE=false
```

### Safe historical ideas

α may use, after exact implementation checks:

- body-diagonal-first enumeration;
- factorization of `d`;
- Girard/Gaussian generation of all representations of `d^2` as two squares;
- primitive-safe diagonal sieve: `d` odd, `d≡1 mod4`, no `3 mod4` prime divisor;
- exact representation collisions and integer-square tests.

### Unsafe historical shortcuts

Do not import without a new N2 completeness proof:

- edge divisibility cuts such as the fast-source `11` and `19` tests;
- any Euler-brick/perfect-only modular filter;
- loop pruning whose proof uses the missing third face being integral;
- optimizations introduced specifically by dropping almost-perfect checks;
- historical later-batch Face-cuboid samples as complete data.

The author explicitly reports that the accelerated historical search dropped most almost-perfect checks and that the later Face-cuboid lists were incomplete.

## Roadmap

### Stage14-num-α2 — Reference collision enumerator

Build the simplest auditable standard-library implementation of the α1 theorem. Use only proven-safe pruning.

For frozen cutoffs compare **canonical key sets**, not only totals:

```text
ALPHA_PAIR_COLLISION_N2_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_FACE_MASKS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_ACTIVE_FACE_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_RAW_EDGE_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_T_EQUAL_MAIN=true
```

No optimization is accepted before these locks pass.

### Stage14-num-α3 — Sum-of-two-squares generation audit

Compare complete generation strategies for `Rep(d^2)`:

1. simple reference generation;
2. factorization/Gaussian-integer synthesis;
3. Girard/Brahmagupta-Fibonacci product generation;
4. segmented/cached diagonal blocks.

Measure factorization cost, number of representations, duplicate work and memory while preserving exact α2 output.

### Stage14-num-α4 — Compatible-representation collision engine

Optimize the collision layer: ordering, indexing, residual-square filters, batching and deduplication. Both role orientations remain mandatory unless a replacement orientation theorem is proved.

### Stage14-num-α5 — Safe-pruning theorem pack

Audit every proposed high-speed filter individually against the complete Stage14 `N2/T` population. Promote only filters with a proof independent of the missing third face. Historical perfect-only congruence tests remain disabled by default.

### Stage14-num-α6 — Frozen-cutoff cross-validation

Require exact equality with ordinary num over multiple frozen cutoffs, including directional counts, masks, active-face ledger, raw edges, max degree, `T(B)` and compatible hashes.

### Stage14-num-α7 — Performance crossover

Benchmark against the ordinary exact num engine under comparable runners and classify:

```text
ALPHA_LOSES
ALPHA_DIAGNOSTIC_ONLY
ALPHA_WINS_CONSTANT_FACTOR
ALPHA_WINS_ASYMPTOTICALLY
```

### Stage14-num-α8 — Large exact cutoff

Only if α7 is favorable, extend the exact Stage14 census beyond the rolling-num frontier while preserving all α2/α6 regression gates.

### Stage14-num-α9 — Optional historical reproduction

Reproduce selected historical diagonal intervals as algorithm validation only. This is never substituted for the Stage14 census.

### Stage14-num-α10+ — Conditional continuation

Continue only on demonstrated performance or structural value.

## Non-goals

- no asymptotic inference from faster finite data;
- no perfect-cuboid nonexistence inference from a finite cutoff;
- no full one-face census requirement before the pair-collision accelerator is evaluated;
- no sacrifice of exactly-two completeness for perfect-cuboid search speed.

## Immediate next task

Start **Stage14-num-α2**: implement the deliberately simple ordered-role collision enumerator over exactly `d<=B` and prove exact key-set equality against ordinary num on small frozen cutoffs.
