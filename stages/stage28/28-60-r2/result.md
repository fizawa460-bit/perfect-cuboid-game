# Stage28-60-r2 — interaction-curvature deepening result

```text
TASK_ID=Stage28-60-r2
CHECKPOINT=60
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
PARENT_CHECKPOINT60_PR=1280
PARENT_CHECKPOINT60_AUDIT=PASS
PARENT_CHECKPOINT60_MERGED=true
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Parent checkpoint60 remains valid

The audited parent result is unchanged:

- Stage19 and Stage20 are disjoint exact-face strata and `M3/N2` is a matched population-size bridge ratio, not survival probability;
- `I_sp=(N2/M2)/(N1/M1)` is positive-divergent by `S25-W02`;
- `I_face=(M3/M2)/(M2/M1)` is positive-divergent by Stage28-60;
- the known local/generic-cover mechanisms do not distinguish the two marginals at power or first-order log-power level;
- the first certified geometric differential remains `space:4 x genus0` versus `third-face:2 x genus1` branch profiles;
- no branch-sensitive physical-height comparison theorem is currently certified;
- double-charge and perfect-cuboid-endpoint firewalls remain in force.

## 2. New r2 theorem candidate: normalized interaction curvature

Define

\[
\mathcal I_{sp}=\frac{N_2/M_2}{N_1/M_1},
\qquad
\mathcal I_{face}=\frac{M_3/M_2}{M_2/M_1}.
\]

Then exactly

\[
\frac{\mathcal I_{face}}{\mathcal I_{sp}}
=\frac{M_3}{N_2}\frac{N_1}{M_2}.
\]

Stage21 and Stage22 imply

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

so

\[
\frac{M_2}{N_1}
\sim \frac{24\pi C_{M_2}}{\kappa}(\log B)^2.
\]

Define

\[
\boxed{
\mathcal K_{28}(B)
=(\log B)^2\frac{\mathcal I_{face}(B)}{\mathcal I_{sp}(B)}.
}
\]

Then

\[
\boxed{
\frac{M_3(B)}{N_2(B)}
\sim
\frac{24\pi C_{M_2}}{\kappa}\mathcal K_{28}(B).
}
\]

This is a new exact/asymptotic adapter from audited population laws.  It does not identify the bridge limit, but it makes the bridge problem equivalent to one normalized interaction-curvature problem.

```text
NORMALIZED_INTERACTION_CURVATURE_THEOREM_CANDIDATE=true
BRIDGE_AND_K28_ASYMPTOTICALLY_CONSTANT_PROPORTIONAL=true
TRUE_BRIDGE_LIMIT_IDENTIFIED=false
```

## 3. Critical relative-interaction threshold

Let

\[
\mathcal J_{28}=\mathcal I_{face}/\mathcal I_{sp}.
\]

The critical scale is exactly `(log B)^(-2)`:

```text
J_28=o((logB)^-2)                 => M3/N2 -> 0
J_28~lambda*(logB)^-2, lambda>0  => M3/N2 -> (24*pi*C_M2/kappa)*lambda
J_28/(logB)^-2 -> infinity       => M3/N2 -> infinity
```

The `(log B)^2` normalizer is not artificial.  `S25-W06` records `N1:(a,b)=(1,4)` and `M2:(1,6)`, so it is exactly the audited two-log intermediate-population gap at common polynomial order.  This is explanatory bookkeeping only and is not an extra independent factor.

## 4. Existing bounds do not decide the threshold

The checkpoint30 bridge corridor gives

\[
\mathcal J_{28}(B)
\gg_\varepsilon
B^{-1/6-\varepsilon}(\log B)^{-2}
\]

and, for fixed `0<delta<1/46`,

\[
\mathcal J_{28}(B)
=o\!\left(B^{3/4}(\log B)^{3-\delta}\right).
\]

Thus the critical `(log B)^(-2)` scale lies inside the current corridor.  The facts `I_sp->infinity` and `I_face->infinity` do not order the two interactions.

```text
INTERACTION_THRESHOLD_RESOLVED=false
DIRECT_BRIDGE_CORRIDOR_IMPROVED=false
```

## 5. Post-merge deep exploration

The r2 batch tests seven materially distinct follow-ups beyond the audited parent checkpoint:

1. exact interaction-quotient algebra — **success**;
2. `N1/M2` asymptotic normalizer — **success**;
3. Manin `(a,b)` explanation of the log-squared normalizer — **success as explanation**;
4. threshold-vs-current-corridor comparison — **negative certificate**;
5. common-host/literal-share reformulation — no stronger estimate;
6. bounded branch-sensitive literature rematch — no direct discharge found;
7. joint selector/covariance shortcut — rejected because it consumes the deferred perfect-cuboid endpoint.

The bounded external rematch checked Huang's toric cover machinery, Kummer point-counting results such as Malmendier--Sung `arXiv:1901.11151`, and degree-two K3 rational-point results such as Martinez-Marin `arXiv:2505.13262`.  None of the checked theorem interfaces simultaneously matches the two present branch profiles, the exact physical height, and the relative marginal strength required by the threshold receiver.  This is a bounded-rematch statement, not a claim of literature nonexistence.

## 6. Sharpened checkpoint60 receiver

The parent gate

```text
DistinctBranchProfilePhysicalHeightMarginalComparison
```

can now be sharpened to

```text
OPEN_GATE_60_R2=RelativeInteractionCurvatureThresholdFromDistinctBranchProfiles
BASE=Y=Bl_4(P1xP1)
SPACE_COVER=degree2; branch profile 4x genus0
THIRD_FACE_COVER=degree2; branch profile 2x genus1
HEIGHT=physical Euclidean R<=B
TARGET=J_28=I_face/I_sp
CRITICAL_SCALE=(log B)^(-2)
NORMALIZED_TARGET=K_28=(log B)^2 J_28
SUFFICIENT_OUTPUT=place J_28 below/at/above (log B)^(-2), or otherwise resolve M3/N2 ordering by a legal one-sided marginal comparison
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

This is strictly more precise than asking generically for “a new global theorem”: it specifies the common base, the two branch profiles, the physical height, the exact comparison quantity and the threshold strength needed to change the Stage28 conclusion.

## 7. Exit

No current theorem proves whether `K_28` tends to zero, a positive finite limit, infinity, or oscillates.  Neither true population exponent is identified.  The r2 contribution is the exact causal compression and sharpened receiver, not a false ordering claim.

```text
MATERIALLY_DISTINCT_R2_ROUTES=7
CHECKPOINT60_R2_BOUNDED_DEEPENING_COMPLETE_CANDIDATE=true
OPEN_GATE_RESEARCH_REQUEST_READY=true
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
REPAIR_REQUIRED=UNKNOWN_PENDING_AUDIT
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=70
NEXT_EXPECTED_COMMAND=Stage28-audit
```