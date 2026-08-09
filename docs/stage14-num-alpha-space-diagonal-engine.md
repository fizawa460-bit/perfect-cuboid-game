# Stage14-num-α — Space-Diagonal Collision Engine

## Purpose

Stage14-num-α is a side experimental numerical track dedicated to one question only:

> Can a space-diagonal-first enumeration, inspired by large perfect-cuboid searches, be converted into a much faster exact Stage14 census engine for primitive one-face / two-face / three-face incidence data?

This is intentionally separate from the ordinary `Stage14-numN` rolling observatory. The normal num track protects its existing exact-census semantics and physical-height history. num-α may change parametrization, enumeration order, storage format, and algorithmic architecture aggressively, but it must reproduce the ordinary num census exactly on overlapping ranges before it is trusted.

## Mathematical object

For a cuboid with edges `a,b,c`, face diagonals `x,y,z`, and space diagonal `d`, the common-diagonal identities are

```text
x^2 = a^2+b^2
y^2 = a^2+c^2
z^2 = b^2+c^2
d^2 = a^2+b^2+c^2
```

Equivalently, each face completion can be viewed through a representation of `d^2` as a sum of two squares, for example

```text
d^2 = a^2 + z^2 = b^2 + y^2 = c^2 + x^2.
```

A space-diagonal-first engine therefore generates structured sum-of-two-squares representations of `d^2` and searches for compatible collisions among them, rather than scanning physical edge triples directly.

The Stage14 use-case is broader than a perfect-cuboid existence search: retain enough information to classify exact incidence multiplicity among the three face conditions, preserve primitive normalization, recover physical height, and produce the same canonical object/raw-edge keys used by the ordinary num track.

## Non-goals

- Do not infer asymptotics from the accelerated census.
- Do not treat historical almost-perfect counts as complete unless their enumeration contract is proved complete.
- Do not replace the ordinary num source until overlap equality is exact.
- Do not optimize for the perfect-cuboid yes/no test at the cost of losing two-face objects; Stage14 specifically needs the one-to-two-to-three transition data.

## Roadmap

### Stage14-num-α1 — Exact algorithm reconstruction and Stage14 dictionary

Reconstruct the space-diagonal-first enumeration mathematically from primary/authoritative algorithm descriptions where possible. Write an explicit dictionary between:

- a representation `d^2 = u^2+v^2`;
- edge / face-diagonal roles;
- compatible pairs/triples of representations;
- Stage14 canonical primitive object keys;
- face masks and raw-pair edges;
- physical cutoff semantics.

Prove exactly which representation collisions correspond to one-face, two-face, and three-face cuboids and identify duplicate symmetries.

Deliverable: an exact specification, not yet an optimized implementation.

### Stage14-num-α2 — Reference implementation

Build a small standard-library reference enumerator using the α1 dictionary. It may be slow, but it must be simple enough to audit. On small cutoffs, compare object-by-object against the existing Stage14 exact enumerator.

Required lock:

```text
ALPHA_REFERENCE_EQUALS_EXISTING_NUM_OBJECT_KEYS=true
ALPHA_REFERENCE_EQUALS_EXISTING_FACE_MASKS=true
ALPHA_REFERENCE_EQUALS_EXISTING_RAW_EDGES=true
```

No performance claim before these are true.

### Stage14-num-α3 — Sum-of-two-squares generation audit

Compare candidate generation strategies for `d^2`:

1. direct Euclid/Pythagorean generation;
2. factorization/Gaussian-integer representation generation;
3. divisor-formula/Girard style representation synthesis;
4. cached or segmented representation generation by diagonal interval.

Measure candidate counts, duplication, factorization cost, and memory. Preserve completeness certificates for the exact target range.

### Stage14-num-α4 — Compatible-representation collision engine

Design the efficient collision layer that reconstructs cuboid edge triples from multiple representations of the same `d^2`. The engine must distinguish:

- single usable face incidence;
- exactly two face incidences;
- all three face incidences;
- degenerate or symmetry-duplicate collisions.

Use canonical sorting/gcd normalization identical to the main Stage14 semantics.

### Stage14-num-α5 — Primitive and physical-height transfer

Prove and implement the exact conversion between the diagonal-first search range and the ordinary Stage14 physical cutoff. Determine whether searching `d<=D` gives a clean complete region for the existing `B` convention or whether edge/diagonal inequalities require a conversion envelope.

Primitive filtering must be applied at the correct stage; a fast diagonal generator must not silently overcount scaled copies.

### Stage14-num-α6 — Cross-validation at existing frozen cutoffs

Run α against multiple already-frozen ordinary num cutoffs and require byte-level/canonical-key equality for:

- total objects;
- directional counts;
- face masks;
- raw-pair edges;
- max degree;
- `T(B)`;
- object and edge hashes where compatible.

Any disagreement blocks further scale-up until adjudicated.

### Stage14-num-α7 — Performance crossover test

Benchmark α against the current exact num engine under identical hardware/runtime constraints. Record wall-clock, peak memory, candidate representations, factorization workload, and output rate.

Classify:

- `ALPHA_LOSES`: no reason to pursue for scale;
- `ALPHA_DIAGNOSTIC_ONLY`: useful alternative cross-check but not faster;
- `ALPHA_WINS_CONSTANT_FACTOR`: modest accelerator;
- `ALPHA_WINS_ASYMPTOTICALLY`: candidate replacement/large-cutoff engine.

### Stage14-num-α8 — Stage14-complete large-cutoff mode

Only if α7 is favorable, scale the algorithm while preserving the complete two-face census. Do not copy the optimization pattern of historical perfect-cuboid searches if it discards almost-perfect/face-cuboid cases needed by Stage14.

The goal is a substantially larger exact Stage14 cutoff than the ordinary num track can reach economically, not a raw perfect-cuboid-only search.

### Stage14-num-α9 — Optional historical-search reproduction

As an independent validation, reproduce selected published diagonal-first search intervals/results where feasible. Treat this as algorithm validation only. Historical incomplete almost-perfect lists are not imported as Stage14 census data.

### Stage14-num-α10+ — Conditional continuation

Continue only if the engine demonstrates either a meaningful performance gain or an independent structural diagnostic unavailable to ordinary num.

If the approach loses decisively after exact overlap validation, freeze the negative result and stop rather than maintaining two expensive enumerators.

## Acceptance contract

num-α is considered successful as an algorithmic experiment only if all of the following hold:

```text
EXACT_OVERLAP_WITH_MAIN_NUM=true
TWO_FACE_ENUMERATION_COMPLETE=true
PRIMITIVE_SEMANTICS_IDENTICAL=true
PHYSICAL_HEIGHT_SEMANTICS_IDENTICAL=true
NO_HISTORICAL_INCOMPLETE_FACE_LIST_USED_AS_CENSUS=true
```

Performance success is separate:

```text
MEANINGFUL_SPEEDUP_PROVED=false
LARGER_EXACT_STAGE14_CUTOFF_REACHED=false
```

until measured.

## Immediate next task

Start **Stage14-num-α1**. Reconstruct the diagonal-first algorithm and prove the exact Stage14 dictionary before writing an optimized search. The central question is whether compatible representations of one `d^2` can enumerate the full Stage14 two-face population without losing or duplicating objects.