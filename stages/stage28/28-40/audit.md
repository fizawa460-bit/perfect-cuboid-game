# Stage28-40 audit history and current re-audit status

## Current fresh re-audit — extended U1-U9 head

```text
AUDIT_VERDICT=PASS
AUDITED_PR=1276
AUDITED_SUBMISSION_HEAD=867cde75579369484c37027c44d92130c3f0e906
CHECKPOINT40_AUDIT=PASS
EXTENDED_U5_U9_AUDIT=PASS
HUANG_V3_SOURCE_AUDIT=PASS
HUANG_MOD_P2_ADAPTER_AUDIT=PASS
HUANG_EXPONENT_SUBSTITUTION_AUDIT=PASS_44_PLUS_EPSILON
HUANG_GROWING_PRIME_UPPER_SIEVE_AUDIT=PASS
HUANG_THIN_COVER_THEOREM_SPECIES_AUDIT=PASS
COARSE_TWO_COVER_GEOMETRY_AUDIT=PASS_AS_REUSED_INTERFACE
ENDPOINT_CIRCULARITY_FIREWALL_AUDIT=PASS
STRUCTURE_RADAR_REMATCH_AUDIT=PASS
DEEP_EXPLORATION_RULE_AUDIT=PASS
OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_TO_CHECKPOINT50=true
NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage28-main-batch
CI_STATUS=NOT_CONFIGURED
PERFECT_CUBOID_CONCLUSION=NONE
```

The extended checkpoint40 research was independently re-audited on the current mathematical submission head. The earlier PASS remains historical provenance for the original U1-U4 head; this section is the authoritative current-head verdict.

### Huang v3 verification

The cited source is genuinely the substantially revised 17 Jul 2026 `arXiv:2111.01509v3`. Its Theorem 3.11 / Corollary 3.13 give a Selberg-sieve upper bound under condition `(EE)` with a uniform covering exponent `n0`, and Corollary 6.2 gives for a smooth proper split toric variety

\[
\gamma=\dim X+\operatorname{rank}\operatorname{Pic}(X)+\varepsilon,
\qquad
h(B)=(\log B)^{-1/2+\varepsilon}.
\]

For the audited Stage18 toric host `Y=Bl_4(P1xP1)`, `dim Y=2`, `rank Pic(Y)=6`. With the submitted mod-`p^2` truncated bad condition, `n0=2`, so the Corollary 3.13 error exponent is

\[
2n_0(\gamma+\dim Y+1)=4(8+2+1)+O(\varepsilon)=44+O(\varepsilon),
\]

exactly as used in the adapter.

The truncated event

\[
\{v_p(A)=1,v_p(B_0)=0\}\cup\{v_p(B_0)=1,v_p(A)=0\}
\]

is detected modulo `p^2`, is contained in the genuine Stage19 parity obstruction, and differs from the full good-split-prime parity mismatch only by valuation-`>=2` tails of `O(p^-2)` on the previously audited reduced toric open. Hence its rejection mass remains

\[
4/p+O(p^{-2})
\]

on split primes and gives sieve dimension `2`. Therefore `G(N)\gg(\log N)^2`; choosing `N=(\log B)^\lambda` with `0<\lambda<1/88` makes the polynomial error negligible and yields the valid derived upper-sieve interface

\[
N_2(B)\ll B(\log B)^5/(\log\log B)^2.
\]

This result is correctly classified as structural rather than a new strongest endpoint upper, since the already certified `N2(B)<<_epsilon B^(1/2+epsilon)` is much stronger.

Huang Theorem 1.6(1) also genuinely supplies an effective positive logarithmic thinning for adelic images of generically finite covers of degree greater than one. Its use here is only theorem-species level for the two degree-two completion covers; no ordering of the cover-dependent saving constants is claimed.

### Extended obstruction-map verification

The reused same-base/same-degree/same-branch-class/same-K3-type statements are treated only as coarse geometric invariants and do not claim equality or birational equivalence of the actual branch divisors. The direct product of the two completion indicators would count the deferred three-face-plus-space endpoint after the exact adapters, so the new endpoint-circularity firewall is correct: Stage28 may compare marginals or centered correlation information but may not consume an endpoint asymptotic/existence theorem.

The terminal StructureRadar rematch does not promote any ACTIVE card into a theorem it does not contain. `SR-STR-169` remains an external same-measure correlation receiver. The resulting current gate

```text
OPEN_GATE_40=GLOBAL_TWO_MARGINAL_RELATIVE_COMPLETION_THEOREM
RECEIVER_MUST_AVOID_DIRECT_ENDPOINT_COUNT=true
```

is narrower than the old gate and is research-request-ready.

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
HISTORICAL_DEEP_EXPLORATION_RULE_AUDIT=PASS
PERFECT_CUBOID_CONCLUSION=NONE
```
