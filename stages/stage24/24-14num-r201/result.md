# 24-14num-r201 result

STATUS=BOOTSTRAP_COMPLETE_CI_SUCCESS
PARENT_STAGE=Stage24
PR=969
CI_RUN=31843524846
CI_CONCLUSION=SUCCESS

## Main result

The existing Stage15 paired enumerator is a valid exact numerical engine for the Stage24 literal transition `M2 -> N2`: it generates the ambient primitive canonical exactly-two population first and applies space integrality only as a final predicate on the same objects.

Therefore `N2(B)/M2(B)` below is a same-run literal survivor ratio, not a cross-population quotient.

## Exact matched locks

At `B=2000`:

- `M2=4812`;
- `M2 direction (a,b,c)=(1342,2136,1334)`;
- `N2=5`;
- `N2 direction (a,b,c)=(2,2,1)`;
- `N2/M2=0.0010390689941812137`;
- ambient three-face objects `M3=7`, integral-space triples `N3=0`.

At `B=100000`:

- `M2=796698`;
- `M2 direction (a,b,c)=(253718,339972,203008)`;
- `N2=89`;
- `N2 direction (a,b,c)=(33,33,23)`;
- `N2/M2=0.00011171108751371284`;
- ambient three-face objects `M3=60`, integral-space triples `N3=0`.

The B=100000 run also records:

- integer Pythagorean triangles with hypotenuse <= B: `161436`;
- glued pairs inside the physical R cutoff before primitive/canonical filtering: `2825200`;
- distinct primitive canonical objects with at least two faces: `796758`;
- exact-two glue multiplicity one: PASS;
- triple glue multiplicity three: PASS.

These are exact finite computation outputs from CI run `31843524846`. They are not asymptotic evidence by themselves.

## Reuse status

NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,Stage15-paired-enumerator
NUM_POPULATION_MATCH=EXACT_FOR_STAGE24_M2_AND_FINAL_SUBSET_CLASSIFICATION_FOR_N2
NUM_EVIDENCE_LEVEL=EXACT_FINITE_BOOTSTRAP
NUM_NEW_COMPUTATION_JUSTIFIED=YES_AMBIENT_M2_DENOMINATOR_NOT_AVAILABLE_IN_STAGE14_NUM

## Engineering decision

No new mathematical enumerator is needed. The bottleneck is scaling the exact shared-edge engine while preserving the same object set.

`24-14num-r202` is therefore the implementation/scaling task:

- streaming/chunked shared-edge generation;
- bounded-memory exact dedup / deterministic shard union;
- overlap equality against this r201 engine;
- then `200k -> 500k -> 1m -> 2m -> 5m -> 10m` as resources permit.

GitHub issue `#970` contains the implementation handoff and immutable acceptance gates.

ASYMPTOTIC_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
R201_CI_PASS=true
NEXT=24-14num-r202
