# SR-STR-222 external literature follow-up — Thorner–Zaman partial upgrade

Date: 2026-08-18
Structure: `SR-STR-222`
Receiver: `Stage14-tH33 / SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio`
Input mode: Work external-literature search, then ChatGPT primary-source applicability check

## Certified outcome

```text
DIRECT_FULL_TARGET_THEOREM_COUNT=0
THORNER_ZAMAN_RAY_CLASS_PARTIAL_UPGRADE=true
SUPER_KAI_INDIVIDUAL_RAY_CLASS=PARTIAL_DIRECT_ENGINE
JOINT_FIXED_RESIDUE_AND_FIXED_SECTOR=false
SR_STR_222_APPLICABILITY=FAIL_FULL_TARGET
TH33_STATUS=UNRESOLVED_EXTERNAL_GATE
NEW_MINIMAL_BARRIER=RayClassToCanonicalSectorOrdinaryResidueAdapter
ARSENAL_PROMOTION=NO
```

No published unconditional theorem located in this search directly supplies the full tH33 target: one fixed ordinary Gaussian residue modulo odd squarefree `d=B^o(1)`, one strict canonical D4 sector, and a fixed-power long radial interval, uniformly in the super-Kai range.

The search does, however, narrow the obstruction. Thorner–Zaman provides a genuine individual Chebotarev asymptotic at polynomial conductor scale. In an abelian ray-class extension of `K=Q(i)`, taking the abelian subgroup to be the full Galois group keeps the fixed field in Theorem 1.4 equal to `Q(i)`. The theorem's conductor parameter is the maximum norm of the Hecke-character conductors. For a ray-class group of finite modulus `(d)`, these finite conductors divide the ray modulus, so their norms are bounded by the finite ray-conductor scale (up to any separately introduced fixed auxiliary normalization modulus). Thus the analytic range is compatible with `d=X^{o(1)}` at conductor level.

This is only a partial upgrade. The Chebotarev theorem counts prime ideals by Frobenius/ray class. It does not itself impose the continuous canonical-sector condition on a chosen Gaussian generator, nor does it directly prove that the canonical D4-sector generator lies in the exact ordinary residue `beta_* mod d`. Passing from an ideal ray class to that generator-level joint condition requires a new exact adapter, or an individual asymptotic for the combined finite ray character and angular Hecke-character family.

## Primary-source ledger

### Thorner–Zaman — partial upgrade

Jesse Thorner and Asif Zaman, *A unified and improved Chebotarev density theorem*, Algebra & Number Theory 13 (2019), 1039–1068; arXiv:1803.02823.

Relevant locator:
- Theorem 1.4.
- Equation (1.11), defining the maximal Hecke conductor `Q`.
- Corollaries 1.2–1.3 for asymptotic regimes.
- Proof architecture in Sections 4–5; Landau–Siegel-zero treatment is retained in the theorem.

Theorem 1.4 gives an unconditional individual conjugacy-class asymptotic once

```text
x >= (D_K * Q * n_K^{n_K})^C
```

for an absolute effective exponent `C`, with the possible exceptional term retained. This provides the analytic engine for a super-Kai individual ray-class count after the ray-class specialization, but not the missing angular/generator condition.

Applicability verdict:

```text
INDIVIDUAL_RAY_CLASS_DENSITY_ENGINE=YES
SUPER_KAI_CONDUCTOR_SCALE=YES_AFTER_RAY_CLASS_SPECIALIZATION
CANONICAL_SECTOR_CONDITION=NO
ORDINARY_CANONICAL_GENERATOR_RESIDUE=NO_DIRECT_STATEMENT
FULL_TH33_DIRECT=NO
```

### Kai / Mitsui — exact geometry but insufficient modulus range

Wataru Kai, *Notes on Mitsui's Prime Number Theorem with Siegel zeros*, arXiv:2209.11816v2.

Kai refines Mitsui's prime-element theorem for bounded convex archimedean regions and congruence classes while retaining a possible Hecke Siegel zero. It allows pseudopolynomial growth of the modulus norm, which matches the already-audited tH31 safe envelope. For `(d) subset Z[i]`, `N((d))=d^2`; the tH33 packet is explicitly beyond that verified pseudopolynomial envelope.

Applicability verdict:

```text
FIXED_SECTOR_PLUS_ORDINARY_RESIDUE_GEOMETRY=YES
SUPER_KAI_MODULUS_RANGE=NO
FULL_TH33_DIRECT=NO
```

### Stucky — sector comparator only

Joshua Stucky, *Gaussian Primes in Narrow Sectors*, arXiv:2008.11325v2.

Stucky gives Gaussian-prime asymptotics with simultaneous norm-short-interval and angular restrictions, but does not impose one growing ordinary Gaussian congruence modulus of the tH33 type.

Applicability verdict:

```text
SECTOR_AND_RADIAL_LOCALIZATION=YES
GROWING_ORDINARY_RESIDUE=NO
FULL_TH33_DIRECT=NO
```

### Averaged progression/sector results

Bombieri–Vinogradov / Barban–Davenport–Halberstam type results, including the number-field/sector literature already identified in tH33, average over moduli, classes, or related families. They do not directly discharge one frozen fixed-U modulus/residue packet without a separately proved exceptional-set-to-physical-measure adapter.

## Narrowed remaining theorem/adapter target

The external search changes the shape of the open gate from a generic "super-Kai individual residue theorem" to a more precise compatibility problem:

```text
RayClassToCanonicalSectorOrdinaryResidueAdapter
```

A successful route may take either form:

1. Prove that the tH33 physical canonical generator condition can be recovered from a finite collection of ray classes, with exact control of unit/conjugation choices and no loss of the fixed sector; or
2. Prove/use an individual prime-element asymptotic with the finite ray character and angular Hecke character imposed simultaneously at polynomial finite-conductor scale.

The adapter must preserve:
- one frozen ordinary modulus `d=B^o(1)`;
- one frozen invertible ordinary residue `beta_* mod d`;
- the strict canonical D4 sector;
- fixed-power radial headroom;
- possible exceptional real Hecke character terms;
- pointwise, not average-over-moduli, lower density at `B^{-o(1)}` relative scale.

## Firewall

This result does **not** prove a fixed-power saving for the fixed-U packet, does not improve the current physical whole-family exponent `1/2`, and does not imply perfect-cuboid nonexistence. `SR-STR-222` remains unresolved and its arsenal decision remains `PENDING`.