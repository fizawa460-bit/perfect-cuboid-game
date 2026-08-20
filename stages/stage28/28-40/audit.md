# Stage28-40 audit history and current re-audit status

## Current status after operator-authorized extended research

```text
CURRENT_AUDIT_STATUS=PENDING_REAUDIT_AFTER_EXTENDED_RESEARCH
PREVIOUS_AUDIT_VERDICT=PASS
PREVIOUS_AUDITED_SUBMISSION_HEAD=fbba8ace257357027a0f359cecdca81cabde89a8
PREVIOUS_AUDIT_SCOPE=original U1-U4 Stage28-40 submission only
POST_AUDIT_EXTENDED_RESEARCH_ADDED=true
PREVIOUS_PASS_APPLIES_TO_CURRENT_HEAD=false
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage28-audit
```

The PASS below remains a durable and correct audit record for its exact historical submission head. It is **not** a current-head PASS because the operator subsequently authorized materially new U5--U9 research on the same PR.

The new head adds, among other things:

- Huang arXiv:2111.01509v3 (17 Jul 2026) toric effective-equidistribution / Selberg-sieve adaptation;
- a submitted mod-`p^2` Stage19 growing-prime upper-sieve adapter;
- an effective degree-two thin-cover rematch;
- exact same-base / same-`-2K_Y` branch-class / same-K3-canonical-type comparison;
- a perfect-cuboid endpoint-circularity firewall for direct joint counts;
- a full terminal StructureRadar Arsenal rematch.

These additions require a fresh independent audit. No prior mathematical PASS is silently inherited onto the new head.

---

## Historical fresh audit — exact head `fbba8ace257357027a0f359cecdca81cabde89a8`

```text
AUDIT_VERDICT=PASS
AUDITED_PR=1276
AUDITED_SUBMISSION_HEAD=fbba8ace257357027a0f359cecdca81cabde89a8
CHECKPOINT40_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_TO_CHECKPOINT50=true
NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage28-main-batch
CI_STATUS=NOT_CONFIGURED
```

### Historical audit scope

The historical audit covered the original Stage28 checkpoint40 deep bridge-upper attack: the repository-wide/StructureRadar reuse preflight, original U1--U4 research ledger, the local-sieve comparison, the numerical upper ledger, and the first OPEN_GATE localization.

### Historical mathematical verification

The global bridge upper was correctly retained without numerical strengthening:

\[
M_3(B)/N_2(B)=o\!\left(B^{3/4}(\log B)^{5-\delta}\right),
\qquad 0<\delta<1/46.
\]

The local comparison was verified:

\[
\log(\alpha_p/\beta_p)
=-2\chi_4(p)/p+O(p^{-2}).
\]

Because `sum_p chi_4(p)/p` converges and the quadratic error is absolutely summable, the relative finite-prime local product has a positive finite limiting constant after finitely many bad primes are absorbed. The two local blocker systems therefore have equal first-order sieve dimension `2`.

The historical audit correctly refused to turn that local statement into `M3/N2=Theta(1)` or an asymptotic ordering.

```text
HISTORICAL_LOCAL_LOG_RATIO_AUDIT=PASS
HISTORICAL_SPACE_SIEVE_DIMENSION_AUDIT=PASS_2
HISTORICAL_THIRD_FACE_SIEVE_DIMENSION_AUDIT=PASS_2
HISTORICAL_LOCAL_DIMENSION_DIFFERENCE_AUDIT=PASS_0
HISTORICAL_GLOBAL_COUNT_RATIO_CONSTANT_PROVED=false
HISTORICAL_SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
```

### Historical deep-exploration verdict

The original endpoint, local-sieve, geometric-cover and direct-relative-receiver routes were sufficient for the first bounded deep-exploration submission, and the first receiver was research-request-ready at that time.

The subsequent U5--U9 work does not make that historical audit wrong; it makes it incomplete for the new head.

```text
HISTORICAL_DEEP_EXPLORATION_RULE_AUDIT=PASS
CURRENT_DEEP_EXPLORATION_REAUDIT_REQUIRED=true
PERFECT_CUBOID_CONCLUSION=NONE
```
