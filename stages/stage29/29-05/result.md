# Stage29-05 — audited dependency, equivalence, route ownership, and double-charge ledger

```text
TASK=29-05_DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
STATUS=AUDITED_PASS_PENDING_MERGE
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
INPUT_29_04=PR1309_AUDITED_PASS_MERGED
PREMATURE_SINGLE_ROUTE_SELECTION=false
MULTI_ROUTE_ATTACK_ALLOWED=true
UNIQUE_PRIMARY_OWNER_REQUIRED=true
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Purpose

Stage29 now has many descriptions of the endpoint: the full four-quadric surface, the degree-64 F7 sign/Kummer presentation, seven K3 quotients, joint V4 and cross quotient, Campedelli quotients, Beauville's irregular cover, modular 8-congruence, local squareclass systems, arrangement/non-Fano tools, and parametrized families. 29-05 does **not** choose one winner. It prevents the same mathematical condition or already-owned theorem from being counted as several independent attacks and gives each current receiver an explicit primary execution owner, supersession, or dormant/umbrella disposition.

## 2. Load-bearing input from 29-04

On the physical host, with

```text
[x:y:z]=[a^2:b^2:c^2],
```

the two edge-ratio Kummer classes are automatically trivial and the four remaining coordinate-squareclass tests are exactly

```text
F_ab, F_ac, F_bc, S.
```

Thus:

```text
R29-KUM4A=DISCHARGED
R29-KUM4B=OPEN
BOOLEAN_16_EQUALS_SIGN_64=false
```

This exact pointwise identity is a deduplication rule: a physical face/space predicate and its corresponding F7 coordinate-squareclass triviality test are one predicate, not two independent savings. It does not identify the global theorem packages, varieties, local sieve laws, or counting measures.

## 3. Material audit repair: receiver completeness

The submission claimed that every active named receiver had exactly one primary owner. Fresh comparison with the canonical controller disproved that claim.

The controller carried 39 residual/retained receiver IDs. The submitted registry owned 30 IDs and left the following 12 without an explicit owner or supersession disposition:

```text
R29-KUM4
R29-NF1QISO
R29-NF3
R29-NF4
R29-NF5
R29-NF6
R29-NF7
R29-NF8
R29-NF-PHYS2
R29-QWEB-CLIFFORD
R29-TERA1
R29-PI1-OPEN
```

This was a material defect because receiver completeness is the central purpose of 29-05.

The audited repair is recorded in `route-registry.json` V2. After repair:

```text
CANONICAL_CONTROLLER_RESIDUAL_OR_RETAINED_IDS_CHECKED=39
SUBMISSION_OWNED_IDS=30
POST_REPAIR_UNCOVERED_IDS=0
RECEIVER_COMPLETENESS=PASS_AFTER_MATERIAL_REPAIR
```

## 4. Canonical attack-route registry

The attack portfolio remains 11 routes:

```text
29-10:
  G10-FULL-ENDPOINT
  G10-LOWGENUS-PICARD
  G10-K3-SIGN

29-11:
  Q11-CAMPEDELLI
  Q11-BEAUVILLE
  Q11-MODULAR
  Q11-BRAUER

29-12:
  J12-JOINT-V4
  J12-LOCAL-SQUARECLASS
  J12-PARAMETRIC
  J12-POP-INTERACTION
