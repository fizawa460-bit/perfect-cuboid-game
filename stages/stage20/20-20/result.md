# Stage20-20 finite Euler-cuboid baseline

EVIDENCE_LEVEL=COMPUTED
CHECKPOINT=20
STATUS=COMPUTED_CANDIDATE_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage20-10

Under the audited Stage20 contract, deterministic enumeration gives M3(B):

B=50: 0
B=100: 0
B=200: 0
B=400: 1
B=800: 3
B=1200: 5
B=1600: 5
B=2000: 7

The first primitive/canonical record is (44,117,240), with R^2=73225. Stage20 does not require R to be integral.

The committed enumerator builds Pythagorean adjacency, combines partners sharing an edge, canonicalizes to 0<a<b<c, enforces global gcd=1 and R<=B, and finally requires all three face sums to be squares. Canonical triples are deduplicated.

An independent direct small-cutoff enumeration is included for exact set comparison at B=400. The frozen table can also be regenerated and compared exactly.

These are exact finite counts only. They do not prove an asymptotic, growth exponent, density, or Stage18-to-20 thinning law. Those questions remain for checkpoints30+ and Stage26.

FINITE_DATA_BASELINE=COMPUTED
ASYMPTOTIC_INFERENCE_FROM_TABLE=NONE
NEXT_CHECKPOINT=30
NEXT_EXPECTED_COMMAND=Stage20-audit
CODEX_REQUIRED=false
