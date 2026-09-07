# Stage32EX2 — V6 member reconstruction / linear-system decision roadmap

Status: **ACTIVE GOAL-DIRECTED MAINLINE BOOTSTRAP**. Stage32EX2 is operationally independent from Stage32 MAIN authority until an explicit hostile-audited promotion adapter is accepted.

## Final target

Fix the exact Stage32 V6 divisor class and decide the following linear-system question rather than stopping at numerical effectivity:

- `GENUINE_V6_GENUS1_MEMBER_ESTABLISHED`: construct or identify an actual **integral irreducible curve member in Picard class V6 of geometric genus 1**, with an exact equation/section/ideal or an equally replayable construction and all target-membership adapters verified; or
- `NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM`: prove, from an exhaustive description of the relevant linear system / fixed-moving decomposition / member geometry, that no integral irreducible V6 member of geometric genus 1 exists.

The intended attack direction is explicit member reconstruction first, because a genuine member would immediately resolve the existence side of the fixed EX2 decision problem. Failure to materialize a member from one chosen coordinate system, symmetry eigenspace, known-curve decomposition, or finite search is **not** the negative terminal outcome.

Current Stage32 context records the numerical facts `D^2=758`, `K.D=186`, `p_a(D)=473`, `h^0(O(D))>=294`, existence of an effective divisor by Riemann--Roch, and a nonnegative known-140 decomposition with 61 nonzero terms and total multiplicity 155. These are source context only until EX2-00 locks the exact artifacts used. In particular:

- `h^0>=294` does not exhibit one explicit section;
- an effective divisor need not be integral, irreducible, or genus 1;
- a known-curve decomposition exhibits an effective divisor in the class but does not classify the whole linear system;
- Picard-class equality does not identify a unique member.

`FULL_TARGET_CLOSURE` is the umbrella EX2 completion state and must carry exactly one of the two terminal outcomes above. A source-gap diagnosis, candidate equation, formal section, reducible divisor, fixed-component lemma, base-locus computation, finite search miss, or partial decomposition is intermediate work only.

## Dependency roadmap

### EX2-00 — source lock and exact target contract

Freeze the precise V6 target and every representation that later leaves may use:

1. the exact Picard64 / primitive-basis V6 vector and field;
2. the resolution / blow-down model in which divisor classes and known curves are represented;
3. the hostile-audited or otherwise explicitly scoped sources for `D^2`, `K.D`, `p_a`, Riemann--Roch effectivity, known-140 pairings/decomposition, exceptional data, and any automorphism action;
4. exact adapters between Picard coordinates, known-curve labels, modular/theta coordinates, projective box coordinates, Cox-like coordinates, or ideal presentations whenever one of those models is used;
5. the distinction between the line bundle/class `L=O(D)`, a section `s in H^0(L)`, its scheme divisor `(s=0)`, its strict transform, normalization, and any downstairs image.

Exit: a compact replayable target contract with no untyped coordinate/model transition. No member/exclusion credit yet.

### EX2-01 — line-bundle realization and section-source inventory

Determine which concrete descriptions of `H^0(L)` are actually source-bound rather than merely numerically known. Audit, separately:

- products/sums of equations of retained known curves whose divisor classes add to V6;
- modular or theta forms whose divisor class can be proved to be V6;
- restrictions of ambient projective forms to the box surface/resolution;
- ideal-sheaf / syzygy / graded-ring descriptions of sections;
- pullback or norm constructions from retained covers/quotients;
- Galois- or symmetry-generated section orbits, but only after the line bundle linearization/action is source-bound.

For every lane record exact input space, output object, field, divisor-class adapter, and whether it spans all of `H^0(L)` or only a subspace.

Exit: one or more executable section-construction lanes, or an exact typed blocker showing which adapter is missing. A blocker routes to another lane; it is not terminal success.

### EX2-02 — exact fixed-component extraction

Use intersection theory to identify **forced** fixed components of the complete linear system, not merely components appearing in one known effective decomposition.

For each retained irreducible curve `E` for which exact intersection data are available, test whether `D.E<0` forces `E` into every effective representative, determine the forced multiplicity by an exact iterative subtraction argument, and update the residual class after each justified subtraction.

