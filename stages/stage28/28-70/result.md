# Stage28-70 — bounded maximal synthesis / closeout candidate

```text
TASK_ID=Stage28-70
CHECKPOINT=70
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=PROVED_SYNTHESIS_CANDIDATE
DEPENDS_ON=Stage28-10,20,30,40-r2,50-r2,60-r2,60-r3
```

## 1. Frozen comparison contract

Stage28 compares, under the same primitive/canonical physical cutoff `R<=B`,

- `N2(B)`: primitive canonical exactly-two-face cuboids with integral space diagonal;
- `M3(B)`: primitive canonical Euler cuboids with exactly three integral face diagonals and no space-diagonal requirement.

The source and target are disjoint exact-face strata. Stage28 is therefore **not** a literal objectwise survival transition. The common host is

\[
H_{\ge2}(B)=M_2(B)+M_3(B),
\]

with matched shares

\[
\Sigma_{19}=N_2/H_{\ge2},\qquad \Phi_{20}=M_3/H_{\ge2},
\]

and the exact bridge identity

\[
\boxed{\Phi_{20}/\Sigma_{19}=M_3/N_2}.
\]

## 2. KNOWN_RESULTS

The strongest audited theorem surface entering checkpoint70 is

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

and

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}
\ge \frac{27}{40\pi^2}>0,
\qquad
M_3(B)\ll_\eta B(\log B)^{5-\eta}
\]

for every fixed `0<eta<1/46`. Neither true population exponent is known.

The certified bridge corridor remains

\[
\boxed{
M_3/N_2\gg_\varepsilon B^{-1/6-\varepsilon}
}
\]

and, for every fixed `0<delta<1/46`,

\[
\boxed{
M_3/N_2=o\!\left(B^{3/4}(\log B)^{5-\delta}\right).
}
\]

The common intermediate laws are

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

and `H_ge2(B)~M2(B)`.

Checkpoint40-r2 proved the first certified geometric differential between the two completion covers over the same base `Y=Bl_4(P1xP1)`:

```text
space cover branch profile      = 4 x genus 0
third-face cover branch profile = 2 x genus 1
cover degree                    = 2 on both sides
total branch class              = -2K_Y on both sides
```

The normalized good-prime local quotient has only finite Euler-product bias after the quadratic-character normalization, and Huang's generic degree-two thin-cover range does not distinguish the two marginals at the relevant exponent level.

Checkpoint50-r2 gives the audited Stage20 Saunderson lower with an explicit coefficient and height adapter:

```text
R<=8r^6
1/8<=s/r<=4/5
liminf M3(B)/B^(1/3) >= 27/(40*pi^2)
```

Checkpoint60-r2 defines

\[
\mathcal I_{sp}=\frac{N_2/M_2}{N_1/M_1},
\qquad
\mathcal I_{face}=\frac{M_3/M_2}{M_2/M_1},
\]

and proves

\[
\frac{\mathcal I_{face}}{\mathcal I_{sp}}
=\frac{M_3}{N_2}\frac{N_1}{M_2}.
\]

Writing

\[
\mathcal J_{28}=\mathcal I_{face}/\mathcal I_{sp},
\qquad
\mathcal K_{28}=(\log B)^2\mathcal J_{28},
\]

one has

\[
\boxed{
\frac{M_3(B)}{N_2(B)}
\sim \frac{24\pi C_{M_2}}{\kappa}\,\mathcal K_{28}(B).
}
\]

Checkpoint60-r3 adds a genuine low-degree fixed-curve differential under the same common-base physical polarization normalization:

```text
M_sp   = pi_sp^*(-K_Y)
M_face = pi_face^*(-K_Y)
M_sp^2 = M_face^2 = 8
Stage19 physical M4 curves = absent
Stage19 all odd physical M-degrees = absent
Stage20 Saunderson physical M-degree = 6
Stage19 M6 absence = NOT proved
```

Thus the fixed-curve spectra are asymmetric through degree five and Stage20 attains degree six, but strict degree-six source/target separation is not established.

## 3. ADDITIONAL_DEDUCTIONS

### 3.1 Exact ordering threshold in normalized interaction curvature

Set

\[
A_{28}=\frac{24\pi C_{M_2}}{\kappa}>0.
\]

Since

\[
M_3/N_2\sim A_{28}\mathcal K_{28},
\]

the unresolved population ordering is asymptotically equivalent to the behavior of one normalized interaction quantity:

```text
K_28 -> 0        <=> M3/N2 -> 0
K_28 -> infinity <=> M3/N2 -> infinity
K_28 -> L>0      =>  M3/N2 -> A_28*L
```

More sharply, the equality threshold `M3/N2 ~ 1` corresponds to

