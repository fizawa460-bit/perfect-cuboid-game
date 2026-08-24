# Stage33-02 hostile audit — BR0A integral Picard / saturation

## Verdict

```text
AUDITED_PR=1357
AUDITED_FUNCTIONAL_HEAD=bb66aa4e4c0852dfbb7d89c32471d3451feeeaec
AUDIT_VERDICT=PASS_AFTER_DIRECT_BOUNDARY_SOURCE_LOCK_AND_HANDOFF_REPAIR
UNIT_STATUS=CLOSED
BR0A=DISCHARGED
STAGE33_PROGRESS=2/11
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_RELEASED_UNITS=[33-03,33-04]
```

The mathematical production result is accepted without changing the computational algorithm. The audit repair is provenance/state-machine hardening only: the load-bearing Stage29 physical-boundary selector is now directly blob-locked, and the mandatory Stage33 machine handoff/controller closure state is materialized.

## Hostile recomputation

The audit did not treat green CI as proof. It downloaded the final functional-head Stage33-02 certificate and the locked Stage32 source artifact, then independently reconstructed the integral data.

Final functional-head evidence:

```text
workflow_run = 32686210328
workflow_conclusion = success
artifact_id = 9505735040
artifact_digest = sha256:75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87
certificate_sha256 = 2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1
```

Locked Stage32 source artifact independently rechecked:

```text
workflow_run = 32614857845
artifact_id = 9486641560
artifact_zip_sha256 = cae5c9b5aa00d9a730510c9f0e01ab609acef9d759fcc93f64708da123d6813d
picard_core_canonical_sha256 = de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870
upstream_commit = 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
upstream_blob = 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

The physical boundary selection was checked against the frozen Stage29 source itself:

```text
stages/stage29/29-02f/boundary_module_probe.m
blob = 315822987e98f9226c877d0ab8e76e1993160cd5
side_inds = [1..24]
exc_inds = [#Cs+j : j in [1..48]]
```

With `#Cs=92`, this is exactly upstream rows `1..24,93..140`, hence exactly 72 components.

## Independent integer-lattice verification

From the locked Stage32 `picard-core.json`, the audit rebuilt the 72x64 matrix `M` from those exact rows and independently verified:

```text
M.shape = 72 x 64
rank_Z/Q(M) = 58
rank ker_Z(M^T) = 14
Pic-rank - image-rank = 64 - 58 = 6
SNF nonzero diagonal = 56 copies of 1 followed by 2,2
saturation index = 4
Pic(Sbar)/im(Div_D) ~= Z^6 + Z/2 + Z/2
```

The supplied rank-14 kernel basis satisfies `K*M=0`, has rank 14, and its own Smith invariants are all 1, so it is a saturated integral kernel basis rather than merely a rational nullspace basis.

The supplied rank-58 saturated-image basis has Smith invariants all 1. Every boundary row has integral coordinates in that saturated basis. The exact index of the original image in the saturated hull is 4, agreeing with the two nontrivial Smith factors `2,2`.

The audit also independently reproduced all three exact matrices/hashes from the Stage32 source artifact:

```text
boundary_to_pic_matrix_sha256 = 12a944f20015b006441fdecb13442891812ad2cdde2046a890e63bc015d5f152
restriction_to_primitive_picard_basis_matrix_sha256 = 5e7765de76183a586b5696692de0490573e74796621d66358cb7ce8433dda1cc
boundary_intersection_matrix_sha256 = f91095ccfbeaf988f3e1998aaef20e9290d2c1ef028373dd373bb5c6a89a83e1
```

`M*G` equals the direct raw Magma pairings stored in the audited Stage32 artifact on all 72 selected rows. `M*G*M^T` is symmetric, with the first 24 side components of self-intersection `-4` and the 48 exceptional components of self-intersection `-2`.

## Closure-contract check

Stage33-02 has eight closure gates. After this hostile audit:

```text
EXACT_DIVISOR_LATTICE_CERTIFIED=true
INTEGRAL_SATURATION_CERTIFIED=true
INTERSECTION_MAPS_CERTIFIED=true
RESTRICTION_MAPS_REQUIRED_DOWNSTREAM_CERTIFIED=true
REPRODUCIBLE_CAS_MANIFEST=true
BR0A=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

Therefore all `8/8` criteria are satisfied and the unit may transition from `AUDIT_REQUIRED` to `CLOSED`.

## Audit repairs

Two closure-record defects were found; neither changes the mathematical result.

1. `cross-stage-picard-adapter.md` referred to the frozen Stage29 BR0A selector but did not directly pin its repository blob. The audit added the exact lock `stages/stage29/29-02f/boundary_module_probe.m @ 315822987e98f9226c877d0ab8e76e1993160cd5`.
2. The mandatory Stage33 machine handoff/controller transition for 33-02 had not yet been materialized. The audit adds `handoff.json`, `audit-state.json`, and advances the controller only after accepting all closure gates.

## Scope firewall

BR0A closure means only that the exact boundary-divisor/Picard integral lattice package required by downstream Stage33 units is complete. It does not compute `BR0B`, `BR0G`, any Q-defined Brauer class, any local evaluation, or any Brauer--Manin obstruction.

```text
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
ROUTE_COLOR_CHANGE_AUTHORIZED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The Stage33 frozen scope continues to retain possible all-primary open-algebraic BR0B terms, including odd-primary unit/character terms until Stage33-03 decides them exactly.
