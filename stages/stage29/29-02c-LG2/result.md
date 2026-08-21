# Stage29-02c-LG2 — Picard 176/192 finite enumeration preflight

```text
TASK_ID=Stage29-02c-LG2
ROLE=UNIBRANCH_LOW_GENUS_FINITE_PICARD_REDUCTION
STATUS=AUDITED_PASS
PARENT_INPUT=PR1292_AUDITED_W29_A
PERFECT_CUBOID_CONCLUSION=NONE
```

## Input already audited

PR #1292 audited Freitag--Salvati Manni Theorem 3.1 on the cuboid surface:

```text
bijective normalization, genus g, canonical/projective degree d
=> d <= 176 + 16g.
```

Together with the audited even-degree constraint on the endpoint surface:

```text
g=0: even 2 <= d <= 176
g=1: even 4 <= d <= 192.
```

This suffix asks whether the resulting finite degree window can actually be turned into a complete Picard-lattice computation without silently assuming effectivity or tractable runtime.

## Exact finite-lattice reduction

Let `S` be the smooth minimal resolution, and let `H=K_S` be the pullback of the canonical hyperplane class. The audited endpoint geometry gives

```text
H^2 = K_S^2 = 16,
H.C = d
```

for a nonexceptional integral curve `C` of canonical/projective degree `d`.

Write

```text
r = gcd(d,16),
m = 16/r,
n = d/r,
y = m C - n H.
```

Then `y` is an integral Picard class and

```text
H.y = m d - 16 n = 0.
```

Thus `y` lies in the negative-definite lattice `H^perp` by the Hodge index theorem.

Adjunction gives

```text
C^2 + d = 2 p_a(C) - 2.
```

Since `p_a(C) >= g`, every genus-zero candidate satisfies

```text
C^2 >= -d-2,
```

and every genus-one candidate satisfies

```text
C^2 >= -d.
```

Also

```text
y^2 = m^2 (C^2 - d^2/16).
```

Therefore every candidate lies in a finite ball in the negative-definite lattice `H^perp`:

```text
g=0:  -y^2 <= m^2 (d^2/16 + d + 2),
g=1:  -y^2 <= m^2 (d^2/16 + d).
```

The congruence condition

```text
y + n H is divisible by m in Pic(S)
```

recovers `C=(y+nH)/m` exactly. Consequently, for each allowed even `d`, the set of numerical Picard classes satisfying degree plus the necessary adjunction lower bound is finite.

This is an exact finiteness reduction. It is not yet a completed enumeration of effective curves.

## Upstream implementation lock

Michael Stoll's public verification repository contains the source used for the published Testa--Stoll computations:

```text
repo=https://github.com/MichaelStollBayreuth/Verification
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

The script constructs:

- the 48 singular points and known low-degree curves;
- the known-curve rank-64 intersection lattice and `PicL` model; the already-audited Testa--Stoll theorem identifies this with the full geometric Picard group;
- the canonical hyperplane class `HinPicL`;
- automorphism and Galois actions;
- negative-definite orthogonal lattices;
- `CloseVectors` searches for degree 2 and 4;
- the K3-quotient/lift machinery used to prove absence of degree-6 curves;
- numerical-effectivity necessary filters via intersection with the known curve configuration.

The degree-6 code also defines `liftcands_pr`, whose lift kernel has rank 44 and whose own estimator is proportional to

```text
const * bound^(44/2) = const * bound^22.
```

Thus the published machinery is a real implementation template, not merely a paper sketch. The audit record `audit.md` separates what is established by the code from the theorem that certifies fullness of the Picard lattice.

## Computational feasibility verdict

The direct statement

```text
FINITE_MATHEMATICAL_SEARCH=true
```

is certified by the reduction above.

The stronger statement

```text
NAIVE_CLOSEVECTORS_TO_D192_IS_TRACTABLE=true
```

is **not** justified.

The published low-degree computation succeeds because the norm bounds are tiny and, for degree 6, because a K3 quotient plus a 44-dimensional lifting kernel sharply structures the search. Extending the same close-vector procedure blindly across every even degree through 176/192 would face rapidly growing negative-definite balls. The source code itself exposes the `bound^22` growth in the lift stage.

No degree-176/192 exhaustive run is claimed in this suffix.

## Required symmetry/node reduction before production enumeration

A practical complete search should exploit all of the following before enumerating lattice vectors:

1. `Aut(S)` orbit reduction from the published order-1536 automorphism action;
2. the known exceptional/low-degree curve configuration as necessary intersection inequalities;
3. Testa--Stoll Lemma 21 incidence bounds (`C.E >= 8` for an unknown rational curve and `C.E >= 4` for a geometric-genus-one curve);
4. the already-classified degree `<=6` boundary/degenerate classes;
5. span/fibration information from Testa--Stoll Theorem 16 where it applies;
6. the unibranch/bijective-normalization hypothesis from Freitag--Salvati Manni, kept explicit throughout.

These are pruning conditions, not substitutes for an effectivity proof.

## Exact residual receivers

```text
R29-LG2=
  SymmetryReducedCompletePicardClassEnumerationForUnibranchGenus0DegreeLE176AndGenus1DegreeLE192

R29-LG2-EFF=
  EffectiveCurveCertificationForSurvivingNumericalPicardClasses

R29-LG2-MB=
  MultibranchAtNodeLowGenusCarrierLedgerOutsideFreitagSalvatiManniTheorem3_1
```

A complete positive-dimensional carrier exclusion needs all applicable effective classes removed and `R29-LG2-MB` handled separately. Even then isolated rational points are not excluded.

## Fresh audit result

The finite-lattice reduction, norm bounds, divisibility reconstruction, upstream code lock, rank-44 lift kernel, `bound^22` feasibility warning, effectivity firewall, and multibranch firewall received a fresh audit and pass. The only mathematical-precision repair was to distinguish the Magma construction of the known rank-64 lattice from the Testa--Stoll theorem that proves it is the full geometric Picard group. A stale controller field recording merged PR #1292 as pending merge was also synchronized.

## Stage routing verdict

This suffix upgrades W29-A from a literature theorem to an exact finite computational receiver, but does **not** close the 176/192 enumeration. The residual computation remains live while the independent foundation queue advances to 29-02d.

```text
LOW_GENUS_GLOBAL_DEGREE_BOUND=PASS_REUSED_PR1292
FINITE_PICARD_REDUCTION=PASS_AUDITED
UPSTREAM_EXACT_LATTICE_IMPLEMENTATION=LOCKED_AUDITED
FULL_D176_D192_ENUMERATION_COMPLETED=false
NAIVE_RUNTIME_TRACTABILITY_ESTABLISHED=false
EFFECTIVITY_CERTIFIED=false
MULTIBRANCH_CASES_COVERED=false
NEW_RESIDUAL_RECEIVER=R29-LG2
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
KEEP_STAGE29_NATIVE=true
ADVANCE_OTHER_FOUNDATION_SUFFIXES_AFTER_AUDIT=true
NEXT_ITEM_AFTER_PASS=29-02d
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
