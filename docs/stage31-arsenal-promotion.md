# Stage31 Arsenal promotion — formal audited harvest

```text
REGISTRY=STAGE31-ARSENAL-FORMAL-R01
STATUS=FORMAL_AUDITED_CLOSED_STAGE_HARVEST
SOURCE_STAGE=Stage31
SOURCE_STAGE_CLOSED=true
SOURCE_MAIN_SNAPSHOT=88ad3370f3abade40c20ff0ce8622474976f5d6f
FINAL_AUDIT_VERDICT=PASS_STAGE31_CLOSED_DIRECT_QUARTIC_CERTIFICATION
FORMAL_SELECTOR_ADDITIONS=0
ROUTER_ONLY_WEAPON_COUNT=3
FORMAL_WORKFLOW_COUNT=1
```

This is the formal Arsenal harvest for the closed and hostile-audited Stage31 quartic-integral-point certification work. The harvest was reverse-indexed from the final closed controller, `31-01/result.md`, source locks, the birational/integral-point/Mordell--Weil/reconstruction certificates, and the final `31-06` hostile audit. Stage31 history was not reread sequentially.

Concrete Paper-E coefficients, point lists, `(p,q)=(11,71)`, reconstructed edge lengths, run IDs, and kernel-count deltas remain provenance unless needed to identify the audited source. The promoted content is the reusable method.

## Authority and audit provenance

```text
controller=stages/stage31/controller.json
controller_blob_sha=f2fe655f623f519705f8acd04d9e0b6486af2b35
source_lock=stages/stage31/source-lock.md
source_lock_blob_sha=ae08801fa9629c8b9e5b84003f5050d24fcf72b7
main_result=stages/stage31/31-01/result.md
main_result_blob_sha=5c87c63da39535962dc063ec568260279ee0ea3c
final_hostile_audit=stages/stage31/31-06/audit.md
final_hostile_audit_blob_sha=149c9025752a8ee39f6a57f45d26f58385edf412
final_audit_state=stages/stage31/31-06/audit-state.json
final_audit_state_blob_sha=25fb3c509926da9dfdaef6ca38c5731369073c3f
```

Final hostile audit preserved the three central firewalls:

```text
birational equivalence != integral-point equivalence
finite/thin family closure != global endpoint closure
CAS output alone != independently locked proof surface
```

It also certified that the direct quartic integral-point proof does not depend on an unproved quartic-to-elliptic integrality transfer, and that the Mordell--Weil result is an independent full-group/saturation cross-check rather than a hidden completeness assumption.

# 1. Formal Arsenal weapons

## S31-W01 — exact genus-one quartic <-> elliptic birational adapter

**Weapon type:** `GENUS_ONE_QUARTIC_ELLIPTIC_BIRATIONAL_ADAPTER`

### Reusable statement / procedure

For a genus-one quartic and an elliptic model intended to describe the same rational curve, certify the adapter at the rational-function level rather than by model labels alone:

```text
1. derive explicit forward rational functions C -> E;
2. derive an explicit inverse on a stated open E -> C;
3. verify the defining polynomial identities exactly;
4. prove inverse denominators are nonzero on the claimed open, or state the excluded locus;
5. enumerate every exceptional source/target point needed to extend the rational maps;
6. check exact round trips on independently certified points when available;
7. record integrality as a separate obligation rather than inheriting it from birationality.
```

Stage31's concrete map is provenance only; the reusable weapon is the requirement that the inverse denominator and exceptional locus be part of the adapter certificate.

### Hypotheses

- an exact genus-one quartic model and exact elliptic model;
- explicit rational maps in both directions on stated opens;
- exact algebraic identity verification;
- complete denominator/exceptional-locus accounting for the claimed rational equivalence.

### Applicability

- quartic genus-one curves converted to Weierstrass form for Mordell--Weil analysis;
- independent model cross-checks;
- rational-point transport where integral/S-integral structure is handled separately.

### Source locks

```text
primary_path=stages/stage31/31-01/birational-map.json
primary_blob_sha=973f61023b7b0b5d322168331b3ecc68a281ca25
independent_verifier=stages/stage31/31-01/verify_stage31.py
independent_verifier_blob_sha=92b956d570367d145d87692ae25c0da5da312233
```

### Certificate / audit provenance

- `31-01/result.md` supplies the exact derivation and maps.
- `verify_stage31.py` independently checks the polynomial derivation, forward images, inverse images, and exceptional finite point handling using exact rational arithmetic.
- `31-06/audit.md` hostile-rechecks the map while explicitly refusing integrality credit from birationality alone.

