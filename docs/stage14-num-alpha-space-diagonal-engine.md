# Stage14-num-α — Space-Diagonal Collision Engine

## Purpose

Stage14-num-α is a side experimental numerical track dedicated to one question only:

> Can a space-diagonal-first enumeration, inspired by large perfect-cuboid searches, be converted into a much faster exact Stage14 census engine for primitive one-face / two-face / three-face incidence data?

This is intentionally separate from the ordinary `Stage14-numN` rolling observatory. The normal num track protects its existing exact-census semantics and physical-height history. num-α may change parametrization, enumeration order, storage format, and algorithmic architecture aggressively, but it must reproduce the ordinary num census exactly on overlapping ranges before it is trusted.

## Mathematical object

For a cuboid with edges `a,b,c`, face diagonals `x,y,z`, and space diagonal `d`,

```text
x^2 = a^2+b^2
y^2 = a^2+c^2
z^2 = b^2+c^2
d^2 = a^2+b^2+c^2.
```

Each active face therefore gives an ordered opposite-edge representation

```text
d^2 = a^2+z^2 = b^2+y^2 = c^2+x^2.
```

`Stage14-num-α1` has now proved the exact collision dictionary:

```text
TWO_FACE_OR_MORE
<=>
two distinct ordered representations of one d^2 have positive-square cross-difference.
```

The representation role must be tried in both orientations; an unordered `{u,v}` alone is insufficient. An all-three-face object gives three collision witnesses and must be canonicalized to one object. A full one-face census cannot be recovered from pair collisions alone; it requires a nested decomposition of the opposite face diagonal square.

Result: `stages/stage14/14-num-alpha1/result.md`.

## Non-goals

- Do not infer asymptotics from the accelerated census.
- Do not treat historical almost-perfect counts as complete unless their enumeration contract is proved complete.
- Do not replace the ordinary num source until overlap equality is exact.
- Do not optimize for the perfect-cuboid yes/no test at the cost of losing two-face objects; Stage14 specifically needs the one-to-two-to-three transition data.

## Roadmap

### Stage14-num-α1 — Exact algorithm reconstruction and Stage14 dictionary — COMPLETE

Locked results:

```text
PAIR_COLLISION_ENUMERATION_COMPLETE_FOR_TWO_FACE_OR_MORE=true
ALL_THREE_REQUIRES_CANONICAL_DEDUP_OF_THREE_WITNESSES=true
UNORDERED_REPRESENTATION_WITHOUT_ROLE_TRIAL_INCOMPLETE=true
FULL_ONE_FACE_FROM_PAIR_COLLISIONS_ALONE=false
FULL_ONE_FACE_REQUIRES_NESTED_FACE_DECOMPOSITION=true
PRIMITIVE_FILTER_MUST_USE_RECONSTRUCTED_EDGE_TRIPLE=true
PHYSICAL_B_TO_DIAGONAL_ENVELOPE_NOT_YET_LOCKED=true
```

### Stage14-num-α2 — Reference implementation

Build a small standard-library reference enumerator implementing the α1 ordered-role collision theorem. Prioritize the current Stage14 two-face population: reconstruct canonical object keys, masks, raw-pair edges and `T`, then compare exact key sets against ordinary num on small frozen cutoffs.

Required lock:

```text
ALPHA_PAIR_COLLISION_N2_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_FACE_MASKS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_RAW_EDGE_KEYS_EQUAL_MAIN=true
ALPHA_PAIR_COLLISION_T_EQUAL_MAIN=true
```

Nested one-face mode is optional at this stage and must not delay validation of the pair-collision accelerator.

### Stage14-num-α3 — Sum-of-two-squares generation audit

Compare candidate generation strategies for `d^2`:

1. direct Euclid/Pythagorean generation;
2. factorization/Gaussian-integer representation generation;
3. divisor-formula/Girard style representation synthesis;
4. cached or segmented representation generation by diagonal interval.

Measure candidate counts, duplication, factorization cost, and memory. Preserve completeness certificates for the exact target range.

### Stage14-num-α4 — Compatible-representation collision engine

Optimize the α1 collision layer after α2 exact equality is locked. Preserve both role orientations and canonical deduplication; do not optimize away exactly-two objects.

### Stage14-num-α5 — Primitive and physical-height transfer

Prove and implement the exact conversion between the diagonal-first search range and the ordinary Stage14 physical cutoff. Determine the diagonal envelope needed for complete ordinary-`B` coverage.

### Stage14-num-α6 — Cross-validation at existing frozen cutoffs

Run α against multiple already-frozen ordinary num cutoffs and require byte-level/canonical-key equality for totals, directional counts, masks, raw-pair edges, max degree, `T(B)`, and compatible hashes.

### Stage14-num-α7 — Performance crossover test

Benchmark α against the current exact num engine under identical hardware/runtime constraints. Classify `ALPHA_LOSES`, `ALPHA_DIAGNOSTIC_ONLY`, `ALPHA_WINS_CONSTANT_FACTOR`, or `ALPHA_WINS_ASYMPTOTICALLY`.

### Stage14-num-α8 — Stage14-complete large-cutoff mode

Only if α7 is favorable, scale while preserving the complete two-face census.

### Stage14-num-α9 — Optional historical-search reproduction

Reproduce selected published diagonal-first intervals/results as algorithm validation only. Historical incomplete almost-perfect lists are not Stage14 census data.

### Stage14-num-α10+ — Conditional continuation

Continue only if the engine demonstrates meaningful performance gain or an independent structural diagnostic.

## Acceptance contract

```text
EXACT_OVERLAP_WITH_MAIN_NUM=true
TWO_FACE_ENUMERATION_COMPLETE=true
PRIMITIVE_SEMANTICS_IDENTICAL=true
PHYSICAL_HEIGHT_SEMANTICS_IDENTICAL=true
NO_HISTORICAL_INCOMPLETE_FACE_LIST_USED_AS_CENSUS=true
```

Performance remains separate:

```text
MEANINGFUL_SPEEDUP_PROVED=false
LARGER_EXACT_STAGE14_CUTOFF_REACHED=false
```

## Immediate next task

Start **Stage14-num-α2**: implement the simplest auditable ordered-representation collision enumerator and require exact canonical-key equality with ordinary num before any optimization.