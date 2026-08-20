# Stage27-20-r305a — separation test against the exact T collision

```text
TASK_ID=Stage27-20-r305a
PARENT_ROUTE=Stage27-20-r305
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The canonical r303b collision receiver requires simultaneous equality of

1. the ordinary Gaussian modulus `d`;
2. the invertible residue `beta mod d`;
3. the angular sector and endpoint/radial decorations;
4. the retained Stage14 physical masks.

This is a fiber-equality condition for the full physical target map `pi(p)`, not a bilinear form whose coefficients have already been separated into independent ideal variables.

No audited Stage27-20 identity presently rewrites the exact indicator

\[
1_{\pi(p)=\pi(p')}
\]

as a `B^{o(1)}`-rank sum of one-variable coefficient products while retaining the physical masks. Therefore the hypotheses of `SR-STR-161` and `SR-STR-165` are not currently met.

The correct missing adapter is now explicit:

`TPhysicalTargetClassLowRankSeparationAdapter`:
produce an exact or `B^{o(1)}`-loss decomposition of the physical target-fiber collision into `B^{o(1)}` separated quadratic/Jacobi or Gaussian-Hecke blocks.

Without that adapter, applying a large sieve to an ambient completion would change the measure and does not discharge r303.

```text
R305_SEPARATION_TEST_EXECUTED=true
EXACT_TARGET_COLLISION_MULTI_COMPONENT=true
LOW_RANK_SEPARATION_ADAPTER_PROVED=false
SR_STR_161_DIRECTLY_APPLICABLE=false
SR_STR_165_DIRECTLY_APPLICABLE=false
R305_STATE=THEOREM_ADAPTER_GATE_PAUSED
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_ROADMAP_ACTION=SEARCH_NEW_STAGE27_20_RECEIVER
```
