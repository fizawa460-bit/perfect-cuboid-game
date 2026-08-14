# Stage14-num-M2 roadmap

STATUS=READY
TRACK_ROLE=AMBIENT_EXACTLY_TWO_NUMERICAL_OBSERVATORY
OWNER_USE=Stage24 primary matched finite denominator; Stage22/26/28 reusable
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false

## Mathematical contract

For each cutoff B, count primitive canonical triples

- 0<a<b<c,
- gcd(a,b,c)=1,
- R=sqrt(a^2+b^2+c^2)<=B,
- exactly two of a^2+b^2, a^2+c^2, b^2+c^2 are squares.

Define

- M2(B): all such triples, with no space-diagonal integrality requirement;
- N2(B): the same triples with R integral.

Thus N2(B) is obtained from exactly the same generated M2 population by the final predicate `is_square(R2)`, and Stage24 gets a literal matched survivor ratio N2(B)/M2(B).

## Existing exact engine

Do not start from zero. `stages/stage15/scripts/paired_enumerator.py` is already an audited exact shared-edge two-Pythagorean enumerator. It generates Stage18-style M2 first and records `space_integral` on the same object. `stages/stage15/replay/validate_paired_enumerator.py` already proves small brute-force equality and Stage14 N2 regression.

The new lane therefore owns scaling/engineering, not a new population definition.

## Route

### num-M2-0 bootstrap
- prove the Stage15 paired enumerator is exactly the Stage14-num-M2 population;
- reproduce frozen Stage18 M2(2000)=4812;
- reproduce frozen Stage14/Stage19 N2(100000)=89;
- profile the existing unchunked engine at B=200000;
- freeze operation/memory/runtime observations as engineering data only.

### num-M2-1 scalable architecture
- remove the global all-object memory bottleneck;
- partition generation by shared-edge/residue/chunk with exact canonical dedup;
- emit exact per-chunk keys or cryptographic locks sufficient for exact disjoint-union verification;
- preserve exact-two/triple separation and `space_integral` classification;
- require bit-for-bit/count equality with the unchunked engine on overlapping cutoffs.

### num-M2-2 scale panel
Target only after num-M2-1 regression succeeds:

200k -> 500k -> 1m -> 2m -> 5m -> 10m

At each cutoff freeze:

- M2(B), N2(B), N2/M2;
- M2 and N2 direction counts a,b,c;
- triples separately;
- object/count/hash regression locks where practical;
- runtime/workload diagnostics.

Larger cutoffs are conditional on measured resource use. Do not assume 500m is feasible for the ambient M2 population.

## Safety

- Stage14 integral-space `N2` census is not the ambient `M2` denominator.
- Finite ratio fits are not asymptotic laws.
- Finite T=0 is not perfect-cuboid nonexistence.
- Do not import alpha diagonal-first pruning that presupposes integral space diagonal into M2 generation.
- Any new pruning must be proved safe for all primitive canonical exactly-two objects before use.

## Codex engineering handoff

CODEX_RECOMMENDED=true
CODEX_SCOPE=NUM_M2_1_SCALABLE_ARCHITECTURE_AFTER_BOOTSTRAP
CODEX_MUST_PRESERVE_POPULATION_CONTRACT=true
CODEX_MUST_REGRESS_AGAINST_STAGE15_PAIRED_ENUMERATOR=true
CODEX_MAY_OPTIMIZE=chunking,indexing,streaming,dedup,parallelism,serialization,CI
CODEX_MAY_NOT_CHANGE=population,cutoff,primitivity,canonicalization,exactly-two mask,space predicate

NEXT=Stage14-num-M2-0