```

Pre-attack infrastructure remains:

```text
I07-KUMMER-BRIDGE   owner=29-07
I08-COVERAGE-ATLAS  owner=29-08
I09-LOCAL-INFRA     owner=29-09
```

and cross-foundation identity/adapter normalization has the explicit non-attack synthesis owner

```text
S06-GLOBAL-SYNTHESIS owner=29-06.
```

The number `11` is an execution-portfolio count only:

```text
ROUTE_COUNT_IS_INDEPENDENT_FOUNDATION_COUNT=false
ROUTE_COUNT_IS_INDEPENDENT_PROBABILITY_COUNT=false
UMBRELLA_OWNERSHIP_PROVES_REDUNDANCY=false
UMBRELLA_OWNERSHIP_RESOLVES_INDEPENDENCE=false
```

If a currently amber/umbrella receiver later produces a materially distinct exact arithmetic model, a Gap Scan may promote or split a route.

## 5. Repaired ownership for omitted receivers

### 5.1 Historical KUM4

```text
R29-KUM4 -> SUPERSEDED_BY [R29-KUM4A,R29-KUM4B]
R29-KUM4A -> DISCHARGED pointwise
R29-KUM4B -> I07-KUMMER-BRIDGE, OPEN count adapter
```

The historical unsplit name is no longer a separate live task.

### 5.2 Non-Fano/Hirzebruch internal receivers

The audited 02hc result classified this as a named theorem ecosystem on F7, not an independent foundation. Therefore the structural crosswalks are assigned to `S06-GLOBAL-SYNTHESIS`, not promoted into new attack routes:

```text
R29-NF1QISO -> S06-GLOBAL-SYNTHESIS
  status=DORMANT_OPEN_NOT_NEEDED

R29-NF3 -> S06-GLOBAL-SYNTHESIS
  umbrella children=NF3A/NF3B/NF3C/NF3D

R29-NF4 -> S06-GLOBAL-SYNTHESIS
  rho order-2 character / Q-twisted intermediate double cover

R29-NF5 -> S06-GLOBAL-SYNTHESIS
  finite-abelian-cover topology versus Campedelli/K3 subcovers

R29-NF6 -> S06-GLOBAL-SYNTHESIS
  Campedelli kernels in non-Fano congruence character lattice

R29-NF7 -> S06-GLOBAL-SYNTHESIS
  two-primary boundary versus mod-2 resonance
  secondary arithmetic candidate=Q11-BRAUER
```

`R29-NF7` ownership does not imply a Brauer relation; that implication remains unproved.

### 5.3 Exact dedup of NF8

The original definition of

```text
R29-NF8 = Stage16To20PopulationMasksVsArrangementSubcoverCharacterSupport
```

is now superseded by the finer 29-04 split:

```text
R29-NF8 -> R29-KUM4A + R29-KUM4B.
```

The pointwise mask/character crosswalk is exactly KUM4A and is discharged. The remaining population/subcover counting problem is exactly KUM4B. NF8 is therefore not a twelfth copy of the same work.

### 5.4 Boundary / Clifford / Terasoma / fundamental-group candidates

```text
R29-NF-PHYS2 -> Q11-BRAUER
  status=OPEN_ADAPTER
  boundary-residue transfer is not a Brauer obstruction by itself

R29-QWEB-CLIFFORD -> Q11-BRAUER
  status=AMBER_NEW_THEOREM_REQUIRED
  no rank-7 Clifford/isotropy obstruction is assumed

R29-TERA1 -> G10-K3-SIGN
  status=AMBER_SPECIALIZATION_ADAPTER
  48-node specialization/resolution remains open

R29-PI1-OPEN -> G10-FULL-ENDPOINT
  status=AMBER_EFFECTIVE_ARITHMETIC_ADAPTER
  no effective cuboid-open Chabauty-Kim theorem is certified
