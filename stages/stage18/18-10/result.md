# Stage18-10 — population contract

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage18 counts primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\]

under the common geometric cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B,
\]

with **exactly two** integral face diagonals. If `F_ab,F_ac,F_bc` denote the three face-square predicates, define

\[
\mathcal B_2(B)=\{(a,b,c):R\le B,\ 1_{F_{ab}}+1_{F_{ac}}+1_{F_{bc}}=2\},
\qquad M_2(B)=\#\mathcal B_2(B).
\]

Stage18 imposes **no** condition `R in Z`. Integral-space-diagonal objects may occur inside Stage18, but that extra condition belongs to Stage19. Exactly-three-face objects belong to Stage20 and are excluded here.

## Frozen Stage15 identity interface

Stage15's ambient denominator `B_2(B)` / `M_2(B)` uses the literal same physical objects, primitive/canonical convention, exactly-two predicate and `R<=B` cutoff. Hence Stage18 target = Stage15 ambient `B_2(B)` as a set.

```text
UPSTREAM_STAGE=Stage15
UPSTREAM_OBJECT=ambient exactly-two population B_2(B)
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
IDENTITY=Stage18 target = Stage15 B_2(B)
```

Stage15 also proves `M_2(B) ~ C_{M_2} B(log B)^5`, `C_{M_2}>0`; checkpoint10 records this only as frozen provenance for later checkpoints. It does not pre-certify Stage18-30/40/50 before this contract is audited.

The Stage16 -> Stage18 thinning comparison belongs formally to Stage22. No ratio, causal, independence, finite-data, or perfect-cuboid conclusion is made here.

```text
EVIDENCE_LEVEL=PROVED
PARENT_STAGE=Stage18
PARENT_CLASS=population_state
TARGET_POPULATION=B_2(B)
COUNT=M_2(B)
SPACE_DIAGONAL_REQUIRED=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=20
CODEX_REQUIRED=false
CODEX_REASON=Exact population/interface freeze; no implementation task is required.
```