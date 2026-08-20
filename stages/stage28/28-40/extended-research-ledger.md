# Stage28-40 — extended deep-research ledger after first audit

```text
TASK_ID=Stage28-40-EXTENDED
PARENT_PR=1276
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=POST_AUDIT_EXTENDED_RESEARCH_PENDING_REAUDIT
PREVIOUS_AUDIT_HEAD=fbba8ace257357027a0f359cecdca81cabde89a8
PREVIOUS_AUDIT_VERDICT=PASS_FOR_OLD_HEAD_ONLY
```

This ledger extends the original U1--U4 checkpoint40 exploration rather than replacing it. The operator explicitly requested that the research continue before a final audit.

## U5 — 2026 Huang effective toric sieve / growing-modulus rematch

A materially new literature input exists after the earlier StructureRadar searches: Zhizhong Huang, arXiv:2111.01509v3, substantially revised 17 July 2026.

The current version gives:

- effective equidistribution on smooth proper split toric varieties with globally generated anticanonical bundle, with polynomial dependence on the finite adelic congruence level;
- a Selberg sieve for collections of local conditions detected modulo a uniformly bounded prime power;
- explicit toric EE data `gamma=dim X+rank Pic(X)+epsilon`, `h(B)=(log B)^(-1/2+epsilon)`;
- effective logarithmic thinning for adelic images of generically finite covers of degree greater than one.

The exact Stage18 shared-edge host is the split toric surface `Y=Bl_4(P1xP1)`, `dim=2`, `rank Pic=6`, with physical radius equal to the frozen anticanonical height.

The Stage19 parity obstruction admits a one-valuation truncated bad subset detected modulo `p^2` and retaining rejection density `4/p+O(p^-2)` on good split primes. Applying Huang with `n0=2` yields a derived growing-prime dimension-two upper sieve. A conservative choice `N=(log B)^lambda`, `lambda<1/88`, gives

\[
N_2(B)\ll B(\log B)^5/(\log\log B)^2.
\]

This does not improve the certified half-power global upper, but it materially closes the former fixed-prime-only theorem-species gap.

Detailed adapter: `stages/stage28/28-40/huang-v3-growing-sieve-adapter.md`.

```text
U5_NEW_LITERATURE_INPUT=true
U5_STAGE19_GROWING_PRIME_UPPER_SIEVE_DERIVED=true
U5_GLOBAL_NUMERIC_UPPER_IMPROVED=false
U5_REAUDIT_REQUIRED=true
```

## U6 — effective degree-two cover comparison

Huang Theorem 1.6(1) is independently relevant to both competing completion covers. A global rational lift lies in the adelic image of the resolved degree-two cover, so each completion population is bounded by a toric-base count with some positive logarithmic saving.

This upgrades the Stage19 thin-cover route from qualitative little-o to an effective log-saving theorem species, but gives different unspecified constants `iota_sp` and `iota_face`; it does not order `N2` and `M3`.

The result is symmetric at the coarse cover-degree level:

```text
SPACE_COVER_DEGREE=2
THIRD_FACE_COVER_DEGREE=2
EFFECTIVE_HILBERT_LOG_SAVING_AVAILABLE_BOTH=true
RELATIVE_IOTA_ORDERING_KNOWN=false
```

Thus generic degree and generic Hilbert-irreducibility thinness do not explain a Stage28 ordering.

## U7 — exact coarse cover geometry comparison

Merged hostile-audited PR #1042 already proves more than the original U3 summary used:

- both conditions live over the same shared-edge two-face base `Y=Bl_4(P1xP1)`;
- the Stage19 space cover branch divisor and Stage20 third-face branch divisor both have bidegree `(4,4)` before the four corner blowups;
- both have multiplicity two at the four toric corners;
- both strict branch classes are `-2K_Y`;
- both degree-two covers therefore have the same K3 canonical type after normalization/resolution;
- the actual branch divisors differ and no birational equivalence is proved.

The physical base height is the same anticanonical radius `R`.

Therefore the following coarse geometric invariants cancel in the Stage28 comparison:

```text
BASE_HOST_DIFFERENCE=false
COVER_DEGREE_DIFFERENCE=false
BRANCH_DIVISOR_CLASS_DIFFERENCE=false
CANONICAL_TYPE_DIFFERENCE=false
PHYSICAL_BASE_HEIGHT_LINE_BUNDLE_DIFFERENCE=false
```

Any genuine global ordering must come from finer arithmetic: the position/factorisation of the branch divisor, distribution of rational/adelic lifts, accumulating curves/multisections, or correlation with the primitive/exact-face physical mask.

This is a stronger negative certificate than merely saying that both are “K3-like”.

## U8 — direct joint-correlation route hits the deferred endpoint

On the common two-face host let

- `I_sp` be the indicator that the space diagonal is integral;
- `I_face` be the indicator that the missing third face is integral.