\[
\boxed{
\mathcal K_{28}(B)\sim \frac{\kappa}{24\pi C_{M_2}}
}
\]

or equivalently

\[
\boxed{
\mathcal J_{28}(B)
\sim \frac{\kappa}{24\pi C_{M_2}}(\log B)^{-2}.
}
\]

Therefore any future theorem proving

```text
liminf K_28 > kappa/(24*pi*C_M2)
```

would certify eventual `M3>N2`, while

```text
limsup K_28 < kappa/(24*pi*C_M2)
```

would certify eventual `M3<N2`. No such theorem is currently available.

### 3.2 Both matched host shares are sparse

Because `H_ge2~M2`, the Stage19 and Stage20 host shares satisfy

\[
\Sigma_{19}\sim N_2/M_2,
\qquad
\Phi_{20}\sim M_3/M_2.
\]

The current upper bounds imply

\[
\Sigma_{19}\to0,
\qquad
\Phi_{20}\to0.
\]

Thus both Stage19 and Stage20 are sparse inside the same at-least-two-face host. Stage28's unresolved question is not whether either share vanishes; it is their **relative** vanishing rate.

### 3.3 The fixed-curve differential cannot by itself order the populations

The audited Stage19 M4/odd-degree obstruction rules out fixed rational curves below physical M-degree six, while Stage20 contains a physical M-degree-six Saunderson curve. Both sides may nevertheless contain degree-six contributions of `B^(1/3)` type, and Stage19 retains the moving-fibre/rank-jump/first-small-point mechanism from Stage14-4al. Hence the fixed-curve spectrum is a causal differential but not a whole-population ordering theorem.

## 4. CAUSAL_SYNTHESIS

The bounded Stage28 evidence now separates three levels cleanly.

1. **Local/generic-cover level:** no certified polynomial or first-order log-power separation. The two degree-two covers have matched total branch class, matched generic thin-cover range, and only finite normalized local Euler-product bias.
2. **Geometric/fixed-curve level:** a real asymmetry exists: `4 x genus0` versus `2 x genus1` branch components, and Stage19 has no physical M4 or odd-degree fixed rational curves whereas Stage20 realizes physical M-degree six.
3. **Global moving-population level:** unresolved. No theorem converts the branch/fixed-curve differential into control of `J_28` at the critical `(log B)^(-2)` scale under the physical height.

The global missing input is therefore not another endpoint bound. It is a relative marginal theorem sensitive to the moving complement and/or branch arithmetic on the two distinct degree-two K3 covers.

## 5. LOWER_STAGE_REINTERPRETATIONS

Later audited stages sharpen lower-stage interfaces without invalidating their historical audits:

- Stage19's historical `sqrt(log B)` lower is superseded for downstream use by the audited quarter-power weapon `S25-W01`: `N2(B)>>B^(1/4)`.
- Stage20's historical one-parameter `B^(1/6)` Saunderson lower is superseded by Stage26's two-parameter `B^(1/3-epsilon)` theorem and then, for Stage28 use, by checkpoint50-r2's explicit `B^(1/3)` liminf coefficient.
- Stage26's `H_ge2~M2` host adapter is retained unchanged and is the correct common host for Stage28.
- No lower-stage population definition, cutoff, primitive convention, or canonicalization rule is invalidated; lower-stage recomputation is not required.

## 6. REFINEMENT_CANDIDATES

```text
R28-RF1=PhysicalLowDegreeRootSpectrumM6
purpose=classify the remaining Stage19 physical M-degree-six rational-curve stratum
status=FINITE_OPTIONAL_REFINEMENT_NOT_STAGE28_BLOCKER

R28-RF2=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
purpose=control J_28=I_face/I_sp relative to (log B)^(-2) under physical R<=B
status=GLOBAL_ORDERING_RECEIVER_RESEARCH_REQUEST_READY

R28-RF3=UniformMovingEllipticFibreSquareLiftHeightCount
purpose=improve Stage20 construction efficiency beyond the current one-third scale or obtain a same-host marginal comparison
status=EXTERNAL_FUTURE_GATE
```

## 7. NEW_HEURISTICS

The matched finite bridge ratios at `B=10^4,5*10^4,2*10^5,10^6` are

```text
0.72, 0.677419355, 0.706896552, 0.858823529
```

They show neither a certified monotone trend nor an asymptotic ordering and are not promoted to theorem status.

The fixed-curve asymmetry makes `M3`-favored behavior plausible at one geometric submechanism, but the uncontrolled Stage19 moving complement prevents promoting this to a population-level heuristic stronger than `UNRESOLVED`.

## 8. OPEN_GATES

