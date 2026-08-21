# Stage28-40-r2 audit history

## Fresh re-audit after U10 repair

```text
AUDITED_PR=1277
AUDITED_REPAIRED_HEAD=c586f916bfb61cee1b87fae71dd99e22e750dfc3
AUDIT_VERDICT=PASS
CHECKPOINT40_R2_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_TO_CHECKPOINT50=true
NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage28-main-batch
```

The previously blocking U10 algebra defect is repaired. The current `branch-component-decomposition.md` now contains the exact four-factor identity

\[
F_{\rm sp}/4=
(u_1u_2-iv_1v_2)(u_1u_2+iv_1v_2)
(u_1v_2-iu_2v_1)(u_1v_2+iu_2v_1),
\]

and multiplying the two conjugate pairs gives

\[
(u_1^2u_2^2+v_1^2v_2^2)
(u_1^2v_2^2+u_2^2v_1^2),
\]

whose expansion is exactly the submitted quartic `F_sp/4`. Therefore the four irreducible `(1,1)` space-branch components and the `4 x genus-0` profile are now supported by a correct load-bearing identity.

U13 remains valid after repair: the corrected space branch support differs mod 2 from the two genus-one third-face branch components, so the radicand quotient is not a square in `Qbar(Y)^*`; the two quadratic extensions over the fixed base are distinct. The firewalls against inferring abstract K3 non-isomorphism/non-birationality or a counting ordering remain intact.

The r2 exhaustion claim also passes. U1-U14 cover materially distinct repo-native lanes: endpoint bounds, finite data, first-order and growing-prime sieve structure, exact relative Euler product, common cover geometry, branch-component geometry, quadratic squareclass separation, explicit Huang thin-cover range, Kummer-height transfer, correlation/endpoint firewalls, and StructureRadar/Arsenal rematches. No additional currently available repo-native route was identified that would yield a strict bridge improvement without genuinely new global arithmetic input or using the deferred perfect-cuboid endpoint.

The remaining receiver is accepted as research-request-ready:

```text
OPEN_GATE_40_R2=DistinctBranchProfileDoubleCoverMarginalComparison
COMMON_HOST=Y=Bl_4(P1xP1)
SPACE_BRANCH_PROFILE=4x_genus0
THIRD_FACE_BRANCH_PROFILE=2x_genus1
REQUIRED_STRENGTH=strict_bridge_upper_improvement_or_asymptotic_ordering
ENDPOINT_COUNT_FORBIDDEN=true
```

```text
U10_FACTORISATION_REPAIR_AUDIT=PASS
U10_BRANCH_PROFILE_AUDIT=PASS
U13_POST_REPAIR_AUDIT=PASS
MATERIALLY_DISTINCT_ROUTES_TOTAL_AUDIT=PASS_14
MAXIMAL_BOUNDED_EXPLORATION_CLAIM_AUDIT=PASS
OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS
PERFECT_CUBOID_ENDPOINT_FIREWALL_AUDIT=PASS
NUMERIC_BRIDGE_UPPER_IMPROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

---

## Historical hostile audit — submission head `c59a9e7028b70599eba3cdacad193940e06e58fa`

```text
AUDIT_VERDICT=FAIL_REPAIR_REQUIRED
CHECKPOINT40_R2_AUDIT=FAIL_REPAIR_REQUIRED
REPAIR_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
NEXT_EXPECTED_COMMAND=Stage28-audit
```

The old head wrote the Stage19 space-branch expression as a sum of two conjugate-pair products. That displayed equality was false. The audit required replacement by the exact four-factor product and a downstream reread of U10/U13/result/controller. That repair was subsequently completed and is superseded operationally by the fresh PASS above; this historical FAIL is retained for provenance.
