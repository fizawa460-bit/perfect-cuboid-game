# Stage28-40 fresh audit

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

## Audit scope

Fresh audit of the Stage28 checkpoint40 deep bridge-upper attack, including the repository-wide/StructureRadar reuse preflight, the four-route research ledger, the new local-sieve comparison, the numerical upper ledger, and the OPEN_GATE localization.

## Mathematical verification

The current global bridge upper is correctly retained without numerical strengthening:

\[
M_3(B)/N_2(B)=o\!\left(B^{3/4}(\log B)^{5-\delta}\right),\qquad 0<\delta<1/46.
\]

The new local comparison is also valid at the stated scope. On split odd primes, the Stage19 space-square acceptance has

\[
\alpha_p=1-4/p+O(p^{-2}),
\]

while on inert odd primes `alpha_p=1`. The Stage20 third-face acceptance is

\[
\beta_p=1-2/p+O(p^{-2})
\]

for every odd prime, with the exact first-order sign encoded by `chi_4`. Hence

\[
\log(\alpha_p/\beta_p)=-2\chi_4(p)/p+O(p^{-2}).
\]

Because the prime sum `sum_p chi_4(p)/p` converges and the quadratic error is absolutely summable, the relative finite-prime local product has a positive finite limiting constant after finitely many bad primes are absorbed. Equivalently, the two local blocker systems have the same first-order sieve dimension `2`: coefficient `4/p` on the density-one-half split primes versus coefficient `2/p` on all odd primes.

The submission correctly does **not** turn this local product statement into a global count-ratio theorem. Stage19 lacks the required growing-modulus uniformity on the same `z=z(B)` scale available for the Stage20 Selberg sieve. Therefore `M3/N2=Theta(1)`, an asymptotic ordering, or any new point exponent remains unproved.

```text
LOCAL_LOG_RATIO_AUDIT=PASS
SPACE_SIEVE_DIMENSION_AUDIT=PASS_2
THIRD_FACE_SIEVE_DIMENSION_AUDIT=PASS_2
LOCAL_DIMENSION_DIFFERENCE_AUDIT=PASS_0
LOCAL_PRODUCT_TO_GLOBAL_TRANSFER_AUDIT=PASS_FALSE
GLOBAL_COUNT_RATIO_CONSTANT_PROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
```

## Deep-exploration / OPEN_GATE audit

Checkpoint40 tested materially distinct endpoint, local-sieve, geometric-cover, and direct-relative-receiver routes. The surviving obstruction is sharpened to a same-host global relative-completion/correlation/height/uniformity theorem with the exact primitive/canonical physical measure and `R<=B` cutoff. That is sufficiently precise to satisfy the roadmap's research-request-ready stopping rule for this upper checkpoint.

```text
DEEP_EXPLORATION_RULE_AUDIT=PASS
OPEN_GATE_40=GLOBAL_SAME_HOST_RELATIVE_COMPLETION_THEOREM
OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS
BLIND_STAGE27_REOPEN_AUDIT=PASS_FALSE
PERFECT_CUBOID_CONCLUSION=NONE
```

The literature rematch is non-load-bearing for the new local comparison and does not promote any external paper into a stronger Stage28 theorem. No repair is required.