### DO_NOT_USE_FOR

```text
birational equivalence => integral-point equivalence
birational equivalence => S-integral equivalence
matching j-invariant/model label => explicit adapter
ignoring inverse denominators or exceptional points
elliptic integral-point list => quartic integral-point completeness without a separate integral adapter
birational adapter closure => parent route/global endpoint closure
```

### Existing Arsenal relation / placement

- Distinct from formal `S30-W01`: that card identifies concrete finite group actions; this card certifies rational maps between genus-one curve models.
- Distinct from provisional `S33-PW04`: that card transports marked basis/dual/adjoint coordinates, not rational points between algebraic curves.
- Related to older Stage14 elliptic-fiber bridge cards, but those are counting/fiber-degree interfaces rather than a fixed-curve exact rational map with denominator/exceptional-locus certification.

```text
FORMAL_ARSENAL=true
FORMAL_SELECTOR=false
PLACEMENT=ROUTER_ONLY
```

---

## S31-W02 — direct integral-model completeness transfer

**Weapon type:** `DIRECT_INTEGRAL_MODEL_COMPLETENESS_TRANSFER`

### Reusable statement / procedure

When a convenient birational elliptic model does not preserve integrality transparently, move the completeness problem through an explicitly *integrally equivalent* auxiliary model instead.

Suppose an integral source model `C(Z)` maps injectively to an auxiliary integral model `Q(Z)` and the image is characterized by an exact arithmetic predicate `P` such as divisibility or congruence. Then

```text
complete Q(Z)
+ exact image predicate P
+ exact inverse on P
=> complete C(Z).
```

Reusable procedure:

```text
1. construct an exact integer/scaled auxiliary model Q;
2. prove the source-to-Q integer map;
3. prove an iff image characterization inside Q(Z), e.g. m | U;
4. certify a complete integral-point enumeration of Q(Z) with a proof-capable method;
5. restore any quotient/sign symmetries omitted by the routine;
6. apply the exact image filter and inverse;
7. exact-replay every retained source point.
```

This is the load-bearing Stage31 repair: an unsafe rational birational-integrality implication is bypassed by a direct integral equivalence plus a complete quartic enumeration.

### Hypotheses

- exact integral source and auxiliary models;
- an exact integral map with an iff image condition;
- complete proof-capable enumeration of the auxiliary model's integral points;
- all sign/symmetry conventions and exceptional image cases accounted for;
- exact inverse reconstruction on the filtered image.

### Applicability

- quartic/hyperelliptic integral-point problems where a CAS routine operates naturally on a scaled model;
- Diophantine reductions where a rational birational map is useful geometrically but unsafe for integral completeness;
- integral-point certification through exact divisibility/congruence image conditions.

### Source locks

```text
integrality_path=stages/stage31/31-01/integrality-transfer.md
integrality_blob_sha=1fca126abdcd36cbe9a12ce7b7ff856a196a4036
integral_points_certificate=stages/stage31/31-01/integral-points-certificate.json
integral_points_certificate_blob_sha=69eb32c5d93a9cee569e7ccd3767c4ac983421cc
independent_verifier=stages/stage31/31-01/verify_stage31.py
independent_verifier_blob_sha=92b956d570367d145d87692ae25c0da5da312233
```

### Certificate / audit provenance

- `31-01/integrality-transfer.md` proves the exact scaled integer equivalence and image divisibility condition.
- `integral-points-certificate.json` locks the proof-capable complete quartic enumeration, software/routine semantics, artifact provenance, and absence of heuristic completeness substitutes.
- `verify_stage31.py` checks every certified source and auxiliary point exactly.
- `31-06/audit.md` hostile-repairs the wording so the credit is exactly the direct scaled integral equivalence, not quartic-to-elliptic integrality.

### DO_NOT_USE_FOR

```text
arbitrary rational birational map as an integral adapter
bounded point search as completeness
sampled/heuristic height bounds as completeness
CAS point list without proof-capable routine semantics
one-way divisibility condition without an iff inverse
complete Q(Z) => complete unrelated C(Z)
finite curve completeness => global endpoint closure
```

### Existing Arsenal relation / placement

No existing formal Arsenal mathematical card owns this direct integer-model completeness transfer. Formal `S30-WF03` supplies the generic semantic credit firewall, but not the mathematical iff image transfer itself.

