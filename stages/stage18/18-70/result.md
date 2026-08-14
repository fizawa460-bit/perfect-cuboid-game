# Stage18-70 bounded maximal synthesis and closeout candidate

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage18 counts primitive canonical cuboids
\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]
with exactly two integral face diagonals and no requirement that the space diagonal be integral. Write this count as \(M_2(B)\).

## Executive synthesis

The frozen Stage15 target theorem, transferred through the audited Stage18 population contract, is
\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5},\qquad C_{M_2}>0.
\]
The matched ambient primitive/canonical count from Stage16 is
\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]
Hence
\[
\boxed{\frac{M_2(B)}{U(B)}\sim\frac{36\zeta(3)C_{M_2}}{\pi}\frac{(\log B)^5}{B^2}\to0}.
\]
The upper and lower ledgers are order-sharp:
\[
M_2(B)\ll B(\log B)^5,\qquad M_2(B)\gg B(\log B)^5.
\]
In particular, \(M_2(B)\to\infty\), so there are infinitely many primitive canonical exactly-two-face cuboids under this population definition.

The checkpoint60 causal normal form is a coupled double-Pythagorean locus. The two successful faces share a unique edge \(s\); after naming the other two edges \(x,y\),
\[
s^2+x^2=p^2,\qquad s^2+y^2=q^2,
\]
and exactly-two additionally requires
\[
x^2+y^2\notin\square.
\]
This explains the arithmetic structure but does not factor the net thinning into independent probabilities.

## Bounded synthesis

The absolute Stage18 population law is settled at full asymptotic resolution supplied by the frozen theorem: polynomial exponent \(1\), logarithmic power \(5\), and positive leading constant \(C_{M_2}\). Relative to the ambient cubic population, the complete exactly-two predicate has a certified net two-power polynomial cost with logarithmic compensation \((\log B)^5\).

That net cost is not decomposed further inside Stage18. Stage18 does not prove that excluding the third integral face is lower order, does not compare exactly-two with at-least-two, and does not identify a separate leading contribution for the negative third-face condition. Those questions require Stage20/26 or a new comparison theorem.

Likewise, Stage18 does not consume the Stage16-to-Stage18 conditional transition. The ratio and causal interpretation of adding the second face to the one-face population belong to Stage22. No space-diagonal condition is imposed here, so Stage19 and Stage24 remain separate receivers.

The finite census at \(B=50,100,200,400,800,1200,1600,2000\) with counts \(16,56,172,494,1347,2350,3536,4812\) remains COMPUTED evidence only. It is consistent with the theorem but is not used to prove it.

## Required Stage70 fields

```text
KNOWN_RESULTS=M_2(B)~C_M2 B(log B)^5 with C_M2>0; M_2/U~[36 zeta(3) C_M2/pi](log B)^5/B^2->0; order-sharp upper/lower ledgers; audited finite census; double-Pythagorean shared-edge causal normal form
ADDITIONAL_DEDUCTIONS=M_2(B)->infinity, hence infinitely many primitive canonical exactly-two-face cuboids; absolute polynomial exponent 1 and logarithmic power 5 are certified at asymptotic resolution; ambient net polynomial cost is two powers of B
CAUSAL_SYNTHESIS=two successful Pythagorean faces share one edge and are coupled through that edge; canonicalization, primitivity, R<=B and physical-object counting are already charged in the source; no independent-probability factorization
LOWER_STAGE_REINTERPRETATIONS=none of Stage16, Stage16S or Stage17 is reopened; Stage15 supplies the literal target theorem and Stage16 supplies the literal ambient source law; Stage16->18 remains Stage22
REFINEMENT_CANDIDATES=separate positive double-Pythagorean locus from third-face exclusion; compare exactly-two with at-least-two after Stage20; seek an explicit order-sharp parametric subfamily only if useful downstream
NEW_HEURISTICS=NONE_REQUIRED_FOR_CLOSEOUT
OPEN_GATES=leading role of third-face exclusion unresolved; exactly-two versus at-least-two unresolved; Stage16->18 conditional thinning reserved for Stage22; Stage18->20 third-face transition reserved for Stage26; no space-diagonal or perfect-cuboid conclusion
NEXT_STAGE_QUESTIONS=Stage19 should impose integral space diagonal on the same exactly-two population; Stage22 should measure the second-face cost from Stage16; Stage26 should measure the third-face cost from Stage18; Stage28 should synthesize interactions
SYNTHESIS_STOP_REASON=further sharpening requires a new comparison theorem, Stage20/26 input, Stage22 transition work, or another stage-specific program
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

## Stage-end artifact decisions

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=Stage18 is a stable population interface expected to be reused by Stage19, Stage22, Stage26 and Stage28, and its net ambient law must remain separated from later incremental transition laws
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE; the quantitative theorem is already inherited from Stage15 and the shared-edge normal form is stage-specific, so promotion would create a duplicate source of truth
```

No new theorem, large computation, literature program, space-diagonal claim, independence claim, or perfect-cuboid conclusion is introduced at checkpoint70.

```text
CODEX_REQUIRED=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT=70
NEXT_STAGE_AFTER_PASS=Stage19
MERGE_ALLOWED=false
```
