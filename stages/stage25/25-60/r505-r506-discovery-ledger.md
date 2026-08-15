# Stage25-60 R504-residual / R505 / R506 discovery ledger — FAIL repair

```text
DISCOVERY_CHECKPOINT=Stage25-60-R504-R505-R506-REPAIR
DEEP_RESEARCH_MODE=true
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,STAGE14_15_ATTACK_LEDGER,PRIMARY_LITERATURE
REUSED_RESULTS=docs/stage14-15-bound-deep-review-queue.md:Q04,Q05,Q06,Q07-Q11;S1415-ATTACK-0522,0544,0583,0204,0724..0784;stages/stage25/25-50/discovery-ledger.md;stages/stage25/25-60/r504-section-lattice.md;stages/stage25/25-60/r504-twist-descent.md;PR#986;PR#989;PR#990-audit;Kuwata-Shioda-arXiv:math/0609473;Kumar-Kuwata-arXiv:1409.2931;Salgado-arXiv:1307.3994;Garbagnati-Salgado-arXiv:2505.15159
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=HOSTILE_AUDIT_REQUIRED_CONCRETE_R504_BASE_CHANGE_MULTISECTION_AND_GROWING_MULTIPLE_EXECUTION_BEFORE_DEEP_STOP
SEARCHED_PATHS=docs/stage16-28-reuse-preflight.md;docs/stage14-15-bound-attack-map.md;docs/stage14-15-bound-deep-review-queue.md;docs/stage14-15-bound-attack-ledger/**;stages/stage19/final.md;stages/stage25/25-50/discovery-ledger.md;stages/stage25/25-60/**;PR#986;PR#987;PR#989;PR#990;primary sources arXiv:math/0609473,1409.2931,1307.3994,2505.15159
SEARCH_TERMS=R504 symmetric k;isotrivial twist;k^4+1;Kummer E0xE0;quadratic base change;rational multisection;rank jump;degree two base change;Jacobian genus three;extra E0 factor;Lattes map;growing multiples;physical height;common squarefree core;common leg;Stage19 exactly two integral space
STRUCTURAL_SIGNATURES=Km(E0xE0);E0:y^2=x^3-4x;twist cover s^2=k^4+1;degree2 pullback cover genus3;Hom(J(C_phi),E0);rational multisection=base change;Lattes degree n^2;Stage19 sf(A)=sf(B);uv=wz;physical R=d<=B
DEPENDENCY_NEIGHBORS=Stage14-Q04;Stage15-Q05/Q06/Q07-Q11;Stage19;Stage23;Stage24;Stage25-R501..R507
CANDIDATES_FOUND=R504-BC0 twist-killing double cover;R504-BC1 k=u^2;R504-BC2 k=(u^2-1)/(2u);R504 rational-multisection equivalence;R504 graph/growing-multiple Lattes aggregation;R505 exact common-core receiver;R506 common-leg rank-one coordinates
CANDIDATES_ACCEPTED=R504 exact Kummer normal form;BC0 no new rational parameter dimension;BC1 rank remains1;BC2 rank remains1;rational base change and rational multisection are equivalent residual mechanisms;growing multiples admit O(B^(1/9)*sqrt(logB)) parameter upper;R505 exact-target identity (previous hostile audit accepted);R506 toric subsumption (previous hostile audit accepted)
CANDIDATES_REJECTED_WITH_REASON=blanket R504 external-gate claim rejected by previous audit for insufficient evidence;BC0 base genus1 and no new independent graph class;BC1 extra genus3 quotient factors j=8000 are not Q-isogenous to E0;BC2 extra quotient factors j=10976 are not Q-isogenous to E0;fixed higher multiples are Lattes maps of degree n^2 and aggregate below quarter power;R505 receiver alone is target restatement not construction;R506 apparent extra dimension collapses by uv=wz
POPULATION_ADAPTERS_PROVED=R504 physical primitive reduction preserves similarity ratios;for every physical R504 box with D<=B, ((t/k)^2,(kt)^2) are ratios of H_X+-X,H_Y+-Y and imply h(t)<=0.5log(2B);exactly-two/canonical filters only decrease the growing-multiple upper;R505 sf(A)=sf(B) is exact integral-space target under Stage19 toric population;R506 projective rank-one coordinates reconstruct the same toric ratios
DISCOVERY_LEDGER_STATUS=COMPLETE_REPAIRED_FOR_FRESH_AUDIT
```