```text
FORMAL_ARSENAL=true
FORMAL_SELECTOR=false
PLACEMENT=ROUTER_ONLY
```

---

## S31-W03 — complete auxiliary-point set -> exact parameter-family reconstruction

**Weapon type:** `COMPLETE_POINT_SET_PARAMETER_PULLBACK`

### Reusable statement / procedure

A complete point set on an auxiliary curve closes an original Diophantine family only after an exact, exhaustive pullback through the family dictionary.

```text
1. start from a certified complete auxiliary point set;
2. enumerate every relevant sign/branch representative;
3. apply the exact branch dictionary back to source parameters;
4. enforce every source hypothesis exactly: integrality, sign/order,
   coprimality, primality or other branch restrictions as applicable;
5. reconstruct the original mathematical object exactly;
6. apply all remaining target predicates exactly;
7. account for every auxiliary point/branch, including degenerate rejects;
8. state closure only for the exact source family represented by the dictionary.
```

The reusable content is not the Stage31 prime values; it is the exhaustive accounting contract from a complete auxiliary curve solution set back to the source family.

### Hypotheses

- complete auxiliary point set;
- exact and source-locked branch/pullback dictionary;
- explicit source-family hypotheses;
- complete accounting of all auxiliary points and branch degeneracies;
- exact reconstruction and final predicates.

### Applicability

- Diophantine families reduced to integral/rational points on auxiliary curves;
- thin or parametrized subfamilies where curve points must be converted back to original integer parameters;
- exact family exclusions where missing one sign/branch would invalidate closure.

### Source locks

```text
reconstruction_path=stages/stage31/31-01/reconstruction-ledger.json
reconstruction_blob_sha=0b829208f4d2b9a67538adc4617af38addbeb00e
source_lock_path=stages/stage31/31-01/source-lock.json
source_lock_blob_sha=e3cb3c18a5cf9c9cbee3e9dd834c439924dbd3d7
independent_verifier=stages/stage31/31-01/verify_stage31.py
independent_verifier_blob_sha=92b956d570367d145d87692ae25c0da5da312233
```

### Certificate / audit provenance

- `reconstruction-ledger.json` records every complete quartic-point branch and the exact family hypotheses.
- `verify_stage31.py` independently reconstructs the admissible source parameters and target predicates by exact integer arithmetic.
- `31-06/audit.md` accepts the exhaustive pullback but confines its conclusion to the exact thin prime family.

### DO_NOT_USE_FOR

```text
complete auxiliary points => source-family closure without a pullback dictionary
silently dropping signs, exceptional points, or degenerate branches
extending a branch dictionary to composite/other parameter families
using source-specific constants as universal reconstruction formulas
thin subfamily exclusion => parent parametric route/global endpoint closure
```

### Existing Arsenal relation / placement

- Related to older Arsenal reconstruction/dictionary recipes, but not duplicate of Stage14 divisor/column reconstruction: this card begins with a *complete auxiliary curve point set* and requires exhaustive branchwise pullback to the original Diophantine family.
- Formal `S30-WF03` remains the parent workflow for the final thin-family/endpoint credit boundary.

```text
FORMAL_ARSENAL=true
FORMAL_SELECTOR=false
PLACEMENT=ROUTER_ONLY
```

# 2. Formal workflow registration

## S31-WF01 — CAS Mordell--Weil proof-capability and full-group lock

**Weapon type / placement:** `WORKFLOW_CAS_MW_FULL_GROUP_CERTIFICATION` / `WORKFLOW`

This is a specialization of formal `S30-WF02 IMMUTABLE_LAYERED_CERTIFICATE_REPLAY`, not a second generic certificate framework. It adds the elliptic/Mordell--Weil-specific semantic distinction between computing a rank or subgroup and proving the full saturated Mordell--Weil group.

### Reusable procedure

```text
1. source-lock the exact elliptic model;
2. pin CAS vendor/version/routine and the routine's documentation semantics;
3. retain raw execution/artifact provenance and digest;
4. separately record rank proof, torsion, returned generators, and
   full-group/saturation proof status;
5. call the generators a full MW basis only when the documented
   full-group flag/certificate actually proves that claim;
6. exact-replay cheap group relations and point membership independently;
7. keep MW certification logically separate from integral-point completeness
   unless a separate integrality/completeness bridge makes it load-bearing.
```

### Hypotheses

