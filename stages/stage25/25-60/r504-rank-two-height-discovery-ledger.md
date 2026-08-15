# Stage25-60 R504 rank-two height discovery / reuse ledger

STATUS=AUDIT_FAIL_NARROW_MOD2_REPAIR_SUBMITTED
ROUTE=R504
CHECKPOINT=60
PARENT_LEDGER=stages/stage25/25-60/r504-second-section-discovery-ledger.md
AUDIT_RECORD=stages/stage25/25-60/r504-rank-two-height-hostile-audit.md
REPAIR_RECORD=stages/stage25/25-60/r504-rank-two-mod2-repair.md

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=R504_NONSPLIT_RANK_JUMP_AUDITED_PASS;R504_SECOND_SECTION_AUDITED_PASS;R504_ORIGINAL_SECTION_LATTICE;R504_GROWING_MULTIPLE_HEIGHT_CERTIFICATE;R504_SECOND_SECTION_DISCOVERY_LEDGER;PR995_HOSTILE_FAIL
REUSE_MATCH_STATUS=STRUCTURAL_CONTINUATION_NO_NEW_ROUTE_ID
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=PR995_HOSTILE_AUDIT_ACCEPTED_ROSATI_FORM_BUT_REQUIRED_EXPLICIT_MOD2_PHYSICAL_COSET_CERTIFICATE
POPULATION_ADAPTERS_PROVED=P_PLUS_2R_PREVIOUS_THETA_B_1_12_RETAINED;FIXED_CLASS_HEIGHT_FORM_ACCEPTED_CONDITIONALLY_BY_HOSTILE_AUDIT
```

## Original discovery block retained

```text
DISCOVERY_CHECKPOINT=60
SEARCHED_PATHS=R504_SECOND_SECTION_MATERIALIZATION;R504_SECTION_LATTICE;R504_NONSPLIT_RANK_JUMP;R504_BASE_CHANGE_BOUNDARY;R504_FULL_SPLIT_NORMAL_FORM
SEARCH_TERMS=RANK_TWO;HEIGHT_PAIRING;ROSATI;V4_CHARACTER;PHYSICAL_2_COVER_COSET;T_DEGREE;BOX_DEGREE;CANCELLATION
STRUCTURAL_SIGNATURES=ORTHOGONAL_E0_QUOTIENT_DIRECTIONS;DEGREE8_BASIS_NORMS;PHYSICAL_2_COVER_KUMMER_CLASS;MINIMUM_NORM5
DEPENDENCY_NEIGHBORS=PR993_RANK_JUMP;PR994_SECOND_PHYSICAL_FAMILY;R504_3P_ORIGINAL_BASE;R501_R502_GLOBAL_QUARTER_LOWER
CANDIDATES_FOUND=GENERAL_aP_PLUS_bR_HEIGHT_FORM;P_PLUS_MINUS_2R;3P;3P_PLUS_2R;GROWING_RANK_TWO_LATTICE
CANDIDATES_ACCEPTED=GENERAL_FIXED_CLASS_DEGREE_FORM_BY_HOSTILE_AUDIT;P_PLUS_2R_EXPLICIT_WITNESS
LIVE_ROUTE_CANDIDATES=GROWING_RANK_TWO_LATTICE_UNIFORM_AGGREGATION;FULL_SPLIT_PRYM_E0_ISOGENY_RESIDUAL
SUBLANES_OPEN=2
TARGETED_COMPUTATION_USED=V4_DIFFERENTIAL_CHARACTER_CHECK;Q_U_GROUP_LAW_DEGREE_REGRESSION;P_PLUS_2R_EXPLICIT_WITNESS_REUSE
FINITE_DATA_USED_AS_PROOF=false
DISCOVERY_LEDGER_STATUS=COMPLETE_FOR_THIS_THEOREM_CHUNK
```

## Hostile-audit boundary

The hostile audit accepted the Rosati cross term `0`, basis norms `8,8`, the quadratic degree formula

\[
\deg_u(x(aP+bR)/H)=8(a^2+b^2),
\]

and the conditional physical formulas

\[
\deg_u t=2(a^2+b^2),\qquad L(a,b)=4+4(a^2+b^2).
\]

It rejected only the previously unsupported assertion that physical membership in `<P,R>` is exactly `a` odd, `b` even. No earlier Stage19 theorem was reopened.

## Narrow repair discovery

The repair uses the full-rational-2-torsion Kummer map on

\[
E_H:y^2=x(x-2H)(x+2H),
\]

\[
\delta(Q)=([x],[x-2H],[x+2H]).
\]

Exact factorization gives

```text
KUMMER_P=(-1,-2,2)
KUMMER_R=(1,2,2)
```

and the physical quartic receiver gives identically

```text
KUMMER_PHYSICAL_IMAGE=(-1,-2,2)=KUMMER_P
```

with an explicit converse reconstruction from square roots of the three Kummer coordinates. Therefore the physical image is exactly `P+2E_H(Q(u))`, and homomorphy gives

```text
PHYSICAL_INTERSECTION_WITH_<P,R>=aP+bR with a odd, b even
RANK_TWO_2DESCENT_CHARACTER_CERTIFICATE=EXPLICIT
AMBIENT_2_SATURATION_ASSUMPTION_USED=false
```

The constant squareclasses `-1` and `2` are nontrivial in `Q(u)`, so the parity classes of `P` and `R` are independent. This directly answers the hostile-audit blocker rather than sampling more lattice points.

## Repaired mathematical handoff

Combining the explicit mod-2 criterion with the already accepted Rosati theorem, norm `1` is only the degenerate `+/-P` class and norm `5` is the first possible nondegenerate physical norm. The previously audited `P+2R` family attains norm `5`, `t` degree `10`, box degree `24`, and `Theta(B^(1/12))` growth.

```text
R504_PHYSICAL_COSET_A_ODD_B_EVEN=REPAIRED_WITH_KUMMER_CERTIFICATE
R504_RANK_TWO_FIXED_CLASS_HEIGHT_CLASSIFICATION=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
R504_RANK_TWO_BEST_FIXED_CLASS_EXPONENT=1/12
R504_RANK_TWO_BEST_FIXED_CLASS_ATTAINED_BY=P_PLUS_2R
R504_RANK_TWO_GROWING_LATTICE_UNIFORM_AGGREGATION_PROVED=false
R504_FULL_SPLIT_PRYM_ISOGENY_RESIDUAL=OPEN
GLOBAL_STAGE25_LOWER_CHANGED=false
```

## Boundary after repair

No claim is made about uniform summation over coefficient pairs `(a,b)` growing with `B`, exact total Mordell-Weil rank, or the non-bielliptic Prym / `E0`-isogeny residual. Those remain the next repo-native checkpoint60 work after a fresh hostile audit of this narrow repair.