The product `I_sp I_face` counts common-host objects satisfying both completion predicates. After the exact-face adapters, this is precisely the three-face-plus-space perfect-cuboid endpoint, which the canonical roadmap explicitly keeps outside Stage16--29.

Hence a Stage28 attack that requires an asymptotic or nontrivial lower bound for

\[
\sum I_{sp}I_{face}
\]

is circular/off-stage: it has replaced the bridge problem by the endpoint problem.

Legal Stage28 correlation technology must instead control the *marginals* or a centered covariance/energy term without requiring an endpoint count or endpoint existence/nonexistence.

```text
DIRECT_JOINT_INTERSECTION_COUNT_ROUTE=OFF_STAGE_ENDPOINT
PERFECT_CUBOID_ENDPOINT_DEFERRED=true
LEGAL_RELATIVE_ROUTE=marginal_comparison_or_centered_energy_without_endpoint_asymptotic
```

This narrows the earlier `joint_correlation` OPEN_GATE: “joint correlation” is not by itself a valid receiver unless its conclusion is stated without consuming an endpoint counting theorem.

## U9 — full classified StructureRadar rematch

The terminal Arsenal classification was rematched to the exact Stage28 bridge receiver.

Useful ACTIVE structural weapons include:

- `SR-STR-161`: separated-coefficient quadratic/Jacobi large-sieve interface;
- `SR-STR-164`: square-lift collision-cover/sieve interface;
- `SR-STR-165`: Gaussian quadratic-Hecke large-sieve transfer after separation/conductor cleanup;
- `SR-STR-166`: charged-once eliminant routing dichotomy;
- `SR-STR-173`: same-measure conditioned support/moment firewall.

None is a direct theorem comparing the two Stage28 marginals on the common host.

The closest exact correlation receivers remain external gates:

- `SR-STR-169`: same-measure selector correlation;
- `SR-STR-174`: pushforward/joint-indicator correlation architecture;
- `SR-STR-223`: moving compatible small-point/fiber-product control.

For Stage28, `SR-STR-223` is especially dangerous if interpreted as a direct joint-lift count, because that again approaches the deferred perfect-cuboid endpoint. `SR-STR-169` is the cleaner marginal/correlation species, but remains unproved on the exact Stage28 common-host measure.

```text
DIRECT_ACTIVE_STAGE28_RELATIVE_WEAPON_FOUND=false
BEST_ACTIVE_SUPPORTING_WEAPONS=SR-STR-161,SR-STR-164,SR-STR-165,SR-STR-166,SR-STR-173
BEST_DIRECT_CORRELATION_RECEIVER=SR-STR-169
BEST_DIRECT_CORRELATION_RECEIVER_STATUS=EXTERNAL_GATE
```

## Rejected fresh near-match — Corrigan 2026

C. C. Corrigan, *A large sieve inequality for characters to quadratic moduli*, Acta Arithmetica 222 (2026), gives a large sieve for additive characters with quadratic-polynomial moduli and a weighted zero-density application.

It is a genuine new 2026 large-sieve result but does not directly match the Stage28 toric physical selector / Gaussian-norm squareclass system, so it is retained only as adjacent literature. No transfer is made without a polynomial-modulus and physical-measure adapter.

```text
CORRIGAN_2026_DIRECT_TRANSFER=false
```

## Extended route synthesis

Original U1--U4 plus U5--U9 now give nine materially distinct investigations.

The strongest global bridge upper remains unchanged. What changed is the obstruction map:

1. first-order local sieve dimensions are equal;
2. Stage19's old fixed-prime-only asymmetry can now be attacked effectively via Huang v3 and a mod-`p^2` truncation;
3. cover degree, base, branch class, canonical type and physical base-height line bundle are also equal at the coarse level;
4. a direct joint-intersection theorem is off-stage because it is the perfect-cuboid endpoint;
5. no classified ACTIVE Arsenal weapon currently supplies the missing marginal comparison.

The remaining legal receiver is therefore narrower:

```text
OPEN_GATE_40=GLOBAL_TWO_MARGINAL_RELATIVE_COMPLETION_THEOREM
RECEIVER_MUST_AVOID_DIRECT_ENDPOINT_COUNT=true
ACCEPTABLE_SPECIES=
  same_host_marginal_ratio;
  centered_covariance_or_energy_without_endpoint_asymptotic;
  arithmetic_comparison_of_two_distinct_-2K_double_covers_under_physical_height;
  matching_lower_or_asymptotic_survivor_sieve_for_one_or_both_marginals
REQUIRED_STRENGTH=strictly improve current M3/N2 corridor or resolve asymptotic ordering
```

```text
MATERIALLY_DISTINCT_ROUTES_TESTED=9
CHECKPOINT40_NUMERIC_UPPER_IMPROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
DEEP_EXPLORATION_EXTENDED=true
PREVIOUS_AUDIT_SUPERSEDED_FOR_CURRENT_HEAD=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage28-audit
PERFECT_CUBOID_CONCLUSION=NONE
```