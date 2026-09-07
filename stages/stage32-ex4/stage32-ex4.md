# Stage32EX4 — absolute marking / retained W-line decision roadmap

Status: **ACTIVE GOAL-DIRECTED MAINLINE**. Stage32EX4 is operationally independent from Stage32 MAIN authority until an explicit hostile-audited promotion adapter is accepted.

## Final target

Fix the current Stage32 O210/Q602 marking problem and decide the absolute identification

`delta_0inf=[P_0-P_infinity] -> one retained nonzero W-line -> one of residues {73,97,235}`

without choosing a convenient gauge representative by hand.

Stage32EX4 has exactly two mathematically terminal outcomes.

1. `ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED`
   - a source-bound marked datum fixes `delta_0inf` in the retained ordered `J(C0)[2]` / `W` coordinates;
   - the resulting nonzero W-line is independently replayable;
   - the exact retained line-to-residue adapter selects one member of `{73,97,235}`;
   - every coordinate/model change used in the construction is tracked and shown not to change the claimed absolute result.

2. `FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE`
   - for the explicitly frozen source package only, enumerate the admissible marked identifications and their ambiguity group;
   - prove that the remaining ambiguity acts nontrivially on the three nonzero W-lines, so no invariant contained in that fixed package can select a unique line;
   - identify the minimal additional datum whose choice would break that ambiguity.

The second outcome is **not** a theorem that no future literature/source/geometry can supply the missing marking. It closes only the named frozen source package and creates an exact re-entry interface for genuinely new data.

`FULL_TARGET_CLOSURE` is the umbrella decision state of EX4 only. Neither terminal outcome by itself excludes Q602, excludes O210, closes V6, closes Stage32, or proves anything about existence/nonexistence of a Perfect Cuboid.

## Fixed mathematical boundary to source-lock in EX4-00

The active lane must distinguish the following objects and must not identify them by notation alone:

- the Bolza genus-2 curve/model `C0`;
- its six hyperelliptic branch/Weierstrass points and the three distinguished V4 character pairs `Z1,Z2,Z3` when those labels are source-bound;
- the abstract class `delta_0inf=[P_0-P_infinity]` and the already recovered abstract character direction `chi_u -> Z3 -> delta_0inf`;
- `J(C0)[2]` as an abstract symplectic F2-module;
- the retained ordered basis `(e1,e2,r*e1,r*e2)` used by the Q602 finite calculation;
- the retained plane `W=span_F2{r*e1,r*e2}` and its three nonzero lines;
- the three Q602 residues `73,97,235`, each already carrying one retained image line `im(T-I)`;
- curve automorphisms written in explicit `x,y` coordinates;
- retained lattice/endomorphism generators such as `S,T,b3,b4`;
- any source pair such as Cecotti `B.7/B.8`;
- the conjugating/model-change isomorphism needed to pass between those presentations.

A trace, order, abstract group presentation, simultaneous-conjugacy orbit, or unmarked isomorphism is not an absolute marking.

## Dependency roadmap

### EX4-00 — source lock and typed marking target

Freeze the exact hostile-audited Stage32 boundary that EX4 may use as authority and separately register provisional/unreviewed candidate inputs.

At minimum source-lock:

- the hostile-audited `16 -> 3` Weierstrass/transvection result and the exact line-to-residue table;
- the hostile-audited Hperp/H-deck character result recovering `chi_u -> Z3 -> delta_0inf` while explicitly leaving the retained W-line unidentified;
- the exact retained `J[2]` basis, Weil pairing, `r` action, torsor plane `W`, and relevant V4/H marking;
- any post-1643 Cecotti/generator-orientation material only at its actual audit/authority status, never upgraded because it is convenient.

Produce a compact typed graph of every object and every currently justified arrow between them. Every later EX4 leaf must point to this graph.

Exit: `EX4_00_SOURCE_LOCK_COMPLETE`; no 3->1 arithmetic credit yet.

### EX4-01 — minimal absolute-datum specification

State exactly what extra datum would make the desired identification mathematically well-defined. The contract must say which of the following are required, and which are derivable:

- ordered/labelled six Weierstrass points or equivalent hyperelliptic coordinate normalization;
- base point and divisor-class convention for `J[2]`;
- symplectic basis of `J[2]`;
- identification of the self-Richelot/CM operator `r` in that basis;
- embedding of the V4 character plane `W` into `J[2]`;
- identification of `chi_u/Z3/delta_0inf` in the same marked module;
- orientation/order of any source generator pair;
- field/Galois/complex-conjugation convention when it changes the marking.

Compute the automorphism group of the data that remains unmarked. Record its action on the three nonzero W-lines. This establishes the exact ambiguity to be killed rather than accumulating more conjugacy invariants blindly.

Exit: one explicit `ABSOLUTE_MARKING_INPUT_CONTRACT` plus the current ambiguity group/action.

### EX4-02 — source inventory by marked content, not by topic

