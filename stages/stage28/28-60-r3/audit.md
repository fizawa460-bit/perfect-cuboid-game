# Stage28-60-r3 fresh audit

```text
TASK_ID=Stage28-audit
AUDITED_PR=1282
AUDITED_MATHEMATICAL_SUBMISSION_HEAD=84057ffb43218a87aeb3ef3ad078faf62033f09b
CHECKPOINT=60-r3
AUDIT_VERDICT=PASS
REPAIR_REQUIRED=false
```

## Scope

This audit independently checks the new r3 load-bearing claims rather than treating CI or the submission labels as proof. The parent checkpoint60 and r2 results remain inherited audited inputs. The new claims are: the Stage19 odd physical M-degree obstruction, the resulting M5 closure/fixed-curve floor, the common physical-polarization adapter, the exact Stage20 Saunderson M-degree-six certificate, and the bounded-stop/open-receiver boundary.

## 1. Stage19 anti-invariant congruence

The exact reconstructed positive Gram matrix for the physical anti-invariant lattice has diagonal entries divisible by 4 and off-diagonal entries even. Therefore every integral norm is divisible by 4. The current head's workflow `Stage28-60-r3 low-degree K3 spectrum` also completes successfully on the audited submission head (run 32439648595), but the mathematical conclusion below is checked independently of that success flag.

For a split physical curve C with deck conjugate delta(C), write x=C-delta(C) and let D be its image on the base Y, so pi^*D=C+delta(C). Then

```text
x^2 = 4 C^2 - 2 D^2.
```

The K3 Neron-Severi lattice is even, hence the first term is 0 mod 4. On Y, with L=-K_Y, adjunction parity gives D^2 == L.D mod 2. For the split component, M_sp.C=L.D. Consequently

```text
-x^2 == 2*(M_sp.C) mod 4.
```

Since every integral anti-invariant norm is 0 mod 4, an odd M_sp.C would force residue 2 mod 4 and is impossible. A deck-invariant non-branch connected pullback has even physical degree because its map to the base has degree 2; the positive physical branch locus is already excluded by the audited branch firewall. Thus the odd-degree obstruction applies to the full positive physical source, not only to one split subcase.

```text
ANTI_INVARIANT_NORM_MOD4_AUDIT=PASS
ODD_PHYSICAL_M_DEGREE_OBSTRUCTION_AUDIT=PASS
STAGE19_PHYSICAL_M5_FIXED_CURVE_AUDIT=ABSENT
```

Together with the inherited audited facts `M_sp.C<4` impossible and `M_sp.C=4` empty, the Stage19 fixed rational-curve floor is at least 6. This only controls finite fixed-curve mechanisms; it does not control the moving/collective complement.

## 2. Common physical polarization

The source and target are different K3 covers of the same two-face toric base Y. The common base bundle is

```text
L=-K_Y=phi^*O_P2(1),
M_sp=pi_sp^*L,
M_face=pi_face^*L,
M_sp^2=M_face^2=8.
```

Therefore source and target curve degrees are directly comparable in the same physical edge-height normalization. This does not identify the two K3 surfaces or their divisor classes literally.

```text
COMMON_PHYSICAL_POLARIZATION_ADAPTER_AUDIT=PASS
LITERAL_SAME_K3_OR_DIVISOR=false
HEIGHT_ADAPTER_POWER_LOSS=0
```

## 3. Saunderson physical M-degree six

For homogeneous Euclid parameters `[r:s]`, the six Saunderson edge/face-diagonal forms A,B,C,D,E,F are all homogeneous of degree 6. Direct symbolic verification gives the three Euler-brick square identities, and `gcd(A,B,C)=1`, so the edge map has pullback `O_P1(6)` and no projective base point.

Moreover

```text
E-A = 2*u*w^2,
F-B = 2*v*w^2,
s/r = (F-B)/(2*D+E-A)
```

on a dense open set. Hence the full K3 parametrization is generically birational to its image. Therefore the Saunderson image curve satisfies exactly

```text
M_face.C_S=6.
```

On the already-audited positive-density cone its physical height is comparable to the sixth power of the primitive parameter height, giving the fixed-curve count scale `Theta(B^(1/3))`.

```text
SAUNDERSON_DEGREE6_ALGEBRA_AUDIT=PASS
SAUNDERSON_PARAMETERIZATION_BIRATIONAL_AUDIT=PASS
STAGE20_SAUNDERSON_PHYSICAL_M_DEGREE_AUDIT=PASS_6
STAGE20_FIXED_M6_RATIONAL_CURVE_AUDIT=PRESENT
```

## 4. Spectral and global firewalls

The 40 distinguished Shimada roots have no M6 witness, but they are explicitly not the complete root spectrum. Therefore no source M6 absence is certified. The correct finite receiver remains

```text
PhysicalLowDegreeRootSpectrumM6
```

with gluing/coset, effectivity/chamber, boundary, automorphism, Q-descent, invariant/split and singular-rational-member checks still required.

The fixed-curve spectrum also does not control the Stage19 moving first-hit/rank-jump/collective complement. Therefore it cannot be promoted to a new numerical bridge bound or source/target ordering. The global receiver remains

```text
MovingComplementOrBranchSensitiveInteractionThresholdTheorem
TARGET=I_face/I_sp relative to (log B)^(-2)
ENDPOINT_COUNT_FORBIDDEN=true
```

This is sufficiently precise/research-request-ready for checkpoint70 closeout. Resolving the finite M6 receiver could sharpen the causal spectrum, but even a complete M6 answer would not remove the global moving-complement gate.

```text
STRICT_SOURCE_TARGET_M6_SPECTRAL_SEPARATION=false
NEW_NUMERIC_BRIDGE_BOUND=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
FIXED_CURVE_SPECTRUM_AS_GLOBAL_ORDERING=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 5. Exploration/advance verdict

The r3 work adds eight materially distinct routes beyond the parent/r2 work and ends with one exact finite receiver plus one genuinely global theorem receiver. No routine algebraic rearrangement visible in the current repository would discharge the global threshold. The bounded-exploration claim is therefore accepted in the Stage16-29 roadmap sense; it is not a claim that the finite M6 classification has already been performed.

```text
MATERIALLY_DISTINCT_R3_ROUTES_AUDIT=PASS_8
MAXIMAL_BOUNDED_EXPLORATION_AUDIT=PASS_WITH_EXPLICIT_M6_FINITE_RECEIVER
OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS
CHECKPOINT60_R3_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_TO_CHECKPOINT70=true
NEXT_CHECKPOINT=70
NEXT_EXPECTED_COMMAND=Stage28-main-batch
```
