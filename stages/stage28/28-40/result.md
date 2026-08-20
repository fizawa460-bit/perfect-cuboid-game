# Stage28-40 — strongest upper ledger and extended deep bridge attack

```text
TASK_ID=Stage28-40
CHECKPOINT=40
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=EXTENDED_RESEARCH_SUBMITTED_PENDING_FRESH_REAUDIT
EVIDENCE_LEVEL=PROVED_REUSE_PLUS_NEW_DERIVED_COMPARISONS_PLUS_2026_LITERATURE_ADAPTATION_PENDING_AUDIT
PREVIOUS_AUDIT_HEAD=fbba8ace257357027a0f359cecdca81cabde89a8
PREVIOUS_AUDIT_VERDICT=PASS_FOR_OLD_HEAD_ONLY
PREVIOUS_AUDIT_SUPERSEDED_FOR_CURRENT_HEAD=true
```

## 1. Certified upper surface remains unchanged

The strongest **already audited** upper control on the Stage28 bridge remains

\[
\boxed{
\frac{M_3(B)}{N_2(B)}
=o\!\left(B^{3/4}(\log B)^{5-\delta}\right)
}
\qquad(0<\delta<1/46).
\]

No new whole-family endpoint theorem found in this extended batch improves that numerical corridor.

```text
CHECKPOINT40_NUMERIC_UPPER_IMPROVED=false
CURRENT_CERTIFIED_BRIDGE_UPPER=o(B^(3/4)(log B)^(5-delta)), 0<delta<1/46
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
```

## 2. First comparative certificate — equal first-order local sieve dimension

On the shared two-face local model let `alpha_p` denote the Stage19 space-square acceptance and `beta_p` the Stage20 third-face acceptance. The already-derived comparison is

\[
\log\frac{\alpha_p}{\beta_p}
=-\frac{2\chi_4(p)}p+O(p^{-2}).
\]

Since `sum_p chi_4(p)/p` converges, the relative finite local products have no polynomial or first-order logarithmic drift. Both known local blocker systems have sieve dimension `2`.

```text
SPACE_LOCAL_SIEVE_DIMENSION=2
THIRD_FACE_LOCAL_SIEVE_DIMENSION=2
FIRST_ORDER_LOCAL_DIMENSION_DIFFERENCE=0
LOCAL_FIRST_ORDER_ORDERING_MECHANISM=ABSENT
M3_OVER_N2_THETA_ONE_PROVED=false
```

## 3. New 2026 route — Huang v3 closes the theorem-species growing-prime gap on the upper-sieve side

A materially new literature input was found after the earlier StructureRadar search campaign:

```text
Zhizhong Huang
Equidistribution of rational points and the geometric sieve for toric varieties
arXiv:2111.01509v3
substantial revision: 17 Jul 2026
```

The relevant results are Theorem 1.4, Theorem 3.11 / Corollary 3.13, Corollary 6.2 and Theorem 1.6(1).

The exact Stage18 shared-edge host is the smooth split toric surface

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad \dim Y=2,
\qquad \operatorname{rank}\operatorname{Pic}(Y)=6,
\]

and the physical radius is the frozen anticanonical height.

For each good split prime, instead of trying to detect the full infinite valuation-parity condition at finite level, reject only the true-bad subset

\[
(v_p(A),v_p(B_0))=(1,0)\ \text{or}\ (0,1).
\]

This condition is detected modulo `p^2`, is contained in the true Stage19 obstruction, and has local mass

\[
\frac4p+O(p^{-2}).
\]

Thus every true Stage19 survivor lies inside a Huang-compatible `n0=2` sieve system of dimension `2`. Substituting the toric EE data and choosing `N=(log B)^lambda` with `lambda<1/88` gives the submitted derived interface

\[
\boxed{
N_2(B)\ll \frac{B(\log B)^5}{(\log\log B)^2}.
}
\]

This is **not** a new strongest global upper; `N2(B)<<_epsilon B^(1/2+epsilon)` remains much stronger. Its value is structural: the old statement that Stage19 only has a fixed-finite-prime local sieve is no longer the correct terminal theorem-species boundary if the mod-`p^2` adapter passes fresh audit.

Detailed derivation:
`stages/stage28/28-40/huang-v3-growing-sieve-adapter.md`.

```text
HUANG_V3_NEW_INPUT=true
STAGE19_GROWING_PRIME_UPPER_SIEVE_DERIVED_PENDING_AUDIT=true
STAGE19_GROWING_PRIME_SIEVE_DIMENSION=2
GLOBAL_N2_STRONGEST_UPPER_REPLACED=false
BRIDGE_ORDERING_RESOLVED_BY_HUANG=false
```

## 4. New effective thin-cover comparison — both sides are generically degree two

Huang Theorem 1.6(1) also supplies an effective positive logarithmic saving for the adelic image of a generically finite cover of degree greater than one over the toric base.

Both Stage19 and Stage20 completion problems are degree-two covers of the common two-face host. After resolution, global rational lifts are contained in their adelic images, so each receives the same theorem **species**

\[
O(B(\log B)^{5-\iota})
\qquad\text{for some }0<\iota<1,
\]

with cover-dependent unspecified `iota`.

This makes the old Stage19 thin-cover zero-density route effective, but it still gives no ordering because `iota_sp` and `iota_face` are not compared.

```text
EFFECTIVE_HILBERT_THINNING_AVAILABLE_SPACE=true
EFFECTIVE_HILBERT_THINNING_AVAILABLE_THIRD_FACE=true
RELATIVE_HILBERT_IOTA_ORDERING_KNOWN=false
```

