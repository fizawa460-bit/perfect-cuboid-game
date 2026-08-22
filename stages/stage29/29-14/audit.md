# Stage29-14 fresh adversarial audit

```text
AUDITED_PR=1322
AUDITED_SUBMISSION_HEAD=f1d2e645879ff0e47d784f8a74e4154389cacf7d
AUDIT_VERDICT=PASS_AFTER_BOUNDED_POSITIVE_REPAIR
BOUNDED_POSITIVE_REPAIR=K3_SMOOTH_LOCUS_RESOLUTION_PUSHFORWARD_PLUS_LOW_DEGREE_SOURCE_PROVENANCE
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## 1. F7 branch avoidance — PASS

The exact finite F7 map on the canonical model is

```text
Sbar -> P2,
[x:y:z]=[a1^2:a2^2:a3^2],
D=V(xyz(x+y)(x+z)(y+z)(x+y+z)).
```

For a physical endpoint rational point all three side coordinates are nonzero and

```text
x+y=b3^2,
x+z=b2^2,
y+z=b1^2,
x+y+z=c^2.
```

Each displayed diagonal coordinate is nonzero on a nondegenerate physical cuboid. Equivalently, over Q a sum of two or three rational squares can vanish only when every summand vanishes. Therefore no physical endpoint Q-image meets any of the seven branch lines.

```text
R29_SLICE_BRANCH=DISCHARGED_PHYSICAL_Q_ENDPOINT_AVOIDS_FULL_F7_BRANCH_DIVISOR
PHYSICAL_ENDPOINT_IN_F7_UNRAMIFIED_LOCUS=true
F7_64_SHEETS_AS_PHYSICAL_COUNTING_MULTIPLICITY=false
```

The last firewall is essential: geometric sign sheets do not convert to canonical primitive population multiplicity.

## 2. Q-liftable S3 fixed loci — PASS

A transposition fixes one of

```text
x=y, x=z, y=z.
```

At `x=y`, the endpoint equation gives `b3^2=x+y=2x=2a1^2`; since `a1 != 0`, this forces `(b3/a1)^2=2`, impossible over Q. The cyclic cases are identical.

For completeness, if a 3-cycle fixed a projective Q-point, its projective scalar `lambda in Q` would satisfy `lambda^3=1`, hence `lambda=1`, forcing `x=y=z`, already excluded. Thus the full Q-liftable coordinate-permutation stabilizer is trivial on physical endpoint rational points.

```text
R29_SLICE_S3FIX=DISCHARGED_NO_PHYSICAL_Q_POINT_ON_COORDINATE_PERMUTATION_FIXED_LOCI
S3_STABILIZER_ON_PHYSICAL_Q_ENDPOINT_TRIVIAL=true
FULL_GEOMETRIC_S4_STABILIZER_CLAIM=false
```

## 3. Testa--Stoll degree <= 6 carrier package — PASS with provenance strengthening

The current Testa--Stoll theorem classifies all integral curves of canonical/projective degree at most six on the cuboid surface. The immutable public verification source

```text
repo=MichaelStollBayreuth/Verification
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

constructs the finite known low-degree curve configuration, verifies the full rank-64 Picard lattice used in the computation, excludes unknown conics in the relevant class search, handles the degree-four classes, and the K3-assisted degree-six computation ends with no degree-six curves on the canonical surface.

The explicit low-degree equations force a zero side/diagonal or a nonphysical equality/field condition on the physical Q-open, so no positive nondegenerate physical perfect-cuboid family is carried by this degree range.

```text
R29_SLICE_LD6=DISCHARGED_IMPORTED_COMPLETE_DEGREE_LE_6_CARRIER_CLASSIFICATION_NO_POSITIVE_PHYSICAL_FAMILY
LOW_DEGREE_CLASSIFICATION_FINITE_EXPLICIT=true
DEGREE_6_INTEGRAL_CURVES_ON_ENDPOINT=false
```

This does not touch isolated rational points or higher-degree carriers. `R29-LG2`, `R29-LG2-EFF`, and `R29-LG2-MB` remain open.

## 4. Combined closed slices — PASS