Requirements:

- distinguish known negative curves from an exhaustive negative-curve classification;
- do not call a component fixed merely because it occurs in the 61-term known decomposition;
- preserve the field/model on every subtraction;
- recompute residual self/canonical intersections and dimension bounds only with justified formulas.

Exit: an exact fixed part `F` and moving residual `M=D-F` to the extent proved, plus an explicit list of unresolved possible fixed components. Full fixed-part classification requires an exhaustiveness argument, not just a bounded scan.

### EX2-03 — base locus and moving-system structure

Analyze the residual linear system `|M|` (or `|D|` if no fixed part is proved):

- dimension / lower bounds actually justified for `H^0(M)`;
- divisorial versus zero-dimensional base locus;
- restrictions to known curves and exceptional curves;
- whether the moving system is composed with a pencil or factors through a known fibration;
- generic-member statements available from Bertini-type input only after their hypotheses are verified on the exact model;
- symmetry decomposition of `H^0(M)` only when an exact linearization is available.

The key decision is whether the system is genuinely moving enough to admit an integral member, or whether its geometry forces reducibility/composition.

Exit: a typed moving-system contract identifying what a generic or selected section can legally be expected to produce.

### EX2-04 — finite-dimensional section reconstruction

Convert at least one section lane into an explicit finite linear-algebra problem.

Possible realizations include:

1. solve for ambient/projective forms with prescribed vanishing orders along source-locked divisors;
2. compute a basis of a graded piece modulo the exact surface ideal;
3. construct products of known component equations and then enlarge beyond their span by syzygy/quotient calculations;
4. isolate small symmetry eigenspaces/invariant subspaces and solve there;
5. reconstruct sections from divisor restrictions and compatibility/gluing constraints.

Every reconstruction must state whether it gives:

- the complete `H^0(L)`;
- a certified subspace;
- or only candidate sections.

Exit: explicit coefficients/equations/section vectors with a deterministic replay, or a precise rank/adapter obstruction.

### EX2-05 — actual member materialization

For every retained nonzero section candidate, materialize its divisor as a scheme on the exact source-bound model.

Verify:

- the section is nonzero in the actual section space, not merely before quotienting by the surface ideal;
- the divisor class is exactly V6, including any fixed part and exceptional corrections;
- no hidden common factor or automatic fixed component has been dropped;
- field of definition is recorded exactly;
- pullback/strict-transform/downstairs-image operations are not conflated.

Exit: one or more exact V6 member schemes suitable for geometric verification. A candidate polynomial without exact V6 membership is not an EX2 member.

### EX2-06 — component decomposition, integrality, and irreducibility

For each exact member scheme, determine its geometric component structure.

Use exact factorization/primary decomposition/saturation or a theorem with checked hypotheses to decide:

- reducedness;
- number of irreducible components over the relevant field and over an algebraic closure when required;
- multiplicities;
- embedded or exceptional components;
- integrality and irreducibility of the target component.

If every reconstructed member in a **properly certified subspace** is reducible, record only a subspace result. To conclude that every member of `|V6|` is reducible requires proof that the subspace is the complete section space or another population-wide argument.

Exit: either an integral irreducible V6 member candidate, or a rigorously scoped reducibility/fixed-component result.

### EX2-07 — geometric genus and normalization verification

For each integral irreducible V6 member candidate, compute or certify the normalization and geometric genus.

Reconcile:

- `p_a=473` from the fixed class;
- singularity/normalization defects on the actual member;
- ambient-surface singularities versus singularities in the smooth ambient locus;
- total delta only through exact local/global adapters.

A genus-1 result must be attached to the **same explicit member** whose V6 membership, field, integrality, and irreducibility were verified in EX2-05/06.

Exit: if geometric genus is exactly 1, produce a positive witness package and route to EX2-09. If not, retain the member as structural information and continue reconstruction/classification.

### EX2-08 — population-wide negative route

If explicit reconstruction repeatedly yields no genus-1 member, switch from search to an actual **linear-system-wide exclusion proof** rather than declaring failure.

A valid negative route must prove an exhaustive statement such as one of:

