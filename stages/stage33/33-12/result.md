# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_BREADTH_AUDIT_REQUIRED_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed receiver

`T(Kc) ~= <4> direct_sum <8>` with Gram `diag(4,8)`, and

```text
Br(Kc)[2] = Hom(T,Z/2) = (1/2 T*)/T*
beta1=t1/8 -> [1,0]
beta2=t2/16 -> [0,1]
```

The named nonzero J2 class is still one of `[1,0]`, `[0,1]`, `[1,1]`. Kernel-lattice fingerprints remain comparison infrastructure only:

```text
[1,0] -> min norm 8
[0,1] -> min norm 4
[1,1] -> min norm 12
```

## Independent named-J2 datum retained

For the normalization `C: z^2=t^4-6t^2+1`, the explicit degree-two map

```text
X=t^2, Y=t z,
E': Y^2=X(X^2-6X+1)
```

sends the named divisor to

```text
phi_*(E_J2)=(0,0) in E'[2].
```

Certificate: `j2-normalization-2isogeny-rational-torsion.json`, SHA256 `81097b3eab3b9f17de5a802b88324c74a7ab80e09c70dc179d4c5af4abd04571`.

## Route ledger

```text
BRANCH_COHOMOLOGICAL_MAP                   EQUIVALENT / ARCHIVED
KERNEL_LATTICE_FINGERPRINT                LIVE / COMPARISON ONLY
NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR       REJECTED_EXACTLY
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION   BLOCKED / MISSING TRANSCENDENTAL CYCLE MARKING
GOOD_REDUCTION_ETALE_SPECIALIZATION       EQUIVALENT-BLOCKED / SAME MARKING INTERFACE
K3_LEVEL_SHIODA_INOSE_CORRESPONDENCE       UNTESTED
```

The naive Shioda-Mitani shortcut is exactly rejected because the J2 quotient has CM field `Q(i)` whereas the canonical Shioda-Mitani elliptic factors for `diag(4,8)` have CM field `Q(sqrt(-2))`.

The direct B-field route is exactly blocked at the retained interface because `t1,t2` are only an abstract isometry basis and `transcendental_marking_materialized=false`; no explicit H2 cycles or CSA-to-cycle pairing adapter are materialized.

## NEW: good-reduction / etale specialization audit

Proper smooth base change can transport prime-to-p etale H2 and the geometric 2-primary cohomological data at a good prime, but it does not itself choose a marked identification of the abstract `t1,t2` with special-fiber cycles. The retained Stage33-12 state has neither an explicit certified good integral Kc model plus marked specialization basis nor a named-J2 coordinate in that basis.

Moreover, evaluating a Brauer class at an `F_q`-rational point lands in `Br(F_q)=0`, so finite-field rational-point evaluation does not directly return either marked `Hom(T,Z/2)` bit.

Therefore the current good-reduction route does not reduce the candidates:

```text
GOOD_REDUCTION_ETALE_SPECIALIZATION=EQUIVALENT_BLOCKED_BY_SAME_MARKING_INTERFACE
CANDIDATES_BEFORE=3
CANDIDATES_AFTER=3
NEW_J2_INDEPENDENT_OBSERVATION=false
```

Certificate: `j2-good-reduction-etale-specialization-route-audit.json`.
Canonical SHA256: `501918bd0ce53060bb0d61a2a4e8985833f5eb57d27a03af53b81251ab5f3399`.
Network-free verifier: `certify_j2_good_reduction_etale_specialization_route_audit.py`.

## Cycle/Loop Guard state

Three materially distinct routes since the last breadth audit have now been rejected/blocked without selecting the marked J2 functional. Under `cycle-exploration-safety-protocol.md`, ordinary same-route MAIN must stop here and broaden before another route is selected.

```text
LOOP_ACTIVE_RECEIVER=named CV J2 -> Br(Kc)[2]=Hom(T,Z/2)
LOOP_CANDIDATE_COUNT=3
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=true
LOOP_BLIND_REDISCOVERY_REQUIRED=true
CYCLE_ROUTE_STATUS=BLOCKED_NO_NEW_INFORMATION
CYCLE_LIVE_CANDIDATES=1
CYCLE_UNTESTED_CANDIDATES=1
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=false
```

Next exact leaf:

`RUN_EXHAUSTIVE_VIEW_AUDIT_PLUS_BLIND_REDISCOVERY_ON_THE_FIXED_NAMED_J2_TO_MARKED_BR_KC_2_RECEIVER; CLASSIFY_ALL_GENERATED_VIEWS_BEFORE_SELECTING_THE_NEXT_ACTIVE_ROUTE`.

## Visible progress / firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
