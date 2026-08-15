# Stage25-60 discovery ledger

```text
DISCOVERY_CHECKPOINT=Stage25-60
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,PRIMARY_LITERATURE
SEARCHED_PATHS=stages/stage25/25-50/**;stages/stage25/25-60/audit.md;stages/stage23/post-stage25-r01/result.md;stages/stage24/post-stage25-r01/result.md;stages/stage21/final.md;stages/stage22/22-controller.json;docs/stage14-15-bound-attack-map.md;docs/stage14-15-bound-deep-review-queue.md;docs/cycle-exploration-safety-protocol.md;Meskhishvili arXiv:1502.02375;Yoshida arXiv:2407.09825
SEARCH_TERMS=causal interaction;cross ratio;order of conditions;primitive gcd;R502 third parametrization;parametric height rigidity;third-face square;bounded similarity multiplicity;uniform varying-fiber height;moving elliptic surface;symmetric k;common core;common leg space
STRUCTURAL_SIGNATURES=M1~B^2logB;M2~Blog^5;N1~Blog^3;N2>>B^1/4;N2<<B^1/2+epsilon;interaction cross ratio;degree8 parametric family;genus7 third-face exception;moving elliptic fibers
DEPENDENCY_NEIGHBORS=Stage16;Stage16S;Stage17;Stage18;Stage19;Stage21;Stage22;Stage23;Stage24;Stage25-50;Stage25-60 hostile audit;Stage14/15 Q03-Q11
CANDIDATES_FOUND=R501 audited positive-power family;R502 Meskhishvili third parametrization;R503 Yoshida uniform varying-fiber height;R504 symmetric-k aggregation;R505 common squarefree-core;R506 common-leg plus space;R507 R501 primitive-height rigidity
CANDIDATES_ACCEPTED=exact causal cross-ratio I;R507 exact primitive-height rigidity;R504 generic non-torsion moving section;R502 source-level primitive-height/multiplicity/exactly-two no-upgrade certificate submitted for fresh audit
CANDIDATES_REJECTED_WITH_REASON=R503 not rejected and remains live but load-bearing uniform varying-fiber height count is not proved;R504 current certified section height too costly for exponent upgrade;R505 no closed independent dimension/height count;R506 no closed independent dimension/height count
POPULATION_ADAPTERS_PROVED=global causal ratios use audited Stage16/17/18/19 adapters;R501 primitive height bounded-factor equivalent to raw degree8 height;R502 primitive gcd <=2592, fixed canonical cone, finite genus7 third-face exceptions, and bounded parameter fiber <=8 give exact Stage19 family count Theta(B^1/4);R504 remains structural and is not promoted to a stronger global count
DISCOVERY_LEDGER_STATUS=COMPLETE_REPAIRED_R502
```

## Persistent route-name registry

```text
R501=Meskhishvili_first_positive_power_family
R502=Meskhishvili_third_parametrization_fallback
R503=Yoshida_uniform_varying_fiber_height
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
ROUTE_IDS_PERSIST_ACROSS_CHECKPOINTS=true
ROUTE_IDS_ARE_NOT_AUDIT_ROUND_NUMBERS=true
```

## Previous hostile-audit finding and repair choice

The first checkpoint60 audit accepted the causal/R501/R504 mathematics but rejected removal of R502 from the live set because only homogeneous degree eight had been checked. The audit permitted either reopening R502 or providing an R507-strength certificate.

The stronger repair option was chosen.

```text
PREVIOUS_AUDIT_VERDICT=FAIL
PREVIOUS_FAIL_SCOPE=R502_ROUTE_BOUNDARY
REPAIR_OPTION_SELECTED=R502_PRIMITIVE_HEIGHT_MULTIPLICITY_EXACTLY_TWO_CERTIFICATE
R502_ROUTE_BOUNDARY_ACCEPTED_BY_PREVIOUS_AUDIT=false
R502_REPAIR_STATUS=SUBMITTED_FOR_FRESH_AUDIT
```

## R502 — full no-upgrade certificate

Meskhishvili's third parametrization homogenizes at `t=m/n` to degree-eight integer edges/diagonals. On `7/2<t<4` it has canonical order `0<A<B<C`.

