# Stage33-05 R05 alternate-route exploration

Status: exploratory only. This branch must not modify Stage33 MAIN mathematical state, controller state, theorem credit, receiver credit, endpoint credit, or Stage33-05 closure flags.

## Purpose

Search for a materially different way to decide the current corrected-J2 arithmetic descent obstruction without requiring the full current `actual Cech overlap matrices -> Pic/2 defect -> integral Pic lift -> HS d2 -> Q-defined descent` route.

Current target only:

- corrected geometric J2 = `(f2,1)`;
- marked J2 = `[1,0]`;
- determine whether the corrected J2 admits the required Q-defined arithmetic Brauer preimage / equivalent exact descent datum;
- no inference of `HS d2=0` from geometric Galois fixedness alone.

## Independent lenses to test

1. **Q-defined provenance / reverse construction**
   Try to identify J2 as the image of an object already defined over Q (Kummer/Jacobian correspondence, 2-torsion/isogeny/Hom correspondence, algebraic cycle, norm correspondence, or another canonical Q-defined source). If an exact Q-defined source maps to marked coordinate `[1,0]`, use that as a candidate bypass of post-hoc descent.

2. **Symmetry / representation forcing**
   Compute the symmetry/Galois character of J2 and the relevant target of the Hochschild-Serre differential. Test whether equivariance forces `d2(J2)=0` because the corresponding eigenspace/character component of the target is zero. Do not infer this from invariance alone; the target representation must be computed exactly.

3. **Finite Galois-module cohomology**
   Replace local Cech overlap materialization by an exact finite Galois action on a certified Picard lattice, if available. Compute the relevant group-cohomology class directly and compare it to the current R5e/R5f obstruction.

4. **Direct Q-defined Brauer representative search**
   Search for a Q(X)-defined quaternion/symbol/Azumaya representative whose geometric restriction has marked coordinate `[1,0]` and whose divisor residues vanish. A successful explicit representative would certify the desired Q-defined preimage without requiring the current overlap route.

5. **Specialization / rigidity discriminator**
   Use good-reduction specializations only as a discriminator or uniqueness/rigidity aid: Frobenius action, Picard specialization, or Brauer pairing may distinguish the marked class or eliminate ambiguity. Specialization alone must not be promoted to Q-descent unless an exact lifting/rigidity theorem closes the implication.

## Repository arsenal rematch

Search Stage14-33 for reusable exact assets, not only Stage29 kernels. Prioritize:

- explicit Q/Q(i) twist and descent adapters;
- Kummer/Jacobian correspondences and marked-class maps;
- computed automorphism/Galois actions on Picard or transcendental lattices;
- exact quotient/eigenspace decompositions;
- previously source-locked Hochschild-Serre, Leray, Kummer-sequence, norm/residue, or Brauer constructions;
- finite-field specialization certificates with exact lifting consequences;
- exact symbolic/quotient compression patterns that can replace full matrix materialization.

## Firewalls

- Do not change `stages/stage33/controller.json` or the authoritative Stage33-05 repair state on this exploratory branch.
- Do not claim `HS d2=0` merely from geometric Galois fixedness.
- Do not reuse the historical Q-defined `ell_J2` / CSA whose full geometric CV class is zero.
- Do not promote a generic split module, auxiliary determinant parity, or partial Pic/2 vector to the actual compactified defect.
- Do not claim Stage33-05 reclosure, Q-defined descent credit, theorem credit, receiver credit, endpoint credit, or perfect-cuboid existence/nonexistence.
- A shortcut counts only if it has an exact comparison back to corrected J2 `(f2,1)` / marked `[1,0]`.

## Exit classes

The exploration should end in exactly one of:

- `ALT_ROUTE_EXACT_BYPASS_FOUND`: an exact alternate proof/certificate decides the corrected-J2 Q-descent question;
- `ALT_ROUTE_REDUCES_WALL`: an exact reduction replaces the full overlap computation by a strictly smaller invariant/computation;
- `COMMON_WALL_IDENTIFIED`: all tested independent routes provably reduce to the same unresolved obstruction, strengthening a Class-3/new-theorem diagnosis;
- `NO_MATERIAL_ALT_ROUTE_FOUND`: no materially different route survives exact firewalls.

Any positive result must be re-audited and explicitly backflowed to Stage33 MAIN; this PR itself is not authoritative Stage33 progress.
