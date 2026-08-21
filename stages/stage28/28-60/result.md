# Stage28-60 — causal decomposition and double-charge synthesis

```text
TASK_ID=Stage28-60
CHECKPOINT=60
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Stage28 is a comparison of two marginals, not one added-condition transition

Stage19 and Stage20 are disjoint exact-face strata. The legal direct bridge remains

\[
\frac{M_3(B)}{N_2(B)}.
\]

Using the common exactly-two-face scale,

\[
S_{sp}=N_2/M_2,
\qquad
F_3=M_3/M_2,
\]

one has the exact identity

\[
\boxed{M_3/N_2=F_3/S_{sp}}.
\]

`S_sp` is a literal Stage18 -> Stage19 survival rate. `F3` is an adjacent-stratum population-size ratio, not an objectwise survival probability.

Both are lower order on the `M2` scale:

\[
S_{sp}\to0,
\qquad
F_3\to0,
\]

while both target populations are polynomially infinite:

\[
N_2\gg B^{1/4},
\qquad
\liminf M_3(B)/B^{1/3}\ge 27/(40\pi^2)>0.
\]

## 2. New causal deduction: third-face interaction is positive-divergent

Stage25 already proves the space interaction invariant

\[
\mathcal I_{sp}
=\frac{N_2/M_2}{N_1/M_1}
\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

Define the analogous face ladder

\[
\mathcal I_{face}
=\frac{M_3/M_2}{M_2/M_1}
=\frac{M_3M_1}{M_2^2}.
\]

Using

\[
M_1\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
M_2\sim C_{M_2}B(\log B)^5,
\]

and the Stage28-50-r2 explicit `M3` liminf gives

\[
\boxed{
\liminf_{B\to\infty}
B^{-1/3}(\log B)^9\mathcal I_{face}(B)
\ge
\frac{81}{160\pi^4C_{M_2}^2}>0.
}
\]

Hence

\[
\boxed{\mathcal I_{face}(B)\to\infty.}
\]

So both the space condition and successive face integrality exhibit positive interaction enhancement after prior face structure, on their respective matched population-ratio scales.

This does not imply stochastic independence, does not multiply the two enhancements, and does not order `M3` against `N2`.

## 3. What does not explain the Stage19/Stage20 difference

Checkpoint40/r2 proves that both completion problems have the same

- toric base `Y=Bl_4(P1xP1)`;
- cover degree `2`;
- total branch class `-2K_Y`;
- K3 canonical type;
- first-order local sieve dimension `2`;
- explicit Huang thin-cover range `eta<1/46`.

The exact normalized local quotient has no relative polynomial drift and no relative first-order logarithmic drift. Therefore the known local/generic-cover data do not explain a relative power or log-power difference.

## 4. Where the first certified structural differential occurs

The completion covers are not identical. Checkpoint40-r2 proves

```text
SPACE_BRANCH_PROFILE=4 x genus-0
THIRD_FACE_BRANCH_PROFILE=2 x genus-1
SAME_QUADRATIC_EXTENSION_OVER_FIXED_BASE=false
```

This is a genuine structural difference. But no existing theorem converts it into a relative physical-height count. Checkpoint50-r2 additionally rules out the shortcut of using the rational space-branch components themselves as a positive physical Stage19 family.

Thus the branch-profile difference is currently **structural evidence**, not a quantified cause of the direct `M3/N2` ratio.

## 5. Construction-side differential

The best known explicit physical families have efficiencies

```text
N2: kappa/h = 2/8 = 1/4
M3: kappa/h = 2/6 = 1/3
```

and Stage28-50-r2 gives a positive explicit `B^(1/3)` liminf coefficient for the M3 family. The resulting `1/12` construction-floor gap is genuine family-level information, but it does not identify the true population exponent gap.

## 6. Double-charge verdict

The Stage19 space-square, squareclass, local-parity and degree-two-cover descriptions are one space condition with multiple proof layers. The Stage20 missing-face square, K3 cover, local blocker, Selberg sieve and Huang theorem are likewise one third-face condition with multiple proof layers.

Within either marginal, alternative proof savings are not multiplied. Across the two marginals, multiplying condition rates would consume the joint three-face-plus-space endpoint, which is outside Stage28.

```text
DOUBLE_CHARGE_CHECK=PASS_CANDIDATE
SPACE_EQUIVALENT_DESCRIPTIONS_RECHARGED=false
THIRD_FACE_PROOF_LAYERS_MULTIPLIED=false
LOCAL_EULER_CONSTANT_PROMOTED_TO_GLOBAL_RATIO=false
COMMON_HUANG_RANGE_CANCELLED_TO_GLOBAL_RATIO=false
BRANCH_PROFILE_PROMOTED_TO_POWER_SAVING=false
CONSTRUCTION_GAP_PROMOTED_TO_TRUE_EXPONENT_GAP=false
POSITIVE_INTERACTION_INVARIANTS_MULTIPLIED=false
PERFECT_CUBOID_JOINT_ENDPOINT_CONSUMED=false
```

## 7. Causal classification

The strongest Stage28 causal statement is now:

1. both completions are rare relative to the two-face scale;
2. both show positive interaction enhancement after prior face conditioning;
3. known first-order local and generic-cover complexity are matched and do not distinguish their rates;
4. the first certified geometric differential is the branch-component profile / quadratic squareclass;
5. known constructions favor the Stage20 target at the family-floor level;
6. no theorem currently converts those differentials into an asymptotic ordering of `M3` and `N2`.

Therefore

```text
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
RELATIVE_LOCAL_POWER_DIFFERENTIAL_PROVED=false
RELATIVE_BRANCH_PROFILE_COUNT_THEOREM_PROVED=false
```

## 8. Remaining receiver

```text
OPEN_GATE_60=DistinctBranchProfilePhysicalHeightMarginalComparison
COMMON_HOST=two-face physical toric environment under R<=B
SOURCE_MARGINAL=N2
TARGET_MARGINAL=M3
REQUIRED_STRENGTH=direct marginal comparison strong enough to improve bridge corridor or resolve ordering
ACCEPTABLE_SPECIES=branch-sensitive rational-lift theorem; same-measure dispersion/energy theorem; moving-height marginal comparison
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

This gate is precise and nonblocking for checkpoint70 bounded synthesis.

## 9. Exit

```text
CHECKPOINT60_CAUSAL_DECOMPOSITION_COMPLETE_CANDIDATE=true
NEW_FACE_INTERACTION_THEOREM_CANDIDATE=true
DOUBLE_CHARGE_CHECK=PASS_CANDIDATE
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
REPAIR_REQUIRED=UNKNOWN_PENDING_AUDIT
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=70
NEXT_EXPECTED_COMMAND=Stage28-audit
PERFECT_CUBOID_CONCLUSION=NONE
```