- exact fixed components force every V6 divisor to be reducible/nonintegral;
- the complete moving system is composed with a map whose members have incompatible genus/component structure;
- the complete section space is reconstructed and every member class is disposed by a finite or parameterized exact argument;
- every integral irreducible member of `|V6|` satisfies a source-bound geometric condition incompatible with genus 1.

Finite zero-hit searches, one eigenspace, one coordinate ansatz, one degree cutoff, or failure of a solver are never enough.

Exit: a complete exclusion certificate candidate, or a residual member family/parameter space that becomes the next work queue.

### EX2-09 — terminal decision certificate

Assemble exactly one terminal candidate.

**Positive witness certificate:**

- explicit equation/section/ideal or replayable construction;
- exact Picard class V6;
- correct field;
- actual member scheme;
- integral and irreducible;
- geometric genus exactly 1;
- all model/strict-transform/normalization adapters verified.

This proposes `GENUINE_V6_GENUS1_MEMBER_ESTABLISHED`. One verified member suffices; population-wide classification is not required.

**Negative linear-system certificate:**

- exact description/exhaustive control of the relevant complete linear system or a theorem applying to every integral irreducible V6 member;
- fixed/moving/base-locus claims proved on the full target population;
- every residual member family disposed;
- no hidden coordinate/model/field population change.

This proposes `NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM`.

Only here may `AUDIT_READY_FULL_TARGET_CLOSURE=true` be proposed.

### EX2-10 — hostile audit and Stage32 promotion boundary

Run `stage32ex2-audit` on the exact candidate head. PASS establishes only the audited EX2 claim ceiling.

Transfer to Stage32 MAIN requires a separate explicit current-target adapter. A positive EX2 member may become an actual-carrier input for EX1/EX3 only after its own exact target/member certificate is accepted. A negative EX2 terminal may close the fixed V6 genus-1 member question but does not by itself close Stage32, Q602/O210, FULL178, an endpoint, or Perfect Cuboid.

No automatic merge.

## Parallel research lanes inside EX2

The dependency labels above do not require a single serial implementation. After EX2-00, the following may run in parallel on scratch branches:

- `SECTION-COORDINATE-LANE`: ambient/modular/theta/graded-ring section construction;
- `FIXED-MOVING-LANE`: exact fixed components, base locus, residual system;
- `SYMMETRY-LANE`: linearized group action and small eigenspaces;
- `KNOWN-CURVE-LANE`: turn the known-140 decomposition into explicit equations and test whether it spans anything beyond the known reducible member;
- `IDEAL-SYZYGY-LANE`: explicit ideal/graded-module reconstruction;
- `NEGATIVE-LINEAR-SYSTEM-LANE`: prove population-wide reducibility or genus obstruction.

Scratch outputs remain provisional. Consolidate only retained successful leaves into the EX2 working PR, with exact assumptions and replay paths.

## Batch / stop semantics

`stage32ex2-mainbatch` advances one coherent mathematical unit. A technique failure is `LEAF_BLOCKED`, not EX2 exhaustion. A source-gap diagnosis must name the exact missing object and reopen condition, then route to a materially distinct lane.

Do not run broad/heavy computation merely because the roadmap names a coordinate or syzygy route. Heavy/artifact-producing work requires the repository authorization gate and storage policy.

## Credit and safety firewalls

- Numerical effectivity is not an explicit member.
- `h^0>=294` is not a section basis and does not imply a generic-member property by itself.
- The 61-term / multiplicity-155 known decomposition is one effective decomposition, not automatically the fixed part or the complete linear system.
- Picard-class equality does not identify a unique divisor member.
- A candidate polynomial is not a V6 member without an exact class/model adapter.
- A reducible or nonreduced V6 divisor is not the positive terminal.
- A member of the wrong field or geometric genus other than 1 is not the positive terminal.
- Failure to find a member in a finite ansatz/subspace is not the negative terminal.
- `NECESSARY_CONDITION_ONLY` and `BRANCH_EXCLUSION` are not `FULL_TARGET_CLOSURE`.
- Stage32EX2 does not by assertion modify Stage32 MAIN, Q602/O210, survivors `[73,97,235]`, receiver/theorem/endpoint credit, or Perfect Cuboid claims.
- Merge requires explicit user authorization.
