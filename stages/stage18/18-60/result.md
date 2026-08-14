# Stage18-60 — causal decomposition

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage18 counts primitive canonical cuboids under the common cutoff `R<=B` with exactly two integral face diagonals and no space-diagonal requirement.

## 1. The exact arithmetic restriction

Any two distinct faces of a cuboid share exactly one edge. Hence every Stage18 object has a unique shared edge among its two successful faces. After relabelling the two non-shared edges as `x,y` and the shared edge as `s`, the positive part of the exactly-two condition is exactly

\[
s^2+x^2=p^2,\qquad s^2+y^2=q^2
\]

for integers `p,q`, while the remaining face satisfies

\[
x^2+y^2\notin \square.
\]

Thus the structural locus is a **double Pythagorean extension sharing one leg**. The two face conditions are coupled through `s`; they are not two disjoint random-square tests.

## 2. The theorem-scale net cost

Audited Stage18-30 gives

\[
\frac{M_2(B)}{U(B)}
\sim
\frac{36\zeta(3)C_{M_2}}{\pi}
\frac{(\log B)^5}{B^2}\to0.
\]

Therefore the full exactly-two predicate has a certified net ambient cost of two polynomial powers of `B`, with logarithmic compensation `(log B)^5`.

This theorem-scale statement does **not** factor as two independent `B^{-1}` probabilities. No independence, correlation coefficient, or product law is claimed.

## 3. What is already charged upstream

The following are common to the ambient source `U(B)` and Stage18 target and therefore are not new thinning mechanisms here:

- strict canonical ordering `0<a<b<c`;
- global primitivity `gcd(a,b,c)=1`;
- the geometric cutoff `R<=B`;
- physical-object counting rather than parametrization multiplicity.

Stage18-20 finite counts are diagnostic only and do not cause or prove the asymptotic loss.

## 4. The role of “exactly” is not overclaimed

The target also excludes the third integral face through `x^2+y^2 not square`. Stage18 has a theorem for the complete exactly-two population, but it does not by itself compare that population with an at-least-two population. Consequently this checkpoint does **not** claim that third-face exclusion is lower order or that it leaves the leading constant unchanged.

The incremental effect of imposing the second face on the Stage16 one-face population is owned by Stage22. The incremental effect of imposing the third face on Stage18 is owned by Stage26. Those transition stages may separate costs that Stage18 records here only as a net ambient law.

## 5. Causal verdict

At current certified resolution:

- the concrete arithmetic structure behind Stage18 is two Pythagorean face equations sharing one edge;
- the complete exactly-two predicate reduces the ambient cubic population to `C_M2 B(log B)^5`, hence a net two-power polynomial thinning;
- the five logarithms belong to the proved counting law and are not split into independent probabilistic factors;
- canonicalization, primitivity, and the common cutoff are not newly charged causes;
- the separate contribution of third-face exclusion is not identified here;
- no statement about integral space diagonal or perfect-cuboid existence/nonexistence is made.

```text
PRIMARY_STRUCTURE=DOUBLE_PYTHAGOREAN_FACES_SHARING_ONE_EDGE
STRUCTURAL_NORMAL_FORM=s^2+x^2=p^2 ; s^2+y^2=q^2 ; x^2+y^2 non-square
AMBIENT_ORDER=U(B) ASYM B^3
STAGE18_ORDER=M_2(B) ~ C_M2 B(log B)^5
NET_AMBIENT_SURVIVAL ~ [36 zeta(3) C_M2/pi](log B)^5/B^2
NET_POLYNOMIAL_COST=TWO_POWERS_OF_B
INDEPENDENT_PROBABILITY_FACTORIZATION=NOT_CLAIMED
CANONICALIZATION_NEW_CAUSE=false
PRIMITIVITY_NEW_CAUSE=false
CUTOFF_NEW_CAUSE=false
THIRD_FACE_EXCLUSION_LEADING_ROLE=UNRESOLVED_IN_STAGE18
STAGE16_TO_18_INCREMENTAL_CAUSE=DEFER_TO_STAGE22
STAGE18_TO_20_INCREMENTAL_CAUSE=DEFER_TO_STAGE26
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
EVIDENCE_LEVEL=DERIVED_FROM_AUDITED_STAGE18_10_20_30_40_50_AND_FROZEN_STAGE15_STAGE16
CODEX_REQUIRED=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=70
```

Checkpoint70 is the bounded maximal synthesis / intrinsic-status closeout. Fresh Stage18-audit is required before proceeding.