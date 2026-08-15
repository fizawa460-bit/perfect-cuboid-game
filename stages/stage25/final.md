# Stage25 final self-contained interface bundle — R01

```text
BUNDLE_ID=STAGE25-FINAL-SELF-CONTAINED-20260816-R01
STATUS=CANDIDATE_PENDING_FRESH_AUDIT
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
SELF_CONTAINMENT=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
STAGE=Stage25
TRANSITION=Stage16 -> Stage19
```

## Executive theorem

Let `M1(B)` be the primitive canonical Stage16 population with exactly one integral face diagonal and no condition on the space diagonal, under `R=sqrt(a^2+b^2+c^2)<=B`. Let `N2(B)` be the primitive canonical Stage19 population with exactly two integral face diagonals and integral `R`, under the same cutoff.

The final Stage25 theorem stack is

\[
\boxed{M_1(B)\sim \frac{3}{4\pi^2}B^2\log B},
\]

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}},
\]

and therefore

\[
\boxed{B^{-7/4}(\log B)^{-1}\ll N_2(B)/M_1(B)
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}}.
\]

Consequently

\[
\boxed{N_2(B)/M_1(B)\to0},\qquad \boxed{N_2(B)\to\infty}.
\]

The final qualitative classification is

```text
STAGE25_CLASS=THIN_BUT_POSITIVE_POWER_INFINITE
GLOBAL_ZERO_DENSITY_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_LOWER_EXPONENT=1/4
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Frozen population contract

```text
CANONICAL=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
HEIGHT=R=sqrt(a^2+b^2+c^2)
CUTOFF=R<=B
SOURCE_STAGE=Stage16
SOURCE_FACE_MASK=EXACTLY_ONE
SOURCE_SPACE_REQUIREMENT=NONE
TARGET_STAGE=Stage19
TARGET_FACE_MASK=EXACTLY_TWO
TARGET_SPACE_REQUIREMENT=R_IN_Z
LITERAL_SUBSET_TRANSITION=false
RATIO_SEMANTICS=MATCHED_POPULATION_SIZE_RATIO
```

Exactly-one and exactly-two masks are disjoint, so the endpoint ratio is not an objectwise survival probability.

## Frozen upstream interfaces

Stage16 supplies the exact leading source asymptotic `M1(B)~3/(4*pi^2) B^2 log B`. Stage19/Stage14 supplies the whole-population upper `N2(B)<<_epsilon B^(1/2+epsilon)`. Stage17, Stage18, Stage21, Stage22, Stage23 and Stage24 supply the audited comparison laws used in the causal cross-ratio analysis. These are imported as frozen audited interfaces; Stage25 does not re-prove their internal analytic number theory.

The only external theorem used in the Stage25 positive-power family proof is Faltings' finiteness theorem for rational points on the fixed genus-7 third-face exception curve. It is used qualitatively, not quantitatively.

## Quarter-power family theorem

For the audited R501 parametrization, reduced rational parameters `(m,n)` in a fixed open cone give primitive canonical Stage19 boxes after bounded normalization. The raw edge/space expressions are homogeneous of degree eight, the primitive gcd is uniformly bounded, and a scale-free invariant bounds parameter multiplicity. Thus parameters `m,n<=T` produce height `O(T^8)` while there are `gg T^2` coprime pairs in the cone.

The remaining third-face square condition is a fixed squarefree degree-16 hyperelliptic equation, hence genus seven. Faltings removes only finitely many rational parameter exceptions. Therefore

\[
N_{R501}(B)=\Theta(B^{1/4}).
\]

R502 independently yields another `Theta(B^(1/4))` family with audited gcd bound `2592`, confirming that primitive reduction does not hide a larger exponent in that route.

## Interaction theorem

Define

\[
F=M_2/M_1,\quad S=N_1/M_1,\quad A=N_2/M_2,\quad T=N_2/N_1.
\]

Then identically

\[
I=A/S=T/F=N_2M_1/(M_2N_1).
\]

Combining the audited adjacent-stage laws with the Stage25 lower gives

\[
I(B)\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

Thus the face/space interaction is positive divergent in exact population-ratio semantics. No probabilistic independence is inferred.

## Deep research route closure

R501 is the proved quarter-power family. R502 is independently closed at the same exponent. R503's direct generic Yoshida section route is closed and its remaining uniform varying-fiber problem is an audited external/base-change theorem gate.

R504 was pushed through original-base sections, low-degree base changes, explicit nonsplit rank jump, a second polynomial section, a full mod-2 physical-coset characterization, fixed-class height classification, and a uniform growing-lattice count. The known rank-two physical lattice contributes at most `O(B^(1/10) log B)`, hence cannot beat the global quarter-power lower. The full-split generic Prym has no generic-base-field `E0` factor; the remaining exceptional unbounded-degree Prym/E0 locus is an audited external-theorem gate.

R505 is the exact common-squarefree-core receiver `sf(A)=sf(B)` and its Stage14/15 reuse chain is accepted; remaining progress requires stronger external/common-core counting input. R506 is an exact toric/common-leg coordinate subsumption of R505, not an independent route. R507 is the audited primitive-height rigidity theorem for R501.

## Backflow and final synchronization

Checkpoint50 propagated the positive-power lower to Stage19, Stage23 and Stage24, giving the current lower ratios and positive-divergent interaction signs. Every later checkpoint60 theorem explicitly kept `GLOBAL_STAGE25_LOWER_CHANGED=false`. Therefore checkpoint70 has no new upstream theorem delta.

```text
BACKFLOW_STATUS=PASS_NO_DELTA_AFTER_CHECKPOINT50
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=true
CHECKPOINT60_CLOSED=true
```

## Open boundary

The following remain intentionally open:

- whether the true growth exponent of `N2(B)` equals `1/4`, `1/2`, or something else;
- a matching `B^(1/2)` lower bound;
- a strict whole-family upper below `B^(1/2+epsilon)`;
- exceptional rational Prym/E0 isogeny specializations of unbounded complexity;
- the R503 uniform exceptional-fiber/base-change problem;
- the R505 common-core global counting problem;
- any existence or nonexistence theorem for a perfect cuboid.

This bundle closes the bounded Stage25 research contract only after fresh checkpoint70 audit PASS and merge.

```text
AUDIT_STATUS=PENDING
STAGE_STATUS=CLOSEOUT_PENDING_FRESH_AUDIT
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
STAGE25_REENTRY_UNLOCKED=false
```
