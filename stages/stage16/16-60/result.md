# Stage16-60 — causal decomposition

Status: **SUBMITTED_FOR_FRESH_AUDIT**

The audited Stage16 theorem is

\[
M_1(B)\asymp B^2\log B,
\qquad
U(B)\asymp B^3,
\qquad
M_1(B)/U(B)\asymp \log(B)/B.
\]

The primary mechanism is the one-face Pythagorean condition. An unrestricted two-edge pair has order `B^2`; a primitive Pythagorean face with scale has host size

\[
\sum_{k\le B}P(B/k)\asymp B\sum_{k\le B}1/k\asymp B\log B,
\]

because `P(X)\asymp X`. The third edge remains free at order `B`. Thus the face condition changes the host from cubic order to `B^2 log B`. The power drop comes from the Pythagorean locus and the logarithm comes from the harmonic scale sum.

Let `H_1(B)` count primitive canonical triples under the same `R<=B` cutoff with at least one integral face. A union bound over the three face choices gives `H_1(B)\ll B^2\log B`, while audited Stage16-30 gives `M_1(B)\gg B^2\log B` and `M_1(B)<=H_1(B)`. Hence

\[
H_1(B)\asymp M_1(B)\asymp B^2\log B.
\]

So the exactly-one mask does not change the proved power/log order relative to at-least-one. This does not prove `H_1(B)-M_1(B)=o(B^2\log B)` or a limiting ratio between those two populations.

Primitivity is enforced in the sharp construction by `(z,k)=1`; the weight `phi(k)/k` still yields `sum phi(k)/k^2 \asymp log B`. Canonical ordering changes multiplicity, not the certified order. Neither is the source of the main power loss.

Stage16 imposes no integral-space-diagonal condition. AR-039 is therefore kept only as a thinner integral-space-diagonal regression subset for later Stage17/21 comparison; its `B^(1/2)` construction is not charged to the Stage16 ambient exponent. The finite directional `ab/ac/bc` imbalance is also not used as a causal input.

```text
SOURCE_ORDER=U(B) ASYM B^3
TARGET_ORDER=M_1(B) ASYM B^2 log B
THINNING_ORDER=log(B)/B
PRIMARY_CAUSE=ONE_FACE_PYTHAGOREAN_DIMENSION_DROP
LOG_SOURCE=HARMONIC_FACE_SCALE_SUM
FREE_THIRD_EDGE_FACTOR=B
EXACT_ONE_MASK_CHANGES_POWER_LOG_ORDER=false
GLOBAL_OVERLAP_LITTLE_O_PROVED=false
PRIMITIVITY_CHANGES_POWER_LOG_ORDER=false
CANONICALIZATION_CHANGES_POWER_LOG_ORDER=false
SPACE_DIAGONAL_CHARGED=false
AR039_ROLE=REGRESSION_SUBSET_FOR_FUTURE_STAGE17_21
DIRECTIONAL_LAW_PROVED=false
```

Checkpoint 60 adds only the derived at-least-one comparison and the causal synthesis of already-audited counting results. Checkpoint 70 remains the intrinsic-status / closeout verdict and requires fresh audit first.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=60
CHECKPOINTS_ATTEMPTED=60
CHECKPOINTS_SUBMITTED=60
NEW_CLAIMS=derived H_1(B) ASYM B^2 log B plus causal decomposition; no stronger M_1 theorem
REUSED_WEAPONS=AR-001,AR-002,AR-039(regression only)
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 60 is a compact synthesis from audited counting ledgers.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
```
