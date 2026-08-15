# Stage25-60 R504 discovery ledger

```text
DISCOVERY_CHECKPOINT=Stage25-60-R504
ROUTE_ID=R504
ROUTE_ID_IS_PERSISTENT=true
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=STAGE24_QUARTIC_FAMILY,STAGE25_R501_R503,STAGE14_15_DEEP_ROUTES,PRIMARY_LITERATURE
SEARCHED_PATHS=stages/stage24/24-50/fresh-lower-surgeon.md;stages/stage24/24-50/u19-r501a-quartic-family.md;stages/stage25/25-60/deeper-lane-triage.md;stages/stage25/25-60/r503-yoshida-generic-rank-zero-gate.md;docs/stage14-15-bound-deep-review-queue.md
SEARCH_TERMS=symmetric-k;quartic;t^4+1=(k^4+1)z^2;congruent-number twist;isotrivial elliptic surface;Mordell-Weil;section height;base change;multisection
STRUCTURAL_SIGNATURES=e=2kpq;x=k^2p^2-q^2;y=k^2q^2-p^2;E_F:Y^2=X^3-4(k^4+1)^2X;3P section;degree20 physical height
DEPENDENCY_NEIGHBORS=Stage15-2;Stage18;Stage19;Stage24-50;Stage25-50;Stage25-60-R503
CANDIDATES_FOUND=original Q(k) section lattice;3P homogenized family;fixed higher multiples;base-change sections;multisections;growing-multiple aggregation
CANDIDATES_ACCEPTED=rank-one original-surface classification;3P exact gcd/height/exactly-two family theorem
CANDIDATES_REJECTED_WITH_REASON=second independent Q(k) section rejected by twist/End_Q rank-one classification;3P global exponent upgrade rejected because family growth is only Theta(B^(1/10));fixed higher multiples do not lower section degree
POPULATION_ADAPTERS_PROVED=3P physical identities exact;primitive gcd bounded;finite third-face exceptions;bounded parameter multiplicity on a fixed open physical cone
DISCOVERY_LEDGER_STATUS=COMPLETE_SUBMITTED_FOR_FRESH_AUDIT
```

## Core new route boundary

The symmetric-k surface is not an uncontrolled moving-rank surface. Its Jacobian is the quadratic twist

\[
Y^2=X^3-4(k^4+1)^2X
\]

of the constant lemniscatic curve `v^2=u^3-4u`. The twisting cover `s^2=k^4+1` is itself `Q`-birational to that same constant curve. The deck involution becomes `Q -> T-Q`, forcing the anti-invariant homomorphism coefficient to be even. Since `End_Q(E0)=Z`, the free `Q(k)` Mordell-Weil rank is one.

This closes the possibility of a second independent rational section on the original base.

## 3P quantitative certificate

For `k=u/v`, the accepted 3P section homogenizes to degree-20 integer coordinates. The exact primitive gcd is

\[
2^{7[u,v\text{ both odd}]}\le128.
\]

The missing third face is controlled by a squarefree degree-32 polynomial, hence a genus-15 hyperelliptic exception curve. The family has bounded parameter fibers and therefore

\[
N_{R504,3P}(B)=\Theta(B^{1/10}).
\]

This is a genuine infinite Stage19 family, but it is quantitatively dominated by the audited R501/R502 `B^(1/4)` families.

## Primary/external search

Primary-source search was used only to check whether an already known lower-degree or higher-rank congruent-number family immediately supersedes the repo-native section analysis. No source was found that supplies the missing Stage25 load-bearing base-change population theorem for this exact physical measure. Nearby congruent-number rank constructions exist, but they do not by themselves give the required primitive/canonical/exactly-two cuboid count.

No literature absence claim is promoted to a global theorem.

## Remaining R504 gates

```text
R504_ORIGINAL_QK_SECTION_LATTICE=CLASSIFIED_RANK_ONE
R504_3P=THETA_B_1_10
R504_FIXED_HIGHER_MULTIPLES=NO_BETTER_FIXED_SECTION_DEGREE
R504_LOW_DEGREE_BASE_CHANGE=OPEN_GATE
R504_MULTI_SECTION=OPEN_GATE
R504_GROWING_MULTIPLE_UNIFORM_AGGREGATION=OPEN_GATE
R504_GLOBAL_EXPONENT_UPGRADE_PROVED=false
```

R505 and R506 remain actionable and are not affected by a PASS or FAIL on this R504 submission.

```text
LIVE_ROUTE_CANDIDATES=R505,R506
SUBLANES_OPENED=R504_SECTION_LATTICE,R504_3P_HEIGHT
SUBLANES_REJECTED=SECOND_INDEPENDENT_QK_SECTION,3P_GLOBAL_EXPONENT_UPGRADE
SUBLANE_REJECTION_REASON=RANK_ONE_ORIGINAL_SURFACE;THETA_B_1_10_BELOW_AUDITED_QUARTER
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
FINITE_DATA_USED_AS_PROOF=false
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03
NUM_EVIDENCE_LEVEL=REGRESSION_ONLY
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_SYMBOLIC_IDENTITY_GCD_AND_SQUAREFREE_CERTIFICATE
```
