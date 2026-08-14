# Stage20-40 — strongest certified upper-bound ledger

EVIDENCE_LEVEL=PROVED
CHECKPOINT=40
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## Strongest certified upper bound
Stage20 is exactly the primitive/canonical Euler-brick population counted in the audited Stage14-e8 Euclidean-height theorem: 0<a<b<c, gcd(a,b,c)=1, all three face diagonals integral, and R=sqrt(a^2+b^2+c^2)<=B, with no integral-space-diagonal requirement.

Stage14-e8 proves, by projecting to the Pythagorean triple on the two largest edges and bounding the remaining completion multiplicity by tau(b^2), that

M_3(B) << B log B * exp(O(log B/log log B)) = B^(1+o(1)).

Equivalently, for every fixed epsilon>0,

M_3(B)=O_epsilon(B^(1+epsilon)).

This strictly improves the ambient cubic bound M_3(B)<=U(B)=O(B^3).

## Additional audited upper information
Stage14-e10 also gives an independent thin-cover logarithmic saving relative to the two-face B(log B)^5 host, but the divisor-envelope bound B^(1+o(1)) is polynomially stronger and is therefore the Stage20 checkpoint40 headline upper bound.

STRONGEST_CERTIFIED_PROJECT_BOUND=M_3(B)=B^(1+o(1))
FOR_ALL_EPSILON=M_3(B)=O_epsilon(B^(1+epsilon))
UPPER_BOUND_PROVENANCE=Stage14-e8
STRICTLY_BETTER_THAN_AMBIENT_CUBIC=true
TRUE_UPPER_EXPONENT_IDENTIFIED=false
SHARPNESS_PROVED=false
MATCHING_LOWER_BOUND_PROVED=false
OPEN_GATE=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED

The polynomial upper exponent ceiling is one, but this does not prove M_3(B)=B^(1+o(1)) as a two-sided order statement. A lower bound must be handled separately at checkpoint50.

## Boundary
The checkpoint30 population-growth OPEN_GATE remains open. The conditional M_3(B)/M_2(B) transition belongs to Stage26. No integral-space-diagonal condition is imposed and no perfect-cuboid conclusion is made.

NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage20-audit
CODEX_REQUIRED=false
