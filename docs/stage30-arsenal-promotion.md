# Stage30 Arsenal promotion — formal audited harvest

```text
REGISTRY=STAGE30-ARSENAL-FORMAL-R01
STATUS=FORMAL_AUDITED_CLOSED_STAGE_HARVEST
SOURCE_STAGE=Stage30
SOURCE_STAGE_CLOSED=true
SOURCE_MAIN_SNAPSHOT=88ad3370f3abade40c20ff0ce8622474976f5d6f
FINAL_AUDIT_VERDICT=PASS_STAGE30_CLOSED_NONOBSTRUCTIVE_MODULAR_KERNEL
FORMAL_SELECTOR_ADDITIONS=0
ROUTER_ONLY_WEAPON_COUNT=3
FORMAL_WORKFLOW_COUNT=2
```

This is the formal Arsenal harvest for the closed and hostile-audited Stage30 finite-group / equivariant-identification / Galois-descent band. It is reverse-indexed from the Stage30-09 immutable final reproducibility surface, Stage30-10 hostile audit, and the audited merged checkpoints that supplied the load-bearing sources. It does not replay Stage30 history sequentially.

The promoted content is the reusable method. Concrete Stage30 `S4`, `K8`, coordinate labels, cocycle name, sign patterns, orbit counts, and zero-elimination outcome remain provenance unless explicitly listed as hypotheses/examples.

## Authority and final audit provenance

```text
final_surface_result=stages/stage30/30-09/result.md
final_surface_result_blob_sha=8b7121f62679edf77e193eba04ccebf199733080
final_certificate=stages/stage30/30-09/final-certificate.json
final_certificate_blob_sha=f1e8b8b823b3f7cce32cf78ec6bec76b875e63e1
final_verifier=stages/stage30/30-09/verify_stage30.py
final_verifier_blob_sha=58e41b524bf134a863696fea5184a45ff4b73961
final_hostile_audit=stages/stage30/30-10/audit.md
final_hostile_audit_blob_sha=9ed229c7078728d21c8152882f1182332682b1af
final_audit_state=stages/stage30/30-10/audit-state.json
final_audit_state_blob_sha=5c36fc39d63c237e80f329b8df66b7f2cb2d0fec
```

Final hostile audit accepted the load-bearing chain:

```text
30-05 common Q(i) model
-> 30-06 source-derived residual action and cocycle
-> 30-06C exhaustive semilinear verification
-> 30-07 exhaustive marked-defect transport
-> 30-08 physical-scope adapter
-> 30-09 immutable final checker surface
-> 30-10 hostile PASS / Stage30 CLOSED
```

Adapter closure did not imply endpoint closure: the parent modular route remained AMBER and no physical endpoint exclusion was proved.

# 1. Formal Arsenal promotions

## S30-W01 — concrete finite equivariant identification with source anchor

**Weapon type:** `FINITE_EQUIVARIANT_ACTION_IDENTIFICATION`

### Reusable statement / procedure

When two finite constructions are suspected to realize the same abstract finite symmetry, do not identify them from abstract group isomorphism, matching orders, or generator names alone.

A reusable exact adapter is obtained by:

```text
1. reconstruct both concrete finite groups/actions from source data;
2. freeze canonical element/action conventions;
3. exhaust the finite equivariant bijection/relabeling space when feasible;
4. treat surviving bijections only as finite-action candidates;
5. source-lock a common geometric/moduli/algebraic model linking the two realizations;
6. derive the actual source action on that common model;
7. compute and verify the resulting action map, kernel, image and stabilizers;
8. only then grant source-target equivariant adapter credit.
```

The Stage30 hostile sequence is important: 24 finite equivariant relabelings survived an exhaustive finite search, but none received source-geometric adapter credit until a common `Q(i)` model was source-locked and the actual action projection was derived.

### Hypotheses

- both finite actions are explicit and exact;
- the relevant finite candidate space is exhaustively enumerable or otherwise exactly classified;
- source and target labels/bases are pinned;
- the intended semantic identification is backed by a common source model or an explicit source-derived map;
- kernel/image/stabilizer claims are checked on the concrete actions.

### Applicability

- two realizations of a finite group acting on different combinatorial/geometric/module objects;
- modular/arrangement action comparison;
- finite source-target coordinate identification;
- exact generator/relabeling diagnostics where semantic selection requires more than a group-theoretic match.

