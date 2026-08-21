# Stage29-02c-LG2 fresh audit

```text
AUDITED_PR=1293
AUDITED_MATHEMATICAL_SUBMISSION_HEAD=af0895a4f02bedb04d6124e994d403c5ef0dd0c6
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## Scope

Fresh audit covered the finite Picard reduction, the exact lattice/coset encoding, the distinction between numerical classes and effective curves, the multibranch firewall, the immutable upstream Magma source lock, computational-feasibility claims, Stage29 routing, and controller state.

## Exact finite Picard reduction

Let `H=K_S`, with `H^2=16`, and let `d=H.C`. Put

```text
r=gcd(d,16)
m=16/r
n=d/r
y=m*C-n*H.
```

Then

```text
H.y = m*d - 16*n = 0,
```

so `y` lies in `H^perp`. Since the intersection form on `Pic(S)_R` has signature `(1,63)` and `H^2>0`, the orthogonal complement is negative definite; ampleness of `H` is not required for this conclusion.

A direct expansion gives

```text
y^2 = m^2*(C^2-d^2/16).
```

Adjunction gives `C^2+d=2p_a(C)-2`. For geometric genus `g`, `p_a(C)>=g`, hence

```text
g=0: C^2 >= -d-2
g=1: C^2 >= -d.
```

Therefore

```text
g=0: -y^2 <= m^2*(d^2/16+d+2)
g=1: -y^2 <= m^2*(d^2/16+d).
```

The inverse condition

```text
C=(y+nH)/m
```

is exact subject to divisibility in `Pic(S)`. Thus for each allowed degree the candidate numerical classes are contained in a finite ball in a negative-definite integral lattice. Since the audited Freitag--Salvati Manni theorem bounds the unibranch windows by even `d<=176` for genus zero and even `d<=192` for genus one, the total numerical search is finite.

```text
FINITE_PICARD_REDUCTION_AUDIT=PASS
ORTHOGONAL_NEGATIVE_DEFINITE_AUDIT=PASS
PICARD_DIVISIBILITY_RECONSTRUCTION_AUDIT=PASS
G0_NORM_BOUND_AUDIT=PASS
G1_NORM_BOUND_AUDIT=PASS
```

## Effectivity and coverage firewall

The finite lattice reduction does not classify effective integral curves by itself. A surviving numerical class still requires an effectivity/carrier certificate. Freitag--Salvati Manni Theorem 3.1 also requires bijective normalization; multibranch-at-node curves are not covered by the 176/192 cap. Isolated rational points are not addressed by a positive-dimensional carrier enumeration.

The submitted three residual receivers are therefore correctly separated:

```text
R29-LG2=SymmetryReducedCompletePicardClassEnumerationForUnibranchGenus0DegreeLE176AndGenus1DegreeLE192
R29-LG2-EFF=EffectiveCurveCertificationForSurvivingNumericalPicardClasses
R29-LG2-MB=MultibranchAtNodeLowGenusCarrierLedgerOutsideFreitagSalvatiManniTheorem3_1
```

```text
EFFECTIVITY_CERTIFIED=false
MULTIBRANCH_CASES_COVERED=false
ISOLATED_RATIONAL_POINTS_EXCLUDED=false
FAMILY_CARRIER_EXCLUSION_EQUALS_ENDPOINT_NONEXISTENCE=false
```

## Upstream computation lock

The immutable source locator was checked directly:

```text
repo=MichaelStollBayreuth/Verification
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

The file constructs the cuboid surface and 48 singular points, the known-curve intersection matrix with rank `64`, `PicL`, `HinPicL`, automorphism/Galois actions, and the low-degree `CloseVectors` machinery. The degree-2 code uses `8*C-H`; the degree-4 code uses `4*C-H`; the degree-6 route passes through the K3 quotient and lifts back to the surface.

The source explicitly has a rank-44 kernel in the degree-6 lifting step and estimates the close-vector count using

```text
LkertrcE_vol * bound^(Dimension(LkertrcE)/2),
```

so the exponent is `44/2=22`.

### Bounded source-attribution repair

The submission could be read as saying that the Magma rank assertion alone proves the *full* Picard group. The code itself constructs the known-curve rank-64 lattice under the generation assumption; the identification of that lattice with the full geometric Picard group is the Testa--Stoll theorem already audited in Stage29-02a. `upstream-code-lock.md` was repaired to separate these two roles.

No finite-reduction formula or receiver changes.

```text
UPSTREAM_SOURCE_LOCK_AUDIT=PASS
UPSTREAM_BLOB_MATCH_AUDIT=PASS
RANK64_KNOWN_CURVE_LATTICE_CODE_AUDIT=PASS
FULL_PICARD_GROUP_THEOREM_REUSE_AUDIT=PASS
DEGREE6_LIFT_KERNEL_RANK_AUDIT=PASS_44
CLOSE_VECTOR_VOLUME_EXPONENT_AUDIT=PASS_22
```

## Computational feasibility

The submission correctly stops before claiming a production enumeration. Finiteness is mathematical; practical tractability through degree 176/192 is not established. The published degree-6 K3/lift strategy is highly specialized and cannot be promoted uniformly to all degrees without a new complete enumerator.

The recommended symmetry, node-incidence, known-curve, congruence and effectivity pruning is admissible as a production plan, but none is counted as a completed search.

```text
FULL_D176_D192_ENUMERATION_COMPLETED=false
NAIVE_RUNTIME_TRACTABILITY_ESTABLISHED=false
PRODUCTION_ENUMERATOR_EXISTS=false
BOUNDED_STOP_AUDIT=PASS
```

## Stage routing / controller repair

PR #1292 is already merged, while the inherited controller still recorded its Work import as `AUDITED_PASS_PENDING_MERGE`. The controller is mechanically synchronized to merged state in this audit.

LG2 itself is accepted as a finite-reduction milestone but remains an open residual computation. It should no longer block exploration of the independent 29-02 foundations. The active suffix head advances to

```text
29-02d_BEAUVILLE_IRREGULAR_COVER_Q_DESCENT
```

while `R29-LG2`, `R29-LG2-EFF`, and `R29-LG2-MB` remain live receivers for later computational work.

No Stage16--28 backflow is triggered.

## Verdict

```text
CHECKPOINT29_02C_LG2_AUDIT=PASS
FINITE_PICARD_REDUCTION_AUDIT=PASS
UPSTREAM_COMPUTATION_LOCK_AUDIT=PASS_AFTER_SOURCE_ATTRIBUTION_REPAIR
FULL_D176_D192_ENUMERATION_COMPLETED=false
EFFECTIVITY_CERTIFIED=false
MULTIBRANCH_CASES_COVERED=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
KEEP_STAGE29_NATIVE=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02d
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
