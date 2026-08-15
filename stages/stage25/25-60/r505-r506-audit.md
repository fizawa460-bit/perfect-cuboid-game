# Stage25-60 R505/R506 hostile fresh audit

Status: **FAIL — R505/R506 mathematics accepted, but the deep-stop / R504-residual boundary is not sufficiently evidenced**

## Scope

This audit treats PR #990 as a fresh checkpoint60 route-boundary submission. It independently attacks:

1. the exact R505 common-squarefree-core receiver;
2. the R506 rank-one/common-leg subsumption claim;
3. reuse of the Stage14/15 deep attack chain;
4. the proposed reclassification of the remaining R504 base-change/multisection/growing-multiple lane;
5. the checkpoint60 deep-stop condition and Stage70 advance request.

## A. R505 exact target receiver — PASS

With

\[
E=4mnrs,\quad X=2rs(m^2-n^2),\quad Y=2mn(r^2-s^2),
\]

and

\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2,
\]

we have exactly

\[
E^2+X^2+Y^2=4AB.
\]

Since the physical primitive normalizer is integral, integrality of the physical space diagonal is equivalent to `AB` being a square. For positive integers `A,B`, this is equivalent to

\[
\operatorname{sf}(A)=\operatorname{sf}(B),
\]

or uniquely

\[
A=kP^2,\qquad B=kQ^2
\]

with positive squarefree `k`. The submitted verifier checks these identities on a large exact grid. This mathematical part is accepted.

## B. R506 subsumption — PASS

Set

\[
u=mr,\quad v=ns,\quad w=ms,\quad z=nr.
\]

Then

\[
uv=wz,\qquad A=u^2+v^2,\qquad B=w^2+z^2.
\]

Conversely, positive rational rank-one data `uv=wz` reconstruct the two toric projective ratios via

\[
m:n=u:z=w:v,\qquad r:s=u:w=z:v.
\]

Hence R506 is not an independent target receiver or parameter dimension; it is R505 in common-leg/rank-one coordinates. This route-subsumption certificate is accepted.

## C. Stage15 reuse for R505 — mathematically relevant, but normative handoff incomplete

The submitted discovery ledger records a substantial and relevant Stage15 chain, including the moving genus-one receiver, exact physical/product height, 2-covering/descent, fixed physical diagonal fibers, codimension-two congruence/sieve gates, blind rediscovery, channel-gcd first moment and complementary-divisor switch.

That is sufficient to accept the statement that the obvious common-core reformulations have already been attacked deeply.

However, the Stage16-28 reuse preflight requires the repository reuse handoff to materialize at every checkpoint, including:

```text
REUSED_RESULTS
REUSE_MATCH_STATUS
STRONGEST_KNOWN_CHECK
STRONGER_PRIOR_RESULT_FOUND
NEW_RESEARCH_JUSTIFIED
```

and the Stage21-28 discovery evidence requires, among the concrete evidence fields, `POPULATION_ADAPTERS_PROVED`.

PR #990's `r505-r506-discovery-ledger.md` includes `REPO_REUSE_PREFLIGHT`, `REUSE_SEARCH_SCOPE`, `SEARCHED_PATHS`, `SEARCH_TERMS`, `STRUCTURAL_SIGNATURES`, `DEPENDENCY_NEIGHBORS`, and candidate fields, but does not materialize the complete mandatory reuse handoff above and does not materialize `POPULATION_ADAPTERS_PROVED`.

This is a workflow blocker for a deep-stop claim.

## D. R504 residual external-gate classification — NOT ACCEPTED YET

The previous hostile R504 audit intentionally left these mechanisms OPEN:

1. low-degree finite base change;
2. multisection becoming a section after base change;
3. growing-multiple uniform aggregation.

PR #990 proposes to move that residual lane to `EXTERNAL_THEOREM_GATE` because a bounded repository/primary-literature search found no ready same-measure adapter.

The current evidence is not yet strong enough for that transition. The discovery ledger names only the broad surface `R504 elliptic-K3/base-change primary literature`; it does not record concrete primary sources/candidate base changes, accepted/rejected candidate instances, or a route-by-route reason why the three previously OPEN mechanisms now require genuinely new external/parametric input rather than another executable repo-native mutation.

A bounded absence search can support a narrow `NO_READY_ADAPTER_FOUND` statement, but by itself it does not certify the checkpoint60 stop-rule clause

> no unexecuted repo-native mutation of an existing normal form remains.

Therefore:

```text
R504_ORIGINAL_BASE_AUDITED_RESULT_ACCEPTED=true
R504_RESIDUAL_EXTERNAL_GATE_ACCEPTED=false
R504_LOW_DEGREE_BASE_CHANGE_ROUTE_REMAINS_OPEN=true
R504_MULTI_SECTION_ROUTE_REMAINS_OPEN=true
R504_GROWING_MULTIPLE_UNIFORM_AGGREGATION_REMAINS_OPEN=true
```

The repair may either execute/close these remaining repo-native candidates with concrete certificates, or provide a concrete search/rejection ledger sufficient to justify external/new-parametric gating.

## E. Deep-stop / Stage70 — FAIL

Because the mandatory reuse handoff is incomplete and R504 residual is not yet certified as an external/new-input gate, checkpoint60's deep-stop rule is not satisfied.

R505 and R506 do not need mathematical reopening. The global Stage25 envelope is unchanged:

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

## Verdict

```text
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=FAIL
HOSTILE_AUDIT=true
R505_EXACT_TARGET_RECEIVER_ACCEPTED=true
R506_TORIC_SUBSUMPTION_ACCEPTED=true
R505_STAGE15_REUSE_CHAIN_ACCEPTED=true
REPO_REUSE_HANDOFF_COMPLETE=false
DISCOVERY_EVIDENCE_BLOCK_COMPLETE=false
R504_RESIDUAL_EXTERNAL_GATE_ACCEPTED=false
R504_RESIDUAL_ROUTE_BOUNDARY_EVIDENCE_COMPLETE=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
GLOBAL_MATHEMATICS_REOPEN_REQUIRED=false
R505_MATHEMATICS_REOPEN_REQUIRED=false
R506_MATHEMATICS_REOPEN_REQUIRED=false
REPAIR_SCOPE=COMPLETE_REUSE_HANDOFF_AND_R504_RESIDUAL_ROUTE_BOUNDARY_EVIDENCE
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```