```

These are umbrella ownership decisions only. They do not prove the candidates redundant or non-independent.

## 6. Existing receiver ownership retained

The submission assignments for KUM3A/B, KUM4B, G1b, X1, PESCH1, KUM-LOC1/2, LG2/EFF/MB, Campedelli, Beauville, modular, Brauer, and L2-ALG/BAD survive audit. `R29-KUM5` remains owned by `S06-GLOBAL-SYNTHESIS` because it is the exact F7-arrangement-S4 versus modular-residual-S4 crosswalk, not a new attack route by itself.

The legacy umbrella

```text
R29-L2
```

is explicitly superseded by

```text
R29-L2-NT   DISCHARGED
R29-L2-ALG  OPEN -> J12-JOINT-V4
R29-L2-BAD  OPEN -> J12-JOINT-V4.
```

## 7. Exact equivalence / non-equivalence ledger

### 7.1 Named recognition merged only at the audited field scope

```text
F7 seven-line cover <-> standard non-Fano/Hirzebruch N=2 cover over Q(i)
```

is one geometric object with an explicit constant-sign Q twist. It is not two independent endpoint foundations. The standard non-Fano Q-cover is **not** identified with the cuboid Q-form.

### 7.2 Same physical predicate, different formulas

```text
Stage19 space-square predicate
= physical S on the exact-two host
= audited Gaussian-norm/squareclass normal form on that chart
= corresponding F7 coordinate-squareclass triviality test on the physical locus.
```

Likewise the Stage20 missing-face completion and its F7 coordinate test enforce the same physical face predicate. Local blocker laws and K3 equations are tools attached to that predicate, not extra independent survival factors.

```text
NO_MULTIPLY_STAGE19_SQUARECLASS_SAVING_BY_F7_SQUARECLASS_SAVING=true
NO_MULTIPLY_STAGE20_LOCAL_BLOCKER_BY_SAME_FACE_PREDICATE_AGAIN=true
```

### 7.3 Distinct dependent arithmetic routes retained

Campedelli remains distinct because every audited quotient is Q-defined and endpoint Q-points push forward to quotient Q-points. Beauville remains distinct because the audited map direction is a degree-two cover `X_cub -> S_endpoint` and its twist/descent problem is not an F7 quotient. Modular and Brauer routes remain separate under their audited Q/Q(i) and obstruction firewalls.

## 8. Cross-route double-charge firewalls

### K3 versus joint V4

The three V4 characters are correlated structural pieces, not three independent probabilities.

```text
INDIVIDUAL_K3_MARGINAL_FACTS_PRIMARY_OWNER=G10-K3-SIGN
J12_JOINT_V4_SEPARATE_CREDIT_REQUIRES=GENUINELY_JOINT_OR_CROSS_CHARACTER_INFORMATION
```

J12 may reuse a K3 theorem as input but may not credit the same marginal theorem again as joint progress.

### Local squareclass

`J12-LOCAL-SQUARECLASS` may reuse Stage19/20 local laws and F7 squareclass coordinates. Separate credit requires a new simultaneous/joint endpoint local restriction or correlation, not a re-statement of one old predicate.

### Population interaction

`J12-POP-INTERACTION` may reuse the 29-04 cost matrix and Stage28 `K_28` normalization. Separate credit requires new relative-rate, ordering, interaction, or moving-complement control; known marginal smallness cannot be credited again.

## 9. Parametric coverage firewall

Saunderson, A2, Meskhishvili-style, and Peschmann-style families remain family/image data until exact coverage is proved. Closing a family or slice does not close the endpoint.

```text
PESCHMANN_PROVEN_F2_ADAPTER=false
PESCHMANN_INDEPENDENCE_RESOLVED=false
PESCHMANN_CROSSWALK_FAILURE_AUTO_RED=false
```

If the 29-08 crosswalk fails, independence is reassessed rather than declaring the route redundant.

## 10. Combination gate

Before multiplying two savings or combining two obstructions, record all of:

```text
SAME_HOST=true
SAME_PHYSICAL_MEASURE=true
DISTINCT_RESTRICTIONS_PROVED=true
DEPENDENCE_HANDLED=true
HEIGHT_COMPATIBLE=true
MULTIPLICITY_COMPATIBLE=true
FIELD_COMPATIBLE=true
QUANTIFIERS_COMPATIBLE=true
```

If any field is not proved, combination is not certified.

## 11. Backflow / roadmap verdict

No frozen Stage16–28 contract repair is forced by this receiver cleanup.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
ROADMAP_MATERIALITY_CERTIFICATE=false
ROADMAP_REWRITE_REQUIRED=false
```

The 11-route portfolio survives as an execution taxonomy after receiver-completeness repair. `GAP_SCAN_A / ROADMAP_REVIEW_A` remains the correct next item.

## 12. Exit

```text
CHECKPOINT29_05_AUDIT=PASS
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
BOUNDED_REPAIR=RECEIVER_COMPLETENESS_PLUS_LEGACY_SUPERSESSION_PLUS_CROSS_ROUTE_CREDIT_FIREWALLS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=GAP_SCAN_A_ROADMAP_REVIEW_A
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
