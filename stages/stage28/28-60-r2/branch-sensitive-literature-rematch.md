# Stage28-60-r2 — bounded branch-sensitive literature rematch

```text
ROUTE=R20_BRANCH_SENSITIVE_LITERATURE_REMATCH
STATUS=NO_DIRECT_DISCHARGE_FOUND_IN_BOUNDED_REMATCH
RECEIVER=relative interaction threshold at (log B)^(-2)
```

Checkpoint40-r2 localized the first certified geometric difference between the two completion covers to their branch profiles on the same toric base:

```text
space cover:       4 genus-0 branch components
third-face cover:  2 genus-1 branch components
```

Checkpoint60-r2 now sharpens the required counting consequence.  It is enough to determine whether

\[
\mathcal J_{28}=\mathcal I_{face}/\mathcal I_{sp}
\]

lies below, at, or above `(log B)^(-2)` under the exact physical height `R<=B`.

A bounded literature rematch checked theorem species closest to this receiver.

## Huang toric Hilbert irreducibility / thin-cover counting

Huang, arXiv:2111.01509 (v3), supplies the effective toric equidistribution, Selberg/geometric-sieve and generically-finite-cover machinery already adapted at checkpoint40.  For the two present degree-two covers it gives the same generic `eta<1/46` thin-cover range.  The theorem is deliberately insensitive to the branch-profile distinction at the strength currently used, so it does not compare `J_28` with `(log B)^(-2)`.

## Kummer counting results

Malmendier--Sung, arXiv:1901.11151, count rational points on a special two-parameter family of Kummer surfaces using elliptic fibrations and obtain Manin-type counting identities.  This confirms that cover/fibration-specific counting can in principle distinguish arithmetic geometry beyond generic thinness.  It does not provide a theorem comparing the present two fixed quadratic covers on `Y=Bl_4(P1xP1)` under the repo's physical big-and-nef Euclidean height, and therefore does not discharge the Stage28 receiver.

## Degree-two K3 rational-point infinitude

Martinez-Marin, arXiv:2505.13262, concerns rational points on degree-two K3 surfaces, including infinitude after controlled field extension and explicit families over `Q`.  It is not a bounded-height asymptotic comparison theorem between two branch profiles and does not supply the required marginal ratio.

## Bounded-rematch verdict

No theorem found in this bounded rematch has all of the following simultaneously:

1. the exact common toric base or a proved adapter to it;
2. sensitivity to the `4 x genus0` versus `2 x genus1` branch decomposition;
3. the exact physical `R<=B` height or a two-sided uniform height adapter;
4. a relative rational-lift count for the two marginals;
5. strength sufficient to place `J_28` relative to `(log B)^(-2)`;
6. no use of the perfect-cuboid joint endpoint count.

This is not a claim that no such theorem exists in the literature.  It records only that the bounded targeted rematch did not locate one.

The external receiver can now be stated more sharply as

```text
OPEN_GATE_60_R2=RelativeInteractionCurvatureThresholdFromDistinctBranchProfiles
BASE=Y=Bl_4(P1xP1)
COVER_1=Stage19 degree-two space cover; branch profile 4x genus0
COVER_2=Stage20 degree-two third-face cover; branch profile 2x genus1
HEIGHT=physical Euclidean R<=B
TARGET_QUANTITY=J_28=I_face/I_sp
CRITICAL_SCALE=(log B)^(-2)
SUFFICIENT_OUTPUT=prove J_28=o(log^-2), J_28~lambda log^-2, or J_28/log^-2->infinity; weaker one-sided bounds that resolve M3/N2 ordering are also acceptable
ENDPOINT_COUNT_FORBIDDEN=true
```

```text
RESEARCH_REQUEST_READY=true
UNBOUNDED_LITERATURE_PROGRAM_PERFORMED=false
DIRECT_DISCHARGE_FOUND=false
AUDIT_REQUIRED=true
```