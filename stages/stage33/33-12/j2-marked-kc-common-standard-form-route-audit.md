# Stage33-12 J2 marked-Kc common-standard-form route audit

Status: `ARCHITECTURE_AUDIT_ONLY_NO_CLOSURE_CREDIT`

Source snapshot: Stage33-12 PR #1463 head `bf5f0da0ecf8640b14ef8215a4079c292874a22f`.

This audit deliberately stops treating Stage33-12 as a search for a direct
dictionary between the Creutz--Viray presentation and the marked
transcendental basis.  Its replacement question is:

> Can the named CV class and each marked Kc candidate be converted, without an
> implicit semantic transfer, into the same geometric or cohomological standard
> form whose exact integral invariant distinguishes the three candidates?

The answer is **yes at the architecture level, with one unbuilt interface**.
The strongest class-2 design is

```text
named CV J2
  -> special-Brauer / mu_2 Cech datum
  -> twisted relative Picard torsor X_J2
  -> T(X_J2) = ker(J2:T(Kc)->Z/2)
  -> minimum norm 4, 8, or 12
  -> [0,1], [1,0], or [1,1].
```

The current degenerate-Clifford four-contact problem should be used only as a
finite constructor for the first two arrows.  A matching component fingerprint
or an unspecified nonzero twist is not enough.

## Fixed comparison target

The following data are already exact and are not recomputed here.

| Marked functional | Kernel reduced Gram matrix | Minimum norm |
|---|---:|---:|
| `[1,0]` | `diag(8,16)` | 8 |
| `[0,1]` | `diag(4,32)` | 4 |
| `[1,1]` | `[[12,-4],[-4,12]]` | 12 |

Source certificates:

- `j2-kc-transcendental-lattice-isometry.json` fixes
  `T(Kc)=<4> direct_sum <8>` but does not materialize a transcendental marking.
- `j2-kc-bfield-halfdual-target.json` fixes
  `beta1=t1/8`, `beta2=t2/16` in `(1/2 T*)/T*` and prevents replacing this
  quotient by the merely equicardinal group `(T*/T)[2]`.
- `j2-brauer-kernel-lattice-fingerprints.json` proves that minimum norm alone
  distinguishes the three index-two kernels.
- `j2-cv-to-discriminant-marking-obstruction.json` proves that the CV basis and
  semantic marked basis still differ by an unselected `GL(2,F2)` adapter.

## Major adapter-family census

In the table, A--F have the meanings required by the Stage33-12 audit request:
A = exact J2-side conversion; B = exact marked-Kc conversion; C = ability to
distinguish all three candidates; D = missing interface; E = constructible from
retained repo data; F = external theorem/input.