- exact curve identity;
- proof-capable CAS routine with source/version semantics pinned;
- raw execution or immutable artifact provenance;
- explicit proof flags or certificate semantics distinguishing rank from full-group/saturation credit;
- independent exact replay for cheap relations where feasible.

### Applicability

- Mordell--Weil basis/rank/torsion certification used in elliptic Chabauty, integral-point, descent, or model-repair workflows;
- external papers/scripts that quote generators but do not prove saturation/full index;
- CAS-assisted proofs requiring hostile audit of what the routine's booleans actually mean.

### Source locks

```text
mw_certificate=stages/stage31/31-01/mordell-weil-certificate.json
mw_certificate_blob_sha=d1cd25c7b660caf06f2074ee7d9439d3bcf64ce5
execution_record=stages/stage31/31-01/magma-execution.json
execution_record_blob_sha=a7176f3e83dc2f6a82b06e41f6f78d8f15a35a12
source_lock=stages/stage31/31-01/source-lock.json
source_lock_blob_sha=e3cb3c18a5cf9c9cbee3e9dd834c439924dbd3d7
independent_verifier=stages/stage31/31-01/verify_stage31.py
independent_verifier_blob_sha=92b956d570367d145d87692ae25c0da5da312233
```

### Audit provenance

`31-06/audit.md` checked the documented Magma `MordellWeilGroup` boolean semantics and accepted the rank/full-group/saturation result specifically as an independent cross-check. The final audit also records that it is not load-bearing for the direct quartic completeness proof.

### DO_NOT_USE_FOR

```text
rank proved => returned subgroup is full Mordell-Weil group
generators found => saturation/full index proved
CAS output without pinned routine/version/documentation semantics
full MW group => complete quartic integral points without an integrality bridge
MW cross-check => duplicate independent proof probability
```

### Existing Arsenal relation

- **Specialization of `S30-WF02`, not duplicate.** Stage30 owns generic immutable source/artifact binding plus independent replay. `S31-WF01` adds the MW-specific proof-credit semantics for rank versus full-group/saturation.
- Generic CAS artifact/source-lock discipline should continue to route to `S30-WF02`; only the MW full-group semantic layer routes here.

# 3. Workflow integration without new IDs

## Thin-family closure firewall -> S30-WF03 specialization

Stage31 does not create a separate generic thin-family workflow. Its audited rule is a specialization of formal `S30-WF03 ADAPTER_CREDIT_LAYER_FIREWALL`:

```text
complete auxiliary curve
+ exhaustive source-family reconstruction
=> exact represented thin-family closure only
!= parent parametric route closure
!= global perfect-cuboid endpoint closure.
```

## CAS + independent exact replay -> S30-WF02 parent

The general pattern

```text
pin source/version/routine/artifact
+ independently replay cheap exact mathematics
+ state which CAS theorem/certificate supplies completeness
```

is already owned by formal `S30-WF02`. Stage31 adds only the MW-specific `S31-WF01` specialization and the mathematical cards above.

# 4. Stage31-specific / non-promoted material

The following remain provenance/examples and are not reusable weapons by themselves:

- the literal Stage31 quartic and elliptic coefficients;
- the concrete complete point lists on those two curves;
- `(p,q)=(11,71)` and the reconstructed edge triple;
- the concrete square/non-square numerical checks;
- the Paper-E Case-I/Case-II formulas as universal formulas outside their source-locked family;
- Magma run/job/artifact IDs as mathematical constants (they remain certificate provenance only);
- the fact that the prime Sophie--Germain subfamily is excluded;
- receiver/kernel names and post-Stage31 active-kernel counts.

# 5. Formal disposition and dedup boundary

```text
FORMAL_ROUTER_WEAPONS=S31-W01,S31-W02,S31-W03
FORMAL_WORKFLOWS=S31-WF01
FORMAL_SELECTOR_ADDITIONS=NONE
S30_WF02_PARENT_OF=S31-WF01_GENERIC_CERTIFICATE_LAYER
S30_WF03_PARENT_OF=STAGE31_INTEGRALITY_AND_THIN_FAMILY_CREDIT_FIREWALLS
STAGE31_SOURCE_MUTATED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

Final firewalls:

```text
birational equivalence != integral-point equivalence
finite/thin family closure != global endpoint closure
CAS output alone != independently locked proof surface
rank proved != full Mordell--Weil group proved
full MW group != quartic integral completeness without an integrality bridge
complete auxiliary point set != source-family closure without exact pullback
router-only adapter weapon != formal theorem/population selector
```