The currently certified closed loci used by 29-14 are a finite collection of proper positive-codimension loci/classes on the irreducible endpoint surface. The low-degree package is finite by the complete classification above. Hence their finite union is geometrically proper.

This is only a geometric noncoverage statement. No theorem proves that a nonempty endpoint rational set has a point outside the union; if the endpoint rational set is empty, rational-point coverage statements can be vacuous.

```text
R29_COV_CLOSED_SLICES=DISCHARGED_CURRENT_CERTIFIED_CLOSED_SLICE_UNION_GEOMETRICALLY_PROPER
GEOMETRIC_GLOBAL_COVERAGE_BY_CURRENT_CLOSED_SLICES=false
GLOBAL_CLOSED_SLICE_ENDPOINT_Q_COVERAGE_PROVED=false
COVERAGE_FRACTION_ASSIGNED=false
```

## 5. Coordinate-sign K3 pushforward — PASS and bounded positive strengthening

Stage29-06 distinguishes the finite normal quotients

```text
Sbar -> Kbar_j
```

from their minimal K3 resolutions `K_j -> Kbar_j`. Each coordinate-sign involution is Q-defined and the canonical quotient map has degree two.

A physical endpoint point has the signed coordinate being quotiented nonzero, so it is not fixed by that sign involution. Section 1 also places it away from the F7 ramification arrangement. Therefore its quotient image lies in the smooth locus of `Kbar_j`. The minimal resolution is an isomorphism over that smooth locus, so the image canonically yields a Q-point on the smooth K3 resolution as well.

```text
R29_COV_K3_PUSH=DISCHARGED_GLOBAL_ENDPOINT_PUSHFORWARD_TO_K3_SMOOTH_LOCUS_AND_RESOLUTION
PHYSICAL_ENDPOINT_QPOINT_PUSHES_TO_KBAR_SMOOTH_QPOINT=true
PHYSICAL_ENDPOINT_QPOINT_GIVES_K3_RESOLUTION_QPOINT=true
K3_QPOINT_IMPLIES_ENDPOINT_QPOINT=false
K3_QUOTIENT_QPOINT_EMPTINESS_PROVED=false
```

This is a one-way strengthening only. In particular `K_c` is the Stage20/Testa--Stoll Euler K3 and has rational families, so no strategy requiring `K_c(Q)=empty` is available.

## 6. Global coverage semantics — PASS

The audited 29-08 Master-Hit proof remains the only certified global parametrized coverage statement among the compared families: every primitive Euler brick, hence every endpoint candidate, is represented after gcd normalization. The universal exponent-one blocker remains conjectural, so `J12-PARAMETRIC` stays AMBER.

The 28 endpoint genus-five and 15 Euler-K3 elliptic fibrations remain geometric counts. Not every individual fibration is certified over Q, and no theorem says known sections or multisections generate all rational points.

No stronger certified natural-slice theorem forcing every endpoint Q-point onto a proper closed exceptional locus was found in the current source/repository screen.

## 7. Portfolio reconstruction

```text
R29_SLICE_BRANCH=DISCHARGED
R29_SLICE_S3FIX=DISCHARGED
R29_SLICE_LD6=DISCHARGED
R29_COV_CLOSED_SLICES=DISCHARGED_GEOMETRIC_NONCOVERAGE
R29_COV_K3_PUSH=DISCHARGED_GLOBAL_PUSHFORWARD_TO_SMOOTH_K3_RESOLUTIONS

GLOBAL_CLOSED_SLICE_ENDPOINT_Q_COVERAGE_PROVED=false
GLOBAL_ENDPOINT_QUOTIENT_PUSHFORWARD_COVERAGE_PROVED=true
GLOBAL_ENDPOINT_PARAMETRIC_CANDIDATE_COVERAGE_PROVED=true

ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-15_ENDPOINT_ARSENAL_REMATCH
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

No imported family, low-degree theorem, K3 architecture, or Peschmann coverage theorem receives new attack credit in 29-14. The only new credit remains the exact branch/symmetry slice closure and the clarified coverage semantics; the resolution-level K3 pushforward is an audit strengthening of the same supporting result.