| Family | A: named J2 -> standard form | B: marked Kc -> same form | C | D: exact missing interface | E | F | Status |
|---|---|---|---|---|---|---|---|
| **R1. Special Brauer / twisted relative Picard / genus-one K3** | Abstractly exact: `J2` gives a nontrivial order-two Sha torsor `X_J2`; no explicit surface or overlap cocycle yet | Exact: each candidate gives its index-two kernel lattice | **Yes**: minimum norms `4/8/12` | Construct the named special-Brauer or twisted-Poincare Cech datum and materialize `X_J2`; then compute `T(X_J2)` | **Probably**: named CSA, graph lifts, split determinant, and four-contact locus are retained; only the assembly is missing | van Geemen §§1.2, 2.1; Huybrechts--Mattei Thm. 1.1, Def.-Prop. 2.8, Lem. 5.1 | **LIVE_ONE_INTERFACE** |
| **R2. Twisted Mukai / derived Hodge** | Not yet: a named B-field lift or a named twisted sheaf/Mukai vector is absent | Exact candidate B-fields and lattices are available; `rho(Kc)=20` is in the high-Picard range | **Yes only after the named lift**; the abstract twisted Mukai lattice by itself may relabel the three nonzero classes | Produce a special-Brauer/B-field lift compatible with the fixed marking, or a twisted sheaf whose Mukai vector certifies that lift | Not from present data without the same R1/R4 interface | Huybrechts--Stellari Thm. 0.4 and Def. 4.1 | **LIVE_ONE_INTERFACE**; **CANNOT_DISTINGUISH_THREE_CANDIDATES** if used without a named lift |
| **R3a. Ordinary `c1(A) mod 2` of the underlying Azumaya algebra** | A global Azumaya representative could be chosen, but ordinary Chern data of the underlying endomorphism algebra are Morita-insensitive to the required Brauer coordinate | No useful marked target beyond the existing three candidates | **No** | None: the proposed invariant discards the needed gerbe/PGL lifting obstruction | Repo data suffice to reject this formulation | The correct invariant lives in the `PGL_2 -> H^2(mu_2)` obstruction or twisted Chern character, not ordinary `c1(End(E))` | **REJECTED_EXACTLY** and **CANNOT_DISTINGUISH_THREE_CANDIDATES** |
| **R3b. PGL lifting obstruction / special-Brauer characteristic class** | Named function-field CSA exists; global splitting modules, transition matrices, determinant normalization, and its `mu_2` Cech class do not | Abstract `H^2(mu_2)/NS` target and marked transcendental functionals are fixed | **Yes**, if the Cech class is evaluated in the fixed K3 marking | Globalize the named CSA over a certified cover and compare the resulting `mu_2` class with the marked half-dual basis | **Probably finite explicit work** using the four resolved contact charts; not yet demonstrated | Huybrechts--Mattei Def.-Prop. 2.8 supplies the representation-independent twisted Chern character once a special-Brauer lift is fixed | **LIVE_ONE_INTERFACE** |
| **R4. K3-level Shioda--Inose / Kummer correspondence** | No explicit K3-level map carrying named J2 has been built | A complex Shioda--Inose structure exists abstractly for the rank-20 K3, but no Q-defined, integral, marked correspondence is fixed | **Only** if integral 2-primary transport is explicit; a rational Hodge correspondence does not suffice | Construct a controlled-field Nikulin/Shioda--Inose diagram and compute pullback of named J2 in the fixed integral marking | **No** with present repo data | Morrison's primitive-embedding criterion (Thm. 6.3; Cor. 6.4) and Ma's Kummer-sandwich Thm. 2.5 give existence species, not this marked arithmetic transport | **CLASS3_LEVEL_NEW_MATHEMATICS_REQUIRED** under the current interface |
| **R5. Degenerate Clifford admissible cover / Hermite inverse** | Exact component fingerprint `[q,1,q]`; transverse q-root glue is forced; the global theta characteristic and equality with named CV J2 remain unknown | Kernel fingerprints are exact; a recovered genus-one K3 can be compared directly | **Yes**, after the named global admissible cover produces `X_J2` | Resolve the four even tangencies, impose global sheet compatibility, identify the resulting cover with named CV J2, and recover the Hermite/torsor model | **Most likely yes**: this is a finite exact construction from retained formulas | van Geemen §8.7 gives the even-Clifford class and explicitly includes the three-component degenerate species; §§8.1--8.3 give the Hermite construction | **LIVE_ONE_INTERFACE**; concrete construction engine for R1/R3b |
| **R6. Direct period, cycle, or B-field evaluation** | Named CSA exists, but no representative topological cycles or CSA-to-cycle pairing map exists | The abstract marked basis `t1,t2` is fixed | **Yes in principle**, but current interface cannot perform even one certified bit | Materialize integral cycles and a compatible B-field evaluation | No new repo-only construction is visible | Standard comparison theory would only legitimize the same missing marked realization | **EQUIVALENT_TO_EXISTING_BLOCK** |
| **R7. Branch cohomology / good reduction / etale specialization / finite Kummer views** | They retain the named abstract class or its specialization | They retain the three marked candidates only after an unbuilt comparison | **No at the current level** | The same CV-to-marked cohomology adapter | Existing certificates already prove the equivalence/block | No additional theorem changes the missing marking | **EQUIVALENT_TO_EXISTING_BLOCK** |

The exact rejection in R3a is elementary and does not depend on a choice of
local splitting bundle.  The reduced-trace pairing identifies a degree-two
Azumaya algebra `A` with `A^dual`, hence `2*c1(A)=0`.  The Picard group of a K3
surface is torsion-free, so `c1(A)=0`; locally this is the familiar identity
`c1(End(E))=0`.  Thus ordinary `c1(A) mod 2` is zero for every one of the three
Brauer candidates.  The surviving characteristic class is instead the central
lifting/gerbe obstruction, which is precisely R3b.

## What is genuinely untried

There are three untried *implementations*, but only two genuinely different
large-scale standards.

1. **Special-Brauer/twisted-Picard standard form.**  The repo has the abstract
   Sha torsor target, but it has not constructed the named special-Brauer lift,
   twisted-Poincare overlap cocycle, or the resulting genus-one K3.  This is the
   main untried class-2 family.
