# Stage16-40 — upper-bound ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Question

Checkpoint 40 freezes the strongest certified upper bound for
\[
M_1(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B,\ \text{exactly one integral face diagonal}\}.
\]

It does not search for a stronger theorem. Stage16-30 has passed fresh audit and already proves the matching two-sided order.

## Certified upper bound

\[
\boxed{M_1(B)\ll B^2\log B.}
\]

This is sharp at the order-of-growth level because the separately audited lower bound gives
\[
M_1(B)\gg B^2\log B.
\]
Thus
\[
\boxed{M_1(B)\asymp B^2\log B.}
\]

No leading asymptotic constant is claimed.

## Upper-bound mechanism

Every exactly-one object has exactly one integral face. Write that face uniquely as
\[
(kx_0,ky_0,kh),
\]
where \((x_0,y_0,h)\) is an unordered primitive Pythagorean triangle and \(k\ge1\) is its scale. Let \(z\) be the third edge.

The cutoff gives \(kh\le B\) and \(z\le B\). If \(P(X)\) counts primitive Pythagorean face shapes with hypotenuse at most \(X\), the Euclid parametrization gives
\[
P(X)\ll X.
\]

Dropping primitivity, canonical ordering, and the exact-one postfilter only enlarges the count, so
\[
M_1(B)
 \le B\sum_{k\le B}P(B/k)
 \ll B\sum_{k\le B}\frac{B}{k}
 \ll B^2\log B.
\]

The three factors in the ledger are therefore:

1. primitive Pythagorean face shapes: \(P(B/k)\ll B/k\);
2. face scale: the harmonic sum \(\sum_{k\le B}1/k\ll\log B\);
3. the free third edge: at most \(B\) choices.

The unique integral face prevents overlap multiplicity.

## What is and is not charged

- **AR-001:** direct reuse for primitive/canonical and exactly-one conventions.
- **AR-002:** direct reuse for the unique primitive Euclid face decomposition.
- **AR-039:** not used; it is a lower-bound construction with integral space diagonal and belongs to checkpoint 50.
- Stage14 \(B^{1/2+o(1)}\) and Stage15 exactly-two bounds are not imported because their physical populations differ.
- Stage16-20 finite counts are not proof input.
- No space-diagonal integrality, direction bias, or accidental-square density is required for this upper bound.
- The same object is not charged through more than one face because exact-one gives a unique marked face.

## Capability and limitation ledger

\`\`\`text
UPPER_BOUND=M_1(B) << B^2 log B
EVIDENCE_LEVEL=PROVED_AND_FRESH_AUDITED_VIA_STAGE16_30
ORDER_SHARP=true
LEADING_CONSTANT_PROVED=false
UNIQUE_FACE_MULTIPLICITY=1
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
FINITE_DATA_USED_AS_PROOF=false
SPACE_DIAGONAL_THEOREM_IMPORTED=false
\`\`\`

Checkpoint 40 adds no stronger mathematical claim than the audited Stage16-30 theorem. It freezes the upper-bound source, legal reuse, and forbidden cross-promotions for later population comparisons.

\`\`\`text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=40
CHECKPOINTS_ATTEMPTED=40
CHECKPOINTS_SUBMITTED=40
NEW_CLAIMS=NONE; upper-bound ledger extracted from audited Stage16-30
REUSED_WEAPONS=AR-001,AR-002
CODEX_REQUIRED=false
CODEX_REASON=Repository write recovery and ledger publication only; the mathematical upper bound was already fresh-audited.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
\`\`\`