### Source locks

```text
finite_action_source=stages/stage30/30-02C/action-tables.json
finite_action_source_blob_sha=d2ae114d859283b30ecfe3bf84448c8b3f6170ec
common_anchor=stages/stage30/30-05/common-anchor.json
common_anchor_blob_sha=8dabd493ba107142898ada88f9e8c0a2371fadf0
final_action_reference=stages/stage30/30-09/action-tables.json
final_action_reference_blob_sha=e179d56a621b4685cef9b3dea43e032bf5be1904
final_equivariant_map=stages/stage30/30-09/equivariant-map.json
final_equivariant_map_blob_sha=cc572f22e6ee42a8b145e13b0bee23bf870bebf0
```

### Audit / certificate provenance

- PR #1329: exact concrete finite action certificates; abstract `S4` shortcut explicitly rejected.
- PR #1330: exhaustive finite identification; all finite relabeling candidates retained only as finite-action candidates.
- PR #1331: hostile audit supplied the common source model and gauge-invariant action projection.
- Stage30-09 final checker independently reconstructs `SL2(Z/4)`, `PSL2(Z/4)`, the concrete kernel, and final action wrappers.
- Stage30-10 final hostile audit accepted the entire chain.

### DO_NOT_USE_FOR

```text
abstract G ~= H => semantic adapter
matching group orders => identification
matching generator names => geometric identification
finite relabeling survivor => source-derived map
gauge representative labels => canonical labels
adapter closure => endpoint/route closure
finite exhaustive match => unconditional theorem outside the enumerated finite objects
```

### Existing Arsenal overlap

- **Stage33 `S33-PW05`: specialization, not duplicate.** `S30-W01` is the stable general pattern for concrete finite equivariant identification. Stage33 PW05 adds module-specific intertwiner/extension/reachability calculations and remains provisional as a stricter specialization.
- **Stage32 `S32-PW05`: complementary, not duplicate.** Stage32 PW05 assumes a validated finite action and uses it to reconstruct missing invariant pairing values by orbit propagation; it does not solve source-target semantic identification.
- No existing formal selector or stable weapon covers the common-anchor firewall at this exact abstraction level.

### Registration

```text
FORMAL_ARSENAL=true
FORMAL_SELECTOR=false
ROUTER_ONLY=true
```

---

## S30-W02 — quadratic semilinear Galois descent cocycle adapter

**Weapon type:** `SEMILINEAR_GALOIS_DESCENT_ADAPTER`

### Reusable statement / procedure

Let `L/K` be a quadratic extension with nontrivial automorphism `sigma`, let a finite group `G` act on an object over `L` through exact representatives `alpha_hat(g)`, and let Galois act on the finite symmetry by an automorphism `theta` of `G`.

A source-locked descent adapter is certified by an explicit cocycle/deck element `c_sigma` satisfying the quadratic cocycle condition and the semilinear compatibility

```text
sigma(alpha_hat(g))
  = c_sigma * alpha_hat(theta(g)) * c_sigma^-1
```

for every relevant `g`, together with exact closure/multiplication checks for the representatives. Generator-level identities are useful derivation data but exhaustive finite verification is the certificate when `G` is small enough.

### Hypotheses

- a source-derived action over `L`, not an arbitrary projectively equivalent lift;
- explicit `sigma`, explicit `theta`, and explicit `c_sigma`;
- the cocycle identity for `c_sigma` is checked;
- the semilinear relation is checked on the full finite group or proved from a complete presentation with verified relations;
- representative multiplication/projective ambiguity is controlled exactly.

### Applicability

- descent of finite group actions from a quadratic extension;
- sign/deck-group lifts of a residual finite symmetry;
- semilinear source-target adapters in Galois-equivariant geometry;
- exact finite descent certificates before transporting arithmetic markings.

### Source locks

```text
semilinear_spec=stages/stage30/30-06/semilinear-spec.json
semilinear_spec_blob_sha=c699105666cd07ff9eded5dd60cf1896c25eaf4f
semilinear_certificate=stages/stage30/30-06C/semilinear-certificate.json
semilinear_certificate_blob_sha=23338d990bc337f456967a5ab8d3b6d81a1b1769
final_galois_wrapper=stages/stage30/30-09/galois-cocycle.json
final_galois_wrapper_blob_sha=ec8d5d7320bf4fc08be490eac81c635c1e283e98
```

