# Stage25 checkpoint60 R503 hostile fresh audit

Status: **PASS — original generic-section route closed; R503 narrowed to an external/base-change theorem gate**

## Scope

This fresh audit independently attacked the R503 Yoshida varying-fiber submission in PR #986. The audit checked the exact family adapter, the external generic-rank-zero input, the two Yoshida Möbius maps, the fixed-orbit physical-height deduction, the scope of the negative conclusion, and checkpoint60 continuation discipline.

## Accepted source adapter and generic-rank obstruction

Yoshida's family is

\[
E_{1,s}:y^2=x(x-(2s)^2)(x+(s^2-1)^2).
\]

With

\[
(a,b,c)=(2s,s^2-1,s^2+1),
\]

we have the exact identity `a^2+b^2=c^2`, so this is the plus-sign Pythagorean/Frey family `y^2=x(x-a^2)(x+b^2)` used in the cited geometric Mordell-Weil calculation. The primary-source recheck confirms geometric generic rank zero for that family. Therefore the original Yoshida surface has no non-torsion generic section.

This conclusion is intentionally narrow: it does not rule out positive-rank specializations, low-degree base changes, or multisections.

## Accepted fixed-fiber height-sparsity certificate

At `s=5/3`, Yoshida's map from `alpha=x([n]P)` to the cuboid parameter is

\[
t=\frac{15(9\alpha-32)}{81\alpha+800},
\]

with a rational Möbius inverse. Hence on the fixed elliptic curve

\[
h(t_n)=h(\alpha_n)+O(1)=\Theta(n^2).
\]

The face-cuboid edge ratio

\[
\rho(t)=\frac{2t}{t^2-1}
\]

is a degree-two rational map. For a primitive integer cuboid of physical height at most `B`, the reduced edge ratio has logarithmic height at most `log B+O(1)`. Thus only

\[
O(\sqrt{\log B})
\]

indices from this explicit fixed-fiber orbit can occur below height `B`.

This is accepted only as an upper bound for Yoshida's displayed fixed-fiber orbit, not as a global Stage19 upper bound.

## Accepted displayed positive-rank-parameter sparsity

At `s=5/3`, Yoshida's displayed transformed parameter is

\[
s'=\frac{4(27\alpha+40)}{27\alpha-640},
\]

again Möbius with rational inverse. Therefore the displayed positive-rank sequence satisfies `h(s'_n)=Theta(n^2)` and contributes only `O(sqrt(log X))` displayed parameters of rational height at most `X`.

This does not imply that all positive-rank specializations are sparse.

## Route classification

The submission correctly does not declare R503 impossible. The direct generic-section route is closed, while the genuinely distinct possibilities remain open:

- low-degree base change / multisection with a non-torsion section and controlled physical height;
- a quantitative theorem giving polynomially many exceptional positive-rank fibers with uniformly small points;
- a uniform small-point count together with the exact Stage19 primitive/canonical/exactly-two adapter.

Therefore the audited route status is

`EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE`.

R504, R505 and R506 remain actionable repo-native checkpoint60 routes, so the checkpoint60 deep stop rule is not satisfied and Stage70 remains blocked.

## Discovery audit

The primary-source revalidation is sufficient for the theorem-class-changing R503 reclassification. The bounded literature search is accepted only as a bounded search outcome; no exhaustive literature nonexistence claim is made. No finite census is used as proof.

## CI

Submission-head workflow `Stage25-60 R503 Yoshida gate audit` run `31874523593` succeeded and mechanically checks the exact Pythagorean adapter, both Möbius maps, the physical edge-ratio map, marker scope, historical checkpoint60 preservation and the pending iteration-controller contract. Historical Stage25-60 causal-deep workflow run `31874523574` also succeeded.

## Verdict

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R503_FAMILY_IDENTIFICATION_ACCEPTED=true
R503_GENERIC_GEOMETRIC_MW_RANK_ACCEPTED=0
R503_GENERIC_NONTORSION_SECTION_EXISTS=false
R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED
R503_FIXED_FIBER_ORBIT_COUNT_UPPER_ACCEPTED=O(sqrt(log B))
R503_DISPLAYED_S_SEQUENCE_COUNT_UPPER_ACCEPTED=O(sqrt(log X))
R503_ROUTE_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE
R503_BASE_CHANGE_MULTISECTION_ROUTE=OPEN_GATE
R503_QUANTITATIVE_EXCEPTIONAL_FIBER_ROUTE=OPEN_GATE
R503_UNIFORM_SMALL_POINT_ROUTE=OPEN_GATE
GLOBAL_STAGE25_ENVELOPE_CHANGED=false
GLOBAL_LOWER_EXPONENT_ABOVE_QUARTER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
FINITE_DATA_USED_AS_PROOF=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #986; then Stage25-main-batch at checkpoint60
```