Inspect candidate sources/assets only for the exact marked data defined in EX4-01. Candidate families may include, when source-locked and applicable:

- Freitag--Salvati Manni theta/modular coordinates;
- Beauville cuboid/Bolza quotient coordinates;
- Stoll/Stoll--Testa marked box/Picard action;
- KRR/Bolza Jacobian/ppav descriptions;
- Cecotti explicit Bolza automorphisms and named lattice generators;
- retained Stage30/Stage33 marked `J[2]`, torsor, or equivariant-action assets;
- Galois/complex-conjugation data already source-bound in Stage32.

For every source record `PROVIDES`, `DOES_NOT_PROVIDE`, or `REQUIRES_ADAPTER` for each field of the EX4-01 contract. A search miss is not repository- or literature-wide absence.

Exit: finite source-to-required-datum matrix and one or more legal next construction lanes.

### EX4-03 — explicit curve/Weierstrass action anchor

Starting from an explicit Bolza curve model, compute the action of every candidate source automorphism on the six branch points and on the even-subset model of `J[2]`. Preserve the actual coordinate formulas and ordered point labels.

For Cecotti-type inputs, derive the branch-point permutation and differential trace directly from the explicit `x,y` formula. Do not identify `B.7/B.8` with retained `S,T` merely because group relations or orders match.

Produce an exact action table on `Z1,Z2,Z3` and, where justified, on `delta_0inf`.

Exit: source-bound curve-side marked action, still without claiming the retained F2^4 basis is identified.

### EX4-04 — retained ppav/J2 basis and operator anchor

Independently reconstruct the retained target side:

- ordered basis `(e1,e2,r*e1,r*e2)`;
- symplectic pairing;
- `W=ker(r mod 2)=span{r*e1,r*e2}` where source-locked;
- matrices/actions of retained generators actually needed by the active lane;
- the three nonzero W-lines and exact residue association.

The goal is a basis-level target object to which the curve-side action can be compared. Abstract `Aut(C0) ~= G` or `End(J) ~= M_2(...)` statements are insufficient.

Exit: independently replayable retained-side marked module.

### EX4-05 — solve the conjugator / model-identification problem

Find all symplectic/module isomorphisms from the source-side marked `J[2]` representation to the retained representation that respect every source-bound structure simultaneously, such as:

- Weil pairing;
- `r` or other distinguished endomorphism;
- V4/H character plane;
- explicit generator actions;
- ordered branch-point action;
- trace/orientation information;
- any source-bound Galois/complex-conjugation action.

Do **not** stop after finding one convenient conjugator. Enumerate all admissible conjugators or prove uniqueness modulo transformations acting trivially on the desired W-line.

The post1648 trace-orientation calculation may be used only at its actual authority status and only as one constraint; `+r` versus `-r` inner-conjugacy orbit selection does not itself fix the inner conjugating element.

Exit: exact admissible-conjugator set and residual ambiguity action on W-lines.

### EX4-06 — bind `chi_u / Z3 / delta_0inf` to a retained W-line

Transport the hostile-audited source-bound direction

`chi_u -> Z3={0,infinity} -> delta_0inf`

through every admissible conjugator from EX4-05.

There are two meaningful outcomes at this leaf:

- every admissible conjugator sends `delta_0inf` to the same retained nonzero W-line: absolute line identified;
- multiple W-lines remain possible: record the exact ambiguity subgroup/orbit and continue to EX4-08 unless a distinct source datum can reduce it.

A literal representative such as `phi2->S, phi6->T^-1` may be reported conditionally but cannot be promoted unless the source fixes that representative rather than only its inner-conjugacy orbit.

Exit: unique line candidate with proof, or exact residual line orbit.

### EX4-07 — exact Q602 residue adapter and independent replay

If EX4-06 gives a unique line, apply the already source-locked Q602 `16 -> 3` line-to-residue map. Produce one exact selected residue among `73,97,235` and replay it independently from:

1. source-side marked data;
2. the source-to-retained conjugator;
3. transported `delta_0inf` line;
4. retained line-to-residue table.

Then hostile-test coordinate invariance: changing only a permitted presentation must transport both the marking and residue labels coherently. A residue number in one arbitrary gauge is not an absolute arithmetic conclusion.

Exit: `ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED_CANDIDATE` if all adapters close.

### EX4-08 — ambiguity obstruction / minimal-new-datum branch

If a unique line is not obtained, do not end with “source insufficient.” Compute the residual ambiguity exactly.

Required tasks:

- enumerate all admissible identifications under the frozen EX4-00/02 source package;
- compute their orbit on the three nonzero W-lines;
- identify the subgroup fixing all presently source-bound structures;
- prove whether that subgroup is transitive on all three lines, swaps exactly two, or leaves one fixed;
- list the minimal additional datum that would reduce the orbit further: e.g. a marked generator, ordered branch pair, level structure, torsor trivialization, ppav basis vector, Galois orientation, or direct divisor/function representing one J[2] class.