## 5. Stronger geometric cancellation certificate

Merged hostile-audited PR #1042 gives the exact cover comparison:

```text
SAME_BASE_HOST=true
BOTH_COVER_DEGREE=2
BOTH_BRANCH_BIDEGREE=4_4
BOTH_CORNER_MULTIPLICITY=2_EACH
BOTH_BRANCH_CLASS=-2K_Y
SAME_K3_CANONICAL_TYPE=true
SAME_BRANCH_DIVISOR=false
BIRATIONAL_EQUIVALENCE_PROVED=false
```

The physical base height is the same anticanonical radius `R`.

Therefore the Stage28 ordering cannot be explained by a difference in any of the following coarse invariants:

- base host;
- cover degree;
- branch divisor class;
- canonical/K3 type;
- physical base-height line bundle.

If an asymptotic ordering exists, it must come from finer arithmetic such as branch position/factorisation, rational/adelic lift distribution, accumulating curves or multisections, or interaction with the primitive/exact-face mask.

## 6. Endpoint-circularity firewall for joint correlation

Let `I_sp` and `I_face` be the two completion indicators on the common two-face host. Their product

\[
I_{sp}I_{face}
\]

is the simultaneous space-plus-third-face condition. After the physical adapters this is exactly the perfect-cuboid endpoint: three integral faces plus integral space diagonal.

The canonical roadmap deliberately keeps that endpoint outside Stage16--29. Consequently a Stage28 route that requires a nontrivial asymptotic/lower theorem for the direct joint intersection is off-stage/circular.

A legal Stage28 correlation theorem must compare the **marginals**, or control a centered covariance/energy term without consuming a perfect-cuboid endpoint counting theorem.

```text
DIRECT_JOINT_INTERSECTION_COUNT_ROUTE=OFF_STAGE_ENDPOINT
ENDPOINT_EXISTENCE_OR_NONEXISTENCE_NOT_CONSUMED=true
LEGAL_CORRELATION_ROUTE=marginal_or_centered_energy_without_endpoint_asymptotic
```

## 7. Full StructureRadar rematch

The classified Arsenal was rematched after the receiver was narrowed.

Supporting ACTIVE mechanisms:

```text
SR-STR-161 separated Jacobi/large-sieve interface
SR-STR-164 square-lift collision-cover/sieve
SR-STR-165 Gaussian quadratic-Hecke large sieve
SR-STR-166 charged-once eliminant router
SR-STR-173 same-measure support/moment firewall
```

No ACTIVE card directly compares the two Stage28 marginals.

The closest direct receiver is `SR-STR-169` (same-measure selector correlation), but it remains an `EXTERNAL_GATE`. `SR-STR-174` and `SR-STR-223` are adjacent correlation/fiber-product gates; any use that becomes a direct global joint-lift count is blocked by the endpoint firewall above.

```text
DIRECT_ACTIVE_STAGE28_RELATIVE_WEAPON_FOUND=false
BEST_DIRECT_CORRELATION_RECEIVER=SR-STR-169
BEST_DIRECT_CORRELATION_RECEIVER_STATUS=EXTERNAL_GATE
```

## 8. Rejected 2026 near-match

Corrigan, *A large sieve inequality for characters to quadratic moduli*, Acta Arithmetica 222 (2026), is a genuine new large-sieve theorem for quadratic-polynomial moduli with a weighted zero-density application. It does not directly match the exact toric physical selector / Gaussian-norm squareclass measure, so no transfer is made without a new modulus/measure adapter.

```text
CORRIGAN_2026_DIRECT_TRANSFER=false
```

## 9. Updated obstruction map

The original U1--U4 and the extended U5--U9 now constitute nine materially distinct investigations.

The surviving legal receiver is narrower than the first #1276 submission:

```text
OPEN_GATE_40=GLOBAL_TWO_MARGINAL_RELATIVE_COMPLETION_THEOREM
OPEN_GATE_REQUIRES_ENDPOINT_COUNT=false
OPEN_GATE_ACCEPTABLE_SPECIES=
  same_host_marginal_ratio;
  centered_covariance_or_energy_without_endpoint_asymptotic;
  arithmetic_comparison_of_the_two_distinct_-2K_double_covers_under_physical_height;
  matching_lower_or_asymptotic_survivor_sieve_for_one_or_both_marginals
OPEN_GATE_POPULATION=primitive canonical common two-face physical host
OPEN_GATE_CUTOFF=R<=B
OPEN_GATE_REQUIRED_STRENGTH=strictly improve current bridge corridor or resolve asymptotic ordering
```

The former `stage19_growing_modulus` item is no longer left as a vague external theorem gate: Huang v3 supplies the theorem framework, and the concrete mod-`p^2` adapter is submitted here for fresh audit.

## 10. Current handoff

Because this work was added after the first audit, the prior PASS is historical for its exact old head only. The current extended head requires a new audit.

```text
MATERIALLY_DISTINCT_ROUTES_TESTED=9
DEEP_EXPLORATION_EXTENDED=true
CHECKPOINT40_COMPLETE_AS_SUBMISSION=true
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING_REAUDIT_AFTER_EXTENDED_RESEARCH
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=50
NEXT_EXPECTED_COMMAND=Stage28-audit
CODEX_REQUIRED=false
PERFECT_CUBOID_CONCLUSION=NONE
```