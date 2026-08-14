# Stage21-20 — finite transition / control baseline

EVIDENCE_LEVEL=COMPUTED
CHECKPOINT=20
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## Reused audited finite tables
Under the common cutoff R<=B, Stage16, Stage17, and Stage16S provide independently frozen finite tables at B=50,100,200,400,800,1200,1600,2000.

Stage16 source counts M1(B):

```text
50:490
100:2620
200:12664
400:59574
800:273901
1200:662207
1600:1234822
2000:1997863
```

Stage17 target counts N1(B):

```text
50:7
100:25
200:67
400:174
800:453
1200:764
1600:1077
2000:1434
```

Stage16S space-at-least counts S_all(B):

```text
50:76
100:324
200:1320
400:5394
800:21658
1200:48921
1600:87045
2000:136060
```

## Cross-enumerator identity
Stage16S separately classifies its integral-space-diagonal population by exact face multiplicity. Its `face1` column is

```text
7,25,67,174,453,764,1077,1434
```

which agrees exactly with the Stage17 N1 column at every shared cutoff.

```text
STAGE17_VS_STAGE16S_FACE1_FINITE_MATCH=EXACT_AT_ALL_SHARED_THRESHOLDS
```

This is a strong finite population/cutoff/multiplicity regression check, not an asymptotic proof.

## Conditional survival diagnostics
The finite Stage16 -> Stage17 survivor fractions N1(B)/M1(B) decrease strongly over the frozen range. Representative values are

```text
B=50:    7/490
B=100:   25/2620
B=200:   67/12664
B=400:   174/59574
B=800:   453/273901
B=1200:  764/662207
B=1600:  1077/1234822
B=2000:  1434/1997863
```

No finite fit is promoted to a theorem. Checkpoint30 owns the exact asymptotic survivor law using the stronger E-1e source interface and Stage17 target theorem.

## Stage16S control diagnostics
The share of the integral-space population having exactly one integral face is N1(B)/S_all(B). It is finite diagnostic evidence for how exceptional face-integrality is inside the space-diagonal population. The complementary Stage16S theorem already proves that all faceful cases are lower order in S_all; checkpoint30/60 may use the theorem-level interface, not this finite table, for interaction classification.

## Boundary
This checkpoint does not claim independence, correlation, enhancement, suppression, or a limiting finite-data ratio. It introduces no new enumerator because all three audited source tables already share the required thresholds and population conventions.

```text
FINITE_DATA_USED_AS_PROOF=false
NEW_COMPUTATION_REQUIRED=false
CROSS_ENUMERATOR_MATCH=PASS
INTERACTION_CLASSIFICATION=DEFER_CHECKPOINT30_PLUS
NEXT_CHECKPOINT=30
NEXT_EXPECTED_COMMAND=Stage21-audit
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