```text
OPEN_GATE_PRIMARY=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
BASE=Y=Bl_4(P1xP1)
SPACE_COVER=degree2; branch profile 4x genus0
THIRD_FACE_COVER=degree2; branch profile 2x genus1
HEIGHT=physical Euclidean R<=B
TARGET=J_28=I_face/I_sp
CRITICAL_SCALE=(log B)^(-2)
NORMALIZED_TARGET=K_28=(log B)^2 J_28
ORDERING_THRESHOLD=K_28 compared with kappa/(24*pi*C_M2)
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true

OPEN_GATE_FINITE_OPTIONAL=PhysicalLowDegreeRootSpectrumM6
STAGE19_M6_ABSENCE_PROVED=false
DISTINGUISHED_L40_IS_COMPLETE_SPECTRUM=false
```

The perfect-cuboid endpoint remains deferred and is not an admissible shortcut for Stage28.

## 9. NEXT_STAGE_QUESTIONS

Stage29 should inherit the certified Stage28 bridge package and place it into the full interaction synthesis:

1. compare the Stage21-28 transition laws on a common cutoff and population ledger;
2. keep the Stage28 `(log B)^2` interaction normalizer charged exactly once;
3. distinguish local, branch-geometric, fixed-curve, moving-family, and construction mechanisms;
4. record that Stage28's relative ordering remains intrinsically unresolved on current theorems;
5. preserve the perfect-cuboid endpoint firewall while identifying the residual obstruction after all transition comparisons are assembled.

## 10. Artifact / arsenal decision

The normalized interaction-curvature adapter and the common-polarization fixed-curve differential are reusable in Stage29. A self-contained Stage28 closeout bundle and a compact arsenal promotion are therefore warranted.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_PATH=stages/stage28/28-70/self-contained-bundle.md
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_PATH=docs/stage28-arsenal-promotion.md
```

## 11. SYNTHESIS_STOP_REASON

Checkpoint60 already exhausted bounded repo-native causal deepening through branch comparison, interaction curvature, low-degree lattice reconstruction, McKinnon/quasi-polarized rematches, and the exact Saunderson M-degree-six adapter. The remaining primary gate requires a substantially new same-measure moving-complement/branch-sensitive theorem; the remaining M6 classification is a finite optional refinement and is not sufficient by itself to resolve the bridge.

Continuing Stage28 with renamed variants of the same receivers would violate the bounded-stop rule.

```text
KNOWN_RESULTS=FROZEN_ABOVE
ADDITIONAL_DEDUCTIONS=ORDERING_THRESHOLD_CONSTANT_AND_COMMON_HOST_SHARE_SPARSITY
CAUSAL_SYNTHESIS=LOCAL_TIE_GEOMETRIC_DIFFERENTIAL_GLOBAL_MOVING_GATE
LOWER_STAGE_REINTERPRETATIONS=LATER_SUPERSESSIONS_WITHOUT_REOPEN
REFINEMENT_CANDIDATES=R28-RF1,R28-RF2,R28-RF3
NEW_HEURISTICS=FINITE_RATIO_NONMONOTONE_AND_FIXED_CURVE_SIGNAL_ONLY
OPEN_GATES=PRIMARY_RELATIVE_INTERACTION_THRESHOLD_PLUS_OPTIONAL_M6_CLASSIFICATION
NEXT_STAGE_QUESTIONS=HANDOFF_TO_STAGE29_INTERACTION_SYNTHESIS
SYNTHESIS_STOP_REASON=FURTHER_PROGRESS_REQUIRES_SUBSTANTIALLY_NEW_THEOREM_OR_OPTIONAL_OFF_STAGE_CLASSIFICATION
SYNTHESIS_STOP_RULE_SATISFIED=YES
```

## 12. Submission / safety state

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false_AT_CHECKPOINT70_BEYOND_ALREADY_INTEGRATED_STAGE28_SUPERSESSIONS
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED; CHECKPOINT70_IS_SYNTHESIS
NUM_REUSE_CHECK=NOT_APPLICABLE_NO_NEW_NUMERICAL_WORK
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
LITERAL_SUBSET_TRANSITION=false
CONSTRUCTION_FAMILY_RATIO_AS_POPULATION_RATIO=false
FIXED_CURVE_SPECTRUM_AS_GLOBAL_ORDERING=false
BRANCH_PROFILE_AS_POWER_SAVING=false
PERFECT_CUBOID_CONCLUSION=NONE
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
REPAIR_REQUIRED=UNKNOWN_PENDING_AUDIT
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
CLOSE_STAGE_AFTER_AUDIT_PASS=true
NEXT_STAGE_AFTER_AUDIT_PASS=Stage29
NEXT_EXPECTED_COMMAND=Stage28-audit
```