2. **PGL lifting obstruction on the four resolved charts.**  This is a concrete
   characteristic-class implementation of item 1.  It is genuinely different
   from ordinary Azumaya `c1`, but it is not an independent final invariant.
3. **Explicit K3-level Shioda--Inose transport.**  This is genuinely different
   from the rejected elliptic-factor isogeny.  It is also the only remaining
   large family whose present cost is class 3 rather than finite adapter work.

Twisted Mukai/moduli-of-twisted-sheaves is a powerful verification and alternate
construction layer for item 1, not a fourth independent selector: without a
named B-field/special-Brauer input, it reproduces the same three unlabeled
twists.  Likewise, period, specialization, branch cohomology, and finite Kummer
views are already certified presentations of the same missing comparison.

## Strategic selection

The selected route is **R1 implemented by R3b and R5**:

```text
CV Azumaya algebra
  -> local splitting modules at the four resolved even contacts
  -> special-Brauer / mu_2 Cech orbit
  -> twisted relative Picard surface X_J2
  -> exact Neron-Severi or transcendental Gram matrix
  -> minimum norm selector.
```

This is preferable to starting with a global derived equivalence because it uses
the exact finite locus already isolated by the repo, while its output is the
standard genus-one K3 needed by the kernel-lattice comparison.  Derived Hodge
theory then becomes an independent verification of the final lattice equality,
not the source of an implicit semantic transfer.

## Minimum exact go/no-go experiment

This experiment is intentionally a route-family discriminator rather than a
single narrow leaf.

1. Prove locally that each of `t=1,-1,0,infinity` contributes exactly one binary
   normalized-sheet pairing.  Enumerate the at-most `2^4` raw pairing patterns.
2. Compute the explicitly proved global sheet-flip action.  Certify orbit
   coverage and disjointness before quotienting; do not trust canonical pruning
   without predecessor reconstruction.
3. For every admissible orbit, construct either:
   - a `mu_2` Cech/special-Brauer class from local splitting modules; or
   - a Hermite symmetric matrix and compactified genus-one K3 `X_epsilon`.
4. Compute an exact invariant for every orbit: preferably `T(X_epsilon)` and its
   minimum norm; an integral marked `H^2(mu_2)` coordinate is also sufficient.
5. Independently restrict the named CV algebra to the same resolved charts and
   identify its Cech orbit.  Equality from the shared `[q,1,q]` component
   fingerprint is forbidden.

**Success:** the named CV orbit is unique and has one of the three certified
minimum norms.  **Class-2 route failure:** exhaustive local/global coverage is
proved but the named CV datum is invariant on at least two admissible orbits
with different fingerprints, or the Cech datum cannot be promoted without an
additional global marked-cohomology theorem.  In that event, further local
fingerprint refinement is not progress.

## MAIN-batch decision budget

- **Batch 1:** exact local resolution, binary-pairing proof, global action, and
  complete orbit/coverage certificate.
- **Batch 2:** named CV local splitting modules and special-Brauer/Cech orbit;
  either select an orbit or certify non-separation.
- **Batch 3:** Hermite/twisted-Picard model and exact lattice fingerprint, or a
  formal class-2 failure certificate.
- **Batch 4 only if successful:** independent replay, source locks, and hostile
  semantic audit for Stage33-12 closure.

Thus **three MAIN batches should decide whether a class-2 winning path exists**;
four is the conservative budget for a certified successful closure.  This is a
go/no-go estimate, not a promise that the coordinate will be selected.

## Exact class-3 escalation contract

Stage33-12 must not be promoted to class 3 merely because one construction is
awkward.  Promotion is justified only after all of the following are committed
as exact negative/equivalence certificates:

1. the four-contact experiment exhausts every admissible local/global pairing,
   yet named CV data remain compatible with at least two different kernel
   fingerprints, or a proved global obstruction prevents construction of the
   special-Brauer/twisted-Picard object;
2. twisted Mukai/derived Hodge input is proved to require exactly the same
   absent named B-field/special-Brauer lift and supplies no independent selector;
3. the PGL lifting-obstruction route is either computed and non-separating or is
   proved equivalent to the same absent marked `H^2(mu_2)` comparison;
4. an explicit K3-level Shioda--Inose route is shown to require a new
   controlled-field, integral 2-primary transport theorem, rather than an
   available finite construction; and
5. branch, specialization, period/cycle, and finite Kummer variants remain
   source-locked to their existing equivalence/block certificates.

At that point the missing theorem must be stated explicitly as follows:

