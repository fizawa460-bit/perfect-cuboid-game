# Stage29-02hb — audited Campedelli quotient foundation

```text
STATUS=AUDITED_PASS_AFTER_BOUNDED_REPAIR
NOVELTY_IN_REPO=HIGH_VALUE_NEW_QUOTIENT_FOUNDATION
LITERATURE_NOVELTY_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Exact global quotient

Keep the endpoint canonical model and resolution separate:

```text
Sbar = canonical cuboid surface with 48 A1 nodes
S    = minimal resolution
```

The finite degree-64 seven-line sign cover is `Sbar -> P2`. For every admissible rank-3 kernel `H <= Gamma=(Z/2)^6`, define

```text
Cbar_H := Sbar/H.
```

Then the original finite morphism factors globally as

```text
Sbar --/H--> Cbar_H --degree 8--> P2.
```

The second map has deck group `Gamma/H=(Z/2)^3` and the branch inertia on the same seven lines is the image of the original sign inertia. When the seven images are the seven nonzero group elements and every triple has nonzero sum, this is exactly a Campedelli line arrangement after algebraic closure.

This is the same quotient map globally, not an analogy between two generic function fields.

```text
SAME_GLOBAL_MAP_AUDIT=PASS
```

## 2. Exact finite kernel classification

The exact checker gives

```text
raw admissible labelings = 1680
GL(3,F2)                 = 168
distinct kernels H       = 10
```

All ten satisfy the local stabilizer-injectivity condition.

The field-of-definition distinction is load-bearing:

```text
geometric / Q(i) S4 orbits = 8 + 2
certified Q S3 orbits       = 6 + 2 + 2.
```

Therefore the original “two arithmetic quotient types” compression is rejected. Three Q-symmetry representatives are certified sufficient for the next arithmetic pass. The exact number of abstract Q-isomorphism classes is not claimed.

```text
R29-CAMP0=DISCHARGED
R29-CAMP0A=DISCHARGED_EXACT_10_KERNELS
R29-CAMP0B=DISCHARGED_GEOMETRIC_QI_8_PLUS_2
R29-CAMP0C=DISCHARGED_CERTIFIED_Q_6_PLUS_2_PLUS_2
```

## 3. Resolution-level degree-8 etale cover

For each admissible kernel, `H` meets every sign-cover point stabilizer trivially. Hence

```text
Sbar -> Cbar_H
```

is finite etale everywhere, including at the rational-double-point locus.

`Cbar_H` has exactly six `A1` singularities, one above each triple branch point. Minimal resolution commutes with this etale local base change, so

```text
S -> C_H
```

is genuinely finite etale of degree eight.

Thus the quotient is not merely a free-action candidate after resolution.

```text
R29-CAMP1=DISCHARGED
RESOLUTION_ETALE_AUDIT=PASS
```

## 4. Campedelli invariants and universal cover

The quotient is a classical Campedelli surface geometrically. Independently, every nontrivial character of `(Z/2)^3` sees four branch lines, giving building bundle `O_P2(2)` and

```text
(beta_H)_*O = O + O(-2)^7.
```

Hence

```text
pg=0
q=0
chi=1
K^2=2.
```

The six A1 resolutions are crepant.

Now, and only now, the Mendes Lopes--Pardini--Reid theorem applies to the established degree-8 etale cover. After base change to `C`, `S` is the universal cover and

```text
pi1(C_H)=(Z/2)^3.
```

## 5. Q-form firewall

Every kernel `H` is Q-defined because it lies in the constant rational coordinate-sign group, so `C_H=S/H` is a Q-surface and the quotient map is Q-defined.

The literature classifies the geometric Campedelli object. It does not identify the particular cuboid quotient with an arbitrarily chosen standard Campedelli Q-model. A Q-form/twist adapter is required before importing external arithmetic statements about a specific Q-model.

Likewise the geometric `S4` symmetry cannot be used as Q arithmetic symmetry; the exact repair is the `6+2+2` certified Q decomposition above.

## 6. Exact one-way rational-point compression

On the physical endpoint open all seven branch forms are nonzero, so the quotient is etale there. Therefore for every admissible kernel

```text
perfect-cuboid Q-point -> C_H(Q).
```

Consequently

```text
C_H(Q)=empty
```

for any one audited quotient would exclude physical endpoint rational points.

The converse is false without `H`-torsor descent. The corrected receiver is

```text
R29-CAMP2=ArithmeticHTorsorDescentForThreeCertifiedQSymmetryRepresentatives.
```

Additional receivers:

```text
R29-CAMP3=SevenCampedelliInvolutionQuotientsWithQFormAndRationalVsEnriquesLedger
R29-CAMP4=CampedelliBrauerAndTwoPrimaryDescentCompatibilityWith29_02f
```

## 7. Population-stage firewall

This is a pointwise endpoint quotient only. It does not transfer Stage16--20 counting populations, physical height, primitivity, canonical ordering, or asymptotic density.

```text
STAGE16_20_POPULATION_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
ASYMPTOTIC_TRANSFER=false
BACKFLOW_TO_STAGE16_28=false
```

## Final state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02HB_AUDIT=PASS
BOUNDED_REPAIR=Q_QI_ORBIT_SPLIT_PLUS_CANONICAL_RESOLUTION_SCOPE_PLUS_QFORM_FIREWALL
SAME_GLOBAL_MAP_AUDIT=PASS
GENERIC_TO_GLOBAL_AUDIT=PASS_AFTER_SCOPE_REPAIR
Q_QI_FIELD_SCOPE_AUDIT=PASS_AFTER_MATERIAL_REPAIR
RESOLUTION_ETALE_AUDIT=PASS
POPULATION_FIREWALL_AUDIT=PASS
R29_CAMP0=DISCHARGED
R29_CAMP1=DISCHARGED
GEOMETRIC_QI_KERNEL_ORBITS=8+2
CERTIFIED_Q_KERNEL_ORBITS=6+2+2
EXACT_Q_ISOMORPHISM_CLASS_COUNT_PROVED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
AUTO_ADVANCE_TO_29_03=false
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
NEXT_ITEM=29-02hc
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