If the frozen package is proved incapable of selecting a unique line, EX4 may propose terminal outcome `FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE`. This is a bounded source-package theorem only.

Exit: unique re-entry datum specification or bounded terminal obstruction candidate.

### EX4-09 — independent cross-check / circularity audit

Before terminal certification, verify that the selected marking or obstruction is not circular.

Check in particular:

- the source did not already choose the desired retained line/residue by convention;
- KRR/Cecotti/Stoll naming was not imported through an undocumented conjugation;
- the same Stage32 residue computation was not used both to choose and to verify the marking;
- complex conjugation/Galois/model changes do not generate an untracked alternative marking;
- a Stage33 or other-stage marked asset, if imported, has an exact semantic adapter to this Bolza/torsor/J[2] population.

Exit: `TERMINAL_CERTIFICATE_INPUTS_INDEPENDENT` or return to the leaf containing the circular/ambiguous adapter.

### EX4-10 — terminal decision certificate

Assemble exactly one replayable candidate.

**Positive marking certificate**

`ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED`

must verify the complete chain

`source marked datum -> curve/J2 marking -> retained basis -> W -> delta_0inf line -> one Q602 residue`.

**Bounded obstruction certificate**

`FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE`

must verify exhaustive admissible-identification coverage for the explicitly named source package and the nontrivial action of the residual ambiguity on W-lines. It must name the minimal missing datum/re-entry condition.

Only here may EX4 propose `FULL_TARGET_CLOSURE=true`. Positive EX4 closure means the marking problem is solved, **not** that the selected residue is eliminated. Negative EX4 closure means the frozen source package is exhausted, **not** that absolute marking is impossible in mathematics.

Exit: `AUDIT_READY_FULL_TARGET_CLOSURE` with exactly one terminal outcome.

### EX4-11 — hostile audit and Stage32 promotion boundary

Run `stage32ex4-audit` against the exact candidate head. A hostile-audit PASS establishes only the audited EX4 outcome.

For the positive terminal, Stage32 MAIN promotion requires a separate current-target adapter proving that the selected absolute line/residue still applies to the current O210/Q602 authority. Promotion may contract `[73,97,235]` to a source-bound selected residue only if the MAIN gate accepts that adapter. It does not automatically exclude Q602/O210.

For the bounded obstruction terminal, promotion is a route/anti-loop fact only: the named frozen source package should not be searched again without one of the listed new-data re-entry conditions.

No automatic merge.

## Parallel-lane plan after EX4-00

The following scratch lanes may run in parallel after the common type/source contract is frozen:

- `CECOTTI_EXPLICIT_AUTOMORPHISM_LANE`
- `FSM_THETA_LEVEL_STRUCTURE_LANE`
- `STOLL_MARKED_BOX_PICARD_LANE`
- `TORSOR_CHARACTER_TO_J2_LANE`
- `GALOIS_COMPLEX_CONJUGATION_ORIENTATION_LANE`
- `G12_CONJUGATOR_ENUMERATION_LANE`
- `AMBIGUITY_STABILIZER_LANE`

Scratch results are non-authoritative. Cross-lane use must label the dependency as provisional or hostile-audited. Successful leaves may be consolidated at an audit-ready checkpoint; freshness synchronization and broad CI belong at that checkpoint, not every micro-diagnostic.

## Batch/stop semantics

`stage32ex4-mainbatch` advances one coherent mathematical unit. A failed source, failed conjugator guess, or residual two/three-line orbit is `LEAF_BLOCKED` or an active residual queue, not EX4 exhaustion.

Do not repeat trace/order/conjugacy-class calculations once their exact information content has been shown incapable of reducing the ambiguity group. Re-entry into a closed subroute requires the named new marked datum.

Heavy/artifact-producing computation is not authorized by this roadmap alone.

## Credit and safety firewalls

- Gauge choice is not absolute marking.
- `delta_0inf in W` is not identification of one nonzero W-line.
- An inner-conjugacy orbit is not an explicit conjugating element.
- Matching group order, generator order, trace, or presentation is not a semantic adapter.
- A literal representative producing residue `73`, `97`, or `235` is conditional until that representative is source-bound.
- The post1648 Cecotti trace-orientation candidate must retain its actual audit status; EX4 bootstrap cannot self-promote it.
- An imported Stage33/other-stage `J[2]` marking needs an exact population/model adapter before use.
- `3 -> 1` by absolute marking is not `1 -> 0`; selecting a residue does not exclude Q602.
- A bounded source-package obstruction is not literature-wide or mathematical impossibility.
- `FULL_TARGET_CLOSURE` here is EX4 marking-decision closure only.
- Stage32 MAIN, Q602/O210, survivors `[73,97,235]`, receiver/theorem/endpoint credit, and Perfect Cuboid claims remain unchanged until separate promotion gates succeed.
- Merge requires explicit user authorization.
