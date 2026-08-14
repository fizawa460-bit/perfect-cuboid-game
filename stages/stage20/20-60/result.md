# Stage20-60 — causal decomposition of the Euler population

EVIDENCE_LEVEL=PROVED
CHECKPOINT=60
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## Frozen population
Stage20 counts primitive/canonical Euler cuboids

```text
0<a<b<c
gcd(a,b,c)=1
R=sqrt(a^2+b^2+c^2)<=B
all three face diagonals integral
space diagonal integrality not required
```

with count `M_3(B)`.

## Causal layer A: two-face host geometry
The natural host is the two-shared-face Pythagorean geometry used in the Stage14-e / Stage18 analysis. Choosing a shared edge `E` and the other edges `X,Y`, two face conditions are

```text
U^2=E^2+X^2
V^2=E^2+Y^2.
```

The third-face condition adds

```text
Z^2=X^2+Y^2.
```

This is not modeled as an independent random-square test.

## Causal layer B: quadratic-cover / K3 mechanism
Stage14-e8 proves that retaining the third-square equation gives a degree-two cover of the toric two-face base `Y=Bl_4(P1 x P1)` whose branch divisor has class `-2K_Y`; after normalization/minimal resolution the Euler-brick compactification is a K3 surface.

Thus the third face is a structured algebraic coupling on the two-face host, not an independent Bernoulli filter.

K3_COVER_PROVENANCE=Stage14-e8_PR_163
INDEPENDENT_THIRD_FACE_MODEL=false

## Causal layer C: local obstruction mechanism
Stage14-e10 proves exact finite-prime blocker masses for third-face completion. For odd `p`,

```text
delta_p = 2(p-chi_4(p))/(p^2+6p+1) = 2/p + O(p^-2),
```

with `delta_2=2/9`.

Every Euler brick avoids every blocker. Fixed finite prime sets have product survival law, and the resulting two-limit argument reproves zero density inside the two-face ambient population. This local sieve explains systematic rarity, but by itself does not identify the true global exponent of `M_3(B)`.

LOCAL_SIEVE_PROVENANCE=Stage14-e10_PR_184
LOCAL_BLOCKERS_EXPLAIN_RARITY=true
LOCAL_SIEVE_TRUE_EXPONENT=false

## Causal layer D: global upper mechanisms
Two distinct audited upper mechanisms must not be multiplied together as independent costs.

1. Stage14-e8 Pythagorean projection plus divisor multiplicity:

```text
M_3(B) << B log B exp(O(log B/log log B)).
```

2. Stage14-e10 degree-two thin-cover theorem:

```text
M_3(B) << B (log B)^(5-eta_EB)
```

for some fixed `eta_EB in (0,1)`.

The e10 bound is asymptotically stronger than the e8 subpower-divisor envelope. Therefore the current strongest certified Stage20 upper bound is

```text
STRONGEST_CERTIFIED_UPPER=M_3(B)<<B(log B)^(5-eta_EB)
ETA_EB_EXPLICIT=false
POLYNOMIAL_UPPER_EXPONENT_AT_MOST_ONE=true
```

This supersedes only the checkpoint40 `strongest-known` metadata. The previously audited e8 bound remains mathematically valid.

## Causal layer E: explicit survival mechanism
Checkpoint50a proves a one-parameter primitive Saunderson family. For every even `m>=10`,

```text
u=m^2-1
v=2m
w=m^2+1
A=u|4v^2-w^2|
B=v|4u^2-w^2|
C=4uvw
```

produces a distinct primitive/canonical Euler brick with `R<31m^6`.

Hence

```text
M_3(B) >> B^(1/6).
```

This gives a concrete correlated arithmetic mechanism that survives all three face-square conditions. It proves that the local/global obstructions thin the host strongly but do not annihilate it.

LOWER_MECHANISM_PROVENANCE=Stage20-50a_PR_937
POPULATION_INFINITE=true
CERTIFIED_LOWER_EXPONENT=1/6

## Current causal envelope
Combining certified lower and strongest upper information,

```text
B^(1/6) << M_3(B) << B(log B)^(5-eta_EB)
```

for some fixed `eta_EB>0`.

This does not identify a true growth exponent, a matched asymptotic, or a sharp lower exponent.

TRUE_EXPONENT_IDENTIFIED=false
ASYMPTOTIC_FORMULA_PROVED=false
LOWER_EXPONENT_SHARP=false
MATCHING_LOWER_BOUND_PROVED=false

## No double charge
The local blockers, K3 thin-cover theorem, and divisor-projection upper bound are alternative/compatible descriptions of the same third-face arithmetic. They are not multiplied as independent survival factors.

DOUBLE_CHARGE_CHECK=PASS

The conditional transition ratio `M_3(B)/M_2(B)` and any statement about independence from prior Stage18 conditions remain reserved for Stage26.

STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26
INDEPENDENT_OF_PRIOR_CONDITIONS=DEFER_STAGE26

## Numerical reuse preflight

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NONE
NUM_POPULATION_MATCH=NO_MATCH
NUM_EVIDENCE_LEVEL=NOT_APPLICABLE
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

No new computation is required for this causal synthesis.

## Boundary
No integral space diagonal is imposed. Nothing here proves or disproves a perfect cuboid.

NEXT_CHECKPOINT=70
NEXT_EXPECTED_COMMAND=Stage20-audit
CODEX_REQUIRED=false