## 1. Matching contract for reused results

```text
REUSE_POPULATION_MATCH=MIXED
REUSE_CUTOFF_MATCH=MIXED
REUSE_MULTIPLICITY_MATCH=MIXED
REUSE_MEASURE_MATCH=MIXED
REUSE_QUANTIFIER_MATCH=MIXED
```

Detailed classification:

- `PR #989 / r504-section-lattice`: exact R504 original-base population and exact Stage19 physical adapter; direct reuse `EXACT` for the rank-one and 3P claims.
- Stage14/15 `Q04`: exact/reusable Kummer and rank-one-collapse geometry, but its older population/height outputs are not direct Stage19 count theorems; `ADAPTER_REQUIRED` and used only as structural guidance.
- Stage14/15 `Q05/Q06`: exact theorem-species guidance for moving genus-one/Kummer support under physical measure; not a lower family; `ADAPTER_REQUIRED`.
- Stage15 attacks `0724..0784`: relevant common-core/physical-height chain. Previous hostile audit explicitly accepted this reuse chain for R505. It is not promoted beyond its audited population/quantifiers.
- Kummer/K3 primary literature: geometry/rank-jump mechanisms only; no direct exact Stage19 count; `ADAPTER_REQUIRED`.

Therefore `REUSE_MATCH_STATUS=MIXED` is intentional and population-aware, not a scope-name placeholder.

## 2. R504 concrete residual search

The previous hostile audit rejected a broad `no ready adapter found` claim. This repair executes named candidates.

### BC0 — twist-killing cover

`C:s^2=k^4+1 -> P1_k` is genus one, `Q`-isomorphic to `E0:y^2=x^3-4x`. It is the cover already underlying the hostile-audited twist descent. It is not a rational parameter base and exposes no independent `End_Q(E0)` class beyond the audited rank-one graph lattice.

Status: `CLOSED_NO_QUARTER_UPGRADE`.

### BC1 — `k=u^2`

The pullback twist cover is `y^2=u^8+1`. Its V4 elliptic quotients have `j=1728,8000,8000`; the two `j=8000` factors have different good-prime trace from `E0`, so no extra `Q`-isogeny factor occurs. The pullback MW rank remains one.

Status: `CLOSED_NO_RANK_JUMP`.

### BC2 — `k=(u^2-1)/(2u)`

After removing a square denominator, the cover is

`y^2=u^8-4u^6+22u^4-4u^2+1`.

The inherited quotient has `j=1728`; the other two quotients have `j=10976` and different `F_3` trace from `E0`. Again there is no extra `E0` factor, hence no rank jump.

Status: `CLOSED_NO_RANK_JUMP`.

### General degree-two residue

For a degree-two `phi`, the twist cover has genus at most three after square-denominator removal. A new section requires an extra `E0` factor in `J(C_phi)`. Thus the exact missing object is now an exceptional `phi` satisfying a concrete Jacobian-isogeny condition plus a Stage19 physical-height adapter.

This is recorded as

```text
R504_DEGREE2_GENERAL_GATE=EXTRA_E0_FACTOR_IN_JACOBIAN_OF_C_phi
R504_LOW_DEGREE_BASE_CHANGE_RESIDUAL=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE
```

not as a universal nonexistence claim.

## 3. Rational multisection is not a second independent lane

A rational base change plus a new section maps to a rational multisection of the original surface. Conversely the normalization of a rational multisection gives the base change and section. Therefore the two previous OPEN bullets are one exact mechanism.

Fixed genus `>1` multisections contribute finitely many rational points; fixed genus-one multisections contribute only polylogarithmically many bounded-height points. A new positive-power one-parameter route therefore needs a rational multisection or an independently varying curve family.

The natural `Q`-defined graph curves on `Km(E0xE0)` generated by `End_Q(E0)=Z` are the multiplication graphs and are handled by the growing-multiple certificate below. A rational multisection outside that graph lattice is genuinely new curve-class input.

## 4. Growing multiples — executed rather than parked

For the audited rank-one graph lattice, multiplication `[n]` descends through the degree-two elliptic quotient to a Lattes map of degree `n^2`. The first physical case `3P` has degree `9`, matching the explicit formula.

For a primitive physical box, exact face identities give

\[
(t/k)^2=(H_X-X)/(H_X+X),\qquad
(kt)^2=(H_Y+Y)/(H_Y-Y).
\]