For coprime positive `m,n`, source-level valuation analysis gives

\[
g_{502}=2^{5[m,n\text{ both odd}]}3^{4[3\mid m]}\le2592.
\]

Hence primitive height satisfies

\[
D/g_{502}\ge m^8/2592,
\]

so primitive reduction cannot create a hidden lower height exponent.

The missing-face condition is a squarefree degree-16 hyperelliptic curve of genus seven, so by Faltings only finitely many rational parameters become three-face objects. The invariant `C/D` gives parameter fibers of size at most eight. Together with `gg T^2` reduced parameters at raw height `O(T^8)`, this proves the family-specific theorem

\[
\boxed{N_{R502}(B)=\Theta(B^{1/4}).}
\]

```text
R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R502_GCD_GLOBAL_BOUND=2592
R502_PARAMETER_FIBER_BOUND=8
R502_THIRD_FACE_EXCEPTION_CURVE_GENUS=7
R502_HIDDEN_GCD_EXPONENT_UPGRADE=false
R502_GLOBAL_EXPONENT_UPGRADE=false
```

This makes R502 eligible for `CLOSED_NO_UPGRADE_WITH_CERTIFICATE` only after fresh audit acceptance.

## Causal decomposition

With `F=M2/M1`, `S=N1/M1`, `A=N2/M2`, `T=N2/N1`,

\[
I=A/S=T/F=N_2M_1/(M_2N_1)
\]

and

\[
I(B)\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

The first hostile audit accepted this theorem; the R502 repair does not reopen it.

## R507 — R501 primitive-height rigidity

The accepted exact gcd remains

\[
g_{501}=2^{7[m,n\text{ both odd}]}3^{4[3\mid m]}\le10368,
\]

with

\[
N_{R501}(B)=\Theta(B^{1/4}).
\]

## R503 — Yoshida varying-fiber route

Status: `LIVE_HIGH_VALUE_EXTERNAL_THEOREM_GATE`.

A uniform varying-fiber rational-point height/count theorem in the exact Stage19 measure is still missing. Positive rank alone is insufficient, consistent with Stage14/15 Q03/Q05.

## R504 — symmetric-k aggregation

The generic non-torsion moving section remains accepted. Current certified height growth does not beat `1/4`, so R504 stays live for further mutation rather than being falsely closed.

## R505 / R506

Both remain live structural receivers. Neither currently has a certified independent parameter dimension plus physical-height estimate sufficient for a stronger polynomial lower.

## Stage14/15 route audit

```text
S1415_ATTACKS_REVIEWED=Q03,Q05,Q07,Q08,Q09,Q10,Q11
S1415_Q03_RELEVANCE=MOVING_ELLIPTIC_HEIGHT_UNIFORMITY_GATE
S1415_Q05_RELEVANCE=MOVING_GENUS_ONE_GLOBAL_AGGREGATION_GATE
S1415_Q07_Q10_RELEVANCE=RECONSTRUCTION_DISPERSION_PELL_INTERNAL_ROUTES_EXHAUSTED_WITHOUT_NEW_INPUT
S1415_Q11_RELEVANCE=QUALITATIVE_LOCAL_SIEVE_NOT_A_LOWER_COUNT
```

## Continuation / stopping discipline

```text
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
LIVE_ROUTE_CANDIDATES=R503,R504,R505,R506
R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
SUBLANES_OPENED=R507
SUBLANES_REPAIRED=R502
SUBLANE_BUDGET=CONTINUE_AFTER_AUDITED_MERGE
NEXT_CHECKPOINT_AFTER_THIS_AUDIT_IF_LIVE_ROUTES_REMAIN=60
STAGE70_ALLOWED=false
```

```text
FORMULA_SUBSTITUTION_ONLY=false
FINITE_DATA_USED_AS_PROOF=false
EXPLORATION_EVIDENCE_COMPLETE=true
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_REASON=previous hostile audit failed R502 route boundary; new source-level R502 Theta(B^1/4) certificate requires fresh audit
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=REGRESSION_ONLY_NO_NEW_CENSUS
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_R502_IDENTITY_GCD_SQUAREFREE_AND_MULTIPLICITY_REGRESSION_ONLY
```
