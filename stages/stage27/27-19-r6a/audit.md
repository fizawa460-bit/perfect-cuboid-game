# Stage27-19-r6a hostile audit

```text
AUDIT_ID=STAGE27-19-R6A-AUDIT-R01
AUDITED_PR=1249
AUDITED_TASK=Stage27-19-r6a
AUDITED_SUBMISSION_HEAD=10c85b46290f078cfe1bb55f3bf4459e0b3311bb
BASE_MAIN=f5c40a048bb6a56e689ed2dc37358ffed16db99f
AUDIT_VERDICT=PASS
REPAIR_REQUIRED=false
AUDIT_REPAIR_PERFORMED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_MU=1/2
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
SUBMITTED_HEAD_STAGE27_19_R6A_CI=PASS
SUBMITTED_HEAD_STAGE27_19_R6A_CI_RUN=32347513983
NEXT_DERIVED_ROUTE_AFTER_MERGE=27-19-r6b
NEXT_TARGET=OCCUPIED_R_SQUARECLASS_COLLISION_SIEVE_WITH_PHYSICAL_MASKS
```

## Independent mathematical audit

### 1. Population and distinctness

Stage19 counts primitive canonical triples with strict ordering `0<a<b<c`. Hence the three physical edges are pairwise distinct. For an exactly-two object, the two successful faces have a unique shared edge `e`; the other edges `x,y` satisfy `x!=y`. Therefore the two positive norm-`R^2` representations used in r6a are genuinely distinct. No hidden equal-edge branch is omitted.

```text
STAGE19_POPULATION_MATCH_AUDIT=PASS
STRICT_CANONICAL_DISTINCTNESS_AUDIT=PASS
TWO_GAUSSIAN_REPRESENTATIONS_DISTINCT_AUDIT=PASS
```

### 2. Norm receiver and product identity

From

`e^2+x^2=A^2`, `e^2+y^2=B^2`, `e^2+x^2+y^2=R^2`,

one gets

`A^2+y^2=R^2`, `B^2+x^2=R^2`.

With `P=AB-xy`, `Q=AB+xy`, direct expansion gives

`PQ=A^2B^2-x^2y^2=(e^2+x^2)(e^2+y^2)-x^2y^2=e^2R^2=(eR)^2`.

Equivalently, using the two norm equations directly,

`PQ=R^2(A^2-x^2)`.

On a physical survivor `Q>0` and `PQ>0`, hence `P>0`.

```text
NORM_R2_RECEIVER_AUDIT=PASS
PQ_IDENTITY_AUDIT=PASS
P_POSITIVITY_AUDIT=PASS
```

### 3. Converse reconstruction

Assume positive `(A,y),(B,x)` satisfy the common norm equation, `A>x`, and `PQ` is a square. Since `PQ=R^2(A^2-x^2)`, the positive integer `A^2-x^2` has rational square root. A rational square root of an integer is integral, so `A^2-x^2=e^2` for an integer `e>0`. Equality of the two norm equations then gives `B^2-y^2=e^2`.

After reimposing the original primitive/canonical mask and `x^2+y^2` nonsquare mask, this reconstructs exactly the Stage19 physical object. The converse is not asserted without those masks.

```text
CONVERSE_RECONSTRUCTION_AUDIT=PASS_WITH_ORIGINAL_MASKS
NAKED_GAUSSIAN_PAIR_BIJECTION_CLAIMED=false
```

### 4. Squarefree-kernel collision

For positive integers `P,Q`, `PQ` is a square iff the parity vectors of all prime valuations agree. Thus there is a unique positive squarefree `d` with

`P=d*u^2`, `Q=d*v^2`.

Adding/subtracting yields

`AB=d(u^2+v^2)/2`, `xy=d(v^2-u^2)/2`,

and positivity gives `eR=d*u*v` from `PQ=(eR)^2`.

```text
SQUAREFREE_KERNEL_COLLISION_AUDIT=PASS
COLLISION_PARAMETERIZATION_AUDIT=PASS
```

### 5. Exact witness

For `(R,e,x,y,A,B)=(1073,840,448,495,952,975)`, independent integer substitution confirms

`P=706440=210*58^2`, `Q=1149960=210*74^2`, and `eR=210*58*74`.

```text
EXACT_WITNESS_AUDIT=PASS
```

### 6. Representation-multiplicity no-go

For every `m>=1`, `R=25m` has the two distinct positive representations

`R^2=(24m)^2+(7m)^2=(20m)^2+(15m)^2`.

Thus the condition “at least two positive representations of `R^2`” alone holds on at least `floor(B/25)` integers `R<=B`; it cannot itself imply a fixed-power sparse support bound. The submitted verifier also confirms that the two displayed base representations do not themselves satisfy the squarefree-kernel collision, so the collision is genuinely stronger than multiplicity alone.

```text
TWO_REPRESENTATION_POSITIVE_DENSITY_NO_GO_AUDIT=PASS
SQUARECLASS_COLLISION_STRICTLY_STRONGER_WITNESS_AUDIT=PASS
```

### 7. Fixed-R multiplicity and counting dimension

The standard bound `r_2(R^2)<=4*tau(R^2)=R^o(1)` implies only `R^o(1)` ordered positive representations and hence `R^o(1)` ordered representation pairs at fixed `R`. This does not create a new power loss. The unresolved theorem is therefore correctly placed on the number of occupied physical space diagonals `R`, with the squareclass collision and physical masks retained.

```text
FIXED_R_CANDIDATE_PAIR_SUBPOWER_AUDIT=PASS
COUNTING_DIMENSION_AUDIT=PASS_OCCUPIED_R_SUPPORT
```

## Lifecycle / anti-loop audit

The r5 factor-packet lane remains frozen; r6a is a different support-level redirect and does not reopen SR-STR-224 or claim a generic literature theorem. The monolithic `stages/stage27/27-controller.json` contains concurrent Stage27-20 history and stale Stage19 lifecycle fields. Replacing it wholesale in this audit would risk erasing unrelated state. Therefore the submitted `controller-sync-delta.json` strategy is accepted: the delta is audited and promoted, but the full controller must be reconciled from a fresh main read after this PR is merged.

```text
R5_UPPER_FACTOR_PACKET_LANE_FROZEN_AUDIT=PASS
ANTI_LOOP_FIREWALL_AUDIT=PASS
MONOLITHIC_CONTROLLER_WHOLESALE_REPLACEMENT_PERFORMED=false
CONTROLLER_SYNC_DELTA_AUDITED=true
CONTROLLER_SYNC_DELTA_APPLY_AFTER_MERGE=true
```

## CI

On the exact submitted head, dedicated workflow `Stage27-19-r6a occupied-R support` run `32347513983` completed successfully. Its verifier, route-JSON validation, and diff check all passed.

```text
SUBMITTED_HEAD_STAGE27_19_R6A_CI=PASS
SUBMITTED_HEAD_STAGE27_19_R6A_CI_RUN=32347513983
```

No fixed-power support deficit has been proved. In particular this audit does not advance checkpoint 50 and does not identify a new `mu<1/2` or the true Stage19 exponent.