Since `H_X,H_Y,|X|,|Y|<=B`, logarithmic height satisfies `h(t)<=0.5 log(2B)`. The canonical Lattes height then gives

\[
h(k)\le {\log(2B)\over 2n^2}+O(1).
\]

Counting rational `k` and using Northcott for degree-`<=2` lifts bounds the number of relevant nondegenerate multiples by `O(sqrt(log B))`. Therefore

\[
N_{R504,all\ multiples}(B)\ll B^{1/9}\sqrt{\log B}=o(B^{1/4}).
\]

Status:

```text
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE
```

This does not include a genuinely new rational multisection; that is precisely the residual gate above.

## 5. Primary-source search and rejection ledger

- Kuwata--Shioda, `arXiv:math/0609473`: explicit elliptic parameters/fibrations on `Km(E1 x E2)`. Relevant to the exact Kummer model, but no exact Stage19 physical-height population theorem.
- Kumar--Kuwata, `arXiv:1409.2931`: explicit Mordell--Weil lattices and base changes on Kummer/Inose-associated K3 surfaces, including CM/isogenous cases. Relevant candidate-generation machinery, but different fibrations/height contracts; no direct R504 population adapter.
- Salgado, `arXiv:1307.3994`: rank-jump mechanism for elliptic K3 surfaces with two elliptic fibrations. It proves existence/rank-jump statements under geometric hypotheses, not the exact bounded-height Stage19 family count required here.
- Garbagnati--Salgado, `arXiv:2505.15159`: multisection/rank-jump geometry for K3 families. Again a theorem species/candidate source, not a direct physical-height adapter for this fixed symmetric-`k` Kummer fibration.

Thus primary literature confirms that the residual mechanism is mathematically real while also making clear what new input is missing. The repair no longer uses an unsupported absence claim.

## 6. R505/R506 accepted mathematics retained

The previous hostile audit accepted:

```text
R505_EXACT_TARGET_RECEIVER_ACCEPTED=true
R506_TORIC_SUBSUMPTION_ACCEPTED=true
R505_STAGE15_REUSE_CHAIN_ACCEPTED=true
```

No R505/R506 mathematical re-opening is performed. The exact receiver remains

\[
\operatorname{sf}(A)=\operatorname{sf}(B)
\iff A=kP^2,\ B=kQ^2,
\]

and `u=mr,v=ns,w=ms,z=nr`, `uv=wz` remains an exact coordinate subsumption.

## 7. Repaired route classes submitted for hostile audit

```text
R501=PROVED_AUDITED_Theta_B_QUARTER
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504_ORIGINAL_BASE=CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R504_BC0=CLOSED_NO_QUARTER_UPGRADE
R504_BC1=CLOSED_NO_RANK_JUMP
R504_BC2=CLOSED_NO_RANK_JUMP
R504_GROWING_MULTIPLES=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE
R504_RESIDUAL=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505=EXTERNAL_THEOREM_GATE_PREVIOUS_MATH_ACCEPTED_BOUNDARY_RECHECK_ONLY
R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_PREVIOUS_MATH_ACCEPTED
R507=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
```

No new global exponent is claimed:

```text
GLOBAL_STAGE25_LOWER=N2(B)>>B^(1/4)
GLOBAL_STAGE25_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
GLOBAL_STAGE25_LOWER_CHANGED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
```

## 8. Deep-stop candidate after repair

The concrete repo-native R504 candidates requested by the hostile audit have now been executed, and growing multiples are quantitatively closed against a quarter-power upgrade. What remains in R504 is an exact new-object gate: produce an exceptional rational multisection/base change with an extra `E0` Jacobian factor and then prove the Stage19 physical-height adapter.

R505's common-core normal form has already undergone the accepted Stage15 deep chain including blind rediscovery; R506 is subsumed.

Therefore this repair again proposes, but does not self-certify,

```text
REPO_REUSE_HANDOFF_COMPLETE_CANDIDATE=true
DISCOVERY_EVIDENCE_BLOCK_COMPLETE_CANDIDATE=true
R504_RESIDUAL_ROUTE_BOUNDARY_EVIDENCE_COMPLETE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
DEEP_STOP_PENDING_HOSTILE_AUDIT=true
STAGE70_ALLOWED=false
NEXT_CHECKPOINT=60
```

A future explicit exceptional `phi`, rational multisection outside the multiplication graph lattice, or new same-measure uniform theorem reopens R504. This is a bounded research stop, not a permanent nonexistence assertion.
