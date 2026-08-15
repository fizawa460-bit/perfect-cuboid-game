# Stage25 checkpoint60 continuation policy

STATUS=NORMATIVE_FOR_STAGE25_60_CONTINUATION

Checkpoint60 is iterative. Audit PASS certifies only the submitted theorem package; checkpoint60 closes only when the deep-stop rule is separately satisfied.

## Persistent route IDs

```text
R501=Meskhishvili_first_parametrization
R502=Meskhishvili_third_parametrization
R503=Yoshida_varying_fiber
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
ROUTE_ID_IS_PERSISTENT=true
AUDIT_ROUND_IS_NOT_ROUTE_ID=true
CHECKPOINT_NUMBER_DOES_NOT_RENUMBER_EXISTING_ROUTE=true
R501_R507_ALLOCATIONS_FROZEN=true
```

A genuinely new route gets the next unused ID; a refinement keeps its existing ID.

## Deep-stop rule

Checkpoint60 may advance to70 only when:

- every assigned route is proved, closed with a certificate, or reduced to an exact external/new-parametric theorem gate;
- no repo-native mutation compatible with Stage14/15 reopen conditions remains unexecuted;
- theorem-changing route boundaries have fresh hostile audit;
- Stage23/24/25 envelopes and backflow remain synchronized;
- any remaining OPEN item names the genuinely new mathematical object/input required.

## Audited history entering this repair

```text
R501=PROVED_AUDITED_Theta_B_QUARTER
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504_ORIGINAL_BASE=ORIGINAL_SURFACE_SECTION_ROUTE_CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R507=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
```

The hostile audit on PR #990 also accepted the R505 exact target receiver, the Stage15 reuse chain, and the R506 toric subsumption. Those mathematics are not reopened in this repair.

## Previous FAIL and exact repair scope

The prior #990 hostile audit failed only because:

1. the mandatory reuse/discovery handoff fields were not materialized;
2. R504's low-degree base-change, multisection, and growing-multiple residual lanes were moved to an external gate without concrete candidate execution.

The repair therefore does not revisit R505/R506 mathematics.

## R504 repair now submitted

### Base change / multisection

The surface is explicitly the product-type Kummer `Km(E0xE0)` with `E0:y^2=x^3-4x` in the present fibration. Rational finite base change plus a new section is exactly equivalent to a rational multisection of the original surface.

Concrete candidates executed:

```text
BC0=twist-killing cover s^2=k^4+1 -> CLOSED_NO_QUARTER_UPGRADE
BC1=k=u^2 -> pullback MW rank1 -> CLOSED_NO_RANK_JUMP
BC2=k=(u^2-1)/(2u) -> pullback MW rank1 -> CLOSED_NO_RANK_JUMP
```

For a general degree-two map `phi`, the pullback twist cover has genus at most3. A new independent section requires an additional `E0`-isogeny factor in `J(C_phi)`. Thus the residual is now an exact new-object gate rather than an unsearched generic mechanism:

```text
R504_DEGREE2_GENERAL_GATE=EXTRA_E0_FACTOR_IN_JACOBIAN_OF_C_phi_PLUS_STAGE19_HEIGHT_ADAPTER
R504_LOW_DEGREE_BASE_CHANGE_RESIDUAL=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE
R504_MULTISECTION_RESIDUAL=SAME_GATE_AS_RATIONAL_BASE_CHANGE
```

### Growing multiples

The existing rank-one graph lattice descends to Lattes maps of degree `n^2`. Exact physical-face ratios imply `h(t)<=0.5 log(2B)`. Canonical quotient height and Northcott then give

\[
N_{R504,all\ multiples}(B)\ll B^{1/9}\sqrt{\log B}=o(B^{1/4}).
\]

Therefore

```text
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE
```

A new rational multisection outside the multiplication graph lattice is not included in this closure; it is precisely the residual base-change/new-curve gate.

## Reuse handoff repair

`r505-r506-discovery-ledger.md` now explicitly materializes all mandatory fields:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=...
REUSED_RESULTS=...
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=...
POPULATION_ADAPTERS_PROVED=...
DISCOVERY_LEDGER_STATUS=COMPLETE_REPAIRED_FOR_FRESH_AUDIT
```

The ledger includes the Stage14/15 deep-review chain and concrete primary sources for Kummer/K3 base-change and multisection mechanisms.

## Current submission state

```text
R504_BC0=CLOSED_NO_QUARTER_UPGRADE_CANDIDATE
R504_BC1=CLOSED_NO_RANK_JUMP_CANDIDATE
R504_BC2=CLOSED_NO_RANK_JUMP_CANDIDATE
R504_GROWING_MULTIPLES=CLOSED_NO_QUARTER_UPGRADE_CANDIDATE
R504_RESIDUAL=EXTERNAL_OR_NEW_EXPLICIT_CURVE_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505=PREVIOUS_HOSTILE_AUDIT_MATH_ACCEPTED
R506=PREVIOUS_HOSTILE_AUDIT_MATH_ACCEPTED
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
DEEP_STOP_PENDING_HOSTILE_AUDIT=true
CHECKPOINT60_CLOSED=false
STAGE70_ALLOWED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
```

If hostile audit accepts the concrete R504 certificates and the repaired handoff, it may set `CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=true` and permit checkpoint70. If it rejects one certificate, only that sublane returns to LIVE; R505/R506 and prior audited results remain frozen.
