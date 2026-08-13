# Stage15-7c — R01 final verdict bundle and audit handoff

Base: Stage15-7a theorem-species separation and Stage15-7b population/provenance lock.

This substage materializes the first full Stage15 final candidate rather than stopping at an outline.

## 1. Artifacts created

- `stages/stage15/final.md`
  - bundle ID `STAGE15-FINAL-SELF-CONTAINED-20260813-R01`;
  - states the common physical populations and exact `R<=B` cutoff;
  - states the ambient toric asymptotic;
  - states the exact Gaussian squareclass survivor normal form;
  - states the Stage15-5 quantitative comparison theorem and its Stage14 numerator provenance;
  - states the independent Stage15-6 causal zero-density theorem and exact local density;
  - separates quantitative and causal theorem species;
  - records finite evidence, external theorem interfaces, negative knowledge, future gates, and perfect-cuboid non-claims.

- `stages/stage15/manifest-r01.md`
  - locks every load-bearing canonical dependency;
  - maps each final claim to its source;
  - lists the inherited external literature interfaces;
  - freezes forbidden theorem promotions and the declared self-containment level.

## 2. Final causal comparison verdict frozen for audit

The R01 candidate verdict is:

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]
while
\[
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
\]
by the Stage14 numerator theorem plus the Stage15 ambient denominator.

Independently, the exact condition `R in Z` is
\[
\operatorname{sf}(A)=\operatorname{sf}(B),
\]
and the same-measure split-prime parity sieve proves
\[
\frac{N_2(B)}{M_2(B)}\to0.
\]

The R01 wording explicitly says that the local squareclass sieve explains zero density but does not internally recover the half-power rate.

## 3. Required audits completed by main-batch

### theorem-species separation audit
PASS. Quantitative and causal proofs are written as separate implication chains.

### population and cutoff audit
PASS. Both numerator and denominator use primitive canonical exactly-two objects; on the survivor population `R=d`, so `R<=B` and `d<=B` coincide exactly.

### measure and quantifier audit
PASS at the synthesis level. The Stage15-6 fixed-finite-set asymptotic is stated with `S` fixed before `B->infinity`; the growing-prime step occurs only after that limit. No growing-modulus rate is claimed.

### provenance and external-theorem contract audit
PASS. The manifest separates internal geometry from the Batyrev--Tschinkel, Huang, and Browning--Loughran interfaces inherited from Stage15-2b, and separately identifies Stage14 Theorem 2.1 as the quantitative numerator source.

### no-double-charge and cross-promotion audit
PASS. The Stage14 numerator rate and Stage15-6 local sieve are not multiplied; reconstruction multiplicity and consumed Stage15-6 receivers are not reused as savings.

### self-contained bundle dependency audit
PASS as a candidate. All load-bearing symbols and theorem statements needed to understand the final verdict are stated in `final.md`; proof provenance is locked in the manifest.

### known-note versus open-gap classification
No new mathematical gap was found in this synthesis pass. The remaining uncertainty is review quality: a fresh hostile audit must test whether R01 omitted a load-bearing hypothesis or overstated self-containment. That is an audit gate, not a new mathematical route.

## 4. Stage15-7 status after three work units

The first three priority units are complete:

1. quantitative-versus-causal theorem reconciliation;
2. population/cutoff/provenance lock;
3. final causal comparison verdict, R01 bundle, and manifest.

The next controller priority is hostile-review hardening. Because the controller forbids the main operator from approving its own PR, this batch stops here rather than inventing `7d` before the fresh audit.

```text
STAGE15_7_SUBSTAGE=7c
STAGE15_7C_FINAL_BUNDLE_R01_CREATED=true
STAGE15_7C_MANIFEST_R01_CREATED=true
STAGE15_7C_FINAL_VERDICT_EXPLICIT=true
STAGE15_7C_THEOREM_SPECIES_SAFE=true
STAGE15_7C_SELF_CONTAINMENT_CANDIDATE=true
STAGE15_7C_NEW_STAGE15_6_ROUTE_OPENED=false
STAGE15_7C_INTERNAL_FINALIZATION_ROUTE_REMAINS=true
STAGE15_7C_AUDIT_REQUIRED=true
STAGE15_7C_CODEX_REQUIRED=false
STAGE15_7C_MERGE_ALLOWED=false
STAGE15_7C_EXIT=FRESH_AUDIT_OF_R01_FINAL_BUNDLE_AND_PROVENANCE_LOCK
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-7c
NEXT_GATE=FRESH_AUDIT_OF_R01_FINAL_BUNDLE_AND_PROVENANCE_LOCK
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
```
