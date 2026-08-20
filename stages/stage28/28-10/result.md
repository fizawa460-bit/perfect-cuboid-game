# Stage28-10 — Stage19 -> Stage20 bridge comparison contract

```text
TASK_ID=Stage28-10
CHECKPOINT=10
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=CONTRACT_PLUS_REUSED_AUDITED_INTERFACES
```

## 1. Canonical Stage28 question

Stage28 compares two already-established populations under the same primitive/canonical Euclidean cutoff `R<=B`:

Source — Stage19:

\[
N_2(B)=\#\{0<a<b<c,\gcd(a,b,c)=1,R\le B,\text{ exactly two integral face diagonals},R\in\mathbf Z\}.
\]

Target — Stage20:

\[
M_3(B)=\#\{0<a<b<c,\gcd(a,b,c)=1,R\le B,\text{ exactly three integral face diagonals}\}.
\]

No integral-space condition is imposed in `M3`.

```text
SOURCE_POPULATION=Stage19 N2
TARGET_POPULATION=Stage20 M3
COMMON_CUTOFF=R<=B
PRIMITIVE_CONVENTION=gcd(a,b,c)=1
CANONICAL_CONVENTION=0<a<b<c
PHYSICAL_OBJECT_MULTIPLICITY=ONE
```

## 2. The bridge is not a literal subset transition

Stage19 requires exactly two integral faces. Stage20 requires exactly three. Therefore the stage populations are disjoint by definition:

\[
\mathcal A_{19}(B)\cap\mathcal A_{20}(B)=\varnothing.
\]

Neither stage population is a subset of the other.

In particular:

- adding a third face to a Stage19 object would leave the Stage19 exactly-two stratum;
- dropping the space-integrality condition from a Stage19 object does not produce a Stage20 object;
- a Stage20 object may or may not have integral space diagonal.

Hence

```text
LITERAL_SUBSET_TRANSITION=false
SOURCE_TARGET_INTERSECTION=EMPTY_BY_EXACT_FACE_MULTIPLICITY
M3_OVER_N2_IS_SURVIVAL_PROBABILITY=false
N2_OVER_M3_IS_SURVIVAL_PROBABILITY=false
```

## 3. Exact common-host adapter

Reuse the audited Stage26 physical host

\[
H_{\ge2}(B)=M_2(B)+M_3(B),
\]

where `M2` counts primitive canonical exactly-two-face cuboids with no space requirement and `M3` counts exactly-three-face Euler cuboids. The two strata are disjoint and exhaust the at-least-two-face physical host.

Stage19 is a literal subset of the `M2` stratum:

\[
N_2(B)\subset M_2(B)\subset H_{\ge2}(B),
\]

while Stage20 is the `M3` stratum:

\[
M_3(B)\subset H_{\ge2}(B).
\]

Define the two matched host shares

\[
\Sigma_{19}(B)=\frac{N_2(B)}{H_{\ge2}(B)},
\qquad
\Phi_{20}(B)=\frac{M_3(B)}{H_{\ge2}(B)}.
\]

Both are literal proportions of the same physical host. Their ratio is exactly

\[
\boxed{
\frac{\Phi_{20}(B)}{\Sigma_{19}(B)}
=
\frac{M_3(B)}{N_2(B)}
}
\]

whenever `N2(B)>0`, which holds for all sufficiently large `B` by the certified positive-power lower bound.

This identity authorizes `M3/N2` as the primary Stage28 matched **population-size bridge ratio**. It does not turn the Stage19 -> Stage20 label into an objectwise transition.

```text
COMMON_HOST=H_GE2=M2+M3
SOURCE_HOST_SHARE=Sigma19=N2/H_GE2
TARGET_HOST_SHARE=Phi20=M3/H_GE2
PRIMARY_BRIDGE_RATIO=M3/N2=Phi20/Sigma19
PRIMARY_BRIDGE_RATIO_SEMANTICS=MATCHED_POPULATION_SIZE_RATIO
CAUSAL_SURVIVAL_SEMANTICS=false
HOST_ADAPTER_STATUS=PROVED_BY_REUSE
```

## 4. Strongest incoming theorem surfaces

Stage28 must preserve interval-valued theorem status rather than manufacture point exponents.

For Stage19, the strongest current certified corridor is

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

For Stage20, the project-wide arsenal supersedes the historical one-parameter Stage20 lower by the Stage26 generalized Saunderson theorem:

\[
\boxed{B^{1/3-\varepsilon}\ll_\varepsilon M_3(B)
\ll_\eta B(\log B)^{5-\eta}},
\qquad 0<\eta<1/46.
\]

Also

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

and Stage26 proves

\[
H_{\ge2}(B)\sim M_2(B).
\]

These are incoming interfaces only. Checkpoint10 does not claim a new ratio limit or asymptotic ordering between `N2` and `M3`.

```text
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
N2_ASYMPTOTIC_PROVED=false
M3_ASYMPTOTIC_PROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
```

## 5. Immediate logical firewalls

The current lower bounds alone do not order the populations. In particular, `M3>>B^(1/3-epsilon)` and `N2>>B^(1/4)` do not imply `M3>N2` asymptotically.

Likewise, the Stage19 upper exponent `1/2` is not a true exponent, and the Stage20 `B(log B)^(5-eta)` upper does not show that `M3` has exponent one.

The bridge therefore starts with an unresolved ordering problem.

```text
ORDERING_FROM_LOWER_BOUNDS_FORBIDDEN=true
ORDERING_FROM_UPPER_ENDPOINTS_FORBIDDEN=true
FINITE_EFFECTIVE_EXPONENT_AS_THEOREM=false
POINT_EXPONENT_PROMOTION=false
```

## 6. Perfect-cuboid endpoint firewall

Stage20 contains all primitive Euler cuboids regardless of whether the space diagonal is integral. A hypothetical perfect cuboid would therefore lie inside Stage20, but not inside Stage19 because Stage19 is the exactly-two-face stratum.

Stage28 compares population sizes; it does not isolate the three-face-plus-space intersection.

```text
PERFECT_CUBOID_POPULATION_IS_STAGE28_SOURCE=false
PERFECT_CUBOID_POPULATION_IS_STAGE28_TARGET=false
PERFECT_CUBOID_EXISTENCE_CONCLUSION=NONE
PERFECT_CUBOID_NONEXISTENCE_CONCLUSION=NONE
```

## 7. Checkpoint roadmap after contract audit

After a fresh audit accepts this comparison contract:

- checkpoint20 should build a matched finite-data baseline for `N2` and `M3` at common cutoffs only;
- checkpoint30 should derive the strongest legal bridge-ratio corridor without assuming point exponents;
- checkpoint40 should record the strongest certified upper-side implications for `M3/N2` or its host-share form;
- checkpoint50 should record the strongest certified lower-side implications;
- checkpoint60 should distinguish the third-face condition from the space-diagonal condition and prevent double charging;
- checkpoint70 should perform bounded synthesis and hand off the cross-stage interaction picture to Stage29.

The deep-exploration rule in the canonical roadmap applies before any unresolved later checkpoint is frozen as an `OPEN_GATE`.

## 8. Reuse and exit

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=Stage19 final; Stage20 final; S25-W01; AR-006; Stage26 H_ge2/S26-W01/S26-W03; Stage27 closeout theorem surface
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS_FOR_CONTRACT_INPUTS
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10
```

Checkpoint10 freezes semantics only. No new theorem branch is opened before audit.

```text
CHECKPOINT10_CONTRACT_COMPLETE=true
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=20
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage28-audit
CODEX_REQUIRED=false
```