> Construct a functorial integral marked realization of the named CV
> Azumaya/gerbe class, compatible with Q-descent (or an explicitly controlled
> extension and descent), into either a B-field in `(1/2 T*)/T*` or an explicit
> twisted relative-Picard K3 `X_J2` with
> `T(X_J2)=ker(J2:T(Kc)->Z/2)` in the fixed Kc marking.

If producing that theorem, rather than executing finite algebra on retained
data, is necessary, the correct status is
`CLASS3_LEVEL_NEW_MATHEMATICS_REQUIRED`.

## External theorem locks

1. Bert van Geemen, [*Some remarks on Brauer groups of K3 surfaces*](https://arxiv.org/abs/math/0408006), Advances in Mathematics **197** (2005), 222--247.  Relevant locations: §1.2 (`Br=Sha` and torsor order/minimal multisection), §2.1 (`T_<alpha>=ker(alpha)`), §§8.1--8.3 (Hermite construction), §8.7 (even Clifford algebra and the reducible three-component degeneration).
2. Daniel Huybrechts and Dominique Mattei, [*The special Brauer group and twisted Picard varieties*](https://arxiv.org/abs/2310.04032), Documenta Mathematica (2025).  Relevant locations: Thm. 1.1 (cyclic extension parametrizing twisted relative Jacobian torsors), Def.-Prop. 2.8 (Azumaya-independent twisted Chern character for a special-Brauer lift in dimension at most two), Lem. 5.1 (`Br(S0) ~= Sha(S0/P1)` for an elliptic K3 with section).
3. Daniel Huybrechts and Paolo Stellari, [*Equivalences of twisted K3 surfaces*](https://arxiv.org/abs/math/0409030), Mathematische Annalen **332** (2005), 901--936.  Relevant locations: Thm. 0.4 (twisted Fourier--Mukai equivalence and integral twisted-Mukai Hodge isometry; converse in the stated high-Picard setting), Def. 4.1 (twisted Mukai vector).
4. David R. Morrison, [*On K3 surfaces with large Picard number*](https://eudml.org/doc/143091), Inventiones Mathematicae **75** (1984), 105--121.  Relevant locations: Thm. 6.3 (primitive embedding criterion for Shioda--Inose structure), Cor. 6.4 (large-Picard consequences).  These are existence statements over the complex/Hodge setting and do not provide the missing named arithmetic transport.
5. Shouhei Ma, [*On K3 surfaces which dominate Kummer surfaces*](https://arxiv.org/abs/0905.4107), Proceedings of the American Mathematical Society **141** (2013), 131--137.  Relevant location: Thm. 2.5 (Kummer sandwich for complex K3 surfaces with Shioda--Inose structure).  Again, this does not identify named J2 in the fixed integral Kc marking.

### Hypotheses and application dictionary

- **van Geemen §§1.2 and 2.1:** the comparison is over a complex elliptic K3
  surface with section.  Apply it to `Kc_C -> P1_C`; the geometric order-two
  class `J2_C` gives a genus-one torsor and its index-two transcendental kernel.
  This does not by itself descend the torsor or its marking to Q.
- **Huybrechts--Mattei:** the input is a complex projective K3 surface and a
  complete generically smooth linear system; Def.-Prop. 2.8 uses dimension at
  most two for independence of the Azumaya representative.  The Kc elliptic
  pencil supplies the linear system after base change to C.  The missing repo
  dictionary is the lift of the named CV CSA to their special-Brauer/twisted
  Picard datum, with Q-descent retained separately.
- **Huybrechts--Stellari:** the input is a complex projective twisted K3 with a
  chosen B-field lift.  The forward implication converts a twisted
  Fourier--Mukai equivalence into an integral twisted-Mukai Hodge isometry; the
  converse quoted in Thm. 0.4 requires the stated orientation and high-Picard
  hypotheses, met geometrically by `rho(Kc)=20`.  The theorem does not choose
  the missing B-field lift for named J2.
- **Morrison/Ma:** their Shioda--Inose and Kummer-sandwich conclusions are
  complex-geometric existence/correspondence statements.  They neither provide
  a Q-defined correspondence nor certify integral 2-primary transport of the
  named CV class, so they receive no marked-coordinate credit here.
- **van Geemen §§8.1--8.3 and 8.7:** the Hermite/even-Clifford formulas supply a
  construction dictionary.  Section 8.7 recognizes the reducible
  three-component species, but it does not remove the need to resolve the four
  tangencies, compactify to a smooth K3, and prove equality with the named CV
  algebra in this exact model.

## Firewalls retained

```text
J2 marked coordinate selected = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
Stage33 progress = 6/11
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
