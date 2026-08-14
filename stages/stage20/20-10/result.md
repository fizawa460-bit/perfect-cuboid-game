# Stage20-10 — Euler-cuboid population contract

EVIDENCE_LEVEL=PROVED
CHECKPOINT=10
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## Population
For B>0 let E(B) be the primitive/canonical Euler-cuboid population

E(B) = {(a,b,c): 0<a<b<c, gcd(a,b,c)=1, R=sqrt(a^2+b^2+c^2)<=B, and all three face diagonals are integral}.

Equivalently all of a^2+b^2, a^2+c^2, b^2+c^2 are perfect squares. No integrality condition is imposed on the space diagonal R. Define

M_3(B)=#E(B).

## Common roadmap contract
POPULATION_STATE=THREE_INTEGER_FACE_DIAGONALS
PRIMITIVE=true
CANONICAL_ORDER=0<a<b<c
SYMMETRY_REMOVAL=canonical_order
COMMON_CUTOFF=R<=B
FACE_MULTIPLICITY=exactly_three
SPACE_DIAGONAL_REQUIRED=false
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false

Because all three faces are integral, `exactly three` and `at least three` coincide. Stage20 is therefore the primitive/canonical Euler-cuboid state under the same R-cutoff used by Stages16-19.

## Boundary
Stage20 does not impose R in Z. Adding an integral space diagonal would be the deferred perfect-cuboid endpoint and is not part of Stage20.

Existing Euler-cuboid literature, constructions and finite data may be reused at later checkpoints only after adaptation to this population/cutoff contract. An infinite family is not automatically a matched asymptotic lower bound.

NEXT_CHECKPOINT=20
NEXT_EXPECTED_COMMAND=Stage20-audit
CODEX_REQUIRED=false
