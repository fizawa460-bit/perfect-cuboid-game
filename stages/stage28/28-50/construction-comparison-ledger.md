# Stage28-50 — construction comparison ledger

```text
CHECKPOINT=50
ROLE=STRONGEST_CERTIFIED_LOWER_BOUND_AND_CONSTRUCTION_LEDGER
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## L1. Stage19 source construction: quarter-power floor

The current audited Stage19 lower interface comes from the Stage25 directional R501/R502 families and their post-Stage25 supersession.  The strongest global statement is

\[
N_2(B)\gg B^{1/4},
\]

and each canonical shared-edge direction also has a quarter-power family.

The later Stage27 lower reentry audited the known R501/R502 mechanism more sharply: each known saturated family has two-dimensional parameter count `kappa=2`, physical height exponent `h=8`, bounded primitive gcd/parameter multiplicity, and only finite exactly-three-face exceptions.  Thus these known families genuinely live at

\[
B^{\kappa/h}=B^{1/4}
\]

and cannot be upgraded merely by re-estimating their old fibers.

```text
SOURCE_KNOWN_CONSTRUCTION_EXPONENT=1/4
SOURCE_KNOWN_PARAMETER_DIMENSION=2
SOURCE_KNOWN_HEIGHT_EXPONENT=8
SOURCE_KNOWN_FAMILY_SATURATED_AT_ONE_QUARTER=true
SOURCE_TRUE_EXPONENT_IDENTIFIED=false
```

## L2. Stage20 target construction: generalized Saunderson

Stage26 proved a two-parameter generalized Saunderson family with parameter count `>>T^2` and height `R<72T^6`.  The prior proof used a divisor-size output fiber and therefore recorded

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}.
\]

Stage28-50 L1 observes that the output itself identifies the candidate cube face `w^3` and its opposite edge `4uvw`.  This reduces the fiber to at most three and yields the fresh candidate theorem

\[
\boxed{M_3(B)\gg B^{1/3}.}
\]

```text
TARGET_KNOWN_CONSTRUCTION_PARAMETER_DIMENSION=2
TARGET_KNOWN_HEIGHT_EXPONENT=6
TARGET_SAFE_GLOBAL_FIBER_BOUND_CANDIDATE=3
TARGET_CONSTRUCTION_EXPONENT_CANDIDATE=1/3
TARGET_TRUE_EXPONENT_IDENTIFIED=false
```

## L3. What the construction exponents do and do not compare

At the level of explicit audited/candidate construction mechanisms, the target construction is more height-efficient:

\[
2/6=1/3>1/4=2/8.
\]

For any fixed saturated Stage19 quarter-power family `F_19(B)` and the distinct-output generalized Saunderson family `F_20(B)`, the construction counts therefore satisfy, after audit of L1,

\[
F_{20}(B)\gg B^{1/3},
\qquad
F_{19}(B)=\Theta(B^{1/4}),
\]

so

\[
\frac{F_{20}(B)}{F_{19}(B)}\gg B^{1/12}.
\]

This is a comparison of selected explicit construction families, not of the full populations.  In particular it does **not** imply `M3(B)>N2(B)` asymptotically because `N2` may contain many points outside the known quarter-power families.

```text
KNOWN_CONSTRUCTION_EFFICIENCY_TARGET_GT_SOURCE=true
CONSTRUCTION_FAMILY_RATIO_EXPONENT=1/12
FULL_POPULATION_ORDERING_FROM_CONSTRUCTION_FLOORS=false
M3_OVER_N2_ORDERING_RESOLVED=false
```

## L4. Bridge lower ratio consequence

Combining the epsilon-free candidate target floor with the current Stage19 upper

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]

gives, for every fixed `epsilon>0`,

\[
\frac{M_3(B)}{N_2(B)}\gg_\varepsilon B^{-1/6-\varepsilon}.
\]

This has the same endpoint-free exponent corridor already recorded at checkpoint30; the new target theorem removes an epsilon loss from the numerator but the Stage19 upper still prevents an epsilon-free `B^{-1/6}` bridge lower.

```text
BRIDGE_LOWER_ENDPOINT_EXPONENT_IMPROVED=false
NUMERATOR_EPSILON_LOSS_REMOVED_CANDIDATE=true
EPSILON_FREE_BRIDGE_B_MINUS_ONE_SIXTH_PROVED=false
```

## L5. Construction-transfer firewall

The two stage populations are disjoint exact-face strata.  A Stage19 object cannot be turned into Stage20 merely by adding a third integral face while preserving the Stage19 definition: doing so leaves the exactly-two stratum, and if its space diagonal remains integral the result is the deferred perfect-cuboid endpoint.

Likewise imposing integral space diagonal on a Stage20 Euler cuboid is exactly the deferred endpoint, not a Stage19 construction.

Therefore neither lower family may be transferred across the bridge by imposing the other completion condition and then counted as a Stage28 source/target family.

```text
SAUNDERSON_PLUS_SPACE_IS_DEFERRED_ENDPOINT=true
STAGE19_FAMILY_PLUS_THIRD_FACE_IS_DEFERRED_ENDPOINT=true
DIRECT_LOWER_FAMILY_TRANSFER_LEGAL=false
ENDPOINT_COUNT_USED=false
```

## L6. Remaining lower-side question

After the bounded-fiber repair, the strongest known explicit target construction has exponent `1/3`, while the strongest known explicit source construction has exponent `1/4`.  Neither is proved optimal.

A genuine further checkpoint50 improvement requires one of:

- an `M3` construction with parameter/height efficiency `kappa/h>1/3` and controlled physical fibers;
- an `N2` construction with `kappa/h>1/4` (which would narrow or reverse the construction-efficiency gap);
- a direct lower comparison of the two marginals on the same physical host that does not count their perfect-cuboid intersection.

```text
OPEN_GATE_50=HigherEfficiencyPhysicalConstructionOrDirectMarginalLowerComparison
M3_CONSTRUCTION_PROGRESS_GATE=kappa/h>1/3
N2_CONSTRUCTION_PROGRESS_GATE=kappa/h>1/4
ENDPOINT_COUNT_FORBIDDEN=true
```