### Audit / certificate provenance

- PR #1332 hostile audit repaired the action to a source-derived lift before accepting the cocycle derivation.
- PR #1333 independently reconstructed the finite group, verified the automorphism, the cocycle identity, all group representatives, all 24 semilinear identities, and all 576 multiplication pairs in the locked Stage30 instance.
- Stage30-09 binds that separately audited exhaustive certificate rather than pretending to re-prove it.
- Stage30-10 hostile audit accepted the final certificate chain.

### DO_NOT_USE_FOR

```text
arbitrary projective lift with the right abstract group
generator-only numerical spot check when exhaustive verification is feasible
cocycle name or sign pattern copied across a changed marking/source model
finite semilinear action => elliptic-curve/Q-rational point descent
finite action descent => global arithmetic class existence
c_sigma == some unrelated defect/kernel element without an explicit object adapter
adapter closure => endpoint closure
```

### Existing Arsenal overlap

- **Stage33 `S33-PW07`: downstream specialization/adjacent, not duplicate.** PW07 uses a common cohomological/translation-valued cocycle to validate a genus-one torsor and Brauer semantics. `S30-W02` is the earlier generic finite-action descent layer; it does not supply the torsor/Brauer dictionary.
- **Stage33 `S33-PW05`: adjacent.** PW05 checks finite-module source-target compatibility after explicit actions are given; `S30-W02` certifies how a finite action itself descends across a quadratic Galois extension.
- No stable formal Arsenal card currently captures this quadratic semilinear finite-action descent contract.

### Registration

```text
FORMAL_ARSENAL=true
FORMAL_SELECTOR=false
ROUTER_ONLY=true
```

---

## S30-W03 — marked finite-defect equivariant transport and descent classification

**Weapon type:** `MARKED_DEFECT_EQUIVARIANT_DESCENT_CLASSIFIER`

### Reusable statement / procedure

Given a finite defect/state set `D`, a finite symmetry group `G`, a Galois action on the marked data, and an explicit adapter `phi` from the defect representation to a target/sign/deck representation:

```text
1. enumerate every defect/state in D;
2. compute its exact image under phi;
3. compute G-orbits and stabilizers as ordinary finite-action data;
4. verify phi is equivariant on all required pairs (g,d) in G x D;
5. compute the actual marked/twisted Galois descent equivalence relation;
6. classify arithmetic marked classes from that relation;
7. keep ordinary G-orbits and marked arithmetic classes separate unless equality is proved.
```

The reusable lesson is the firewall: an ordinary finite orbit partition is not automatically the arithmetic marked-class partition. The descent cocycle and marking can refine or change the equivalence relation.

### Hypotheses

- the complete finite defect set is known;
- its finite action and the target action are exact;
- the adapter `phi` is explicit and verified on the full finite population or by a complete proof;
- the relevant Galois/twisted equivalence relation is source-locked;
- class/stabilizer computations are exact.

### Applicability

- finite obstruction/defect sets transported between equivalent models;
- marked torsion/deck/sign states;
- finite arithmetic descent classes where unmarked orbit data are insufficient;
- exhaustive source-target classification after a semilinear descent adapter is available.

### Source locks

```text
defect_source=stages/stage30/30-07/defect-classification.json
defect_source_blob_sha=0a42601ec958f0e914b7e6be5f3461560657e644
final_defect_reference=stages/stage30/30-09/defect-classification.json
final_defect_reference_blob_sha=02257e31f9bcdcad801b1fd4581d40b3cb746000
final_equivariant_map=stages/stage30/30-09/equivariant-map.json
final_equivariant_map_blob_sha=cc572f22e6ee42a8b145e13b0bee23bf870bebf0
```

### Audit / certificate provenance

- PR #1334 hostile audit independently reconstructed the complete finite defect set, the explicit target adapter, all residual-action/defect equivariance pairs, ordinary orbits/stabilizers, and marked descent classes.
- Stage30-09 final checker independently re-derives every finite target image and verifies the marked-class count/firewalls.
- Stage30-10 hostile audit accepts the classification as part of the closed adapter kernel.

### DO_NOT_USE_FOR

```text
ordinary orbit membership => arithmetic equivalence
same stabilizer size => same marked class
finite defect image => impossibility/elimination
concrete Stage30 defect count/order/orbit sizes as universal constants
concrete Stage30 adapter formula as universal formula
finite classification => theorem outside the enumerated defect population
zero/nonzero elimination count => endpoint closure
```

### Existing Arsenal overlap

- **Stage33 `S33-PW05`: specialization/adjacent.** PW05 computes reachable images/intertwiners for finite modules. `S30-W03` adds the explicit distinction between ordinary group orbits and Galois-marked arithmetic equivalence on a complete defect set.
- **Stage32 `S32-PW05`: complementary.** Orbit reconstruction of invariant values is not marked arithmetic-class classification.
- No formal stable Arsenal card currently owns this marked-orbit/descent firewall.

### Registration

```text
FORMAL_ARSENAL=true
FORMAL_SELECTOR=false
ROUTER_ONLY=true
```

# 2. Workflow formal registrations

## S30-WF01 — FINITE_EQUIVARIANT_IDENTIFICATION_AUDIT

**Class:** Workflow formal registration.

```text
concrete finite actions
-> exhaustive candidate identification/relabeling
-> candidate set only
-> common source model / source-derived action
-> exact kernel/image/intertwining checks
-> semantic adapter credit
```

This workflow formalizes the hostile Stage30 lesson that finite equivariance is necessary but may not be sufficient for semantic identification.

**Overlap:** Stage33 provisional `V4_EQUIVARIANT_TRANSPORT_AUDIT` is a module-specific specialization. It should not become a second generic workflow at final Stage33 promotion unless it adds a genuinely different contract beyond intertwiners/reachability.

## S30-WF02 — IMMUTABLE_FINITE_CERTIFICATE_REPLAY

**Class:** Workflow formal registration.

Stage30-09's final surface pins immutable mathematical artifacts by Git blob SHA, deliberately excludes mutable controller state from permanent mathematical input locks, independently reconstructs cheap finite objects, and binds separately audited exhaustive subcertificates rather than silently claiming to have recomputed them.

Reusable workflow:

```text
pin immutable mathematical sources
-> independently reconstruct cheap structural invariants
-> bind audited expensive/exhaustive subcertificates by immutable provenance
-> cross-check derived wrappers/firewalls
-> final hostile audit
```

**Overlap:** this formally subsumes the generic immutable-pinning/replay portion of Stage32 provisional `CANONICAL_EVIDENCE_CHAIN`. Stage32's additional numerical-candidate replay and semantic-promotion ladder remain separate provisional workflows.

# 3. Stage30-specific / non-promoted material

The following remain provenance/examples and are not formal weapons by themselves:

- the concrete order-24 Stage30 arrangement/modular action tables and their element IDs;
- the facts `|SL2(Z/4)|=48`, `|PSL2(Z/4)|=24` as standalone Arsenal cards;
- the concrete `V_mod` IDs and exact Stage30 sign-deck patterns;
- the concrete `Q(i)` cuboid/modular model and chosen `X(4)` gauge as a universal model;
- the concrete cocycle label `delta_a3` and the Stage30 generator formulas;
- the eight concrete `K8` defect rows, their endpoint sign images, orbit multiplicities, singleton marked classes, and zero elimination count;
- the Stage30 physical-endpoint/open-locus facts;
- `R29-KUM5` discharge and the post-Stage30 kernel-count delta as reusable mathematical weapons.

These facts are source/certificate provenance for the procedures above. They are not transported to unrelated finite groups or Galois descent problems without a fresh adapter.

# 4. Formal router/selector disposition

```text
FORMAL_ROUTER_WEAPONS=S30-W01,S30-W02,S30-W03
FORMAL_WORKFLOWS=S30-WF01,S30-WF02
FORMAL_SELECTOR_ADDITIONS=NONE
REASON=adapter/procedure weapons do not state a global population bound or endpoint theorem
STAGE30_SOURCE_MUTATED=false
ENDPOINT_CLOSURE_CLAIM=false
PERFECT_CUBOID_CONCLUSION=NONE
```

Stage30 is CLOSED and audited, so these entries are formal stable Arsenal content rather than provisional active-stage cards. Reuse still requires exact hypothesis and source-target adapter matching.